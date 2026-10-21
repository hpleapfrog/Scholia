---
id: kb:computing:json-utf8-no-bom
type: 命题
title: 系统之间交换的 JSON 必须用 UTF-8（封闭生态除外），网络传输不得添加 BOM
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 计算机 · 格式与编码规范
  学段: 不限
  适用: 想核对「JSON 到底该用什么编码」「BOM 能不能加」「解析器能读 BOM 是否等于允许发送」时
  条件: "**适用于 RFC 8259（STD 90，Standards Track，2017-12，DOI 10.17487/RFC8259）§8.1 原文**；本条只主张**系统之间的交换**与**网络传输**这两个场景，**不主张**解析器必须接受或拒绝哪一种字节序列，也**不主张**封闭生态内部该用什么编码（§8.1 对该情形不作规定）"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-154]
license: CC-BY-SA-4.0
---

## 陈述

**系统之间、且不属于封闭生态的 JSON 交换必须用 UTF-8；网络传输的 JSON 不得在开头添加 BOM——但解析器可以选择忽略它。这两条都是带范围的规范要求，不是「JSON 一律 UTF-8、任何 BOM 都非法」的全称判断。**

| 场景 | 规范怎么说 | 出处 |
|---|---|---|
| 系统之间、**非封闭生态**的交换 | **必须**用 UTF-8 编码 | §8.1 第一句 |
| **网络传输**的 JSON 文本 | 实现**不得**在开头添加 BOM（U+FEFF） | §8.1 第二段 |
| 解析 JSON 文本 | 实现**可以**忽略 BOM，而不把它当成错误 | §8.1 第二段 |
| **封闭生态内部**的交换 | §8.1 **没有规定**编码；UTF-8 的 MUST 不适用 | §8.1 第一句的限定条件 |

逐条对应原文（短引用）：

编码要求，注意「非封闭生态」这个限定（§8.1）：

> JSON text exchanged between systems that are not part of a closed
> ecosystem MUST be encoded using UTF-8 [RFC3629].

规范给出的理由是互操作性，而不是「UTF-8 更先进」（§8.1）：

> Previous specifications of JSON have not required the use of UTF-8
> when transmitting JSON text.  However, the vast majority of JSON-
> based software implementations have chosen to use the UTF-8 encoding,
> to the extent that it is the only encoding that achieves
> interoperability.

BOM 禁令的范围是**网络传输**，而解析方的容忍是 MAY（§8.1）：

> Implementations MUST NOT add a byte order mark (U+FEFF) to the
> beginning of a networked-transmitted JSON text.  In the interests of
> interoperability, implementations that parse JSON texts MAY ignore
> the presence of a byte order mark rather than treating it as an
> error.

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-154 | 官方文件 | 高 | IETF / RFC Editor，**RFC 8259**《The JavaScript Object Notation (JSON) Data Interchange Format》（T. Bray, Ed., Textuality），STD 90，Standards Track，2017-12，DOI 10.17487/RFC8259，**§1–§14 与附录 A 全文已核**（899 行 / 28,360 字节，SHA-256 `61a5378f…d2d7`） | 官方公开规范（IETF Trust · BCP 78 / Revised BSD 法律条款）· **仅引用条款号与短引用，不转载全文** |

## 论证

### A1 · UTF-8 的要求带着一个未被定义的例外（尚无攻击）

- **主张**：「JSON 必须用 UTF-8」只在「系统之间、且不属于封闭生态」的交换里成立；§8.1 **没有定义**封闭生态的边界，也**没有说**封闭生态内部可以用 UTF-16 或 UTF-32
- **前提**：ev-154 §8.1 第一句的限定语「that are not part of a closed ecosystem」，以及同节第二段对互操作理由的说明；附录 A 只把这次修订概括为「require the use of UTF-8 when transmitted over a network」
- **推理**：规范把 UTF-8 的强制力**限定在互操作场景**，理由是「只有它达到互操作」。省略限定语，就会把一条条件命题读成全称命题；但反过来，也不能从「封闭生态被除外」推出「封闭生态内部用 UTF-16 就是规范认可的做法」——§8.1 对此保持沉默
- **证据**：ev-154
- **被攻击**：尚无攻击。**本条不主张封闭生态内部可以用任何特定编码**，只主张 UTF-8 的 MUST 不覆盖那里
- **署名**：@hpleapfrog · 2026-10-21

### A2 · BOM 的禁令与容忍不对称，且各有限定（尚无攻击）

- **主张**：发送方**不得**加 BOM（限**网络传输**的 JSON 文本），解析方**可以**忽略 BOM；解析器的容忍不构成对发送方的授权，也不能把禁令扩大到所有 JSON 文本
- **前提**：ev-154 §8.1 第二段的两句原文——主语分别是「实现（作为发送方）」与「实现（作为解析方）」，助动词分别是 MUST NOT 与 MAY
- **推理**：MAY 给的是**解析方**的选择权；它没有改变**发送方**的 MUST NOT。两个句子还各带范围：禁令只写 `networked-transmitted`，没有写「任何 JSON 文件」；因此「我的解析器能吃 BOM」与「我可以发 BOM」是两个不同的命题，后者即便在网络传输里也不成立
- **证据**：ev-154
- **被攻击**：尚无攻击。**本条不主张带 BOM 的本地文件一定解析失败**——那取决于实现，而不由 §8.1 决定
- **署名**：@hpleapfrog · 2026-10-21

## 怎么反驳它

- [ ] 找到 **RFC 8259 之后取代它**的规范（若有，本条 §8.1 的版本限定即失效）
- [ ] 给出一个「系统之间、非封闭生态」的交换实例，说明它合法地不用 UTF-8（§8.1 的 MUST 反例）
- [ ] 指出本条把「网络传输」的 BOM 禁令**扩大**到了所有 JSON 文本（本条只主张网络传输）
- [ ] 指出本条把解析器的「MAY 忽略」读成了「MUST 忽略」（那是另一条不成立的命题）

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-21 | 建立条目；核毕 RFC 8259 §1–§14 与附录 A 全文；登记 ev-154；按 §8.1 归集编码要求、BOM 禁令与解析容忍三条规则 | ev-154 | @hpleapfrog |
