#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抽取 OpenStax 教材里 Teacher Support 的受众标记（结果见 os-teacher-markers.csv）。

为什么要有这个脚本：本库曾声称「统计可复算」而**库里既没有脚本也没有数据**——
那是一次被对抗审查击中的错误。这个脚本补上那个支点。

## 它做什么

1. 读 `collections/physics.collection.xml`，取出全部 `<col:module>`（含所属章）
2. 取每个模块的 `modules/<id>/index.cnxml`
3. 找出 `class="os-teacher"` 的 `<note>`（**不是全部 `<note>`**——这个过滤条件是关键，
   早先没写明，照字面实现会得到不同的数）
4. 在这些 note 里，找出**每个 `<para>` 开头的受众标记** `<span>[BL]</span>` 这种
5. 输出明细 CSV：每个（模块 × 章 × 段落）一行

## 粒度（重要）

标记挂在 **`<para>`** 上，不是 `note` 上。所以：

- 「有多少个标记」= **段落级**计数
- 一条建议可以**同时**标给多个群体（`<span>[BL]</span><span>[OL]</span>`）
- 因此**不能**把「标记数」读成「档位卡数」

## 复算

```bash
python evidence/os-teacher-markers.py            # 需要能访问 api.github.com
python evidence/os-teacher-markers.py --ref main # 可指定 ref（默认 main）
```

会同时打印所用 ref 的 **commit 哈希**——没有它，「可复算」只是一句话。

**许可**：OpenStax《Physics》为 CC BY 4.0，本脚本只做统计与短引用。
"""
from __future__ import annotations

import argparse
import base64
import csv
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

REPO = "openstax/osbooks-physics"
API = "https://api.github.com"
HERE = os.path.dirname(os.path.abspath(__file__))
MARKERS = ("BL", "OL", "AL", "EL")
TAG = re.compile(r"^\[(" + "|".join(MARKERS) + r")\]")


def token() -> str:
    """优先环境变量，其次 git credential（避免把令牌写进仓库）。"""
    t = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if t:
        return t.strip()
    try:
        import subprocess
        out = subprocess.run(
            ["git", "credential", "fill"],
            input="protocol=https\nhost=github.com\n\n",
            capture_output=True, text=True, timeout=20).stdout
        m = re.search(r"^password=(.*)$", out, re.M)
        if m:
            return m.group(1).strip()
    except Exception:
        pass
    return ""


def api(path: str, tok: str):
    req = urllib.request.Request(
        f"{API}/repos/{REPO}/{path}",
        headers={"User-Agent": "scholia-kbcheck",
                 "Accept": "application/vnd.github+json",
                 **({"Authorization": f"Bearer {tok}"} if tok else {})})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def fetch_text(path: str, tok: str, ref: str) -> str:
    j = api(f"contents/{path}?ref={ref}", tok)
    return base64.b64decode(j["content"]).decode("utf-8", "replace")


def localname(el) -> str:
    return el.tag.rsplit("}", 1)[-1] if isinstance(el.tag, str) else ""


def parse_collection(xml: str):
    """返回 [(chapter_index, chapter_title, module_id)]。

    **cnxml 有默认命名空间，`el.tag == "module"` 永远为假**——必须按 localname 匹配。
    """
    root = ET.fromstring(xml)
    out = []
    ci = 0
    for sub in root.iter():
        if localname(sub) != "subcollection":
            continue
        ci += 1
        title = ""
        for ch in sub:
            if localname(ch) == "title":
                title = "".join(ch.itertext()).strip()
                break
        for mod in sub.iter():
            if localname(mod) != "module":
                continue
            mid = mod.get("document") or mod.get("{http://cnx.org/ns/col}document") or ""
            if mid:
                out.append((ci, title, mid))
    return out


def parse_module(xml: str, mid: str):
    """返回 (严格行, 宽松计数)。

    **两种口径，结果不同——这不是 bug，是必须写明的规则。**

    - **严格**：标记是 `<para>` 开头的连续 `<span>[XX]</span>`
      —— 对应「这条**建议**给哪些群体」
    - **宽松**：`os-teacher` note 文本里出现 `[XX]` 即计入
      —— 会多抓到**裸文本**标记（如 `<span>[BL]</span>[EL]English learners…`
      里的 `[EL]` 不在 span 内）

    本库历史上声称的 `649` 与脚本严格规则的 `637` **不一致**，
    差别就来自这里。**「可复算」必须连同规则一起给出。**
    """
    root = ET.fromstring(xml)
    strict, loose = [], {m: 0 for m in MARKERS}
    note_count = 0
    for note in root.iter():
        if localname(note) != "note":
            continue
        cls = note.get("class") or ""
        if "os-teacher" not in cls:
            continue            # ← 关键过滤：不是全部 <note>
        note_count += 1
        text = "".join(note.itertext())
        for m in MARKERS:
            loose[m] += text.count(f"[{m}]")
        pi = 0
        for para in note.iter():
            if localname(para) != "para":
                continue
            pi += 1
            marks = []
            for child in para:
                if localname(child) != "span":
                    break
                t = "".join(child.itertext()).strip()
                mm = TAG.match(t)
                if mm:
                    marks.append(mm.group(1))
                else:
                    break
            if marks:
                body = " ".join("".join(para.itertext()).split())
                strict.append((mid, cls, pi, marks, body[:80]))
    return strict, loose, note_count


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="main")
    ap.add_argument("--out", default=os.path.join(HERE, "os-teacher-markers.csv"))
    args = ap.parse_args()

    tok = token()
    if not tok and os.environ.get("SCHOLIA_REQUIRE_TOKEN"):
        print("需要 GITHUB_TOKEN（未设 SCHOLIA_REQUIRE_TOKEN 时可匿名，但速率很低）", file=sys.stderr)

    # 记录所用 commit —— 没有它，「可复算」只是一句话
    try:
        commit = api(f"commits/{args.ref}", tok)["sha"]
    except Exception as e:
        commit = f"(取不到: {type(e).__name__})"
        print(f"警告：取不到 commit 哈希：{e}", file=sys.stderr)

    coll = fetch_text("collections/physics.collection.xml", tok, args.ref)
    mods = parse_collection(coll)
    chapters = sorted({(c, t) for c, t, _ in mods})
    print(f"ref={args.ref}  commit={commit}")
    print(f"章级 subcollection: {len(chapters)}   章内 module: {len(mods)}")

    all_rows, counts = [], {m: 0 for m in MARKERS}
    loose_total = {m: 0 for m in MARKERS}
    note_total = 0
    per_module = []
    for ci, title, mid in mods:
        try:
            xml = fetch_text(f"modules/{mid}/index.cnxml", tok, args.ref)
        except Exception as e:
            print(f"  跳过 {mid}: {type(e).__name__}", file=sys.stderr)
            continue
        strict, loose, ncount = parse_module(xml, mid)
        note_total += ncount
        for m in MARKERS:
            loose_total[m] += loose[m]
        for _, _, _, marks, _ in strict:
            for m in marks:
                counts[m] += 1
        per_module.append((ci, mid, len(strict)))
        for _, cls, pi, marks, body in strict:
            all_rows.append((commit, ci, title, mid, cls, pi, "+".join(marks), body))

    print(f"`os-teacher` 便签总数: {note_total}")
    print()
    print(f"{'标记':<8}{'严格（段落 span）':>18}{'宽松（任意出现）':>18}")
    for m in MARKERS:
        print(f"[{m}]".ljust(8) + f"{counts[m]:>18}{loose_total[m]:>18}")
    print(f"{'合计':<8}{sum(counts.values()):>18}{sum(loose_total.values()):>18}")
    print()
    print("含标记的模块: %d / %d" % (len(per_module), len(mods)))
    print()
    print("注：本库历史声称的 649（BL 207 / OL 245 / AL 191 / EL 6）与上面两列都不等——")
    print("    那是一次**规则未写明**的旧统计。两列之差即口径之差（[EL] 常为裸文本，不在 span 内）。")

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["commit", "chapter_index", "chapter", "module", "note_class",
                    "para_index", "markers", "text_head"])
        w.writerows(all_rows)
    print(f"明细已写入 {args.out}（{len(all_rows)} 行）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
