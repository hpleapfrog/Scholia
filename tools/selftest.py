#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""接口自检：把「工具真的能用」也变成一条可执行的命令。

为什么要有
----------
`kbcheck` 查的是**内容**（格式、链接、证据），`verify_rules` 查的是**规则会不会响**。
两者都不查**别人实际会碰的三个接口**：

| 接口 | 谁在用 | 坏了会怎样 |
|---|---|---|
| `tools/scholia_mcp.py` | 挂到 agent 上的人 | 握手成功、工具一调就崩，或悄悄返回 `error:` 文本 |
| `tools/make_tasks.py --json` | 想接脚本 / 派活的人 | 输出的 JSON 解析不了，或与 `docs/GAPS.md` 数字不一致 |
| `tools/new_entry.py` | 想加第一条内容的新人 | 生成的骨架缺字段，第一次跑 `kbcheck` 就满屏红 |

这三件事都属于「单看代码没问题，跑起来才发现」。所以这里**真的启动子进程**、
**真的走一遍 stdio 握手**、**真的在临时目录里生成一个条目**，而不是 import 一下函数。

设计约束
--------
- 零第三方依赖；不联网；**不写仓库**（临时目录用完即删）。
- 每个检查独立报 PASS/FAIL，最后汇总；任一失败退出码 1。
- 输出用英文短句：CI 日志与 Windows 控制台都不会把它变成乱码。

用法
----
    python tools/selftest.py
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
PY = sys.executable

sys.path.insert(0, str(TOOLS))
import gaps  # noqa: E402  与 GAPS 页面 / MCP / make_tasks 共用同一个 compute()

ENV = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
CHECKS = []


class Failed(AssertionError):
    """一条检查失败。消息会直接打给用户，所以要写清「期望 vs 实际」。"""


def need(cond, msg):
    if not cond:
        raise Failed(msg)


def check(fn):
    CHECKS.append(fn)
    return fn


def load(name):
    p = ROOT / name
    need(p.exists(), f"missing {name} — run python tools/kbcheck.py --write-index")
    return json.loads(p.read_text(encoding="utf-8"))


def run(args, cwd=ROOT, timeout=240):
    return subprocess.run(
        [PY] + [str(a) for a in args], cwd=str(cwd),
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        env=ENV, timeout=timeout,
    )


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def front_matter(text):
    norm = text.replace("\r\n", "\n")
    need(norm.startswith("---\n"), "file does not start with front-matter")
    end = norm.find("\n---", 3)
    need(end > 0, "front-matter is not closed")
    out = {}
    for line in norm[4:end].split("\n"):
        if line and not line[0].isspace() and ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out, norm


def generated_block(rel):
    text = (ROOT / rel).read_text(encoding="utf-8").replace("\r\n", "\n")
    m = re.search(r"<!-- kbcheck:begin -->\n(.*?)<!-- kbcheck:end -->", text, re.S)
    need(m, f"{rel}: generated block not found (R-INDEX-02 should have caught this)")
    return m.group(1)


# ── 1. 生成物自洽 ──────────────────────────────────────────────────────────
@check
def generated_files():
    idx = load("index.json")
    cites = load("citations.json")["by_id"]
    evid = load("evidence.json")["entries"]

    need(idx.get("schema_version", 0) >= 5,
         f"index.json schema_version={idx.get('schema_version')}, expected >= 5")
    objs = idx.get("objects") or []
    need(objs, "index.json has no objects")

    missing = [o["path"] for o in objs if not (ROOT / o["path"]).exists()]
    need(not missing, f"{len(missing)} object paths do not exist, e.g. {missing[:3]}")
    missing_en = [o["path_en"] for o in objs
                  if o.get("path_en") and not (ROOT / o["path_en"]).exists()]
    need(not missing_en, f"{len(missing_en)} English paths do not exist, e.g. {missing_en[:3]}")

    no_title_en = [o["id"] for o in objs if o.get("path_en") and not o.get("title_en")]
    need(not no_title_en,
         f"{len(no_title_en)} objects have path_en but no title_en, e.g. {no_title_en[:3]}")

    ids = {o["id"] for o in objs}
    stray = [k for k in cites if k not in ids and k not in
             {e.get("id") for e in (idx.get("事件") or [])}]
    need(not stray, f"citations.json has {len(stray)} ids not in index: {stray[:3]}")

    need(len(evid) == idx["统计"]["证据条数"],
         f"evidence.json has {len(evid)} entries, index says {idx['统计']['证据条数']}")

    paths = [o for o in objs if o["type"] == "路径"]
    need(paths, "no 路径 objects")
    bad = [o["id"] for o in paths
           if o.get("覆盖度") and o["覆盖度"]["已覆盖"] > o["覆盖度"]["声明"]]
    need(not bad, f"coverage exceeds declared outcomes: {bad}")
    return f"{len(objs)} objects, {len(cites)} citations, {len(evid)} evidence, {len(paths)} paths"


# ── 2. gaps 计算确定，且计数与条目数一致 ──────────────────────────────────
@check
def gaps_determinism():
    idx = load("index.json")
    cites = load("citations.json")["by_id"]
    evid = load("evidence.json")["entries"]
    a = gaps.compute(idx, cites, evid, root=ROOT)
    b = gaps.compute(idx, cites, evid, root=ROOT)
    need(json.dumps(a, sort_keys=True, ensure_ascii=False) ==
         json.dumps(b, sort_keys=True, ensure_ascii=False),
         "two compute() calls disagree — gap counts are not deterministic")

    for key, g in a["分组"].items():
        need(g["数量"] == len(g["条目"]),
             f"group {key}: 数量={g['数量']} but 条目={len(g['条目'])}")
    total = sum(g["数量"] for g in a["分组"].values())
    need(a["统计"]["缺口合计"] == total,
         f"统计.缺口合计={a['统计']['缺口合计']} but groups sum to {total}")
    pending = (a["统计"].get("状态") or {}).get("待审")
    if pending is not None:
        split = a["分组"]["review"]["数量"] + a["分组"]["review-blocked"]["数量"]
        need(split == pending,
             f"review + review-blocked = {split}, but index says {pending} 待审 — "
             "the two groups are supposed to partition all pending entries")
    for it in a["分组"]["review-blocked"]["条目"]:
        need(it.get("无论证") or it.get("无证据") or it.get("未读证据"),
             f"review-blocked item {it['id']} states no blocker — a blocked entry "
             "must say whether the argument is missing, nothing is cited, or which evidence is unread")
    return " ".join(f"{k}={v}" for k, v in gaps.counts(a).items())


# ── 3. 生成的 GAPS 页面与 compute() 同源 ──────────────────────────────────
@check
def gaps_pages_in_sync():
    idx = load("index.json")
    data = gaps.compute(idx, load("citations.json")["by_id"],
                        load("evidence.json")["entries"], root=ROOT)
    ids = {o["id"] for o in idx["objects"]}

    for rel, en in (("docs/GAPS.md", False), ("docs/GAPS.en.md", True)):
        blk = generated_block(rel)
        rows = {name: int(n) for name, n in
                re.findall(r"^\| \*\*(.+?)\*\* \| (\d+) \|", blk, re.M)}
        need(len(rows) == len(data["顺序"]),
             f"{rel}: {len(rows)} gap rows, expected {len(data['顺序'])}")
        for key in data["顺序"]:
            g = data["分组"][key]
            name = g["名称_en"] if en else g["名称"]
            need(name in rows, f"{rel}: missing row for {name!r}")
            need(rows[name] == g["数量"],
                 f"{rel}: {name!r} says {rows[name]}, compute() says {g['数量']}")

        # 页面上出现的每个对象 id 都必须真实存在——生成物也会过时，
        # 而过时的生成物比手写的更危险：它看起来是机器算的。
        listed = re.findall(r"`(kb:[^`]+)`", blk)
        unknown = sorted(set(listed) - ids)
        need(not unknown, f"{rel}: lists unknown ids {unknown[:3]}")
        need(f"**{data['统计']['对象']}** " in blk,
             f"{rel}: object count does not match index.json")
    return "both pages agree with compute()"


# ── 4. make_tasks 的 JSON 是稳定的机器接口 ────────────────────────────────
@check
def make_tasks_json():
    r = run(["tools/make_tasks.py", "--json"])
    need(r.returncode == 0, f"exit {r.returncode}: {r.stderr[-400:]}")
    need("Traceback" not in r.stderr, f"traceback on stderr: {r.stderr[-400:]}")
    data = json.loads(r.stdout)
    for key in ("统计", "分组", "顺序"):
        need(key in data, f"missing top-level key {key!r}")
    need(data["顺序"] == [g[0] for g in gaps.GROUPS],
         f"顺序={data['顺序']} does not match gaps.GROUPS order")

    direct = gaps.compute(load("index.json"), load("citations.json")["by_id"],
                          load("evidence.json")["entries"], root=ROOT)
    need(data["统计"] == direct["统计"], "统计 differs from compute()")
    for key in direct["顺序"]:
        need(data["分组"][key]["数量"] == direct["分组"][key]["数量"],
             f"{key}: CLI says {data['分组'][key]['数量']}, compute() says "
             f"{direct['分组'][key]['数量']}")

    # 人类可读模式也要能跑，且不漏组。
    r2 = run(["tools/make_tasks.py", "--limit", "2"])
    need(r2.returncode == 0, f"human mode exit {r2.returncode}: {r2.stderr[-400:]}")
    for key in direct["顺序"]:
        need(direct["分组"][key]["名称"] in r2.stdout,
             f"human output is missing group {key}")
    return f"{len(direct['顺序'])} groups, JSON and text agree"


# ── 5. new_entry 在空目录里也能产出合规骨架 ───────────────────────────────
@check
def new_entry_scaffold():
    sys.path.insert(0, str(TOOLS))
    import kbcheck  # noqa: E402  借用它的必填字段清单，避免这里再抄一份

    tmp = Path(tempfile.mkdtemp(prefix="scholia-selftest-"))
    try:
        (tmp / "tools").mkdir()
        shutil.copy2(TOOLS / "new_entry.py", tmp / "tools" / "new_entry.py")
        shutil.copytree(ROOT / "templates", tmp / "templates")

        r = run([tmp / "tools" / "new_entry.py", "-t", "命题", "-s", "物理",
                 "--slug", "selftest-demo", "--title", "自检示例",
                 "--external-prereq", "几何中的角|angle|数学|初中|ev-000"], cwd=tmp)
        need(r.returncode == 0, f"exit {r.returncode}: {r.stderr[-600:]}")
        out = tmp / "knowledge" / "physics" / "claims" / "自检示例.md"
        need(out.exists(), f"scaffold not written to {out}")

        fm, text = front_matter(out.read_text(encoding="utf-8"))
        for field in kbcheck.REQUIRED_FIELDS:
            need(field in fm, f"generated entry is missing front-matter field {field!r}")
        need(fm["id"] == "kb:physics:selftest-demo",
             f"id={fm['id']!r}, expected kb:physics:selftest-demo")
        need(fm["type"] == "命题", f"type={fm['type']!r}")
        for sec in kbcheck.REQUIRED_SECTIONS["命题"]:
            need(f"\n## {sec}" in text, f"generated entry is missing section ## {sec}")
        need("外部先修:" in text and "angle" in text,
             "--external-prereq was not written into front-matter")
        need("selftest-demo.en.md" in r.stdout,
             "stdout does not tell the user where the English edition goes")

        # 负样本：坏的 slug / 缺 subject / 重复生成，都必须**失败**。
        bad_slug = run([tmp / "tools" / "new_entry.py", "-t", "命题", "-s", "物理",
                        "--slug", "Bad_Slug", "--title", "x"], cwd=tmp)
        need(bad_slug.returncode != 0, "non-ASCII/uppercase slug was accepted")
        no_subject = run([tmp / "tools" / "new_entry.py", "-t", "命题",
                          "--slug", "x", "--title", "x"], cwd=tmp)
        need(no_subject.returncode != 0, "missing --subject was accepted")
        again = run([tmp / "tools" / "new_entry.py", "-t", "命题", "-s", "物理",
                     "--slug", "selftest-demo", "--title", "自检示例"], cwd=tmp)
        need(again.returncode != 0, "overwriting an existing entry was allowed without --force")
        return "scaffold has all fields; 3 bad invocations refused"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ── 6. MCP：握手 + 只读 + 每个工具都能调 ──────────────────────────────────
class MCPClient:
    def __init__(self):
        self.proc = subprocess.Popen(
            [PY, str(TOOLS / "scholia_mcp.py")], cwd=str(ROOT),
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, encoding="utf-8", errors="replace", bufsize=1, env=ENV)
        self._id = 0

    def rpc(self, method, params=None):
        self._id += 1
        msg = {"jsonrpc": "2.0", "id": self._id, "method": method}
        if params is not None:
            msg["params"] = params
        self.proc.stdin.write(json.dumps(msg, ensure_ascii=False) + "\n")
        self.proc.stdin.flush()
        line = self.proc.stdout.readline()
        if not line:
            err = self.proc.stderr.read()[:400] if self.proc.stderr else ""
            raise Failed(f"MCP closed stdout during {method}: {err}")
        return json.loads(line)

    def call(self, name, args=None):
        r = self.rpc("tools/call", {"name": name, "arguments": args or {}})
        need("error" not in r, f"{name}: JSON-RPC error {r.get('error')}")
        text = r["result"]["content"][0]["text"]
        need(not text.startswith("error:"), f"{name} raised: {text[:240]}")
        return json.loads(text)

    def close(self):
        try:
            self.proc.stdin.close()
        except OSError:
            pass
        try:
            self.proc.wait(timeout=15)
        except subprocess.TimeoutExpired:
            self.proc.kill()


@check
def mcp_handshake_and_readonly():
    watched = ["index.json", "citations.json", "evidence.json"]
    before = {name: sha(ROOT / name) for name in watched}

    c = MCPClient()
    try:
        init = c.rpc("initialize", {"protocolVersion": "2024-11-05"})
        need("result" in init, f"initialize failed: {init}")
        need(init["result"]["serverInfo"]["name"] == "scholia",
             f"serverInfo={init['result']['serverInfo']}")
        need(c.rpc("ping")["result"] == {}, "ping did not return an empty result")

        listed = c.rpc("tools/list")["result"]["tools"]
        names = [t["name"] for t in listed]
        expected = {"scholia_stats", "scholia_search", "scholia_list",
                    "scholia_external_prereqs", "scholia_get_object", "scholia_cite",
                    "scholia_get_evidence", "scholia_gaps", "scholia_rules"}
        need(set(names) == expected,
             f"tools/list mismatch: missing={sorted(expected - set(names))} "
             f"extra={sorted(set(names) - expected)}")
        for t in listed:
            need(t.get("inputSchema", {}).get("type") == "object",
                 f"{t['name']}: inputSchema is not an object schema")
    finally:
        c.close()

    after = {name: sha(ROOT / name) for name in watched}
    changed = [n for n in watched if before[n] != after[n]]
    need(not changed, f"MCP server modified {changed} — it must be read-only")
    return f"{len(names)} tools, handshake ok, 3 files untouched"


@check
def mcp_tools_callable():
    idx = load("index.json")
    cites = load("citations.json")["by_id"]
    evid = load("evidence.json")["entries"]
    objs = idx["objects"]
    direct = gaps.compute(idx, cites, evid, root=ROOT)

    with_arg = next(o for o in objs if o.get("论证"))
    cite_id = next(iter(cites))
    ev_id = next(iter(evid))
    ext = (idx.get("外部先修") or {}).get("按标识") or []
    need(ext, "index.json has no 外部先修 groups to exercise the tool")

    c = MCPClient()
    try:
        stats = c.call("scholia_stats")
        need(stats["对象总数"] == len(objs),
             f"stats says {stats['对象总数']} objects, index has {len(objs)}")

        s = c.call("scholia_search", {"query": "加速度", "limit": 2})
        need(s["count"] > 0 and s["results"], "Chinese search returned nothing")
        need(all(r.get("path") for r in s["results"]), "search results lack path")

        en = c.call("scholia_search", {"query": "electric field", "limit": 5})
        need(any(r.get("title_en") for r in en["results"]),
             "English search returns no title_en — English readers cannot identify entries")
        need(en["results"][0].get("title_en") == "Electric field",
             "exact title match is not ranked first: "
             f"{[r.get('title_en') for r in en['results']]}")
        reordered = c.call("scholia_search", {"query": "field electric", "limit": 1})
        need(reordered["count"] > 0, "multi-term AND search found nothing for 'field electric'")

        listed = c.call("scholia_list", {"type": "知识点", "limit": 1})
        want = sum(1 for o in objs if o["type"] == "知识点")
        need(listed["count"] == want,
             f"scholia_list count={listed['count']}, expected {want}")
        need(len(listed["results"]) == 1, "limit was not applied by scholia_list")

        g = c.call("scholia_external_prereqs", {"key": ext[0]["标识"]})
        need(g.get("标识") == ext[0]["标识"], "external_prereqs did not return the group")

        content = c.call("scholia_get_object", {"id": with_arg["id"]})
        full = c.call("scholia_get_object", {"id": with_arg["id"], "part": "full"})
        need("## 论证" not in content["markdown"],
             "part=content leaked the reviewer half (## 论证)")
        need("## 论证" in full["markdown"], "part=full is missing ## 论证")
        need(len(content["markdown"]) < len(full["markdown"]),
             "part=content is not shorter than part=full")

        cite = c.call("scholia_cite", {"id": cite_id})
        need(cite.get("status") and cite.get("来源"),
             "scholia_cite must return status and 来源 together")

        ev = c.call("scholia_get_evidence", {"id": ev_id})
        need("核验深度" in ev, "scholia_get_evidence is missing 核验深度")

        gaps_out = c.call("scholia_gaps")
        got = {x["key"]: x["数量"] for x in gaps_out["缺口"]}
        need(got == gaps.counts(direct),
             f"MCP gaps {got} != compute() {gaps.counts(direct)}")
        grp = c.call("scholia_gaps", {"group": "review", "limit": 2})
        need(grp["数量"] == direct["分组"]["review"]["数量"], "group count mismatch")
        need(len(grp["条目"]) == 2, "limit was not applied by scholia_gaps")
        need(grp.get("还有", 0) == grp["数量"] - 2, "scholia_gaps did not report the remainder")

        rules = c.call("scholia_rules")
        need("R-" in rules.get("markdown", ""), "scholia_rules returned no rule ids")

        bad = c.rpc("tools/call", {"name": "no_such_tool", "arguments": {}})
        text = bad["result"]["content"][0]["text"]
        need(text.startswith("error:"), "unknown tool did not report an error")
        return "9/9 tools returned usable payloads; unknown tool reported an error"
    finally:
        c.close()


@check
def mcp_print_config():
    r = run(["tools/scholia_mcp.py", "--print-config"])
    need(r.returncode == 0, f"exit {r.returncode}: {r.stderr[-400:]}")
    first = r.stdout.split("\n\n", 1)[0]
    cfg = json.loads(first)
    args = cfg["mcpServers"]["scholia"]["args"]
    need(args and args[0].endswith("scholia_mcp.py"),
         f"--print-config points at {args!r}, not scholia_mcp.py")
    return "config parses and points at the server"


# ── 9. 复核包：把材料摆到一页，但不替人回答 ────────────────────────────────
@check
def review_packet():
    idx = load("index.json")
    data = gaps.compute(idx, load("citations.json")["by_id"],
                        load("evidence.json")["entries"], root=ROOT)
    items = data["分组"]["review"]["条目"]
    need(items, "no reviewable entries to build a packet for")
    oid = items[0]["id"]

    r = run(["tools/review_packet.py", "--id", oid])
    need(r.returncode == 0, f"exit {r.returncode}: {r.stderr[-400:]}")
    out = r.stdout
    for needle in (oid, "三个问题", "M-07", "来源", "复核记录"):
        need(needle in out, f"packet is missing {needle!r}")
    need(re.search(r"`ev-\d+`", out), "packet lists no evidence id")

    if len(items) > 1:
        oid2 = items[1]["id"]
        r3 = run(["tools/review_packet.py", "--id", oid, "--id", oid2])
        need(r3.returncode == 0, f"two --id exit {r3.returncode}: {r3.stderr[-400:]}")
        need(oid in r3.stdout and oid2 in r3.stdout,
             "two --id values produced fewer than two packets — --id must default to all")

    r4 = run(["tools/review_packet.py", "--group", "review", "--limit", "1"])
    need(r4.returncode == 0, f"--group exit {r4.returncode}: {r4.stderr[-400:]}")
    need("复核包" in r4.stdout and oid in r4.stdout,
         "--group review did not produce the same top-ranked packet")

    if data["分组"]["review-blocked"]["数量"]:
        r5 = run(["tools/review_packet.py", "--group", "review-blocked", "--limit", "1"])
        need(r5.returncode == 0, f"blocked group exit {r5.returncode}: {r5.stderr[-400:]}")
        need("还不能开始复核" in r5.stdout,
             "a review-blocked packet does not warn that the evidence is unread")

    tmp = Path(tempfile.mkdtemp(prefix="scholia-packet-"))
    try:
        r2 = run(["tools/review_packet.py", "--id", oid, "--out", tmp])
        need(r2.returncode == 0, f"--out exit {r2.returncode}: {r2.stderr[-400:]}")
        files = sorted(tmp.glob("review-*.md"))
        need(len(files) == 1, f"--out wrote {len(files)} files, expected 1")
        text = files[0].read_text(encoding="utf-8")
        need("三个问题" in text and oid in text,
             "--out file does not contain the packet")
        return (f"{oid}: packet has sources, questions, group path, blocked warning, "
                "multiple --id render, and --out writes one file")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    print(f"selftest: {len(CHECKS)} checks, repo {ROOT}\n")
    failed = 0
    for fn in CHECKS:
        name = fn.__name__
        try:
            detail = fn()
        except Exception as e:  # noqa: BLE001  一条失败不应中断其余检查
            failed += 1
            print(f"FAIL  {name}\n      {type(e).__name__}: {e}")
        else:
            print(f"PASS  {name}" + (f"  [{detail}]" if detail else ""))
    print()
    if failed:
        print(f"{len(CHECKS) - failed}/{len(CHECKS)} checks passed — {failed} FAILED")
        return 1
    print(f"{len(CHECKS)}/{len(CHECKS)} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
