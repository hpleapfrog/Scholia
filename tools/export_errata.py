#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把全库的**勘误**导成一份能直接用的表。

为什么要单独导
--------------
本库最不可替代的资产不是「一个知识库」，是 **500 多条教科书勘误**：
每一条都指到某本书的某一处，写着原来说了什么、出版方接受与否。
但它们现在是 500 多个 `.md` 文件——教师想查「这本教材第 6 章有哪些已确认的错」，
得一个个点开。

**一份 CSV 就能回答这个问题。** 教师、出版社编辑、写教材的人不需要 Git，也不需要读规范。

导出什么
--------
`type=命题` 且标题以「勘误」开头的对象（本库的约定：勘误条目一律这样起标题）。
列见 `FIELDS`；`溯源` 与 `状态` 一起给，读的人才知道**这条有多硬**。

用法
----
    python tools/export_errata.py                 # 写 exports/errata.csv + errata.json
    python tools/export_errata.py --check         # 只比对：与磁盘上的不一致就退出码 1

**`--check` 存在的理由**：导出的表是生成物。内容一改、表没重导，它就开始骗人——
而「看起来像数据的东西过期了」比没有这份数据更糟。CI 里跑 `--check` 就能挡住。

边界
----
- 只导**已有条目**，不改判定：`状态` 是条目自己的，`溯源` 是本脚本读 `index.json` 得来的。
- 不合并重复、不改写标题、不翻译——导出层不加任何本库没有的判断。
"""
import argparse
import csv
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "exports"
CSV_PATH = OUT_DIR / "errata.csv"
JSON_PATH = OUT_DIR / "errata.json"

FIELDS = [
    ("学科", "subject"),
    ("本库条目", "id"),
    ("勘误编号", "errata_no"),
    ("标题", "title"),
    ("原文位置", "locator"),
    ("永久链接", "url"),
    ("状态", "status"),
    ("溯源档", "tier"),
    ("本库路径", "path"),
]


def load(name):
    p = ROOT / name
    if not p.exists():
        raise SystemExit(f"x 缺少 {name} —— 先跑 python tools/kbcheck.py --write-index")
    return json.loads(p.read_text(encoding="utf-8"))


def collect():
    """挑出勘误条目，拼上引用材料里**已解析好**的定位。"""
    index = load("index.json")
    cites = load("citations.json").get("by_id", {})
    evid = load("evidence.json").get("entries", {})
    rows = []
    for o in index.get("objects", []):
        if o.get("type") != "命题" or not (o.get("title") or "").startswith("勘误"):
            continue
        cite = cites.get(o["id"], {})
        ids = cite.get("证据") or []
        first = evid.get(ids[0], {}) if ids else {}
        title = o["title"]
        no = ""
        m = title.split("#", 1)
        if len(m) == 2 and m[1][:1].isdigit():
            no = "".join(ch for ch in m[1].split("：")[0] if ch.isdigit())
        rows.append({
            "subject": (o.get("学科") or "").split(" ")[0],
            "id": o["id"],
            "errata_no": no,
            "title": title,
            "locator": (first.get("定位") or "")[:400],
            "url": first.get("链接") or "",
            "status": o.get("status") or "",
            "tier": o.get("溯源") or "",
            "path": o.get("path") or "",
        })
    rows.sort(key=lambda r: (r["subject"], r["errata_no"] or "999999", r["title"]))
    return rows


def render():
    rows = collect()
    buf = io.StringIO()
    # utf-8-sig：Excel 双击打开中文不乱码。BOM 只在这个字符串里，文件仍按 utf-8 写。
    w = csv.DictWriter(buf, fieldnames=[k for k, _v in FIELDS], lineterminator="\n")
    w.writeheader()
    for r in rows:
        w.writerow({k: r.get(v, "") for k, v in FIELDS})
    csv_text = "\ufeff" + buf.getvalue()
    by_subject = {}
    for r in rows:
        by_subject[r["subject"]] = by_subject.get(r["subject"], 0) + 1
    payload = {
        "$comment": "由 tools/export_errata.py 生成，**请勿手改**。"
                    "每条只主张「该书该处有这条勘误记录」，不主张当前版本仍然如此。",
        "schema_version": 1,
        "repo": "https://github.com/hpleapfrog/Scholia",
        "count": len(rows),
        "by_subject": by_subject,
        "columns": {k: v for k, v in FIELDS},
        "entries": rows,
    }
    return csv_text, json.dumps(payload, ensure_ascii=False, indent=1) + "\n", rows


def main():
    ap = argparse.ArgumentParser(description="导出全库勘误为 CSV / JSON")
    ap.add_argument("--check", action="store_true",
                    help="只比对，不写盘；不一致则退出码 1")
    args = ap.parse_args()

    csv_text, json_text, rows = render()
    if args.check:
        bad = []
        for p, want in ((CSV_PATH, csv_text), (JSON_PATH, json_text)):
            if not p.exists():
                bad.append(f"{p.relative_to(ROOT)}: 不存在")
            elif p.read_text(encoding="utf-8").replace("\r\n", "\n") != want:
                bad.append(f"{p.relative_to(ROOT)}: 与内容不一致（重跑不带 --check 的那条命令）")
        if bad:
            for b in bad:
                print(f"x {b}")
            return 1
        print(f"导出物与内容一致：{len(rows)} 条勘误")
        return 0

    OUT_DIR.mkdir(exist_ok=True)
    CSV_PATH.write_text(csv_text, encoding="utf-8", newline="")
    JSON_PATH.write_text(json_text, encoding="utf-8", newline="")
    print(f"已写 {CSV_PATH.relative_to(ROOT)} · {JSON_PATH.relative_to(ROOT)}"
          f"（{len(rows)} 条勘误）")
    counts = {}
    for r in rows:
        counts[r["subject"]] = counts.get(r["subject"], 0) + 1
    print("  " + " · ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
