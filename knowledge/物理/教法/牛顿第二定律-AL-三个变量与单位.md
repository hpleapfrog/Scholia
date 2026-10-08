---
id: kb:physics:method-newton2-al-three-vars
type: 教法
title: 牛顿第二定律 · 进阶：三个变量分别解，与两个混淆
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: 已经会代 F = ma、但不能把它当关系式看的学生
  条件: 已学过单位换算；知道重力的概念
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[牛顿第二定律](../知识点/牛顿第二定律.md)"]
evidence: [ev-040]
license: CC-BY-SA-4.0
---

## 做法

### 一、把方程对三个变量分别解一遍

> `Write the equation for Newton's second law and show how it can be solved for all three`
> `variables, F, m, and a. Explain the practical implications for each case.`
> `Ask students how the other two variables would behave if one quantity is held constant.`

**关键在最后一句**：「如果其中一个量保持不变，另外两个会怎样」——
**这一步把等式变成关系**。

### 二、点出「等于」与「成正比」的区别

> `Students might confuse the terms equal and proportional.`

**这不只是措辞问题**：

| 说法 | 说得通吗 |
|---|---|
| `F` **等于** `ma` | ✅ 对**同一个物体**恒成立（这是定义式） |
| `a` **正比于** `F` | ⚠️ **只有在 `m` 不变时才成立** |
| `a` **反比于** `m` | ⚠️ **只有在 `F` 不变时才成立** |

**只写「`F = ma` 所以 `a` 与 `F` 成正比」而不声明 `m` 不变，是错的。**

### 三、用宇航员问出「重量是力」

> `Ask students if they think an astronaut weighs the same on the moon as they do on Earth.`
> `Talk about the difference between mass and weight.`

**教材把这个问题和另一条提示里的混淆绑在一起**：

> `Students might confuse weight, which is a force, and g, which is the acceleration due to gravity.`

| | 是什么 | 在月球上 |
|---|---|---|
| **质量** `m` | 惯性的量度 | **不变** |
| **重量** `mg` | **一个力** | **变小**（`g` 小） |
| `g` | **重力加速度** | **变小** |

**宇航员的「体重」变了，质量没变**——而 `F = ma` 里的 `m` 是**质量**。

### 四、先复习单位换算

> `Review how to convert between units.`

（`[BL]` 档给的就是这一条——**AL 档的做法也建立在它上面**。）

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **AL**（教材标记 `[AL]`） |
| 先修 | 单位换算；质量与重量的区别（**这正是本条要讲的东西**——教材把它当 AL 内容） |
| 认知负荷 | 中——难点在**把等式读成关系** |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **还不熟单位换算**的学生 | 教材把这个放在 `[BL]` 档，说明**它不是 AL 的前提，而是更靠前的东西** | **强**（教材分了档） |
| 还没建立「力」这个概念的**矢量**含义的学生 | 「合力」的方向决定了加速度的方向，而这条 `[AL]` 提示**不处理矢量** | **中** |
| 本档（AL）**以外**的学生 | 教材为该段落标的就是 `[AL]`；OL 档另给了不同建议 | **中**——标签明确划了范围，但「未标」仍不等于「不适用」，只是**未经检验** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 「`a` 与 `F` 成正比」不说条件 | **这正是教材点名的混淆**。`a ∝ F` 必须挂在「`m` 不变」上 |
| 重量与质量只讲一遍 | 教材**在同一节的 AL 档里出现了两次**（混淆提示 + 宇航员追问），说明它预期学生会混 |
| 三个变量分别解变成三条公式 | 教材的落点是 `Ask students how the other two variables would behave if one quantity is held constant`——**变量之间的关系**，不是三个孤立式子 |
| 把 `g` 与 `G` 也一起讲混 | 本条处理的是**重量（力）与 `g`（加速度）**；`G`（引力常数）是另一件事（见 [混淆 G 与 g](../误解/混淆G与g.md)）。**两者一起讲容易被学生合成一锅** |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-040 | 教材（全文） | 低 | OpenStax《Physics》第 4 章 · Newton's Second Law of Motion，[m54142](https://github.com/openstax/osbooks-physics/blob/main/modules/m54142/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 AL 档指定（尚无攻击）

- **主张**：这是教材为进阶学生指定的做法
- **前提**：m54142 的 Teacher Support 用 `[AL]` 标记上述内容（ev-040）
- **推理**：分档标记即教材对该段落的指定
- **证据**：ev-040
- **被攻击**：**「教材指定」≠「实测有效」**；
  且教材的 AL 提示**只有三段话**，本条的「做法」一节把散在提示与相邻模块里的内容组织了起来，
  **这层组织是本库加的，不是教材的**——这一点必须让读者看见
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（#8 批量转换 · 第 5 批） | Issue #8 | @hpleapfrog |
