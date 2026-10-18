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


def sample_biling03(root, _v):
    """删掉一份文档的英译本。"""
    for rel in ("knowledge/README.en.md", "AGENTS.en.md", "evidence/README.en.md"):
        p = root / rel
        if p.exists():
            p.unlink()
            return True
    return False


def _objects(root):
    """所有中文知识对象（front-matter 里有 id 的 .md）。

    这里刻意**不用正则**：本仓库的写文件通道会把反斜杠转义吃掉（反斜杠加 s 会变成斜杠加 s），
    所以下面一律用「按行切」的字符串操作，不写任何反斜杠转义。
    """
    out = []
    for p in sorted((root / "knowledge").rglob("*.md")):
        if p.name.endswith(".en.md"):
            continue
        t = read(p)
        if front_matter_of(t)[0] and field_of(t, "id"):
            out.append((p, t))
    return out


def field_of(text, key):
    """取 front-matter 顶层字段的值（按行找，不经正则）。"""
    fm = front_matter_of(text)[0]
    for line in fm.split(chr(10)):
        s = line.strip()
        if s.startswith(key + ":"):
            return s[len(key) + 1:].strip().strip('"')
    return None


def set_field(text, key, value):
    """把 front-matter 里某个字段的值换掉；找不到就返回 None。"""
    fm, body = front_matter_of(text)
    out, done = [], False
    for line in fm.split(chr(10)):
        s = line.strip()
        if not done and s.startswith(key + ":"):
            indent = line[:len(line) - len(line.lstrip())]
            out.append(indent + key + ": " + value)
            done = True
        else:
            out.append(line)
    return (chr(10).join(out) + body) if done else None


def drop_field(text, key):
    """删掉 front-matter 里某个字段；找不到就返回 None。"""
    fm, body = front_matter_of(text)
    out, done = [], False
    for line in fm.split(chr(10)):
        if not done and line.strip().startswith(key + ":"):
            done = True
            continue
        out.append(line)
    return (chr(10).join(out) + body) if done else None


def insert_before_first_section(text, snippet):
    fm, body = front_matter_of(text)
    i = body.find(chr(10) + "## ")
    if i < 0:
        return None
    return fm + body[:i + 1] + snippet + chr(10) + body[i + 1:]


def sample_schema01(root, _v):
    """删掉一个必填字段（license）。"""
    for p, t in _objects(root):
        t2 = drop_field(t, "license")
        if t2:
            write(p, t2)
            return True
    return False


def sample_schema03(root, _v):
    """把最后一条的 id 改成第一条的 id（撞 id）。"""
    objs = _objects(root)
    if len(objs) < 2:
        return False
    first_id = field_of(objs[0][1], "id")
    p, t = objs[-1]
    t2 = set_field(t, "id", first_id)
    if not t2:
        return False
    write(p, t2)
    return True


def sample_schema04(root, _v):
    """`evidence: []`。"""
    for p, t in _objects(root):
        t2 = set_field(t, "evidence", "[]")
        if t2:
            write(p, t2)
            return True
    return False


def sample_schema05(root, _v):
    """把「## 变更记录」改成「## 变更记录X」——**带后缀的同名小节不算存在**。

    这是校验器曾经的弱点：按子串找小节，改名后子串还在，于是检查通过。
    现在改成整行匹配，这个样本才真的能失败；保留它就是为了防这条退回去。
    """
    for p, t in _objects(root):
        t2 = t.replace(chr(10) + "## 变更记录", chr(10) + "## 变更记录X", 1)
        if t2 != t:
            write(p, t2)
            return True
    return False


def sample_schema06(root, _v):
    """把知识点的 `> [!TIP]` 改坏。"""
    for p, t in _objects(root):
        if field_of(t, "type") == "知识点" and "> [!TIP]" in t:
            write(p, t.replace("> [!TIP]", "> TIP", 1))
            return True
    return False


def sample_schema07(root, _v):
    """学段写成非法值。"""
    for p, t in _objects(root):
        t2 = set_field(t, "学段", "幼儿园")
        if t2:
            write(p, t2)
            return True
    return False


def sample_schema08(root, _v):
    """created 写成斜杠日期。"""
    for p, t in _objects(root):
        t2 = set_field(t, "created", "2026/10/18")
        if t2:
            write(p, t2)
            return True
    return False


def sample_evid01(root, _v):
    """evidence 指向不存在的编号。"""
    for p, t in _objects(root):
        t2 = set_field(t, "evidence", "[ev-999]")
        if t2:
            write(p, t2)
            return True
    return False


def sample_link01(root, _v):
    """正文加一条指向不存在文件的链接。"""
    for p, t in _objects(root):
        t2 = insert_before_first_section(t, "[坏链](does-not-exist-zzz.md)" + chr(10) + chr(10))
        if t2:
            write(p, t2)
            return True
    return False


def sample_link02(root, _v):
    """正文加一条目标存在、锚点不存在的链接。"""
    for p, t in _objects(root):
        t2 = insert_before_first_section(t, "[坏锚点](../README.md#nope-zzz)" + chr(10) + chr(10))
        if t2:
            write(p, t2)
            return True
    return False

def sample_schema02(root, _v):
    """status 写成不受 type 约束的值。"""
    for p, t in _objects(root):
        if field_of(t, "type") == "知识点" and field_of(t, "status") == "有效":
            write(p, set_field(t, "status", "已确证"))
            return True
    return False


def sample_schema09(root, _v):
    """author 写成没有 @ 的名字。"""
    for p, t in _objects(root):
        t2 = set_field(t, "author", "张三")
        if t2:
            write(p, t2)
            return True
    return False


def sample_schema10(root, _v):
    """license 写成 MIT。"""
    for p, t in _objects(root):
        t2 = set_field(t, "license", "MIT")
        if t2:
            write(p, t2)
            return True
    return False


def sample_schema11(root, _v):
    """id 前缀换成别的学科的 slug。"""
    for p, t in _objects(root):
        i = field_of(t, "id") or ""
        if i.count(":") >= 2:
            t2 = set_field(t, "id", "kb:wrong:" + i.split(":")[-1])
            if t2:
                write(p, t2)
                return True
    return False


def sample_schema12(root, _v):
    """教法的 knowledge_point 指到命题上。"""
    for p, t in _objects(root):
        if field_of(t, "type") != "教法":
            continue
        fm, body = front_matter_of(t)
        out, done = [], False
        for line in fm.split(chr(10)):
            if not done and line.strip().startswith("knowledge_point:"):
                out.append("knowledge_point: [\"../claims/" + "x" + ".md\"]".replace(
                    chr(92) + '"', '"'))
                done = True
            else:
                out.append(line)
        if done:
            write(p, chr(10).join(out) + body)
            return True
    return False


def sample_schema13(root, _v):
    """教法的 `水平档` 写成无法识别的值。"""
    for p, t in _objects(root):
        if field_of(t, "type") != "教法":
            continue
        t2 = set_field(t, "水平档", "ZZ")
        if t2:
            write(p, t2)
            return True
    return False


SAMPLES = [
    ("R-SCHEMA-17", "命题写「暂定确认」但 ## 论证 为空", sample_schema17),
    ("R-SCHEMA-18", "「变更记录」里有比 updated 更晚的日期", sample_schema18),
    ("R-BILING-02", "英译本的 status 与中文原件不一致", sample_biling02),
    ("R-GRAPH-05", "攻击条目没有 攻击 边", sample_graph05),
    ("R-README-02", "学科 README 状态列与 front-matter 不一致", sample_readme02),
    ("R-EVID-04", "正文引用了不存在的证据编号", sample_evid04),
    ("R-BILING-03", "文档缺英译本（删掉 knowledge/README.en.md）", sample_biling03),
    ("R-SCHEMA-01", "front-matter 删掉必填字段 license", sample_schema01),
    ("R-SCHEMA-03", "两条对象撞同一个 id", sample_schema03),
    ("R-SCHEMA-04", "evidence 写成空数组", sample_schema04),
    ("R-SCHEMA-05", "必备小节标题被改坏", sample_schema05),
    ("R-SCHEMA-06", "知识点首行的 [!TIP] 被改坏", sample_schema06),
    ("R-SCHEMA-07", "学段写成「幼儿园」", sample_schema07),
    ("R-SCHEMA-08", "created 写成 2026/10/18", sample_schema08),
    ("R-EVID-01", "evidence 指向 ev-999", sample_evid01),
    ("R-LINK-01", "正文加了指向不存在文件的链接", sample_link01),
    ("R-LINK-02", "链接目标存在但锚点不存在", sample_link02),
    ("R-SCHEMA-02", "知识点写成「已确证」", sample_schema02),
    ("R-SCHEMA-09", "author 写成「张三」", sample_schema09),
    ("R-SCHEMA-10", "license 写成 MIT", sample_schema10),
    ("R-SCHEMA-11", "id 前缀换成别的学科", sample_schema11),
    ("R-SCHEMA-12", "教法的 knowledge_point 指向不存在的文件", sample_schema12),
    ("R-SCHEMA-13", "教法的水平档写成 ZZ", sample_schema13),
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
