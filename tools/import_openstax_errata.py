#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 OpenStax 公开勘误记录批量转成 `命题` 条目。

为什么要有它
------------
仓库的最小目标是「一本教材的一章——200 条勘误」。OpenStax 的勘误系统公开、
可逐条永久链接，且记录里带位置、说明与出版方处理意见——正好是 `命题` 需要的
「谁说的 · 在哪 · 说了什么」。手工抄 200 条既慢又容易抄错，所以结构交给脚本。

**它不判断勘误对不对。** 每条只主张「出版方已记录并接受该勘误」；
不主张「当前网页版仍是错的」。二者不是一回事，条目的 `条件` 写明了这一点。

用法
----
    python tools/import_openstax_errata.py \
        --snapshot evidence/openstax-up1-errata-200.json

    python tools/import_openstax_errata.py --profile calc3 \
        --snapshot evidence/calc3-ch6-errata-308.json

`--profile` 选择书目、学科与证据编号：`up1` = 物理（默认），`calc3` = 数学。
默认是 **dry-run**：只打印将要写什么。确认后加 `--write`。

    python tools/import_openstax_errata.py \
        --snapshot evidence/openstax-up1-errata-200.json --limit 3 --print 1

复核已生成条目是否与快照逐条对应（不联网、不改文件）：

    python tools/import_openstax_errata.py \
        --snapshot evidence/openstax-up1-errata-200.json --verify

生成物（目录、前缀由 profile 决定）：
- knowledge/<学科>/claims/勘误-<前缀>-<id>.md
- knowledge/<学科>/claims/<英文编号>-errata-<id>.en.md
- 对应 README.md / README.en.md 的 `## 教材勘误` 表各一行（幂等）
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATE = "2026-10-20"
AUTHOR = "@hpleapfrog"
PERMALINK = "https://openstax.org/errata/{id}"

PROFILES = {
    "up1": {
        "claims": ROOT / "knowledge" / "physics" / "claims",
        "readme_zh": ROOT / "knowledge" / "physics" / "README.md",
        "readme_en": ROOT / "knowledge" / "physics" / "README.en.md",
        "prefix": "UP1",
        "en_stem": "up1",
        "slug": "physics",
        "subject_zh": "物理",
        "book_zh": "University Physics Volume 1",
        "book_en": "University Physics Volume 1",
        "evidence": "ev-150",
        "source_zh": "OpenStax《University Physics Volume 1》勘误 #{eid}",
        "source_en": "OpenStax *University Physics Volume 1* erratum #{eid}",
    },
    "calc3": {
        "claims": ROOT / "knowledge" / "mathematics" / "claims",
        "readme_zh": ROOT / "knowledge" / "mathematics" / "README.md",
        "readme_en": ROOT / "knowledge" / "mathematics" / "README.en.md",
        "prefix": "CV3",
        "en_stem": "calc3",
        "slug": "math",
        "subject_zh": "数学",
        "book_zh": "Calculus Volume 3",
        "book_en": "Calculus Volume 3",
        "evidence": "ev-152",
        "source_zh": "OpenStax《Calculus Volume 3》第 6 章勘误 #{eid}",
        "source_en": "OpenStax *Calculus Volume 3* Ch. 6 erratum #{eid}",
    },
}
P = PROFILES["up1"]

ERRATA_KIND = {
    "Typo": "排版/笔误",
    "Incorrect answer, calculation, or solution": "答案/计算错误",
    "General/pedagogical suggestion or question": "被接受的教学建议",
    "Other factual inaccuracy in content": "内容事实性错误",
    "Broken link": "链接失效",
    "Other": "其他（出版方已接受）",
    "": "未分类（出版方已接受）",
}

# 短引用上限：勘误说明是用户提交的文本，只引到能定位问题为止。
QUOTE_LIMIT = 700


def chapter_of(entry):
    m = re.search(r"Chapter\s+(\d+)", entry.get("location") or "")
    return m.group(1) if m else ""


def clean(text, limit=None):
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text).strip()
    if limit and len(text) > limit:
        cut = text[:limit]
        # 尽量在句末或词边界收尾，避免把公式/单词截成半截。
        for mark in (". ", "。", "; ", "；", "\n"):
            pos = cut.rfind(mark)
            if pos > limit * 0.6:
                cut = cut[: pos + len(mark)]
                break
        text = cut.rstrip() + "……"
    return text


def one_line(text, limit=90):
    text = clean(text).replace("|", "/").replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text[:limit].rstrip() + ("…" if len(text) > limit else "")


def quote(text):
    return "\n".join("> " + line if line.strip() else ">" for line in clean(text).split("\n"))


def yaml_str(text):
    return json.dumps(text, ensure_ascii=False)


def title_zh(entry):
    ch = chapter_of(entry)
    loc = clean(entry.get("location") or "")
    desc = re.sub(r"^Chapter\s+[\d.]+", "", loc).strip(" :,;·—-")
    desc = one_line(desc or "教材勘误", 70)
    return f"勘误 #{entry['id']}：第 {ch} 章 · {desc}"


def title_en(entry):
    ch = chapter_of(entry)
    loc = clean(entry.get("location") or "")
    desc = re.sub(r"^Chapter\s+[\d.]+", "", loc).strip(" :,;·—-")
    desc = one_line(desc or "textbook erratum", 80)
    return f"Erratum #{entry['id']} in {P['book_en']} (Chapter {ch}): {desc}"


def body_zh(entry):
    eid = entry["id"]
    link = PERMALINK.format(id=eid)
    loc = one_line(entry.get("location") or "", 180)
    submitted = (entry.get("created") or "")[:10]
    detail = quote(clean(entry.get("detail") or "", QUOTE_LIMIT))
    notes = quote(clean(entry.get("resolution_notes") or "", 400))
    kind = ERRATA_KIND.get(entry.get("error_type") or "", "出版方已接受")
    return f"""## 陈述

OpenStax《{P['book_zh']}》的公开勘误记录 [#{eid}]({link}) 针对 **{loc}** 记录如下
（提交 {submitted}；状态 {entry.get('status')}；处理 {entry.get('resolution')}）：

{detail}

出版方处理意见：

{notes}

> [!NOTE]
> 本条只主张「出版方已记录并接受该勘误」。**它不等于本库复核过当前网页版正文**；
> 引用时请以永久链接中的记录为准。

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| {P['evidence']} | 出版社勘误表 | 高 | OpenStax《{P['book_zh']}》勘误 #{eid} · [永久链接]({link}) · 第 {chapter_of(entry)} 章 | 外部来源 · 仅引用定位与短引用 |

## 论证

### A1 · 出版方勘误记录（尚无攻击）

- **主张**：OpenStax 已将 #{eid} 记录为已接受的勘误，并给出应更正的内容
- **前提**：公开勘误页 #{eid} 显示位置、说明、状态 {entry.get('status')} 与处理 {entry.get('resolution')}（{P['evidence']}）
- **推理**：出版方对自身教材的勘误记录，是该处存在错误并应按记录更正的直接依据；本库不在此之外补充推断
- **证据**：{P['evidence']}
- **被攻击**：尚无攻击
- **署名**：{AUTHOR} · {DATE}

## 性质

**{kind}**：本条记录的是出版方已接受的更正；它不表示当前网页版仍显示错误文本。

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| {DATE} | 批量录入（OpenStax 公开勘误系统快照） | {P['evidence']} · 勘误 #{eid} | {AUTHOR} |
"""


def body_en(entry, zh_name):
    eid = entry["id"]
    link = PERMALINK.format(id=eid)
    loc = one_line(entry.get("location") or "", 180)
    submitted = (entry.get("created") or "")[:10]
    detail = quote(clean(entry.get("detail") or "", QUOTE_LIMIT))
    notes = quote(clean(entry.get("resolution_notes") or "", 400))
    kind = ERRATA_KIND.get(entry.get("error_type") or "", "accepted by the publisher")
    kind_en = {
        "排版/笔误": "Typo",
        "答案/计算错误": "Incorrect answer, calculation, or solution",
        "被接受的教学建议": "Accepted pedagogical suggestion",
        "内容事实性错误": "Factual inaccuracy",
        "链接失效": "Broken link",
        "其他（出版方已接受）": "Other (accepted by the publisher)",
        "未分类（出版方已接受）": "Unclassified (accepted by the publisher)",
    }.get(kind, "Accepted by the publisher")
    return f"""> **English version of [`{zh_name}`]({zh_name}).**

## Statement

The public errata record [#{eid}]({link}) for OpenStax *{P['book_en']}* concerns
**{loc}** and states the following (submitted {submitted}; status {entry.get('status')};
resolution {entry.get('resolution')}):

{detail}

Publisher's resolution:

{notes}

> [!NOTE]
> This entry claims only that "the publisher recorded and accepted this erratum".
> **It does not claim that this repository checked the current web text**; cite the
> permanent link when verifying.

## Basis

| Number | Type | Grade | Locator | License |
|---|---|---|---|---|
| {P['evidence']} | publisher errata list | high | OpenStax *{P['book_en']}* erratum #{eid} · [permanent link]({link}) · Chapter {chapter_of(entry)} | external source · locators and short quotes only |

## Argument

### A1 · Publisher's errata record (no attack yet)

- **Claim**: OpenStax recorded #{eid} as an accepted erratum and gave the correction to be made
- **Premise**: the public errata page #{eid} shows the location, description, status {entry.get('status')} and resolution {entry.get('resolution')} ({P['evidence']})
- **Reasoning**: a publisher's errata record for its own textbook is direct grounds that the passage is wrong and should be corrected as recorded; this repository adds no inference beyond that
- **Evidence**: {P['evidence']}
- **Attacked**: no attack yet
- **Signed**: {AUTHOR} · {DATE}

## Nature

**{kind_en}**: the entry records a correction accepted by the publisher; it does not assert that the current web text still shows the error.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| {DATE} | Batch import (OpenStax public errata snapshot) | {P['evidence']} · erratum #{eid} | {AUTHOR} |
"""


def front_matter(entry, title, lang):
    eid = entry["id"]
    submitted = (entry.get("created") or "")[:10]
    if lang == "zh":
        apply = f"使用 OpenStax《{P['book_zh']}》的教师与学生"
        cond = (
            f"公开勘误记录 #{eid}（{submitted} 提交，{entry.get('status')} / {entry.get('resolution')}）；"
            "引用的是记录本身，不是当前网页版正文"
        )
    else:
        apply = f"teachers and students using OpenStax *{P['book_en']}*"
        cond = (
            f"public errata record #{eid} (submitted {submitted}, {entry.get('status')} / {entry.get('resolution')}); "
            "the record itself is cited, not the current web text"
        )
    return f"""---
id: kb:{P['slug']}:{P['en_stem']}-errata-{eid}
type: 命题
title: {yaml_str(title)}
status: 待审
author: "{AUTHOR}"
created: {DATE}
updated: {DATE}
scope:
  学科: {P['subject_zh']}
  学段: 大学
  适用: {yaml_str(apply)}
  条件: {yaml_str(cond)}
edges:
  先修: []
  支持: []
  攻击: []
evidence: [{P['evidence']}]
license: CC-BY-SA-4.0
---
"""


def insert_rows(path, rows, section):
    text = path.read_text(encoding="utf-8")
    # 按行去重：允许先试跑 1 条、再补其余 199 条，而不重复登记。
    new_rows = [r for r in rows if (re.search(r"\(claims/([^)]+)\)", r).group(1) not in text)]
    if not new_rows:
        return 0
    lines = text.split("\n")
    start = next((i for i, line in enumerate(lines) if line.startswith(section)), None)
    if start is None:
        start = next((i for i, line in enumerate(lines) if line.startswith("## 命题")), None)
    if start is None:
        raise SystemExit(f"x {path}: 找不到 `{section}` 或 `## 命题`")
    header = next(
        (i for i in range(start, len(lines)) if lines[i].startswith("|")),
        None,
    )
    if header is None:
        raise SystemExit(f"x {path}: `## 命题` 下找不到表格")
    last = header + 1
    for j in range(header + 2, len(lines)):
        if not lines[j].startswith("|"):
            break
        last = j
    lines[last + 1:last + 1] = new_rows
    path.write_text("\n".join(lines), encoding="utf-8")
    return len(new_rows)


def verify(entries, full_count):
    """逐条核对生成物：引用文本与快照一致，中英配对存在，README 已登记。"""
    norm = lambda s: re.sub(r"\s+", " ", (s or "").replace("\u3000", " ")).strip()

    def unquote(text):
        parts = []
        for line in text.split("\n"):
            if line.startswith("> "):
                parts.append(line[2:])
            elif line == ">":
                parts.append("")
        return norm("\n".join(parts))

    readme_zh = P["readme_zh"].read_text(encoding="utf-8")
    readme_en = P["readme_en"].read_text(encoding="utf-8")
    problems = []
    zh_ok = en_ok = trace_ok = reg_ok = 0

    for entry in entries:
        eid = entry["id"]
        zh_name = f"勘误-{P['prefix']}-{eid}.md"
        en_name = f"{P['en_stem']}-errata-{eid}.en.md"
        zh_path, en_path = P["claims"] / zh_name, P["claims"] / en_name

        if not zh_path.exists() or not en_path.exists():
            missing = [p.name for p in (zh_path, en_path) if not p.exists()]
            problems.append(f"#{eid}: 缺少 {', '.join(missing)}")
        else:
            zh_ok += 1
            en_ok += 1
            zh_text = zh_path.read_text(encoding="utf-8")
            en_text = en_path.read_text(encoding="utf-8")
            if f"id: kb:{P['slug']}:{P['en_stem']}-errata-{eid}" not in zh_text or f"evidence: [{P['evidence']}]" not in zh_text:
                problems.append(f"#{eid}: 中文条目缺 id 或证据编号")
            quoted_zh = unquote(zh_text)
            quoted_en = unquote(en_text)
            matched = True
            for field, limit, label in (
                ("detail", QUOTE_LIMIT, "说明"),
                ("resolution_notes", 400, "处理意见"),
            ):
                expected = norm(clean(entry.get(field) or "", limit))
                if expected not in quoted_zh:
                    problems.append(f"#{eid}: 中文条目的{label}与快照不一致")
                    matched = False
                elif expected not in quoted_en:
                    problems.append(f"#{eid}: 英文条目的{label}与快照不一致")
                    matched = False
            if matched:
                trace_ok += 1

        if zh_name not in readme_zh:
            problems.append(f"#{eid}: 中文 README 未登记 {zh_name}")
        if en_name not in readme_en:
            problems.append(f"#{eid}: 英文 README 未登记 {en_name}")
        if zh_name in readme_zh and en_name in readme_en:
            reg_ok += 1

    if full_count is not None and full_count != len(entries):
        problems.append(f"快照 count={full_count} 与本次校验条数 {len(entries)} 不一致")

    print(
        f"校验 {len(entries)} 条：中英条目 {zh_ok}/{len(entries)} · "
        f"引用与快照一致 {trace_ok}/{len(entries)} · README 登记 {reg_ok}/{len(entries)}"
    )
    for line in problems[:20]:
        print("  x " + line)
    if len(problems) > 20:
        print(f"  … 另有 {len(problems) - 20} 条")
    return 1 if problems else 0


def main():
    ap = argparse.ArgumentParser(description="把 OpenStax 勘误快照批量转为命题条目")
    ap.add_argument("--snapshot", required=True, help="脱敏快照 JSON（evidence/*errata*.json）")
    ap.add_argument("--profile", choices=sorted(PROFILES), default="up1", help="书目/学科配置（默认 up1=物理）")
    ap.add_argument("--limit", type=int, default=0, help="只处理前 N 条（试跑用；默认全部）")
    ap.add_argument("--print", dest="show", type=int, default=0, help="打印前 N 条中文正文")
    ap.add_argument("--write", action="store_true", help="真正写文件（默认 dry-run）")
    ap.add_argument("--verify", action="store_true", help="只核对已生成条目与快照，不写文件")
    args = ap.parse_args()

    global P
    P = PROFILES[args.profile]

    snap_path = (ROOT / args.snapshot) if not Path(args.snapshot).is_absolute() else Path(args.snapshot)
    snap = json.loads(snap_path.read_text(encoding="utf-8"))
    entries = snap["entries"]
    if args.limit:
        entries = entries[: args.limit]
    ids = [e["id"] for e in entries]
    if len(ids) != len(set(ids)):
        raise SystemExit("x 快照里有重复 id")

    if args.verify:
        return verify(entries, None if args.limit else snap.get("count"))

    rows_zh, rows_en, samples = [], [], []
    for entry in entries:
        eid = entry["id"]
        zh_name = f"勘误-{P['prefix']}-{eid}.md"
        en_name = f"{P['en_stem']}-errata-{eid}.en.md"
        zh = front_matter(entry, title_zh(entry), "zh") + "\n" + body_zh(entry)
        en = front_matter(entry, title_en(entry), "en") + "\n" + body_en(entry, zh_name)
        if args.show and len(samples) < args.show:
            samples.append(zh)
        if args.write:
            (P["claims"] / zh_name).write_text(zh, encoding="utf-8")
            (P["claims"] / en_name).write_text(en, encoding="utf-8")
        rows_zh.append(
            f"| [{title_zh(entry)}](claims/{zh_name}) | 待审 | "
            f"{P['source_zh'].format(eid=eid)}（`{P['evidence']}`） |"
        )
        rows_en.append(
            f"| [{title_en(entry)}](claims/{en_name}) | 待审 | "
            f"{P['source_en'].format(eid=eid)} (`{P['evidence']}`) |"
        )

    for block in samples:
        print(block)
        print("\n" + "=" * 70 + "\n")

    book = snap.get("book") or {}
    print(f"快照 {snap_path.name}：{snap.get('count')} 条，本次处理 {len(entries)} 条")
    print(
        f"书：{book.get('title', P['book_en'])}（ISBN {book.get('isbn_13', '—')}），"
        f"章：{snap.get('chapters')}；profile={args.profile}"
    )
    if not args.write:
        print("dry-run：未写文件。加 --write 生成并可重复运行（README 行按文件名幂等）。")
        return 0

    n_zh = insert_rows(P["readme_zh"], rows_zh, "## 教材勘误：OpenStax")
    n_en = insert_rows(P["readme_en"], rows_en, "## Textbook errata: OpenStax")
    print(f"写入 {len(entries)} 对条目；README 新增行 {n_zh} / {n_en}（0 表示已登记）")
    print("下一步：python tools/kbcheck.py --write-index && python tools/kbcheck.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
