---
id: kb:physics:method-shm-all-build-oscillators
type: 教法
title: 简谐运动 · 不分档：先做振子，再给名词
status: 有效
author: "@hpleapfrog"
created: 2026-10-23
updated: 2026-10-23
scope:
  学科: 物理
  学段: 高中
  水平档: 不分档（教材未分档，三个档位共用）
  适用: 第一次接触振动、还分不清「周期」「频率」「振幅」的学生
  条件: 学生已学过力与牛顿第一定律
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[简谐运动](../concepts/简谐运动.md)"]
evidence: [ev-164]
license: CC-BY-SA-4.0
---

## 做法

教材在这一节给的是**动手在前、命名在后**：

> `[BL] [OL] [AL] Find springs or rubber bands with different amounts of stiffness. Ask students to attach weights to these to construct oscillators.`

**先让学生把振子做出来**，然后才引入术语：

> `Introduce the terms frequency and time period. Ask students to observe how the stiffness of the spring affects them. How does mass of the system affect them? How does the initial force applied affect them?`

三问各排除一个变量：**刚度**、**质量**、**初始力**。教材没有给答案，
因为这三问的答案要学生从自己做的振子里看出来。

### 前一步必须补：力

> `[BL] Review the concept of force.` / `[BL] [OL] [AL] Introduce Hooke's law and force constant of a spring.`

没有「回复力」这个概念，学生看到的是「来回动」，而不是「被拉回去」。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **不分档**（教材同一段标了 `[BL] [OL] [AL]`） |
| 先修 | 力、牛顿第一定律；胡克定律刚引入 |
| 认知负荷 | 低到中——负荷在「改一个量、看什么变」 |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **没有弹簧／橡皮筋可用**的课堂 | 三问全部依赖学生手里的振子；没有器材，这条退化成背结论 | **强** |
| 已能写出 `x(t) = A cos(ωt+φ)` 的学生 | 他们要的是相位与能量，不是搭振子 | **中** |
| 需要立刻算周期公式的学生 | 本条不产出公式 | **中** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 一次改两个量（换个更硬的簧 **又** 换个更重的砝码） | 教材三问是**分开**的：刚度、质量、初始力各问一次；混着改，学生看到的差别归不了因 |
| 直接给 `T = 2π√(m/k)` | 教材的顺序是先观察再命名；先给公式，三问就失去意义 |
| 只做簧、不做别的振子 | 「所有振动都有力」这个结论要靠多个振子（摆在后面才出现）才能建立 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-164 | 教材（全文） | 低 | OpenStax《Physics》第 5 章 · Simple Harmonic Motion，[m54154](https://github.com/openstax/osbooks-physics/blob/main/modules/m54154/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为三个档位同时指定（尚无攻击）

- **主张**：这条「做振子 → 三问 → 命名」是教材对 `[BL] [OL] [AL]` 同时给的做法
- **前提**：m54154 的 Teacher Support 用三段标记覆盖三档，并要求用不同刚度的弹簧与砝码搭振子（ev-164）
- **推理**：标记与三问都取自原文；「不分档」即原文的标注方式
- **证据**：ev-164
- **被攻击**：
  - **「教材指定」≠「实测有效」**：器材差异很大，本条完全依赖手边有没有弹簧
  - **「一次只改一个量」是我补的风险**，教材只列了三问，没写这条纪律
- **署名**：@hpleapfrog · 2026-10-23

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-23 | 建立条目：从 m54154 摘出「做振子 + 三问」 | `tools/os_source.py 简谐运动`（ev-164） | @hpleapfrog |
