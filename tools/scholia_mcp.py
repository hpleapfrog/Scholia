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
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.json"
CITATIONS = ROOT / "citations.json"
EVIDENCE = ROOT / "evidence.json"
PROTOCOL = "2024-11-05"


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
        "description": "按关键词搜索知识对象（标题/id/学科）。/ Search objects by keyword.",
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
        "name": "scholia_get_object",
        "description": "取某个对象的完整 Markdown（给 id 或 path）。/ Get an object's full markdown.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {"type": "string", "description": "如 kb:med:prop-osa-pap-titration"},
                "path": {"type": "string", "description": "仓库内路径"},
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
        "name": "scholia_rules",
        "description": "列出规则注册表（机械校验 / 人工复核）。/ List the rule registry.",
        "inputSchema": {"type": "object", "properties": {}},
    },
]


def _brief(o):
    """检索结果只回**导航字段**。

    `来源` / `适用` / `条件` 曾经也塞在这里：一次默认 20 条的搜索要 6k tokens，
    **比读一条正文还贵**。要引用时用 `scholia_cite` 取那一条（约 160 tokens）。
    """
    return {
        "id": o["id"], "type": o["type"], "title": o["title"], "status": o["status"],
        "path": o["path"], "path_en": o.get("path_en"),
        "学科": o.get("学科", ""),
        "可作事实引用": o.get("可作事实引用", True),
    }


def tool_call(name, args):
    idx = load_index()
    objs = idx.get("objects", [])

    if name == "scholia_stats":
        return idx.get("统计", {})

    if name == "scholia_search":
        q = str(args.get("query", "")).lower()
        typ = args.get("type")
        limit = int(args.get("limit", 5))
        hits = []
        for o in objs:
            if typ and o["type"] != typ:
                continue
            hay = " ".join([o.get("title", ""), o["id"], o.get("学科", ""), o.get("path", "")]).lower()
            if q in hay:
                hits.append(_brief(o))
        return {"count": len(hits), "results": hits[:limit]}

    if name == "scholia_list":
        typ, subj, st = args.get("type"), args.get("subject"), args.get("status")
        limit = int(args.get("limit", 100))
        hits = [o for o in objs
                if (not typ or o["type"] == typ)
                and (not subj or subj in o.get("学科", ""))
                and (not st or o["status"] == st)]
        return {"count": len(hits), "results": [_brief(o) for o in hits[:limit]]}

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
        return {"meta": _brief(target), "markdown": p.read_text(encoding="utf-8")}

    if name == "scholia_cite":
        oid = args.get("id", "")
        entry = load_citations().get(oid)
        return entry or {"error": "not found", "id": oid}

    if name == "scholia_get_evidence":
        ev = args.get("id", "")
        entry = load_evidence().get(ev)
        return entry or {"error": "not found", "id": ev}

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


if __name__ == "__main__":
    main()
