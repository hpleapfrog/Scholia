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
    # 下标写法在 Markdown 里是 `V_rms`、在 cnxml 里是 `Vrms`：下划线不是文字，去掉再比。
    # 引文里常为了强调把关键词加粗（`**MUST NOT**`）：那是排版，不是原文的一部分。
    s = s.replace("**", "").replace("__", "")
    s = s.replace("_", "")
    # 上标与数量级：`3.0×10⁶` 与 `3.0× 10 6` 是**同一个数**的两种排法，
    # 而 cnxml 的 MathML 一定把它拆成 `10` + `<m:mn>6</m:mn>`。不归一化，物理条目会整片假阴性。
    s = s.translate(str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789"))
    # **先压空白，再处理「数字之间的空格」**：MathML 里 `10` 与 `6` 之间隔着
    # `<m:mspace>` 与换行，压缩前那是一个 `\n   `，不是空格——顺序反了就永远匹配不到。
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s*([×÷])\s*", r"\1", s)
    s = re.sub(r"(?<=[0-9]) (?=[0-9])", "", s)
    # 等号两侧的空格：`p = hλ` 与 `p=hλ` 是同一个式子。教科书排印与转写常不一样。
    s = re.sub(r" ?= ?", "=", s)
    # `[BL] [OL] [AL]` 与 `[bl][ol][al]` 是同一串标记的两种排法：方括号周围有没有空格不算差别。
    s = re.sub(r"[ \t]*([\[\]])[ \t]*", r"\1", s)
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
    # **表格里的反引号不是引文**：那是文件路径、哈希、注册表行（`rfc-editor.org/...`、
    # `451 / Unavailable For Legal Reasons / RFC 7725`）。把它们当引文去比，
    # 只会得到一堆「引文未在原文中出现」的假阳性。
    def _in_table(pos):
        start = text.rfind("\n", 0, pos) + 1
        return text[start:start + 1] == "|"
    found = [(m.start(), m.group(1)) for m in cands if not _in_table(m.start())]
    if include_blockquotes:
        # **整段引用块要合成一条**：RFC 的句子按 72 列折行，逐行比对必然失败，
        # 而失败的形状和「伪造引文」一模一样——这是最危险的一类假阳性。
        for block in re.finditer(r"(?m)(?:^>.*(?:\n|$))+", text):
            raw = block.group(0).rstrip("\n")
            body = " ".join(re.sub(r"^>\s?", "", ln) for ln in raw.split("\n"))
            inner = re.findall(r"`([^`\n]{%d,400})`" % MIN_CHARS, body)
            found.extend((block.start(), q) for q in inner)
            if not inner:
                found.append((block.start(), body.strip("`").strip()))
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
    joined_nospace = joined.replace(" ", "")
    for _label, text in sources:
        sents.extend(sentences(text))
    results = []
    for item in quotes_of(entry, include_blockquotes=True):
        q = normalize(item["quote"])
        if q and q in joined:
            results.append({**item, "命中": True, "相似度": 1.0, "原文": item["quote"]})
            continue
        # 句末标点不算差别：原文是陈述句 `…charge.`、条目写成疑问句 `…charge?` 的情形真实存在，
        # 而那是**转写的标点**，不是改动了原文。只对句末生效，句中一个字都不能动。
        # 长引文里若只差**空格排布**（MathML 把下标拆出来就会这样），按去空格再比一次。
        if len(q) >= 40 and q.replace(" ", "") in joined.replace(" ", ""):
            results.append({**item, "命中": True, "相似度": 1.0,
                            "原文": "（仅空格排布不同：" + item["quote"][:60] + "）"})
            continue
        if q and q.rstrip(" .?!") in joined:
            results.append({**item, "命中": True, "相似度": 1.0,
                            "原文": "（句末标点不同：" + item["quote"][:60] + "）"})
            continue
        # 引文里用 `...` / `…` 省略中间部分：**每一段都要在原文里**，否则不算命中。
        parts = [normalize(x).rstrip(" .?!") for x in re.split(r"\.{3}|…", q)
                 if len(normalize(x)) >= 8]
        if parts and all(p in joined or (len(p) >= 30 and p.replace(" ", "") in joined_nospace)
                         for p in parts):
            results.append({**item, "命中": True, "相似度": 1.0,
                            "原文": "（分段命中：" + " / ".join(x[:40] for x in parts) + "）"})
            continue
        best_r, best_s = 0.0, ""
        for s in sents:
            ratio = difflib.SequenceMatcher(None, q, s).quick_ratio()
            if ratio < best_r:
                continue
            ratio = difflib.SequenceMatcher(None, q, s).ratio()
            if ratio > best_r:
                best_r, best_s = ratio, s
        # 拼接引文：每一句都在原文里，但**不相邻**——中间被删掉了一段却没打省略号。
        # 这比「整句找不到」更常见，也更危险：读起来完全像原文。
        pieces = [normalize(x) for x in re.split(r"(?<=[.?!]) ", q) if len(x) >= 25]
        spliced = len(pieces) >= 2 and all(x in joined for x in pieces)
        results.append({**item, "命中": best_r >= threshold,
                        "相似度": round(best_r, 2), "原文": best_s,
                        "拼接": spliced})
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
            if r.get("拼接"):
                print("      ⚠ 疑似**拼接引文**：每一句都在原文里，但彼此不相邻"
                      "（中间省略的内容没有标 `…`）")
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
