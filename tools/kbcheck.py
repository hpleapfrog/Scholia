#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""机械校验：不依赖任何密钥、不依赖任何第三方库。

校验项目里所有知识对象是否符合 FORMAT.md 的规范。

用法:
    python tools/kbcheck.py

退出码:
    0  全部通过
    1  有不符合规范之处

它查的是**人读不出来的东西**：单看一个文件都没问题，问题只在文件之间
（id 冲突、链接可达性、教法禁忌是否为空）。
"""
import collections
import json
import os
import posixpath
import re
import sys
from pathlib import Path

# 仓库根目录（本文件在 tools/ 下）
ROOT = Path(__file__).resolve().parent.parent

# 同目录的 `gaps.py`：缺口清单的**唯一**计算入口。
# `docs/GAPS.md` 的生成块、`make_tasks.py`、MCP 的 `scholia_gaps` 都走它——
# 四处呈现、一个脑子，否则「页面说 37、任务清单说 35」这种矛盾没人发现。
sys.path.insert(0, str(Path(__file__).resolve().parent))
import gaps  # noqa: E402  同目录、只读、零依赖

TYPES = {"知识点", "命题", "教法", "误解", "路径", "资源"}

ALLOWED_STATUS = {
    "知识点": {"草案", "待审", "有效", "争议", "需复审", "已失效"},
    "命题": {"草案", "待审", "争议", "暂定确认", "已确证", "已推翻", "失据", "需复审", "已失效"},
    "教法": {"草案", "待审", "有效", "争议", "需复审", "已失效"},
    "误解": {"草案", "待审", "有效", "争议", "需复审", "已失效"},
    "资源": {"草案", "待审", "有效", "争议", "需复审", "已失效"},
    "路径": {"草案", "待审", "有效", "争议", "需复审", "已失效"},
}

REQUIRED_FIELDS = ["id", "type", "title", "status", "author", "created",
                   "updated", "scope", "edges", "evidence", "license"]

REQUIRED_SECTIONS = {
    "知识点": ["定义", "关联", "论证", "变更记录"],
    "命题": ["陈述", "依据", "论证", "变更记录"],
    "教法": ["做法", "禁忌", "风险", "证据", "论证", "变更记录"],
    "误解": ["陈述", "出现频率", "变更记录"],
    "路径": ["编排", "自检", "变更记录"],
    "资源": ["定位", "变更记录"],
}

# ── `事件`：与知识对象**并列的另一类记录**，单开顶层 `events/` ──────────────
# 命题回答「什么是真的」（有真值、可被论证攻防）；事件回答「发生了什么」
# （时间索引的事实，只有证据、没有可攻击的主张）。
# 因此：事件**不进** `objects`、不进学科统计、没有「论证」段、没有任何边。
EVENT_TYPE = "事件"
EVENT_DIR = "events/"

# 库外的未核稿：**不是知识对象**，不参与配对、不参与状态统计。
# 它存在是因为「删掉别人的稿子」比「把它放错地方」更糟（见 drafts/README.md）。
DRAFT_DIR = "drafts/"
EVENT_FIELDS = ["id", "type", "title", "status", "author", "created",
                "updated", "evidence", "license"]
EVENT_SECTIONS = ["陈述", "依据", "变更记录"]
# 状态只回答「这条现在还在更新吗」——不含 已确证/已推翻/失据/已失效。
EVENT_STATUS = {"持续更新", "已封存"}
EVENT_ID_PREFIX = "kb:event:"

# scope.学段 的枚举。组合用「至」连接（如「初中至高中」），不要在值里用 `/`。
ALLOWED_STAGES = {"小学", "初中", "高中", "大学", "不限"}

# 教法 scope.水平档 允许的档位代码；跨全部档位的方法写「不分档」。
ALLOWED_LEVEL_CODES = {"BL", "OL", "AL"}
LEVEL_UNDIVIDED = "不分档"
LEVEL_ALLOWED = ALLOWED_LEVEL_CODES | {LEVEL_UNDIVIDED}

# 可选字段 `外部先修`：声明「要懂这条，先会 X」，而 X 在本库**没有节点**。
# 它与 `edges.先修` 分开：后者是**库内图**上的边，前者只是**声明**（见 FORMAT.md §3）。
# `标识` 是稳定 ASCII 键，用来把「同一个前置在多个条目里反复出现」数出来。
EXTERNAL_PREREQ_KEY = "外部先修"
EXTERNAL_PREREQ_FIELDS = ("名称", "标识", "学科", "学段", "来源")
EXTERNAL_PREREQ_ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")
EXTERNAL_PREREQ_SOURCE = re.compile(r"^ev-\d+$")

# 指向本仓库自身的绝对链接（Issue 模板里出现过）。
# 它们必须和相对链接一样被校验——否则改标题就会悄悄改坏一个链接，而没人发现。
SELF_URL = re.compile(
    r"^https?://github\.com/hpleapfrog/Scholia/(?:blob|tree)/[^/]+/(.+)$")

# 许可：本库知识内容统一 CC BY-SA 4.0（见 LICENSE）
ALLOWED_LICENSE = "CC-BY-SA-4.0"

# 学科 → id 前缀（slug）。id 必须与学科一致，防止跨学科编号漂移。
SUBJECT_SLUGS = {"物理": "physics", "生活": "life", "医学": "med",
                 "地理": "geog", "科学": "science",
                 "交通": "transport", "计算机": "computing", "经济": "econ",
                 "法律": "law", "数学": "math"}

# 学科目录名（`knowledge/<subject>/`）。**与 id 前缀（SUBJECT_SLUGS）是两套名字**：
# id 前缀要短（`kb:med:`），目录名要能读（`knowledge/medicine/`）。
# 目录名是给人和 URL 看的——路径里出现中文会在复制链接、跨工具处理时变成百分号编码。
SUBJECT_DIRS = {"物理": "physics", "生活": "life", "医学": "medicine",
                "地理": "geography", "科学": "science", "交通": "transport",
                "计算机": "computing", "经济": "economics", "法律": "law",
                "数学": "mathematics"}

# 证据表的枚举（见 evidence/README.md 表头图例）
EVIDENCE_CATEGORIES = {"教材", "论文", "指南", "官方文件", "交互式模拟",
                       "出版社勘误表", "本库数据"}
EVIDENCE_GRADES = {"高", "中", "低", "—"}
EVIDENCE_DEPTHS = {"全文", "摘要", "仅定位", "未核验", "—"}
# 核验深度的排序：用来算「覆盖这个成果的证据，最高读到了哪一层」
DEPTH_RANK = {"未核验": 1, "仅定位": 2, "摘要": 3, "全文": 4, "—": 0}
DEPTH_NAME = {v: k for k, v in DEPTH_RANK.items() if k != "—"}

# 只有「命题」可以说是「已确证」——其余都是组织层或条件性的
ONLY_CLAIMS_CAN_BE_CONFIRMED = True

# 禁止在知识对象里出现的结论性用语（AI 或人都不能写）
FORBIDDEN_PHRASES = []

# 没有 .md 扩展名、但含 Markdown 链接的文档，必须一并检查
EXTRA_TEXT_FILES = ["LICENSE", "LICENSE-CODE"]

# ── 机器可读索引（index.json）────────────────────────────────────────────
# 给 AI 与其他程序读的唯一入口。**由本脚本生成，不手写** ——
# 手写的索引必然与内容脱节，那就是「信息是错的」。

INDEX_FILE = ROOT / "index.json"
CITATIONS_FILE = ROOT / "citations.json"
EVIDENCE_FILE = ROOT / "evidence.json"

# 状态的含义（给机器读；与 FORMAT.md §4 一致）
STATUS_MEANING = {
    "草案": "刚写下，尚未自检",
    "待审": "内容完整，但没有任何人独立复核过",
    "有效": "当前没有已知的**存活攻击**；**不等于**已被独立复核",
    "争议": "存活集合里存在结论互相冲突的论证",
    "暂定确认": "作者已核对，但**没有非作者的独立复核**",
    "已确证": "本库最高等级：有一名**非作者**的复核者按规则核过。"
              "复核者可以是人，也可以是 agent——**是谁写在 `复核者` 字段上**",
    "需复审": "刚被改动过，**还没有人重新看过**",
    "已推翻": "已被论证推翻",
    "失据": "**曾有论证，但被击倒了** —— 主张还在，**当前没有任何支撑它的论证**",
    "已失效": "依据已过时或被取代",
}

# `事件` 的状态含义（与知识对象的状态分开）
EVENT_STATUS_MEANING = {
    "持续更新": "**事件仍在发展**，本条随新进展增补证据行",
    "已封存": "**事件已不再发展**，不再增补",
}

# **不要把它当事实引用**的状态
NOT_CITABLE = {"失据", "已推翻", "已失效"}

# 状态的中英对照（给 AI 与双语文档用）
STATUS_EN = {
    "草案": "draft",
    "待审": "pending review",
    "有效": "effective",
    "争议": "disputed",
    "暂定确认": "provisionally confirmed",
    "已确证": "confirmed",
    "需复审": "needs re-review",
    "已推翻": "overturned",
    "失据": "unsupported",
    "已失效": "expired",
}

EVENT_STATUS_EN = {
    "持续更新": "ongoing",
    "已封存": "archived",
}

# ── 溯源档：机器算得出、又不冒充真值的那一维 ────────────────────────────────
# `status` 回答「有没有站得住的论证」（要人判），`溯源档` 回答
# 「它踩的每一份来源，被读到了哪一层」（机器可算）。
# 取**最弱一环**：一条论证引了 5 份来源、4 份读完，剩 1 份只核了位置——
# 这条链的强度仍是「只核了位置」，不是「4/5 读完了」。
# 它**不是**第七种 status：不表示真假，也不参与 `暂定确认` 的判定，
# 所以「0 条已确证」与「98% 全文核读」可以同时成立，且两句话都是真的。
# agent 复核（写 `已确证` 的第二条通道）必须留的记录字段：**四个都得有**，缺一个就等于没记录。
# 为什么是这四个：模型是谁、什么时候、引文核了几条、**哪些判不了**——
# 最后一项是这条规则的良心：一份不说自己边界的复核记录，比没有记录更危险。
AGENT_REVIEW_SECTION = "复核记录"
AGENT_REVIEW_FIELDS = ("模型", "日期", "引文核验", "限制")

TIER_ORDER = ["T4", "T3", "T2", "T1", "T0"]
TIER_MEANING = {
    "T4": "**全文核读**：引用的每一份来源都通读过，含定位、许可与版本",
    "T3": "**摘要核读**：最弱的一份只读到摘要",
    "T2": "**仅定位**：最弱的一份只核了「这一页有没有这段」，没有通读",
    "T1": "**未核验**：最弱的一份登记了，但没有人打开过",
    "T0": "**无据**：引用的证据里有一条已作废，或索引里根本没有这个编号",
}
TIER_EN = {
    "T4": "**read in full** — every cited source was read end to end (locator, licence, version)",
    "T3": "**read as summary** — the weakest cited source was read only as a summary",
    "T2": "**located only** — the weakest source was checked for “is this passage here”, not read",
    "T1": "**unverified** — the weakest source is registered but nobody has opened it",
    "T0": "**no basis** — a cited evidence record is void, or the id is not in the registry",
}

# 每个学科的覆盖说明（手写；**不写数字**，数字由 objects 自动统计在旁边）
SUBJECT_NOTES = {
    "物理": "覆盖中国高中物理的一部分。按人教版章级主题对照，**一半左右**的章级主题"
            "一条概念都没有（缺口清单见 `knowledge/physics/coverage/`）。",
    "地理": "全部是同一本香港教材的勘误。",
    "生活": "出行规则：北京地铁与民航的官方规定（含两份官方文件）。",
    "科学": "一条勘误。",
    "医学": "临床指南与随机试验的结论；一律以「指南 / 研究规定了 X」表述，**不提供诊疗建议**。",
    "交通": "道路交通与轨道交通：只收**官方文件**能核验的结论，不收办事流程。",
    "计算机": "标准与官方文档能定位的结论；**不收教程式步骤**。",
    "经济": "统计数据与权威文本能定位的结论；**不收预测与建议**。",
    "法律": "成文法文本的制度性规定（构成要件 · 期限 · 法律效果）；**不收个案裁判与法律意见**。",
    "数学": "OpenStax《Calculus Volume 3》第 6 章（Vector Calculus）的出版社勘误；"
            "每条只主张「出版方已记录并接受」，不主张当前网页版仍错。",
}
SUBJECTS_FALLBACK = "本学科尚无覆盖说明 —— **不要假设它覆盖了什么**，请看 objects。"

# 学科说明的英文版（给 START.en.md 的生成块用）
SUBJECT_NOTES_EN = {
    "物理": "Part of Chinese senior-high physics. Against the PEP chapter-level topics, "
            "about half the chapters have not a single concept here (gap list in `knowledge/physics/coverage/`).",
    "地理": "All errata from one Hong Kong textbook.",
    "生活": "Travel rules: official Beijing metro and civil-aviation provisions (two official documents).",
    "科学": "One erratum.",
    "医学": "Conclusions from clinical guidelines and randomized trials; always phrased as "
            "\"the guideline specifies X\" — **no treatment advice**.",
    "交通": "Road and rail: only conclusions verifiable in **official documents**; no how-to procedures.",
    "计算机": "Conclusions locatable in standards and official docs; **no tutorial steps**.",
    "经济": "Conclusions locatable in statistical releases and authoritative texts; **no forecasts or advice**.",
    "法律": "Institutional provisions of statute law (elements · deadlines · legal effect); "
            "**no case rulings or legal advice**.",
    "数学": "Publisher errata from Chapter 6 (Vector Calculus) of OpenStax *Calculus Volume 3*; "
            "each entry claims only that the publisher recorded and accepted it, not that the current web text is still wrong.",
}
SUBJECTS_FALLBACK_EN = "No coverage note yet — **do not assume what it covers**; read `objects`."

EVIDENCE_INDEX = ROOT / "evidence" / "README.md"


def parse_evidence_index():
    """把 `evidence/README.md` 的索引表解析成结构化数据。

    **为什么要进机器索引**：条目里的 `证据: ["ev-039"]` 只是一个编号。
    **AI 引用一个编号等于没引用** —— 它得再打开另一个文件才知道那是哪本书哪一页。
    把定位带进来，AI 才有可能**给出真实来源**而不是空编号。
    """
    if not EVIDENCE_INDEX.exists():
        return {}
    out = {}
    for line in EVIDENCE_INDEX.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 8 or not re.fullmatch(r"ev-\d+", cells[0]):
            continue
        _, cat, grade, depth, locator, year, lic, used = cells[:8]
        void = "作废" in cat
        out[cells[0]] = {
            "类别": cat,
            "等级": grade,
            "核验深度": depth,
            "定位": re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", locator),   # 链接只留文字
            "链接": (re.search(r"\]\((http[^)]+)\)", locator) or [None, ""])[1]
                    if re.search(r"\]\((http[^)]+)\)", locator) else "",
            "时间": year,
            "许可": lic,
            "作废": void,
            "引用处": used,
        }
    return out


def reviewer_kind(o):
    """`已确证` 是**谁**签的：`"人"` / `"agent"` / `None`。

    这一格不能省。2026-11-05 起 agent 也能写 `已确证`，于是「已确证」这三个字
    不再自动等于「有一个人类看过」。**读者有权一眼看出是谁**——
    所以它被算成一个字段，而不是藏在正文某一段里。
    """
    names = set(re.findall(r"@([\w][\w.\-]*)", fm_value(o["fm"], "author") or ""))
    names |= set(re.findall(r"@([\w][\w.\-]*)",
                            section_body(o["text"], "变更记录") or ""))
    if len(names) >= 2:
        return "人"
    if (section_body(o["text"], AGENT_REVIEW_SECTION) or "").strip():
        return "agent"
    return None


def provenance_tier(ids, evidence):
    """一条对象踩到的**最弱一环**读到了哪一层（T0–T4）。

    为什么取最弱而不取平均、不取最多：一条论证的可核性由它**最薄的那份来源**
    决定。5 份来源里 4 份读完、1 份只核了位置，读者顺着最薄的那份一路核下去，
    就会撞上「这里其实没人读过」。平均分会把这件事藏起来。

    **它不回答「对不对」**，只回答「顺着它能不能一路核到底」。所以它既能与
    「0 条已确证」共存，也不构成对 `status` 的任何背书。
    """
    depths = []
    for e in ids:
        rec = evidence.get(e)
        if not rec or rec.get("作废"):
            return "T0"
        depths.append(DEPTH_RANK.get(rec.get("核验深度"), 0))
    if not depths:
        return "T0"
    worst = min(depths)
    return {4: "T4", 3: "T3", 2: "T2", 1: "T1"}.get(worst, "T0")


def build_indexes(objects, events):
    """生成**三份**机器可读文件 —— 每份只装一件事。

    **为什么拆**：原来所有东西都在 `index.json` 里（179 KB ≈ 48k tokens），
    而 `llms.txt` 说「唯一需要解析的文件是 index.json」——
    那等于让每个只想知道「有没有这条」的 AI，**先吃下全部定位与全部证据**。

    | 文件 | 装什么 | 什么时候读 |
    |---|---|---|
    | `index.json` | 导航 + **能不能引用**：id / type / title / status / path / path_en / 学科 / 学段 / 可作事实引用 | 每次先读这个 |
    | `citations.json` | **要引用时才需要**：`证据` / `来源`（解析好的定位）/ `适用` / `条件` / 免责块 / 引用须写明 | 确定要引某条之后，按 id 取一条 |
    | `evidence.json` | 全部证据登记（类别 · 等级 · 核验深度 · 定位 · 许可 · 是否作废） | 需要核实出处、或要解释「这条为什么失据」时 |

    **三份都是生成物**，手改会被校验判失败。
    """
    evidence = parse_evidence_index()

    def src_list(ids):
        out = []
        for e in ids:
            r = evidence.get(e)
            if not r:
                out.append(f"{e}（**索引里没有这一条**）")
                continue
            mark = "**已作废** " if r["作废"] else ""
            out.append(f"{mark}{e}：{r['定位']}")
        return out

    objs, cites = [], {}
    ext_groups = collections.defaultdict(lambda: {
        "名称": set(), "学科": set(), "学段": set(), "对象": []})
    # 路径强度：R-GRAPH-07 的两个维度（单环节 / 证据薄）写进索引，
    # 否则它只活在终端提示里——agent 与任务清单都看不见。
    path_stats = path_outcome_stats(objects)
    for rel, o in sorted(objects.items()):
        st = fm_value(o["fm"], "status")
        ids = evidence_ids_of(o["fm"])
        ext = external_prereqs_of(o["fm"])
        pre_h = o["text"].split("\n## ", 1)[0]
        _id = fm_value(o["fm"], "id")
        _en = en_path(rel, _id) if _id else None
        _en_exists = bool(_en and (ROOT / _en).exists())
        entry = {
            "id": _id,
            "type": o["type"],
            "title": fm_value(o["fm"], "title"),
            "status": st,
            "path": rel,
            # 英文译本的路径（文件名由 id 派生）；没有译本时为 null。
            # **AI 引用时说中文页还是英文页要说得出来**——只给一个 path，
            # 英文读者会被送去中文文件。
            "path_en": _en if _en_exists else None,
            "学科": fm_nested(o["fm"], "学科"),
            "学段": fm_nested(o["fm"], "学段"),
            "可作事实引用": st not in NOT_CITABLE,
            "先修": [Path(x).name for x in fm_links(o["fm"], "先修")],
            "论证": sorted(arg_ids(o["text"])),
            # 最弱一环读到了哪一层：T4 全文 / T3 摘要 / T2 仅定位 / T1 未核验 / T0 无据。
            # 与 `status` **正交**：状态要人判，这一维机器算得出。
            "溯源": provenance_tier(ids, evidence),
        }
        # `复核者` 只在这一格有意义时出现：其它状态没有「谁签的」这回事。
        if st == "已确证":
            entry["复核者"] = reviewer_kind(o)
        # 英文标题：让英文页面与英文检索能**用英文叫出这条**，而不是把中文标题
        # 塞给英文读者。只读一次 en 文件的前 4 KB（front-matter 一定在里面）。
        if _en_exists:
            head = (ROOT / _en).read_text(encoding="utf-8")[:4000]
            m = re.search(r"^title:\s*(.+)$", head, re.M)
            if m:
                entry["title_en"] = m.group(1).strip().strip('"')
        # 路径的覆盖度：`已覆盖/声明` 是「有没有」，`单环节成果` 是「够不够」。
        # 只在**声明了 outcomes** 的路径上写——没声明时这个数字没有意义。
        if o["type"] == "路径":
            d = path_stats.get(rel) or {}
            if d.get("声明"):
                cov = {"已覆盖": d["已覆盖"], "声明": d["声明"]}
                if d["单环节"]:
                    cov["单环节成果"] = d["单环节"]
                if d["证据薄"]:
                    cov["证据薄成果"] = d["证据薄"]
                entry["覆盖度"] = cov
        # 可选字段：没有就不写，避免给 700+ 条对象各加一个空数组。
        if ext:
            entry["外部先修"] = ext
            for e in ext:
                g = ext_groups[e["标识"]]
                g["名称"].add(e["名称"])
                g["学科"].add(e["学科"])
                g["学段"].add(e["学段"])
                if _id not in g["对象"]:
                    g["对象"].append(_id)
        objs.append(entry)
        cite = {
            "status": st,
            "溯源": provenance_tier(ids, evidence),
            "证据": ids,
            "来源": src_list(ids),
            "适用": fm_nested(o["fm"], "适用"),
            "条件": fm_nested(o["fm"], "条件"),
            "免责块在正文最前": "> [!CAUTION]" in pre_h,
            "引用时须写明": (f"state={st}"
                        + ("；本库判定它**没有说话算数的论证**" if st in NOT_CITABLE else "")),
        }
        if ext:
            cite["外部先修"] = [{
                "名称": e["名称"],
                "标识": e["标识"],
                "学科": e["学科"],
                "学段": e["学段"],
                "来源": src_list([e["来源"]])[0] if e["来源"] else "",
            } for e in ext]
        if st == "已确证":
            cite["复核者"] = entry.get("复核者")
        cites[_id] = cite

    by_type, by_status, by_subject = collections.Counter(), collections.Counter(), collections.Counter()
    by_tier = collections.Counter()
    for x in objs:
        by_type[x["type"]] += 1
        by_status[x["status"]] += 1
        by_subject[x["学科"].split(" ")[0]] += 1
        by_tier[x["溯源"]] += 1

    # 事件：与 objects 并列的一节。只有证据，没有论证、没有边。
    events_list = []
    for rel, o in sorted(events.items()):
        ids = evidence_ids_of(o["fm"])
        _eid = fm_value(o["fm"], "id")
        _een = en_path(rel, _eid) if _eid else None
        events_list.append({
            "id": _eid,
            "title": fm_value(o["fm"], "title"),
            "status": fm_value(o["fm"], "status"),
            "path": rel,
            "path_en": _een if _een and (ROOT / _een).exists() else None,
            "最后更新": fm_value(o["fm"], "updated"),
        })
        cites[_eid] = {
            "status": fm_value(o["fm"], "status"),
            "证据": ids,
            "来源": src_list(ids),
            "适用": None,
            "条件": None,
            "免责块在正文最前": False,
            "引用时须写明": (f"state={fm_value(o['fm'], 'status')}；"
                        "事件只记录官方发布了什么，**不可作真值判断**"),
        }

    ext_summary = {
        "说明": "`objects[].外部先修` 声明的是**本库没有对应节点**的前置："
                "它只说明「要懂这条，先会 X」，**不是 `先修` 边**，也不表示 X 已在库内。"
                "同一个 `标识` 在 ≥2 个对象里出现时，说明该考虑为它建一个知识点节点。",
        "按标识": [{
            "标识": k,
            "名称": sorted(g["名称"]),
            "学科": sorted(g["学科"]),
            "学段": sorted(g["学段"]),
            "出现次数": len(g["对象"]),
            "对象": g["对象"],
        } for k, g in sorted(ext_groups.items())],
    }

    index = {
        "$comment": "由 tools/kbcheck.py 生成，**请勿手改**。运行 `python tools/kbcheck.py --write-index` 重新生成。",
        "schema_version": 6,
        "repo": "https://github.com/hpleapfrog/Scholia",
        "读到这个文件的 AI 请注意": [
            "**本库是跨学科的**，覆盖程度**按学科差别很大**；它**不只做物理**。",
            "**本库没有任何一条处于 `已确证`。** 不要把这里的任何内容当作『已确证的事实』转述。",
            "每条对象还有一个与 `status` **正交**的 `溯源`（T0–T4）：它说的是"
            "**引用的来源被读到了哪一层**（取最弱一环），不是真假。"
            "`T4`＝引用的每一份来源都通读过；`T2`=最弱那份只核了位置；"
            "`T1`=登记了但没人打开过；`T0`=有作废或查不到的编号。"
            "**引用时请连它一起给出**——「T4 · 全书通读」与「T2 · 只核了位置」"
            "对读者是完全不同的承诺，而 `status` 这一栏看不出这个差别。",
            "`可作事实引用=false` 的条目（状态为 失据/已推翻/已失效）**不要引用**。",
            "**判断「本库有没有 X」要查本文件的 `objects`，不要凭印象。**",
            "**不要整读 `index.json` 之外的东西**：本文件只回答「有什么、能不能引」。"
            "确定要引用某一条之后，再去 `citations.json` 按 id 取那一条的定位与限定"
            "（`适用` / `条件` / 免责块），别把整份 `citations.json` 读进来。",
            "引用任何一条时，**请把 `citations.json` 里那条的 `来源` 给出**"
            "（书名 / 章节 / 页面 URL），并**连 `status` 一起给** —— **只写「ev-039」等于没写来源**。",
            "每条对象有两个路径：`path` 是**中文正本**，`path_en` 是**英文译本**"
            "（文件名由 `id` 派生，同目录；没有译文时为 null）。"
            "**给英文读者引用时请用 `path_en`，不要把中文文件名发给对方。**",
            "`objects[].外部先修` 是**本库没有节点**的前置（名称/标识/学科/学段/来源），"
            "**不是 `先修` 边**；它只说明「要懂这条，先会 X」。"
            "同一个 `标识` 在多个对象里出现，说明该考虑建节点，而不是说本库已经有 X。",
            "本文件顶层的 `事件` 与 `objects` **是两回事**：`objects` 是知识对象"
            "（命题/知识点/…），`事件` 是**按时间记录事实**的另一类记录，"
            "**不含论证、不可作真值判断**；引用事件时给 `status`（持续更新/已封存）"
            "与 `来源`，**不要说「本库确认了」某事件**。",
            "本库里**没有**的内容，**不要算作本库的内容** —— "
            "你可以用别的来源回答，**但要说明那不是本库说的**。",
            "教法（type=教法）的证据主要是**一本美国教材**，**不代表在中国课堂实测有效**。",
            "**转述任何对象前，先去 `citations.json` 取它的 `适用` / `条件` / `免责块在正文最前`** —— "
            "限定不是免责声明的装饰：医学条目的操作参数**只在该人群与条件下成立**，"
            "转述时**必须把限定连同数字一起给出**。",
        ],
        "状态含义": STATUS_MEANING,
        "状态英文": STATUS_EN,
        "复核者含义": "`已确证` 条目的 `复核者`：`人` = 有一名非作者的人类署名；"
                      "`agent` = 由 agent 复核并留下四栏 `## 复核记录`。"
                      "**两者都是 `已确证`，但来源不同——转述时请照抄这个字段。**",
        "溯源档含义": TIER_MEANING,
        "溯源档英文": TIER_EN,
        "溯源档怎么算": "取该对象 `citations.json` 里全部 `证据` 的**最弱一环**"
                        "（`evidence.json` 的 `核验深度`）：任一条作废或查不到 → T0。"
                        "它**不是** `status`：不表示真假，不参与「已确证」判定。",
        "事件状态含义": EVENT_STATUS_MEANING,
        "事件状态英文": EVENT_STATUS_EN,
        "统计": {
            "对象总数": len(objs),
            "按类型": dict(by_type),
            "按状态": dict(by_status),
            "按溯源档": {k: by_tier[k] for k in TIER_ORDER if by_tier.get(k)},
            "按学科": dict(by_subject),
            "已确证条数": by_status.get("已确证", 0),
            "事件条数": len(events_list),
            "证据条数": len(evidence),
            "作废证据条数": sum(1 for r in evidence.values() if r["作废"]),
            "外部先修标识数": len(ext_groups),
            "外部先修声明数": sum(len(v["对象"]) for v in ext_groups.values()),
        },
        "known_limits": {
            "总览": "本库是**跨学科**的，**各学科覆盖程度差别很大**。"
                    "判断「有没有 X」请查 `objects`（或该学科的 `knowledge/<subject>/README.md`），"
                    "**不要假设它覆盖了什么**。",
            "按学科": {
                s: {"条数": n, "说明": SUBJECT_NOTES.get(s, SUBJECTS_FALLBACK)}
                for s, n in sorted(by_subject.items())
            },
            "教法来源": "绝大多数整理自 OpenStax《Physics》（美国高中教材，CC BY），"
                    "记录的是「这本教材建议怎么教」，**不是**「这样教有效」。",
            "程序性知识": "本库**不装**「怎么做一件事」的流程（见 FORMAT.md「本库不装什么」）。",
        },
        "外部先修": ext_summary,
        "objects": objs,
        "事件": events_list,
    }

    citations = {
        "$comment": "由 tools/kbcheck.py 生成，**请勿手改**。**按 id 取一条**，不要整份读。"
                    "这里装的是引用时要写进去的东西：定位、限定、免责块位置。",
        "schema_version": 3,
        "by_id": cites,
    }

    evid = {
        "$comment": "由 tools/kbcheck.py 从 evidence/README.md 生成，**请勿手改**。"
                    "`核验深度` 是「本库读过多少」：全文 / 摘要 / 仅定位 / 未核验。",
        "schema_version": 1,
        "entries": evidence,
    }

    return {"index.json": index, "citations.json": citations, "evidence.json": evid}


def build_index(objects, events):
    """兼容层：返回 `index.json` 那部分（生成块与统计只需要它）。"""
    return build_indexes(objects, events)["index.json"]


def check_index(objects, events, errors):
    """三份机器文件都必须与内容一致——不一致就报错，并告诉怎么修。

    **这是「防止信息是错的」的机制部分**：索引不能手写、不能过期。
    """
    for name, want_obj in build_indexes(objects, events).items():
        p = ROOT / name
        want = json.dumps(want_obj, ensure_ascii=False, separators=(",", ":")) + "\n"
        if not p.exists():
            errors.append(f"{name} 不存在 —— 运行 `python tools/kbcheck.py --write-index` 生成（R-INDEX-01）")
            continue
        have = p.read_text(encoding="utf-8").replace("\r\n", "\n")
        if have != want:
            errors.append(
                f"{name} **与内容不一致**（内容改过但索引没重新生成）—— "
                "运行 `python tools/kbcheck.py --write-index`，然后一起提交（R-INDEX-01）")


def write_index(objects, events):
    """写三份：`index.json`（导航）· `citations.json`（引用时才取）· `evidence.json`（证据登记）。"""
    paths = []
    for name, payload in build_indexes(objects, events).items():
        p = ROOT / name
        p.write_text(
            json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n",
            encoding="utf-8")
        paths.append(p)
    return paths


def parse_front_matter(text):
    """取出 front-matter 原文；没有则返回 None。"""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 3)
    return text[4:end + 1] if end > 0 else None


def front_matter_keys(fm):
    return re.findall(r"^([A-Za-z_][A-Za-z0-9_]*):", fm, re.M)


def fm_value(fm, key):
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip('"') if m else None


def scan_text_files():
    """所有含 Markdown 链接的文档。

    注意：不只是 .md —— LICENSE / LICENSE-CODE 没有扩展名，但同样含相对链接。
    漏掉它们会形成盲区（曾真实漏掉一处引用）。
    """
    files = []
    for base, dirs, names in os.walk(ROOT):
        # `archive/` 是移出任务范围的旧学科：**留在库里但不参与校验**，
        # 也不该因为它的旧链接把主库判红。
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", "__pycache__", "archive"}]
        for n in names:
            if n.endswith((".md", ".yml", ".yaml")):
                files.append(Path(base) / n)
    for n in EXTRA_TEXT_FILES:
        p = ROOT / n
        if p.exists():
            files.append(p)
    return sorted(files)


def resolve_link(src_path, target):
    """把 Markdown 链接目标解析成仓库内的相对路径；解析不到返回 None。"""
    tgt = target.split("#")[0].strip()
    if not tgt or re.match(r"^(https?:|mailto:)", tgt):
        return None
    p = (src_path.parent / tgt.replace("/", os.sep)).resolve()
    try:
        return p.relative_to(ROOT).as_posix()
    except ValueError:
        return None


def fm_links(fm, key):
    """取出 front-matter 里某个键（含缩进块形式）中的 Markdown 链接目标。

    **`[ \\t]*` 不能写成 `\\s*`**：`\\s` 匹配换行，于是「`先修:` 后面什么都没写、
    下面是缩进块」会被当成**行内值**，只取到块里的第一条——
    多行列表的后几项被静默丢掉，而「漏读」不会报错，只会让检查显得通过。
    """
    m = re.search(rf"^[ \t]*{key}:[ \t]*(.+)$", fm, re.M)
    if m:
        line = m.group(1)
    else:
        b = re.search(rf"^[ \t]*{key}:[ \t]*\n((?:[ \t]+.*\n?)*)", fm, re.M)
        line = b.group(1) if b else ""
    return re.findall(r"\[[^\]]*\]\(([^)]+)\)", line)


SCOPE_KEYS = ("学科", "学段", "适用", "条件", "水平档", "范围")


def fm_nested(fm, key):
    """取 front-matter 里可能是缩进（如 scope 下）的键值。

    **优先在 `scope:` 块里找。** 可选字段 `外部先修` 的每个列表项也带 `学科` / `学段`，
    而它们说的是**前置**的学科与学段，不是本条对象的。若全局取第一个匹配，
    把 `外部先修` 写在 `scope` 前面就会让对象的学科/学段被前置的值顶掉——
    这种错误不会报错，只会让索引与医学/学段检查悄悄用错值。
    """
    if key in SCOPE_KEYS:
        m = re.search(r"^scope:[ \t]*\n((?:[ \t]+.*\n?)*)", fm, re.M)
        if m:
            mm = re.search(rf"^[ \t]+{key}:\s*(.+)$", m.group(1), re.M)
            if mm:
                return mm.group(1).strip()
    m = re.search(rf"^[ \t]*{key}:\s*(.+)$", fm, re.M)
    return m.group(1).strip() if m else ""


def _parse_external_block(fm):
    """把可选字段 `外部先修` 解析成 `(found, raw_entries, problems)`。

    `raw_entries` 每项形如 `{"line": 行号, "fields": {子字段: 值}}`；
    **不在这里判合法性**——格式错误要由 `check_external_prereqs` 带规则 ID 报出来，
    而索引生成只需要能读出来的部分（坏样本会在校验里失败，不会静默进索引）。

    只支持块列表：

    ```yaml
    外部先修:
      - 名称: 几何中的角
        标识: angle
        学科: 数学
        学段: 初中
        来源: ev-026
    ```

    行内值只接受 `[]`，但空声明仍会由 `check_external_prereqs` 按「声明了却没有任何条目」
    报错——没有库外前置就删掉字段。写成别的行内值会报问题，因为本库的解析器不装 YAML，
    无法可靠处理行内 map 列表。
    """
    lines = fm.split("\n")
    start = next((i for i, line in enumerate(lines)
                  if re.match(r"^外部先修:[ \t]*(.*)$", line)), None)
    if start is None:
        return False, [], []

    inline = re.match(r"^外部先修:[ \t]*(.*)$", lines[start]).group(1).strip()
    # `外部先修: # 说明` / `外部先修: [] # 没有` 都是合法 YAML；注释不参与判断。
    inline = re.split(r"(?:^|\s+)#", inline, maxsplit=1)[0].strip()
    problems = []
    if inline and inline != "[]":
        problems.append((start + 1, "`外部先修` 必须是缩进列表（或 `[]`），不能写成行内值"))
        return True, [], problems

    entries, cur = [], None
    for i in range(start + 1, len(lines)):
        line = lines[i]
        if not line.strip():
            continue
        if not line.startswith((" ", "\t")):
            break
        stripped = line.lstrip()
        if stripped.startswith("-"):
            if cur is not None:
                entries.append(cur)
            cur = {"line": i + 1, "fields": {}}
            rest = stripped[1:].strip()
            if rest:
                if ":" not in rest:
                    problems.append((i + 1, "`-` 后面必须是 `子字段: 值`"))
                else:
                    k, v = rest.split(":", 1)
                    cur["fields"][k.strip()] = v.strip()
            continue
        if cur is None:
            problems.append((i + 1, "`外部先修` 的子字段必须写在 `-` 列表项下"))
            continue
        if ":" not in stripped:
            problems.append((i + 1, "`外部先修` 列表项内必须是 `子字段: 值`"))
            continue
        k, v = stripped.split(":", 1)
        k = k.strip()
        if k in cur["fields"]:
            problems.append((i + 1, f"同一项里重复子字段 `{k}`"))
        cur["fields"][k] = v.strip()
    if cur is not None:
        entries.append(cur)

    if inline == "[]" and entries:
        problems.append((start + 1, "`外部先修: []` 后面不能再跟列表项"))
    return True, entries, problems


def _clean_external_value(v):
    """去掉首尾空白、成对引号与 YAML 行内注释。

    FORMAT 的示例在值后面写了 `# ...` 注释；用户复制示例时，注释不能
    变成 `来源` / `学段` 的一部分。YAML 里 `#` 只有前面有空白时才是注释，
    所以只按「空白 + #」切；引号内的 `#` 保留。
    """
    v = (v or "").strip()
    if not v:
        return ""
    quote = v[0] if v[0] in "\"'" else ""
    if quote:
        end = v.find(quote, 1)
        if end != -1:
            return v[1:end].strip()
    v = re.split(r"\s+#", v, maxsplit=1)[0].strip()
    return v.strip('"').strip("'").strip()


def external_prereqs_of(fm):
    """取出**结构完整**的 `外部先修` 条目（供索引与双语比对使用）。

    缺子字段的条目在这里被跳过；它们会由 `check_external_prereqs` 报错。
    """
    _found, raw, _problems = _parse_external_block(fm)
    out = []
    for e in raw:
        f = {k: _clean_external_value(v) for k, v in e["fields"].items()}
        if all(f.get(k) for k in EXTERNAL_PREREQ_FIELDS):
            out.append({k: f[k] for k in EXTERNAL_PREREQ_FIELDS})
    return out


def external_source_ids(fm):
    """`外部先修.来源` 里的证据编号（与对象自己的 `evidence` 分开）。"""
    return [e["来源"] for e in external_prereqs_of(fm)
            if EXTERNAL_PREREQ_SOURCE.fullmatch(e["来源"])]


# YAML 里**不能作为裸标量（plain scalar）开头**的指示符。
# 值以这些字符开头时必须加引号，否则严格 YAML 解析器（GitHub 渲染 front-matter
# 时用的那种）会报错，文件页面直接显示解析异常。
# 真实事故：`条件: **仅指……**` 的 `**` 被当成 alias 起始符，
# 报 "did not find expected alphabetic or numeric character while scanning an alias"。
_YAML_BAD_PLAIN_START = ("*", "`", "&", "!", "|", ">", "%", "@")


def check_front_matter_shape(fm, rel, errors):
    """front-matter 的每个 `key: value` 值若以 YAML 指示符开头且未加引号，报错。

    零第三方依赖（本库校验器不装 PyYAML），只做这条最易复发、且会破坏
    GitHub 页面渲染的检查；其余 YAML 合法性仍靠人工与本库自身的解析习惯。
    """
    for i, line in enumerate(fm.split("\n"), 1):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        m = re.match(r"^[^:]+:\s*(.+)$", s)
        if not m:
            continue
        v = m.group(1)
        if v[0] in _YAML_BAD_PLAIN_START:
            errors.append(
                f"{rel}: front-matter 第 {i} 行的值以 {v[0]!r} 开头，"
                f"裸标量不允许（需加引号）—— 严格 YAML 解析器会报错（R-SCHEMA-15）")


STAGES = ("小学", "初中", "高中", "大学")


def stages_of(obj):
    """从 scope.学段 解析出学段集合，例如「初中至高中」-> {初中, 高中}。"""
    v = fm_nested(obj["fm"], "学段")
    return {s for s in STAGES if s in v}


def has_section(text, name):
    """是否存在**独立的** `## name` 标题（整行匹配）。

    **为什么不能用子串**：`## 变更记录X` 里包含 `## 变更记录`，
    于是把标题改个名就能让「必备小节」检查通过——注入样本实测过，确实拦不住。
    标题必须整行相等，后缀、加字、夹空格都不算。
    """
    return re.search(rf"^## {re.escape(name)}\s*$", text, re.M) is not None


def section_body(text, name):
    """取 `## name` 到下一个 `##` 之间的正文。"""
    m = re.search(rf"^##\s+{re.escape(name)}\s*$", text, re.M)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^##\s+", rest, re.M)
    return rest[:nxt.start()] if nxt else rest


# 论证 ID 形如 `### A1 · …` / `### M2 · …` / `### K3 · …`
ARG_ID = re.compile(r"^###\s+([A-Z]+\d+)\s*[·:：]", re.M)


def arg_ids(text):
    """取条目 `## 论证` 下的论证 ID 集合（小写）。

    英文译本用 `## Argument`（.en.md 不受 `REQUIRED_SECTIONS` 约束，章节名是英文），
    这里一并认——否则指向 .en.md 的 `#a1` 类锚点会误报「锚点不存在」。
    """
    body = section_body(text, "论证") or section_body(text, "Argument")
    return {x.lower() for x in ARG_ID.findall(body or "")}


# 论证标题/正文里表示「已被击倒」的字样
DEFEATED = re.compile(r"(被击倒|已击倒|已推翻|已失效)")
# 论证标题里声称「存活」的字样
CLAIMS_ALIVE = re.compile(r"[（(]\s*存活")


def arg_states(text):
    """返回 {id: {"title": 标题, "defeated": 是否标为被击倒, "alive": 是否自称存活}}。

    只读 `### <ID> · <标题>` 那一行，以及紧随其后到下一个标题之间的少量文字
    —— 因为「被击倒」这个判断通常写在标题里或 `- **状态**` 一行里。
    """
    body = section_body(text, "论证") or ""
    out = {}
    heads = list(ARG_ID.finditer(body))
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(body)
        chunk = body[m.start():end]
        # 标题行本身 + 前 12 行
        head_line = chunk.splitlines()[0] if chunk else ""
        blk = "\n".join(chunk.splitlines()[:14])
        out[m.group(1).lower()] = {
            "title": head_line.strip(),
            "defeated": bool(DEFEATED.search(head_line) or
                             re.search(r"\*\*状态\*\*\s*[:：]\s*\*\*(被击倒|已击倒)", blk)),
            "alive": bool(CLAIMS_ALIVE.search(head_line)),
        }
    return out


def check_argument_liveness(objects, warnings):
    """论证的「生存状态」与图上进边是否自洽。

    这一条是 `FORMAT.md` §6「论证被攻击 → 求存活集合 → 定状态」主链路的机械版本。
    它**不判断攻击本身**（那要人读），只报两种**结构上明显不对**的情形：

    1. `支持` 边指向一个**已被击倒**的论证 —— 那支撑是空的
    2. 论证自称**存活**，却**没有任何 `攻击` 边** —— 空集上的真空真命题

    > [!NOTE]
    > **曾经还有第三条：「`攻击` 边指向已被击倒的论证」——已删除。**
    >
    > 那条检查**给的是错的建议**：攻击边指向被它击倒的论证，
    > **本来就是攻击要做的事**。它被删掉，而不是被调低到「提示」，
    > 是因为**一个给错建议的检查比没有检查更糟**——它会训练人忽略提示。
    """
    inbound_support = collections.defaultdict(list)
    inbound_attack = collections.defaultdict(list)
    for rel, o in objects.items():
        for key, bucket in (("支持", inbound_support), ("攻击", inbound_attack)):
            for tgt in fm_links(o["fm"], key):
                anchor = tgt.split("#")[1].strip().lower() if "#" in tgt else ""
                r = resolve_link(o["path"], tgt)
                if r and anchor:
                    bucket[(r, anchor)].append(rel)

    for rel, o in objects.items():
        for aid, st in arg_states(o["text"]).items():
            sup = inbound_support.get((rel, aid), [])
            atk = inbound_attack.get((rel, aid), [])

            if st["defeated"] and sup:
                warnings.append(
                    f"{rel}: 论证 `{aid}` 已标为**被击倒**，却仍有 {len(sup)} 条 `支持` 边"
                    f"（如 {sup[0]}）—— 那些支撑是空的，应改指替代论证")
            if st["alive"] and not atk:
                warnings.append(
                    f"{rel}: 论证 `{aid}` 自称**存活**，但它**没有任何 `攻击` 边**"
                    f"—— 无攻击者时的「存活」是空转（FORMAT.md §6）")


def check_arguments(objects, errors):
    """`支持` / `攻击` 边必须落到**具体某个论证**上。

    这是本库的核心机制（论证被攻击 → 存活集合 → 状态），
    所以边不能只指向条目，必须带论证锚点。
    """
    for rel, o in objects.items():
        for key in ("支持", "攻击"):
            for tgt in fm_links(o["fm"], key):
                anchor = tgt.split("#")[1].strip().lower() if "#" in tgt else ""
                r = resolve_link(o["path"], tgt)
                dest = objects.get(r) if r else None
                if dest is None:
                    errors.append(f"{rel}: `{key}` 指向的不是知识对象 -> {tgt}（R-GRAPH-02）")
                    continue
                if not anchor:
                    errors.append(
                        f"{rel}: `{key}` 必须带论证锚点（如 `#a1`）-> {tgt}"
                        f"；只指向条目无法定位被攻击的是哪条论证（R-GRAPH-02）")
                    continue
                ids = arg_ids(dest["text"])
                if not ids:
                    errors.append(f"{rel}: `{key}` 指向的条目里没有可定位的论证 ID -> {tgt}（R-GRAPH-02）")
                elif anchor not in ids:
                    errors.append(
                        f"{rel}: `{key}` 的锚点 `#{anchor}` 在目标条目里不存在"
                        f"（该条目可用: {', '.join('#' + x for x in sorted(ids))}）（R-GRAPH-02）")

        # 同一条目内论证 ID 必须唯一
        raw = [x.lower() for x in ARG_ID.findall(section_body(o["text"], "论证") or "")]
        dup = [x for x, c in collections.Counter(raw).items() if c > 1]
        if dup:
            errors.append(f"{rel}: `## 论证` 里论证 ID 重复 {sorted(set(dup))}（R-GRAPH-02）")


def check_graph(objects, errors, warnings):
    """先修关系与教法归属的图校验 —— 这些是单看一个文件查不出来的。"""
    prereq = {}

    for rel, o in objects.items():
        t, fm, path = o["type"], o["fm"], o["path"]

        # 先修边只能连「知识点」
        for tgt in fm_links(fm, "先修"):
            r = resolve_link(path, tgt)
            dest = objects.get(r) if r else None
            # `路径` 是唯一例外：它的 `先修` 声明的是**路径外前置**——
            # 「这条路径要求你先会的东西，但本路径不教它」。
            # `check_paths` 一直靠这个字段判「先修缺口」不在路径内，
            # 而这条检查以前把它一并禁掉了：两条规则互相打架，
            # 只是此前所有路径的 `先修` 都写成 `[]`，从没撞上。
            if t not in ("知识点", "路径"):
                errors.append(
                    f"{rel}: 只有「知识点」（以及声明路径外前置的「路径」）可以有 `先修` 边"
                    f"（FORMAT.md §2），本条 type={t}（R-GRAPH-01）")
            if dest is None:
                errors.append(f"{rel}: `先修` 指向的不是知识对象 -> {tgt}（R-GRAPH-01）")
            elif dest["type"] != "知识点":
                errors.append(
                    f"{rel}: `先修` 必须指向「知识点」，实际指向 type={dest['type']} -> {tgt}（R-GRAPH-01）")
            else:
                prereq.setdefault(rel, []).append(r)
                # 跨学段先修边：允许，但要求作者显式认领（警告，不阻塞）
                a, b = stages_of(o), stages_of(dest)
                if a and b and not (a & b):
                    warnings.append(
                        f"{rel}: 跨学段先修边 —— 「{Path(rel).stem}」({'/'.join(sorted(a))}) "
                        f"先修「{Path(r).stem}」({'/'.join(sorted(b))})。"
                        f"请确认这是概念前置，而非「进阶」关系")

        # 教法必须有 knowledge_point，且指向「知识点」
        if t == "教法":
            kps = fm_links(fm, "knowledge_point")
            if not kps:
                errors.append(f"{rel}: 「教法」缺 `knowledge_point`（FORMAT.md §4）（R-SCHEMA-12）")
            for tgt in kps:
                r = resolve_link(path, tgt)
                dest = objects.get(r) if r else None
                if dest is None:
                    errors.append(f"{rel}: `knowledge_point` 指向的不是知识对象 -> {tgt}（R-SCHEMA-12）")
                elif dest["type"] != "知识点":
                    errors.append(
                        f"{rel}: `knowledge_point` 必须指向「知识点」，实际 type={dest['type']}（R-SCHEMA-12）")

    # 先修图环检测
    for n in list(prereq):
        prereq.setdefault(n, [])
    color, stack = {}, []

    def dfs(n):
        color[n] = 1
        stack.append(n)
        for m in prereq.get(n, []):
            if color.get(m) == 1:
                i = stack.index(m)
                errors.append("先修图存在环: " + " → ".join(
                    Path(x).stem for x in stack[i:] + [m]) + "（R-GRAPH-01）")
            elif color.get(m, 0) == 0:
                dfs(m)
        stack.pop()
        color[n] = 2

    for n in prereq:
        if color.get(n, 0) == 0:
            dfs(n)


def check_paths(objects, errors, warnings):
    """路径的先修缺口 + 跨学段提示。"""
    for rel, o in objects.items():
        if o["type"] != "路径":
            continue
        # **只看正文，不看 front-matter。**
        # `edges.先修` 里的链接是「路径外前置」的声明，不是「本路径引用了它」；
        # 早先按整篇扫链接，于是声明成路径外前置的概念又被当成路径内引用，
        # 进而要求它的先修也必须在路径内——路径外前置等于白声明，还会连锁报错。
        body = o["text"]
        fm = parse_front_matter(body)
        if fm:
            body = body[body.find("\n---", 3) + 4:]
        prose = re.sub(r"```.*?```", "", body, flags=re.S)

        refs = set()
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", prose):
            r = resolve_link(o["path"], target)
            dest = objects.get(r)
            if not dest:
                continue
            if dest["type"] == "知识点":
                refs.add(r)
            elif dest["type"] == "教法":
                # 路径通常引用「教法」；知识点要通过教法的 knowledge_point 才能连上
                for kp in fm_links(dest["fm"], "knowledge_point"):
                    kr = resolve_link(dest["path"], kp)
                    if kr and objects.get(kr, {}).get("type") == "知识点":
                        refs.add(kr)

        outside = set()
        for tgt in fm_links(o["fm"], "先修"):
            r = resolve_link(o["path"], tgt)
            if r:
                outside.add(r)

        for r in sorted(refs):
            for p in fm_links(objects[r]["fm"], "先修"):
                pr = resolve_link(objects[r]["path"], p)
                if pr and pr not in refs and pr not in outside:
                    errors.append(
                        f"{rel}: 先修缺口 —— 引用了「{Path(r).stem}」，"
                        f"但它的先修「{Path(pr).stem}」不在本路径内，也未声明为路径外前置")

        # 路径跨学段提示
        pstage = stages_of(o)
        for r in sorted(refs):
            kstage = stages_of(objects[r])
            if pstage and kstage and not (pstage & kstage):
                warnings.append(
                    f"{rel}: 路径跨学段 —— 路径为 {'/'.join(sorted(pstage))}，"
                    f"但引用了 {'/'.join(sorted(kstage))} 的知识点「{Path(r).stem}」")


def check_path_steps(objects, errors):
    """`路径` 的每个环节都必须连到一个**真实存在的知识对象**。

    **为什么要有这一条**：`FORMAT.md` §2 把 `路径` 定义为「**知识点的编排**」，
    但在此之前**没有任何检查要求环节连到东西**。

    实测过：一份「从进站到出站」的乘车流程（环节是**动作**，
    第 3、4 步的 `条目` 列只能写 `—`）**完全通过了校验**——
    它报了「缺 README」和「缺 `## 论证`」，**对环节全空一字未提**。

    **这条检查补的就是那个洞。** 它同时是「路径 = 教学编排」这个定义的机械版本：
    一个环节如果**指不出库里对应的东西**，它就不是这个库意义上的「环节」。
    """
    for rel, o in objects.items():
        if o["type"] != "路径":
            continue
        body = section_body(o["text"], "编排")
        if not body:
            continue
        for line in body.splitlines():
            s = line.strip()
            if not s.startswith("|"):
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) < 2:
                continue
            # 只认「第一格是序号」的数据行，跳过表头与分隔行
            if not re.fullmatch(r"\d+", cells[0]):
                continue
            step = cells[0]
            name = cells[1][:24]
            found = False
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", s):
                r = resolve_link(o["path"], target)
                if r and r in objects:
                    found = True
                    break
            if not found:
                errors.append(
                    f"{rel}: 第 {step} 步「{name}」**没有连到任何知识对象**"
                    f"（`条目` 列必须指向库里存在的条目）"
                    f"—— 路径是「知识点的编排」，指不出对象的步骤不是环节（R-GRAPH-04）")


PATH_COVERAGE = {}      # 路径 rel -> (已覆盖成果数, 声明成果数)


def path_outcome_stats(objects):
    """每条路径的成果覆盖：数量 + 两个「够不够」维度。**纯计算，不报错。**

    为什么要单独拎出来：`R-GRAPH-07` 原本只在终端打印提示——
    读者、agent 和任务清单都看不见「这条路径只有一个环节覆盖」。
    算一次、写进 `index.json`，同一条事实才能被所有下游用上
    （`scholia_search` 能看见，`make_tasks.py` 能派活，`docs/GAPS.md` 能统计）。

    返回 `{路径 rel: {声明, 已覆盖, 缺覆盖, 单环节, 证据薄, 深度上限, 覆盖外}}`。
    `声明` 为 0 表示这条路径没写 `outcomes`（覆盖度仍只能人工判断）。
    """
    ev = parse_evidence_index()
    out = {}
    for rel, o in objects.items():
        if o["type"] != "路径":
            continue

        m = re.search(r"^outcomes:\s*\n((?:[ \t]+.*\n?)*)", o["fm"], re.M)
        block = m.group(1) if m else ""
        declared = re.findall(r"\b(o\d+)\b", block)

        body = section_body(o["text"], "编排") or ""
        covered = set(re.findall(r"\b(o\d+)\b", body))

        steps = collections.Counter()
        depths = collections.defaultdict(list)
        for line in body.splitlines():
            s = line.strip()
            if not s.startswith("|"):
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) < 2:
                continue
            # 成果编号**不保证在最后一列**：`运动学入门-BL` 的表是
            # `# | 环节 | 条目 | 覆盖 | 时长`，覆盖在倒数第二列。
            # 只扫最后一列会让这条路径**报成「没有单环节覆盖」**——
            # 假干净比没检查更糟。所以扫全部单元格，链接也从任意单元格取。
            outs = []
            for c in cells:
                outs += re.findall(r"\b(o\d+)\b", c)
            outs = sorted(set(outs))
            if not outs:
                continue
            link = None
            for c in cells:
                mm = re.search(r"\[[^\]]*\]\(([^)#]+)", c)
                if mm:
                    link = mm.group(1)
                    break
            dest = resolve_link(o["path"], link) if link else None
            for oid in outs:
                steps[oid] += 1
                if dest and dest in objects:
                    for e in evidence_ids_of(objects[dest]["fm"]):
                        d = ev.get(e, {}).get("核验深度")
                        if d:
                            depths[oid].append(d)

        missing = [x for x in declared if x not in covered]
        thin = [x for x in declared if 0 < steps.get(x, 0) <= 1]
        unread = [x for x in declared if depths.get(x)
                  and max((DEPTH_RANK.get(d, 0) for d in depths[x])) <= DEPTH_RANK["仅定位"]]
        # 深度上限单独算：报告里「证据最高只到 —」看起来像**没数据**，
        # 而真相是「所有覆盖条目的证据都读到了 全文」——两者要让读者分得清。
        per_outcome_best = [max((DEPTH_RANK.get(d, 0) for d in depths[x]), default=0)
                            for x in declared if depths.get(x)]
        out[rel] = {
            "声明": len(declared),
            "已覆盖": len(declared) - len(missing),
            "缺覆盖": missing,
            "单环节": thin,
            "证据薄": unread,
            "深度上限": DEPTH_NAME.get(min(per_outcome_best), "") if per_outcome_best else "",
            "覆盖外": sorted(covered - set(declared)),
        }
    return out


def check_path_outcomes(objects, errors, warnings):
    """目标覆盖度 —— 从前是人工判断，这里改成机械校验。

    路径在 front-matter 声明 `outcomes`（可观测的学习成果，编号 o1/o2/…），
    并在 `## 编排` 表里为每个环节标注它覆盖哪些成果。校验器检查：
    每个声明的成果是否至少被一个环节覆盖。

    **「有没有」之外再算两个可查的维度**（这是「够不够」里**机器能算**的那部分，
    教学上够不够仍要人判）：

    1. **冗余度**：这个成果被**几个环节**覆盖。只有 1 个环节 = 一处讲砸就没有第二次机会
    2. **读没读过**：覆盖它的这些条目，其证据的**最高核验深度**
       （`仅定位` / `未核验` 的覆盖，说到底是「排了个位置」，不是「有依据地覆盖」）
    """
    data = path_outcome_stats(objects)
    stats = {}
    strength = {}
    for rel, d in data.items():
        if not d["声明"]:
            warnings.append(
                f"{rel}: 未声明 `outcomes` —— 目标覆盖度无法机械校验（仍是人工判断）")
            continue

        stats[rel] = (d["已覆盖"], d["声明"])
        PATH_COVERAGE[rel] = stats[rel]
        strength[rel] = (d["单环节"], d["证据薄"], d["深度上限"])

        if d["单环节"]:
            warnings.append(
                f"{rel}: 成果 {d['单环节']} **只由一个环节覆盖** —— "
                "覆盖度是「有没有」，冗余度是「够不够」的第一层（R-GRAPH-07）")
        if d["证据薄"]:
            warnings.append(
                f"{rel}: 成果 {d['证据薄']} 的覆盖条目**证据最高只到 `仅定位`/`未核验`** —— "
                "位置排上了，依据还没读过（R-GRAPH-07）")

        if d["缺覆盖"]:
            errors.append(
                f"{rel}: 目标覆盖度不足 —— 以下学习成果没有任何环节覆盖: "
                f"{d['缺覆盖']}（R-GRAPH-03）")
        if d["覆盖外"]:
            errors.append(
                f"{rel}: 编排里覆盖了未声明的成果编号: {d['覆盖外']}（R-GRAPH-03）")

    return stats, strength


def argument_graph(objects):
    """统计进边：每个条目被多少个**条目**支持 / 攻击。"""
    sup, atk = collections.Counter(), collections.Counter()
    for o in objects.values():
        for key, c in (("支持", sup), ("攻击", atk)):
            for tgt in fm_links(o["fm"], key):
                r = resolve_link(o["path"], tgt)
                if r:
                    c[r] += 1
    return sup, atk


def check_evidence_ids(objects, events, errors):
    """`evidence:` 里的编号必须真的登记在 `evidence/README.md` 里，且不能是已作废的。

    **为什么要有这一条**：本库曾经把 `ev-002`（后来判定为**构造数据**）当作
    全库等级最高的证据，并且有 26 条边指向它。**一个写错的编号不会被任何东西发现**——
    条目照样通过，读者照信。

    报两种：

    1. 编号**不在索引里** —— 多半是笔误，也可能是引用了不存在的证据
    2. 编号**已被标为作废** —— 引用作废证据等于把撤回过的东西再拿回来用

    知识对象与 `事件` 都查（事件只有证据，编号写错同样要拦住）。
    """
    index = ROOT / "evidence" / "README.md"
    if not index.exists():
        return
    text = index.read_text(encoding="utf-8")
    known, void = set(), set()
    for line in text.splitlines():
        m = re.match(r"\s*\|\s*(ev-\d+)\s*\|\s*([^|]*)\|", line)
        if not m:
            continue
        known.add(m.group(1).lower())
        if "已作废" in m.group(2) or "作废" in m.group(2):
            void.add(m.group(1).lower())

    for rel, o in {**objects, **events}.items():
        own = {x.lower() for x in evidence_ids_of(o["fm"])}
        ext = {x.lower() for x in external_source_ids(o["fm"])} - own
        for ev in sorted(own):
            if ev not in known:
                errors.append(f"{rel}: `evidence` 引用了索引里没有的编号 -> {ev}（R-EVID-01）")
            elif ev in void:
                errors.append(
                    f"{rel}: `evidence` 引用了**已作废**的编号 -> {ev}"
                    f"（作废的证据不能再来支撑结论）（R-EVID-01）")
        for ev in sorted(ext):
            if ev not in known:
                errors.append(
                    f"{rel}: `外部先修.来源` 引用了索引里没有的编号 -> {ev}（R-EVID-01）")
            elif ev in void:
                errors.append(
                    f"{rel}: `外部先修.来源` 引用了**已作废**的编号 -> {ev}"
                    f"（作废的证据不能再来声明前置）（R-EVID-01）")


def check_external_prereqs(objects, errors, warnings):
    """R-SCHEMA-20：可选字段 `外部先修` 的形状、枚举、来源格式与复发提示。

    **它只管「声明得是否完整」，不管「这个前置是否真的必需」。**
    后者是内容判断，和 `M-03` 一样留给人；本字段的价值是把「库里没有 X 节点，
    但 N 个条目都需要它」从**正文里的一句备注**变成**可查询、可计数的声明**。

    报错（阻塞）：
    - `外部先修:` 声明了却没有任何列表项；
    - 列表项缺五个子字段之一、出现未知子字段、同一项重复子字段；
    - `标识` 不是 `[a-z0-9][a-z0-9-]*`，或在同一条目里重复；
    - `学段` 不是枚举值；
    - `来源` 不是单个 `ev-###`（编号是否存在/作废由 `R-EVID-01` 管）。

    提示（不阻塞）：
    - 同一个 `标识` 在 ≥2 个对象里出现 —— 「该考虑建节点」；
    - 同一个 `名称` 配了不同 `标识` —— 可能是同一前置被写成了两个键；
    - `学科` 不在本库已登记的学科里 —— 不阻塞（库外前置本来就可能来自未收录学科），
      但要求确认不是笔误。
    """
    seen = collections.defaultdict(list)      # 标识 -> [(rel, 名称)]
    names = collections.defaultdict(set)      # 名称 -> {标识}
    for rel, o in sorted(objects.items()):
        found, raw, problems = _parse_external_block(o["fm"])
        for line, msg in problems:
            errors.append(f"{rel}: {msg}（front-matter 第 {line} 行）（R-SCHEMA-20）")
        if not found:
            continue
        if not raw and not problems:
            errors.append(
                f"{rel}: `外部先修` 声明了却没有任何条目 —— "
                "没有库外前置就删掉这个字段；有就写成缩进列表（R-SCHEMA-20）")
        local_ids = set()
        for e in raw:
            f = {k: _clean_external_value(v) for k, v in e["fields"].items()}
            line = e["line"]
            unknown = [k for k in f if k not in EXTERNAL_PREREQ_FIELDS]
            missing = [k for k in EXTERNAL_PREREQ_FIELDS if not f.get(k)]
            if unknown:
                errors.append(
                    f"{rel}: `外部先修` 第 {line} 行有未知子字段 {unknown} —— "
                    f"只允许 {list(EXTERNAL_PREREQ_FIELDS)}（R-SCHEMA-20）")
            if missing:
                errors.append(
                    f"{rel}: `外部先修` 第 {line} 行缺子字段 {missing} —— "
                    "五项都要写：名称 / 标识 / 学科 / 学段 / 来源（R-SCHEMA-20）")
                continue
            key, name = f["标识"], f["名称"]
            if not EXTERNAL_PREREQ_ID.fullmatch(key):
                errors.append(
                    f"{rel}: `外部先修.标识` 必须是 ASCII 稳定键 "
                    f"`[a-z0-9][a-z0-9-]*` -> {key!r}（R-SCHEMA-20）")
            if key in local_ids:
                errors.append(
                    f"{rel}: `外部先修.标识` 在同一条目里重复 -> {key!r}（R-SCHEMA-20）")
            local_ids.add(key)
            if f["学段"] not in ALLOWED_STAGES:
                errors.append(
                    f"{rel}: `外部先修.学段` 取值非法 -> {f['学段']!r}"
                    "（允许 小学/初中/高中/大学/不限，单个值）（R-SCHEMA-20）")
            if not EXTERNAL_PREREQ_SOURCE.fullmatch(f["来源"]):
                errors.append(
                    f"{rel}: `外部先修.来源` 必须是单个 `ev-###` -> {f['来源']!r}"
                    "（R-SCHEMA-20）")
            if f["学科"] not in SUBJECT_SLUGS:
                warnings.append(
                    f"{rel}: `外部先修.学科` = {f['学科']!r} 不在本库已登记的学科里 —— "
                    "库外前置可以来自未收录学科，但请确认不是笔误（R-SCHEMA-20）")
            if key and name:
                seen[key].append((rel, name))
                names[name].add(key)

    for key, uses in sorted(seen.items()):
        rels = sorted({rel for rel, _ in uses})
        if len(rels) < 2:
            continue
        shown = "、".join(Path(r).stem for r in rels)
        warnings.append(
            f"`外部先修` 标识 `{key}` 出现在 {len(rels)} 个条目（{shown}）—— "
            "同一个前置反复出现，考虑为它建一个知识点节点（R-SCHEMA-20）")

    for name, keys in sorted(names.items()):
        if len(keys) > 1:
            warnings.append(
                f"`外部先修.名称` {name!r} 配了 {len(keys)} 个不同标识 "
                f"{sorted(keys)} —— 若指同一个前置，请统一 `标识`（R-SCHEMA-20）")


def check_readme_coverage(objects, errors):
    """每个知识对象都必须在**它所属学科的 README** 里被提到。

    **为什么要有这一条**：本库的 `物理/README.md` 是读者进库后的第一张表。
    它**漏过两次**——一次是 5 条 `教法`（被一次对抗审查发现），
    一次是 9 条（第 4 批 5 条 + 第 5 批 4 条，**我自己写完忘了登记**）。

    **索引不会自己追上内容。** 这一条把它变成机械可查的：
    文件名（`<name>.md`）必须出现在 `knowledge/<subject>/README.md` 里。
    """
    for rel, o in objects.items():
        parts = Path(rel).parts
        if len(parts) < 3 or parts[0] != "knowledge":
            continue
        subject_readme = ROOT / parts[0] / parts[1] / "README.md"
        if not subject_readme.exists():
            errors.append(f"{rel}: 所属学科缺少 README -> knowledge/{parts[1]}/README.md（R-README-01）")
            continue
        if o["path"].name not in subject_readme.read_text(encoding="utf-8"):
            errors.append(
                f"{rel}: **学科 README 里没有登记它**"
                f"（`knowledge/{parts[1]}/README.md` 必须提到 `{o['path'].name}`）"
                "（R-README-01）")


# ── 链接锚点 ──────────────────────────────────────────────────────────────
_TEXT_CACHE = {}


def _repo_text(rel):
    if rel not in _TEXT_CACHE:
        p = ROOT / rel
        _TEXT_CACHE[rel] = (p.read_text(encoding="utf-8").replace("\r\n", "\n")
                            if p.exists() else "")
    return _TEXT_CACHE[rel]


def slugify(heading):
    t = re.sub(r"[*`]", "", heading.strip()).lower()
    t = re.sub(r"[^\w\- ]", "", t)
    return t.replace(" ", "-")


def heading_slugs(text):
    seen, out = {}, set()
    for line in text.splitlines():
        m = re.match(r"^#{1,6}\s+(.*)$", line)
        if m:
            s = slugify(m.group(1))
            n = seen.get(s, 0)
            out.add(s if n == 0 else f"{s}-{n}")
            seen[s] = n + 1
    return out


def anchor_ok(rel, anchor):
    """锚点要么是一个标题 slug，要么是一个论证 ID（如 `a1`）。"""
    if anchor.lower() in heading_slugs(_repo_text(rel)):
        return True
    return anchor.lower() in {a.lower() for a in arg_ids(_repo_text(rel))}


# ── 单对象规则（此前只写在 FORMAT.md 里，没有机械检查）─────────────────────

def evidence_ids_of(fm):
    """取**对象自己的** `evidence` 编号（不含 `外部先修.来源`）。

    `外部先修` 也有 `来源: ev-###`，所以**不能**再对整个 front-matter 做
    `re.findall("ev-\\d+")`：那会把「前置的来源」算成本条的论证证据，
    进而污染 `citations.json`、`R-EVID-03` 与中英译本的一致性比对。

    行内 `[ev-001, ev-002]` 与块列表都认——块列表是 YAML 的合法写法，
    早先只认行内，会把块写法误报成「无来源」。
    """
    m = re.search(r"^evidence:[ \t]*(.+)$", fm, re.M)
    if m and m.group(1).strip():
        return re.findall(r"ev-\d+", m.group(1))
    b = re.search(r"^evidence:[ \t]*\n((?:[ \t]+.*\n?)*)", fm, re.M)
    return re.findall(r"ev-\d+", b.group(1)) if b else []


def check_evidence_nonempty(objects, errors):
    """**无来源不入库**。`evidence: []` 不算有来源。"""
    for rel, o in objects.items():
        if not evidence_ids_of(o["fm"]):
            errors.append(
                f"{rel}: `evidence` 为空 —— 本库「无来源不入库」，"
                "每个对象至少引一条证据（FORMAT.md §3）（R-SCHEMA-04）")


def check_knowledge_tip(objects, errors):
    """`知识点` 正文第一行必须是「读完你会什么」的 `> [!TIP]`。"""
    for rel, o in objects.items():
        if o["type"] != "知识点":
            continue
        after = o["text"].split("---\n", 2)[-1]
        first = next((ln.strip() for ln in after.splitlines() if ln.strip()), "")
        if not first.startswith("> [!TIP]"):
            errors.append(
                f"{rel}: `知识点` 正文第一行必须是 `> [!TIP]`（读完你会什么）（R-SCHEMA-06）")


def check_teaching_level(objects, errors):
    """`教法` 必须有 `scope.水平档`；值是档位代码（可多档）或「不分档」。"""
    for rel, o in objects.items():
        if o["type"] != "教法":
            continue
        lv = fm_nested(o["fm"], "水平档")
        if not lv:
            errors.append(
                f"{rel}: `教法` 缺 `scope.水平档`（BL / OL / AL 组合，"
                "或跨全部档位的「不分档」）（R-SCHEMA-13）")
            continue
        codes = set(re.findall(r"\b(BL|OL|AL)\b", lv))
        if LEVEL_UNDIVIDED not in lv and not codes:
            errors.append(f"{rel}: `水平档` 无法识别 -> {lv!r}（R-SCHEMA-13）")


def check_medical(objects, errors):
    """医学条目必须有 `scope.条件`，且正文开头是免责 `> [!CAUTION]` 块。

    见 `knowledge/medicine/README.md`「边界的一次修正（2026-10-12）」：
    指南原文的规定可以收录，但必须带人群限定与免责，且以「指南规定了 X」表述。
    """
    for rel, o in objects.items():
        if "医学" not in fm_nested(o["fm"], "学科"):
            continue
        if not fm_nested(o["fm"], "条件"):
            errors.append(f"{rel}: 医学条目必须有 `scope.条件`（人群与限定）（R-SCHEMA-14）")
        head = o["text"].split("\n## ", 1)[0]
        if "> [!CAUTION]" not in head:
            errors.append(
                f"{rel}: 医学条目正文开头必须有 `> [!CAUTION]` 免责块（R-SCHEMA-14）"
                "（人群限定 + 非医疗建议）")


def check_stage(objects, errors):
    """`scope.学段` 只能用枚举值，组合用「至」。"""
    for rel, o in objects.items():
        v = fm_nested(o["fm"], "学段")
        if not v:
            errors.append(f"{rel}: 缺 `scope.学段`（R-SCHEMA-07）")
            continue
        for part in re.split(r"[至、,，]", v):
            part = part.strip()
            if part and part not in ALLOWED_STAGES:
                errors.append(
                    f"{rel}: `学段` 取值非法 -> {v!r}（R-SCHEMA-07）"
                    "（允许 小学/初中/高中/大学/不限，组合用「至」）")


def check_dates(objects, errors):
    for rel, o in objects.items():
        c, u = fm_value(o["fm"], "created"), fm_value(o["fm"], "updated")
        ok = True
        for k, val in (("created", c), ("updated", u)):
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(val or "")):
                errors.append(f"{rel}: `{k}` 必须是 YYYY-MM-DD -> {val!r}（R-SCHEMA-08）")
                ok = False
        if ok and u < c:
            errors.append(f"{rel}: `updated`（{u}）早于 `created`（{c}）（R-SCHEMA-18）")


def check_author(objects, errors):
    for rel, o in objects.items():
        a = (fm_value(o["fm"], "author") or "").strip().strip('"')
        if not a:
            errors.append(f"{rel}: 缺 `author`（不可匿名）（R-SCHEMA-09）")
        elif not (a.startswith("@") or a.startswith("AI")):
            errors.append(
                f"{rel}: `author` 应形如 `@handle` 或 "
                f"`AI（模型）· 经 @某人复核 · 日期` -> {a!r}（R-SCHEMA-09）")


def check_section_order(objects, errors):
    """必备小节的**顺序**固定（FORMAT.md §1.3）。此前只查存在，没查顺序。"""
    for rel, o in objects.items():
        order = REQUIRED_SECTIONS[o["type"]]
        pos = []
        for sec in order:
            m = re.search(rf"^## {re.escape(sec)}\s*$", o["text"], re.M)
            pos.append(m.start() if m else -1)
        if all(p >= 0 for p in pos) and pos != sorted(pos):
            errors.append(
                f"{rel}: 必备小节顺序应为 {' · '.join(order)}（FORMAT.md §1.3）（R-SCHEMA-05）")


def check_readme_path_numbers(objects, errors):
    """`路径` 在学科 README 表格里手写的「覆盖度 X/Y」必须与**实际算出来的**一致。

    这张表是手写的，每给路径加一步就会旧一次——加一步、忘记改 README，
    于是页面说 5/5 而实际已经 6/6。**数字和实际不符时，读者信的是页面。**
    """
    import re as _re
    for rel, (got, total) in PATH_COVERAGE.items():
        p = ROOT / rel
        rp = p.parent.parent / "README.md"
        if not rp.exists():
            continue
        name = p.name
        for line in rp.read_text(encoding="utf-8").split(chr(10)):
            if name not in line or "覆盖度" not in line:
                continue
            m = _re.search(r"覆盖度\s*\*{0,2}(\d+)\s*/\s*(\d+)", line)
            if m and (int(m.group(1)), int(m.group(2))) != (got, total):
                errors.append(
                    f"{rp.relative_to(ROOT).as_posix()}: 「{name}」的覆盖度写成 "
                    f"{m.group(1)}/{m.group(2)}，实际是 {got}/{total}"
                    f"（R-README-03）")


def check_status_docs(errors):
    """状态词表写了好几处，最容易漏。要求人类文档列全（FORMAT.md §4 + 学科图例）。"""
    all_status = set()
    for s in ALLOWED_STATUS.values():
        all_status |= s
    for rel in ("FORMAT.md", "knowledge/README.md"):
        text = _repo_text(rel)
        missing = sorted(s for s in all_status if s not in text)
        if missing:
            errors.append(f"{rel}: 状态图例不全，缺 {missing}（R-DOC-01）")


def check_rule_registry(errors):
    """R-DOC-02：中英两份规则注册表必须覆盖同一组 ID，且各自没有重复。

    这两张表生成 `docs/RULES.md` / `docs/RULES.en.md`。多一行、少一行，
    生成结果看上去都「有规则」——只有把 ID 集合对起来，才会发现英文页少了
    四条、中文页把一条英文描述粘进了中文表。规则表是**规范的目录**，
    目录缺项比正文缺项更难发现，因为读者不知道缺了什么。
    """
    for label, rules in (("MECH_RULES", MECH_RULES), ("MECH_RULES_EN", MECH_RULES_EN),
                         ("MANUAL_RULES", MANUAL_RULES), ("MANUAL_RULES_EN", MANUAL_RULES_EN)):
        ids = [rid for rid, _ in rules]
        dup = sorted({r for r in ids if ids.count(r) > 1})
        if dup:
            errors.append(f"{label}: 规则 ID 重复 {dup}（R-DOC-02）")
    for label, zh, en in (("机械校验", MECH_RULES, MECH_RULES_EN),
                          ("人工复核", MANUAL_RULES, MANUAL_RULES_EN)):
        a, b = {r for r, _ in zh}, {r for r, _ in en}
        if a != b:
            errors.append(
                f"{label}规则中英不一致：仅中文 {sorted(a - b)}，仅英文 {sorted(b - a)}（R-DOC-02）")


def check_license(objects, errors):
    """知识内容统一 CC BY-SA 4.0（见 LICENSE）。"""
    for rel, o in objects.items():
        v = (fm_value(o["fm"], "license") or "").strip()
        if v != ALLOWED_LICENSE:
            errors.append(f"{rel}: `license` 必须是 {ALLOWED_LICENSE} -> {v!r}（R-SCHEMA-10）")


def check_id_prefix(objects, errors):
    """`id` 前缀必须与学科一致（防止跨学科编号漂移）。"""
    for rel, o in objects.items():
        subj = (fm_nested(o["fm"], "学科") or "").split()
        subj = subj[0] if subj else ""
        slug = SUBJECT_SLUGS.get(subj)
        if not slug:
            errors.append(f"{rel}: 未知 / 缺失学科 -> {subj!r}（见 SUBJECT_SLUGS）（R-SCHEMA-11）")
            continue
        i = fm_value(o["fm"], "id") or ""
        if not i.startswith(f"kb:{slug}:"):
            errors.append(
                f"{rel}: `id` 前缀应与学科一致（`kb:{slug}:…`）-> {i!r}（R-SCHEMA-11）")


def check_type_dir(objects, errors):
    """R-SCHEMA-16：文件所在目录必须与 `type` 对应。

    目录名是英文之后（`concepts/` `claims/` `methods/` …），**目录和 `type` 是同一件事的两种写法**：
    一个 `命题` 落在 `methods/` 里，读者按目录找东西就会找错，而单看文件内容完全合法。
    这条只有在「目录名有语义」的前提下才有意义——中文目录那次改造之前它无法成立。
    """
    want = {"知识点": "concepts", "命题": "claims", "教法": "methods",
            "误解": "misconceptions", "路径": "paths", "资源": "resources"}
    for rel, o in sorted(objects.items()):
        parts = Path(rel).parts
        if len(parts) < 3 or parts[0] != "knowledge":
            continue
        expect = want.get(o["type"])
        if expect and parts[2] != expect:
            errors.append(f"{rel}: type={o['type']} 应放在 `{expect}/` 下，"
                          f"实际在 `{parts[2]}/`（R-SCHEMA-16）")


def check_doc_bilingual(errors):
    """R-BILING-03：**文档类**文件必须有同名 `.en.md`。

    条目级的双语由 `R-BILING-01` 管；但规范、入口、索引这些「文档」此前只靠 `M-10` 的人工约定——
    结果它们真的缺了英文（`knowledge/README` 与覆盖度页长期只有中文，`AGENTS` 则是**内联双语**，
    与「一个文档两份文件」的约定不一致）。

    **豁免**（写清理由，不靠默契）：
    - `templates/*.md`：骨架是中文写给人抄的，翻译一份没有读者；
    - `.github/*`：Issue / PR 模板由 GitHub 渲染，双语会挤在表单里。

    生成的规则表、索引等由 `R-INDEX-01/02` 管，不在此列。
    """
    targets = ["AGENTS.md", "README.md", "START.md", "FORMAT.md", "CONTRIBUTING.md",
               "knowledge/README.md", "evidence/README.md", "events/README.md",
               "docs/RULES.md", "docs/decisions/README.md",
               "knowledge/physics/coverage/README.md"]
    for d in sorted(set(SUBJECT_DIRS.values())):
        targets.append(f"knowledge/{d}/README.md")
    for rel in targets:
        p = ROOT / rel
        if not p.exists():
            continue
        if not (p.parent / (p.stem + ".en.md")).exists():
            errors.append(f"{rel}: 缺英文译本 -> 应为 {p.stem}.en.md（R-BILING-03；"
                          f"templates/ 与 .github/ 豁免）")


def check_evidence_table(errors):
    """证据表的 `类别` / `等级` / `核验深度` 必须是枚举值（作废行除外）。"""
    for ev, r in parse_evidence_index().items():
        if r["作废"]:
            continue
        if r["类别"] not in EVIDENCE_CATEGORIES:
            errors.append(f"evidence/README.md: {ev} 类别非法 -> {r['类别']!r}（R-EVID-02）")
        if r["等级"] not in EVIDENCE_GRADES:
            errors.append(f"evidence/README.md: {ev} 等级非法 -> {r['等级']!r}（R-EVID-02）")
        if r["核验深度"] not in EVIDENCE_DEPTHS:
            errors.append(f"evidence/README.md: {ev} 核验深度非法 -> {r['核验深度']!r}（R-EVID-02）")


# `未核验`（没打开过）与 `仅定位`（打开了但没读）都撑不起「确认」。
UNREAD_DEPTHS = {"未核验", "仅定位"}
CONFIRMING_STATUSES = ("暂定确认", "已确证")


def check_evidence_verified_support(objects, errors):
    """`暂定确认` / `已确证` 必须至少有**一条读过的**证据。

    **防的是「来源本身是被人造出来的」**：一个格式完全合法的定位
    只能证明**它在那儿**，证明不了**它说了什么**——
    洗稿站、仿冒页、为这次引用新造的站点，定位全都合法。
    `未核验` = 从没打开；`仅定位` = 打开了但没读正文。
    **两条都不能单独把状态推到「确认」。**

    **误报处理**：若一个 `资源` 只主张「该文件存在于该地址」，
    把核验深度补成 `全文`/`摘要`（读一遍），或让条目停在 `待审`/`有效`。
    """
    ev = parse_evidence_index()
    for rel, o in objects.items():
        st = fm_value(o["fm"], "status")
        if st not in CONFIRMING_STATUSES:
            continue
        ids = evidence_ids_of(o["fm"])
        known = {e: ev[e] for e in ids if e in ev and not ev[e]["作废"]}
        if not known:
            continue                      # 缺编号 / 作废由 R-EVID-01 管
        if all(r["核验深度"] in UNREAD_DEPTHS for r in known.values()):
            detail = " · ".join(f"{e}={r['核验深度']}" for e, r in known.items())
            errors.append(
                f"{rel}: `status` 是「{st}」，但它的证据**没有一条读过**"
                f"（{detail}）—— 没读过就不能说「确认」；"
                "把核验深度补成 `全文`/`摘要`，或把状态退回 `待审`（R-EVID-03）")


# ── 生成块：人类文档里的数字/清单，唯一来源是本脚本 ────────────────────────
GENERATED_BEGIN = "<!-- kbcheck:begin -->"
GENERATED_END = "<!-- kbcheck:end -->"

SUBJECT_ORDER = ["物理", "生活", "医学", "地理", "科学",
                 "交通", "计算机", "经济", "法律", "数学"]
TYPE_ORDER = ["教法", "知识点", "命题", "误解", "资源", "路径"]
TYPE_EN = {"教法": "methods", "知识点": "concepts", "命题": "claims",
           "误解": "misconceptions", "资源": "resources", "路径": "paths"}
SUBJECT_EN = {"物理": "Physics", "生活": "Life", "医学": "Medicine",
              "地理": "Geography", "科学": "Science",
              "交通": "Transport", "计算机": "Computing", "经济": "Economics",
              "法律": "Law", "数学": "Mathematics"}

# ── 规则注册表：每条规则一个 ID，分「机械校验」与「人工复核」──────────────
# 改了任何一条规则，**必须同时改这里的清单与对应的检查**——否则 R-INDEX-02 会失败。
# 这就是「规则即代码」：规则不再散在散文里，而是可枚举、可校验的清单。
def check_status_has_argument(objects, errors):
    """R-SCHEMA-17：说了「核对过」的状态，必须有论证撑着。

    FORMAT §6 把状态定义为「存活论证集合算出来的结果」。但在此之前，**空集也能算出状态**：
    一条命题写上 `暂定确认`、`## 论证` 里（尚无论证），校验全绿。
    那等于把整套「证据 + 反驳」的机制留了一个后门——**状态可以宣称一件没发生的事**。
    空集只能对应「待审」（从未论证）或「失据」（曾有论证被击倒），而后者本身也必须有论证。
    """
    need = {"暂定确认", "已确证", "失据", "已推翻"}
    for rel, o in sorted(objects.items()):
        st = fm_value(o["fm"], "status")
        if st in need and not arg_ids(o["text"]):
            errors.append(
                f"{rel}: status=「{st}」，但 `## 论证` 里一条论证都没有 —— "
                f"「{st}」必须由存活（或被击倒）的论证算出来；空集请写「待审」（R-SCHEMA-17）")


def inbound_edge_map(objects, key):
    """入边表：`{被指向的条目: [(指向它的条目, 锚点), …]}`。

    `支持` / `攻击` 的语义是**入边**——条目自己写了什么不算，要看在库里有谁指向它。
    单看一个文件永远查不出「这条被几条边指着」，所以统一在这里算一次。
    """
    out = collections.defaultdict(list)
    for rel, o in objects.items():
        for tgt in fm_links(o["fm"], key):
            r = resolve_link(o["path"], tgt)
            if not r:
                continue
            anchor = tgt.split("#")[1].strip().lower() if "#" in tgt else ""
            out[r].append((rel, anchor))
    return out


def check_status_reachability(objects, errors):
    """R-SCHEMA-19：`已确证` / `争议` / `已推翻` 必须有**结构上的依据**，不能只改一个字段。

    这三个状态全库目前是 **0 条**。0 不是问题——问题是**从 0 到「写了就通过」以前没有门槛**：
    把 `status:` 手动改成「已确证」，其余什么都不用动，校验照样全绿。
    **本库最难拿到的状态，变成了一个字段值。**

    现在每个状态各要求一个**机器能查**的前提（必要，**不是**充分；人该判的仍然写 M-07）：

    | 状态 | 机器要求 | 人仍然要判 |
    |---|---|---|
    | `已确证` | 两条通道**之一**：①`author` 与「变更记录」里 **≥2 个不同 `@` 署名**；②`## 复核记录` 四栏齐全（模型 · 日期 · 引文核验 · 限制）。**两条通道都要求**引用的每份证据读到 `全文` | 记录里说的核验是否**真的发生过**（M-07） |
    | `争议` | ≥2 条论证 **且** ≥1 条**入边 `攻击`** | 两个存活论证的结论是否**真的冲突** |
    | `已推翻` | ≥1 条**未被击倒**的入边 `攻击` | 攻击方自己站不站得住 |

    **为什么 `争议` 也要攻击边**：没有攻击边的「争议」和没有攻击者的「存活」是同一个毛病
    （见 `check_argument_liveness`）——**冲突必须在图上看得见**，否则它只是作者的一句心情。
    """
    atk_in = inbound_edge_map(objects, "攻击")
    evidence = parse_evidence_index()
    for rel, o in sorted(objects.items()):
        st = fm_value(o["fm"], "status")
        if st == "已确证":
            # 两条署名通道（2026-11-05 决定）：**人或 agent 都可以复核**。
            # 机器只查「署名/记录在不在」，判断仍归 M-07。
            names = set(re.findall(r"@([\w][\w.\-]*)", fm_value(o["fm"], "author") or ""))
            names |= set(re.findall(r"@([\w][\w.\-]*)", section_body(o["text"], "变更记录") or ""))
            body = section_body(o["text"], AGENT_REVIEW_SECTION) or ""
            missing = [f for f in AGENT_REVIEW_FIELDS if f not in body] if body.strip() else None
            record_ok = bool(body.strip()) and not missing
            if len(names) < 2 and not record_ok:
                if body.strip() and missing:
                    errors.append(
                        f"{rel}: status=「已确证」，`## {AGENT_REVIEW_SECTION}` 缺 {missing} —— "
                        f"记录要答得上「谁审的（模型）· 什么时候（日期）· 引文核了几条（引文核验）· "
                        f"哪些判不了（限制）」（R-SCHEMA-19）")
                else:
                    errors.append(
                        f"{rel}: status=「已确证」，但既没有第二名复核者的 `@` 署名，"
                        f"也没有 `## {AGENT_REVIEW_SECTION}` —— `已确证` 必须能追到**是谁核的**："
                        "在「变更记录」里写下复核者（人），或留一份四栏记录（agent）"
                        "（R-SCHEMA-19）")
            ids = evidence_ids_of(o["fm"])
            shallow = [e for e in ids
                       if not evidence.get(e) or evidence[e].get("作废")
                       or evidence[e].get("核验深度") != "全文"]
            if shallow:
                detail = "、".join(
                    f"{e}（{'索引里没有' if not evidence.get(e) else evidence[e].get('核验深度')}）"
                    for e in shallow[:4])
                errors.append(
                    f"{rel}: status=「已确证」，但引用的证据没有全部读到 `全文` —— {detail}。"
                    "确证的前提是**每一份来源都通读过**（溯源 T4）：没读透就说「复核过」，"
                    "复核的只是自己脑子里那版（R-SCHEMA-19）")
        elif st == "争议":
            n_args = len(arg_ids(o["text"]))
            if n_args < 2 or not atk_in.get(rel):
                errors.append(
                    f"{rel}: status=「争议」，但它有 {n_args} 条论证、"
                    f"{len(atk_in.get(rel, []))} 条入边 `攻击` —— "
                    "「争议」= 存活论证**结论冲突**，冲突必须落在图上：至少 2 条论证、"
                    "且至少 1 条指向本条某论证的 `攻击` 边（R-SCHEMA-19）")
        elif st == "已推翻":
            live = [(a, anc) for (a, anc) in atk_in.get(rel, [])
                    if fm_value(objects[a]["fm"], "status") not in NOT_CITABLE]
            if not live:
                errors.append(
                    f"{rel}: status=「已推翻」，但没有任何**未被击倒**的入边 `攻击` —— "
                    "推翻要由站得住的攻击产生；只是「支撑被拆掉」请写 `失据`（R-SCHEMA-19）")


def evidence_origin(rec):
    """一条证据的**来源标识** = 定位文本里「发布主体 + 作品」那一段。

    这只是**对定位字符串的一种切法**，不是对内容的判断：
    切出来相同 → 同一本书 / 同一份文件（同一来源，**可证**）；
    切出来不同 → **不代表**独立（两本书可能同一套编委）；
    切不出来 → `（未识别）`，**未识别不等于独立**，要人补（M-03）。
    """
    loc = (rec or {}).get("定位", "") or ""
    m = re.search(r"^\s*(.{0,40}?《[^》]+》)", loc)
    if m:
        return m.group(1).strip()
    m = re.search(r"^\s*([A-Za-z0-9][\w.\- ]{1,40}?)[，、·（(]", loc)
    if m:
        return m.group(1).strip()
    return ""


def check_support_homology(objects, warnings):
    """R-GRAPH-06：同一论证上的多条 `支持`，**共享的是几份证据、几个来源**。

    「15 条支持」被写强度写过一次（见 docs/decisions/support-count-not-strength.md），
    而「同一来源的多个观测不等于多份证据」在本库已经**撞过两次**
    （`ev-002` 与「类比按学段」）。

    原来说「独立性算不出来（来源是自由文本）」——**其中一半其实算得出来**：
    几条边的证据**编号并集**、以及它们的**来源标识是否同一个**，都是定位文本上的结构事实。
    算不出来的只剩「同一出版方的两份材料算不算独立」，那留给人（M-03）。

    - ≥2 条 `支持` 边、证据并集只有 **0 或 1 个编号** → 提示：条数不构成强度
    - ≥2 条 `支持` 边、但**来源标识只有一个** → 提示：这些边指向**同一份材料**
    - 其余情况只**如实列出**编号、来源标识与类别，把判断留给人

    提示不阻塞：多条边来自同一来源**是合法的**，只是不能被读成多份印证。
    """
    ev = parse_evidence_index()
    sup_in = inbound_edge_map(objects, "支持")
    report = []
    for rel, edges in sorted(sup_in.items()):
        if len(edges) < 2:
            continue
        groups = collections.defaultdict(set)
        for src, anchor in edges:
            groups[anchor or "（无锚点）"].add(tuple(sorted(evidence_ids_of(objects[src]["fm"]))))
        for anchor, evsets in sorted(groups.items()):
            ids = sorted({e for s in evsets for e in s})
            origins = collections.Counter()
            unknown = 0
            for e in ids:
                o_ = evidence_origin(ev.get(e))
                if o_:
                    origins[o_] += 1
                else:
                    unknown += 1
            cats = collections.Counter(ev.get(e, {}).get("类别", "（未登记）") for e in ids)
            obits = " · ".join(f"{k}×{v}" for k, v in sorted(origins.items())) or "（未识别）"
            cbits = " · ".join(f"{k}×{v}" for k, v in sorted(cats.items()))
            if len(ids) <= 1:
                warnings.append(
                    f"{rel}: 论证 `{anchor}` 有 {len(edges)} 条 `支持` 边，"
                    f"但证据并集只有 {ids or ['（无 evidence）']} —— "
                    f"这些边**不是独立印证**，条数不代表强度（R-GRAPH-06）")
            elif len(origins) == 1 and not unknown:
                warnings.append(
                    f"{rel}: 论证 `{anchor}` 有 {len(edges)} 条 `支持` 边、{len(ids)} 份证据，"
                    f"但来源标识只有 **1 个**（{next(iter(origins))}）—— "
                    f"它们是**同一份材料的 {len(ids)} 个位置**，不是 {len(ids)} 份独立证据（R-GRAPH-06）")
            report.append((rel, anchor, len(edges), ids, len(origins) + (1 if unknown else 0),
                            obits + (f" · （未识别）×{unknown}" if unknown else ""), cbits))
    return report


def check_updated_matches_changelog(objects, errors):
    """R-SCHEMA-18：`updated` 与「变更记录」里最后一行日期必须一致。

    两个时间戳说的是同一件事。不一致时，读者没法判断「这条最后改于什么时候」——
    而 `updated` 已经进了 `index.json` 与生成块。
    """
    for rel, o in sorted(objects.items()):
        body = section_body(o["text"], "变更记录") or ""
        dates = re.findall(r"\|\s*(20\d\d-\d\d-\d\d)\s*\|", body)
        upd = fm_value(o["fm"], "updated")
        if dates and upd and max(dates) != upd:
            errors.append(
                f"{rel}: `updated`={upd}，但「变更记录」最后一行是 {max(dates)}（R-SCHEMA-18）")


def check_bilingual_fields(objects, events, en_fm, errors):
    """R-BILING-02：英译本的 `type` / `status` / `evidence` 必须与中文原件一致。

    `M-10`（改一份同步另一份）里，**语义**只能人判，但**这三个字段是结构**。
    在此之前，把英译本的 `status` 改掉、中文不动，两边都「合法」——
    于是同一个 `id` 在两种语言里有两套状态，而读者只会看到自己那一份。
    """
    zh = {}
    for bucket in (objects, events):
        for rel, o in bucket.items():
            oid = fm_value(o["fm"], "id")
            if oid:
                zh[oid] = o
    for rel, fm in sorted(en_fm.items()):
        oid = fm_value(fm, "id") if fm else None
        if not oid or oid not in zh:
            continue
        z = zh[oid]
        zt = z.get("type") or fm_value(z["fm"], "type")
        if fm_value(fm, "type") != zt:
            errors.append(f"{rel}: 英译本 type={fm_value(fm, 'type')!r} "
                          f"与中文原件 {zt!r} 不一致（R-BILING-02）")
        if fm_value(fm, "status") != fm_value(z["fm"], "status"):
            errors.append(f"{rel}: 英译本 status=「{fm_value(fm, 'status')}」"
                          f"与中文原件「{fm_value(z['fm'], 'status')}」不一致（R-BILING-02）")
        en_ev = sorted(set(evidence_ids_of(fm or "")))
        zh_ev = sorted(set(evidence_ids_of(z["fm"])))
        if en_ev != zh_ev:
            errors.append(f"{rel}: 英译本 evidence={en_ev} 与中文原件 {zh_ev} 不一致"
                          f"（R-BILING-02）")
        # `名称` 可以翻译，但稳定键 / 学科 / 学段 / 来源是结构，必须一致。
        def ext_sig(x):
            return sorted((e["标识"], e["学科"], e["学段"], e["来源"])
                          for e in external_prereqs_of(x))
        if ext_sig(fm or "") != ext_sig(z["fm"]):
            errors.append(
                f"{rel}: 英译本的 `外部先修` 与中文原件不一致"
                f"（比较 标识/学科/学段/来源，`名称` 可翻译）（R-BILING-02）")


def check_attack_has_edge(objects, errors):
    """R-GRAPH-05：攻击条目自己必须有一条 `攻击` 边。

    「攻击」在本库是**落到某个论证上的主张**（`攻击: ["[X](x.md#a1)"]`）。
    一个放在 `attacks/` 里、却不指向任何论证的文件，只是一条评论——
    它拿走了「独立条目、独立状态」的全部形式，却不承担「击倒某条论证」的功能。
    """
    for rel, o in sorted(objects.items()):
        if "/attacks/" not in rel:
            continue
        if not fm_links(o["fm"], "攻击"):
            errors.append(f"{rel}: 攻击条目没有任何 `攻击` 边 —— "
                          f"攻击必须落到**具体某个论证**上，否则它只是一条评论（R-GRAPH-05）")


def check_readme_status(objects, errors):
    """R-README-02：学科 README 里手写的状态列，必须与 front-matter 一致。

    学科 README 是读者进库后的第一张表，而它的「状态」列是**手写的**。
    手写的状态会漂移：条目从 `有效` 改成 `需复审`，README 还写着 `有效`——
    读者看到的是旧的，而且没有任何检查会告诉他。
    """
    statuses = set(STATUS_MEANING)
    for subj_dir in sorted(set(SUBJECT_DIRS.values())):
        rp = ROOT / "knowledge" / subj_dir / "README.md"
        if not rp.exists():
            continue
        for line in rp.read_text(encoding="utf-8").replace("\r\n", "\n").splitlines():
            if not line.startswith("|"):
                continue
            m = re.search(r"\]\(([^)#]+)", line)
            if not m:
                continue
            tgt = os.path.normpath(os.path.join(str(rp.parent), m.group(1)))
            rel = os.path.relpath(tgt, str(ROOT)).replace(os.sep, "/")
            o = objects.get(rel)
            if not o:
                continue
            cells = [c.strip().strip("*").strip("`") for c in line.strip().strip("|").split("|")]
            shown = [c for c in cells if c in statuses]
            real = fm_value(o["fm"], "status")
            if shown and shown[0] != real:
                errors.append(
                    f"{rp.relative_to(ROOT).as_posix()}: 表里写的状态是「{shown[0]}」，"
                    f"但 `{Path(rel).name}` 的 front-matter 是「{real}」（R-README-02）")


def check_body_evidence_ids(objects, errors):
    """R-EVID-04：正文里出现的 `ev-###` 必须已在证据索引登记。

    front-matter 的 `evidence` 会被校验（R-EVID-01），但**正文里写的编号没有**——
    写错一位、或者引一个不存在的编号，全库都不会有反应。
    **这条只查「编号是否存在」，不要求它属于本条**：正文引用别人的证据、
    讨论一条已作废的证据，都是合法的写法（前者如 RFC 条目互引，后者如欧姆定律讨论 ev-002）。
    """
    idx = parse_evidence_index()
    for rel, o in sorted(objects.items()):
        body = re.sub(r"\A---.*?\n---", "", o["text"], count=1, flags=re.S)
        for e in sorted(set(re.findall(r"ev-\d+", body))):
            if e not in idx:
                errors.append(f"{rel}: 正文引用了 `{e}`，但它不在证据索引里（R-EVID-04）")


MECH_RULES = [
    ("R-SCHEMA-01", "front-matter 必填 11 字段，顶层键不重复"),
    ("R-SCHEMA-02", "type 合法；status 受 type 约束；只有「命题」可用「已确证」"),
    ("R-SCHEMA-03", "id 唯一"),
    ("R-SCHEMA-04", "`evidence` 非空（无来源不入库）"),
    ("R-SCHEMA-05", "必备小节齐全，且顺序固定；六种类型都要有 `## 论证`"),
    ("R-SCHEMA-06", "`知识点` 正文第一行是 `> [!TIP]`（读完你会什么）"),
    ("R-SCHEMA-07", "`scope.学段` 用枚举（小学/初中/高中/大学/不限，组合用「至」）"),
    ("R-SCHEMA-08", "`created` / `updated` 为 YYYY-MM-DD，且 updated ≥ created"),
    ("R-SCHEMA-09", "`author` 形如 `@handle` 或 `AI（模型）· 经 @复核 · 日期`"),
    ("R-SCHEMA-10", "`license` 必须是 CC-BY-SA-4.0"),
    ("R-SCHEMA-11", "`id` 前缀与学科一致（物理→physics · 生活→life · 医学→med · 地理→geog · 科学→science · 交通→transport · 计算机→computing · 经济→econ · 法律→law）"),
    ("R-SCHEMA-12", "`教法` 有 `knowledge_point`，且指向「知识点」"),
    ("R-SCHEMA-13", "`教法` 有 `scope.水平档`，取值 BL / OL / AL（可多档）或「不分档」"),
    ("R-SCHEMA-14", "医学条目有 `scope.条件`，且正文开头是 `> [!CAUTION]` 免责块"),
    ("R-SCHEMA-15", "front-matter 的 `key: value` 值不得以 YAML 指示符（`*` `&` `!` `|` `>` `%` `@` `` ` ``）开头而不加引号（否则严格 YAML 解析器报错）"),
    ("R-SCHEMA-16", "文件所在目录与 `type` 对应（concepts / claims / methods / misconceptions / paths / resources）"),
    ("R-SCHEMA-17", "「暂定确认 / 已确证 / 失据 / 已推翻」必须有 ≥1 条论证（空集只能写「待审」）"),
    ("R-SCHEMA-18", "`updated` 与「变更记录」最后一行的日期一致"),
    ("R-SCHEMA-19", "`已确证` 需 ≥2 个不同的 `@` 署名 · `争议` 需 ≥2 条论证且 ≥1 条入边 `攻击` · `已推翻` 需 ≥1 条未被击倒的入边 `攻击`（状态不能只靠改一个字段）"),
    ("R-SCHEMA-20", "可选字段 `外部先修`：每项五个子字段齐全；`标识` 为 ASCII 稳定键且同条目不重复；`学段` 用枚举；`来源` 为单个已登记 `ev-###`；同一 `标识` 在 ≥2 个对象出现 → 提示「考虑建节点」"),
    ("R-EVENT-01", "`事件` 单开顶层 `events/`，与 `objects` **分开**：`type`=事件、`status` 只用持续更新/已封存、必填段 陈述/依据/变更记录、**无论证、无任何边**、`id` 前缀 `kb:event:`、`evidence` 非空；且每个事件须登记在 `events/README.md`"),
    ("R-LINK-01", "链接目标存在（相对链接 · 指向本仓库的绝对链接 · YAML `url:`）"),
    ("R-LINK-02", "锚点存在（标题 slug 或论证 ID）"),
    ("R-BILING-01", "英译本文件名由 `id` 派生（`<id 末段去类型前缀>.en.md`，与中文原件同目录）；缺译本给提示、不判失败"),
    ("R-BILING-03", "文档类文件（根级 / 学科 README / 覆盖度 / docs）必须有同名 `.en.md`；`templates/` 与 `.github/` 豁免"),
    ("R-BILING-02", "英译本的 `type` / `status` / `evidence` 与中文原件一致（`M-10` 里可机械化的那一半）"),
    ("R-LINK-03", "英文页面的站内链接指向英文页（该页存在时）；例外：`English version of` 行、指向无译本文件的链接"),
    ("R-GRAPH-01", "`先修` 只连「知识点」（`路径` 可声明路径外前置），且无环"),
    ("R-GRAPH-02", "`支持` / `攻击` 边的论证锚点存在"),
    ("R-GRAPH-03", "`路径` 每个成果至少被一个环节覆盖（未声明 outcomes 给警告）"),
    ("R-GRAPH-04", "`路径` 每个环节至少连到一个库内对象"),
    ("R-GRAPH-05", "攻击条目（`claims/attacks/`）必须有一条 `攻击` 边，落到具体论证上"),
    ("R-GRAPH-06", "同一论证上的多条 `支持` 边：证据编号并集只有 ≤1 份、或来源标识只有 1 个 → 提示「条数不构成强度」"),
    ("R-GRAPH-07", "路径的每个成果：只由 1 个环节覆盖、或覆盖条目的证据最高只到 `仅定位`/`未核验` → 提示（覆盖「有没有」之外的强度）"),
    ("R-EVID-01", "`evidence` 编号已登记且未作废"),
    ("R-EVID-02", "证据表 `类别` / `等级` / `核验深度` 取值合法"),
    ("R-EVID-03", "`暂定确认` / `已确证` 必须至少有一条 `核验深度` 为 `全文` / `摘要` 的证据（没读过不能说确认）"),
    ("R-EVID-04", "正文里出现的 `ev-###` 必须在证据索引登记（防笔误与幽灵引用；不要求属于本条）"),
    ("R-INDEX-01", "三份机器文件（`index.json` / `citations.json` / `evidence.json`）与内容一致（改内容必须重生成）"),
    ("R-INDEX-02", "人类文档的生成块与来源一致（README 统计 · START 学科总览 · knowledge 索引 · 物理覆盖度统计 · 规则表）"),
    ("R-README-01", "每个对象都在所属学科 README 里登记"),
    ("R-README-03", "学科 README 路径表里手写的「覆盖度 X/Y」与实际一致"),
    ("R-README-02", "学科 README 里手写的状态列与 front-matter 一致"),
    ("R-DOC-01", "状态图例在 FORMAT.md 与 knowledge/README.md 里列全"),
    ("R-DOC-02", "规则注册表中英两份的 ID 集合相同，且各自没有重复 ID"),
]

MANUAL_RULES = [
    ("M-01", "英文引用附近必须有中文说明（面向学习者可读性三条之一）"),
    ("M-02", "面向学习者的内容写在前面"),
    ("M-03", "`支持` 边的**跨来源独立性**仍由人判断 —— `R-GRAPH-06` 只算得出「同一来源标识」那一半"),
    ("M-04", "`教法` 的 `禁忌` 标注证据强度（强/弱），且与 `风险` 不混"),
    ("M-05", "不上传教材原文或扫描页"),
    ("M-06", "新引用资源逐条核对许可（教材 CC BY ≠ 它嵌的东西也是）"),
    ("M-07", "AI 攻击需人复核 + 署名披露（AI **可以**复核并写「已确证」，但必须留四栏 `## 复核记录`；复核者是谁由 `复核者` 字段披露）"),
    ("M-08", "统计数字不手写（交给 `--write-index` 生成）"),
    ("M-09", "对抗任务派发必须包含「质疑证据是否真实存在」与「质疑来源是否为本次引用而伪造」"),
    ("M-10", "文档中英成对存放（`<name>.md` 中文 + 同目录 `<id 派生>.en.md` 英文），改一份同步另一份"),
    ("M-11", "注册证据过**来源三问**：谁发布的（可问责主体）· 是哪个版本、什么时候生效（条目只声明该版本如此）· 是不是为这次引用现造的（有独立于本主张而存在的理由，且能在不同发布主体处找到第二来源；同源转载不算）；自建站点 / 无主体转载页 / 反查不到的标识符不登记"),
    ("M-12", "`外部先修` 的**真实性**（这条前置是否真的必需）与**是否该为它建节点**由人判断；机器只查声明形状、来源登记与同名复发"),
]

MECH_RULES_EN = [
    ("R-SCHEMA-01", "front-matter requires 11 fields; no duplicate top-level keys"),
    ("R-SCHEMA-02", "valid type; status constrained by type; only 命题 may use 已确证"),
    ("R-SCHEMA-03", "unique id"),
    ("R-SCHEMA-04", "`evidence` non-empty (no source, no entry)"),
    ("R-SCHEMA-05", "required sections present, fixed order; all six types have `## 论证`"),
    ("R-SCHEMA-06", "`知识点` first body line is `> [!TIP]` (what you'll know)"),
    ("R-SCHEMA-07", "`scope.学段` uses the enum (小学/初中/高中/大学/不限; combine with 「至」)"),
    ("R-SCHEMA-08", "`created` / `updated` are YYYY-MM-DD; updated ≥ created"),
    ("R-SCHEMA-09", "`author` is `@handle` or `AI（model）· 经 @reviewer · date`"),
    ("R-SCHEMA-10", "`license` must be CC-BY-SA-4.0"),
    ("R-SCHEMA-11", "`id` prefix matches subject (物理→physics · 生活→life · 医学→med · 地理→geog · 科学→science · 交通→transport · 计算机→computing · 经济→econ · 法律→law)"),
    ("R-SCHEMA-12", "`教法` has `knowledge_point` pointing to a 知识点"),
    ("R-SCHEMA-13", "`教法` has `scope.水平档`, values BL / OL / AL (multiple ok) or 「不分档」"),
    ("R-SCHEMA-14", "medical entries have `scope.条件` and body starts with a `> [!CAUTION]` block"),
    ("R-SCHEMA-15", "a front-matter `key: value` value must not start unquoted with a YAML indicator (`*` `&` `!` `|` `>` `%` `@` `` ` ``) — strict YAML parsers reject it"),
    ("R-SCHEMA-16", "a file sits in the folder its `type` maps to (concepts / claims / methods / misconceptions / paths / resources)"),
    ("R-SCHEMA-17", "「暂定确认 / 已确证 / 失据 / 已推翻」requires ≥1 argument (an empty set may only be 「待审」)"),
    ("R-SCHEMA-18", "`updated` matches the last date row in 「变更记录」"),
    ("R-SCHEMA-19", "`已确证` needs ≥2 distinct `@` signatures · `争议` needs ≥2 arguments and ≥1 incoming `攻击` edge · `已推翻` needs ≥1 undefeated incoming `攻击` edge (a status cannot be changed by editing one field)"),
    ("R-SCHEMA-20", "optional field `外部先修`: every item has all five subfields; `标识` is a stable ASCII key and unique within an entry; `学段` uses the enum; `来源` is a single registered `ev-###`; the same `标识` in ≥2 objects → hint 「consider building a node」"),
    ("R-EVENT-01", "`事件` lives top-level in `events/`, **separate** from `objects`: `type`=event, `status` only 持续更新/已封存, required sections 陈述/依据/变更记录, **no argument and no edges**, `id` prefix `kb:event:`, non-empty `evidence`; each event must be registered in `events/README.md`"),
    ("R-LINK-01", "link targets exist (relative · repo-absolute · YAML `url:`)"),
    ("R-LINK-02", "anchors exist (heading slug or argument id)"),
    ("R-BILING-01", "an English edition's filename is derived from its `id` (`<id-tail minus type prefix>.en.md`, same folder as the Chinese original); a missing translation is a notice, not a failure"),
    ("R-BILING-03", "documents (root / subject READMEs / coverage / docs) must have a same-named `.en.md`; `templates/` and `.github/` exempt"),
    ("R-BILING-02", "an English edition's `type` / `status` / `evidence` match the Chinese original (the mechanisable half of `M-10`)"),
    ("R-LINK-03", "links inside an English page point at the English page (when it exists); exempt: `English version of` lines and links to files that have no translation"),
    ("R-GRAPH-01", "`先修` connects only 知识点 (a `路径` may declare prerequisites outside the path), acyclic"),
    ("R-GRAPH-02", "`支持` / `攻击` edge argument anchors exist"),
    ("R-GRAPH-03", "`路径` each outcome covered by ≥1 环节 (undeclared outcomes → warning)"),
    ("R-GRAPH-04", "`路径` each 环节 connects to ≥1 in-repo object"),
    ("R-GRAPH-05", "attack entries in `claims/attacks/` carry at least one `攻击` edge to a specific argument"),
    ("R-GRAPH-06", "multiple `支持` edges on one argument whose evidence union has ≤1 item, or whose source identifier is a single one → hint 「count is not strength」"),
    ("R-GRAPH-07", "each path outcome covered by only 1 step, or its covering entries' evidence tops out at `仅定位`/`未核验` → hint (strength beyond 「is it covered」)"),
    ("R-EVID-01", "`evidence` id registered and not voided"),
    ("R-EVID-02", "evidence table `类别` / `等级` / `核验深度` values valid"),
    ("R-EVID-03", "`暂定确认` / `已确证` needs ≥1 evidence with `核验深度` of `全文` / `摘要` (unread can't be confirmed)"),
    ("R-EVID-04", "every `ev-###` mentioned in the body is registered in the evidence index (catches typos and ghost citations; need not belong to that entry)"),
    ("R-INDEX-01", "the three machine files (`index.json` / `citations.json` / `evidence.json`) match content (regenerate on change)"),
    ("R-INDEX-02", "human-doc generated blocks match their source (README stats · START subject overview · knowledge index · physics coverage stats · rule table)"),
    ("R-README-01", "every object registered in its subject README"),
    ("R-README-03", "the coverage figure `X/Y` typed into the subject README path table matches the computed one"),
    ("R-README-02", "the hand-written status column in a subject README matches the front-matter"),
    ("R-DOC-01", "status legend listed in FORMAT.md and knowledge/README.md"),
    ("R-DOC-02", "the Chinese and English rule registries cover the same id set, and neither repeats an id"),
]

MANUAL_RULES_EN = [
    ("M-01", "Chinese gloss near English quotations (one of three readability rules)"),
    ("M-02", "learner-facing content comes first"),
    ("M-03", "`支持` edge **cross-source independence** is still judged by humans — `R-GRAPH-06` only computes the 'same source identifier' half"),
    ("M-04", "`教法` `禁忌` marks evidence strength (strong/weak), not mixed with `风险`"),
    ("M-05", "don't upload textbook originals or scans"),
    ("M-06", "check license per new source (textbook CC BY ≠ what it embeds is too)"),
    ("M-07", "AI attack needs human review + author disclosure (AI can't be the reviewer for 已确证)"),
    ("M-08", "statistics not hand-written (generated by `--write-index`)"),
    ("M-09", "adversarial dispatch must include \"question whether the evidence really exists\" and \"question whether the source was fabricated for this citation\""),
    ("M-10", "documents stored bilingually (`<name>.md` Chinese + `<id-derived>.en.md` English in the same folder); sync both"),
    ("M-11", "new evidence passes the **three source questions**: who publishes it (an accountable body) · which version and when it took effect (the entry claims only that version) · was it made up for this citation (it exists for reasons independent of the claim, and a second source can be found at a different publishing body; same-origin reposts don't count); self-built sites, attribution-free repost pages and identifiers that don't resolve are not registered"),
    ("M-12", "the **truth** of an `外部先修` (is this prerequisite really required) and **whether to build a node for it** are human judgements; the machine only checks declaration shape, source registration and recurrence"),
]


def render_stats_block(index):
    s = index["统计"]
    by, sub = s["按类型"], s["按学科"]
    types = " · ".join(f"{k} {TYPE_EN[k]} {by[k]}" for k in TYPE_ORDER if by.get(k))
    subs = " · ".join(f"{k} {SUBJECT_EN[k]} {sub[k]}" for k in SUBJECT_ORDER if sub.get(k))
    tier = s.get("按溯源档") or {}
    total = s["对象总数"] or 1
    # 溯源档：**取最弱一环**。这一行是「0 条已确证」的另一半——
    # 只报状态，读者会把「待审」读成「没核过」；两个数并排出现才是完整的事实。
    tn = " · ".join(f"{k} {tier[k]}" for k in TIER_ORDER if tier.get(k))
    deep = tier.get("T4", 0) + tier.get("T3", 0)
    return "\n".join([
        "| | |",
        "|---|---|",
        f"| 对象 / Objects | **{s['对象总数']}** —— {types} |",
        f"| 事件 / Events | **{s.get('事件条数', 0)}** —— 顶层 `events/`，与对象**分开**（无论证、无真值） |",
        f"| 学科 / Subjects | {subs} |",
        f"| 证据 / Evidence | {s['证据条数']}（含作废 / void {s['作废证据条数']}） |",
        f"| 溯源 / Provenance | **{deep} / {s['对象总数']}（{deep / total:.0%}）读到全文或摘要** —— {tn} |",
        f"| 已确证 / Confirmed | **{s['已确证条数']}** |",
    ])


def render_subject_overview_block(index, en=False):
    """`START.md` 的学科总览 —— **全部来自 `index.json`**。

    **为什么必须是生成块**：`START.md` 是唯一面向普通读者的人口页，
    却曾长期手写「医学 2 条」「生活 5 条」「其他学科内容很少（12 条）」这类枚举。
    内容涨到 141 条时，那张手写表还停在 12 条 —— **读者按它判断「这里没有我要的东西」，
    然后离开**。手写的目录比没有目录更糟：它是有依据的错误。
    """
    objs = index["objects"]
    by_subject = collections.defaultdict(collections.Counter)
    for o in objs:
        by_subject[o["学科"].split(" ")[0]][o["type"]] += 1

    keys = [k for k in SUBJECT_ORDER if k in by_subject] + \
           [k for k in sorted(by_subject) if k not in SUBJECT_ORDER]
    suffix = ".en.md" if en else ".md"

    if en:
        lines = ["| Subject | Entries | What's in it | What it collects |", "|---|---|---|---|"]
    else:
        lines = ["| 学科 | 条数 | 里面有什么 | 收什么 |", "|---|---|---|---|"]
    for k in keys:
        c = by_subject[k]
        if en:
            bits = " · ".join(f"{TYPE_EN[t]} {c[t]}" for t in TYPE_ORDER if c.get(t))
            note = SUBJECT_NOTES_EN.get(k, SUBJECTS_FALLBACK_EN)
            name = SUBJECT_EN.get(k, k)
        else:
            bits = " · ".join(f"{t} {c[t]}" for t in TYPE_ORDER if c.get(t))
            note = SUBJECT_NOTES.get(k, SUBJECTS_FALLBACK)
            name = k
        lines.append(f"| [{name}](knowledge/{SUBJECT_DIRS.get(k, k)}/README{suffix}) "
                     f"| {sum(c.values())} | {bits} | {note} |")
    lines.append(f"| **{'Total' if en else '合计'}** | **{index['统计']['对象总数']}** "
                 f"| — | — |")
    return "\n".join(lines)


def render_coverage_block():
    """`knowledge/physics/coverage/README.md` 的统计表 —— 从**同一页的总览表**数出来。

    **这一条是真事故**：总览表逐行标了 🟢/🟡/🔴，但下面手写的统计写着「6 · 10 · 11」（共 27），
    而表里只有 25 行、实际是 5 · 7 · 13。**统计与它自己的表对不上，而没有人能一眼看出来。**
    既然数字能从表里数出来，就不该手写。
    """
    p = ROOT / "knowledge" / SUBJECT_DIRS["物理"] / "coverage" / "README.md"
    if not p.exists():
        return None
    text = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    body = section_body(text, "总览") or ""
    marks = {"🟢": "有覆盖", "🟡": "部分覆盖", "🔴": "完全缺"}
    cnt = collections.Counter()
    for line in body.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 3:
            continue
        for m in marks:
            if cells[2].startswith(m):
                cnt[m] += 1
                break
    total = sum(cnt.values())
    if not total:
        return None
    lines = ["| | 章级主题数 | 占比 |", "|---|---|---|"]
    for m in ("🟢", "🟡", "🔴"):
        lines.append(f"| {m} {marks[m]} | **{cnt[m]}** | {cnt[m] / total:.0%} |")
    lines.append(f"| **合计** | **{total}** | 100% |")
    return "\n".join(lines)


def render_subject_block(index):
    sub = index["统计"]["按学科"]
    keys = [k for k in SUBJECT_ORDER if k in sub] + \
           [k for k in sorted(sub) if k not in SUBJECT_ORDER]
    lines = ["| 学科 | 条目数 |", "|---|---|"]
    for k in keys:
        lines.append(f"| [{k}]({SUBJECT_DIRS.get(k, k)}/README.md) | {sub[k]} |")
    ev = index["统计"].get("事件条数", 0)
    if ev:
        lines.append(f"| [事件（顶层）](../events/README.md) | {ev} |")
    lines.append(f"| **合计** | **{index['统计']['对象总数']}** |")
    return "\n".join(lines)


def render_subject_block_en(index):
    """`knowledge/README.en.md` 的学科表 —— 与中文版**同源**（同一份 `index.json`）。"""
    sub = index["统计"]["按学科"]
    keys = [k for k in SUBJECT_ORDER if k in sub] + \
           [k for k in sorted(sub) if k not in SUBJECT_ORDER]
    lines = ["| Subject | Entries |", "|---|---|"]
    for k in keys:
        name = SUBJECT_EN.get(k, k)
        lines.append(f"| [{name}]({SUBJECT_DIRS.get(k, k)}/README.en.md) | {sub[k]} |")
    ev = index["统计"].get("事件条数", 0)
    if ev:
        lines.append(f"| [Events (top level)](../events/README.en.md) | {ev} |")
    lines.append(f"| **Total** | **{index['统计']['对象总数']}** |")
    return "\n".join(lines)


def verified_rules():
    """哪些机械规则**有注入样本**（`tools/verify_rules.py` 的 `SAMPLES`）。

    规则表说「已强制」很容易，说和查是两件事。这张清单让两者可以对照：
    **没有样本的规则，只是"写了检查函数"，没有人验证过它会失败。**
    读不到时返回空集（不因为自测脚本坏了就挡住校验）。
    """
    try:
        sys.path.insert(0, str(ROOT / "tools"))
        import verify_rules as vr           # noqa: E402  同目录、零副作用（main 有 __main__ 守卫）
        return {e[0] for e in vr.SAMPLES}
    except Exception:
        return set()


def render_physics_methods_block(index, english=False):
    """物理 README 教法小节的**覆盖统计**——生成，不手写。

    这一页以前只列教法，不列「**还有多少知识点没有人写过怎么讲**」。
    参数是现成的：知识点数、教法挂到了几个知识点上；差就是缺口。
    """
    concepts = [o for o in index["objects"]
                if o["type"] == "知识点" and o.get("学科") == "物理"]
    covered = set()
    for p in (ROOT / "knowledge" / "physics").rglob("methods/*.md"):
        if p.name.endswith(".en.md"):
            continue
        fm = parse_front_matter(p.read_text(encoding="utf-8")) or ""
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", fm):
            covered.add(Path(link).stem)
    hit = sum(1 for o in concepts if Path(o["path"]).stem in covered)
    miss = len(concepts) - hit
    if english:
        lines = ["| Concepts | With a method | Without |", "|---|---|---|",
                 f"| {len(concepts)} | {hit} | **{miss}** |", "",
                 "> Generated by `kbcheck.py`. To see *which* concepts lack a method, run "
                 "`python tools/make_tasks.py` (grouped by path)."]
    else:
        lines = ["| 知识点 | 有教法 | 缺教法 |", "|---|---|---|",
                 f"| {len(concepts)} | {hit} | **{miss}** |", "",
                 "> 由 `kbcheck.py` 生成。**缺哪些**按路径归拢在 `python tools/make_tasks.py` 里。"]
    return chr(10).join(lines)


def render_rules_block():
    done = verified_rules()
    lines = [
        f"**机械校验（{len(MECH_RULES)} 条，其中 {len(done & {r for r, _ in MECH_RULES})} 条有注入样本）**"
        f" —— 由 `tools/kbcheck.py` 强制；改规则必须同步改检查：",
        "",
        "> **「注入样本」= 在 [`tools/verify_rules.py`](../tools/verify_rules.py) 里有一个**会失败**的样本。**",
        "> 标 `—` 的规则**只有检查函数、没有任何人验证过它会失败**——它们可能是空转的。",
        "> 这不是缺陷清单，是**待补清单**：补一个样本，就把它变成 ✅。",
        "", "| ID | 规则 | 注入样本 |", "|---|---|---|",
    ]
    for rid, text in MECH_RULES:
        mark = "✅" if rid in done else "—"
        lines.append(f"| `{rid}` | {text} | {mark} |")
    lines += [
        "",
        f"**人工复核（{len(MANUAL_RULES)} 条）** —— 无法机械化，按 [CONTRIBUTING](../CONTRIBUTING.md) 的自检表执行：",
        "", "| ID | 规则 |", "|---|---|",
    ]
    for rid, text in MANUAL_RULES:
        lines.append(f"| `{rid}` | {text} |")
    return "\n".join(lines)


def render_rules_block_en():
    done = verified_rules()
    lines = [
        f"**Mechanically enforced ({len(MECH_RULES_EN)}, of which {len(done & {r for r, _ in MECH_RULES_EN})} have an injected sample)**"
        f" — enforced by `tools/kbcheck.py`; change a rule, change the check:",
        "",
        "> **An injected sample means [`tools/verify_rules.py`](../tools/verify_rules.py) contains a** failing **sample for it.**",
        "> A rule marked `—` **has a check function that nobody has watched fail** — it may be a no-op.",
        "> This is not a defect list but a **to-do list**: add a sample and it turns ✅.",
        "", "| ID | Rule | Injected sample |", "|---|---|---|",
    ]
    for rid, text in MECH_RULES_EN:
        mark = "✅" if rid in done else "—"
        lines.append(f"| `{rid}` | {text} | {mark} |")
    lines += [
        "",
        f"**Human-reviewed ({len(MANUAL_RULES_EN)})** — not mechanizable; run the checklist in [CONTRIBUTING](../CONTRIBUTING.en.md):",
        "", "| ID | Rule |", "|---|---|",
    ]
    for rid, text in MANUAL_RULES_EN:
        lines.append(f"| `{rid}` | {text} |")
    return "\n".join(lines)


GAPS_TOP = 10      # 每组在页面上最多列几条；完整清单交给 make_tasks


def _gap_item_line(key, it, en=False):
    """`docs/GAPS.md` 里一行的写法。**不加链接**：这一页是仪表盘，不是索引。"""
    if key == "external":
        n = it["出现次数"]
        if en:
            # 英文页面只给稳定标识：名称来自中文条目，硬翻会造出一个不存在的英文名。
            return f"`{it['标识']}` — {n} objects"
        names = " / ".join(it.get("名称") or [it["标识"]])
        return f"`{it['标识']}`（{names}）—— {n} 个对象"
    if key == "coverage":
        return it["章"]
    # 英文页面优先用英文标题（`title_en`）；没有就退回中文标题——
    # 宁可显示中文，也不要显示一个编出来的英文名。
    title = (it.get("title_en") or it["title"]) if en else it["title"]
    if key == "todo":
        # 标题常常就是一整句命题，这里只留够认人的长度；要全文去条目里看。
        short = title if len(title) <= 48 else title[:48] + "…"
        line = it["行"] if len(it["行"]) <= 96 else it["行"][:96] + "…"
        if en:
            return f"`{it['id']}` · {short} — body: {line}"
        return f"`{it['id']}` · {short} —— {line}"
    if key in ("path-thin", "path-shallow"):
        outs = ", ".join(it["成果"]) if en else "、".join(it["成果"])
        return f"{title} —— {outs}"
    if key == "review":
        dep = it.get("下游依赖", 0)
        tail = (f" — {dep} other entries list it as a prerequisite" if en
                else f" — {dep} 条别的条目先修它") if dep else ""
        return f"`{it['id']}` · {title}{tail}"
    if key == "review-blocked":
        evs = ", ".join(f"`{e}`" for e in it.get("未读证据") or [])
        if it.get("无论证"):
            why = "argument not written" if en else "论证未写"
        elif it.get("无证据"):
            why = "no evidence cited" if en else "没有引用证据"
        else:
            why = f"evidence unread: {evs}" if en else f"证据未读：{evs}"
        return f"`{it['id']}` · {title} — {why}" if en else f"`{it['id']}` · {title} —— {why}"
    if key == "provenance":
        evs = ", ".join(f"`{e}`" for e in it.get("薄证据") or []) or "—"
        tier = it.get("溯源", "?")
        return (f"`{it['id']}` · {title} — {tier}, weakest: {evs}" if en
                else f"`{it['id']}` · {title} —— {tier}，最弱：{evs}")
    return f"`{it['id']}` · {title}"


def render_gaps_block(data, en=False):
    """`docs/GAPS.md` 的生成块：**一页看全库缺什么**。

    这一页不是「待办清单的复制品」——它是**同一份计算**的另一种排法：
    上面一张表回答「哪类缺口有多大」，下面每组列前 10 条回答「从哪条开始」。
    完整清单（含 JSON）在 `python tools/make_tasks.py`，两者共用 `gaps.compute()`。
    """
    s = data["统计"]
    p = s.get("路径成果") or {}
    st = s.get("状态") or {}
    L = []
    if en:
        L.append(f"**{s['对象']}** objects · **{s['可作事实引用']}** citable as fact · "
                 f"**{s['不可作事实引用']}** not citable · **{s['证据']}** evidence records · "
                 f"**{s['事件']}** events")
        if st:
            L.append(f"**{st.get('已确证', 0)} confirmed** · {st.get('暂定确认', 0)} provisional · "
                     f"{st.get('有效', 0)} valid · {st.get('待审', 0)} awaiting review")
        if p:
            L.append(f"**{p['条数']}** paths · all **{p['声明']}** learning outcomes covered · "
                     f"**{p['单环节']}** ({p['单环节占比']}%) taught exactly once")
        tr = s.get("溯源") or {}
        if tr:
            L.append(" · ".join(f"{k} {tr[k]}" for k in TIER_ORDER if tr.get(k))
                     + " — provenance tier (**weakest link** over cited evidence)")
        L += ["", "| Gap | Count | Why it counts as a gap |", "|---|---|---|"]
    else:
        L.append(f"**{s['对象']}** 条对象 · **{s['可作事实引用']}** 条可作事实引用 · "
                 f"**{s['不可作事实引用']}** 条不可引用 · **{s['证据']}** 条证据 · "
                 f"**{s['事件']}** 条事件")
        if st:
            L.append(f"**已确证 {st.get('已确证', 0)}** · 暂定确认 {st.get('暂定确认', 0)} · "
                     f"有效 {st.get('有效', 0)} · 待审 {st.get('待审', 0)}")
        if p:
            L.append(f"**{p['条数']}** 条路径 · **{p['声明']}** 个学习成果全部有环节覆盖 · "
                     f"**{p['单环节']}** 个（{p['单环节占比']}%）只讲一次")
        tr = s.get("溯源") or {}
        if tr:
            L.append(" · ".join(f"{k} {tr[k]}" for k in TIER_ORDER if tr.get(k))
                     + " —— 溯源档（**取最弱一环**，与「已确证」正交）")
        L += ["", "| 缺口 | 数量 | 为什么算缺口 |", "|---|---|---|"]

    for key in data["顺序"]:
        g = data["分组"][key]
        L.append(f"| **{g['名称_en'] if en else g['名称']}** | {g['数量']} | "
                 f"{g['为什么_en'] if en else g['为什么']} |")

    L.append("")
    L.append("> " + ("One object can appear in several rows — **do not add the counts up**."
                     if en else
                     "**同一个对象可能同时出现在几行里，别把数量相加**。"))
    r = data["分组"]["review"]["数量"]
    rb = data["分组"]["review-blocked"]["数量"]
    pending = (s.get("状态") or {}).get("待审")
    if pending is not None:
        L.append("> " + (f"**The one exact partition:** review {r} + review-blocked {rb} "
                         f"= every `待审` entry ({pending})." if en else
                         f"**唯一不重叠的一对：**三分钟复核 {r} + 复核前置 {rb} "
                         f"= 全部 `待审` 条目（{pending}）。"))

    for key in data["顺序"]:
        g = data["分组"][key]
        items = g["条目"]
        if not items:
            continue
        name = g["名称_en"] if en else g["名称"]
        how = g["怎么做_en"] if en else g["怎么做"]
        L += ["", f"### {name} ({g['数量']})" if en else f"### {name}（{g['数量']}）", "",
              f"> {how}", ""]
        for it in items[:GAPS_TOP]:
            L.append("- " + _gap_item_line(key, it, en))
        if len(items) > GAPS_TOP:
            rest = len(items) - GAPS_TOP
            L.append(f"- …and {rest} more — full list: `python tools/make_tasks.py --json`"
                     if en else
                     f"- …还有 {rest} 项 —— 完整清单：`python tools/make_tasks.py --json`")
    return "\n".join(L)


def _rough_k(payload):
    """整份文件的**数量级** token 估计：字符数 ÷ 3.2。

    这不是计费口径，也不假装是。它存在的唯一目的，是让「整读一份」与
    「按 id 取一条」的差距**有一个可核对的数字**——旧版手写的 ≈14k 在
    条目涨到 746 条后已经差了七倍，而没有任何检查会发现。
    """
    raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n"
    return max(1, round(len(raw) / 3.2 / 1000))


def render_machine_files_block(built, en=False):
    """`llms.txt` 的「三份文件多大」表——**生成物**，不手写。

    这张表曾经手写 `≈14k / ≈18k / ≈9k`。库涨到 746 条对象后，真实值是
    `≈96k / ≈158k / ≈38k`：**同一段文字在教人省 token，却把成本少报了一个数量级。**
    数字会漂，所以数字必须由脚本写。
    """
    idx, cit, ev = built["index.json"], built["citations.json"], built["evidence.json"]
    if en:
        lines = [
            "| File | Holds | Entries | Whole file ≈ tokens |",
            "|---|---|---|---|",
            f"| [`index.json`](index.json) | navigation + whether it may be cited | "
            f"{len(idx['objects'])} objects · {len(idx['事件'])} events | **≈{_rough_k(idx)}k** |",
            f"| [`citations.json`](citations.json) | citation kit, **by id** | "
            f"{len(cit['by_id'])} entries | **≈{_rough_k(cit)}k** |",
            f"| [`evidence.json`](evidence.json) | evidence registry | "
            f"{len(ev['entries'])} entries | **≈{_rough_k(ev)}k** |",
            "",
            "> Generated by `tools/kbcheck.py` (characters ÷ 3.2 — a **rough order of magnitude**, "
            "not a billing figure). The point is the ratio: one `scholia_cite` is ≈160 tokens.",
        ]
    else:
        lines = [
            "| 文件 | 装什么 | 条目 | 整份 ≈ tokens |",
            "|---|---|---|---|",
            f"| [`index.json`](index.json) | 导航 + 能不能引用 | "
            f"{len(idx['objects'])} 条对象 · {len(idx['事件'])} 条事件 | **≈{_rough_k(idx)}k** |",
            f"| [`citations.json`](citations.json) | 引用材料，**按 id 取** | "
            f"{len(cit['by_id'])} 条 | **≈{_rough_k(cit)}k** |",
            f"| [`evidence.json`](evidence.json) | 证据登记 | "
            f"{len(ev['entries'])} 条 | **≈{_rough_k(ev)}k** |",
            "",
            "> 由 `tools/kbcheck.py` 生成（字符数 ÷ 3.2，**数量级**而已，不是计费口径）。"
            "重点在比例：`scholia_cite` 取一条 ≈160 tokens。",
        ]
    return "\n".join(lines)


def generated_blocks(objects, events):
    built = build_indexes(objects, events)
    index = built["index.json"]
    # 缺口只算一次：`docs/GAPS.md` 与 `make_tasks.py` / MCP 共用同一个 `gaps.compute()`
    gap_data = gaps.compute(index,
                            built["citations.json"]["by_id"],
                            built["evidence.json"]["entries"],
                            root=ROOT)
    blocks = {
        "README.md": render_stats_block(index),
        "README.en.md": render_stats_block(index),
        "knowledge/README.md": render_subject_block(index),
        "knowledge/README.en.md": render_subject_block_en(index),
        "knowledge/physics/README.md": render_physics_methods_block(index),
        "knowledge/physics/README.en.md": render_physics_methods_block(index, english=True),
        "START.md": render_subject_overview_block(index),
        "START.en.md": render_subject_overview_block(index, en=True),
        "docs/RULES.md": render_rules_block(),
        "docs/RULES.en.md": render_rules_block_en(),
        "docs/GAPS.md": render_gaps_block(gap_data),
        "docs/GAPS.en.md": render_gaps_block(gap_data, en=True),
        "llms.txt": render_machine_files_block(built),
        "llms.en.txt": render_machine_files_block(built, en=True),
    }
    cov = render_coverage_block()
    if cov:
        blocks["knowledge/physics/coverage/README.md"] = cov
        # 统计表是纯数字，中英两份共用同一段生成内容
        blocks["knowledge/physics/coverage/README.en.md"] = cov
    return blocks


def sync_generated(objects, events, write, errors):
    """人类文档里的数字/清单由本脚本生成——**不手写**（写了就会漂移）。"""
    for rel, body in generated_blocks(objects, events).items():
        p = ROOT / rel
        if not p.exists():
            errors.append(f"{rel}: 文件不存在（生成块的目标文件）（R-INDEX-02）")
            continue
        text = p.read_text(encoding="utf-8").replace("\r\n", "\n")
        if GENERATED_BEGIN not in text or GENERATED_END not in text:
            errors.append(
                f"{rel}: 缺少生成块标记（{GENERATED_BEGIN} / {GENERATED_END}）（R-INDEX-02）")
            continue
        pre, rest = text.split(GENERATED_BEGIN, 1)
        old, post = rest.split(GENERATED_END, 1)
        new = f"\n{body}\n"
        if old != new:
            if write:
                p.write_text(pre + GENERATED_BEGIN + new + GENERATED_END + post,
                             encoding="utf-8")
            else:
                errors.append(
                    f"{rel}: 生成块与来源不一致（数字/清单过期）"
                    " —— 运行 `python tools/kbcheck.py --write-index`（R-INDEX-02）")


def check_event_object(fm, text, rel, ids, events, errors):
    """校验一个 `事件` 条目（与知识对象分开的另一套规则）。

    事件记录「发生了什么」：只有陈述/依据/变更记录，没有论证、没有边；
    `evidence` 必须非空（事件只需要证据，证据为空等于没有事件）。
    """
    keys = front_matter_keys(fm)
    dup = [k for k, c in collections.Counter(keys).items() if c > 1]
    if dup:
        errors.append(f"{rel}: front-matter 顶层键重复 {dup}（R-SCHEMA-01）")
    missing = [k for k in EVENT_FIELDS if k not in keys]
    if missing:
        errors.append(f"{rel}: 事件 front-matter 缺字段 {missing}（R-SCHEMA-01）")
    check_front_matter_shape(fm, rel, errors)

    t, st, i = fm_value(fm, "type"), fm_value(fm, "status"), fm_value(fm, "id")
    if t != EVENT_TYPE:
        errors.append(f"{rel}: `事件` 的 `type` 必须是 {EVENT_TYPE!r} -> {t!r}（R-EVENT-01）")
    if st not in EVENT_STATUS:
        errors.append(
            f"{rel}: `事件` 的 `status` 只能是 {'/'.join(sorted(EVENT_STATUS))} -> {st!r}（R-EVENT-01）")
    for sec in EVENT_SECTIONS:
        if not has_section(text, sec):
            errors.append(f"{rel}: 事件缺必备小节「{sec}」（R-SCHEMA-05）")
    if not (i or "").startswith(EVENT_ID_PREFIX):
        errors.append(f"{rel}: `事件` 的 `id` 前缀必须是 {EVENT_ID_PREFIX!r} -> {i!r}（R-EVENT-01）")
    if i in ids:
        errors.append(f"{rel}: id 与 {ids[i]} 重复 -> {i}（R-SCHEMA-03）")
    elif i:
        ids[i] = rel

    # 事件没有边：不安全
    for key in ("edges", "先修", "支持", "攻击", EXTERNAL_PREREQ_KEY):
        if re.search(rf"^[ \t]*{key}:", fm, re.M):
            errors.append(
                f"{rel}: `事件` 不应有 `{key}`（事件记录事实，不分先修、不支持、不攻击）（R-EVENT-01）")

    # 事件只需要证据：证据为空等于没有事件
    if not re.findall(r"ev-\d+", fm):
        errors.append(
            f"{rel}: `事件` 的 `evidence` 为空 —— 事件只需要证据，证据为空等于没有事件"
            "（R-SCHEMA-04）")

    events[rel] = {"fm": fm, "text": text}


def check_event_readme(events, errors):
    """每个 `事件` 都必须在 `events/README.md` 里被登记。"""
    p = ROOT / EVENT_DIR / "README.md"
    if not p.exists():
        if events:
            errors.append(f"{EVENT_DIR}README.md 不存在（事件目录需要索引）（R-EVENT-01）")
        return
    txt = p.read_text(encoding="utf-8")
    for rel in events:
        name = rel.split("/")[-1]
        if name not in txt:
            errors.append(
                f"{rel}: **事件索引里没有登记它**"
                f"（`{EVENT_DIR}README.md` 必须提到 `{name}`）（R-EVENT-01）")


# 英文译本的文件名由 `id` 派生：取 id 最后一段，去掉类型前缀，加 `.en.md`。
# **为什么不再用「同名 .en.md」**：那会让英文页继承中文文件名（`参考系.en.md`），
# 于是英文读者点开的是 `.../物理/知识点/参考系.en.md`——**英文内容的文件名是中文**。
# 由 id 派生有三个好处：名字是英文、改名不影响、**配对可以机械校验**（R-BILING-01）。
EN_SLUG_PREFIX = re.compile(r"^(kp|prop|method|mis|miscon|misconception|path|res|resource|attack)-")


def en_slug(oid):
    return EN_SLUG_PREFIX.sub("", (oid or "").split(":")[-1])


def en_path(zh_rel, oid):
    """中文条目 -> 它的英文译本该在哪。**同目录**，文件名由 id 派生。"""
    d = posixpath.dirname(zh_rel)
    return (d + "/" if d else "") + en_slug(oid) + ".en.md"


def check_bilingual_pairs(objects, events, en_docs, errors, warnings):
    """R-BILING-01：英译本的文件名必须由 `id` 派生；配对按 `id` 认。

    **这条规则是「配对」从字符巧合变成机械关系的关键。** 原来的约定是「同名 `.en.md`」：
    既让英文页沿用中文文件名，又让校验器无法判断「谁和谁是一对」——
    同名只是**字符上的巧合**。`id` 才是配对键：唯一、稳定、重命名文件也不变。

    **缺译本只报 warning，不判失败。** 「双语」是承诺，但把它变成硬门槛
    等于给每个中文条目加一道翻译工序——那是**另一条政策**，要改得单独决定，
    不该夹在一次命名修复里悄悄生效。**缺口仍然可见（每次跑都列出来）。**
    """
    zh_by_id = {}
    for bucket in (objects, events):
        for rel, o in bucket.items():
            oid = fm_value(o["fm"], "id")
            if oid:
                zh_by_id[oid] = rel

    seen = set()
    for rel, oid in sorted(en_docs.items()):
        if rel.startswith(DRAFT_DIR):
            continue
        name = rel.split("/")[-1]
        # README 与规格文档（FORMAT / CONTRIBUTING / docs/…）本来就没有 id，
        # 它们不是「某个条目的译本」，不参与配对。
        is_page = (rel.startswith("knowledge/") or rel.startswith(EVENT_DIR + "/")) \
            and not name.startswith("README")
        if not is_page and not oid:
            continue
        if not oid:
            errors.append(f"{rel}: 英文译本缺 front-matter `id`（必须与中文原件同一个 id）（R-BILING-01）")
            continue
        if oid not in zh_by_id:
            errors.append(f"{rel}: 英文译本的 `id` 在中文原件里找不到 -> {oid}（R-BILING-01）")
            continue
        want = en_path(zh_by_id[oid], oid)
        if rel != want:
            errors.append(f"{rel}: 英文文件名必须由 `id` 派生 -> 应为 {want}"
                          f"（英文文件名里不该出现中文）（R-BILING-01）")
        seen.add(oid)

    for oid, zh_rel in sorted(zh_by_id.items()):
        if oid not in seen:
            want = en_path(zh_rel, oid)
            if (ROOT / want).exists():
                warnings.append(f"{zh_rel}: 英文译本的 id 与文件名对不上 -> 应为 {want}")
            else:
                warnings.append(f"{zh_rel}: 缺英文译本（M-10 的人工项）-> 应为 {want}")


def check_link_language(link_records, en_docs, objects, events, errors):
    """R-LINK-03：英文页面里的站内链接必须落在英文页上。

    豁免两类：① `English version of` 行（有意指向中文原件的约定行）；
    ② 指向**没有英文译本**的文件（README、docs、模板）——那些本来就只有一份。
    """
    zh_by_id = {}
    for bucket in (objects, events):
        for rel, o in bucket.items():
            oid = fm_value(o["fm"], "id")
            if oid:
                zh_by_id[rel] = oid

    for rel, label, target, target_rel, en_pointer in link_records:
        if rel not in en_docs:
            continue          # 只看英文页面（含英文 README）
        if target in en_pointer:
            continue          # 约定行：指向中文原件
        oid = zh_by_id.get(target_rel)
        if not oid:
            continue          # 目标没有英文译本（README / docs / 模板），不算错
        alt = en_path(target_rel, oid)
        if (ROOT / alt).exists():
            alt_rel = posixpath.relpath(alt, posixpath.dirname(rel))
            errors.append(f"{rel}: 英文页面的链接指向了中文页 -> "
                          f"[{label}]({target}) 应为 {alt_rel}"
                          "（确需指向中文原件时，把该链接写在 `English version of` 行里）"
                          "（R-LINK-03）")


def check_all():
    errors = []
    warnings = []
    ids = {}
    objects = {}
    events = {}
    en_docs = {}          # 英文译本：rel -> 它的 id（None = 缺 id）
    en_fm = {}            # 英文译本：rel -> 它的 front-matter（R-BILING-02 要比字段）
    link_records = []     # 供 R-LINK-03 二次判定：语言是否落错
    md_files = scan_text_files()

    for path in md_files:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        fm = parse_front_matter(text)

        # knowledge/ 下是知识对象；顶层 events/ 下是「事件」——与对象**分开**的另一类
        # 记录（不分先修/支持/攻击，没有论证，不并入 objects）。
        # 两种语言的 README 与英文译本 .en.md 都不是条目。
        _name = rel.split("/")[-1]
        is_readme = _name.startswith("README") or _name.endswith(".en.md")
        is_event = rel.startswith(EVENT_DIR) and not is_readme
        is_object = rel.startswith("knowledge/") and not is_readme

        if _name.endswith(".en.md"):
            en_docs[rel] = fm_value(fm, "id") if fm else None
            en_fm[rel] = fm

        if is_event:
            if fm is None:
                errors.append(f"{rel}: 事件缺 front-matter（R-SCHEMA-01）")
            else:
                check_event_object(fm, text, rel, ids, events, errors)
        elif is_object:
            if fm is None:
                errors.append(f"{rel}: 知识对象缺 front-matter（R-SCHEMA-01）")
            else:
                keys = front_matter_keys(fm)
                dup = [k for k, c in collections.Counter(keys).items() if c > 1]
                if dup:
                    errors.append(f"{rel}: front-matter 顶层键重复 {dup}（R-SCHEMA-01）")

                missing = [k for k in REQUIRED_FIELDS if k not in keys]
                if missing:
                    errors.append(f"{rel}: front-matter 缺字段 {missing}（R-SCHEMA-01）")

                check_front_matter_shape(fm, rel, errors)

                t, st, i = fm_value(fm, "type"), fm_value(fm, "status"), fm_value(fm, "id")

                if t not in TYPES:
                    errors.append(f"{rel}: type 非法 -> {t!r}（R-SCHEMA-02）")
                else:
                    if st not in ALLOWED_STATUS[t]:
                        errors.append(f"{rel}: type={t} 不允许 status={st!r}（R-SCHEMA-02）")
                    for sec in REQUIRED_SECTIONS[t]:
                        if not has_section(text, sec):
                            errors.append(f"{rel}: 缺必备小节「{sec}」（R-SCHEMA-05）")
                    # FORMAT.md §5：所有类型都必须有 ## 论证（草案下可留空）
                    if not has_section(text, "论证"):
                        errors.append(f"{rel}: 缺必备小节「论证」（所有类型都必须有）（R-SCHEMA-05）")

                if i in ids:
                    errors.append(f"{rel}: id 与 {ids[i]} 重复 -> {i}（R-SCHEMA-03）")
                elif i:
                    ids[i] = rel

                # 只有「命题」可以用「已确证」
                if ONLY_CLAIMS_CAN_BE_CONFIRMED and t != "命题" and st == "已确证":
                    errors.append(
                        f"{rel}: 只有「命题」可以用「已确证」（{t} 不存在唯一正确）（R-SCHEMA-02）")

                if t in TYPES:
                    objects[rel] = {"type": t, "fm": fm, "text": text, "path": path}

        # 代码围栏必须成对
        if text.count("```") % 2 != 0:
            errors.append(f"{rel}: ``` 代码围栏数量为奇数（未闭合）")

        # 链接可达 + 锚点存在（剥掉代码块，模板代码里的链接不检查）
        prose = re.sub(r"```.*?```", "", text, flags=re.S)
        prose = re.sub(r"`[^`\n]*`", "", prose)
        links = re.findall(r"\[([^\]]*)\]\(([^)]+)\)", prose)
        # YAML 里的 `url:`（Issue 模板的 contact_links 用过）也要查——
        # 它同样指向本仓库，改标题一样会改坏它。
        # **但 GitHub Actions 的 `url: ${{ steps... }}` 不是链接**：按 `\S+` 截出来会是
        # `${{` 这一截，于是流水线文件一加进来就报一条假断链。带 `{` 的一律跳过。
        links += [(u, u) for u in re.findall(r"^\s*url:\s*(\S+)", text, re.M)
                  if "{" not in u]
        # R-LINK-03 的豁免：`English version of …` 行是有意指向中文正本的约定行
        en_pointer = set()
        for _ln in prose.splitlines():
            if "English version of" in _ln:
                en_pointer.update(t for _, t in
                                  re.findall(r"\[([^\]]*)\]\(([^)]+)\)", _ln))
        for label, target in links:
            if target.startswith("mailto:"):
                continue
            m = SELF_URL.match(target)
            if m:
                # 指向本仓库的绝对链接：路径**从仓库根算起**，不是从当前文件。
                sp, _, anchor = m.group(1).partition("#")
                cand = ROOT / sp
                if not cand.exists():
                    errors.append(f"{rel}: 链接目标不存在 -> [{label}]({target})（R-LINK-01）")
                    continue
                target_rel = sp
            elif target.startswith("http"):
                continue
            else:
                path_part, _, anchor = target.partition("#")
                path_part = path_part.strip()
                if not path_part:
                    target_rel = rel
                else:
                    cand = path.parent / path_part.replace("/", os.sep)
                    if not cand.exists():
                        errors.append(
                            f"{rel}: 链接目标不存在 -> [{label}]({target})（R-LINK-01）")
                        continue
                    target_rel = os.path.relpath(cand, ROOT).replace(os.sep, "/")
            # R-LINK-03 要等全部对象收齐才能判（目标是不是「有译本的条目」）
            link_records.append((rel, label, target, target_rel, en_pointer))
            if anchor and target_rel.endswith(".md") \
                    and not anchor_ok(target_rel, anchor):
                errors.append(f"{rel}: 锚点不存在 -> [{label}]({target})（R-LINK-02）")

    # 图校验：单看一个文件查不出来的那部分
    check_bilingual_pairs(objects, events, en_docs, errors, warnings)
    check_link_language(link_records, en_docs, objects, events, errors)
    check_graph(objects, errors, warnings)
    check_arguments(objects, errors)
    check_argument_liveness(objects, warnings)
    check_evidence_ids(objects, events, errors)
    check_external_prereqs(objects, errors, warnings)
    check_readme_coverage(objects, errors)
    check_paths(objects, errors, warnings)
    check_path_steps(objects, errors)
    stats, strength = check_path_outcomes(objects, errors, warnings)
    argstats = argument_graph(objects)
    homology = check_support_homology(objects, warnings)
    check_index(objects, events, errors)

    # 单对象规则（FORMAT.md 里写了、此前没有机械检查的那些）
    check_evidence_nonempty(objects, errors)
    check_knowledge_tip(objects, errors)
    check_teaching_level(objects, errors)
    check_medical(objects, errors)
    check_stage(objects, errors)
    check_dates(objects, errors)
    check_author(objects, errors)
    check_section_order(objects, errors)
    check_status_docs(errors)
    check_rule_registry(errors)
    check_license(objects, errors)
    check_id_prefix(objects, errors)
    check_evidence_table(errors)
    check_doc_bilingual(errors)
    check_readme_path_numbers(objects, errors)
    check_type_dir(objects, errors)
    check_status_has_argument(objects, errors)
    check_status_reachability(objects, errors)
    check_updated_matches_changelog(objects, errors)
    check_bilingual_fields(objects, events, en_fm, errors)
    check_attack_has_edge(objects, errors)
    check_readme_status(objects, errors)
    check_body_evidence_ids(objects, errors)
    check_evidence_verified_support(objects, errors)
    # 事件（与知识对象分开的另一套规则）
    check_event_readme(events, errors)
    sync_generated(objects, events, False, errors)

    return md_files, ids, errors, warnings, stats, argstats, objects, events, strength, homology


def main():
    write = "--write-index" in sys.argv
    (md_files, ids, errors, warnings, stats, argstats, objects, events,
     strength, homology) = check_all()

    print(f"扫描 {len(md_files)} 个文档，识别知识对象 {len(objects)} 条，事件 {len(events)} 条")
    print()

    if write:
        paths = write_index(objects, events)
        sync_generated(objects, events, True, [])
        print("已生成 " + " · ".join(p.name for p in paths)
              + f"（{len(objects)} 条对象 + {len(events)} 条事件）+ 文档生成块 —— 请与内容一起提交")
        return 0

    if warnings:
        print("提示（不阻塞）：")
        for w in warnings:
            print(f"  ! {w}")
        print()

    if errors:
        print("不符合规范之处：")
        for e in errors:
            print(f"  x {e}")
        print()
        # 按规则汇总：一次报 20 条时，先看「哪几条规则在响」比逐行读快得多
        by_rule = collections.Counter(
            m.group(1) for m in (re.search(r"（(R-[A-Z]+-[0-9]+)）", e) for e in errors) if m
        )
        if by_rule:
            print("按规则汇总（同一条规则的多处错误通常一个改法）：")
            for rid, n in by_rule.most_common():
                print(f"  {rid:14s} × {n}")
            unlabeled = len(errors) - sum(by_rule.values())
            if unlabeled:
                print(f"  {'（未标 ID）':12s} × {unlabeled}")
            print()
            print("  规则说明：docs/RULES.md")
            print()
        print(f"结果：{len(errors)} 处问题")
        return 1

    print("结果：全部通过")
    print("  · front-matter 完整")
    print("  · type / status 合法（只有「命题」可以用「已确证」）")
    print("  · id 唯一")
    print("  · 链接与锚点全部可达（含指向本仓库的绝对链接）")
    print("  · 每个对象都有来源；知识点有 `[!TIP]`；教法有 `水平档`；医学有免责块")
    print("  · 学段 / 日期 / 署名 取值合法")
    print("  · 人类文档里的统计数字与 index.json 一致")
    print("  · 必备小节齐全且顺序正确")
    print("  · 英文译本的文件名由 `id` 派生，且与中文原件一一对应")
    print("  ── 以下几项是单看一个文件查不出来的 ──")
    print("  · `先修` 边只连「知识点」，且无环")
    print("  · `教法` 都有 `knowledge_point`，且指向「知识点」")
    print("  · `支持` / `攻击` 边都落在具体论证上（锚点存在）")
    print("  · 每条路径的「先修缺口」已机械校验（无缺口）")
    print("  · `已确证` / `争议` / `已推翻` 的结构前提已校验（R-SCHEMA-19）")
    print("  · 可选字段 `外部先修` 的形状 / 枚举 / 来源 / 复发提示已校验（R-SCHEMA-20）")
    for rel, (cov, total) in sorted(stats.items()):
        thin, unread, ceiling = strength.get(rel, ([], [], ""))
        bits = []
        if thin:
            bits.append(f"单环节覆盖 {','.join(thin)}")
        if unread:
            bits.append(f"这些成果的证据最高只到 仅定位/未核验：{','.join(unread)}")
        # 深度这一维**总是**报出来：只报异常会让人分不清「没问题」与「没测」
        bits.append(f"覆盖深度下限 {ceiling or '（无可判定的证据行）'}")
        extra = f"  【{' · '.join(bits)}】" if bits else ""
        print(f"  · 目标覆盖度：{Path(rel).stem} —— {cov}/{total} "
              f"({cov/total:.0%})，无未覆盖成果{extra}")

    sup, atk = argstats
    if sup or atk:
        print("  ── 论证图（进边）──")
        print("  ! 条数不代表强度：来自**同一来源**的多个实例**不是独立证据**"
              "（见 FORMAT.md §6）")
        for rel in sorted(set(sup) | set(atk)):
            bits = []
            if sup.get(rel):
                bits.append(f"支持 {sup[rel]}")
            if atk.get(rel):
                bits.append(f"攻击 {atk[rel]}")
            print(f"    · {Path(rel).stem}：{' · '.join(bits)}")
    if homology:
        print("  ── 支持边的证据构成（可数的事实先摆出来，跨来源是否独立仍要人判 M-03）──")
        for rel, anchor, n, ids, n_origin, obits, cbits in homology:
            print(f"    · {Path(rel).stem} `{anchor}`：{n} 条支持 · "
                  f"{len(ids)} 份证据 · {n_origin} 个来源标识（{obits}）· 类别 {cbits}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
