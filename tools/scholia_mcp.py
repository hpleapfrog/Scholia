#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scholia MCP server —— 让 agent 直接查这个知识库（零依赖、只读、不联网）。

用法（在 agent 的 MCP 配置里）：

    {
      "mcpServers": {
        "scholia": { "command": "python", "args": ["tools/scholia_mcp.py"] }
      }
    }

也可以手动跑来自检：

    echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' | python tools/scholia_mcp.py

传输：stdio，**换行分隔的 JSON-RPC 2.0**（MCP 规范）。
数据：只读三份生成物与各 `.md` 文件——不写、不改、不联网。

**三份文件各管一件事，别整读**：
`index.json`（导航 + 能不能引用）· `citations.json`（按 id 取引用材料）· `evidence.json`（证据登记）。
`scholia_search` 只回导航字段；要引用时再取 `scholia_cite`。

**English:** Zero-dependency, read-only MCP server (stdio, newline-delimited
JSON-RPC). Exposes the knowledge base as tools; reads only `index.json` and the
`.md` files. No writes, no network.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.json"
CITATIONS = ROOT / "citations.json"
EVIDENCE = ROOT / "evidence.json"
PROTOCOL = "2024-11-05"

# 缺口清单与 `docs/GAPS.md`、`make_tasks.py` **共用同一个 compute()**。
# 各算各的迟早会出现「页面说 37、工具说 35」，而这种矛盾没有任何检查会发现。
sys.path.insert(0, str(Path(__file__).resolve().parent))
import gaps  # noqa: E402  同目录、只读、零依赖


def _load(path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_index():
    return _load(INDEX)


def load_citations():
    return _load(CITATIONS).get("by_id", {})


def load_evidence():
    return _load(EVIDENCE).get("entries", {})


TOOLS = [
    {
        "name": "scholia_stats",
        "description": "库的统计（对象数 / 按类型 / 按学科 / 证据数）。/ Library statistics.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "scholia_search",
        "description": "按关键词搜索知识对象（标题 / 英文标题 / id / 学科 / 路径）。"
                       "多个词按 AND 匹配，结果按相关度排序（标题精确 > 开头 > 包含 > id）。"
                       " / Search objects; terms are ANDed and ranked by title relevance.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "关键词 / keyword"},
                "type": {"type": "string", "description": "可选：知识点/命题/教法/误解/路径/资源"},
                "limit": {"type": "integer", "description": "默认 20"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "scholia_list",
        "description": "列出对象，可按 type / 学科 / status 过滤。/ List objects with filters.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "type": {"type": "string"},
                "subject": {"type": "string", "description": "学科，如 物理"},
                "status": {"type": "string"},
                "limit": {"type": "integer"},
            },
        },
    },
    {
        "name": "scholia_external_prereqs",
        "description": "查「库外前置」：条目声明需要、但本库**没有节点**的前置。"
                       "可按稳定标识聚合（看它被几个条目需要，是否该建节点），或按对象 id 列出。"
                       "/ Query out-of-library prerequisites.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "key": {"type": "string", "description": "稳定标识，如 angle / vector"},
                "id": {"type": "string", "description": "对象 id，如 kb:physics:kp-refraction"},
            },
        },
    },
    {
        "name": "scholia_get_object",
        "description": "取一条条目的 Markdown。`part=\"content\"`（默认）只给**学习者半**"
                       "（读完你会什么 · 定义/陈述/做法 · 关联 · 禁忌/风险），约 460 tokens；"
                       "要判断这条论证是否成立时才用 `part=\"full\"`（约 1125）。"
                       "/ Get an entry. Default returns only the reader-facing half.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {"type": "string", "description": "如 kb:med:prop-osa-pap-titration"},
                "path": {"type": "string", "description": "仓库内路径"},
                "part": {"type": "string", "enum": ["content", "full"],
                         "description": "content（默认，学习者半）| full（连论证与变更记录）"},
            },
        },
    },
    {
        "name": "scholia_cite",
        "description": "取某条对象的**引用材料**：来源（已解析的定位）/ 证据编号 / 适用 / 条件 / 免责块位置 / 引用须写明。"
                       "引用一条之前取这一条即可，不要整读 citations.json。/ Citation kit for one entry.",
        "inputSchema": {
            "type": "object",
            "properties": {"id": {"type": "string", "description": "如 kb:physics:prop-centripetal-is-not-a-new-force"}},
            "required": ["id"],
        },
    },
    {
        "name": "scholia_get_evidence",
        "description": "取某条证据（类别 / 等级 / 核验深度 / 定位 / 许可）。/ Get one evidence entry.",
        "inputSchema": {
            "type": "object",
            "properties": {"id": {"type": "string", "description": "如 ev-049"}},
            "required": ["id"],
        },
    },
    {
        "name": "scholia_gaps",
        "description": "查「这个库还缺什么」：复核 / 复核前置 / 缺教法 / 库外前置 / 单环节覆盖 / 待补 / 覆盖度。"
                       "只列机器数得出来的缺口，与 `docs/GAPS.md` 同源。"
                       "/ Machine-countable gaps, same source as docs/GAPS.md.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "group": {"type": "string",
                          "description": "可选：review / translate / methods / external / "
                                         "path-thin / path-shallow / todo / coverage"},
                "limit": {"type": "integer", "description": "每组最多列几条（默认 5，0=只给数量）"},
            },
        },
    },
    {
        "name": "scholia_rules",
        "description": "列出规则注册表（机械校验 / 人工复核）。/ List the rule registry.",
        "inputSchema": {"type": "object", "properties": {}},
    },
]


def _search_rank(o, terms):
    """相关度：**标题精确 = 0**，标题开头 = 1，标题包含 = 2，id 命中 = 3，其余 = 4。

    没有排序时，`electric field` 的第一条是「带电粒子在电场中的运动」——
    那条标题更长、只是**恰好先出现在索引里**。检索的第一条应该是**你叫得出名字的那条**。
    """
    q = " ".join(terms)
    title = (o.get("title") or "").lower()
    title_en = (o.get("title_en") or "").lower()
    if title == q or title_en == q:
        return 0
    if title.startswith(q) or title_en.startswith(q):
        return 1
    if all(t in title for t in terms) or all(t in title_en for t in terms):
        return 2
    if all(t in o["id"].lower() for t in terms):
        return 3
    return 4


def _brief(o):
    """检索结果只回**导航字段**。

    `来源` / `适用` / `条件` 曾经也塞在这里：一次默认 20 条的搜索要 6k tokens，
    **比读一条正文还贵**。要引用时用 `scholia_cite` 取那一条（约 160 tokens）。

    `外部先修` 只回**稳定标识**（不回名称/来源）：它是「本库没有这个节点」的信号，
    几个字符就能让 agent 知道该不该继续查。
    """
    brief = {
        "id": o["id"], "type": o["type"], "title": o["title"], "status": o["status"],
        "path": o["path"], "path_en": o.get("path_en"),
        "学科": o.get("学科", ""),
        "可作事实引用": o.get("可作事实引用", True),
    }
    # 英文标题：英文读者要能用英文认出这条。没有译本时不存在这个字段。
    if o.get("title_en"):
        brief["title_en"] = o["title_en"]
    ext = o.get("外部先修") or []
    if ext:
        brief["外部先修"] = [e["标识"] for e in ext]
        # 聚合提示：同一个标识出现>=2个对象时建议用 scholia_external_prereqs 聚合
        brief["外部先修提示"] = ["用 scholia_external_prereqs(key=...) 聚合查看「库外前置」是否该建节点（跨条目复用时最省）"]
    return brief


# 复核者半的小节。FORMAT §0：每个条目分成两半——前半给学习者，后半给复核者。
_REVIEW_SECTIONS = ("依据", "证据", "论证", "变更记录", "变更记录 ")


def _content_half(md):
    """截到第一个「复核者半」小节之前。

    这不是摘要，是**原文的一部分**：本库的条目本来就分成两半
    （前半答「它是什么」，后半答「我凭什么这么说」）。回答「这条讲什么」只要前半，
    平均 461 tokens，比全文 1125 省 59%——而且不会像自动摘要那样把片段说成结论。
    """
    cut = len(md)
    for sec in _REVIEW_SECTIONS:
        i = md.find("\n## " + sec)
        if 0 < i < cut:
            cut = i
    return md[:cut].rstrip() + "\n"


def tool_call(name, args):
    idx = load_index()
    objs = idx.get("objects", [])

    if name == "scholia_stats":
        return idx.get("统计", {})

    if name == "scholia_search":
        q = str(args.get("query", "")).strip().lower()
        terms = [t for t in re.split(r"\s+", q) if t]
        typ = args.get("type")
        limit = int(args.get("limit", 5))
        hits = []
        for o in objs:
            if typ and o["type"] != typ:
                continue
            ext_text = " ".join(
                f"{e.get('名称', '')} {e.get('标识', '')}"
                for e in (o.get("外部先修") or []))
            # 英文标题也进检索词：否则用英文搜「electric field」只能靠 id 碰运气。
            hay = " ".join([o.get("title", ""), o.get("title_en") or "", o["id"],
                            o.get("学科", ""), o.get("path", ""), ext_text]).lower()
            # 多个词按 AND 匹配（`field electric` 也能找到），再按标题相关度排序。
            if not terms or all(t in hay for t in terms):
                hits.append((_search_rank(o, terms), _brief(o)))
        hits.sort(key=lambda x: (x[0], len(x[1]["title"]), x[1]["id"]))
        return {"count": len(hits), "results": [b for _rank, b in hits[:limit]]}

    if name == "scholia_list":
        typ, subj, st = args.get("type"), args.get("subject"), args.get("status")
        limit = int(args.get("limit", 100))
        hits = [o for o in objs
                if (not typ or o["type"] == typ)
                and (not subj or subj in o.get("学科", ""))
                and (not st or o["status"] == st)]
        return {"count": len(hits), "results": [_brief(o) for o in hits[:limit]]}

    if name == "scholia_external_prereqs":
        oid = args.get("id")
        key = args.get("key") or args.get("标识")
        if oid:
            for o in objs:
                if o["id"] == oid:
                    return {"id": oid, "外部先修": o.get("外部先修") or []}
            return {"error": "not found", "id": oid}
        data = idx.get("外部先修") or {}
        if key:
            for group in data.get("按标识") or []:
                if group.get("标识") == key:
                    return group
            return {"error": "not found", "key": key}
        return data

    if name == "scholia_get_object":
        oid, path = args.get("id"), args.get("path")
        target = None
        for o in objs:
            if (oid and o["id"] == oid) or (path and o["path"] == path):
                target = o
                break
        if not target:
            return {"error": "not found", "id": oid, "path": path}
        p = ROOT / target["path"]
        if not p.exists():
            return {"error": "file missing", "path": target["path"]}
        md = p.read_text(encoding="utf-8")
        part = args.get("part", "content")
        if part == "full":
            return {"meta": _brief(target), "part": "full", "markdown": md}
        return {"meta": _brief(target), "part": "content",
                "markdown": _content_half(md),
                "note": "只给学习者半（定义/陈述/做法 + 关联/禁忌）。"
                        "要判断论证是否成立，用 part=\"full\"。"}

    if name == "scholia_cite":
        oid = args.get("id", "")
        entry = load_citations().get(oid)
        if not entry:
            return {"error": "not found", "id": oid}
        # 增强：为外部先修附加聚合提示，避免多次调用
        try:
            ext = entry.get("外部先修") or []
            if ext:
                idx = load_index()
                agg = idx.get("外部先修") or {}
                bykey = {}
                for g in (agg.get("按标识") or []):
                    k = g.get("标识")
                    if k:
                        bykey[k] = g
                hints = []
                for e in ext:
                    k = e.get("标识")
                    g = bykey.get(k)
                    if g and g.get("出现次数", 0) >= 2:
                        hints.append(f"外部先修 `{k}` 在 {g['出现次数']} 个对象中出现（跨条目复用）——用 scholia_external_prereqs(key='{k}') 判断是否该建节点")
                if hints:
                    entry = dict(entry)
                    entry["外部先修聚合提示"] = hints
        except Exception:
            pass
        return entry

    if name == "scholia_get_evidence":
        ev = args.get("id", "")
        entry = load_evidence().get(ev)
        return entry or {"error": "not found", "id": ev}

    if name == "scholia_gaps":
        data = gaps.compute(idx, load_citations(), load_evidence(), root=ROOT)
        grp = args.get("group")
        limit = int(args.get("limit", 5))
        if grp:
            g = data["分组"].get(grp)
            if not g:
                return {"error": "unknown group", "group": grp, "available": data["顺序"]}
            out = {k: v for k, v in g.items() if k != "条目"}
            out["条目"] = g["条目"][:limit] if limit else []
            if limit and g["数量"] > limit:
                out["还有"] = g["数量"] - limit
            return out
        # 默认只回数量：想知道「有多少」的调用不该付「列出 570 条」的钱。
        return {
            "统计": data["统计"],
            "缺口": [{"key": k,
                      "名称": data["分组"][k]["名称"],
                      "数量": data["分组"][k]["数量"],
                      "为什么": data["分组"][k]["为什么"]} for k in data["顺序"]],
            "提示": "加 group=<key> 看具体条目；完整清单用 `python tools/make_tasks.py --json`。"
                    "同一对象可能出现在多组，别把数量相加。",
        }

    if name == "scholia_rules":
        p = ROOT / "docs" / "RULES.md"
        return {"markdown": p.read_text(encoding="utf-8") if p.exists() else "RULES.md missing"}

    raise ValueError(f"unknown tool: {name}")


def handle(msg):
    method = msg.get("method")
    mid = msg.get("id")
    if method == "initialize":
        pv = (msg.get("params") or {}).get("protocolVersion") or PROTOCOL
        return {"jsonrpc": "2.0", "id": mid, "result": {
            "protocolVersion": pv,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "scholia", "version": "1.0.0"},
        }}
    if method == "ping":
        return {"jsonrpc": "2.0", "id": mid, "result": {}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": mid, "result": {"tools": TOOLS}}
    if method == "tools/call":
        params = msg.get("params") or {}
        name = params.get("name")
        args = params.get("arguments") or {}
        try:
            result = tool_call(name, args)
            text = json.dumps(result, ensure_ascii=False, indent=2)
        except Exception as e:  # noqa: BLE001
            text = f"error: {e}"
        return {"jsonrpc": "2.0", "id": mid, "result": {
            "content": [{"type": "text", "text": text}],
            "isError": False,
        }}
    if method in ("notifications/initialized", "notifications/cancelled"):
        return None
    if mid is None:
        return None
    return {"jsonrpc": "2.0", "id": mid,
            "error": {"code": -32601, "message": f"method not found: {method}"}}


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        resp = handle(msg)
        if resp is not None:
            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
            sys.stdout.flush()


def print_config():
    """`--print-config`：直接打出可粘贴的 MCP 配置（含绝对路径）。

    挂载 MCP 最常卡的一步是「配置里该写什么路径」。与其让人去猜，
    不如让脚本按**自己所在的位置**算出来——拷贝即用。
    """
    cfg = {"mcpServers": {"scholia": {
        "command": sys.executable,
        "args": [str(Path(__file__).resolve())],
    }}}
    print(json.dumps(cfg, ensure_ascii=False, indent=2))
    print()
    print("# 把上面这段加到 agent 的 MCP 配置里即可（settings → MCP）。")
    print("# command 用的是本机 " + "Python 解释器的绝对路径" + "，换机器后重跑本命令。")
    return 0


if __name__ == "__main__":
    if "--print-config" in sys.argv:
        sys.exit(print_config())
    main()
