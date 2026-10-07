---
id: kb:physics:method-atom-ol-balloon-analogy
type: 教法
title: 原子结构 · 年级水平：用「黑暗中找气球」讲不确定原理
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  适用: 在不确定原理上卡住的学生
  条件: 学生需要先接受「测量会扰动被测对象」
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[原子结构](../知识点/原子结构.md)"]
evidence: [ev-035]
license: CC-BY-SA-4.0
---

## 做法

**用一个可当场演示的日常情境，替代抽象的测量扰动说法。**

教材原文（短引用）：

> `Another model for explaining the uncertainty principle for students struggling with the concept:
> Imagine searching for a floating balloon in a dark room. When your hand strikes the balloon,
> you provide an impulse and move it from its original spot. While you learned the position of the
> object, you disturbed it during your search. As a result, it has a new momentum that is unknown!`

**这个类比的映射：**

| 类比里 | 物理里 |
|---|---|
| 黑暗的房间 | 看不见的**微观尺度** |
| 手去摸气球 | **测量动作**（要碰到才能测） |
| 摸到气球的瞬间把它推走 | 测量给出的**冲量**改变了动量 |
| 「摸到位置」却「动量未知」 | **位置与动量不能同时确定** |

**要点**：教材把它定位为 `Another model for ... students struggling with the concept`——
**这是给卡住的人的备用路径，不是主路径。**

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **OL**（教材标记 `[OL]`） |
| 先修 | 学生已听过标准表述但**没接受** |
| 认知负荷 | 中——负荷放在**把抽象说法换成可想象的动作** |

## 禁忌

**对谁不适用？**

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| 还没听过标准表述的学生 | 教材明写这是给 `struggling with the concept` 的人用的**替代路径**；先用它替代主路径会**绕过标准表述** | **中** —— 教材明示用途 |
| 本档以外的学生 | 教材为各档**另给了不同做法**，未声明本做法可跨档 | **弱** —— 未经检验 |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| **类比被当成原理本身** | 「因为摸就推走了所以不确定」是**测量扰动**图像。而量子不确定原理**不是**「仪器不够好」——它不因仪器改进而消失。**这是本类比最大的危险** |
| 学生由此认为「粒子本来有确定位置，只是我们测不到」 | 这正是隐藏变量诠释的思路。**教材的类比没有说这一点，但学生会自己补上** |
| 把气球换成小球 | 气球的关键是**轻、易被推动**。换成重物，扰动效应就没了，类比失效 |

> [!WARNING]
> **这个类比的失效模式与 [水管类比](../教法/水管类比.md) 同类，但后果更重。**
>
> 水管类比失准只是让学生对电路机制理解偏；**这个类比失准会让学生理解成「量子力学只是测不准」**——
> 那是**一个关于物理学性质的错误结论**，不是一处细节偏差。
>
> **教材把它标为备用路径是对的；但用它时必须明确说「类比到此为止」。**

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-035 | 教材（全文） | 低 | OpenStax《Physics》第 22 章 · ，[m54582](https://github.com/openstax/osbooks-physics/blob/main/modules/m54582/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 OL 档指定（尚无攻击）

- **主张**：这是教材为年级水平学生指定的做法
- **前提**：m54582 的 Teacher Support 用 `[OL]` 标记，并明确注明用途是给卡住的学生（ev-035）
- **推理**：分档标记即教材对该水平的指定
- **证据**：ev-035
- **被攻击**：
  - **「教材指定」≠「实测有效」**
  - **类比可能制造新的错误概念**——教材没有讨论这一点，而本条目在 `风险` 里指出了
- **署名**：@hpleapfrog · 2026-10-05
- **待补**：使用该类比后，学生是否更倾向「隐藏变量」诠释（可用前后测检验）

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（#8 批量转换 · 第 3 批） | Issue #8 | @hpleapfrog |
