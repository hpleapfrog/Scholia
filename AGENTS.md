# AGENTS.md — 给 AI agent 的入口

> English → [**AGENTS.en.md**](AGENTS.en.md)

> 本文件写给**在本仓库里工作的 AI agent**（编码 agent、LLM agent）。
> 人类贡献者请读 [CONTRIBUTING.md](CONTRIBUTING.md)；只想读内容的人请读 [START.md](START.md)。

---

## 一、这个库是什么

一个**证据可追溯**的跨学科知识库。每条内容都带**来源**、**状态**与**反驳**；
「什么是真的」由证据等级 + 反驳关系**按规则算出**，不靠投票。

## 二、你可以怎么用这个库

| 方式 | 入口 |
|---|---|
| 机器可读的三份文件 | [index.json](index.json)（导航）· [citations.json](citations.json)（按 id 取引用材料）· [evidence.json](evidence.json)（证据登记）——**均为生成物，勿手改** |
| AI 读取约定（状态、能不能引用、怎么省 token） | [llms.txt](llms.txt) |
| **还缺什么**（一页看全，生成物） | [docs/GAPS.md](docs/GAPS.md) · 要开工：`python tools/make_tasks.py --limit 3` |
| **要复核一条**（把来源、证据、三个问题摆到一页） | `python tools/review_packet.py --id <id>`——**只排版，不替你回答** |
| **MCP server**（可直接挂到 agent） | [`tools/scholia_mcp.py`](tools/scholia_mcp.py) |

**挂到 agent 上：**

```json
{
  "mcpServers": {
    "scholia": { "command": "python", "args": ["tools/scholia_mcp.py"] }
  }
}
```

提供的只读工具：`scholia_stats` · `scholia_search` · `scholia_list` · `scholia_get_object`
（`part="content"` 只取学习者半，`full` 才连论证）· `scholia_cite` · `scholia_get_evidence` ·
`scholia_external_prereqs`（按 `标识` 汇总库外前置）· `scholia_gaps`（机器数得出来的缺口，
与 `docs/GAPS.md` 同源）· `scholia_rules`。

> **引用任何一条时**：连 `status` 与 `来源` 一起给；**`可作事实引用=false`（失据/已推翻/已失效）的不要引用**；
> 医学条目要把 `适用` / `条件` 连同内容一起给。详见 [llms.txt](llms.txt)。

## 三、你在这个仓库里改东西时

**改完必须跑校验：**

```bash
python tools/kbcheck.py                 # 必须通过
python tools/kbcheck.py --write-index   # 若改了内容：重生成三份机器文件与文档生成块
python tools/verify_rules.py            # 改了规则：每条规则要有会失败的注入样本
python tools/selftest.py                # 改了 MCP / make_tasks / new_entry / review_packet：真的起进程跑一遍
python tools/quote_check.py <条目> --module <m#####>   # 动了英文引文：引文必须**真的在来源里**
python tools/evid.py next               # 要新编号：别自己数（编号是全局键，手数看不见别的分支）
```

铁律：

1. **`index.json` / `citations.json` / `evidence.json` 与文档里的 `<!-- kbcheck:begin --> … <!-- kbcheck:end -->` 是生成物**——手改会被校验判失败。改它们只能靠 `--write-index`。
   **三份各管一件事，别整读**：`index.json` 导航 · `citations.json` 按 id 取一条 · `evidence.json` 核出处。
2. **一个知识点 = 一个 `.md`**；`front-matter` 11 个字段必填（**知识对象**；`事件` 单开顶层 `events/`，用另一套 9 字段、**无论证、无任何边**，见 [FORMAT.md](FORMAT.md) §4「`事件`」）；正文第一行、状态、水平档、医学免责块等见 [FORMAT.md](FORMAT.md)。
   **英文译本的文件名由 `id` 派生**（`frame-of-reference.en.md`），**不要**写成「中文名 + `.en.md`」——
   那会让英文页顶着中文文件名（`R-BILING-01`，见 [FORMAT.md](FORMAT.md) §0）。
3. **改规则要同时改检查**：规则清单在 [`docs/RULES.md`](docs/RULES.md)（由脚本里的 `RULES` 生成）与 [`tools/kbcheck.py`](tools/kbcheck.py) 的检查函数。加规则须有**会失败的注入样本**，写进 [`tools/verify_rules.py`](tools/verify_rules.py)（见 CONTRIBUTING「新规则入库门槛」）。
4. **不写死会漂移的数字**（统计数字一律由脚本生成）。
5. **不上传教材原文或扫描页**——只存定位、短引用、原创摘要。
6. **AI 可以当攻击方，也可以当复核者，并能写 `已确证`**（见 [FORMAT.md](FORMAT.md) §6）。
   硬条件：`## 复核记录` 四栏齐全（模型 · 日期 · 引文核验 · 限制）**且**引用的每份证据都读到 `全文`；
   索引会给这条打上 `复核者: agent`，读者一眼看得到**不是人签的**。
   **「限制」一栏不许空**：说得出自己判不了什么，才配叫复核。
7. **新增条目先用脚手架起手**：`python tools/new_entry.py --type <类型> --subject <学科> --slug <slug> --title "<标题>"`
   —— 骨架来自 [`templates/`](templates/README.md)。**结构交给脚本，内容留给你**；
   生完立刻跑 `kbcheck`，它报的错就是待办清单。

## 四、语言

**本库文档中英对照**：`<name>.md` 中文、`<name>.en.md` 英文（含本文件）。
每条内容先中文、后英文；引文保留原文并配中文说明。
