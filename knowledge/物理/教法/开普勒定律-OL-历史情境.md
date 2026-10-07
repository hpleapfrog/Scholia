---
id: kb:physics:method-kepler-ol-historical-context
type: 教法
title: 开普勒定律 · 年级水平：把「手工算了多少」讲出来
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  适用: 已能使用 r³/T²，但把定律当成「公式」的学生
  条件: 无
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[开普勒定律](../知识点/开普勒定律.md)"]
evidence: [ev-031]
license: CC-BY-SA-4.0
---

## 做法

教材把这一节的 `[OL]` 教学提示**大部分放在「历史情境」上**，而不是放在公式上。

### 一、讲清开普勒当时领先到什么程度

> `Discuss the historical setting in which Kepler worked. Most people still thought Earth was the
> center of the universe, and yet Kepler not only knew that the planets circled the sun,
> he found patterns in the paths they followed. What would it be like to be that far ahead of
> almost everyone?`

教材还点名了一个可用的叙事资源（《宇宙》第三集）。

### 二、让他「手工算」的量级可感

> `Impress upon the students that Kepler had to crunch an enormous amount of data and that
> all his calculations had to be done by hand. Ask students to think of similar projects where
> scientists found order in a daunting amount of data (the periodic table, DNA structure,
> climate models, etc.).`

### 三、动手画椭圆（图钉与绳）

教材给出**图钉 + 绳**画椭圆的方法，并追问：

> `Why does the string and pin method create a shape that conforms to Kepler's second law?
> That is, why is the shape an ellipse?`

### 四、一条最容易漏的适用范围（`[OL]`）

> `Emphasize that this approach only works for two satellites orbiting the same parent body.
> The parent body must be the same because r²/T² = GM/(4π²) and M is the mass of the parent body.
> If M changes, the ratio r³/T² also changes.`

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **OL**（教材标记 `[OL]`） |
| 先修 | 能代入 `r³/T²` 做比较；知道椭圆的长轴 / 短轴 / 焦点 |
| 教具 | 图钉 + 绳 + 铅笔（低成本，可课堂或带回家） |
| 认知负荷 | 中——负荷放在**把公式还原成一件发生过的事** |

## 禁忌

**对谁不适用？**

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| 还不知道「同一中心天体」这一限制的学生 | 教材专门强调 `only works for two satellites orbiting the same parent body`——**不点明就会跨天体乱比** | **强**（教材明示 `Emphasize`） |
| 只想快速拿公式解题的学生 | 本做法花在历史上的时间**不产出解题能力**，考试导向的短课时里性价比低 | **中** —— 由做法性质推出 |
| 本档以外的学生 | 教材为各档**另给了不同做法**，未声明本做法可跨档 | **弱** —— 未经检验 |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 历史讲成故事会 | 教材的落点是**「他领先于几乎所有人」**与**「手工算」**，都指向一件事：**这条定律的得出代价极大**。跑偏成轶事就丢了这个功能 |
| 图钉绳画椭圆只动手不追问 | 教材明确要问「**为什么这个画法得到的是椭圆**」。只画不问就退化成手工课 |
| `r³/T²` 跨天体乱用 | 这是本节**最容易犯的实质错误**。教材用 `Emphasize` 标出，说明它预期学生会犯 |
| 「面积定律」讲成「速度不变」 | 教材的表述是**相等时间扫过相等面积**，而**速度与距离都在变** |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-031 | 教材（全文） | 低 | OpenStax《Physics》第 7 章 · Kepler's Laws of Planetary Motion，[m54192](https://github.com/openstax/osbooks-physics/blob/main/modules/m54192/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 OL 档指定（尚无攻击）

- **主张**：这是教材为年级水平学生指定的做法
- **前提**：m54192 的 Teacher Support 用 `[OL]` 标记上述各条（ev-031）
- **推理**：分档标记即教材对该水平的指定
- **证据**：ev-031
- **被攻击**：**「教材指定」≠「实测有效」**；教材给的历史叙事资源（《宇宙》）与课时成本未评估
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（#8 批量转换 · 第 2 批） | Issue #8 | @hpleapfrog |
