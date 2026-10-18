#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""规则自测：每条机械规则配一个**会失败**的注入样本。

为什么要有这个文件
------------------
`docs/RULES.md` 说某条规则「机械校验」，但**「规则表里写了」和「代码真的在查」是两件事**。
2026-10-18 的一次审计发现：六条本该被拦的情形（状态与论证不一致、译文与原文状态不同步、
孤儿攻击、README 状态列漂移、正文引用不存在的证据、`updated` 与变更记录不符）
**全部能通过校验**——规则表上它们看起来都是"已强制"。

所以：**每条规则都带一个会失败的样本**，在**临时副本**里注入、跑校验、断言那条规则确实报错。
不污染仓库（CONTRIBUTING 的「新规则入库门槛」第 1 条）。

用法
----
    python tools/verify_rules.py            # 全部跑一遍，0 = 全过
    python tools/verify_rules.py -v         # 打印每步细节

样本的**目标文件是动态挑的**（不写死路径）：条目改名、增删都不会让自测静默失效。
"""
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERBOSE = "-v" in sys.argv


def read(p):
    return io.open(p, encoding="utf-8").read()


def write(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)


def front_matter_of(text):
    """返回 (fm, body)。front-matter 与正文要分开改——正文里常有 YAML 示例。"""
    if not text.startswith("---"):
        return "", text
    end = text.index("\n---", 3)
    return text[:end], text[end:]


def kv(fm, key):
    m = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.+)$", fm)
    return m.group(1).strip().strip('"') if m else None


# ── 样本定义：每个返回 False 表示"前提不成立，跳过" ───────────────────────────

def sample_schema17(root, _v):
    """命题写「暂定确认」，但 ## 论证 被掏空。"""
    for p in sorted((root / "knowledge").rglob("*.md")):
        if p.name.endswith(".en.md") or "attacks" in p.parts:
            continue
        t = read(p)
        fm, body = front_matter_of(t)
        if kv(fm, "type") != "命题" or "## 论证" not in body or "## 变更记录" not in body:
            continue
        if not re.search(r"(?m)^### [A-Z]+\d+", body):
            continue
        i, j = body.index("## 论证"), body.index("## 变更记录")
        fm2 = re.sub(r"(?m)^status:.*$", "status: 暂定确认", fm, count=1)
        write(p, fm2 + body[:i] + "## 论证\n\n（尚无论证）\n\n" + body[j:])
        return True
    return False


def sample_schema18(root, _v):
    """「变更记录」里出现一个比 `updated` 更晚的日期。"""
    for p in sorted((root / "knowledge").rglob("*.md")):
        if p.name.endswith(".en.md"):
            continue
        t = read(p)
        fm, body = front_matter_of(t)
        upd = kv(fm, "updated")
        if not upd or "## 变更记录" not in body:
            continue
        newer = "2099-01-01"
        i = body.index("## 变更记录")
        body2 = body[:i] + body[i:].replace("\n|", f"\n| {newer} | 注入样本 | 自测 | 自测 |\n|", 1)
        if body2 == body:
            continue
        write(p, fm + body2)
        return True
    return False


def sample_biling02(root, _v):
    """英译本的 status 与中文原件不一致。"""
    for p in sorted((root / "knowledge").rglob("*.en.md")):
        t = read(p)
        fm, body = front_matter_of(t)
        st = kv(fm, "status")
        if not st:
            continue
        new = "有效" if st != "有效" else "待审"
        write(p, re.sub(r"(?m)^status:.*$", f"status: {new}", fm, count=1) + body)
        return True
    return False


def sample_graph05(root, _v):
    """攻击条目把自己的 攻击 边清空（孤儿攻击）。"""
    for p in sorted((root / "knowledge").rglob("attacks/*.md")):
        if p.name.endswith(".en.md"):
            continue
        fm, body = front_matter_of(read(p))
        # 只改 front-matter，且锚到「行尾的 ]」——链接文本里也有 ]，非贪婪会提前截断
        fm2 = re.sub(r"(?m)^  攻击: \[[\s\S]*?\]\s*$", "  攻击: []", fm, count=1)
        if fm2 == fm:
            continue
        write(p, fm2 + body)
        return True
    return False


def sample_readme02(root, _v):
    """学科 README 的状态列与 front-matter 不一致。"""
    for rp in sorted((root / "knowledge").glob("*/README.md")):
        lines = read(rp).split("\n")
        for k, line in enumerate(lines):
            if not line.startswith("|") or "](" not in line:
                continue
            m = re.search(r"\]\(([^)#]+)", line)
            if not m:
                continue
            target = (rp.parent / m.group(1)).resolve()
            if not target.exists():
                continue
            fm, _ = front_matter_of(read(target))
            real = kv(fm, "status")
            if not real:
                continue
            fake = "已确证" if real != "已确证" else "草案"
            # 把这一行里出现的中文状态名换成另一个合法状态名
            new_line = re.sub(r"(?<![\w])(草案|待审|有效|争议|暂定确认|已确证|需复审|失据|已推翻|已失效)(?![\w])",
                              fake, line, count=1)
            if new_line == line:
                continue
            lines[k] = new_line
            write(rp, "\n".join(lines))
            return True
    return False


def sample_evid04(root, _v):
    """正文引用一个不存在的证据编号。"""
    for p in sorted((root / "knowledge").rglob("*.md")):
        if p.name.endswith(".en.md"):
            continue
        fm, body = front_matter_of(read(p))
        # 必须是**知识对象**：README 与索引页没有 front-matter id，规则本来就不适用
        # （Windows 与 Linux 的 Path 排序不同，靠 sorted 取第一个文件会挑到不同的文件）
        if not kv(fm, "id") or not kv(fm, "type"):
            continue
        if "## " not in body:
            continue
        i = body.index("## ")
        write(p, fm + body[:i] + "\n（另见 ev-999。）\n\n" + body[i:])
        return True
    return False


SAMPLES = [
    ("R-SCHEMA-17", "命题写「暂定确认」但 ## 论证 为空", sample_schema17),
    ("R-SCHEMA-18", "「变更记录」里有比 updated 更晚的日期", sample_schema18),
    ("R-BILING-02", "英译本的 status 与中文原件不一致", sample_biling02),
    ("R-GRAPH-05", "攻击条目没有 攻击 边", sample_graph05),
    ("R-README-02", "学科 README 状态列与 front-matter 不一致", sample_readme02),
    ("R-EVID-04", "正文引用了不存在的证据编号", sample_evid04),
]


def run_check(root):
    r = subprocess.run([sys.executable, str(root / "tools" / "kbcheck.py")],
                       cwd=str(root), capture_output=True, text=True, encoding="utf-8")
    return (r.stdout or "") + (r.stderr or "")


def main():
    failures = []
    for rule, desc, fn in SAMPLES:
        tmp = tempfile.mkdtemp(prefix="scholia_selftest_")
        repo = Path(tmp) / "repo"
        try:
            shutil.copytree(str(ROOT), str(repo),
                            ignore=shutil.ignore_patterns(".git", "__pycache__"))
            if not fn(repo, VERBOSE):
                print(f"SKIP  {rule}  {desc}  ← 没找到可用样本，自测失去覆盖")
                failures.append((rule, "no-sample"))
                continue
            out = run_check(repo)
            if rule in out:
                print(f"PASS  {rule}  {desc}")
            else:
                print(f"FAIL  {rule}  {desc}  ← 注入后没报这条规则")
                failures.append((rule, "not-detected"))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    total = len(SAMPLES)
    print(f"\n{total - len(failures)}/{total} 条规则被注入样本成功触发")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
