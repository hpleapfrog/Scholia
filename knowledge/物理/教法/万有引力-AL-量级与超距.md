---
id: kb:physics:method-gravitation-al-magnitude
type: 教法
title: 万有引力 · 进阶：两个 10 kg 球有多大引力
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: 已经能代入 F = GmM/r²、但对引力的「弱」没有量级感的学生
  条件: 已能用科学计数法做乘除
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[万有引力定律](../知识点/万有引力定律.md)"]
evidence: [ev-037]
license: CC-BY-SA-4.0
---

## 做法

教材的 `[AL]` 提示走一条**跟「天体」相反**的路：**用身边的物体，把引力算小到看不见。**

### 一、先让人犹豫，再让人算

> `Ask the students what the attraction would be between two 10 kg balls separated by a`
> `distance of 1.0 m. Could they feel it?`
> `Later, ask them to calculate it after they have done some similar calculations.`

**顺序是设计好的**：先**猜**（愿不愿意为「能感觉到」辩护），后**算**。

教材给出的答案：

```
F = G·mM/r² = (6.67×10⁻¹¹)(10 × 10 / 1²) = 6.67×10⁻⁹ N
```

**这个数字的作用不是「算对」，是让人对「引力很弱」有量级感**——
弱到两个 10 kg 的球之间**永远不可能被感觉到**。

### 二、把「超距作用」这件事挑明

> `Ask if anyone thinks it is strange or even mysterious that a force can act at a distance`
> `across empty space. Ask the students to compare and contrast gravitational force with`
> `magnetic and electrostatic forces.`
> `Note how much force at a distance is like magic or having superpowers.`

**教材不回避这件事，而是把它当成一个可以停下来讨论的点。**

### 三、说清 G 为什么是「普适」而 g 不是

> `Ask if anyone can explain why G is a universal constant that applies anywhere in the`
> `universe. Have them discuss the idea that the laws of physics are the same everywhere`
> `and that, at one time, people were not so sure about this.`
> `Emphasize that g is not a universal constant.`

**这一条还带一个观念史的点**：**「物理定律处处相同」本身曾经是不确定的。**

### 四、狭义与广义相对论的区别

> `Ask if anyone knows the difference between special relativity and general relativity.`
> `Special relativity is a theory of spacetime and applies to observers moving at constant`
> `velocity. General relativity is a theory of gravity and applies to observers that are`
> `accelerating. General relativity is broader and includes special relativity, which was`
> `published first.`

### 五、让学生记住三个值

> `Have the students memorize the values of G, g, and π to three significant figures.`

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **AL**（教材标记 `[AL]`） |
| 先修 | 能用科学计数法做乘除；知道牛顿、库仑力的概念 |
| 认知负荷 | 中高——同时装**量级**、**超距**、**相对论**三件事 |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **还不熟科学计数法乘除**的学生 | 第一节的全部意义在 `6.67×10⁻⁹ N` 这个结果上；算不出来就只剩「很小」这个形容词 | **强**——由做法性质推出 |
| 还没分清质量与重量的学生 | 教材另有一条 `[BL]` 提示专门查这件事（`Check to make sure students are clear about the distinction between mass and weight`） | **中**（教材明示顺序：BL 在前） |
| 本档（AL）**以外**的学生 | 教材为该段落标的就是 `[AL]`；BL 与 OL 档另给了不同建议 | **中**——标签明确划了范围，但「未标」仍不等于「不适用」，只是**未经检验** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 「超距作用像魔法」被讲成结论 | 教材的措辞是 `Note how much force at a distance is like magic or having superpowers`——**是一个类比，用来承认它反直觉**，不是解释。讲成结论会把学生推向「物理学也说不清」 |
| 狭义 / 广义相对论讲成两套并列理论 | 教材给的关系是 **广义更宽、且包含狭义**，而且**狭义发表在前**。讲成并列就丢了这层 |
| 五个 `sin` 式那类「形式演示」喧宾夺主 | 本条的落点是**量级感**，不是数学技巧 |
| 先算后猜 | 教材明确是 `Ask … Could they feel it?` **然后** `Later, ask them to calculate it`。顺序反了就没有那个落差 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-037 | 教材（全文） | 低 | OpenStax《Physics》第 7 章 · Newton's Law of Universal Gravitation and Einstein's Theory of General Relativity，[m54189](https://github.com/openstax/osbooks-physics/blob/main/modules/m54189/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 AL 档指定（尚无攻击）

- **主张**：这是教材为进阶学生指定的做法
- **前提**：m54189 的 Teacher Support 用 `[AL]` 标记上述各条（ev-037）
- **推理**：分档标记即教材对该段落的指定
- **证据**：ev-037
- **被攻击**：**「教材指定」≠「实测有效」**；
  且教材把「相对论」放进这条 `[AL]` 提示里，**但它属于本库尚未建立的知识点**（见 [万有引力定律](../知识点/万有引力定律.md) 的缺口一节）
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（#8 批量转换 · 第 4 批） | Issue #8 | @hpleapfrog |
