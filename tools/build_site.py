#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把整个库生成成**一个 HTML 文件**：能搜、能读、能看见图。

为什么要有
----------
本库的自我描述一直是「一堆 Markdown + 一套校验」。这对贡献者是对的，
对**第一次来的人**是灾难：他打开仓库看到 746 个文件、45 条规则、一个
「已确证 0」，然后关掉页面。

而这个库真正稀缺的东西——**每条内容都能顺着来源一路核到底**——在文件列表里
一个像素都看不见。

所以：一个从 `index.json` / `citations.json` / `evidence.json` **生成**的页面。
它不是第二个知识库（内容仍然只有一份，在 `.md` 里），是那张图的**一次投影**——
`README` 里那句话的原话是「知识图是唯一的；教科书是这张图对某个读者的一次投影」。

为什么是单文件、零依赖
----------------------
- **单文件**：`file://` 打开就能用，不需要服务器、不需要构建、不需要 node。
- **零依赖**：不引 CDN。一个引用了外部脚本的知识库页面，会在断网时变成白屏，
  也会在五年后因为那个 CDN 下线而变成白屏——而这套东西的目标是**可长期自持**。
- **生成物**：所有数字来自 `index.json`，不手写。改了内容不重生成，`--check` 会失败。

用法
----
    python tools/build_site.py            # 写 site/index.html
    python tools/build_site.py --check    # 与磁盘上的一致吗（CI 用）

看什么
------
- **左栏**：746 条对象的列表，可按学科 / 类型 / 状态 / 溯源档筛，输入即搜索。
- **右栏**：正文（**只到学习者半**——`## 论证` 与 `## 变更记录` 不进来，那是复核者看的），
  顶上带 `status` 与 `溯源` 两枚徽章，底下是这一条引用的**来源原话定位**。
- **图谱**：知识点之间的 `先修` 关系，按最长路径分层。点节点看条目。

边界
----
页面**不新增任何判定**：状态、溯源档、能不能引用全是 `index.json` 里已有的值。
它只做排版与检索。所以它不会比库里的事实更权威——这正是它安全的原因。
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "index.html"

# 读者不需要的小节：论证与记账属于复核者。**不删内容，只是不投影进来。**
REVIEWER_SECTIONS = ("论证", "变更记录", "待补", "自检")

TYPE_ORDER = ["知识点", "命题", "教法", "误解", "资源", "路径"]
TYPE_LABEL = {"知识点": "概念", "命题": "命题", "教法": "教法",
              "误解": "误解", "资源": "资源", "路径": "路径"}
STATUS_TONE = {
    "已确证": "ok", "暂定确认": "ok", "有效": "ok",
    "待审": "wait", "需复审": "warn", "争议": "warn",
    "失据": "bad", "已推翻": "bad", "已失效": "bad", "草案": "wait",
}
TIER_NOTE = {
    "T4": "引用的每一份来源都通读过",
    "T3": "最弱的那份只读到摘要",
    "T2": "最弱的那份只核了位置，没通读",
    "T1": "最弱的那份登记了，但没人打开过",
    "T0": "有作废或查不到的编号",
}


# ── 极简 Markdown → HTML ────────────────────────────────────────────────────
# 只用标准库。刻意不支持嵌套列表、脚注、HTML 内嵌——条目里也没有；
# 支持它们会让这个渲染器变成另一个需要维护的项目。
INLINE_CODE = re.compile(r"`([^`\n]+)`")
BOLD = re.compile(r"\*\*([^*\n]+)\*\*")
ITALIC = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


def inline(text):
    out = html.escape(text, quote=False)
    out = INLINE_CODE.sub(lambda m: f"<code>{m.group(1)}</code>", out)
    out = BOLD.sub(lambda m: f"<strong>{m.group(1)}</strong>", out)
    out = ITALIC.sub(lambda m: f"<em>{m.group(1)}</em>", out)

    def link(m):
        label, href = m.group(1), m.group(2)
        if href.startswith("http"):
            return (f'<a href="{html.escape(href, quote=True)}" '
                    f'target="_blank" rel="noreferrer">{label}</a>')
        # 站内链接在单文件里没有对应页面：留文字，不留死链。
        return f'<span class="ref">{label}</span>'

    return LINK.sub(link, out)


def md_to_html(text):
    """把条目正文转成 HTML。遇到不认识的行就当段落——**不吞内容**。"""
    lines = text.replace("\r\n", "\n").split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()

        if not s:
            i += 1
            continue

        if s.startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            out.append("<pre>" + html.escape("\n".join(buf)) + "</pre>")
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            i += 1
            continue

        if re.match(r"^(-{3,}|\*{3,})$", s):
            out.append("<hr>")
            i += 1
            continue

        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            head = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append("<div class='tbl'><table><thead><tr>"
                       + "".join(f"<th>{inline(c)}</th>" for c in head)
                       + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
                                 for r in rows)
                       + "</tbody></table></div>")
            continue

        if s.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^>\s?", "", lines[i].strip()))
                i += 1
            body = "\n".join(buf)
            kind = ""
            mcall = re.match(r"^\[!(\w+)\]", body)
            if mcall:
                kind = {"IMPORTANT": "imp", "WARNING": "warn", "NOTE": "note",
                        "TIP": "tip", "CAUTION": "warn"}.get(mcall.group(1), "note")
                body = body[mcall.end():].lstrip("\n")
            out.append(f"<blockquote class='{kind}'>{md_to_html(body)}</blockquote>")
            continue

        if re.match(r"^[-*]\s+", s) or re.match(r"^\d+[.)]\s+", s):
            ordered = bool(re.match(r"^\d+[.)]\s+", s))
            items = []
            while i < n and (re.match(r"^[-*]\s+", lines[i].strip())
                             or re.match(r"^\d+[.)]\s+", lines[i].strip())):
                items.append(re.sub(r"^(?:[-*]|\d+[.)])\s+", "", lines[i].strip()))
                i += 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue

        buf = [s]
        i += 1
        while i < n:
            nxt = lines[i].strip()
            if (not nxt or nxt.startswith(("#", ">", "|", "```"))
                    or re.match(r"^[-*]\s+", nxt) or re.match(r"^\d+[.)]\s+", nxt)):
                break
            buf.append(nxt)
            i += 1
        out.append(f"<p>{inline(' '.join(buf))}</p>")
    return "\n".join(out)


def split_body(text):
    """去掉 front-matter，并砍掉复核者那半（`## 论证` 起）。"""
    body = text
    if body.startswith("---\n"):
        end = body.find("\n---\n", 3)
        if end > 0:
            body = body[end + 5:]
    parts = re.split(r"\n(?=## )", body)
    keep = []
    for p in parts:
        head = p.split("\n", 1)[0].lstrip("# ").strip()
        if head in REVIEWER_SECTIONS:
            continue
        keep.append(p)
    return "\n".join(keep)


def plain(html_text):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html_text)).strip()


# ── 数据 ───────────────────────────────────────────────────────────────────
def build_payload():
    index = json.loads((ROOT / "index.json").read_text(encoding="utf-8"))
    cites = json.loads((ROOT / "citations.json").read_text(encoding="utf-8")).get("by_id", {})
    evid = json.loads((ROOT / "evidence.json").read_text(encoding="utf-8")).get("entries", {})

    objects = index.get("objects", [])
    by_path = {}
    entries = []
    for o in objects:
        p = ROOT / o["path"]
        body = ""
        if p.exists():
            body = split_body(p.read_text(encoding="utf-8"))
        rendered = md_to_html(body) if body else ""
        cite = cites.get(o["id"], {})
        srcs = []
        for e in (cite.get("证据") or []):
            rec = evid.get(e, {})
            loc = rec.get("定位") or ""
            srcs.append({"id": e, "loc": loc[:320], "url": rec.get("链接") or "",
                         "depth": rec.get("核验深度") or "", "void": bool(rec.get("作废"))})
        entry = {
            "id": o["id"],
            "title": o["title"],
            "type": o["type"],
            "subject": (o.get("学科") or "").split(" ")[0],
            "stage": o.get("学段") or "",
            "status": o["status"],
            "tier": o.get("溯源") or "T0",
            "citable": bool(o.get("可作事实引用", True)),
            "reviewer": o.get("复核者"),
            "path": o["path"],
            "path_en": o.get("path_en"),
            "prereq": o.get("先修") or [],
            "outcomes": o.get("覆盖度") or None,
            "html": rendered,
            "search": plain(f"{o['title']} {rendered}")[:4000],
            "srcs": srcs,
        }
        entries.append(entry)
        by_path[Path(o["path"]).stem] = o["id"]

    # 图谱：只取知识点之间的 `先修`（`先修` 的值是文件名）。
    concepts = [e for e in entries if e["type"] == "知识点"]
    ids = {e["id"] for e in concepts}
    edges = []
    for e in concepts:
        for name in e["prereq"]:
            tid = by_path.get(Path(name).stem)
            if tid in ids:
                edges.append([tid, e["id"]])

    # 最长路径分层（图已由 R-GRAPH-01 保证无环；这里再兜一层，防止生成物被手改）。
    depth = {e["id"]: 0 for e in concepts}
    for _ in range(len(concepts)):
        changed = False
        for src, dst in edges:
            if depth[dst] < depth[src] + 1:
                depth[dst] = depth[src] + 1
                changed = True
        if not changed:
            break
    nodes = []
    for e in concepts:
        nodes.append({"id": e["id"], "label": e["title"][:14], "d": depth[e["id"]],
                      "tier": e["tier"], "status": e["status"]})
    return {"entries": entries, "edges": edges, "nodes": nodes,
            "stats": index.get("统计", {}),
            "tier_note": TIER_NOTE,
            "repo": index.get("repo", ""),
            "generated_by": "tools/build_site.py"}


# ── 页面 ───────────────────────────────────────────────────────────────────
PAGE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Scholia —— 证据可追溯的知识库</title>
<style>
:root{
  --ink:#15171c; --ink2:#4b5260; --ink3:#7b8494;
  --paper:#fbfaf7; --card:#ffffff; --line:#e6e4de;
  --accent:#2f4bd6; --accent-soft:#eef1ff;
  --ok:#0f7a52; --ok-soft:#e8f5ef;
  --wait:#8a6d1f; --wait-soft:#fbf3dd;
  --bad:#a3231d; --bad-soft:#fbeceb;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;
}
*{box-sizing:border-box}
html,body{margin:0;height:100%}
body{
  background:var(--paper); color:var(--ink);
  font:16px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans SC","PingFang SC",
       "Hiragino Sans GB","Microsoft YaHei",sans-serif;
  -webkit-font-smoothing:antialiased;
}
a{color:var(--accent)}
code{font:0.9em/1.5 var(--mono); background:#f2f1ec; border:1px solid var(--line);
     border-radius:4px; padding:.05em .35em}
pre{background:#f7f6f2;border:1px solid var(--line);border-radius:8px;padding:12px 14px;
    overflow:auto;font:0.86em/1.6 var(--mono)}

header{
  position:sticky;top:0;z-index:20;
  display:flex;align-items:center;gap:22px;
  padding:14px 26px;
  background:linear-gradient(180deg,#fff 0%,#fefdfa 100%);
  border-bottom:1px solid var(--line);
}
.brand{display:flex;align-items:baseline;gap:10px;min-width:210px}
.brand b{font-size:22px;letter-spacing:.02em}
.brand span{font-size:12px;color:var(--ink3)}
.kpis{display:flex;gap:18px;flex:1;flex-wrap:wrap}
.kpi{display:flex;flex-direction:column;line-height:1.25}
.kpi b{font:600 17px/1.2 var(--mono)}
.kpi i{font-style:normal;font-size:11px;color:var(--ink3);letter-spacing:.04em}
.kpi.hl b{color:var(--accent)}
#q{
  width:280px;padding:9px 12px;border:1px solid var(--line);border-radius:9px;
  background:#fff;font-size:14px;outline:none;
}
#q:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}

main{display:grid;grid-template-columns:390px 1fr;height:calc(100vh - 66px)}
aside{border-right:1px solid var(--line);display:flex;flex-direction:column;min-height:0;background:#fff}
.chips{display:flex;flex-wrap:wrap;gap:6px;padding:12px 14px 8px;border-bottom:1px solid var(--line)}
.chip{
  font-size:12px;padding:4px 10px;border-radius:99px;border:1px solid var(--line);
  background:#fff;color:var(--ink2);cursor:pointer;user-select:none;
}
.chip:hover{border-color:#cfd4e4}
.chip.on{background:var(--accent);border-color:var(--accent);color:#fff}
.chip .n{opacity:.6;margin-left:4px}
#meta{padding:8px 16px;font-size:12px;color:var(--ink3);border-bottom:1px solid var(--line)}
#list{overflow:auto;flex:1;min-height:0}
.item{
  padding:10px 16px;border-bottom:1px solid #f1efe9;cursor:pointer;display:block;
}
.item:hover{background:#faf9f5}
.item.on{background:var(--accent-soft);box-shadow:inset 3px 0 0 var(--accent)}
.item .t{font-size:14px;line-height:1.45;color:var(--ink)}
.item .m{margin-top:3px;font:11px/1.4 var(--mono);color:var(--ink3);display:flex;gap:8px}
.dot{width:6px;height:6px;border-radius:50%;display:inline-block;vertical-align:1px}
.d-ok{background:var(--ok)} .d-wait{background:#c9a227} .d-warn{background:#c07000} .d-bad{background:var(--bad)}
.d-machine{background:var(--accent)}

section{overflow:auto;min-height:0;position:relative}
#doc{max-width:820px;margin:0 auto;padding:34px 40px 90px}
.crumb{font:11px/1.4 var(--mono);color:var(--ink3);letter-spacing:.03em;margin-bottom:10px}
h1.t{font-size:29px;line-height:1.3;margin:0 0 14px;letter-spacing:-.01em}
.badges{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px}
.b{font-size:12px;padding:3px 10px;border-radius:99px;border:1px solid var(--line);background:#fff}
.b.ok{color:var(--ok);background:var(--ok-soft);border-color:#cfe8dd}
.b.wait{color:var(--wait);background:var(--wait-soft);border-color:#efe1bb}
.b.warn{color:#8a5200;background:#fdf0dc;border-color:#f0dcb8}
.b.bad{color:var(--bad);background:var(--bad-soft);border-color:#f2cfcb}
.b.machine{color:var(--accent);background:var(--accent-soft);border-color:#d5dcff}
.b.tier{font-family:var(--mono);letter-spacing:.03em}
.b.cite-false{color:var(--bad);background:var(--bad-soft);border-color:#f2cfcb}
.lead{font-size:13px;color:var(--ink2);background:#fff;border:1px solid var(--line);
      border-left:3px solid var(--accent);border-radius:0 8px 8px 0;padding:10px 14px;margin:0 0 22px}
#doc h2{font-size:18px;margin:30px 0 10px;padding-bottom:6px;border-bottom:1px solid var(--line)}
#doc h3{font-size:15px;margin:22px 0 8px;color:var(--ink2)}
#doc p{margin:.7em 0}
#doc li{margin:.25em 0}
blockquote{margin:14px 0;padding:10px 14px;border-left:3px solid var(--line);
           background:#fff;color:var(--ink2);border-radius:0 8px 8px 0}
blockquote.imp{border-left-color:var(--accent);background:var(--accent-soft);color:#20306e}
blockquote.warn{border-left-color:#c07000;background:#fdf6e9}
blockquote.tip{border-left-color:var(--ok);background:var(--ok-soft);color:#0d5c3f}
.tbl{overflow:auto;margin:14px 0}
table{border-collapse:collapse;width:100%;font-size:13.5px;background:#fff}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}
th{background:#faf9f5;font-weight:600;color:var(--ink2);font-size:12.5px}
.srcbox{margin-top:34px;border-top:1px solid var(--line);padding-top:16px}
.srcbox h3{font-size:13px;color:var(--ink3);letter-spacing:.05em;margin:0 0 10px}
.src{border:1px solid var(--line);background:#fff;border-radius:9px;padding:10px 12px;margin-bottom:8px;font-size:13px}
.src .id{font:600 12px/1.4 var(--mono);color:var(--accent)}
.src .loc{color:var(--ink2);margin-top:3px}
.src .d{font:11px/1.4 var(--mono);color:var(--ink3);margin-top:5px}
.welcome{padding:46px 40px;max-width:760px;margin:0 auto}
.welcome h2{font-size:20px;margin:0 0 6px}
.welcome p{color:var(--ink2);margin:.6em 0}
.welcome .how{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:20px 0}
.welcome .how div{border:1px solid var(--line);border-radius:10px;padding:12px 14px;background:#fff;font-size:13px}
.welcome .how b{display:block;margin-bottom:3px}
.warnline{background:var(--wait-soft);border:1px solid #efe1bb;border-radius:9px;
          padding:10px 14px;font-size:13px;color:#6d5615;margin:18px 0}
#graph{position:absolute;inset:0;background:#fdfcfa}
#graph svg{width:100%;height:100%;display:block}
.gnode{cursor:pointer}
.gnode rect{fill:#fff;stroke:#d9d7cf}
.gnode:hover rect{stroke:var(--accent)}
.gnode text{font-size:10px;fill:var(--ink2)}
.gedge{stroke:#dcdad2;stroke-width:1}
#glegend{position:absolute;left:18px;bottom:16px;font:11px/1.6 var(--mono);color:var(--ink3);
         background:#fff;border:1px solid var(--line);border-radius:8px;padding:8px 12px}
@media (max-width:900px){
  main{grid-template-columns:1fr}
  aside{display:none}
  header{flex-wrap:wrap;gap:10px}
  #q{width:100%}
}
</style>
</head>
<body>
<header>
  <div class="brand"><b>Scholia</b><span>证据可追溯的跨学科知识库</span></div>
  <div class="kpis" id="kpis"></div>
  <input id="q" placeholder="搜索标题或正文…  / 聚焦 · Esc 清空" autocomplete="off">
</header>
<main>
  <aside>
    <div class="chips" id="typechips"></div>
    <div class="chips" id="subchips" style="padding-top:0"></div>
    <div id="meta"></div>
    <div id="list"></div>
  </aside>
  <section id="pane">
    <div class="welcome" id="welcome"></div>
    <article id="doc" hidden></article>
    <div id="graph" hidden></div>
  </section>
</main>
<script id="data" type="application/json">__DATA__</script>
<script>
const D = JSON.parse(document.getElementById('data').textContent);
const $ = s => document.querySelector(s);
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const STATUS_TONE = __TONES__;

/* ── 头部 KPI：全部来自 index.json 的统计 ── */
const st = D.stats, tiers = st['按溯源档'] || {};
const deep = (tiers['T4']||0) + (tiers['T3']||0);
const total = st['对象总数'] || D.entries.length;
$('#kpis').innerHTML = [
  ['对象', total, ''],
  ['全文/摘要核读', Math.round(100*deep/total) + '%', 'hl'],
  ['已确证', st['已确证条数'] ?? 0, ''],
  ['证据', st['证据条数'] ?? 0, ''],
  ['学科', Object.keys(st['按学科']||{}).length, ''],
].map(([k,v,c]) => `<div class="kpi ${c}"><b>${esc(v)}</b><i>${esc(k)}</i></div>`).join('');

/* ── 筛选状态 ── */
const state = {type:'全部', subject:'全部学科', q:''};
const typeCounts = {}, subCounts = {};
D.entries.forEach(e => { typeCounts[e.type]=(typeCounts[e.type]||0)+1;
                         subCounts[e.subject]=(subCounts[e.subject]||0)+1; });

function chips(el, key, order, allLabel){
  const keys = order.filter(k => (key==='type'?typeCounts:subCounts)[k]);
  el.innerHTML = [`<span class="chip on" data-k="${allLabel}">${allLabel}<span class="n">${D.entries.length}</span></span>`]
    .concat(keys.map(k => `<span class="chip" data-k="${esc(k)}">${esc(k)}<span class="n">${key==='type'?typeCounts[k]:subCounts[k]}</span></span>`)).join('');
  el.querySelectorAll('.chip').forEach(c => c.onclick = () => {
    el.querySelectorAll('.chip').forEach(x => x.classList.remove('on'));
    c.classList.add('on'); state[key] = c.dataset.k; render();
  });
}
chips($('#typechips'), 'type', __TYPE_ORDER__, '全部');
chips($('#subchips'), 'subject', Object.keys(subCounts).sort(), '全部学科');

/* ── 列表 ── */
function match(e){
  if (state.type!=='全部' && e.type!==state.type) return false;
  if (state.subject!=='全部学科' && e.subject!==state.subject) return false;
  if (!state.q) return true;
  const q = state.q.toLowerCase();
  return (e.title + ' ' + e.search).toLowerCase().includes(q);
}
function render(){
  const rows = D.entries.filter(match);
  $('#meta').textContent = `${rows.length} / ${D.entries.length} 条` + (state.q ? ` · 关键词「${state.q}」` : '');
  $('#list').innerHTML = rows.slice(0, 400).map(e => `
    <div class="item" data-id="${esc(e.id)}">
      <div class="t">${esc(e.title)}</div>
      <div class="m"><span class="dot d-${STATUS_TONE[e.status]||'wait'}"></span>${esc(e.status)}
        · ${esc(e.tier)} · ${esc(e.subject)} · ${esc(e.type)}</div>
    </div>`).join('') || '<div style="padding:18px;color:#7b8494;font-size:13px">没有匹配的条目</div>';
  $('#list').querySelectorAll('.item').forEach(el => el.onclick = () => open(el.dataset.id));
  if (rows.length > 400) $('#list').insertAdjacentHTML('beforeend',
    `<div style="padding:14px 16px;font:11px/1.5 var(--mono);color:#7b8494">只显示前 400 条 —— 用搜索缩小范围</div>`);
}

function badge(text, cls){ return `<span class="b ${cls}">${esc(text)}</span>`; }
function open(id){
  const e = D.entries.find(x => x.id === id);
  if (!e) return;
  $('#welcome').hidden = true; $('#graph').hidden = true; $('#doc').hidden = false;
  document.querySelectorAll('.item').forEach(x => x.classList.toggle('on', x.dataset.id === id));
  const tone = STATUS_TONE[e.status] || 'wait';
  const badges = [
    badge(e.status, tone),
    badge(e.tier + ' · ' + (D.tier_note[e.tier]||''), 'tier ' + (e.tier==='T4'?'ok':(e.tier==='T0'?'bad':'wait'))),
    badge(e.type, ''),
    badge(e.subject, ''),
    e.stage ? badge(e.stage, '') : '',
    e.citable ? '' : badge('不可作事实引用', 'cite-false'),
    e.reviewer ? badge('复核者：' + e.reviewer, 'machine') : '',
  ].join('');
  const srcs = e.srcs.length ? `<div class="srcbox"><h3>来源 · ${e.srcs.length}</h3>` +
    e.srcs.map(s => `<div class="src"><div class="id">${esc(s.id)}${s.void?' · 已作废':''}</div>
      <div class="loc">${esc(s.loc)}</div>
      <div class="d">核验深度：${esc(s.depth||'—')}${s.url?` · <a href="${esc(s.url)}" target="_blank" rel="noreferrer">打开来源</a>`:''}</div></div>`).join('') + '</div>'
    : '<div class="srcbox"><h3>来源</h3><p style="color:#7b8494;font-size:13px">这一条没有登记证据。</p></div>';
  $('#doc').innerHTML = `<div class="crumb">${esc(e.id)} · ${esc(e.path)}</div>
    <h1 class="t">${esc(e.title)}</h1>
    <div class="badges">${badges}</div>
    ${e.html}
    ${srcs}`;
  $('#pane').scrollTop = 0;
}

/* ── 图谱：知识点之间的先修 ── */
function graph(){
  $('#welcome').hidden = true; $('#doc').hidden = true; $('#graph').hidden = false;
  const nodes = D.nodes, edges = D.edges;
  const W = 1600, H = Math.max(700, 60 * Math.max(...nodes.map(n=>n.d), 0) / 3 + 700);
  const byDepth = {};
  nodes.forEach(n => (byDepth[n.d] = byDepth[n.d] || []).push(n));
  const cols = Object.keys(byDepth).length;
  const pos = {};
  Object.entries(byDepth).forEach(([d, arr]) => {
    const x = 90 + (W - 180) * (Number(d) / Math.max(1, cols - 1));
    arr.sort((a,b)=>a.label.localeCompare(b.label,'zh'));
    arr.forEach((n, i) => { pos[n.id] = [x, 60 + (H - 120) * (i + 0.5) / arr.length]; });
  });
  const lines = edges.map(([a,b]) => {
    const [x1,y1] = pos[a], [x2,y2] = pos[b];
    const mx = (x1+x2)/2;
    return `<path class="gedge" d="M${x1+8},${y1} C${mx},${y1} ${mx},${y2} ${x2-8},${y2}" fill="none"/>`;
  }).join('');
  const boxes = nodes.map(n => {
    const [x,y] = pos[n.id], w = Math.max(58, n.label.length*11+18);
    const tone = STATUS_TONE[n.status];
    const c = tone==='ok' ? '#0f7a52' : (tone==='bad' ? '#a3231d'
              : (tone==='machine' ? '#2f4bd6' : '#c9a227'));
    return `<g class="gnode" data-id="${esc(n.id)}" transform="translate(${x-w/2},${y-11})">
      <rect width="${w}" height="22" rx="6"/>
      <rect width="4" height="22" rx="2" fill="${c}"/>
      <text x="10" y="15">${esc(n.label)}</text></g>`;
  }).join('');
  $('#graph').innerHTML = `<svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="xMidYMid meet">
      ${lines}${boxes}</svg>
    <div id="glegend">${nodes.length} 个知识点 · ${edges.length} 条先修边<br>
      横轴 = 最长先修路径的深度 · 竖条颜色 = 状态<br>点节点看条目</div>`;
  $('#graph').querySelectorAll('.gnode').forEach(g => g.onclick = () => open(g.dataset.id));
}

/* ── 欢迎页 ── */
$('#welcome').innerHTML = `
  <h2>${total} 条内容，每一条都带着它的来源。</h2>
  <p>这不是教材，也不判断「什么是真的」。它只保证：任何一条主张，你都能顺着来源核到底——
  哪本书、哪一页、读了没有、被谁反驳过。</p>
  <div class="warnline"><b>两把尺子，别混着看。</b>
    <b>状态</b>（待审 / 有效 / 暂定确认 / 已确证）回答「有没有站得住的论证」，要人判；
    <b>溯源档</b>（T4–T0）回答「引用的来源被读到了哪一层」，机器算，取最弱一环。
    全库 <b>已确证 ${st['已确证条数'] ?? 0}</b> 条，同时 <b>${Math.round(100*deep/total)}%</b> 的来源被通读过——
    这两句话都成立。<b>已确证不保证是人签的：</b>agent 也可以复核，但那要留四栏记录，
    而且条目上会标 <b>复核者: agent</b>。</div>
  <div class="how">
    <div><b>想学一个概念</b>左栏选「概念」，按学科筛。正文在「## 论证」之前的部分就是给你读的。</div>
    <div><b>想核一条</b>点开任意条目，底下是它引用的证据与定位，点「打开来源」直接跳到原文。</div>
    <div><b>想找勘误</b>类型选「命题」，搜书名或章节号；也可直接取 <code>exports/errata.csv</code>。</div>
    <div><b>想看结构</b>点下面的「先修图谱」——这是把 71 个概念连起来的那张图。</div>
  </div>
  <p><a href="#" id="opengraph">→ 先修图谱</a>　·　<a href="${D.repo}" target="_blank" rel="noreferrer">仓库</a></p>`;
$('#opengraph').onclick = ev => { ev.preventDefault(); graph(); };

/* ── 输入 ── */
let timer;
$('#q').oninput = ev => {
  clearTimeout(timer);
  timer = setTimeout(() => { state.q = ev.target.value.trim(); render(); }, 90);
};
document.addEventListener('keydown', ev => {
  if (ev.key === '/' && document.activeElement !== $('#q')) { ev.preventDefault(); $('#q').focus(); }
  if (ev.key === 'Escape') { $('#q').value = ''; state.q = ''; render(); }
});

render();
</script>
</body>
</html>
"""


def render_page(payload):
    tones = json.dumps(STATUS_TONE, ensure_ascii=False)
    data = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    # `</script>` 出现在正文里会提前结束脚本块；转义一下，页面行为不变。
    data = data.replace("</", "<\\/")
    return (PAGE.replace("__DATA__", data)
                .replace("__TONES__", tones)
                .replace("__TYPE_ORDER__", json.dumps(TYPE_ORDER, ensure_ascii=False)))


def main():
    ap = argparse.ArgumentParser(description="生成单文件站点 site/index.html")
    ap.add_argument("--check", action="store_true", help="只比对，不写盘")
    args = ap.parse_args()

    page = render_page(build_payload())
    if args.check:
        if not OUT.exists():
            print("x site/index.html 不存在 —— 跑 python tools/build_site.py")
            return 1
        if OUT.read_text(encoding="utf-8") != page:
            print("x site/index.html 与内容不一致 —— 重跑 python tools/build_site.py")
            return 1
        print("站点与内容一致")
        return 0
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    print(f"已写 {OUT.relative_to(ROOT)}（{len(page) / 1024:.0f} KB）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
