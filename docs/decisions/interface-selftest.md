# 接口自检：`kbcheck` 看不见的那一半

> **English → [interface-selftest.en.md](interface-selftest.en.md)**

> 定于 **2026-10-30**。命令是 `python tools/selftest.py`；这里记**为什么**要单独有它。

## 原来的样子

CI 跑两条命令：

| 命令 | 查什么 |
|---|---|
| `tools/kbcheck.py` | **内容**：front-matter、链接、证据、图关系、生成物一致性 |
| `tools/verify_rules.py` | **规则**：每条机械规则有没有一个会失败的注入样本 |

两条都很有用，但它们都**不运行**另外三个接口：

| 接口 | 谁在用 | 坏了会怎样 |
|---|---|---|
| `tools/scholia_mcp.py` | 把库挂到 agent 上的人 | 握手成功，工具一调就崩 |
| `tools/make_tasks.py --json` | 想接脚本 / 派活的人 | 输出的 JSON 解析不了 |
| `tools/new_entry.py` | 想加第一条内容的新人 | 生成的骨架缺字段，第一次跑 `kbcheck` 满屏红 |

> **2026-11-01 补记**：后来加入 `tools/review_packet.py`（把复核材料摆到一页）——
> 它是第四个接口，`selftest` 现在有九条检查。本节保留当时「三个接口」的原始范围。

## 为什么 `kbcheck` 看不见

因为它查的是**磁盘上的内容**，不是**别人调用时的行为**。

最刺眼的一处：MCP server 的 `tools/call` 把异常**吞掉**了——

```python
except Exception as e:
    text = f"error: {e}"
return {"content": [{"type": "text", "text": text}], "isError": False}
```

这是有意的（一个工具出错不该杀死整个会话），但它意味着：**一个坏掉的工具，在朴素客户端看来
是一次成功的调用**。`kbcheck` 永远不会走到这段代码，所以 CI 可以全绿，而 agent 拿到的是
一行 `error: ...` 文本。

## 改成什么

`tools/selftest.py`：**九条检查，真的起进程，不 import 函数**。

| 检查 | 证明了什么 |
|---|---|
| `generated_files` | 三份生成物自洽：路径都存在、`title_en` 与 `path_en` 同进同退、引用 id 不悬空 |
| `gaps_determinism` | `compute()` 跑两次结果相同；每组「数量」等于「条目数」；`review` + `review-blocked` 恰好等于全部 `待审` |
| `gaps_pages_in_sync` | `docs/GAPS.md` / `.en.md` 的每个数字都与 `compute()` 一致，页面上的 id 都真实存在 |
| `make_tasks_json` | `--json` 能解析、顶层结构齐全、数字与 `compute()` 一致；人类可读模式不漏组 |
| `new_entry_scaffold` | 在**临时目录**里生成一条，11 个字段与必备小节齐全；坏 slug / 缺 subject / 覆盖已有文件都被拒绝 |
| `mcp_handshake_and_readonly` | `initialize` / `ping` / `tools/list` 正常；9 个工具齐全；跑完三份机器文件**哈希不变** |
| `mcp_tools_callable` | 9 个工具逐个调用，返回可用载荷；`content` 不含 `## 论证`；未知工具报错而不是静默 |
| `mcp_print_config` | `--print-config` 打出的 JSON 能解析，路径确实指向 server |
| `review_packet` | `tools/review_packet.py` 为一条真实待审条目生成材料：含 id、来源、证据、三个问题与 `M-07` 警告；`--out` 只写一个文件 |

`mcp_tools_callable` 里有一处**故意写死**：工具名集合必须**恰好等于**那九个。
多一个、少一个都会失败——加工具的人因此必须同时改自检与文档，而不是让测试悄悄适应新现实。
同理，`review_packet` 检查**不替人回答**那三个问题：它只断言材料齐全，断言不了复核结论。

## 一条设计选择：起进程，不 import

import 函数只能证明「模块能加载」。真正会坏的是：

- stdio 握手（换行分隔的 JSON-RPC，少一个 `flush` 就卡死）；
- `--json` 的输出被某句 `print` 污染（人类可读的提示混进 stdout，JSON 就解析不了）；
- `new_entry` 依赖当前工作目录（在仓库里测会**写进仓库**，只能去临时目录）。

所以自检用 `subprocess` 起真的解释器，`new_entry` 在 `tempfile.mkdtemp()` 里跑，
MCP 通过管道一问一答。代价是慢一点——**本机约 3 秒**（数字随机器变化，别当基准），
仍然比一次全量 `verify_rules` 快。

## 代价（不粉饰）

1. **它知道接口的形状。** 工具名、JSON 顶层键、11 个必填字段，都在自检里出现了一次。
   这是有意的重复：接口变了，自检就该红。
2. **它不判断内容对不对。** 论证站不站得住、证据可不可靠，仍然归 `kbcheck` 与人的复核。
3. **它只覆盖「调用一次」的路径。** 并发调用、超大 `limit`、恶意输入都不在范围内。

## 没做的

- **没有完整的 MCP 协议一致性测试。** 只测 `initialize` / `ping` / `tools/list` / `tools/call`，
  没有测通知、取消、分页。
- **CI 只在 Ubuntu 上跑。** 本地在 Windows 上验证过（路径分隔符、控制台编码都踩过），
  但没有 Windows runner。
- **不测工具描述是否准确。** 描述是给人看的，机器只能测它存在。
