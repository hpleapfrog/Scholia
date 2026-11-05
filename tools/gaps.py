#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""缺口清单：**一处**算清「这个库还缺什么」。

为什么单独成模块
----------------
同一批缺口有四个出口：

| 出口 | 给谁看 |
|---|---|
| `tools/make_tasks.py` | 想开工的人（可建 Issue） |
| `docs/GAPS.md` | 第一次进库的人（一页看全） |
| `scholia_gaps`（MCP） | agent（决定下一步查什么） |
| `tools/kbcheck.py` 的提示 | 提交前的人 |

**四张嘴说同一件事，就必须只有一个脑子。** 各算各的，迟早出现
「页面说 37、任务清单说 35」这种自相矛盾——而且这种矛盾没有任何检查会发现，
因为两边都「算对了」，只是算的不是同一件事。

所以：计算只在这里做一次，其余三处只负责**呈现**。

口径（什么算「缺口」）
----------------------
只收**机器能数出来**的缺口。机器数不出来的（论证站不站得住、前置是否真实必需、
教学上够不够）一律不进来——把它们混进来，会让这张表看起来比实际更权威。

用法
----
    from gaps import compute
    data = compute(index, cites, evid)      # 三个 dict 都来自生成物
    data["分组"]["review"]["条目"]           # 该组的具体条目

零依赖、只读、不写盘。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 读过全文/摘要，才算「有资格复核」
READ_DEPTH = {"全文", "摘要"}

# 每组的元信息。中英各一份：`docs/GAPS.md` 与 `docs/GAPS.en.md` 用**同一批数字**，
# 否则两份页面会在「翻译的时候」悄悄分叉。
# 字段：key / 中文名 / 英文名 / 中文为什么 / 英文为什么 / 中文怎么做 / 英文怎么做
GROUPS = [
    ("review", "三分钟复核", "Three-minute review",
     "状态是「待审」，论证已写、证据也读过了 —— 只差**一次复核**。复核者可以是人（署名），也可以是 agent（留四栏 `## 复核记录`），两者都写 `已确证`。",
     "Status is `待审`, the argument is written and the evidence has been read — "
     "only one review is missing: by a human (signature) or an agent (four-field `## 复核记录`) — either can write `已确证`.",
     "人或 agent 复核一条（agent 用 `tools/review_packet.py` + `tools/quote_check.py`，写完 `## 机审记录`）。按下游依赖数排序。",
     "Open a “review one entry” issue; no writing needed. Sorted by downstream dependents: "
     "editing it affects the most other entries."),
    ("review-blocked", "待审，但复核还开不了口", "Awaiting review, evidence unread",
     "状态是「待审」，但引用的证据至少有一条只到 `仅定位`/`未核验`（或论证还没写、没引用证据）—— "
     "复核者打开来源也无从判断。这是「复核」的**前置条件**，不是另一种复核。",
     "Status is `待审`, but at least one cited source is only located, not read "
     "(or the argument is missing, or nothing is cited) — a reviewer has nothing to compare against. "
     "This is the **precondition** for review, not another kind of review.",
     "打开该证据的定位，读完并把 `核验深度` 改成 `摘要`/`全文`；或换一份已读过的来源。",
     "Open the source at its locator, read it, raise `核验深度` to `摘要`/`全文`; "
     "or cite a source that has already been read."),
    ("provenance", "溯源档没到 T4 的条目", "Provenance below T4",
     "引用的来源里**最弱的一份**没有读到全文（`T3` 摘要 / `T2` 仅定位 / `T1` 未核验 / `T0` 无据）。"
     "这不是「内容可能不对」，是「顺着它核到底会撞上没读过的地方」。",
     "The **weakest** cited source was not read in full (`T3` summary / `T2` located only / "
     "`T1` unverified / `T0` no basis). This does not mean the content is wrong — it means "
     "a reader following the chain hits a place nobody has read.",
     "打开那条证据的定位读一遍，把 `核验深度` 提到 `全文`；或换一条已读过的来源。",
     "Open that source at its locator, read it, raise `核验深度` to `全文`; "
     "or cite a source that has already been read in full."),
    ("translate", "补英文译本", "Missing English edition",
     "没有 `path_en`：英文读者点进来会落到中文页。",
     "No `path_en`: an English reader lands on a Chinese page.",
     "文件名由 `id` 派生（`<id 末段去类型前缀>.en.md`），与中文原件同目录。",
     "The filename is derived from `id` (`<id tail minus type prefix>.en.md`), "
     "in the same folder as the Chinese original."),
    ("methods", "缺教法的知识点", "Concepts without a method",
     "知识点回答「是什么」，教法回答「怎么讲」。覆盖度页只数前者，所以这一栏在别处看不见。",
     "A concept answers *what it is*; a method answers *how to teach it*. "
     "The coverage page counts only the former, so this gap is invisible elsewhere.",
     "从教材里找有标记的课堂做法（[BL]/[OL]/[AL]），新建「教法」条目并挂 `knowledge_point`。",
     "Find a marked classroom practice in a textbook ([BL]/[OL]/[AL]), "
     "create a 教法 entry and point its `knowledge_point` at the concept."),
    ("external", "库外前置：该建节点了吗", "Out-of-library prerequisites",
     "同一个 `外部先修` 标识出现在 ≥2 个对象里 —— 它在多条链路前面反复出现。",
     "The same `外部先修` key appears in ≥2 objects — it recurs in front of several chains.",
     "先判断这条前置是否真实必需（M-12）；决定建节点后，把各条目的声明迁到 `edges.先修`。",
     "First judge whether the prerequisite is really required (M-12); if you build a node, "
     "migrate the declarations to `edges.先修`."),
    ("path-thin", "路径成果只有一处覆盖", "Outcomes covered by a single step",
     "某个学习成果只被一个环节覆盖：那一处讲砸，学生就没有第二次机会。",
     "A learning outcome is covered by exactly one step: if that step fails, "
     "the student gets no second chance.",
     "给这些成果补第二个环节（换一种讲法 / 换一个入口），或把它拆成更小的成果。",
     "Add a second step for these outcomes (another explanation or entry point), "
     "or split them into smaller outcomes."),
    ("path-shallow", "路径覆盖的证据没读过", "Coverage not backed by read evidence",
     "覆盖该成果的条目，证据最高只到 `仅定位`/`未核验` —— 位置排上了，依据还没读。",
     "The entries covering this outcome have evidence at most at `仅定位`/`未核验` — "
     "the slot is scheduled, the basis has not been read.",
     "把覆盖条目的证据核验深度补到 `摘要`/`全文`，或换一条有依据的条目来覆盖。",
     "Raise the covering entries' verification depth to `摘要`/`全文`, "
     "or cover it with an entry that has a read basis."),
    ("todo", "条目自己写下的「待补」", "Gaps the entries wrote themselves",
     "作者在正文里留了 `**待补**：` —— 这是条目自己承认的缺口，不是外部推测。",
     "The author left `**待补**:` in the body — a gap the entry admits to, not one inferred from outside.",
     "按正文里那句话补内容；补完删掉标记。",
     "Fill in what that sentence asks for, then delete the marker."),
    ("coverage", "物理覆盖度仍为 🔴 的章", "Physics chapters still 🔴",
     "对照人教版目录，整章在本库没有任何知识点。",
     "Against the PEP catalogue, the whole chapter has no concept entry in this library.",
     "先采集该章的核心概念，再写知识点；覆盖度页会随条目自动更新。",
     "Collect the chapter's core concepts first, then write concept entries; "
     "the coverage page updates itself."),
]

GROUP_MAP = {g[0]: {"名称": g[1], "名称_en": g[2], "为什么": g[3], "为什么_en": g[4],
                    "怎么做": g[5], "怎么做_en": g[6]} for g in GROUPS}


def _load(root, name):
    p = Path(root) / name
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def _read(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except OSError:
        return ""


def _methods_cover(root):
    """哪些知识点的文件名（stem）已经有教法挂上去。

    直接扫 `methods/*.md` 的 `knowledge_point:` 行：`index.json` 里不存这条边，
    而它正是「缺教法」的判据。读不到就返回空集（宁可多报，不静默少报）。
    """
    covered = set()
    for p in Path(root).rglob("knowledge/*/methods/*.md"):
        if p.name.endswith(".en.md"):
            continue
        text = _read(p)
        m = re.search(r"^knowledge_point:\s*(.+)$", text, re.M)
        if not m:
            continue
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", m.group(1)):
            covered.add(Path(link).stem)
    return covered


def _todo_markers(root, objs):
    """正文里写着 `**待补**` / `待补：` 的条目（每条只报第一处）。"""
    out = []
    for o in objs:
        text = _read(Path(root) / o["path"])
        if not text:
            continue
        for line in text.split("\n"):
            if "**待补**" in line or "待补：" in line:
                out.append({
                    "id": o["id"], "title": o["title"], "title_en": o.get("title_en"),
                    "path": o["path"],
                    "行": line.strip("->- ").strip()[:120],
                })
                break
    return out


def _physics_coverage(root):
    """物理覆盖度页 `## 总览` 里「本库现状」列以 🔴 开头的章。"""
    p = Path(root) / "knowledge" / "physics" / "coverage" / "README.md"
    text = _read(p)
    if not text:
        return []
    section, out = "", []
    for line in text.replace("\r\n", "\n").split("\n"):
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if section != "总览" or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        # 只看「本库现状」列（第 3 列）以 🔴 开头的行：整行含 🔴 会把
        # 统计块与正文里的「🔴 完全缺」也算成章级主题。
        if len(cells) >= 3 and cells[2].startswith("🔴"):
            out.append({"章": cells[1]})
    return out


def compute(index, cites=None, evid=None, root=ROOT):
    """算出全库缺口。`index` / `cites` / `evid` 是生成物内容，缺省从磁盘读。

    返回：`{"统计": {...}, "分组": {key: {"名称","为什么","怎么做","数量","条目"}}, "顺序": [...]}`
    """
    root = Path(root)
    if cites is None:
        cites = (_load(root, "citations.json") or {}).get("by_id", {})
    if evid is None:
        evid = (_load(root, "evidence.json") or {}).get("entries", {})

    objs = index.get("objects", [])
    stats = index.get("统计", {})

    # 下游依赖：有多少条别的条目把它写进 `先修`。复核排序用它——
    # 这是启发式，不说明哪条更重要，只说明改它会影响多少条别的条目。
    inbound = {}
    for o in objs:
        for name in o.get("先修") or []:
            stem = Path(name).stem
            inbound[stem] = inbound.get(stem, 0) + 1

    review, review_blocked = [], []
    for o in objs:
        if o["status"] != "待审":
            continue
        ev_ids = list(cites.get(o["id"], {}).get("证据", []))
        depths = [evid.get(e, {}).get("核验深度") for e in ev_ids]
        unread = [e for e, d in zip(ev_ids, depths) if d not in READ_DEPTH]
        if o.get("论证") and depths and not unread:
            review.append({
                "id": o["id"], "title": o["title"], "title_en": o.get("title_en"),
                "path": o["path"], "path_en": o.get("path_en"),
                "下游依赖": inbound.get(Path(o["path"]).stem, 0),
            })
        else:
            review_blocked.append({
                "id": o["id"], "title": o["title"], "title_en": o.get("title_en"),
                "path": o["path"], "path_en": o.get("path_en"),
                "下游依赖": inbound.get(Path(o["path"]).stem, 0),
                "未读证据": unread,
                "无论证": not o.get("论证"),
                "无证据": not ev_ids,
            })
    review.sort(key=lambda x: (-x["下游依赖"], x["title"] or ""))
    review_blocked.sort(key=lambda x: (-x["下游依赖"], x["title"] or ""))

    translate = [{"id": o["id"], "title": o["title"], "title_en": o.get("title_en"),
                  "path": o["path"]}
                 for o in objs if not o.get("path_en")]

    # 溯源档低于 T4：最弱一环没读到全文。列出**是哪几条证据**拖低的——
    # 只说「这条不够好」没有用，要说「去读 ev-043」。
    provenance = []
    for o in objs:
        tier = o.get("溯源")
        if tier in (None, "T4"):
            continue
        ev_ids = list((cites.get(o["id"]) or {}).get("证据") or [])
        weak = [e for e in ev_ids
                if e not in evid or evid[e].get("作废")
                or evid[e].get("核验深度") != "全文"]
        provenance.append({"id": o["id"], "title": o["title"],
                           "title_en": o.get("title_en"), "path": o["path"],
                           "path_en": o.get("path_en"), "溯源": tier,
                           "薄证据": weak})
    provenance.sort(key=lambda x: (x["溯源"], -(len(x["薄证据"])), x["title"] or ""))

    covered = _methods_cover(root)
    methods = [{"id": o["id"], "title": o["title"], "title_en": o.get("title_en"),
                "path": o["path"]}
               for o in objs
               if o["type"] == "知识点" and Path(o["path"]).stem not in covered]

    external = [g for g in (index.get("外部先修") or {}).get("按标识", [])
                if g.get("出现次数", 0) >= 2]
    external.sort(key=lambda g: (-g.get("出现次数", 0), g.get("标识", "")))

    path_thin, path_shallow = [], []
    for o in objs:
        cov = o.get("覆盖度") or {}
        if cov.get("单环节成果"):
            path_thin.append({"id": o["id"], "title": o["title"],
                              "title_en": o.get("title_en"), "path": o["path"],
                              "成果": cov["单环节成果"]})
        if cov.get("证据薄成果"):
            path_shallow.append({"id": o["id"], "title": o["title"],
                                 "title_en": o.get("title_en"), "path": o["path"],
                                 "成果": cov["证据薄成果"]})
    path_thin.sort(key=lambda x: (-len(x["成果"]), x["title"] or ""))
    path_shallow.sort(key=lambda x: (-len(x["成果"]), x["title"] or ""))

    items = {
        "review": review,
        "review-blocked": review_blocked,
        "provenance": provenance,
        "translate": translate,
        "methods": methods,
        "external": external,
        "path-thin": path_thin,
        "path-shallow": path_shallow,
        "todo": _todo_markers(root, objs),
        "coverage": _physics_coverage(root),
    }

    groups = {}
    for key in items:
        meta = GROUP_MAP[key]
        groups[key] = {"key": key, **meta,
                       "数量": len(items[key]), "条目": items[key]}

    # 路径成果的全局账：**73 个成果全部有环节覆盖，其中 67 个（92%）只讲一次**。
    # 这组数字原来只活在 README 的一句手写叙述里；写进生成物，页面与文档才能引用同一个事实。
    path_cov = [o["覆盖度"] for o in objs if (o.get("覆盖度") or {}).get("声明")]
    path_stats = {
        "条数": len(path_cov),
        "声明": sum(c["声明"] for c in path_cov),
        "已覆盖": sum(c["已覆盖"] for c in path_cov),
        "单环节": sum(len(c.get("单环节成果") or []) for c in path_cov),
    }
    path_stats["单环节占比"] = (
        round(100 * path_stats["单环节"] / path_stats["声明"])
        if path_stats["声明"] else 0)

    return {
        "统计": {
            "对象": len(objs),
            "可作事实引用": sum(1 for o in objs if o.get("可作事实引用", True)),
            "不可作事实引用": sum(1 for o in objs if not o.get("可作事实引用", True)),
            "证据": stats.get("证据条数", len(evid)),
            "事件": stats.get("事件条数", len(index.get("事件") or [])),
            "状态": stats.get("按状态") or {},
            "溯源": stats.get("按溯源档") or {},
            "路径成果": path_stats,
            "缺口合计": sum(g["数量"] for g in groups.values()),
        },
        "分组": groups,
        "顺序": [g[0] for g in GROUPS],
    }


def counts(data):
    """`{key: 数量}`，给测试与摘要用。"""
    return {k: g["数量"] for k, g in data["分组"].items()}
