# `水平档` 的展开式是推断，不是引用

> 规则见 [FORMAT.md](../../FORMAT.md)「`水平档` 记什么」。

## 四个缩写在教材里没有图例

实测（脚本与明细见 [`evidence/os-teacher-markers.py`](../../evidence/os-teacher-markers.py)）：

- `Below Level` 全书**只出现一次**（且是在散文里）；
- `Advanced Learners` **一次都没有**；
- 只有 `English Learners` 有旁证（m54057 里 `[BL][EL]` 后紧跟 `English learners may need…`）。

> **所以「`[BL]` = 低于年级水平」是对常见教育缩写的推断，不是引用。**
> **本库的 `(知识点 × 水平档)` 模型建立在这个推断上。**

## `[EL]` 不是水平档

**`[EL]`（English Learners）不是水平档，是语言身份**，不要与其他三个并列为「分档标记」。

## 统计口径必须连同规则与 commit 给出

同一份源文件，两种口径结果不同：

| 口径 | 含义 | 结果 |
|---|---|---|
| **宽松** | `os-teacher` note 文本里出现该字符串 | 648（BL 207 / OL 245 / AL 191 / EL 5） |
| **严格** | 标记是 `<para>` 开头的连续 `<span>` | 637（EL **0**——它常是裸文本） |

> 教训与 `ev-020` 相同：**写死一个会漂移的数字，等于把它变成断言。** 数字要连同规则 + commit 一起给。
