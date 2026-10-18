#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成一份**符合 FORMAT.md 的条目骨架**——把录入成本压到「填空」。

为什么要有它
------------
本库的头号未决问题是「录入成本能否压到 5 分钟以内」。在此之前，绝大多数条目是
30–60 分钟的**完整对象**：要记 11 个 front-matter 字段、6 个必备小节、状态枚举、
水平档、论证 ID 格式…… 这些**都不是知识**，但每一条写错都会让校验失败。

所以：**结构交给脚本，内容留给人。**

用法
----
    python tools/new_entry.py --type 命题 --subject 物理 \\
        --slug deceleration-not-a-term --title "「减速」不是物理术语"

    python tools/new_entry.py --type 教法 --subject 物理 --slug force-bl-push-table \\
        --title "力-BL-两个学生推桌子" --level BL \\
        --kp 知识点/力-高中.md

    python tools/new_entry.py --type 事件 --slug irkutsk-plague-2026 \\
        --title "伊尔库茨克反瘟疫研究所事件"

它只做三件事：选对目录 · 抄对模板 · 填掉机器能填的字段。
**证据编号、`适用` / `条件`、论证内容仍然要你自己写**——那些是内容，不是格式。

生成后跑一次 `python tools/kbcheck.py`，它会告诉你还差哪几步（这是故意的）。
"""
import argparse
import datetime
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"

# 类型 → (模板文件, 学科内子目录)；`事件` 单开顶层 events/，不进 knowledge/
TYPE_ALIASES = {
    "知识点": ("知识点.md", "知识点"),
    "命题": ("命题.md", "命题"),
    "教法": ("教法.md", "教法"),
    "误解": ("误解.md", "误解"),
    "路径": ("路径.md", "路径"),
    "资源": ("资源.md", "资源"),
    "事件": ("事件.md", None),
}
TYPE_EN = {
    "concept": "知识点", "concepts": "知识点",
    "claim": "命题", "claims": "命题",
    "method": "教法", "methods": "教法",
    "misconception": "误解", "misconceptions": "误解",
    "path": "路径", "paths": "路径",
    "resource": "资源", "resources": "资源",
    "event": "事件", "events": "事件",
}

# 与 tools/kbcheck.py 的 SUBJECT_SLUGS 保持一致（id 前缀必须与学科匹配，R-SCHEMA-11）
SUBJECT_SLUGS = {"物理": "physics", "生活": "life", "医学": "med", "地理": "geog",
                 "科学": "science", "交通": "transport", "计算机": "computing",
                 "经济": "econ", "法律": "law"}

# 中文标题里不能进文件名的半角字符 → 全角（Windows 禁止半角 \ / : * ? " < > |）
_UNSAFE = {"/": "／", "\\": "＼", ":": "：", "*": "＊", "?": "？",
           '"': "＂", "<": "＜", ">": "＞", "|": "｜"}

DEFAULT_AUTHOR = "@hpleapfrog"


def fail(msg):
    print(f"x {msg}", file=sys.stderr)
    return 2


def read_template(tpl_name):
    """取出模板里 ```markdown 围栏中的骨架。

    模板本身是**给人读的说明页**，骨架放在围栏里——这样模板自己不会被当成条目，
    也不会因为占位符链接而让校验器报「链接目标不存在」。
    """
    p = TEMPLATES / tpl_name
    if not p.exists():
        raise SystemExit(f"x 模板不存在 -> {p}")
    text = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    m = re.search(r"^```markdown\n(.*?)\n```$", text, re.S | re.M)
    if not m:
        raise SystemExit(f"x {p} 里找不到 ```markdown 围栏（模板结构被改坏了）")
    return m.group(1)


def safe_name(title):
    out = "".join(_UNSAFE.get(ch, ch) for ch in title)
    return re.sub(r"\s+", " ", out).strip()


def main():
    ap = argparse.ArgumentParser(
        description="生成符合 FORMAT.md 的条目骨架（本库头号未决问题的补丁）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="类型可用中文或英文别名：\n"
               "  知识点 concept · 命题 claim · 教法 method · 误解 misconception\n"
               "  路径 path · 资源 resource · 事件 event")
    ap.add_argument("--type", "-t", required=True, help="条目类型（中文或英文别名）")
    ap.add_argument("--subject", "-s", help="学科：物理/生活/医学/地理/科学/交通/计算机/经济/法律")
    ap.add_argument("--slug", required=True, help="id 后缀，ASCII，如 ohm-law")
    ap.add_argument("--title", required=True, help="人类可读标题（也就是文件名）")
    ap.add_argument("--author", default=DEFAULT_AUTHOR, help=f"署名（默认 {DEFAULT_AUTHOR}）")
    ap.add_argument("--stage", default="不限", help="学段：小学/初中/高中/大学/不限（默认 不限）")
    ap.add_argument("--level", help="教法专用：BL / OL / AL / 不分档")
    ap.add_argument("--kp", help="教法专用：指回知识点的相对路径，如 知识点/力-高中.md")
    ap.add_argument("--evidence", default="ev-000",
                    help="证据编号（默认 ev-000 是占位符；必须先在 evidence/README.md 登记真来源）")
    ap.add_argument("--force", action="store_true", help="允许覆盖已存在的文件")
    args = ap.parse_args()

    tname = TYPE_ALIASES.get(args.type) or TYPE_ALIASES.get(TYPE_EN.get(args.type.lower(), ""))
    if not tname:
        return fail(f"未知类型 {args.type!r}；可用：" + " / ".join(TYPE_ALIASES))
    tpl_name, subdir = tname
    kind = tpl_name[:-3]

    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", args.slug):
        return fail("--slug 只能用小写字母、数字与连字符（如 ohm-law）")

    is_event = subdir is None
    if is_event:
        prefix = "kb:event:"
        target_dir = ROOT / "events"
        oid = prefix + args.slug
        subject, kp_rel = "", ""
    else:
        if not args.subject:
            return fail("--subject 必填（事件除外）")
        if args.subject not in SUBJECT_SLUGS:
            return fail(f"未知学科 {args.subject!r}；可用：" + " / ".join(SUBJECT_SLUGS))
        prefix = f"kb:{SUBJECT_SLUGS[args.subject]}:"
        target_dir = ROOT / "knowledge" / args.subject / subdir
        oid = prefix + args.slug
        subject = args.subject
        if kind == "教法" and not args.kp:
            return fail("教法必须用 --kp 指回一个知识点（如 --kp 知识点/力-高中.md）")
        # `--kp` 可以写成「相对学科目录」（知识点/力-高中.md）或「相对教法目录」
        # （../知识点/力-高中.md）；统一换算成**相对目标文件**的路径——
        # 写错方向是这里最常见的失败，而它只会表现为一条「链接目标不存在」。
        kp_rel = ""
        if args.kp:
            raw = args.kp.strip()
            cand = (target_dir / raw) if raw.startswith(".") \
                else (ROOT / "knowledge" / args.subject / raw)
            if not cand.exists():
                print(f"! 警告：{raw} 现在还不存在 —— 生成后 `knowledge_point` 会是断链，"
                      f"校验器会拦下它（R-SCHEMA-12）", file=sys.stderr)
            kp_rel = os.path.relpath(cand, target_dir).replace(os.sep, "/")

    if kind == "教法" and not args.level:
        return fail("教法必须用 --level 给水平档（BL / OL / AL，或跨档的「不分档」）")

    body = read_template(tpl_name)
    today = datetime.date.today().isoformat()
    body = (body
            .replace("{{ID}}", oid)
            .replace("{{TITLE}}", args.title)
            .replace("{{AUTHOR}}", args.author)
            .replace("{{DATE}}", today)
            .replace("{{EVIDENCE}}", args.evidence)
            .replace("{{SUBJECT}}", subject)
            .replace("{{STAGE}}", args.stage)
            .replace("{{LEVEL}}", args.level or "")
            .replace("{{APPLY}}", "待填：对谁成立")
            .replace("{{CONDITION}}", "待填：在什么条件下成立（含版本 / 生效时间）")
            .replace("{{KPATH}}", kp_rel))

    target_dir.mkdir(parents=True, exist_ok=True)
    out = target_dir / f"{safe_name(args.title)}.md"
    if out.exists() and not args.force:
        return fail(f"文件已存在 -> {out.relative_to(ROOT).as_posix()}（要覆盖加 --force）")
    out.write_text(body, encoding="utf-8")
    rel = out.relative_to(ROOT).as_posix()

    readme = (ROOT / "events" / "README.md") if is_event \
        else (ROOT / "knowledge" / subject / "README.md")

    print(f"已生成 {rel}")
    print()
    print("还差这几步（跑一遍 kbcheck 就会逐条报出来）")
    print(f"  1. 填 front-matter 的 `适用` / `条件` —— 缺了它，结论会被误用")
    print(f"  2. 把 `{args.evidence}` 换成真实编号，并在 "
          f"{(ROOT / 'evidence' / 'README.md').relative_to(ROOT).as_posix()} 登记（来源三问）")
    print(f"  3. 在 {readme.relative_to(ROOT).as_posix()} 里登记这一条（R-README-01）")
    if kind == "教法":
        print(f"  4. 核对 `knowledge_point` 是否指对了知识点（当前 {kp_rel}）")
    if kind == "路径":
        print(f"  4. 编排表每一行的 `条目` 列都要有链接；`覆盖` 列要覆盖全部 outcomes")
    print()
    print("  最后：python tools/kbcheck.py --write-index")
    return 0


if __name__ == "__main__":
    sys.exit(main())
