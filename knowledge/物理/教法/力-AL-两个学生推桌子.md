---
id: kb:physics:method-force-al-desk
type: 教法
title: 力 · 进阶：两个学生推一张桌子
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: 已经知道「力改变运动」、但把力当标量处理的学生
  条件: 已接触矢量及其表示
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[力（高中）](../知识点/力-高中.md)"]
evidence: [ev-041]
license: CC-BY-SA-4.0
---

## 做法

教材的 `[AL]` 提示**用同一张课桌走了三步**，每一步加一个概念。

### 第一步：一个人推，桌子动；两个人对着推，桌子不动

> `Ask students what would happen if more than one force is applied to an object. Take a heavy`
> `object such as a desk for demonstration. Ask one student to push it from one side.`
> `Explain how force and motion work. Now ask a second student to push it in the opposite`
> `direction. Ask students why no motion occurs, even though the first student applies the`
> `same amount of force. Introduce the concept of adding forces.`

**关键是最后那个追问**：

> **「第一个学生用的力**一点没变**，为什么桌子不动了？」**

**学生必须把「力」与「合力」分开**才能回答。教材不用公式，用这张桌子。

### 第二步：把「大小与方向」这件事说破

> `Explain that both magnitude and direction must be considered when talking about forces.`
> `By using physical objects, demonstrate how different forces acting together can be additive`
> `if they act in the same direction or cancel one another if they act in opposite directions.`

**两句话给出顺次的两条规则**：

| 情形 | 结果 |
|---|---|
| 同向 | **相加** |
| 反向 | **相消** |

> `Explain the terms acting on and being acted on.`

**这一句是为第三定律埋的**：「甲**施于**乙」与「乙**被**甲施」是同一个相互作用的两个说法。

### 第三步：把力学图上

> `Ask students to give everyday examples of situations where multiple forces act together.`
> `Draw free-body diagrams for some of these situations.`

**教材要求学生自己举例，然后画受力图**——注意顺序：
**先有真实情境，后有图**，不是先教画图规则。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **AL**（教材标记 `[AL]`） |
| 先修 | 矢量及其表示（教材在 `[BL]` 档要求复习它） |
| 教具 | **一张重课桌** + 两名学生（教材指定）；画图用纸笔 |
| 认知负荷 | 中高——**同时处理「两个力」与「方向」两层** |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **还没接触过矢量**的学生 | 第二步整个建立在「力有方向」上；教材把矢量复习放在 `[BL]` 档，说明**它不是 AL 的前提而是更靠前的东西** | **强**（教材分了档） |
| 教室没有可推的重物、或人数不足 | 教材的演示**要两个人对着推同一张桌子**——这是一条**有物理条件的做法** | **中**——由做法本身推出 |
| 本档（AL）**以外**的学生 | 教材为该段落标的就是 `[AL]`；OL 与 BL 档另给了不同建议 | **中**——标签明确划了范围，但「未标」仍不等于「不适用」，只是**未经检验** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 桌子不动被解释成「力抵消了所以没有力」 | **两个力都还在**，抵消的是它们的**合效果**。这正是第一步那个追问要防的 |
| 直接教画受力图的规则 | 教材的落点是 `Ask students to give everyday examples`——**先举例，后画图**。反过来会把受力图变成一套记号 |
| `acting on` / `being acted on` 一带而过 | 教材专门列了这一句，而**第三定律整个建立在它上面** |
| 两个人推桌子变成游戏 | 教材的第一步是**先让一个人推**（桌子动），**再让两个人对着推**（不动）。少了前半段就没有对照 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-041 | 教材（全文） | 低 | OpenStax《Physics》第 4 章 · Force，[m54135](https://github.com/openstax/osbooks-physics/blob/main/modules/m54135/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 AL 档指定（尚无攻击）

- **主张**：这是教材为进阶学生指定的做法
- **前提**：m54135 的 Teacher Support 用 `[AL]` 标记上述内容（ev-041）
- **推理**：分档标记即教材对该段落的指定
- **证据**：ev-041
- **被攻击**：**「教材指定」≠「实测有效」**；
  且本条依赖**一张重课桌**——**换到教室条件不同的地方（或没有第二个学生配合）就做不了**，
  这一点教材没说。属于本库[覆盖度对照](../覆盖度/README.md) 记的「教法的可迁移性无数据」的一例
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（#8 批量转换 · 第 6 批） | Issue #8 | @hpleapfrog |
