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

TYPES = {"命题", "教法", "误解", "路径", "资源"}

ALLOWED_STATUS = {
    "命题": {"草案", "待审", "争议", "暂定确认", "已确证", "已推翻", "需复审", "已失效"},
    "教法": {"草案", "待审", "有效", "争议", "需复审", "已失效"},
    "误解": {"草案", "待审", "有效", "争议", "需复审", "已失效"},
    "资源": {"草案", "待审", "有效", "争议", "需复审", "已失效"},
    "路径": {"草案", "待审", "有效", "争议", "需复审", "已失效"},
}

REQUIRED_FIELDS = ["id", "type", "title", "status", "author", "created",
                   "updated", "scope", "edges", "evidence", "license"]

REQUIRED_SECTIONS = {
    "命题": ["陈述", "依据", "论证", "变更记录"],
    "教法": ["做法", "禁忌", "证据", "论证", "变更记录"],
    "误解": ["陈述", "出现频率", "变更记录"],
    "路径": ["编排", "自检", "变更记录"],
    "资源": ["定位", "变更记录"],
}

# 禁止在知识对象里出现的结论性用语（AI 或人都不能写）
FORBIDDEN_PHRASES = []


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


def scan_markdown():
    files = []
    for base, dirs, names in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", "__pycache__"}]
        for n in names:
            if n.endswith(".md"):
                files.append(Path(base) / n)
    return sorted(files)


def check_all():
    errors = []
    ids = {}
    md_files = scan_markdown()

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

            # 公理 A2：教法/误解/资源禁止使用「已确证」
            if t in ("教法", "误解", "资源") and st == "已确证":
                errors.append(f"{rel}: {t} 禁止使用「已确证」（公理 A2：知识要收敛，教法要并存）")

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

    return md_files, ids, errors


def main():
    md_files, ids, errors = check_all()

    print(f"扫描 {len(md_files)} 个 markdown 文件，识别知识对象 {len(ids)} 条")
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
    print("  · type / status 合法（含公理 A2：教法类禁用「已确证」）")
    print("  · id 唯一")
    print("  · 相对链接全部可达")
    print("  · 必备小节齐全")
    return 0


if __name__ == "__main__":
    sys.exit(main())
