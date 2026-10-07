---
id: kb:physics:method-mech-energy-bl-units
type: 教法
title: 机械能守恒 · 低于年级水平：先分清能量不是力也不是功率
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 低于年级水平（BL）
  适用: 容易把能量、力、功率混成一回事的学生
  条件: 无
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a1)"]
  攻击: []
knowledge_point: ["[机械能守恒](../知识点/机械能守恒.md)"]
evidence: [ev-028]
license: CC-BY-SA-4.0
---

## 做法

**先把三个概念的量纲关系说清楚，再讲守恒。**

教材原文（短引用）：

> `Make it clear that energy is a different property with different units than either force or power.`

> `Be sure there is a clear understanding of the distinction between kinetic and potential energy and
> between velocity and acceleration. Explain that the word potential means that the energy is available
> but it does not mean that it has to be used or will be used.`

**四组区分**：

| 容易混 | 要分清 |
|---|---|
| 能量 / 力 / 功率 | **三个不同量纲，单位不同** |
| 动能 / 势能 | 动能看运动，势能看位置 |
| 速度 / 加速度 | 一个描述运动，一个描述变化 |
| 势能「存在」/「被使用」 | `potential` 只表示**可用**，不表示**会用** |

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **BL**（教材标记 `[BL]`） |
| 先修 | 无（本做法本身是前提澄清） |
| 认知负荷 | 低——负荷放在**概念区分**，不在计算 |

## 禁忌

**对谁不适用？**

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| 还没学过功率的学生 | 教材要求区分「能量 / 力 / 功率」，功率尚未出现时这条区分无从建立 | **中** —— 由做法推出 |
| 本档以外的学生 | 教材为各档**另给了不同做法**，未声明本做法可跨档 | **弱** —— 未经检验 |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 「势能只是可用、不必用」被讲成「势能不一定存在」 | 教材说的是**是否被使用**，不是**是否存在**。混淆会让学生以为势能是概率性的 |
| 概念区分做成术语背诵 | 四组区分若不配例子，就退化成一堆定义。教材把它们放在 `[BL]`，正是因为这是**最基础的混淆点** |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-028 | 教材（全文） | 低 | OpenStax《Physics》§9.2 Mechanical Energy and Conservation of Energy，[m54273](https://github.com/openstax/osbooks-physics/blob/main/modules/m54273/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 BL 档指定（存活）

- **主张**：这是教材为低于年级水平学生指定的做法
- **前提**：m54273 的 Teacher Support 用 `[BL]` 标记两条区分要求（ev-028）
- **推理**：分档标记即教材对该水平的指定
- **证据**：ev-028
- **被攻击**：**「教材指定」≠「实测有效」**
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（#8 批量转换 · 第 1 批） | Issue #8 | @hpleapfrog |
