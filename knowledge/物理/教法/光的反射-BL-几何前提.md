---
id: kb:physics:method-reflection-bl-geometry
type: 教法
title: 光的反射 · 低于年级水平：先补几何，再说「弹跳是简化」
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 低于年级水平（BL）
  适用: 几何基础薄弱、或习惯把「反射」当成「弹跳」的学生
  条件: 学生学过角的概念
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[光的反射](../知识点/光的反射.md)"]
evidence: [ev-026]
license: CC-BY-SA-4.0
---

## 做法

**两个前提都要先立，否则后面的公式没有落脚点。**

### 前提一：角的含义（来自几何）

教材原文（短引用）：

> `Recall that, in geometry, angles are numbers that tell how far two straight lines are spread apart.
> The lines must be straight lines for the number to have meaning.`

### 前提二：「光会弹回来」是简化

> `Explain that light bounces is a simplification. The geometry of the path of a bouncing ball is similar
> to that of light, but what happens at the point of impact is different at the molecular level.`

**要点**：第二个前提**不是补充说明，是防错**。
「弹跳」这个日常说法给出的是**宏观几何**的相似，而机制完全不同——
不说破，学生会把光的反射理解成小球撞墙。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **BL**（教材标记 `[BL]`） |
| 先修 | **几何里的「角」**——先确认这个，再讲反射 |
| 认知负荷 | 低——负荷放在**澄清既有概念**，不在新公式 |

## 禁忌

**对谁不适用？**

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| 尚未掌握「角」的几何含义的学生 | 教材明示 `The lines must be straight lines for the number to have meaning`——**前提不成立时，入射角/反射角都无意义** | **强**（教材明示） |
| 本档以外的学生 | 教材为各档**另给了不同做法**，未声明本做法可跨档 | **弱** —— 未经检验 |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 把「弹跳是简化」当成「弹跳是错的」 | 教材说的是**几何相似、机制不同**，不是「弹跳完全错」。过度纠正会让学生连几何图像一起丢掉 |
| 跳过几何前提直接上公式 | 教材把它排在最前，说明编写者认为这是常见断点 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-026 | 教材（全文） | 低 | OpenStax《Physics》第 16 章 · Reflection，[m54357](https://github.com/openstax/osbooks-physics/blob/main/modules/m54357/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 BL 档指定（尚无攻击）

- **主张**：这是教材为低于年级水平学生指定的做法
- **前提**：m54357 的 Teacher Support 用 `[BL]` 标记两条建议（ev-026）
- **推理**：分档标记即教材对该水平的指定
- **证据**：ev-026
- **被攻击**：**「教材指定」≠「实测有效」**
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（#8 批量转换 · 第 1 批） | Issue #8 | @hpleapfrog |
