#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""取某个知识点的教材原文（Teacher Support），用来写 `教法`。

为什么要有
----------
写 `教法` 需要「教材建议怎么教」的**原文**。手工找一遍的路径是：

   概念 front-matter 的 evidence → evidence.json 的定位 → m##### →
   raw.githubusercontent.com/openstax/osbooks-physics/main/modules/<m>/index.cnxml

这条路能走通，但每一步都容易记错（openstax.org 的网页是 SPA 空壳，抓不到正文）。
把它固化成脚本，剩下四十多条教法才好推进。

用法
----
    python tools/os_source.py 电容                 # 按概念文件名（不带 .md）
    python tools/os_source.py knowledge/physics/concepts/电容.md
    python tools/os_source.py --list               # 列出所有能定位到模块的概念

缓存
----
下载的 cnxml 放在 `.cache/os/`（已在 .gitignore），不提交；`--refresh` 强制重下。

**许可**：OpenStax《Physics》为 CC BY 4.0。本脚本只做**定位与短摘录**，不整段转载。
"""
import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "os"
# 同一个 m##### 可能在不同的书里：Physics、College Physics、University Physics 各有源仓库。
# 只试第一个会 404（实测：m42324 / m42344 就不在 osbooks-physics 里）。
REPOS = ["osbooks-physics", "osbooks-college-physics", "osbooks-university-physics"]
RAW = "https://raw.githubusercontent.com/openstax/{repo}/main/modules/{mod}/index.cnxml"
MODULE = re.compile(r"\bm(\d{5})\b")


def load_evidence():
    p = ROOT / "evidence.json"
    if not p.exists():
        raise SystemExit("x 缺少 evidence.json —— 先跑 python tools/kbcheck.py --write-index")
    return json.loads(p.read_text(encoding="utf-8")).get("entries", {})


def module_of(concept: Path, evid: dict):
    """从概念的 front-matter 取 evidence 编号，再从证据定位里取 m#####。"""
    text = concept.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, None
    fm = text[4:text.find("\n---", 3)]
    ids = re.findall(r"ev-\d+", fm)
    for e in ids:
        loc = (evid.get(e) or {}).get("定位") or ""
        m = MODULE.search(loc)
        if m:
            return "m" + m.group(1), e
    return None, (ids[0] if ids else None)


def fetch(module: str, refresh=False):
    """按 REPOS 顺序试，命中即返回 (文本, 实际仓库)。"""
    CACHE.mkdir(parents=True, exist_ok=True)
    for name in REPOS:
        p = CACHE / f"{name}__{module}.cnxml"
        if p.exists() and not refresh:
            return p.read_text(encoding="utf-8"), name
    errors = []
    for name in REPOS:
        url = RAW.format(repo=name, mod=module)
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                data = r.read().decode("utf-8")
        except Exception as e:                               # noqa: BLE001
            errors.append(f"{name}: {e}")
            continue
        (CACHE / f"{name}__{module}.cnxml").write_text(data, encoding="utf-8")
        return data, name
    raise SystemExit("x 三个源仓库都没找到 " + module + chr(10) + "  " + chr(10).join(errors))


def teacher_blocks(xml: str):
    """取出每段 Teacher Support 的纯文本（含 [BL]/[OL]/[AL] 标记）。"""
    out = []
    for m in re.finditer("Teacher Support", xml):
        seg = xml[m.start():m.start() + 2600]
        txt = re.sub(r"<[^>]+>", " ", seg)
        txt = re.sub(r"\s+", " ", txt).strip()
        # 只保留到下一段 Teacher Support 之前
        cut = txt.find("Teacher Support", 20)
        out.append(txt[:cut] if cut > 0 else txt)
    # 去重（同一段常被抓两遍：标题 + 正文）
    uniq, seen = [], set()
    for t in out:
        k = t[:60]
        if k in seen:
            continue
        seen.add(k)
        uniq.append(t)
    return uniq


def concepts():
    return sorted((ROOT / "knowledge").rglob("concepts/*.md"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("concept", nargs="?", help="概念文件名（不含 .md）或路径")
    ap.add_argument("--list", action="store_true", help="列出能定位到模块的概念")
    ap.add_argument("--scan", action="store_true",
                    help="扫描「还没有教法」的概念：它们的原文里有没有 Teacher Support")
    ap.add_argument("--refresh", action="store_true", help="强制重新下载")
    ap.add_argument("--max", type=int, default=4, help="最多打印几段")
    args = ap.parse_args()

    evid = load_evidence()

    if args.list:
        for p in concepts():
            if p.name.endswith(".en.md"):
                continue
            mod, e = module_of(p, evid)
            print(f"{p.stem:<24} {mod or '—':<8} {e or ''}")
        return 0

    if args.scan:
        have, lack = [], []
        covered = set()
        for mp in (ROOT / "knowledge").rglob("methods/*.md"):
            if mp.name.endswith(".en.md"):
                continue
            fm = mp.read_text(encoding="utf-8")
            for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", fm.split("---")[1] if fm.startswith("---") else ""):
                covered.add(Path(link).stem)
        for p in concepts():
            if p.name.endswith(".en.md") or p.stem in covered:
                continue
            mod, _e = module_of(p, evid)
            if not mod:
                lack.append((p.stem, "无模块定位"))
                continue
            try:
                xml, repo = fetch(mod)
            except SystemExit:
                lack.append((p.stem, f"{mod} 取不到"))
                continue
            n = len(teacher_blocks(xml))
            (have if n else lack).append((p.stem, f"{mod} @{repo.replace('osbooks-','')}" if n else f"{mod} 无 Teacher Support"))
        print(f"有原文可用：{len(have)}（这些可以直接写）")
        for name, info in have:
            print(f"  + {name:<26} {info}")
        print()
        print(f"需另找来源：{len(lack)}")
        for name, info in lack:
            print(f"  - {name:<26} {info}")
        return 0

    if not args.concept:
        ap.print_help()
        return 1

    target = Path(args.concept)
    if not target.exists():
        cand = [p for p in concepts()
                if p.name == args.concept or p.stem == args.concept]
        if not cand:
            raise SystemExit(f"x 找不到概念：{args.concept}")
        target = cand[0]

    mod, e = module_of(target, evid)
    if not mod:
        raise SystemExit(f"x {target.name} 的 evidence 里没有 m##### 定位，取不到模块")
    xml, repo = fetch(mod, args.refresh)
    print(f"# {target.stem} —— {mod}（{e}）@ {repo}")
    print(f"# 源：{RAW.format(repo=repo, mod=mod)}")
    print()
    blocks = teacher_blocks(xml)
    if not blocks:
        print("！这个模块里没有 Teacher Support（也没有 [BL]/[OL]/[AL] 标记）。")
        print("  这本书可能根本不带教学提示（实测：College Physics 就完全没有）。")
        print("  写 `教法` 需要另找来源，或者暂时留空——**不要凭印象补**。")
        return 2
    for b in blocks[:args.max]:
        print("-" * 70)
        print(b)
        print()
    print(f"（共 {len(blocks)} 段 Teacher Support）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
