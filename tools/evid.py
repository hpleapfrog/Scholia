#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""领一个证据编号：`ev-###` 不能在脑子里数，也不能只看自己这一支。

为什么要有
----------
2026-11-05 实测到一次撞号：本地主干上新写的三条草稿引用了 `ev-196`，
而另一条分支 `events/irkutsk-conference-postponed`（PR #130）**也**在用 `ev-196`。
两边都「按规则数了下一个空号」，两边都没错，**合并时才撞**。

编号是**全局唯一键**，但它是**手工分配**的，而手工分配看不见别的分支。
`R-EVID-01` 只能在合并之后报「引用了不存在的编号」——那时两边的稿子都已经写完。

这个脚本把「哪一号还空着」变成一条命令：它扫**当前工作区 + 全部 ref**。

用法
----
    python tools/evid.py next            # 下一个真正空着的编号
    python tools/evid.py next --n 3      # 连着领三个（写多条时要一次领够）
    python tools/evid.py --check         # 哪些编号「已经有人在用，但还没登记」

`--check` 的读法
----------------
列出来的编号是**在飞**的：某个分支或工作区已经引用了它，但 `evidence/README.md`
里还没有这一行。合并前必须把它们补齐；否则 `kbcheck` 会在合并那一刻失败。
这不是错误清单，是**合并前的对账单**。

边界
----
- 只看 `ev-\\d{3}`；编号补零到三位，超过 999 之后本脚本会按同样的规则继续（`ev-1000`）。
- **不判断该不该引用**：它分配的只是编号，来源三问（`M-11`）仍然要人答。
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATTERN = re.compile(r"ev-(\d{3,4})")
SCAN_DIRS = ["knowledge", "events", "evidence", "drafts", "templates", "docs"]


def _git(*args):
    try:
        out = subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                             text=True, encoding="utf-8", timeout=120)
    except (OSError, subprocess.SubprocessError):
        return ""
    return out.stdout if out.returncode == 0 else ""


def registered():
    """`evidence/README.md` 里已登记的编号（这是唯一权威的一列）。"""
    p = ROOT / "evidence" / "README.md"
    if not p.exists():
        return set()
    ids = set()
    for line in p.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(ev-\d+)\s*\|", line.strip())
        if m:
            ids.add(m.group(1))
    return ids


def in_tree():
    """工作区里**被引用**的编号（含草稿：草稿也可能带着编号进库）。"""
    used = {}
    for d in SCAN_DIRS:
        base = ROOT / d
        if not base.exists():
            continue
        for p in base.rglob("*.md"):
            try:
                text = p.read_text(encoding="utf-8")
            except OSError:
                continue
            for m in PATTERN.finditer(text):
                used.setdefault(f"ev-{m.group(1)}", set()).add(
                    p.relative_to(ROOT).as_posix())
    return used


def in_refs():
    """全部本地分支 / 远端分支里引用的编号 —— 撞号就撞在这里。"""
    refs = [r for r in _git("for-each-ref", "--format=%(refname)", "refs/heads", "refs/remotes")
            .splitlines() if r.strip()]
    out = {}
    for ref in refs:
        # `git grep` 只看该 ref 里的内容；路径限定在可能放编号的目录。
        text = _git("grep", "-h", "-o", "-E", r"ev-[0-9]{3,4}", ref, "--", *SCAN_DIRS)
        for m in PATTERN.finditer(text):
            key = f"ev-{m.group(1)}"
            out.setdefault(key, set()).add(ref.split("refs/")[-1])
    return out


def next_free(taken, n):
    num = max((int(x.split("-")[1]) for x in taken), default=0)
    picks = []
    while len(picks) < n:
        num += 1
        cand = f"ev-{num:03d}"
        if cand not in taken:
            picks.append(cand)
    return picks


def main():
    ap = argparse.ArgumentParser(description="分配 / 核对证据编号 ev-###")
    ap.add_argument("action", nargs="?", default="next", choices=["next", "check"])
    ap.add_argument("--n", type=int, default=1, help="一次领几个（默认 1）")
    args = ap.parse_args()

    reg = registered()
    tree = in_tree()
    refs = in_refs()
    # `ev-000` 是 `templates/` 里的**占位符**，不是编号；把它当占用会让下一号从 001 重来。
    for bucket in (tree, refs):
        bucket.pop("ev-000", None)
    taken = set(reg) | set(tree) | set(refs)

    if args.action == "check":
        inflight = {k: v for k, v in {**{k: set(v) for k, v in tree.items()},
                                     **{k: set(v) for k, v in refs.items()}}.items()
                    if k not in reg}
        if not inflight:
            print("没有「在飞」的编号：工作区与各分支引用的 ev-### 都已登记。")
            return 0
        print("已在用、但 evidence/README.md 里还没登记（合并前补齐）：")
        for k in sorted(inflight):
            where = sorted(inflight[k])[:4]
            more = "" if len(inflight[k]) <= 4 else f" 等 {len(inflight[k])} 处"
            print(f"  {k} —— {', '.join(where)}{more}")
        print()
        print("这些编号**不要重新分配**：它们已经被写了，补登记即可。")
        return 0

    picks = next_free(taken, args.n)
    print(" ".join(picks))
    print()
    print(f"已占用的最大编号：ev-{max((int(x.split('-')[1]) for x in taken), default=0):03d}"
          f"（登记 {len(reg)} · 工作区 {len(tree)} · 分支 {len(refs)}）")
    far = {k: v for k, v in refs.items() if k not in reg}
    if far:
        print("其它分支已占用、但还没登记（**不要用这些编号**）：")
        for k in sorted(far):
            print(f"  {k} —— {', '.join(sorted(far[k]))[:80]}")
    print()
    print("领到编号之后：在 evidence/README.md 加一行（来源三问见 M-11），"
          "再跑 python tools/kbcheck.py --write-index。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
