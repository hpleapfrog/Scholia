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


# ── 改动登记：跑完一个样本就把被碰过的文件复原 ────────────────────────────
# 早先的做法是**每个样本整份复制仓库**。仓库涨到 700+ 对象之后，一次自测要复制三十多份、
# 跑三分多钟——慢到没人愿意在改规则时跑它，那它就会真的没人跑。
# 现在只复制一次，改动前登记原文、跑完复原。
_OBJ_CACHE = {}   # 副本路径 -> 该副本里所有知识对象的 (路径, 原文)
_BACKUP = {}      # 路径 -> 原始内容
_CREATED = []     # 新建出来的文件（复原时删掉）


def write(p, s):
    p = Path(p)
    key = str(p)
    if key not in _BACKUP:
        _BACKUP[key] = read(p) if p.exists() else None
    # **先写临时文件再 replace**，不要原地截断：
    # 副本是硬链接建出来的，原地 `open("w")` 会**改到原仓库那份文件**。
    # os.replace 只替换目录项，原文件的另一个名字不受影响。
    tmp = p.with_name(p.name + ".selftest.tmp")
    io.open(tmp, "w", encoding="utf-8", newline="").write(s)
    os.replace(str(tmp), str(p))


def remove(p):
    p = Path(p)
    key = str(p)
    if key not in _BACKUP:
        _BACKUP[key] = read(p) if p.exists() else None
    if p.exists():
        p.unlink()


def rename(p, new_name):
    """在**同一目录**下改名（内容不变）。"""
    p = Path(p)
    dst = p.parent / new_name
    if str(dst) not in _BACKUP:
        _BACKUP[str(dst)] = read(dst) if dst.exists() else None
    if dst.exists():
        dst.unlink()
    os.rename(str(p), str(dst))
    _CREATED.append(str(p))     # 原路径“消失”了，复原时要写回去


def move(p, dst):
    """把文件移到另一个路径（同目录改名或跨目录搬）。复原时两边都还原。"""
    p, dst = Path(p), Path(dst)
    if str(dst) not in _BACKUP:
        _BACKUP[str(dst)] = read(dst) if dst.exists() else None
    if str(p) not in _BACKUP:
        _BACKUP[str(p)] = read(p) if p.exists() else None
    os.replace(str(p), str(dst))


def restore():
    """把本轮样本碰过的文件全部复原。"""
    for path, content in list(_BACKUP.items()):
        p = Path(path)
        if content is None:
            p.unlink(missing_ok=True)
        else:
            tmp = p.with_name(p.name + ".selftest.tmp")
            io.open(tmp, "w", encoding="utf-8", newline="").write(content)
            os.replace(str(tmp), str(p))
    for path in _CREATED:
        Path(path).unlink(missing_ok=True)
    _BACKUP.clear()
    del _CREATED[:]


def _link_or_copy(src, dst):
    """用**硬链接**建副本；不支持时退回复制。

    为什么：仓库有 1500+ 个文件，Windows 上完整复制一次要 30 秒——
    自测从「几秒」变成了「几分钟」，那就没人愿意跑了。
    硬链接复制同一卷上是毫秒级。**代价是所有写入必须先 replace（见 write）**，
    否则会顺着链接改到原仓库。
    """
    try:
        os.link(src, dst)
    except OSError:
        shutil.copy2(src, dst)


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

    **结果缓存**：仓库有 1500+ 个 md，每个样本重扫一遍要 30 秒（Windows 上读文件慢）。
    样本是「挑目标 → 改动 → 复原」，所以扫一遍的结果在整个自测期间都有效。
    """
    key = str(root)
    if key in _OBJ_CACHE:
        return _OBJ_CACHE[key]
    out = []
    for p in sorted((root / "knowledge").rglob("*.md")):
        if p.name.endswith(".en.md"):
            continue
        t = read(p)
        if front_matter_of(t)[0] and field_of(t, "id"):
            out.append((p, t))
    _OBJ_CACHE[key] = out
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

def _paths(root):
    """所有路径条目（同样缓存：见 `_objects`）。"""
    key = "paths:" + str(root)
    if key in _OBJ_CACHE:
        return _OBJ_CACHE[key]
    out = []
    for p in sorted((root / "knowledge").rglob("paths/*.md")):
        if p.name.endswith(".en.md"):
            continue
        out.append((p, read(p)))
    _OBJ_CACHE[key] = out
    return out


def sample_graph01(root, _v):
    """给一条「命题」加上 先修 边（先修只能连知识点）。"""
    for p, t in _objects(root):
        if field_of(t, "type") != "命题":
            continue
        t2 = set_field(t, "先修", '["[x](x.md)"]')
        if t2:
            write(p, t2)
            return True
    return False


def sample_graph01_path_bad(root, _v):
    """`路径` 的外部先修指向**教法**（允许路径有先修，但目标仍必须是知识点）。"""
    for p, t in _paths(root):
        t2 = set_field(t, "先修", '["[x](../methods/x.md)"]')
        if t2:
            write(p, t2)
            return True
    return False


def sample_graph01_block_list(root, _v):
    """知识点用**多行块**写 `先修`，且第二项指向不存在的文件。

    这是 `fm_links` 的回归样本：早先行内匹配用了 ``\\s*``，会把块里的
    **第一条**当成行内值、把后面的项全部丢掉——检查看起来通过，其实是没读到。
    只放一条坏链接、且放在**第二条**，才测得出来。
    """
    for p, t in _objects(root):
        if field_of(t, "type") != "知识点":
            continue
        lines = read(p).split(chr(10))
        for i, line in enumerate(lines):
            if line.strip().startswith("先修:"):
                lines[i] = "  先修:"
                lines.insert(i + 1, '    - "[好](/dev/null)"')
                lines.insert(i + 2, '    - "[坏](不存在-zzz.md)"')
                break
        else:
            continue
        write(p, chr(10).join(lines))
        return True
    return False


def sample_graph01_cycle(root, _v):
    """两个知识点互相当对方的先修（成环）。"""
    concepts = [x for x in _objects(root) if field_of(x[1], "type") == "知识点"]
    same_dir = {}
    for p, t in concepts:
        same_dir.setdefault(str(p.parent), []).append((p, t))
    for group in same_dir.values():
        if len(group) < 2:
            continue
        (p1, t1), (p2, t2) = group[0], group[1]
        n1, n2 = p1.name, p2.name
        w1 = set_field(t1, "先修", '["[x](' + n2 + ')"]')
        w2 = set_field(t2, "先修", '["[x](' + n1 + ')"]')
        if w1 and w2:
            write(p1, w1)
            write(p2, w2)
            return True
    return False


def sample_graph02(root, _v):
    """`支持` 边指向存在的条目，但锚点在目标里不存在。"""
    concepts = [x for x in _objects(root) if field_of(x[1], "type") == "知识点"]
    if not concepts:
        return False
    target = concepts[0][0].name
    for p, t in _objects(root):
        if field_of(t, "type") != "命题" or p.parent.name == "attacks":
            continue
        rel = "../concepts/" + target
        t2 = set_field(t, "支持", '["[x](' + rel + '#zzz99)"]')
        if t2:
            write(p, t2)
            return True
    return False


def sample_graph03(root, _v):
    """把编排表里某个成果编号抹掉（成果无人覆盖）。"""
    for p, t in _paths(root):
        fm, body = front_matter_of(t)
        i = body.find(chr(10) + "## 编排")
        if i < 0:
            continue
        j = body.find(chr(10) + "## ", i + 1)
        seg = body[i:j if j > 0 else len(body)]
        if "o4" in seg:
            new = body[:i] + seg.replace("o4", "—") + (body[j:] if j > 0 else "")
            write(p, fm + new)
            return True
    return False


def sample_graph04(root, _v):
    """把编排表某一行的「条目」列换成 —（环节指不出对象）。"""
    NL = chr(10)
    for p, t in _paths(root):
        fm, body = front_matter_of(t)
        lines = body.split(NL)
        in_table = False
        for k, line in enumerate(lines):
            s = line.strip()
            if s.startswith("| #") or s.startswith("|  #"):
                in_table = True
                continue
            if in_table and s.startswith("|---"):
                continue
            if in_table and s.startswith("|"):
                cells = [c.strip() for c in s.strip("|").split("|")]
                if len(cells) >= 3 and "](" in cells[2]:
                    cells[2] = "—"
                    lines[k] = "| " + " | ".join(cells) + " |"
                    write(p, fm + NL.join(lines))
                    return True
            elif in_table and not s.startswith("|"):
                in_table = False
    return False


def sample_schema14(root, _v):
    """医学条目正文开头的 `> [!CAUTION]` 免责块被改坏。"""
    for p, t in _objects(root):
        if not (field_of(t, "学科") or "").startswith("医学"):
            continue
        if "> [!CAUTION]" not in t:
            continue
        write(p, t.replace("> [!CAUTION]", "> CAUTION", 1))
        return True
    return False


def sample_schema15(root, _v):
    """front-matter 的值以 `*` 开头且不加引号（严格 YAML 解析器会报错）。"""
    for p, t in _objects(root):
        t2 = set_field(t, "updated", "*2026-10-18")
        if t2:
            write(p, t2)
            return True
    return False


def sample_schema16(root, _v):
    """把一条「知识点」移到 `methods/`（目录与 type 不符）。"""
    for p, t in _objects(root):
        if p.parent.name != "concepts" or field_of(t, "type") != "知识点":
            continue
        dest_dir = p.parent.parent / "methods"
        if not dest_dir.is_dir() or (dest_dir / p.name).exists():
            continue
        move(p, dest_dir / p.name)
        return True
    return False


def sample_event01(root, _v):
    """事件的 `status` 写成「持续更新 / 已封存」以外的值。"""
    for p in sorted((root / "events").glob("*.md")):
        if p.name.startswith("README") or p.name.endswith(".en.md"):
            continue
        t2 = set_field(read(p), "status", "有效")
        if t2:
            write(p, t2)
            return True
    return False


def sample_biling01(root, _v):
    """把英译本改成不由 `id` 派生的文件名。"""
    for p in sorted((root / "knowledge").rglob("*.en.md")):
        if p.name.startswith("README"):
            continue
        t = read(p)
        if not front_matter_of(t)[0] or not field_of(t, "id"):
            continue
        dest = p.with_name(p.name.replace(".en.md", "-renamed.en.md"))
        if dest.exists():
            continue
        move(p, dest)
        return True
    return False


def sample_link03(root, _v):
    """英文页面里加一条指向中文原件（且有译本）的链接。"""
    zh = {}
    for p, t in _objects(root):
        oid = field_of(t, "id")
        if oid:
            zh[oid] = p
    for p in sorted((root / "knowledge").rglob("*.en.md")):
        if p.name.startswith("README"):
            continue
        t = read(p)
        oid = field_of(t, "id")
        if not oid or oid not in zh or zh[oid].parent != p.parent:
            continue
        t2 = insert_before_first_section(
            t, "[中文正本](./" + zh[oid].name + ")" + chr(10) + chr(10))
        if t2:
            write(p, t2)
            return True
    return False


def sample_evid02(root, _v):
    """证据表的「类别」写成非法值。"""
    p = root / "evidence" / "README.md"
    lines = read(p).split(chr(10))
    for k, line in enumerate(lines):
        if not re.match(r"\s*\|\s*ev-\d+\s*\|", line):
            continue
        cells = line.split("|")
        if len(cells) < 6 or "作废" in cells[2]:
            continue
        cells[2] = " ZZ "
        lines[k] = "|".join(cells)
        write(p, chr(10).join(lines))
        return True
    return False


def sample_evid03(root, _v):
    """把某条 `暂定确认` 所引唯一证据的核验深度改成「未核验」。"""
    for p, t in _objects(root):
        if field_of(t, "status") != "暂定确认":
            continue
        ids = re.findall(r"ev-\d+", front_matter_of(t)[0])
        if len(ids) != 1:
            continue
        ep = root / "evidence" / "README.md"
        lines = read(ep).split(chr(10))
        for k, line in enumerate(lines):
            if not re.match(r"\s*\|\s*" + re.escape(ids[0]) + r"\s*\|", line):
                continue
            cells = line.split("|")
            if len(cells) < 6 or "作废" in cells[2]:
                continue
            cells[4] = " 未核验 "
            lines[k] = "|".join(cells)
            write(ep, chr(10).join(lines))
            return True
        return False
    return False


def sample_index01(root, _v):
    """把 `citations.json` 改坏（手改了机器文件）。"""
    p = root / "citations.json"
    if not p.exists():
        return False
    write(p, "{}\n")
    return True


def sample_index02(root, _v):
    """往 README 的生成块里塞一行（数字/清单过期）。"""
    p = root / "README.md"
    t = read(p)
    marker = "<!-- kbcheck:begin -->"
    if marker not in t:
        return False
    write(p, t.replace(marker, marker + chr(10) + "注入样本", 1))
    return True


def sample_readme01(root, _v):
    """把一条对象从它的学科 README 里删掉。"""
    for p, t in _objects(root):
        rel = p.relative_to(root)
        if rel.parts[0] != "knowledge":
            continue
        rp = root / rel.parts[0] / rel.parts[1] / "README.md"
        if not rp.exists():
            continue
        txt = read(rp)
        if p.name not in txt:
            continue
        write(rp, txt.replace(p.name, "ZZZ.md"))
        return True
    return False


def sample_readme03(root, _v):
    """把学科 README 路径表里手写的「覆盖度 X/Y」改大一位。"""
    import re as _re
    # 只看**学科** README（knowledge/<subject>/README.md）
    # —— `knowledge/README.md` 是总索引，那里也有「覆盖度」字样，但不受这条规则管
    for rp in sorted((root / "knowledge").glob("*/README.md")):
        lines = read(rp).split(chr(10))
        for i, line in enumerate(lines):
            # 必须是**路径表**里的那一行：既提到 paths/ 又有覆盖度数字
            if "覆盖度" not in line or "paths/" not in line:
                continue
            m = _re.search(r"覆盖度\s*\*{0,2}(\d+)\s*/\s*(\d+)", line)
            if not m:
                continue
            lines[i] = line.replace(m.group(0), "覆盖度 %s/%s" % (
                int(m.group(1)) + 9, m.group(2)), 1)
            write(rp, chr(10).join(lines))
            return True
    return False


def sample_doc01(root, _v):
    """FORMAT.md 的状态图例里删掉一个状态词。"""
    p = root / "FORMAT.md"
    t = read(p)
    if "已失效" not in t:
        return False
    write(p, t.replace("已失效", "已退役"))
    return True


# ── 2026-10-20 新增：状态可达性 / 支持边同源 / 覆盖强度 ──────────────────────

def _claims_with_argument(root):
    """带论证 ID 的命题（用来当 `支持` 边的靶）。攻击条目跳过。"""
    for p in sorted((root / "knowledge").rglob("claims/*.md")):
        if p.name.endswith(".en.md") or "attacks" in p.parts:
            continue
        fm, body = front_matter_of(read(p))
        if kv(fm, "type") != "命题":
            continue
        m = re.search(r"(?m)^### ([A-Z]+)(\d+)", body)
        if m:
            yield p, fm, body, (m.group(1) + m.group(2)).lower(), \
                len(re.findall(r"(?m)^### [A-Z]+\d+", body))


def sample_schema19_confirmed(root, _v):
    """命题直接写「已确证」——全条只有作者一个人的署名。"""
    for p, fm, body, _a, _n in _claims_with_argument(root):
        if kv(fm, "status") == "已确证":
            continue
        names = set(re.findall(r"@([\w][\w.\-]*)", fm + body))
        if len(names) > 1:
            continue
        write(p, re.sub(r"(?m)^status:.*$", "status: 已确证", fm, count=1) + body)
        return True
    return False


def sample_schema19_disputed(root, _v):
    """只有一条论证的命题直接写「争议」——图上没有任何冲突可言。"""
    for p, fm, body, _a, n in _claims_with_argument(root):
        if n >= 2 or kv(fm, "status") == "争议":
            continue
        write(p, re.sub(r"(?m)^status:.*$", "status: 争议", fm, count=1) + body)
        return True
    return False


def sample_schema19_overturned(root, _v):
    """命题写「已推翻」，但没有任何一条 `攻击` 边指着它。"""
    for p, fm, body, _a, n in _claims_with_argument(root):
        if n < 1 or kv(fm, "status") == "已推翻":
            continue
        write(p, re.sub(r"(?m)^status:.*$", "status: 已推翻", fm, count=1) + body)
        return True
    return False


def sample_graph06(root, _v):
    """两条 `支持` 边指向同一个论证，两个支持者引的是**同一份证据**。"""
    target = None
    for p, fm, body, anchor, _n in _claims_with_argument(root):
        target = (p, anchor)
        break
    if not target:
        return False
    by_ev = {}
    for p in sorted((root / "knowledge").rglob("*.md")):
        if p.name.endswith(".en.md") or p == target[0]:
            continue
        fm, body = front_matter_of(read(p))
        ev = kv(fm, "evidence") or ""
        if len(re.findall(r"ev-\d+", ev)) != 1:
            continue
        if not re.search(r"(?m)^\s*支持: \[\]\s*$", fm):
            continue
        by_ev.setdefault(ev, []).append((p, fm, body))
    pair = next((v for v in by_ev.values() if len(v) >= 2), None)
    if not pair:
        return False
    n = 0
    for p, fm, body in pair[:2]:
        rel = os.path.relpath(str(target[0]), str(p.parent)).replace("\\", "/")
        new = re.sub(r"(?m)^(\s*支持): \[\]\s*$",
                     rf'\1: ["[命题：注入样本]({rel}#{target[1]})"]', fm, count=1)
        if new != fm:
            write(p, new + body)
            n += 1
    return n == 2


def sample_graph07(root, _v):
    """把某个成果**唯一**覆盖条目所依据的证据，核验深度从 `全文` 改成 `仅定位`。

    只挑「全路径里只出现一次」的成果：这样这条成果的依据就是这一条证据，
    改完之后「覆盖到了，但依据没读过」才成立。
    """
    ep = root / "evidence" / "README.md"
    for p, t in _paths(root):
        _fm, body = front_matter_of(t)
        i = body.find(chr(10) + "## 编排")
        if i < 0:
            continue
        j = body.find(chr(10) + "## ", i + 1)
        seg = body[i:j if j > 0 else len(body)]
        rows = [r for r in seg.splitlines() if r.strip().startswith("|")]
        seen = {}
        for r in rows:
            cells = [c.strip() for c in r.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            # 与 kbcheck 同一处置：**不按列位取「覆盖」**。这个样本自己要是只扫末列，
            # 碰上 `# | 环节 | 条目 | 覆盖 | 时长` 就挑不出成果，然后**静默 SKIP**——
            # 而 SKIP 看起来像「样本没找到可用数据」，实际是样本读不懂输入。
            for oid in re.findall(r"\b(o\d+)\b", " ".join(cells)):
                seen.setdefault(oid, []).append(r)
        single = [oid for oid, v in seen.items() if len(v) == 1]
        for oid in single:
            r = seen[oid][0]
            link = None
            for c in r.strip().strip("|").split("|"):
                mm = re.search(r"\[[^\]]*\]\(([^)#]+)", c)
                if mm:
                    link = mm.group(1)
            if not link:
                continue
            obj = (p.parent / link).resolve()
            if not obj.exists():
                continue
            ofm, _ob = front_matter_of(read(obj))
            ids = re.findall(r"ev-\d+", kv(ofm, "evidence") or "")
            if len(ids) != 1:
                continue
            lines = read(ep).splitlines(True)
            hit = False
            for k, line in enumerate(lines):
                if line.strip().startswith(f"| {ids[0]} |") and "| 全文 |" in line:
                    cells = line.strip().strip("|").split("|")
                    cells[3] = " 仅定位 "
                    lines[k] = "| " + " | ".join(c.strip() for c in cells) + " |\n"
                    hit = True
            if hit:
                write(ep, "".join(lines))
                return True
    return False


def sample_graph07b(root, _v):
    """把「覆盖」列**挤出末列**，看 R-GRAPH-07 还认不认得出这条路径的单环节覆盖。

    这是一条**回归样本**，不是新的失败模式。2026-10-20 的第一版实现按列位取值
    （只扫 `cells[-1]`），碰上 `运动学入门-BL` 那种
    `# | 环节 | 条目 | 覆盖 | 时长` 的表，就把整条路径读成「没有单环节覆盖」——
    **假干净**。`sample_graph07` 改的是证据深度，列位解析错成什么样它都照样 PASS，
    所以这里补一条专门盯**输入形状**的样本。

    做法：找一条「覆盖」确实在末列的路径，给整张表追加一列（备注），
    并插入一个只被**一个新环节**覆盖的成果 `o9`。
    列位解析的实现会**悄悄不再报这条路径**（`o9` 在输出里根本不出现）；
    扫全部单元格的实现会在 thin 列表末尾报出它——所以断言写的是 `'o9']`
    而不是裸 `o9`：要的是「它出现在单环节覆盖列表的末尾」，
    不是「输出里某处恰好有这两个字符」。
    """
    for p, t in _paths(root):
        fm, body = front_matter_of(t)
        m = re.search(r"(?m)^outcomes:[ \t]*\n((?:[ \t]+.*\n?)+)", fm)
        if not m:
            continue
        decl = re.findall(r"\b(o\d+)\b", m.group(1))
        # 注入点必须还不存在，否则「o9 出现了」证明不了任何事
        if not decl or "o9" in decl:
            continue
        i = body.find(chr(10) + "## 编排")
        if i < 0:
            continue
        k = body.find(chr(10) + "## ", i + 1)
        k = k if k > 0 else len(body)
        pre, seg, post = body[:i + 1], body[i + 1:k], body[k:]
        lines = seg.splitlines(True)
        rows = [n for n, r in enumerate(lines) if r.strip().startswith("|")]
        if len(rows) < 3:
            continue
        data = [n for n in rows if re.match(r"\|\s*\d+\s*\|", lines[n].strip())]
        # 前提：表是「4 列 + 覆盖在末列」。形状一旦变了，这条样本就该大声 SKIP
        ok = True
        for n in data:
            cells = [c.strip() for c in lines[n].strip().strip("|").split("|")]
            if len(cells) != 4 or not re.fullmatch(r"o\d+(?:, ?o\d+)*", cells[-1]):
                ok = False
                break
        if not ok or not data:
            continue
        link = None
        for n in data:
            mm = re.search(r"\[[^\]]*\]\(([^)]+)\)", lines[n])
            if mm:
                link = mm.group(1)
        if not link:
            continue
        out = list(lines)
        for idx, n in enumerate(rows):
            s = out[n].rstrip("\n").rstrip()
            out[n] = (s + " 备注 |\n" if idx == 0 else
                      s + " --- |\n" if idx == 1 else s + "  |\n")
        out.insert(data[-1] + 1,
                   f"| {len(data) + 1} | 注入环节（自测样本） | [注入]({link}) | o9 |  |\n")
        fm_lines = fm.splitlines(True)
        last_o = max(n for n, r in enumerate(fm_lines) if re.match(r"^\s+- o\d", r))
        if not fm_lines[last_o].endswith("\n"):
            fm_lines[last_o] += "\n"
        fm_lines.insert(last_o + 1, "  - o9: 注入成果（自测样本，非真实条目内容）\n")
        write(p, "".join(fm_lines) + pre + "".join(out) + post)
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
    ("R-GRAPH-01", "命题加了 先修 边", sample_graph01),
    ("R-GRAPH-01", "两个知识点互为先修（成环）", sample_graph01_cycle),
    ("R-GRAPH-01", "路径的外部先修指向教法", sample_graph01_path_bad),
    ("R-GRAPH-01", "多行块先修里的第二条是坏链接", sample_graph01_block_list),
    ("R-GRAPH-02", "支持边锚点在目标里不存在", sample_graph02),
    ("R-GRAPH-03", "路径的某个成果无人覆盖", sample_graph03),
    ("R-GRAPH-04", "路径某环节指不出对象", sample_graph04),
    ("R-SCHEMA-14", "医学条目的 [!CAUTION] 免责块被改坏", sample_schema14),
    ("R-SCHEMA-15", "front-matter 值以 * 开头不加引号", sample_schema15),
    ("R-SCHEMA-16", "知识点被移出 concepts/（目录与 type 不符）", sample_schema16),
    ("R-EVENT-01", "事件 status 写成非法值", sample_event01),
    ("R-BILING-01", "英译本文件名不由 id 派生（改名）", sample_biling01),
    ("R-LINK-03", "英文页面加了一条指向中文页的链接", sample_link03),
    ("R-EVID-02", "证据表「类别」写成 ZZ", sample_evid02),
    ("R-EVID-03", "暂定确认的唯一证据核验深度改成未核验", sample_evid03),
    ("R-INDEX-01", "citations.json 被改坏", sample_index01),
    ("R-INDEX-02", "README 生成块被塞进一行", sample_index02),
    ("R-README-01", "对象从学科 README 里被删掉", sample_readme01),
    ("R-README-03", "README 里的覆盖度数字被改大", sample_readme03),
    ("R-README-03", "README 里的覆盖度数字被改大", sample_readme03),
    ("R-DOC-01", "FORMAT.md 状态图例删掉「已失效」", sample_doc01),
    ("R-SCHEMA-19", "命题一个人署名就写「已确证」", sample_schema19_confirmed, "但全条只有"),
    ("R-SCHEMA-19", "只有一条论证、零攻击边就写「争议」", sample_schema19_disputed, "status=「争议」"),
    ("R-SCHEMA-19", "没有未被击倒的攻击就写「已推翻」", sample_schema19_overturned, "status=「已推翻」"),
    ("R-GRAPH-06", "两条支持边引的是同一份证据", sample_graph06, "但证据并集只有"),
    ("R-GRAPH-07", "成果唯一覆盖条目的证据被改成未读", sample_graph07, "证据最高只到"),
    ("R-GRAPH-07", "把「覆盖」列挤出末列后仍要报出单环节覆盖", sample_graph07b, "'o9']"),
]


def run_check(root):
    # 子进程强制 UTF-8：Windows 控制台默认 GBK，管道输出会让上层按 UTF-8 解码失败
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    r = subprocess.run([sys.executable, str(root / "tools" / "kbcheck.py")],
                       cwd=str(root), capture_output=True, text=True,
                       encoding="utf-8", env=env)
    return (r.stdout or "") + (r.stderr or "")


def _mktemp():
    """临时副本放在**与仓库同一个卷**上。

    这不是洁癖：硬链接不能跨盘，默认临时目录在 C: 而仓库在 D: 时会**静默退回复制**，
    1500 个文件 30 秒——自测从几秒变成几分钟，然后就没人跑了。
    """
    for base in (str(ROOT.parent), None):
        try:
            return tempfile.mkdtemp(prefix="scholia_selftest_", dir=base)
        except OSError:
            continue
    return tempfile.mkdtemp(prefix="scholia_selftest_")


def _mktemp():
    """临时副本放在**与仓库同一个卷**上。

    这不是洁癖：硬链接不能跨盘，默认临时目录在 C: 而仓库在 D: 时会**静默退回复制**，
    1500 个文件 30 秒——自测从几秒变成几分钟，然后就没人跑了。
    """
    for base in (str(ROOT.parent), None):
        try:
            return tempfile.mkdtemp(prefix="scholia_selftest_", dir=base)
        except OSError:
            continue
    return tempfile.mkdtemp(prefix="scholia_selftest_")


def main():
    # 同一条（规则, 描述）只跑一次：重复登记不会报错，只会白跑一遍——
    # 而重复往往是「把一行粘了两次」，正是这类机械操作最容易出的错。
    seen_pairs, samples = set(), []
    for s in SAMPLES:
        k = (s[0], s[1])
        if k in seen_pairs:
            continue
        seen_pairs.add(k)
        samples.append(s)
    # `--only R-GRAPH`：只跑某条（或某个前缀）规则的样本。
    # 全量跑一次约 1~2 分钟（每个样本都要整跑一次 kbcheck），
    # 而改一条规则时只需要看那一条——**让常用路径变短**比让全量变快更值。
    if "--only" in sys.argv:
        prefix = sys.argv[sys.argv.index("--only") + 1]
        samples = [s for s in samples if s[0].startswith(prefix)]
        if not samples:
            print(f"没有以 {prefix!r} 开头的规则样本")
            return 1

    # 复制一次、样本间复原（并发跑过一版，实测没用：瓶颈在复制，不在算）。
    tmp = _mktemp()
    repo = Path(tmp) / "repo"
    failures = []
    try:
        shutil.copytree(str(ROOT), str(repo),
                        ignore=shutil.ignore_patterns(".git", "__pycache__"),
                        copy_function=_link_or_copy)
        for idx, entry in enumerate(samples):
            rule, desc, fn = entry[:3]
            # 第 4 项（可选）：这条样本要在那份输出里**确实看到**的话。
            # 有的规则在**未注入的仓库里**就已经报别的数据（例如 R-GRAPH-07 的
            # 「单环节覆盖」分支）——只 grep 规则 ID 会**假装通过**。写死要看到的句子，
            # 才证明**这一支**在查。
            expect = entry[3] if len(entry) > 3 else rule
            try:
                if not fn(repo, VERBOSE):
                    print(f"SKIP  {rule}  {desc}  ← 没找到可用样本，自测失去覆盖")
                    failures.append((rule, "no-sample"))
                    continue
                out = run_check(repo)
                if expect in out:
                    print(f"PASS  {rule}  {desc}")
                else:
                    print(f"FAIL  {rule}  {desc}  ← 注入后没报这条规则")
                    failures.append((rule, "not-detected"))
            finally:
                restore()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    total = len(samples)
    rules = {e[0] for e in samples}
    print(f"\n{total - len(failures)}/{total} 个样本成功触发（覆盖 {len(rules)} 条规则）")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
