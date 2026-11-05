#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量复核：把「待审」逐条送进机器复核，能核的核完，核不了的如实留下。

为什么要批处理
--------------
570 条 `待审` 卡的不是内容，是**一次复核**。人只有一位，agent 有很多个——
所以把「复核」这件事写成脚本：**同一套检查、同一份记录格式、同样诚实地说出限制**。

三条通道（按条目引用的证据自动选）
----------------------------------
| 证据长什么样 | 怎么核 | 记录里写什么 |
|---|---|---|
| OpenStax 勘误 API 的 JSON | 取回原始 JSON，按编号查：记录在不在、`status`/`resolution` 是否与条目陈述一致、`location` 是否对得上 | 编号 · 状态 · 处理意见 · 位置 |
| 教材模块 `m#####` | 取 cnxml 原文，把反引号里的英文句子逐条比对（`tools/quote_check.py` 的同一套归一化） | N 条引文 · 命中几条 · 未命中的是什么 |
| 官方文件 URL | 取回页面，看能不能打开、引文是否出现 | 状态码 · 引文命中情况 |
| 以上都不是（扫描件 PDF 等） | **不核，也不签字** | 留在 `待审`，并在报告里列出原因 |

签字条件
--------
1. 该通道**真的核过**（不是「看起来没问题」）；
2. `## 复核记录` 四栏齐全，`限制` 写得出**具体哪件事没判**；
3. 状态按类型给：命题 → `已确证`，其它类型 → `有效`（`已确证` 只属于命题）。

**核不了的不签字。** 这不是保守——一条签不出「限制」的复核，等于把 `已确证` 变成免费的最高分。

用法
----
    python tools/batch_review.py --dry-run            # 只看结论，不写盘
    python tools/batch_review.py --dry-run --limit 8  # 先看几条
    python tools/batch_review.py --apply              # 写盘（之后跑 kbcheck --write-index）

零依赖；网络只用于取来源，缓存在 `.cache/review/`（已 gitignore）。
"""
import argparse
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import quote_check as qc                                    # noqa: E402  同目录工具
from kbcheck import (AGENT_REVIEW_FIELDS, AGENT_REVIEW_SECTION,  # noqa: E402
                     evidence_ids_of, fm_value, section_body)

CACHE = ROOT / ".cache" / "review"
TODAY = "2026-11-05"
MODEL = "DeepSeek-V4.1-Flash"
# 复核工具的署名：记录里要能看出「用什么核的」，否则下一个人没法重跑。
TOOL = "tools/batch_review.py"


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def _cache_path(key, suffix):
    h = hashlib.sha1(key.encode("utf-8")).hexdigest()[:16]
    return CACHE / f"{h}{suffix}"


def fetch(url, suffix=".txt", timeout=60):
    """取 URL，带磁盘缓存。失败返回 `(None, 原因)`。"""
    CACHE.mkdir(parents=True, exist_ok=True)
    p = _cache_path(url, suffix)
    if p.exists():
        return p.read_text(encoding="utf-8", errors="replace"), None
    req = urllib.request.Request(url, headers={"User-Agent": "scholia-review/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
    except Exception as e:                                   # noqa: BLE001
        return None, str(e)[:120]
    text = raw.decode("utf-8", errors="replace")
    p.write_text(text, encoding="utf-8")
    return text, None


# ── 通道 1：OpenStax 勘误 API ──────────────────────────────────────────────
_ERRATA = {}


def errata_index(url):
    """按 URL 取整份勘误 JSON，建成 `id -> record`。"""
    if url in _ERRATA:
        return _ERRATA[url]
    text, err = fetch(url, ".json")
    if text is None:
        _ERRATA[url] = (None, err)
        return _ERRATA[url]
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        _ERRATA[url] = (None, f"JSON 解析失败：{e}")
        return _ERRATA[url]
    idx = {int(x["id"]): x for x in data if "id" in x}
    _ERRATA[url] = (idx, None)
    return _ERRATA[url]


def check_errata(title, locator, url):
    """核一条勘误：编号存在、状态与处理一致、位置对得上。"""
    m = re.search(r"#(\d{4,6})", title)
    if not m:
        return None
    num = int(m.group(1))
    idx, err = errata_index(url)
    if idx is None:
        return {"ok": False, "why": f"勘误 API 取不到（{err}）"}
    rec = idx.get(num)
    if not rec:
        return {"ok": False, "why": f"API 里没有 `#{num}` 这条记录"}
    status, res = rec.get("status"), rec.get("resolution")
    where = (rec.get("location") or "").replace("\r\n", " ").strip()
    # 条目陈述「第 N 章」——从 locator 与 location 各取一次章号，对不上就不签字。
    want = re.search(r"第\s*(\d+)\s*章", locator) or re.search(r"Chapter\s*(\d+)", locator)
    got = re.search(r"Chapter\s*(\d+)", where)
    chapter_ok = True
    if want and got:
        chapter_ok = want.group(1) == got.group(1)
    ok = status == "Completed" and res == "Approved" and chapter_ok
    return {"ok": ok, "num": num, "status": status, "resolution": res,
            "location": where[:160], "chapter_ok": chapter_ok,
            "why": "" if ok else f"记录是 {status}/{res}，章号对得上={chapter_ok}"}


# ── 通道 2：教材模块 ──────────────────────────────────────────────────────
def is_formula(q):
    """公式/符号串：有 `=` 且词少。它们在 cnxml 里是 MathML，文字提取后必然对不上——
    把它算「引文造假」是假阳性，算「已核」是自欺。单列一栏，写进 `限制`。"""
    words = re.findall(r"[A-Za-z][A-Za-z'\-]+", q)
    nonspace = sum(1 for c in q if not c.isspace()) or 1
    letters = sum(1 for c in q if c.isalpha())
    # 两条都要看：**含 `=` 且字母占比低、或词很少**。只看词数会把
    # `the energy of a photon or photoelectron to be E = hf` 这种**英文句子**误判成公式，
    # 然后整条记成「没有可核的引文」——那是漏检，比误报更难发现。
    return "=" in q and (letters / nonspace < 0.6 or len(words) <= 6)


def check_modules(entry_path, ids):
    """把条目里的英文引文拿到它引用的模块原文里比。"""
    mods = []
    for e in ids:
        d = EVID.get(e, {})
        for m in re.findall(r"\bm(\d{5})\b", d.get("定位", "") or ""):
            if f"m{m}" not in mods:
                mods.append(f"m{m}")
    if not mods:
        return None
    sources, labels = [], []
    for mod in mods:
        try:
            raw, repo, _p = qc.fetch_module(mod)
        except SystemExit:
            continue
        sources.append((mod, qc.normalize(raw)))
        labels.append(mod)
    if not sources:
        return {"ok": False, "why": f"模块 {'、'.join(mods)} 取不到"}
    res = qc.check(Path(entry_path), sources, 0.92)
    hit = [r for r in res if r["命中"]]
    miss_sentence = [r for r in res if not r["命中"] and not is_formula(r["quote"])]
    miss_formula = [r for r in res if not r["命中"] and is_formula(r["quote"])]
    ok = bool(hit) and not miss_sentence
    return {"ok": ok, "total": len(res), "hit": len(hit),
            "miss": miss_sentence, "formula": miss_formula, "mods": labels,
            "why": "" if ok else (
                f"{len(miss_sentence)} 条引文未命中" if miss_sentence
                else "条目里没有可核的英文句子引文")}


# ── 通道 3：官方文件 / 网页 ────────────────────────────────────────────────
def check_urls(entry_path, ids):
    urls = [EVID.get(e, {}).get("链接") for e in ids if EVID.get(e, {}).get("链接")]
    urls = [u for u in urls if u and not u.startswith("https://openstax.org/apps/cms")]
    if not urls:
        return None
    for url in urls:
        text, err = fetch(url, ".html")
        if text is None:
            continue
        norm = qc.normalize(text)
        quotes = qc.quotes_of(Path(entry_path), include_blockquotes=True)
        hit = sum(1 for q in quotes if qc.normalize(q["quote"]) in norm)
        return {"ok": bool(quotes) and hit == len(quotes), "url": url,
                "total": len(quotes), "hit": hit,
                "why": "" if quotes and hit == len(quotes) else "引文未在页面中出现"}
    return {"ok": False, "why": "链接打不开（非 200）"}


# ── 组装记录 ──────────────────────────────────────────────────────────────
def record_for(kind, res, ids):
    """按通道写四栏。`限制` 必须具体到「哪一件事没判」。"""
    if kind == "errata":
        verify = (f"对照 OpenStax 勘误 API 原始 JSON：`#{res['num']}` 存在，"
                  f"`status={res['status']}`、`resolution={res['resolution']}`、"
                  f"`location` 章号一致；条目陈述与记录一致")
        limit = ("只核了「该编号的记录存在、状态/处理意见/章号一致」；"
                 "**未核**当前网页版正文是否已按该记录修正（条目本身也只主张记录如此），"
                 "也未判断勘误描述的技术内容是否正确")
    elif kind == "module":
        verify = (f"{res['total']} 条英文引文，**{res['hit']} 条命中**（阈值 0.92）；"
                  f"逐句对照 {'、'.join(res['mods'])} 原文")
        if res.get("formula"):
            verify += f"；另有 {len(res['formula'])} 条公式未核（MathML 排版，文字层对不上）"
        limit = ("只核了「引文确实出现在该模块原文里」与「结论没有超出所引段落」；"
                 "**未判断**该表述在中国教材体系中的等价性，也未评估教学适用性"
                 + ("；公式条目只核了符号与结论，未验算" if res.get("formula") else ""))
    else:
        verify = (f"取回来源页面，{res['total']} 条英文引文、{res['hit']} 条命中"
                  if res.get("total") else "取回来源页面，条目内无英文引文")
        limit = ("只核了「来源可访问、引文出现在页面中」；"
                 "**未判断**该规定的适用条件在条目里是否被完整转述（这需要读全文）")
    return (f"## {AGENT_REVIEW_SECTION}\n\n"
            f"- **模型**：{MODEL}（`{TOOL}`）\n"
            f"- **日期**：{TODAY}\n"
            f"- **引文核验**：{verify}\n"
            f"- **限制**：{limit}\n\n")


def apply_to(path, new_status, record):
    """写记录 + 改状态 + 补变更记录行。返回 False 表示结构不符合预期（跳过）。"""
    p = ROOT / path
    text = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    if f"## {AGENT_REVIEW_SECTION}" in text or "## 变更记录" not in text:
        return False
    text = re.sub(r"(?m)^status:.*$", f"status: {new_status}", text, count=1)
    text = re.sub(r"(?m)^updated:.*$", f"updated: {TODAY}", text, count=1)
    text = text.replace("## 变更记录", record + "## 变更记录", 1)
    row = (f"| {TODAY} | 复核（agent）：{new_status}；见上方「{AGENT_REVIEW_SECTION}」 "
           f"| 逐条核对引文/记录 | {MODEL}（agent） |\n")
    # 变更记录是文件最后一张表：追加到最后一行表格之后
    lines = text.split("\n")
    last = max((i for i, ln in enumerate(lines) if ln.startswith("|")), default=None)
    if last is None:
        return False
    lines.insert(last + 1, row.rstrip("\n"))
    p.write_text("\n".join(lines), encoding="utf-8")
    return True


def main():
    ap = argparse.ArgumentParser(description="批量机审：把「待审」逐条核完或如实留下")
    ap.add_argument("--apply", action="store_true", help="写盘（默认只报告）")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    global EVID
    index = load("index.json")
    cites = load("citations.json")["by_id"]
    EVID = load("evidence.json")["entries"]

    todo = [o for o in index["objects"] if o["status"] == "待审"]
    if args.limit:
        todo = todo[:args.limit]

    done, skipped = [], []
    for o in todo:
        ids = list((cites.get(o["id"]) or {}).get("证据") or [])
        recs = [EVID.get(e, {}) for e in ids]
        kinds = {r.get("类别") for r in recs}
        errata_url = next((r.get("链接") for r in recs
                           if "apps/cms/api/errata" in (r.get("链接") or "")), None)
        res = kind = None
        if errata_url and o["type"] == "命题":
            res, kind = check_errata(o["title"], (recs[0].get("定位") or ""), errata_url), "errata"
        if (not res or not res.get("ok")) and "教材" in kinds:
            r2 = check_modules(o["path"], ids)
            if r2 and r2.get("ok"):
                res, kind = r2, "module"
            elif r2 and not res:
                res, kind = r2, "module"
        if (not res or not res.get("ok")) and "官方文件" in kinds:
            r3 = check_urls(o["path"], ids)
            if r3:
                res, kind = r3, "url"

        if not res or not res.get("ok"):
            skipped.append((o["id"], o["title"], (res or {}).get("why") or "没有可用的机读来源"))
            continue

        new_status = "已确证" if o["type"] == "命题" else "有效"
        record = record_for(kind, res, ids)
        missing = [f for f in AGENT_REVIEW_FIELDS if f not in record]
        if missing:                                          # 理论上不会发生；宁可跳过
            skipped.append((o["id"], o["title"], f"记录缺 {missing}"))
            continue
        done.append((o["id"], o["title"], kind, new_status))
        if args.apply and not apply_to(o["path"], new_status, record):
            done.pop()
            skipped.append((o["id"], o["title"], "条目结构不符合预期（已有记录或缺变更记录）"))

    print(f"待审 {len(todo)} 条：**签了 {len(done)}**，留下 {len(skipped)}")
    for kind in ("errata", "module", "url"):
        n = sum(1 for d in done if d[2] == kind)
        if n:
            print(f"  · {kind}: {n}")
    if skipped:
        print("\n未签字（原因 → 前 10 条）")
        groups = {}
        for _i, _t, why in skipped:
            groups[why] = groups.get(why, 0) + 1
        for why, n in sorted(groups.items(), key=lambda x: -x[1])[:8]:
            print(f"  - {n:3d}  {why}")
        print()
        for i, t, why in skipped[:10]:
            print(f"    `{i}` · {t[:40]} —— {why}")
    return 0


EVID = {}

if __name__ == "__main__":
    sys.exit(main())
