#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""引文核验：条目里那些**加了引号的英文句子**，原文里到底有没有。

为什么要有
----------
本库全部的规则都在查「结构」：编号登记了没有、链接通不通、锚点存不存在。
**没有一条规则打开来源，看那句话本身在不在。** 于是最危险的一类错误畅通无阻：

    把转述写进引号。

它比一个明显写错的句子更糟——明显写错的会被读者发现，而
`Temperature is literally defined as what we measure on a thermometer.`
读起来完全像教材，只有翻到原文那一页才知道原文写的是
`operationally defined to be what we measure with a thermometer`。

实测：2026-11-05 的三条物理草稿共 31 条英文引文，对来源逐条比对，**0 条命中**
（见 `drafts/README.md`）。这个脚本就是那次事故的产物。

它回答什么、不回答什么
----------------------
| 回答 | 不回答 |
|---|---|
| 「这句话在来源正文里出现了吗」 | 「这句话说得对吗」 |
| 「最接近的原文是哪一句、差多少」 | 「这条论证站不站得住」 |

**命中不等于论点正确**，未命中也不必然是指控：可能是引文跨了段落、
可能是译者加了连接词。所以它报的是**相似度与原文句子**，由人裁决。

用法
----
    # 拿条目自己登记的 evidence 去定位模块（需要 evidence.json 里能解析出 m#####）
    python tools/quote_check.py knowledge/physics/concepts/简谐运动.md

    # 指定本地来源（.cnxml / .txt / .md 都行；可给多个）
    python tools/quote_check.py drafts/physics/温度与温标.md --source .cache/cp13/m42214.cnxml

    # 指定模块编号，走 tools/os_source.py 的同一套缓存与三个源仓库
    python tools/quote_check.py 某条目.md --module m42216

    # 只看不通过的那几条 / 机器可读
    python tools/quote_check.py 某条目.md --module m42217 --only-miss --json

退出码
------
    0  全部引文命中（相似度 ≥ 阈值）
    1  有引文未命中
    2  用法错误：给不出任何来源
"""
import argparse
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

CACHE = ROOT / ".cache" / "os"
REPOS = ["osbooks-physics", "osbooks-college-physics", "osbooks-university-physics"]
RAW = "https://raw.githubusercontent.com/openstax/{repo}/main/modules/{mod}/index.cnxml"
MODULE = re.compile(r"\bm(\d{5})\b")

# 引文的准入条件：太短的（`p = F/A`、`CC BY 4.0`）不当作「引文」查——
# 它们是指号，不是句子；拿它们去比对只会制造噪音。
MIN_CHARS = 24
MIN_WORDS = 5


def normalize(s):
    """把 Markdown / cnxml / 各种排印符号压成可比对的形式。

    **不能只做 strip**：cnxml 里 `v` 与 `rms` 分处两个标签，`−` 是 U+2212 而不是
    连字符，弯引号与直引号在字节层面完全不同。不统一这些，命中率会被排版差异吃掉。
    """
    s = re.sub(r"<[^>]+>", "", s)
    for a, b in [("\u2212", "-"), ("\u2013", "-"), ("\u2014", "-"),
                 ("\u2018", "'"), ("\u2019", "'"),
                 ("\u201c", '"'), ("\u201d", '"'),
                 ("\u00a0", " "), ("\u2009", " "), ("\u202f", " ")]:
        s = s.replace(a, b)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def sentences(text):
    """切成句子——不是为了语法，是为了给「最接近的原文」一个可读的落点。"""
    out = []
    for part in re.split(r"(?<=[.!?])\s+|\n{2,}", text):
        p = part.strip()
        if 20 < len(p) < 600:
            out.append(p)
    return out


def quotes_of(path, include_blockquotes=False):
    """取出条目里**当作原文引用**的片段。

    两种载体：反引号（本库的常规写法）与 `> ` 引用块（整段摘录）。
    只收英文句子——中文引文没法用字面比对验证，硬比只会给出假阴性。
    """
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    cands = list(re.finditer(r"`([^`\n]{%d,400})`" % MIN_CHARS, text))
    found = [(m.start(), m.group(1)) for m in cands]
    if include_blockquotes:
        for m in re.finditer(r"^> (.{24,400})$", text, re.M):
            # 引用块里常写成 `> \`the passage\``：反引号是排版，不是引文的一部分。
            # 不剥掉它，同一条引文会被当成两条——一条命中、一条「未命中」，虚报一个失败。
            found.append((m.start(), m.group(1).lstrip("> ").strip().strip("`").strip()))
    out, seen = [], set()
    for pos, q in sorted(found):
        q = q.strip()
        ascii_ratio = sum(1 for c in q if ord(c) < 128) / max(1, len(q))
        words = len(re.findall(r"[A-Za-z][A-Za-z'\-]+", q))
        if ascii_ratio < 0.9 or words < MIN_WORDS:
            continue
        key = normalize(q)
        if key in seen:
            continue
        seen.add(key)
        line = text.count("\n", 0, pos) + 1
        out.append({"quote": q, "line": line})
    return out


def load_sources(paths):
    """读本地来源文件，返回 [(标签, 规范化正文)]。"""
    out = []
    for p in paths:
        p = Path(p)
        if not p.exists():
            raise SystemExit(f"x 来源文件不存在：{p}")
        out.append((str(p), normalize(p.read_text(encoding="utf-8"))))
    return out


def fetch_module(mod):
    """按 os_source.py 的同一套缓存与仓库顺序取模块原文。"""
    CACHE.mkdir(parents=True, exist_ok=True)
    for name in REPOS:
        p = CACHE / f"{name}__{mod}.cnxml"
        if p.exists():
            return p.read_text(encoding="utf-8"), name, p
    import urllib.request
    errors = []
    for name in REPOS:
        try:
            with urllib.request.urlopen(RAW.format(repo=name, mod=mod), timeout=60) as r:
                data = r.read().decode("utf-8")
        except Exception as e:                                   # noqa: BLE001
            errors.append(f"{name}: {e}")
            continue
        p = CACHE / f"{name}__{mod}.cnxml"
        p.write_text(data, encoding="utf-8")
        return data, name, p
    raise SystemExit(f"x 三个源仓库都取不到 {mod}\n  " + "\n  ".join(errors))


def modules_from_evidence(entry):
    """从条目 front-matter 的 `evidence` → `evidence.json` 的 `定位` 里找 `m#####`。"""
    text = entry.read_text(encoding="utf-8")
    head = text[:text.find("\n---", 3)] if text.startswith("---") else ""
    ids = re.findall(r"ev-\d+", head)
    evp = ROOT / "evidence.json"
    if not ids or not evp.exists():
        return []
    evid = json.loads(evp.read_text(encoding="utf-8")).get("entries", {})
    mods = []
    for e in ids:
        m = MODULE.search((evid.get(e) or {}).get("定位") or "")
        if m and f"m{m.group(1)}" not in mods:
            mods.append(f"m{m.group(1)}")
    return mods


def check(entry, sources, threshold):
    """逐条引文在来源里找。返回结果列表（含最接近的原文句）。"""
    sents, joined = [], " ".join(t for _l, t in sources)
    for _label, text in sources:
        sents.extend(sentences(text))
    results = []
    for item in quotes_of(entry, include_blockquotes=True):
        q = normalize(item["quote"])
        if q and q in joined:
            results.append({**item, "命中": True, "相似度": 1.0, "原文": item["quote"]})
            continue
        best_r, best_s = 0.0, ""
        for s in sents:
            ratio = difflib.SequenceMatcher(None, q, s).quick_ratio()
            if ratio < best_r:
                continue
            ratio = difflib.SequenceMatcher(None, q, s).ratio()
            if ratio > best_r:
                best_r, best_s = ratio, s
        results.append({**item, "命中": best_r >= threshold,
                        "相似度": round(best_r, 2), "原文": best_s})
    return results


def main():
    ap = argparse.ArgumentParser(
        description="核对条目里的英文引文是否真的出现在来源正文里")
    ap.add_argument("entry", help="条目（.md）路径")
    ap.add_argument("--source", action="append", default=[],
                    help="本地来源文件（可重复）；.cnxml/.txt/.md 均可")
    ap.add_argument("--module", action="append", default=[],
                    help="OpenStax 模块编号（如 m42214，可重复）")
    ap.add_argument("--threshold", type=float, default=0.92,
                    help="判定为「同一句」的最低相似度（默认 0.92）")
    ap.add_argument("--only-miss", action="store_true", help="只打印未命中的")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    args = ap.parse_args()

    entry = Path(args.entry)
    if not entry.exists():
        raise SystemExit(f"x 条目不存在：{entry}")

    sources, labels = [], []
    if args.source:
        sources = load_sources(args.source)
        labels = [p for p, _t in sources]
    for mod in args.module:
        raw, repo, path = fetch_module(mod)
        sources.append((f"{mod} @ {repo}", normalize(raw)))
        labels.append(f"{mod} @ {repo}（缓存 {path.relative_to(ROOT)}）")
    if not sources:
        mods = modules_from_evidence(entry)
        if not mods:
            raise SystemExit(
                "x 给不出来源：条目里没有可解析的 `m#####` 定位。\n"
                "  用 --source 指定本地来源，或 --module 指定模块编号。")
        for mod in mods:
            raw, repo, path = fetch_module(mod)
            sources.append((f"{mod} @ {repo}", normalize(raw)))
            labels.append(f"{mod} @ {repo}（缓存 {path.relative_to(ROOT)}）")

    results = check(entry, sources, args.threshold)
    hit = sum(1 for r in results if r["命中"])

    if args.json:
        print(json.dumps({
            "entry": str(entry),
            "sources": labels,
            "threshold": args.threshold,
            "total": len(results),
            "hit": hit,
            "results": results,
        }, ensure_ascii=False, indent=1))
        return 0 if hit == len(results) else 1

    print(f"条目：{entry}")
    for lab in labels:
        print(f"来源：{lab}")
    print(f"引文 {len(results)} 条 · 命中 {hit} · 未命中 {len(results) - hit}"
          f"（阈值 {args.threshold}）")
    print()
    for r in results:
        if args.only_miss and r["命中"]:
            continue
        mark = "OK " if r["命中"] else "XX "
        print(f"{mark}{r['相似度']:.2f}  L{r['line']}  {r['quote'][:96]}")
        if not r["命中"]:
            print(f"      原文：{r['原文'][:200]}")
        print()
    if hit != len(results):
        print("未命中的引文**不要留在引号里**：要么改成原文，要么去掉引号写成自己的话。")
        print("（跨段落引用、译者补连接词也会造成未命中——这一条由人裁决，脚本不替你判。）")
        return 1
    print("全部命中。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
