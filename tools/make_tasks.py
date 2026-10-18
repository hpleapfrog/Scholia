#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""路标：从库的缺口自动生成**可直接开工的任务**。

为什么要有
----------
一个新人对这个仓库最大的障碍不是"不会写"，是**不知道能做什么**。
读 527 行 FORMAT 才知道能干什么，等于把路修在没人看得见的地方。

这个脚本读三份机器文件（不联网、零依赖），把**已经存在的缺口**变成任务清单：

| 任务组 | 从哪来 | 难度 |
|---|---|---|
| `review` 复核 | 状态 `待审` 且有论证、证据已读过全文的条目 | **3 分钟**，不需要写内容 |
| `translate` 补译本 | `path_en` 为 null 的条目 | 中，需要翻译 |
| `todo` 待补 | 正文里写着 `**待补**：` 的条目 | 不定 |
| `coverage` 覆盖度 | `knowledge/physics/coverage/README.md` 里 🔴 的章 | 大，需要采集与撰写 |

用法
----
    python tools/make_tasks.py                  # 打印清单（默认只统计，不改任何东西）
    python tools/make_tasks.py --limit 3        # 每组最多列 3 条
    python tools/make_tasks.py --gh --limit 3   # 用 gh 建 issue（需要 gh 已登录）

**默认什么都不做**——只读、只打印。要建 issue 必须显式 `--gh`。
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
READ_DEPTH = {"全文", "摘要"}


def load(name):
    p = ROOT / name
    if not p.exists():
        raise SystemExit(f"x 缺少 {name} —— 先跑 python tools/kbcheck.py --write-index")
    return json.loads(p.read_text(encoding="utf-8"))


def tasks():
    index = load("index.json")
    cites = load("citations.json").get("by_id", {})
    evid = load("evidence.json").get("entries", {})
    out = {}

    # 复核：状态待审 + 有论证 + 每条证据都读过全文/摘要
    review = []
    for o in index["objects"]:
        if o["status"] != "待审":
            continue
        c = cites.get(o["id"], {})
        # `论证` 在 index 里（图关系），`证据/来源` 在 citations 里（引用材料）—— 两份各取所需
        if not o.get("论证"):
            continue
        depths = [evid.get(e, {}).get("核验深度") for e in c.get("证据", [])]
        if depths and all(d in READ_DEPTH for d in depths):
            review.append(o)
    out["review"] = review

    out["translate"] = [o for o in index["objects"] if not o.get("path_en")]

    todo = []
    for o in index["objects"]:
        p = ROOT / o["path"]
        if not p.exists():
            continue
        body = p.read_text(encoding="utf-8")
        for line in body.split("\n"):
            if "**待补**" in line or "待补：" in line:
                todo.append((o, line.strip("->- ").strip()[:80]))
                break
    out["todo"] = todo

    cov = []
    cp = ROOT / "knowledge" / "physics" / "coverage" / "README.md"
    if cp.exists():
        for line in cp.read_text(encoding="utf-8").split("\n"):
            if "🔴" in line and line.startswith("|"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) >= 2:
                    cov.append(cells[1])
    out["coverage"] = cov
    return out


HEAD = {
    "review": ("三分钟复核", "开一个「复核一条」Issue，回答三个是/否。**不需要写内容。**"),
    "translate": ("补英文译本", "按 `id` 派生文件名，与中文原件同目录。"),
    "todo": ("兑现「待补」", "条目自己写下的缺口。"),
    "coverage": ("补覆盖度缺口", "物理按人教版对照仍为 🔴 的章。"),
}


def render(t, limit):
    lines = []
    for key in ("review", "translate", "todo", "coverage"):
        items = t[key]
        title, why = HEAD[key]
        lines.append(f"\n## {title}（{len(items)} 项）\n\n{why}\n")
        if not items:
            lines.append("（无）\n")
            continue
        shown = items[:limit] if limit else items
        for it in shown:
            if key in ("review", "translate"):
                lines.append(f"- `{it['id']}` · {it['title']} — `{it['path']}`")
            elif key == "todo":
                lines.append(f"- `{it[0]['id']}` · {it[1]}")
            else:
                lines.append(f"- {it}")
        if limit and len(items) > limit:
            lines.append(f"- …还有 {len(items) - limit} 项")
    return "\n".join(lines)


def create_issues(t, limit):
    made = 0
    for key in ("review", "translate"):
        for it in t[key][:limit]:
            title = f"[{'复核' if key == 'review' else '译本'}] {it['title']}"
            body = (f"条目：`{it['id']}`\n\n路径：`{it['path']}`\n\n"
                    + ("按「复核一条」模板回答三个问题即可。"
                       if key == "review" else "英文译本文件名由 `id` 派生，与中文原件同目录。"))
            r = subprocess.run(["gh", "issue", "create", "--title", title, "--body", body],
                               cwd=str(ROOT), capture_output=True, text=True)
            if r.returncode == 0:
                made += 1
                print("  +", (r.stdout or "").strip())
            else:
                print("  x 建 issue 失败：", (r.stderr or "").strip()[:120])
    return made


def main():
    limit = 20
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    t = tasks()
    print("# 可开工的任务（由 tools/make_tasks.py 从库的现状生成）")
    print(render(t, limit))
    if "--gh" in sys.argv:
        print("\n创建 issue：")
        n = create_issues(t, limit)
        print(f"\n共创建 {n} 个")
    else:
        print("\n（只读模式。加 `--gh` 才会建 issue。）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
