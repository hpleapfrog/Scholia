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
                 "法律": "law"}

# 证据表的枚举（见 evidence/README.md 表头图例）
EVIDENCE_CATEGORIES = {"教材", "论文", "指南", "官方文件", "交互式模拟",
                       "出版社勘误表", "本库数据"}
EVIDENCE_GRADES = {"高", "中", "低", "—"}
EVIDENCE_DEPTHS = {"全文", "摘要", "仅定位", "未核验", "—"}

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

# 状态的含义（给机器读；与 FORMAT.md §4 一致）
STATUS_MEANING = {
    "草案": "刚写下，尚未自检",
    "待审": "内容完整，但没有任何人独立复核过",
    "有效": "当前没有已知的**存活攻击**；**不等于**已被独立复核",
    "争议": "存活集合里存在结论互相冲突的论证",
    "暂定确认": "作者已核对，但**没有非作者的独立复核**",
    "已确证": "本库最高等级：有**非作者**的独立复核。**（截至生成时，全库一条都没有）**",
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

# 每个学科的覆盖说明（手写；**不写数字**，数字由 objects 自动统计在旁边）
SUBJECT_NOTES = {
    "物理": "覆盖中国高中物理的一部分。按人教版章级主题对照，**一半左右**的章级主题"
            "一条概念都没有（缺口清单见 `knowledge/物理/覆盖度/`）。",
    "地理": "全部是同一本香港教材的勘误。",
    "生活": "出行规则：北京地铁与民航的官方规定（含两份官方文件）。",
    "科学": "一条勘误。",
    "医学": "临床指南与随机试验的结论；一律以「指南 / 研究规定了 X」表述，**不提供诊疗建议**。",
    "交通": "道路交通与轨道交通：只收**官方文件**能核验的结论，不收办事流程。",
    "计算机": "标准与官方文档能定位的结论；**不收教程式步骤**。",
    "经济": "统计数据与权威文本能定位的结论；**不收预测与建议**。",
    "法律": "成文法文本的制度性规定（构成要件 · 期限 · 法律效果）；**不收个案裁判与法律意见**。",
}
SUBJECTS_FALLBACK = "本学科尚无覆盖说明 —— **不要假设它覆盖了什么**，请看 objects。"

# 学科说明的英文版（给 START.en.md 的生成块用）
SUBJECT_NOTES_EN = {
    "物理": "Part of Chinese senior-high physics. Against the PEP chapter-level topics, "
            "about half the chapters have not a single concept here (gap list in `knowledge/物理/覆盖度/`).",
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


def build_index(objects, events):
    """生成机器可读索引。

    **这是本库给 AI 的入口。** 它要解决两个问题：

    1. AI 读了内容之后，**把一条 `失据` 的命题当成既成事实讲出去**
       —— 所以每条都带 `可作事实引用`；
    2. AI 引用时只给一个 `ev-039` 这样的编号，**读者无从核实**
       —— 所以每条都带 `来源`（解析好的真实定位），全局另有一份 `证据索引`。

    `objects` 是知识对象；`事件` 是**并列的另一类记录**（见 EVENT_TYPE 注释），
    单开一节，不进 `objects`、不计入对象总数。
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

    objs = []
    for rel, o in sorted(objects.items()):
        st = fm_value(o["fm"], "status")
        ids = re.findall(r"ev-\d+", o["fm"])
        pre_h = o["text"].split("\n## ", 1)[0]
        _id = fm_value(o["fm"], "id")
        _en = en_path(rel, _id) if _id else None
        objs.append({
            "id": _id,
            "type": o["type"],
            "title": fm_value(o["fm"], "title"),
            "status": st,
            "path": rel,
            # 英文译本的路径（文件名由 id 派生）；没有译本时为 null。
            # **AI 引用时说中文页还是英文页要说得出来**——只给一个 path，
            # 英文读者会被送去中文文件。
            "path_en": _en if _en and (ROOT / _en).exists() else None,
            "学科": fm_nested(o["fm"], "学科"),
            "学段": fm_nested(o["fm"], "学段"),
            "适用": fm_nested(o["fm"], "适用"),
            "条件": fm_nested(o["fm"], "条件"),
            "免责块在正文最前": "> [!CAUTION]" in pre_h,
            "证据": ids,
            "来源": src_list(ids),
            "先修": [Path(x).name for x in fm_links(o["fm"], "先修")],
            "论证": sorted(arg_ids(o["text"])),
            "可作事实引用": st not in NOT_CITABLE,
            "引用时须写明": (f"state={st}"
                        + ("；本库判定它**没有说话算数的论证**" if st in NOT_CITABLE else "")),
        })

    by_type, by_status, by_subject = collections.Counter(), collections.Counter(), collections.Counter()
    for x in objs:
        by_type[x["type"]] += 1
        by_status[x["status"]] += 1
        by_subject[x["学科"].split(" ")[0]] += 1

    # 事件：与 objects 并列的一节。只有证据，没有论证、没有边。
    events_list = []
    for rel, o in sorted(events.items()):
        ids = re.findall(r"ev-\d+", o["fm"])
        events_list.append({
            "id": fm_value(o["fm"], "id"),
            "title": fm_value(o["fm"], "title"),
            "status": fm_value(o["fm"], "status"),
            "path": rel,
            "path_en": en_path(rel, fm_value(o["fm"], "id"))
                       if fm_value(o["fm"], "id") and
                       (ROOT / en_path(rel, fm_value(o["fm"], "id"))).exists() else None,
            "证据": ids,
            "来源": src_list(ids),
            "最后更新": fm_value(o["fm"], "updated"),
        })

    return {
        "$comment": "由 tools/kbcheck.py 生成，**请勿手改**。运行 `python tools/kbcheck.py --write-index` 重新生成。",
        "schema_version": 2,
        "repo": "https://github.com/hpleapfrog/Scholia",
        "读到这个文件的 AI 请注意": [
            "**本库是跨学科的**，覆盖程度**按学科差别很大**；它**不只做物理**。",
            "**本库没有任何一条处于 `已确证`。** 不要把这里的任何内容当作『已确证的事实』转述。",
            "`可作事实引用=false` 的条目（状态为 失据/已推翻/已失效）**不要引用**。",
            "引用任何一条时，**请把它的 `证据` 解析成 `证据索引` 里那条的真实定位**"
            "（书名 / 章节 / 页面 URL），并**连 `status` 一起给出** —— **只写「ev-039」等于没写来源**。",
            "**判断「本库有没有 X」要查本文件的 `objects`，不要凭印象。**",
            "每条对象有两个路径：`path` 是**中文正本**，`path_en` 是**英文译本**"
            "（文件名由 `id` 派生，同目录；没有译文时为 null）。"
            "**给英文读者引用时请用 `path_en`，不要把中文文件名发给对方。**",
            "本文件顶层的 `事件` 与 `objects` **是两回事**：`objects` 是知识对象"
            "（命题/知识点/…），`事件` 是**按时间记录事实**的另一类记录，"
            "**不含论证、不可作真值判断**；引用事件时给 `status`（持续更新/已封存）"
            "与 `来源`，**不要说「本库确认了」某事件**。",
            "本库里**没有**的内容，**不要算作本库的内容** —— "
            "你可以用别的来源回答，**但要说明那不是本库说的**。",
            "教法（type=教法）的证据主要是**一本美国教材**，**不代表在中国课堂实测有效**。",
            "**转述任何对象前，先看它的 `适用` / `条件` / `免责块在正文最前`** —— "
            "限定不是免责声明的装饰：医学条目的操作参数**只在该人群与条件下成立**，"
            "转述时**必须把限定连同数字一起给出**；`免责块在正文最前=true` 的条目，"
            "**转述前必须读 `path` 指向的文件正文开头**。",
        ],
        "状态含义": STATUS_MEANING,
        "状态英文": STATUS_EN,
        "事件状态含义": EVENT_STATUS_MEANING,
        "事件状态英文": EVENT_STATUS_EN,
        "统计": {
            "对象总数": len(objs),
            "按类型": dict(sorted(by_type.items())),
            "按状态": dict(sorted(by_status.items())),
            "按学科": dict(sorted(by_subject.items())),
            "已确证条数": by_status.get("已确证", 0),
            "事件条数": len(events_list),
            "证据条数": len(evidence),
            "作废证据条数": sum(1 for e in evidence.values() if e["作废"]),
        },
        "known_limits": {
            "总览": "本库是**跨学科**的，**各学科覆盖程度差别很大**。"
                    "判断「有没有 X」请查 `objects`（或该学科的 `knowledge/<学科>/README.md`），"
                    "**不要假设它覆盖了什么**。",
            "按学科": {
                s: {"条数": n, "说明": SUBJECT_NOTES.get(s, SUBJECTS_FALLBACK)}
                for s, n in sorted(by_subject.items())
            },
            "教法来源": "绝大多数整理自 OpenStax《Physics》（美国高中教材，CC BY），"
                    "记录的是「这本教材建议怎么教」，**不是**「这样教有效」。",
            "程序性知识": "本库**不装**「怎么做一件事」的流程（见 FORMAT.md「本库不装什么」）。",
        },
        "证据索引": evidence,
        "objects": objs,
        "事件": events_list,
    }


def check_index(objects, events, errors):
    """`index.json` 必须与内容一致——不一致就报错，并告诉怎么修。

    **这是「防止信息是错的」的机制部分**：索引不能手写、不能过期。
    """
    want = json.dumps(build_index(objects, events), ensure_ascii=False, indent=2, sort_keys=False) + "\n"
    if not INDEX_FILE.exists():
        errors.append("index.json 不存在 —— 运行 `python tools/kbcheck.py --write-index` 生成")
        return
    have = INDEX_FILE.read_text(encoding="utf-8").replace("\r\n", "\n")
    if have != want:
        errors.append(
            "index.json **与内容不一致**（内容改过但索引没重新生成）—— "
            "运行 `python tools/kbcheck.py --write-index`，然后一起提交")


def write_index(objects, events):
    INDEX_FILE.write_text(
        json.dumps(build_index(objects, events), ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8")
    return INDEX_FILE


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
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", "__pycache__"}]
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
    """取出 front-matter 里某个键（含缩进块形式）中的 Markdown 链接目标。"""
    m = re.search(rf"^[ \t]*{key}:\s*(.+)$", fm, re.M)
    if m:
        line = m.group(1)
    else:
        b = re.search(rf"^[ \t]*{key}:\s*\n((?:[ \t]+.*\n?)*)", fm, re.M)
        line = b.group(1) if b else ""
    return re.findall(r"\[[^\]]*\]\(([^)]+)\)", line)


def fm_nested(fm, key):
    """取 front-matter 里可能是缩进（如 scope 下）的键值。"""
    m = re.search(rf"^[ \t]*{key}:\s*(.+)$", fm, re.M)
    return m.group(1).strip() if m else ""


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
                f"裸标量不允许（需加引号）—— 严格 YAML 解析器会报错")


STAGES = ("小学", "初中", "高中", "大学")


def stages_of(obj):
    """从 scope.学段 解析出学段集合，例如「初中至高中」-> {初中, 高中}。"""
    v = fm_nested(obj["fm"], "学段")
    return {s for s in STAGES if s in v}


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
                    errors.append(f"{rel}: `{key}` 指向的不是知识对象 -> {tgt}")
                    continue
                if not anchor:
                    errors.append(
                        f"{rel}: `{key}` 必须带论证锚点（如 `#a1`）-> {tgt}"
                        f"；只指向条目无法定位被攻击的是哪条论证")
                    continue
                ids = arg_ids(dest["text"])
                if not ids:
                    errors.append(f"{rel}: `{key}` 指向的条目里没有可定位的论证 ID -> {tgt}")
                elif anchor not in ids:
                    errors.append(
                        f"{rel}: `{key}` 的锚点 `#{anchor}` 在目标条目里不存在"
                        f"（该条目可用: {', '.join('#' + x for x in sorted(ids))}）")

        # 同一条目内论证 ID 必须唯一
        raw = [x.lower() for x in ARG_ID.findall(section_body(o["text"], "论证") or "")]
        dup = [x for x, c in collections.Counter(raw).items() if c > 1]
        if dup:
            errors.append(f"{rel}: `## 论证` 里论证 ID 重复 {sorted(set(dup))}")


def check_graph(objects, errors, warnings):
    """先修关系与教法归属的图校验 —— 这些是单看一个文件查不出来的。"""
    prereq = {}

    for rel, o in objects.items():
        t, fm, path = o["type"], o["fm"], o["path"]

        # 先修边只能连「知识点」
        for tgt in fm_links(fm, "先修"):
            r = resolve_link(path, tgt)
            dest = objects.get(r) if r else None
            if t != "知识点":
                errors.append(
                    f"{rel}: 只有「知识点」可以有 `先修` 边（FORMAT.md §2），本条 type={t}")
            if dest is None:
                errors.append(f"{rel}: `先修` 指向的不是知识对象 -> {tgt}")
            elif dest["type"] != "知识点":
                errors.append(
                    f"{rel}: `先修` 必须指向「知识点」，实际指向 type={dest['type']} -> {tgt}")
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
                errors.append(f"{rel}: 「教法」缺 `knowledge_point`（FORMAT.md §4）")
            for tgt in kps:
                r = resolve_link(path, tgt)
                dest = objects.get(r) if r else None
                if dest is None:
                    errors.append(f"{rel}: `knowledge_point` 指向的不是知识对象 -> {tgt}")
                elif dest["type"] != "知识点":
                    errors.append(
                        f"{rel}: `knowledge_point` 必须指向「知识点」，实际 type={dest['type']}")

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
                    Path(x).stem for x in stack[i:] + [m]))
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
        prose = re.sub(r"```.*?```", "", o["text"], flags=re.S)

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

        external = set()
        for tgt in fm_links(o["fm"], "先修"):
            r = resolve_link(o["path"], tgt)
            if r:
                external.add(r)

        for r in sorted(refs):
            for p in fm_links(objects[r]["fm"], "先修"):
                pr = resolve_link(objects[r]["path"], p)
                if pr and pr not in refs and pr not in external:
                    errors.append(
                        f"{rel}: 先修缺口 —— 引用了「{Path(r).stem}」，"
                        f"但它的先修「{Path(pr).stem}」不在本路径内，也未声明为外部先修")

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
                    f"—— 路径是「知识点的编排」，指不出对象的步骤不是环节")


def check_path_outcomes(objects, errors, warnings):
    """目标覆盖度 —— 从前是人工判断，这里改成机械校验。

    路径在 front-matter 声明 `outcomes`（可观测的学习成果，编号 o1/o2/…），
    并在 `## 编排` 表里为每个环节标注它覆盖哪些成果。校验器检查：
    每个声明的成果是否至少被一个环节覆盖。
    """
    stats = {}
    for rel, o in objects.items():
        if o["type"] != "路径":
            continue

        m = re.search(r"^outcomes:\s*\n((?:[ \t]+.*\n?)*)", o["fm"], re.M)
        block = m.group(1) if m else ""
        declared = re.findall(r"\b(o\d+)\b", block)

        if not declared:
            warnings.append(
                f"{rel}: 未声明 `outcomes` —— 目标覆盖度无法机械校验（仍是人工判断）")
            continue

        body = section_body(o["text"], "编排") or ""
        covered = set(re.findall(r"\b(o\d+)\b", body))

        missing = [x for x in declared if x not in covered]
        stats[rel] = (len(declared) - len(missing), len(declared))

        if missing:
            errors.append(
                f"{rel}: 目标覆盖度不足 —— 以下学习成果没有任何环节覆盖: {missing}")
        extra = covered - set(declared)
        if extra:
            errors.append(
                f"{rel}: 编排里覆盖了未声明的成果编号: {sorted(extra)}")

    return stats


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
        ids = re.findall(r"ev-\d+", o["fm"], re.I)
        for ev in sorted({x.lower() for x in ids}):
            if ev not in known:
                errors.append(f"{rel}: `evidence` 引用了索引里没有的编号 -> {ev}")
            elif ev in void:
                errors.append(
                    f"{rel}: `evidence` 引用了**已作废**的编号 -> {ev}"
                    f"（作废的证据不能再来支撑结论）")


def check_readme_coverage(objects, errors):
    """每个知识对象都必须在**它所属学科的 README** 里被提到。

    **为什么要有这一条**：本库的 `物理/README.md` 是读者进库后的第一张表。
    它**漏过两次**——一次是 5 条 `教法`（被一次对抗审查发现），
    一次是 9 条（第 4 批 5 条 + 第 5 批 4 条，**我自己写完忘了登记**）。

    **索引不会自己追上内容。** 这一条把它变成机械可查的：
    文件名（`<name>.md`）必须出现在 `knowledge/<学科>/README.md` 里。
    """
    for rel, o in objects.items():
        parts = Path(rel).parts
        if len(parts) < 3 or parts[0] != "knowledge":
            continue
        subject_readme = ROOT / parts[0] / parts[1] / "README.md"
        if not subject_readme.exists():
            errors.append(f"{rel}: 所属学科缺少 README -> knowledge/{parts[1]}/README.md")
            continue
        if o["path"].name not in subject_readme.read_text(encoding="utf-8"):
            errors.append(
                f"{rel}: **学科 README 里没有登记它**"
                f"（`knowledge/{parts[1]}/README.md` 必须提到 `{o['path'].name}`）")


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
    m = re.search(r"^evidence:\s*(.+)$", fm, re.M)
    return re.findall(r"ev-\d+", m.group(1)) if m else []


def check_evidence_nonempty(objects, errors):
    """**无来源不入库**。`evidence: []` 不算有来源。"""
    for rel, o in objects.items():
        if not evidence_ids_of(o["fm"]):
            errors.append(
                f"{rel}: `evidence` 为空 —— 本库「无来源不入库」，"
                "每个对象至少引一条证据（FORMAT.md §3）")


def check_knowledge_tip(objects, errors):
    """`知识点` 正文第一行必须是「读完你会什么」的 `> [!TIP]`。"""
    for rel, o in objects.items():
        if o["type"] != "知识点":
            continue
        after = o["text"].split("---\n", 2)[-1]
        first = next((ln.strip() for ln in after.splitlines() if ln.strip()), "")
        if not first.startswith("> [!TIP]"):
            errors.append(
                f"{rel}: `知识点` 正文第一行必须是 `> [!TIP]`（读完你会什么）")


def check_teaching_level(objects, errors):
    """`教法` 必须有 `scope.水平档`；值是档位代码（可多档）或「不分档」。"""
    for rel, o in objects.items():
        if o["type"] != "教法":
            continue
        lv = fm_nested(o["fm"], "水平档")
        if not lv:
            errors.append(
                f"{rel}: `教法` 缺 `scope.水平档`（BL / OL / AL 组合，"
                "或跨全部档位的「不分档」）")
            continue
        codes = set(re.findall(r"\b(BL|OL|AL)\b", lv))
        if LEVEL_UNDIVIDED not in lv and not codes:
            errors.append(f"{rel}: `水平档` 无法识别 -> {lv!r}")


def check_medical(objects, errors):
    """医学条目必须有 `scope.条件`，且正文开头是免责 `> [!CAUTION]` 块。

    见 `knowledge/医学/README.md`「边界的一次修正（2026-10-12）」：
    指南原文的规定可以收录，但必须带人群限定与免责，且以「指南规定了 X」表述。
    """
    for rel, o in objects.items():
        if "医学" not in fm_nested(o["fm"], "学科"):
            continue
        if not fm_nested(o["fm"], "条件"):
            errors.append(f"{rel}: 医学条目必须有 `scope.条件`（人群与限定）")
        head = o["text"].split("\n## ", 1)[0]
        if "> [!CAUTION]" not in head:
            errors.append(
                f"{rel}: 医学条目正文开头必须有 `> [!CAUTION]` 免责块"
                "（人群限定 + 非医疗建议）")


def check_stage(objects, errors):
    """`scope.学段` 只能用枚举值，组合用「至」。"""
    for rel, o in objects.items():
        v = fm_nested(o["fm"], "学段")
        if not v:
            errors.append(f"{rel}: 缺 `scope.学段`")
            continue
        for part in re.split(r"[至、,，]", v):
            part = part.strip()
            if part and part not in ALLOWED_STAGES:
                errors.append(
                    f"{rel}: `学段` 取值非法 -> {v!r}"
                    "（允许 小学/初中/高中/大学/不限，组合用「至」）")


def check_dates(objects, errors):
    for rel, o in objects.items():
        c, u = fm_value(o["fm"], "created"), fm_value(o["fm"], "updated")
        ok = True
        for k, val in (("created", c), ("updated", u)):
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(val or "")):
                errors.append(f"{rel}: `{k}` 必须是 YYYY-MM-DD -> {val!r}")
                ok = False
        if ok and u < c:
            errors.append(f"{rel}: `updated`（{u}）早于 `created`（{c}）")


def check_author(objects, errors):
    for rel, o in objects.items():
        a = (fm_value(o["fm"], "author") or "").strip().strip('"')
        if not a:
            errors.append(f"{rel}: 缺 `author`（不可匿名）")
        elif not (a.startswith("@") or a.startswith("AI")):
            errors.append(
                f"{rel}: `author` 应形如 `@handle` 或 "
                f"`AI（模型）· 经 @某人复核 · 日期` -> {a!r}")


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
                f"{rel}: 必备小节顺序应为 {' · '.join(order)}（FORMAT.md §1.3）")


def check_status_docs(errors):
    """状态词表写了好几处，最容易漏。要求人类文档列全（FORMAT.md §4 + 学科图例）。"""
    all_status = set()
    for s in ALLOWED_STATUS.values():
        all_status |= s
    for rel in ("FORMAT.md", "knowledge/README.md"):
        text = _repo_text(rel)
        missing = sorted(s for s in all_status if s not in text)
        if missing:
            errors.append(f"{rel}: 状态图例不全，缺 {missing}")


def check_license(objects, errors):
    """知识内容统一 CC BY-SA 4.0（见 LICENSE）。"""
    for rel, o in objects.items():
        v = (fm_value(o["fm"], "license") or "").strip()
        if v != ALLOWED_LICENSE:
            errors.append(f"{rel}: `license` 必须是 {ALLOWED_LICENSE} -> {v!r}")


def check_id_prefix(objects, errors):
    """`id` 前缀必须与学科一致（防止跨学科编号漂移）。"""
    for rel, o in objects.items():
        subj = (fm_nested(o["fm"], "学科") or "").split()
        subj = subj[0] if subj else ""
        slug = SUBJECT_SLUGS.get(subj)
        if not slug:
            errors.append(f"{rel}: 未知 / 缺失学科 -> {subj!r}（见 SUBJECT_SLUGS）")
            continue
        i = fm_value(o["fm"], "id") or ""
        if not i.startswith(f"kb:{slug}:"):
            errors.append(
                f"{rel}: `id` 前缀应与学科一致（`kb:{slug}:…`）-> {i!r}")


def check_evidence_table(errors):
    """证据表的 `类别` / `等级` / `核验深度` 必须是枚举值（作废行除外）。"""
    for ev, r in parse_evidence_index().items():
        if r["作废"]:
            continue
        if r["类别"] not in EVIDENCE_CATEGORIES:
            errors.append(f"evidence/README.md: {ev} 类别非法 -> {r['类别']!r}")
        if r["等级"] not in EVIDENCE_GRADES:
            errors.append(f"evidence/README.md: {ev} 等级非法 -> {r['等级']!r}")
        if r["核验深度"] not in EVIDENCE_DEPTHS:
            errors.append(f"evidence/README.md: {ev} 核验深度非法 -> {r['核验深度']!r}")


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
        ids = re.findall(r"ev-\d+", o["fm"])
        known = {e: ev[e] for e in ids if e in ev and not ev[e]["作废"]}
        if not known:
            continue                      # 缺编号 / 作废由 R-EVID-01 管
        if all(r["核验深度"] in UNREAD_DEPTHS for r in known.values()):
            detail = " · ".join(f"{e}={r['核验深度']}" for e, r in known.items())
            errors.append(
                f"{rel}: `status` 是「{st}」，但它的证据**没有一条读过**"
                f"（{detail}）—— 没读过就不能说「确认」；"
                "把核验深度补成 `全文`/`摘要`，或把状态退回 `待审`")


# ── 生成块：人类文档里的数字/清单，唯一来源是本脚本 ────────────────────────
GENERATED_BEGIN = "<!-- kbcheck:begin -->"
GENERATED_END = "<!-- kbcheck:end -->"

SUBJECT_ORDER = ["物理", "生活", "医学", "地理", "科学",
                 "交通", "计算机", "经济", "法律"]
TYPE_ORDER = ["教法", "知识点", "命题", "误解", "资源", "路径"]
TYPE_EN = {"教法": "methods", "知识点": "concepts", "命题": "claims",
           "误解": "misconceptions", "资源": "resources", "路径": "paths"}
SUBJECT_EN = {"物理": "Physics", "生活": "Life", "医学": "Medicine",
              "地理": "Geography", "科学": "Science",
              "交通": "Transport", "计算机": "Computing", "经济": "Economics",
              "法律": "Law"}

# ── 规则注册表：每条规则一个 ID，分「机械校验」与「人工复核」──────────────
# 改了任何一条规则，**必须同时改这里的清单与对应的检查**——否则 R-INDEX-02 会失败。
# 这就是「规则即代码」：规则不再散在散文里，而是可枚举、可校验的清单。
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
    ("R-EVENT-01", "`事件` 单开顶层 `events/`，与 `objects` **分开**：`type`=事件、`status` 只用持续更新/已封存、必填段 陈述/依据/变更记录、**无论证、无任何边**、`id` 前缀 `kb:event:`、`evidence` 非空；且每个事件须登记在 `events/README.md`"),
    ("R-LINK-01", "链接目标存在（相对链接 · 指向本仓库的绝对链接 · YAML `url:`）"),
    ("R-LINK-02", "锚点存在（标题 slug 或论证 ID）"),
    ("R-BILING-01", "英译本文件名由 `id` 派生（`<id 末段去类型前缀>.en.md`，与中文原件同目录）；缺译本给提示、不判失败"),
    ("R-LINK-03", "英文页面的站内链接指向英文页（该页存在时）；例外：`English version of` 行、指向无译本文件的链接"),
    ("R-GRAPH-01", "`先修` 只连「知识点」，且无环"),
    ("R-GRAPH-02", "`支持` / `攻击` 边的论证锚点存在"),
    ("R-GRAPH-03", "`路径` 每个成果至少被一个环节覆盖（未声明 outcomes 给警告）"),
    ("R-GRAPH-04", "`路径` 每个环节至少连到一个库内对象"),
    ("R-EVID-01", "`evidence` 编号已登记且未作废"),
    ("R-EVID-02", "证据表 `类别` / `等级` / `核验深度` 取值合法"),
    ("R-EVID-03", "`暂定确认` / `已确证` 必须至少有一条 `核验深度` 为 `全文` / `摘要` 的证据（没读过不能说确认）"),
    ("R-INDEX-01", "`index.json` 与内容一致（改内容必须重生成）"),
    ("R-INDEX-02", "人类文档的生成块与来源一致（README 统计 · START 学科总览 · knowledge 索引 · 物理覆盖度统计 · 规则表）"),
    ("R-README-01", "每个对象都在所属学科 README 里登记"),
    ("R-DOC-01", "状态图例在 FORMAT.md 与 knowledge/README.md 里列全"),
]

MANUAL_RULES = [
    ("M-01", "英文引用附近必须有中文说明（面向学习者可读性三条之一）"),
    ("M-02", "面向学习者的内容写在前面"),
    ("M-03", "`支持` 边的**独立性**由人判断（来源是自由文本，算不出）"),
    ("M-04", "`教法` 的 `禁忌` 标注证据强度（强/弱），且与 `风险` 不混"),
    ("M-05", "不上传教材原文或扫描页"),
    ("M-06", "新引用资源逐条核对许可（教材 CC BY ≠ 它嵌的东西也是）"),
    ("M-07", "AI 攻击需人复核 + 署名披露（AI 不能当「已确证」的复核者）"),
    ("M-08", "统计数字不手写（交给 `--write-index` 生成）"),
    ("M-09", "对抗任务派发必须包含「质疑证据是否真实存在」与「质疑来源是否为本次引用而伪造」"),
    ("M-10", "文档中英成对存放（`<name>.md` 中文 + 同目录 `<id 派生>.en.md` 英文），改一份同步另一份"),
    ("M-11", "注册证据过**来源三问**：谁发布的（可问责主体）· 是哪个版本、什么时候生效（条目只声明该版本如此）· 是不是为这次引用现造的（有独立于本主张而存在的理由，且能在不同发布主体处找到第二来源；同源转载不算）；自建站点 / 无主体转载页 / 反查不到的标识符不登记"),
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
    ("R-EVENT-01", "`事件` lives top-level in `events/`, **separate** from `objects`: `type`=event, `status` only 持续更新/已封存, required sections 陈述/依据/变更记录, **no argument and no edges**, `id` prefix `kb:event:`, non-empty `evidence`; each event must be registered in `events/README.md`"),
    ("R-LINK-01", "link targets exist (relative · repo-absolute · YAML `url:`)"),
    ("R-LINK-02", "anchors exist (heading slug or argument id)"),
    ("R-BILING-01", "an English edition's filename is derived from its `id` (`<id-tail minus type prefix>.en.md`, same folder as the Chinese original); a missing translation is a notice, not a failure"),
    ("R-LINK-03", "links inside an English page point at the English page (when it exists); exempt: `English version of` lines and links to files that have no translation"),
    ("R-GRAPH-01", "`先修` connects only 知识点, acyclic"),
    ("R-GRAPH-02", "`支持` / `攻击` edge argument anchors exist"),
    ("R-GRAPH-03", "`路径` each outcome covered by ≥1 环节 (undeclared outcomes → warning)"),
    ("R-GRAPH-04", "`路径` each 环节 connects to ≥1 in-repo object"),
    ("R-EVID-01", "`evidence` id registered and not voided"),
    ("R-EVID-02", "evidence table `类别` / `等级` / `核验深度` values valid"),
    ("R-EVID-03", "`暂定确认` / `已确证` needs ≥1 evidence with `核验深度` of `全文` / `摘要` (unread can't be confirmed)"),
    ("R-INDEX-01", "`index.json` consistent with content (regenerate on change)"),
    ("R-INDEX-02", "human-doc generated blocks match their source (README stats · START subject overview · knowledge index · physics coverage stats · rule table)"),
    ("R-README-01", "every object registered in its subject README"),
    ("R-DOC-01", "status legend listed in FORMAT.md and knowledge/README.md"),
]

MANUAL_RULES_EN = [
    ("M-01", "Chinese gloss near English quotations (one of three readability rules)"),
    ("M-02", "learner-facing content comes first"),
    ("M-03", "`支持` edge **independence** is judged by humans (source is free text, can't compute)"),
    ("M-04", "`教法` `禁忌` marks evidence strength (strong/weak), not mixed with `风险`"),
    ("M-05", "don't upload textbook originals or scans"),
    ("M-06", "check license per new source (textbook CC BY ≠ what it embeds is too)"),
    ("M-07", "AI attack needs human review + author disclosure (AI can't be the reviewer for 已确证)"),
    ("M-08", "statistics not hand-written (generated by `--write-index`)"),
    ("M-09", "adversarial dispatch must include \"question whether the evidence really exists\" and \"question whether the source was fabricated for this citation\""),
    ("M-10", "documents stored bilingually (`<name>.md` Chinese + `<id-derived>.en.md` English in the same folder); sync both"),
    ("M-11", "new evidence passes the **three source questions**: who publishes it (an accountable body) · which version and when it took effect (the entry claims only that version) · was it made up for this citation (it exists for reasons independent of the claim, and a second source can be found at a different publishing body; same-origin reposts don't count); self-built sites, attribution-free repost pages and identifiers that don't resolve are not registered"),
]


def render_stats_block(index):
    s = index["统计"]
    by, sub = s["按类型"], s["按学科"]
    types = " · ".join(f"{k} {TYPE_EN[k]} {by[k]}" for k in TYPE_ORDER if by.get(k))
    subs = " · ".join(f"{k} {SUBJECT_EN[k]} {sub[k]}" for k in SUBJECT_ORDER if sub.get(k))
    return "\n".join([
        "| | |",
        "|---|---|",
        f"| 对象 / Objects | **{s['对象总数']}** —— {types} |",
        f"| 事件 / Events | **{s.get('事件条数', 0)}** —— 顶层 `events/`，与对象**分开**（无论证、无真值） |",
        f"| 学科 / Subjects | {subs} |",
        f"| 证据 / Evidence | {s['证据条数']}（含作废 / void {s['作废证据条数']}） |",
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
        lines.append(f"| [{name}](knowledge/{k}/README{suffix}) | {sum(c.values())} "
                     f"| {bits} | {note} |")
    lines.append(f"| **{'Total' if en else '合计'}** | **{index['统计']['对象总数']}** "
                 f"| — | — |")
    return "\n".join(lines)


def render_coverage_block():
    """`knowledge/物理/覆盖度/README.md` 的统计表 —— 从**同一页的总览表**数出来。

    **这一条是真事故**：总览表逐行标了 🟢/🟡/🔴，但下面手写的统计写着「6 · 10 · 11」（共 27），
    而表里只有 25 行、实际是 5 · 7 · 13。**统计与它自己的表对不上，而没有人能一眼看出来。**
    既然数字能从表里数出来，就不该手写。
    """
    p = ROOT / "knowledge" / "物理" / "覆盖度" / "README.md"
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
        lines.append(f"| [{k}]({k}/README.md) | {sub[k]} |")
    ev = index["统计"].get("事件条数", 0)
    if ev:
        lines.append(f"| [事件（顶层）](../events/README.md) | {ev} |")
    lines.append(f"| **合计** | **{index['统计']['对象总数']}** |")
    return "\n".join(lines)


def render_rules_block():
    lines = [
        f"**机械校验（{len(MECH_RULES)} 条）** —— 由 `tools/kbcheck.py` 强制；改规则必须同步改检查：",
        "", "| ID | 规则 |", "|---|---|",
    ]
    for rid, text in MECH_RULES:
        lines.append(f"| `{rid}` | {text} |")
    lines += [
        "",
        f"**人工复核（{len(MANUAL_RULES)} 条）** —— 无法机械化，按 [CONTRIBUTING](../CONTRIBUTING.md) 的自检表执行：",
        "", "| ID | 规则 |", "|---|---|",
    ]
    for rid, text in MANUAL_RULES:
        lines.append(f"| `{rid}` | {text} |")
    return "\n".join(lines)


def render_rules_block_en():
    lines = [
        f"**Mechanically enforced ({len(MECH_RULES_EN)})** — enforced by `tools/kbcheck.py`; change a rule, change the check:",
        "", "| ID | Rule |", "|---|---|",
    ]
    for rid, text in MECH_RULES_EN:
        lines.append(f"| `{rid}` | {text} |")
    lines += [
        "",
        f"**Human-reviewed ({len(MANUAL_RULES_EN)})** — not mechanizable; run the checklist in [CONTRIBUTING](../CONTRIBUTING.en.md):",
        "", "| ID | Rule |", "|---|---|",
    ]
    for rid, text in MANUAL_RULES_EN:
        lines.append(f"| `{rid}` | {text} |")
    return "\n".join(lines)


def generated_blocks(objects, events):
    index = build_index(objects, events)
    blocks = {
        "README.md": render_stats_block(index),
        "README.en.md": render_stats_block(index),
        "knowledge/README.md": render_subject_block(index),
        "START.md": render_subject_overview_block(index),
        "START.en.md": render_subject_overview_block(index, en=True),
        "docs/RULES.md": render_rules_block(),
        "docs/RULES.en.md": render_rules_block_en(),
    }
    cov = render_coverage_block()
    if cov:
        blocks["knowledge/物理/覆盖度/README.md"] = cov
    return blocks


def sync_generated(objects, events, write, errors):
    """人类文档里的数字/清单由本脚本生成——**不手写**（写了就会漂移）。"""
    for rel, body in generated_blocks(objects, events).items():
        p = ROOT / rel
        if not p.exists():
            errors.append(f"{rel}: 文件不存在（生成块的目标文件）")
            continue
        text = p.read_text(encoding="utf-8").replace("\r\n", "\n")
        if GENERATED_BEGIN not in text or GENERATED_END not in text:
            errors.append(
                f"{rel}: 缺少生成块标记（{GENERATED_BEGIN} / {GENERATED_END}）")
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
                    " —— 运行 `python tools/kbcheck.py --write-index`")


def check_event_object(fm, text, rel, ids, events, errors):
    """校验一个 `事件` 条目（与知识对象分开的另一套规则）。

    事件记录「发生了什么」：只有陈述/依据/变更记录，没有论证、没有边；
    `evidence` 必须非空（事件只需要证据，证据为空等于没有事件）。
    """
    keys = front_matter_keys(fm)
    dup = [k for k, c in collections.Counter(keys).items() if c > 1]
    if dup:
        errors.append(f"{rel}: front-matter 顶层键重复 {dup}")
    missing = [k for k in EVENT_FIELDS if k not in keys]
    if missing:
        errors.append(f"{rel}: 事件 front-matter 缺字段 {missing}")
    check_front_matter_shape(fm, rel, errors)

    t, st, i = fm_value(fm, "type"), fm_value(fm, "status"), fm_value(fm, "id")
    if t != EVENT_TYPE:
        errors.append(f"{rel}: `事件` 的 `type` 必须是 {EVENT_TYPE!r} -> {t!r}")
    if st not in EVENT_STATUS:
        errors.append(
            f"{rel}: `事件` 的 `status` 只能是 {'/'.join(sorted(EVENT_STATUS))} -> {st!r}")
    for sec in EVENT_SECTIONS:
        if f"## {sec}" not in text:
            errors.append(f"{rel}: 事件缺必备小节「{sec}」")
    if not (i or "").startswith(EVENT_ID_PREFIX):
        errors.append(f"{rel}: `事件` 的 `id` 前缀必须是 {EVENT_ID_PREFIX!r} -> {i!r}")
    if i in ids:
        errors.append(f"{rel}: id 与 {ids[i]} 重复 -> {i}")
    elif i:
        ids[i] = rel

    # 事件没有边：不安全
    for key in ("edges", "先修", "支持", "攻击"):
        if re.search(rf"^[ \t]*{key}:", fm, re.M):
            errors.append(
                f"{rel}: `事件` 不应有 `{key}`（事件记录事实，不分先修、不支持、不攻击）")

    # 事件只需要证据：证据为空等于没有事件
    if not re.findall(r"ev-\d+", fm):
        errors.append(
            f"{rel}: `事件` 的 `evidence` 为空 —— 事件只需要证据，证据为空等于没有事件")

    events[rel] = {"fm": fm, "text": text}


def check_event_readme(events, errors):
    """每个 `事件` 都必须在 `events/README.md` 里被登记。"""
    p = ROOT / EVENT_DIR / "README.md"
    if not p.exists():
        if events:
            errors.append(f"{EVENT_DIR}README.md 不存在（事件目录需要索引）")
        return
    txt = p.read_text(encoding="utf-8")
    for rel in events:
        name = rel.split("/")[-1]
        if name not in txt:
            errors.append(
                f"{rel}: **事件索引里没有登记它**"
                f"（`{EVENT_DIR}README.md` 必须提到 `{name}`）")


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
        name = rel.split("/")[-1]
        # README 与规格文档（FORMAT / CONTRIBUTING / docs/…）本来就没有 id，
        # 它们不是「某个条目的译本」，不参与配对。
        is_page = (rel.startswith("knowledge/") or rel.startswith(EVENT_DIR + "/")) \
            and not name.startswith("README")
        if not is_page and not oid:
            continue
        if not oid:
            errors.append(f"{rel}: 英文译本缺 front-matter `id`（必须与中文原件同一个 id）")
            continue
        if oid not in zh_by_id:
            errors.append(f"{rel}: 英文译本的 `id` 在中文原件里找不到 -> {oid}")
            continue
        want = en_path(zh_by_id[oid], oid)
        if rel != want:
            errors.append(f"{rel}: 英文文件名必须由 `id` 派生 -> 应为 {want}"
                          f"（英文文件名里不该出现中文）")
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
            errors.append(f"{rel}: R-LINK-03 英文页面的链接指向了中文页 -> "
                          f"[{label}]({target}) 应为 {alt_rel}"
                          "（确需指向中文原件时，把该链接写在 `English version of` 行里）")


def check_all():
    errors = []
    warnings = []
    ids = {}
    objects = {}
    events = {}
    en_docs = {}          # 英文译本：rel -> 它的 id（None = 缺 id）
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

        if is_event:
            if fm is None:
                errors.append(f"{rel}: 事件缺 front-matter")
            else:
                check_event_object(fm, text, rel, ids, events, errors)
        elif is_object:
            if fm is None:
                errors.append(f"{rel}: 知识对象缺 front-matter")
            else:
                keys = front_matter_keys(fm)
                dup = [k for k, c in collections.Counter(keys).items() if c > 1]
                if dup:
                    errors.append(f"{rel}: front-matter 顶层键重复 {dup}")

                missing = [k for k in REQUIRED_FIELDS if k not in keys]
                if missing:
                    errors.append(f"{rel}: front-matter 缺字段 {missing}")

                check_front_matter_shape(fm, rel, errors)

                t, st, i = fm_value(fm, "type"), fm_value(fm, "status"), fm_value(fm, "id")

                if t not in TYPES:
                    errors.append(f"{rel}: type 非法 -> {t!r}")
                else:
                    if st not in ALLOWED_STATUS[t]:
                        errors.append(f"{rel}: type={t} 不允许 status={st!r}")
                    for sec in REQUIRED_SECTIONS[t]:
                        if f"## {sec}" not in text:
                            errors.append(f"{rel}: 缺必备小节「{sec}」")
                    # FORMAT.md §5：所有类型都必须有 ## 论证（草案下可留空）
                    if "## 论证" not in text:
                        errors.append(f"{rel}: 缺必备小节「论证」（所有类型都必须有）")

                if i in ids:
                    errors.append(f"{rel}: id 与 {ids[i]} 重复 -> {i}")
                elif i:
                    ids[i] = rel

                # 只有「命题」可以用「已确证」
                if ONLY_CLAIMS_CAN_BE_CONFIRMED and t != "命题" and st == "已确证":
                    errors.append(
                        f"{rel}: 只有「命题」可以用「已确证」（{t} 不存在唯一正确）")

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
        links += [(u, u) for u in re.findall(r"^\s*url:\s*(\S+)", text, re.M)]
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
                    errors.append(f"{rel}: 链接目标不存在 -> [{label}]({target})")
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
                            f"{rel}: 链接目标不存在 -> [{label}]({target})")
                        continue
                    target_rel = os.path.relpath(cand, ROOT).replace(os.sep, "/")
            # R-LINK-03 要等全部对象收齐才能判（目标是不是「有译本的条目」）
            link_records.append((rel, label, target, target_rel, en_pointer))
            if anchor and target_rel.endswith(".md") \
                    and not anchor_ok(target_rel, anchor):
                errors.append(f"{rel}: 锚点不存在 -> [{label}]({target})")

    # 图校验：单看一个文件查不出来的那部分
    check_bilingual_pairs(objects, events, en_docs, errors, warnings)
    check_link_language(link_records, en_docs, objects, events, errors)
    check_graph(objects, errors, warnings)
    check_arguments(objects, errors)
    check_argument_liveness(objects, warnings)
    check_evidence_ids(objects, events, errors)
    check_readme_coverage(objects, errors)
    check_paths(objects, errors, warnings)
    check_path_steps(objects, errors)
    stats = check_path_outcomes(objects, errors, warnings)
    argstats = argument_graph(objects)
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
    check_license(objects, errors)
    check_id_prefix(objects, errors)
    check_evidence_table(errors)
    check_evidence_verified_support(objects, errors)
    # 事件（与知识对象分开的另一套规则）
    check_event_readme(events, errors)
    sync_generated(objects, events, False, errors)

    return md_files, ids, errors, warnings, stats, argstats, objects, events


def main():
    write = "--write-index" in sys.argv
    md_files, ids, errors, warnings, stats, argstats, objects, events = check_all()

    print(f"扫描 {len(md_files)} 个文档，识别知识对象 {len(objects)} 条，事件 {len(events)} 条")
    print()

    if write:
        p = write_index(objects, events)
        sync_generated(objects, events, True, [])
        print(f"已生成 {p.relative_to(ROOT).as_posix()}"
              f"（{len(objects)} 条对象 + {len(events)} 条事件）+ 文档生成块 —— 请与内容一起提交")
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
    print("  ── 以下五项是单看一个文件查不出来的 ──")
    print("  · `先修` 边只连「知识点」，且无环")
    print("  · `教法` 都有 `knowledge_point`，且指向「知识点」")
    print("  · `支持` / `攻击` 边都落在具体论证上（锚点存在）")
    print("  · 每条路径的「先修缺口」已机械校验（无缺口）")
    for rel, (cov, total) in sorted(stats.items()):
        print(f"  · 目标覆盖度：{Path(rel).stem} —— {cov}/{total} "
              f"({cov/total:.0%})，无未覆盖成果")

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
    return 0


if __name__ == "__main__":
    sys.exit(main())
