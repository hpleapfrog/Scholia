# AGENTS.md — 给 AI agent 的入口

> 本文件写给**在本仓库里工作的 AI agent**（编码 agent、LLM agent）。
> 人类贡献者请读 [CONTRIBUTING.md](CONTRIBUTING.md)；只想读内容的人请读 [START.md](START.md)。
>
> **English:** Instructions for AI agents working **inside** this repository.
> Human contributors → [CONTRIBUTING.md](CONTRIBUTING.md); readers → [START.md](START.md).

---

## 一、这个库是什么 / What this is

一个**证据可追溯**的跨学科知识库。每条内容都带**来源**、**状态**与**反驳**；
"什么是真的"由证据等级 + 反驳关系**按规则算出**，不靠投票。

**English:** A cross-disciplinary, source-traceable knowledge base. Every entry
carries its source, status, and rebuttals; truth is computed from evidence grade +
rebuttal structure by rules, never by vote.

## 二、你可以怎么用这个库 / How to consume it

| 方式 / How | 入口 / Entry |
|---|---|
| 机器可读的全部对象 | [index.json](index.json)（**生成物，勿手改**） |
| AI 读取约定（状态、能不能引用） | [llms.txt](llms.txt) |
| **MCP server**（可直接挂到 agent） | [`tools/scholia_mcp.py`](tools/scholia_mcp.py) |

**挂在 agent 上 / Wire it as an MCP server:**

```json
{
  "mcpServers": {
    "scholia": { "command": "python", "args": ["tools/scholia_mcp.py"] }
  }
}
```

提供的只读工具 / read-only tools: `scholia_stats` · `scholia_search` ·
`scholia_list` · `scholia_get_object` · `scholia_get_evidence` · `scholia_rules`。

> **引用任何一条时**：连 `status` 与 `来源` 一起给；**`可作事实引用=false`（失据/已推翻/已失效）的不要引用**；
> 医学条目要把 `适用` / `条件` 连同内容一起给。详见 [llms.txt](llms.txt)。

## 三、你在这个仓库里改东西时 / If you edit here

**改完必须跑校验：**

```bash
python tools/kbcheck.py                 # 必须通过
python tools/kbcheck.py --write-index   # 若改了内容：重生成 index.json 与文档生成块
```

铁律 / hard rules:

1. **`index.json` 与文档里的 `<!-- kbcheck:begin --> … <!-- kbcheck:end -->` 是生成物**——手改会被校验判失败。改它们只能靠 `--write-index`。
2. **一个知识点 = 一个 `.md`**；`front-matter` 11 个字段必填（**知识对象**；`事件` 单开顶层 `events/`，用另一套 9 字段、**无论证、无任何边**，见 [FORMAT.md](FORMAT.md) §4「`事件`」）；正文第一行、状态、水平档、医学免责块等见 [FORMAT.md](FORMAT.md)。
3. **改规则要同时改检查**：规则清单在 [`docs/RULES.md`](docs/RULES.md)（由脚本里的 `RULES` 生成）与 [`tools/kbcheck.py`](tools/kbcheck.py) 的检查函数。加规则须有**会失败的注入样本**（见 CONTRIBUTING「新规则入库门槛」）。
4. **不写死会漂移的数字**（统计数字一律由脚本生成）。
5. **不上传教材原文或扫描页**——只存定位、短引用、原创摘要。
6. **AI 可以当攻击方，不能当 `已确证` 的复核者**（见 [FORMAT.md](FORMAT.md) §6）。
7. **新增条目先用脚手架起手**：`python tools/new_entry.py --type <类型> --subject <学科> --slug <slug> --title "<标题>"`
   —— 骨架来自 [`templates/`](templates/README.md)。**结构交给脚本，内容留给你**；
   生完立刻跑 `kbcheck`，它报的错就是待办清单。

**English:** After editing, always run `kbcheck` (and `--write-index` for content
changes). `index.json` and the marked generated blocks are outputs — never hand-edit.
One concept = one `.md`; 11 required front-matter fields; rules live in
`docs/RULES.md` + the check functions; never hard-code drifting numbers; never upload
textbook text/scans; AI may attack, never be the independent reviewer for `已确证`.

## 四、语言 / Language

**本库文档中英对照。** 每条内容先中文、后英文；引文保留原文并配中文说明。

**English:** Documentation is bilingual (Chinese first, then English); quotations keep
the original text with a Chinese gloss.
