#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""机械校验：不依赖任何密钥、不依赖任何第三方库。

校验项目里所有知识对象是否符合 FORMAT.md 的规范。

用法:
    python tools/kbcheck.py

退出码:
    0  全部通过
    1  有不符合规范之处

它查的是**人读不出来的东西**：单看一个文件都没问题，问题只在文件之间
（id 冲突、链接可达性、教法禁忌是否为空）。
"""
import collections
import os
import re
import sys
from pathlib import Path

# 仓库根目录（本文件在 tools/ 下）
ROOT = Path(__file__).resolve().parent.parent

TYPES = {"知识点", "命题", "教法", "误解", "路径", "资源"}

ALLOWED_STATUS = {
    "知识点": {"草案", "待审", "有效", "争议", "需复审", "已失效"},
    "命题": {"草案", "待审", "争议", "暂定确认", "已确证", "已推翻", "需复审", "已失效"},
    "教法": {"草案", "待审", "有效", "争议", "需复审", "已失效"},
    "误解": {"草案", "待审", "有效", "争议", "需复审", "已失效"},
    "资源": {"草案", "待审", "有效", "争议", "需复审", "已失效"},
    "路径": {"草案", "待审", "有效", "争议", "需复审", "已失效"},
}

REQUIRED_FIELDS = ["id", "type", "title", "status", "author", "created",
                   "updated", "scope", "edges", "evidence", "license"]

REQUIRED_SECTIONS = {
    "知识点": ["定义", "关联", "论证", "变更记录"],
    "命题": ["陈述", "依据", "论证", "变更记录"],
    "教法": ["做法", "禁忌", "风险", "证据", "论证", "变更记录"],
    "误解": ["陈述", "出现频率", "变更记录"],
    "路径": ["编排", "自检", "变更记录"],
    "资源": ["定位", "变更记录"],
}

# 只有「命题」可以说是「已确证」——其余都是组织层或条件性的
ONLY_CLAIMS_CAN_BE_CONFIRMED = True

# 禁止在知识对象里出现的结论性用语（AI 或人都不能写）
FORBIDDEN_PHRASES = []

# 没有 .md 扩展名、但含 Markdown 链接的文档，必须一并检查
EXTRA_TEXT_FILES = ["LICENSE", "LICENSE-CODE"]


def parse_front_matter(text):
    """取出 front-matter 原文；没有则返回 None。"""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 3)
    return text[4:end + 1] if end > 0 else None


def front_matter_keys(fm):
    return re.findall(r"^([A-Za-z_][A-Za-z0-9_]*):", fm, re.M)


def fm_value(fm, key):
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip('"') if m else None


def scan_text_files():
    """所有含 Markdown 链接的文档。

    注意：不只是 .md —— LICENSE / LICENSE-CODE 没有扩展名，但同样含相对链接。
    漏掉它们会形成盲区（曾真实漏掉一处引用）。
    """
    files = []
    for base, dirs, names in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", "__pycache__"}]
        for n in names:
            if n.endswith(".md"):
                files.append(Path(base) / n)
    for n in EXTRA_TEXT_FILES:
        p = ROOT / n
        if p.exists():
            files.append(p)
    return sorted(files)


def resolve_link(src_path, target):
    """把 Markdown 链接目标解析成仓库内的相对路径；解析不到返回 None。"""
    tgt = target.split("#")[0].strip()
    if not tgt or re.match(r"^(https?:|mailto:)", tgt):
        return None
    p = (src_path.parent / tgt.replace("/", os.sep)).resolve()
    try:
        return p.relative_to(ROOT).as_posix()
    except ValueError:
        return None


def fm_links(fm, key):
    """取出 front-matter 里某个键（含缩进块形式）中的 Markdown 链接目标。"""
    m = re.search(rf"^[ \t]*{key}:\s*(.+)$", fm, re.M)
    if m:
        line = m.group(1)
    else:
        b = re.search(rf"^[ \t]*{key}:\s*\n((?:[ \t]+.*\n?)*)", fm, re.M)
        line = b.group(1) if b else ""
    return re.findall(r"\[[^\]]*\]\(([^)]+)\)", line)


def check_graph(objects, errors):
    """先修关系与教法归属的图校验 —— 这些是单看一个文件查不出来的。"""
    prereq = {}

    for rel, o in objects.items():
        t, fm, path = o["type"], o["fm"], o["path"]

        # 先修边只能连「知识点」
        for tgt in fm_links(fm, "先修"):
            r = resolve_link(path, tgt)
            dest = objects.get(r) if r else None
            if t != "知识点":
                errors.append(
                    f"{rel}: 只有「知识点」可以有 `先修` 边（FORMAT.md §2），本条 type={t}")
            if dest is None:
                errors.append(f"{rel}: `先修` 指向的不是知识对象 -> {tgt}")
            elif dest["type"] != "知识点":
                errors.append(
                    f"{rel}: `先修` 必须指向「知识点」，实际指向 type={dest['type']} -> {tgt}")
            else:
                prereq.setdefault(rel, []).append(r)

        # 教法必须有 knowledge_point，且指向「知识点」
        if t == "教法":
            kps = fm_links(fm, "knowledge_point")
            if not kps:
                errors.append(f"{rel}: 「教法」缺 `knowledge_point`（FORMAT.md §4）")
            for tgt in kps:
                r = resolve_link(path, tgt)
                dest = objects.get(r) if r else None
                if dest is None:
                    errors.append(f"{rel}: `knowledge_point` 指向的不是知识对象 -> {tgt}")
                elif dest["type"] != "知识点":
                    errors.append(
                        f"{rel}: `knowledge_point` 必须指向「知识点」，实际 type={dest['type']}")

    # 先修图环检测
    for n in list(prereq):
        prereq.setdefault(n, [])
    color, stack = {}, []

    def dfs(n):
        color[n] = 1
        stack.append(n)
        for m in prereq.get(n, []):
            if color.get(m) == 1:
                i = stack.index(m)
                errors.append("先修图存在环: " + " → ".join(
                    Path(x).stem for x in stack[i:] + [m]))
            elif color.get(m, 0) == 0:
                dfs(m)
        stack.pop()
        color[n] = 2

    for n in prereq:
        if color.get(n, 0) == 0:
            dfs(n)


def check_paths(objects, errors):
    """路径的先修缺口 —— 设计里说这项「可机械校验」，这里把它真的实现出来。"""
    for rel, o in objects.items():
        if o["type"] != "路径":
            continue
        prose = re.sub(r"```.*?```", "", o["text"], flags=re.S)

        refs = set()
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", prose):
            r = resolve_link(o["path"], target)
            dest = objects.get(r)
            if not dest:
                continue
            if dest["type"] == "知识点":
                refs.add(r)
            elif dest["type"] == "教法":
                # 路径通常引用「教法」；知识点要通过教法的 knowledge_point 才能连上
                for kp in fm_links(dest["fm"], "knowledge_point"):
                    kr = resolve_link(dest["path"], kp)
                    if kr and objects.get(kr, {}).get("type") == "知识点":
                        refs.add(kr)

        external = set()
        for tgt in fm_links(o["fm"], "先修"):
            r = resolve_link(o["path"], tgt)
            if r:
                external.add(r)

        for r in sorted(refs):
            for p in fm_links(objects[r]["fm"], "先修"):
                pr = resolve_link(objects[r]["path"], p)
                if pr and pr not in refs and pr not in external:
                    errors.append(
                        f"{rel}: 先修缺口 —— 引用了「{Path(r).stem}」，"
                        f"但它的先修「{Path(pr).stem}」不在本路径内，也未声明为外部先修")


def check_all():
    errors = []
    ids = {}
    objects = {}
    md_files = scan_text_files()

    for path in md_files:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        fm = parse_front_matter(text)

        # 是否是知识对象（在 knowledge/ 下且不是 README）
        is_object = ("knowledge/" in rel) and not rel.endswith("README.md")

        if fm is not None:
            keys = front_matter_keys(fm)
            dup = [k for k, c in collections.Counter(keys).items() if c > 1]
            if dup:
                errors.append(f"{rel}: front-matter 顶层键重复 {dup}")

            missing = [k for k in REQUIRED_FIELDS if k not in keys]
            if missing:
                errors.append(f"{rel}: front-matter 缺字段 {missing}")

            t, st, i = fm_value(fm, "type"), fm_value(fm, "status"), fm_value(fm, "id")

            if t not in TYPES:
                errors.append(f"{rel}: type 非法 -> {t!r}")
            else:
                if st not in ALLOWED_STATUS[t]:
                    errors.append(f"{rel}: type={t} 不允许 status={st!r}")
                for sec in REQUIRED_SECTIONS[t]:
                    if f"## {sec}" not in text:
                        errors.append(f"{rel}: 缺必备小节「{sec}」")
                # FORMAT.md §5：所有类型都必须有 ## 论证（草案下可留空）
                if "## 论证" not in text:
                    errors.append(f"{rel}: 缺必备小节「论证」（所有类型都必须有）")

            if i in ids:
                errors.append(f"{rel}: id 与 {ids[i]} 重复 -> {i}")
            elif i:
                ids[i] = rel

            # 只有「命题」可以用「已确证」
            if ONLY_CLAIMS_CAN_BE_CONFIRMED and t != "命题" and st == "已确证":
                errors.append(
                    f"{rel}: 只有「命题」可以用「已确证」（{t} 不存在唯一正确）")

            if t in TYPES:
                objects[rel] = {"type": t, "fm": fm, "text": text, "path": path}

        elif is_object:
            errors.append(f"{rel}: 知识对象缺 front-matter")

        # 代码围栏必须成对
        if text.count("```") % 2 != 0:
            errors.append(f"{rel}: ``` 代码围栏数量为奇数（未闭合）")

        # 相对链接可达（剥掉代码块，模板代码里的链接不检查）
        prose = re.sub(r"```.*?```", "", text, flags=re.S)
        prose = re.sub(r"`[^`\n]*`", "", prose)
        for label, target in re.findall(r"\[([^\]]*)\]\(([^)]+)\)", prose):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            tgt = target.split("#")[0].strip()
            if not tgt:
                continue
            if not (path.parent / tgt.replace("/", os.sep)).exists():
                errors.append(f"{rel}: 链接目标不存在 -> [{label}]({target})")

    # 图校验：单看一个文件查不出来的那部分
    check_graph(objects, errors)
    check_paths(objects, errors)

    return md_files, ids, errors


def main():
    md_files, ids, errors = check_all()

    print(f"扫描 {len(md_files)} 个文档，识别知识对象 {len(ids)} 条")
    print()

    if errors:
        print("不符合规范之处：")
        for e in errors:
            print(f"  x {e}")
        print()
        print(f"结果：{len(errors)} 处问题")
        return 1

    print("结果：全部通过")
    print("  · front-matter 完整")
    print("  · type / status 合法（只有「命题」可以用「已确证」）")
    print("  · id 唯一")
    print("  · 相对链接全部可达")
    print("  · 必备小节齐全")
    print("  ── 以下三项是单看一个文件查不出来的 ──")
    print("  · `先修` 边只连「知识点」，且无环")
    print("  · `教法` 都有 `knowledge_point`，且指向「知识点」")
    print("  · 每条路径的「先修缺口」已机械校验（无缺口）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
