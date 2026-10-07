---
id: kb:physics:method-refraction-bl-geometry
type: 教法
title: 折射 · 低于年级水平：先补几何，再推 n > 1
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 初中 / 高中
  水平档: 低于年级水平（BL）
  适用: 角的概念不牢、或用公式时只代数字不看含义的学生
  条件: 无
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[光的折射](../知识点/光的折射.md)"]
evidence: [ev-038]
license: CC-BY-SA-4.0
---

## 做法

教材的 `[BL]` 提示**不碰折射定律**，只补两件更靠前的事。

### 一、先把「角」说清

> `An angle is the measure of the separation of two lines or rays originating from a single`
> `point. The length of the lines is not relevant.`

**最后那句是关键**：学生画示意图时会把「角的大小」和「线画多长」联系起来。
教材把这一点单独拎出来否定。

> [!IMPORTANT]
> **这条提示在「光的反射」模块里也出现过一次**（ev-026），措辞不同、内容相同。
>
> | 模块 | 原话 |
> |---|---|
> | 反射（m54357） | `angles are numbers that tell how far two straight lines are spread apart` |
> | **折射（m54365）** | `An angle is the measure of the separation of two lines or rays originating from a single point` |
>
> **教材在两个地方各讲了一遍同一件事。** 这是「几何的角」是一个**真实且反复出现的前置**的证据
> （也是本库缺这个节点的证据，见 [光的折射](../知识点/光的折射.md)）。

### 二、`n > 1` 要**推**出来，不要背

> `Be sure students understand that if c is always greater than v, n must always be greater`
> `than one. Demonstrating division using numbers that can be divided easily can reinforce`
> `student understanding.`

**做法有两步**：

1. **逻辑**：光在真空里最快 ⇒ `c > v` ⇒ `c / v > 1`
2. **算例**：**特意挑能整除的数**做除法，让学生自己看到 `n` 总是大于 1

**第二步的设计是刻意的**——「能整除」意味着**学生不必分心算算术**，
注意力全在「结果比 1 大」上。

### 三、一个方程三个量，知道两个就够

> `If an equation has two variables and a constant, such as n=c/v, the value of only one`
> `variable is needed to find the other.`

**这是在补「解方程」这一层**：`n = c / v` 里有三个符号，但 `c` 是常数，
所以**只要一个变量就能求另一个**。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **BL**（教材标记 `[BL]`） |
| 先修 | 角的概念（**本库尚无对应节点**）；能做法是除法 |
| 认知负荷 | 低——教材刻意**避开折射定律**，只补前置 |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| 已经能熟练使用折射定律的学生 | 本做法**不做折射定律**，对他们是纯粹的时间浪费 | **强**——由做法性质推出 |
| 本档（BL）**以外**的学生 | 教材为该段落标的就是 `[BL]`；OL 与 AL 档另给了不同建议 | **中**——标签明确划了范围，但「未标」仍不等于「不适用」，只是**未经检验** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 「角与线段长度无关」只讲不讲反例 | 学生画图时**仍然**会犯。教材专门否定这一条，说明它预期学生已经这么想了 |
| `n > 1` 讲成「记住折射率都大于 1」 | 教材的措辞是 `Be sure students understand that **if** c is always greater than v, **then** …`——**是一个推理，不是一个事实** |
| 应付了事地做「能整除」的算例 | 特意挑能整除的数是**为了把注意力留在结论上**。换成难算的数就把这一步毁了 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-038 | 教材（全文） | 低 | OpenStax《Physics》第 16 章 · Refraction，[m54365](https://github.com/openstax/osbooks-physics/blob/main/modules/m54365/index.cnxml) | **CC BY 4.0** |
| ev-026 | 教材（全文） | 低 | OpenStax《Physics》第 16 章 · Reflection，[m54357](https://github.com/openstax/osbooks-physics/blob/main/modules/m54357/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 BL 档指定（尚无攻击）

- **主张**：这是教材为低于年级水平学生指定的做法
- **前提**：m54365 的 Teacher Support 用 `[BL]` 标记上述各条（ev-038）
- **推理**：分档标记即教材对该段落的指定
- **证据**：ev-038、ev-026
- **被攻击**：**「教材指定」≠「实测有效」**；
  且两条证据**同属一家出版社**，按 `FORMAT.md` §6 **不是独立证据**
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（#8 批量转换 · 第 4 批） | Issue #8 | @hpleapfrog |
