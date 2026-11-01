#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""路标：从库的缺口自动生成**可直接开工的任务**。

为什么要有
----------
一个新人对这个仓库最大的障碍不是"不会写"，是**不知道能做什么**。
读 527 行 FORMAT 才知道能干什么，等于把路修在没人看得见的地方。

这个脚本读三份机器文件（不联网、零依赖），把**已经存在的缺口**变成任务清单。
**缺口怎么算不在这里**——在 [`gaps.py`](gaps.py)。这里只负责把同一份数据
排版成人能读的清单；`docs/GAPS.md` 与 MCP 的 `scholia_gaps` 用的是同一个 `compute()`。

| 任务组 | 从哪来 | 难度 |
|---|---|---|
| `review` 复核 | 状态 `待审` 且有论证、证据已读过全文的条目 | **3 分钟**，不需要写内容 |
| `review-blocked` 复核前置 | 状态 `待审`，但证据只到 `仅定位`/`未核验`（或无论证 / 无证据） | 小，先读来源 |
| `translate` 补译本 | `path_en` 为 null 的条目 | 中，需要翻译 |
| `methods` 缺教法 | 没有任何 `教法` 挂在下面的 `知识点` | 大，需要教材原文 |
| `external` 库外前置 | 同一个 `外部先修` 标识出现在 ≥2 个对象里 | 判断 + 可能建节点 |
| `path-thin` 单环节覆盖 | 路径成果只被一个环节覆盖（R-GRAPH-07） | 中，补第二个入口 |
| `path-shallow` 证据薄覆盖 | 覆盖条目的证据最高只到 `仅定位`/`未核验` | 小，补核验深度 |
| `todo` 待补 | 正文里写着 `**待补**：` 的条目 | 不定 |
| `coverage` 覆盖度 | `knowledge/physics/coverage/README.md` 里 🔴 的章 | 大，需要采集与撰写 |

用法
----
    python tools/make_tasks.py                  # 打印清单（默认只统计，不改任何东西）
    python tools/make_tasks.py --limit 3        # 每组最多列 3 条
    python tools/make_tasks.py --json           # 输出 JSON（便于脚本 / agent 消费）
    python tools/make_tasks.py --gh --limit 3   # 用 gh 建 issue（需要 gh 已登录）

**默认什么都不做**——只读、只打印。要建 issue 必须显式 `--gh`。
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import gaps  # noqa: E402  同目录、只读、零依赖


def load(name):
    p = ROOT / name
    if not p.exists():
        raise SystemExit(f"x 缺少 {name} —— 先跑 python tools/kbcheck.py --write-index")
    return json.loads(p.read_text(encoding="utf-8"))


def collect():
    """读三份生成物，交给 `gaps.compute()` 算一次。"""
    return gaps.compute(
        load("index.json"),
        load("citations.json").get("by_id", {}),
        load("evidence.json").get("entries", {}),
        root=ROOT,
    )


def split_fm(path):
    """粗读 front-matter 的 `key: value`（本工具只需要 title 一行）。"""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    fm, out = text[4:end], {}
    for line in fm.split("\n"):
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out, text


def concept_to_paths():
    """知识点 -> 覆盖它的路径标题。

    缺教法的一栏原来是一张平铺的 48 项清单——**知道缺，但不知道该从哪条链补**。
    按路径归拢之后，一眼能看出「静电学这条链一条教法都没有」。
    """
    out = {}
    for p in sorted((ROOT / "knowledge").rglob("paths/*.md")):
        if p.name.endswith(".en.md"):
            continue
        fm, _body = split_fm(p)
        title = fm.get("title", p.stem).strip('"')
        for link in re.findall(r"\]\(\.\./concepts/([^)#]+)\.md\)", p.read_text(encoding="utf-8")):
            out.setdefault(link, []).append(title)
    return out


def render(data, limit):
    path_map = concept_to_paths()
    lines = []
    for key in data["顺序"]:
        g = data["分组"][key]
        lines.append(f"\n## {g['名称']}（{g['数量']} 项）\n\n{g['为什么']}\n\n> {g['怎么做']}\n")
        items = g["条目"]
        if not items:
            lines.append("（无）\n")
            continue

        if key == "methods":
            lines.append("> 同一个知识点可能挂在多条路径下，下面的行数**不能相加**。\n")
            groups = {}
            for o in items:
                for title in path_map.get(Path(o["path"]).stem, ["（未被任何路径覆盖）"]):
                    groups.setdefault(title, []).append(o)
            for title, group in sorted(groups.items(), key=lambda kv: -len(kv[1])):
                names = " · ".join(o["title"] for o in group)
                lines.append(f"- **{title}** —— 缺 {len(group)} 条：{names}")
            continue

        if key == "external":
            shown = items[:limit] if limit else items
            for x in shown:
                names = " / ".join(x.get("名称") or [x["标识"]])
                objs = " · ".join(f"`{i}`" for i in x.get("对象") or [])
                meta = " · ".join(x.get("学科") or []) + " · " + " · ".join(x.get("学段") or [])
                lines.append(f"- `{x['标识']}`（{names}）—— {x['出现次数']} 个对象：{objs}；{meta}")
            if limit and len(items) > limit:
                lines.append(f"- …还有 {len(items) - limit} 项")
            continue

        shown = items[:limit] if limit else items
        for it in shown:
            if key == "review":
                dep = it.get("下游依赖", 0)
                tail = f"（{dep} 条别的条目先修它）" if dep else ""
                lines.append(f"- `{it['id']}` · {it['title']} — `{it['path']}`{tail}")
            elif key == "review-blocked":
                evs = "、".join(f"`{e}`" for e in it.get("未读证据") or [])
                if it.get("无论证"):
                    why = "论证未写"
                elif it.get("无证据"):
                    why = "没有引用证据"
                else:
                    why = f"证据未读：{evs}"
                lines.append(f"- `{it['id']}` · {it['title']} —— {why}")
            elif key in ("translate", "methods"):
                lines.append(f"- `{it['id']}` · {it['title']} — `{it['path']}`")
            elif key == "todo":
                lines.append(f"- `{it['id']}` · {it['title']} —— {it['行']}")
            elif key in ("path-thin", "path-shallow"):
                outs = "、".join(it["成果"])
                lines.append(f"- `{it['id']}` · {it['title']} —— {outs}")
            else:
                lines.append(f"- {it.get('章') or it}")
        if limit and len(items) > limit:
            lines.append(f"- …还有 {len(items) - limit} 项")
    return "\n".join(lines)


def summary(data):
    """一行摘要：先看总量，再决定读哪一节。"""
    parts = [f"{data['分组'][k]['名称']} {data['分组'][k]['数量']}" for k in data["顺序"]]
    return " · ".join(parts)


def create_issues(data, limit):
    """只给**适合直接开工**的四组建 issue；其余几组需要判断或大块采集。"""
    made = 0
    tag = {"review": "复核", "translate": "译本", "methods": "教法",
           "external": "库外前置"}
    for key in ("review", "translate", "methods", "external"):
        for it in data["分组"][key]["条目"][:limit]:
            if key == "external":
                names = " / ".join(it.get("名称") or [it["标识"]])
                title = f"[{tag[key]}] {names}"
                objs = "、".join(f"`{x}`" for x in it.get("对象") or [])
                body = (f"`外部先修` 标识：`{it['标识']}`\n\n"
                        f"出现次数：{it['出现次数']}\n\n对象：{objs}\n\n"
                        f"学科：{' / '.join(it.get('学科') or [])}；"
                        f"学段：{' / '.join(it.get('学段') or [])}\n\n"
                        "先确认这条前置是否真实必需（M-12）。若决定建节点，"
                        "建好后把这些条目迁到 `edges.先修`，并删除对应的 `外部先修` 声明。")
            else:
                title = f"[{tag[key]}] {it['title']}"
                body = (f"条目：`{it['id']}`\n\n路径：`{it['path']}`\n\n"
                        + {"review": "按「复核一条」模板回答三个问题即可。",
                           "translate": "英文译本文件名由 `id` 派生，与中文原件同目录。",
                           "methods": "这个知识点还没有任何教法条目：缺的是「怎么讲」，"
                                      "需要教材里有标记的课堂做法（[BL]/[OL]/[AL]）。"}[key])
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
    data = collect()
    if "--json" in sys.argv:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return 0
    print("# 可开工的任务（由 tools/make_tasks.py 从库的现状生成）")
    print(f"\n> {summary(data)}")
    print(render(data, limit))
    if "--gh" in sys.argv:
        print("\n创建 issue：")
        n = create_issues(data, limit)
        print(f"\n共创建 {n} 个")
    else:
        print("\n（只读模式。加 `--gh` 才会建 issue。）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
