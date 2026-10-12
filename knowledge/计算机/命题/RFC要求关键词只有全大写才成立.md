---
id: kb:computing:prop-rfc-keywords-require-uppercase
type: 命题
title: RFC 里的 MUST / SHOULD / MAY 只在全大写时才有规范含义
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「这份 RFC 里的 must / should 算不算规范要求」时
  条件: "**适用于 BCP 14 组合（RFC 2119 + RFC 8174）**；本条只陈述 BCP 14 的规定，**不判断任何具体 RFC 的合规性**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-052, ev-053]
license: CC-BY-SA-4.0
---

## 陈述

IETF 的 **BCP 14** 由两份文档组成：**RFC 2119**（1997）定义五条关键词，
**RFC 8174**（2017）补上大小写限定。合起来的规定是：

> The words have the meanings specified herein **only when they are in all capitals**.
> When these words are **not capitalized**, they have their **normal English meanings**
> and are not affected by this document.（RFC 8174 §2）

RFC 9110 §2.2 引用这条规定时的写法：

> …interpreted as described in BCP 14 [RFC2119] [RFC8174] **when, and only when,
> they appear in all capitals**, as shown here.（RFC 9110 §2.2）

五条关键词的强度（RFC 2119 §1–§5）：

| 关键词 | 强度 | 定义要点（短引用） |
|---|---|---|
| `MUST` / `MUST NOT` | **绝对** | "an **absolute requirement**" / "an **absolute prohibition**" |
| `SHOULD` / `SHOULD NOT` | **有条件可偏离** | 允许忽略，但 "**the full implications must be understood and carefully weighed**" |
| `MAY` | **真正可选** | "an item is **truly optional**"；实现间仍须准备互操作 |

> [!IMPORTANT]
> **规范里的小写 must 不是要求，小写 should 不是建议。**
>
> RFC 8174 说得更绝：这些词 "**can be used as defined here, but using them is not
> required**"，"**a lot of normative text does not use them and is still normative**"。
>
> 换句话说：**大写不是「规范性」的必要条件，小写也不是「非规范性」的标志**。
> 判断一段话是不是要求，看的是**它在规范里的位置与措辞**，
> **不是这几个词的大小写**。

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-052 | **官方文件** | **高** | [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.txt)，BCP 14，1997-03，**§1–§5** | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |
| ev-053 | **官方文件** | **高** | [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.txt)，BCP 14，2017-05，**§2**（OLD / NEW 对照） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 规定本身写明了大小写条件（尚无攻击）

- **主张**：RFC 里的这组关键词**只在全大写时**有规范含义
- **前提**：RFC 8174 §2 用 "**only when they are in all capitals**" 与
  "**not capitalized … normal English meanings**" 两句把两种情况分开；
  RFC 9110 §2.2 采纳了新写法 "when, and only when, they appear in all capitals"（ev-053, ev-054）
- **推理**：
  1. 这属于「**规范规定了什么**」——正是[计算机](../README.md)学科收的东西
  2. 它**可被读者逐条证伪**：点开两份 RFC 的 §2 与 §2.2 即可
  3. RFC 8174 的存在本身证明**这个问题曾经真的造成过混淆**——
     它的标题就叫 "Ambiguity of Uppercase vs Lowercase"
- **证据**：ev-052, ev-053, ev-054
- **被攻击**：见 A2

### A2 · 本条只声明 BCP 14 的规定，不判断任何具体 RFC（尚无攻击）

- **主张**：本条声明的是「**BCP 14 这么规定**」，**不声明「某份 RFC 的某句话因此无效」**
- **前提**：RFC 8174 自己说了，规范性文本 "**does not require the use of these key words**"，
  不用它们也仍然是规范性的（ev-053）
- **推理**：
  1. 也就是说：**小写 must 不构成要求，但那句话本身可能仍然是要求**——
     要看它在规范里的位置与措辞，不能只看大小写
  2. 判断「某句话是不是要求」**需要通读该 RFC 的上下文**，
     本库**没有做过这种逐句判断**
  3. 所以本条**不能被用来支持「RFC 9110 里某句小写 must 可以忽略」**
- **证据**: ev-053
- **被攻击**：**本库没有核对任何一份具体 RFC 里小写 must 的实际用法**。
  「某份 RFC 里的小写 must 到底是不是要求」——**这个问题本库一条都没查**。
  另外：**本库没有查 BCP 14 是否仍是 IETF 当前的 Best Current Practice**，
  也没有查是否有更新 RFC 2119 或 8174 的后续文档。
- **署名**：@hpleapfrog · 2026-10-12
- **待补**：RFC Editor 上 BCP 14 的当前状态；至少一份具体 RFC 里小写 must 的实例分析

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **规范的正文里不会写「这几个词要大写才算数」——那句话在另一份 RFC 里。**
>
> 你在读一份 RFC 时，眼前能看到的是 **一段带 must 的话**；
> 规范里写的是 **两份文档共同决定这句话的强度**。
>
> **本库的使命是「去除噪音、存放真实信息」。**
> 这个对比就是判据：**眼前这段话的字面，本库不必重复；
> 眼前看不到而标准写明的，才是本库该装的。**
> 「这句话到底是不是硬性要求」——这个问题在任何一份 RFC 的正文里都找不到答案，
> 而 BCP 14 把它写成了一个可查的规定。

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-12 | 建立条目；**本学科第一条 `命题`**，也是 `计算机` 学科的第二条对象 | ev-052 与 ev-053 登记入库后按学科边界选题 | @hpleapfrog |
