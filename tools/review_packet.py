#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把「复核一条」要用的材料摆到一页上——**不判断，只排版**。

为什么要有
----------
全库最大的缺口是 **570 条「三分钟复核」**（见 [`docs/GAPS.md`](../docs/GAPS.md)）。
挡住人的往往不是判断，而是**找材料**：条目在哪、引了哪份证据、定位是什么、
原文短引用在哪一段、Issue 模板要填什么。

这个脚本把这几样从三份生成物和正文里取出来，拼成一页 Markdown。
它**不回答**那三个问题，也不给「通过 / 不通过」的建议——那必须由**非作者的人**
看完来源后自己写（`M-07`：AI 不能当 `已确证` 的复核者）。

用法
----
    python tools/review_packet.py --id kb:physics:kp-acceleration
    python tools/review_packet.py --id kb:physics:kp-acceleration --id kb:physics:kp-electric-field
    python tools/review_packet.py --group review --limit 3 --out review/
    python tools/review_packet.py --group review-blocked --limit 1

默认只打印，不写盘；`--out` 才写文件（目录不存在会创建）。
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import gaps  # noqa: E402  与 GAPS 页面 / make_tasks / MCP 共用同一个缺口计算

QUESTIONS = [
    ("它引用的来源，你打得开吗？", "404 / 链接失效 / 要付费看不到"),
    ("那一页上，真的有这句话吗？", "措辞不同、意思更宽、原文根本没这句"),
    ("它的结论有没有超出那一页？", "原文限定人群 / 版本 / 条件，条目写成普遍成立"),
]


def load(name):
    p = ROOT / name
    if not p.exists():
        raise SystemExit(f"x 缺少 {name} —— 先跑 python tools/kbcheck.py --write-index")
    return json.loads(p.read_text(encoding="utf-8"))


def section(md, name):
    """取 `## <name>` 到下一个 `## ` 之间的正文（没有就返回空串）。"""
    m = re.search(rf"(?ms)^## {re.escape(name)}\s*\n(.*?)(?=^## |\Z)", md)
    return m.group(1).strip() if m else ""


def first_section(md):
    """front-matter 之后的第一个 `## ` 小节——也就是「这条在说什么」。"""
    body = md.split("\n---", 1)[-1]
    m = re.search(r"(?ms)^## (.+?)\s*\n(.*?)(?=^## |\Z)", body)
    if not m:
        return "", ""
    return m.group(1).strip(), m.group(2).strip()


def clip(text, n):
    text = text.strip()
    return text if len(text) <= n else text[:n].rstrip() + "\n\n…（截断；全文见条目）"


def packet(o, cite, evid, md):
    title = o["title"]
    out = [
        f"# 复核包：{title}",
        "",
        f"- **id**：`{o['id']}`",
        f"- **路径**：`{o['path']}`",
        f"- **状态**：`{o['status']}`",
        f"- **学科 / 学段**：{o.get('学科', '—')} / {o.get('学段', '—')}",
        "",
        "> **这个包只把材料摆到一起，不判断。** 三个问题必须由**非作者的人**看完来源后回答；",
        "> AI 可以帮忙找材料，但不能当 `已确证` 的复核者（`M-07`）。",
        "",
        "## 1. 条目怎么说",
        "",
    ]
    head, head_body = first_section(md)
    if head and head != "依据":
        out += [f"### {head}", "", clip(head_body, 1600), ""]
    else:
        out += ["（没有找到正文首节；请直接打开条目）", ""]

    out += ["## 2. 条目说依据是什么", ""]
    basis = section(md, "依据")
    if basis:
        out += [clip(basis, 3200), ""]
    else:
        # 不是所有类型都有 `## 依据`：知识点用 `## 论证`，教法用 `## 证据`。
        # 这里退回它实际有的那一节，而不是把「类型不同」误报成「缺依据」。
        fallback = section(md, "证据") or section(md, "论证")
        if fallback:
            out += ["（这类条目没有单独的 `## 依据` 小节；下面是它实际有的论证 / 证据节。）", "",
                    clip(fallback, 3200), ""]
        else:
            out += ["（没有 `## 依据` / `## 证据` / `## 论证` 小节；请直接打开条目核对。）", ""]

    out += ["## 3. 来源（引用时必须连状态一起给）", ""]
    srcs = cite.get("来源") or []
    if srcs:
        out += [f"- {s}" for s in srcs]
    else:
        out += ["- （citations.json 里没有解析后的来源）"]
    out.append("")

    ev_ids = cite.get("证据") or []
    if ev_ids:
        out += ["| 证据 | 类别 | 等级 | 核验深度 | 定位 | 链接 |", "|---|---|---|---|---|---|"]
        for e in ev_ids:
            r = evid.get(e) or {}
            link = r.get("链接") or "—"
            out.append(
                f"| `{e}` | {r.get('类别', '—')} | {r.get('等级', '—')} | "
                f"{r.get('核验深度', '—')} | {r.get('定位', '—')} | {link} |")
        out.append("")
        unread = [e for e in ev_ids
                  if (evid.get(e) or {}).get("核验深度") not in gaps.READ_DEPTH]
        if unread:
            evs = "、".join(f"`{e}`" for e in unread)
            out += [
                "> [!WARNING]",
                f"> **这条还不能开始复核：** {evs} 只到 `仅定位`/`未核验`。",
                "> 先把来源读到 `摘要`/`全文`，否则三个问题里的第 2、3 个无从回答。",
                "",
            ]

    limits = []
    if cite.get("适用"):
        limits.append(f"- **适用**：{cite['适用']}")
    if cite.get("条件"):
        limits.append(f"- **条件**：{cite['条件']}")
    if cite.get("引用时须写明"):
        limits.append(f"- **引用时须写明**：{cite['引用时须写明']}")
    if cite.get("免责块在正文最前"):
        limits.append("- **免责块在正文最前**：是（医学内容，转述时不能省略）")
    if limits:
        out += ["**转述时必须一起给出的限定：**", ""] + limits + [""]

    out += [
        "## 4. 三个问题（只问原文有没有这么说）",
        "",
        "| # | 问题 | 什么算「否」 |",
        "|---|---|---|",
    ]
    for i, (q, no) in enumerate(QUESTIONS, 1):
        out.append(f"| {i} | {q} | {no} |")
    out += [
        "",
        "> **不要回答「这个结论对不对」。** 那是论证攻防，不是复核。",
        "",
        "## 5. 复核记录（复制到 Issue）",
        "",
        "```text",
        f"条目：{o['id']}",
        "来源可打开：是 / 否",
        "原文有这句话：是 / 否",
        "结论未超出：是 / 否",
        "复核者（非作者）：@",
        "日期：",
        "备注：",
        "```",
        "",
        f"提交入口：[`.github/ISSUE_TEMPLATE/复核一条.yml`]"
        f"(../.github/ISSUE_TEMPLATE/复核一条.yml)",
        "",
    ]
    return "\n".join(out)


def select(args, index, cites, evid):
    objs = {o["id"]: o for o in index.get("objects", [])}
    if args.id:
        chosen = []
        for oid in args.id:
            if oid not in objs:
                raise SystemExit(f"x 没有这个 id：{oid}")
            chosen.append(objs[oid])
        # `--id` 默认全取：一次点名三个 id、却只拿到一个，是工具在替人做决定。
        limit = args.limit if args.limit is not None else len(chosen)
        return chosen[:limit] if limit else chosen

    data = gaps.compute(index, cites, evid, root=ROOT)
    key = args.group or "review"
    if key not in data["分组"]:
        raise SystemExit(f"x 没有这个缺口组：{key}（可选：{', '.join(data['顺序'])}）")
    items = data["分组"][key]["条目"]
    chosen = []
    for it in items:
        o = objs.get(it.get("id"))
        if o:
            chosen.append(o)
    limit = args.limit if args.limit is not None else 1
    return chosen[:limit] if limit else chosen


def main():
    ap = argparse.ArgumentParser(
        description="把「复核一条」的材料拼成一页（只排版，不判断）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="例：\n"
               "  python tools/review_packet.py --id kb:physics:kp-acceleration\n"
               "  python tools/review_packet.py --group review --limit 3 --out review/")
    ap.add_argument("--id", action="append", default=[], help="要复核的 id（可重复）")
    ap.add_argument("--group", help="从缺口组里取：review / review-blocked / methods / …")
    ap.add_argument("--limit", type=int, default=None,
                    help="最多取几条（--group 默认 1；--id 默认全部；0 = 全部）")
    ap.add_argument("--out", help="输出目录；省略则打印到 stdout")
    args = ap.parse_args()
    if args.limit is not None and args.limit < 0:
        ap.error("--limit must be >= 0 (0 means all)")

    index = load("index.json")
    cites = load("citations.json").get("by_id", {})
    evid = load("evidence.json").get("entries", {})

    chosen = select(args, index, cites, evid)
    if not chosen:
        raise SystemExit("x 没有选中任何条目")

    packets = []
    for o in chosen:
        p = ROOT / o["path"]
        if not p.exists():
            raise SystemExit(f"x 正文不存在：{o['path']}")
        packets.append(packet(o, cites.get(o["id"], {}), evid,
                              p.read_text(encoding="utf-8")))

    if args.out:
        outdir = Path(args.out)
        outdir.mkdir(parents=True, exist_ok=True)
        for o, text in zip(chosen, packets):
            slug = o["id"].rsplit(":", 1)[-1]
            dest = outdir / f"review-{slug}.md"
            dest.write_text(text, encoding="utf-8")
            print(dest.as_posix())
    else:
        print("\n\n---\n\n".join(packets))
    return 0


if __name__ == "__main__":
    sys.exit(main())
