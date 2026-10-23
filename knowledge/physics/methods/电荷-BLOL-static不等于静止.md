---
id: kb:physics:method-charge-blol-static-is-not-still
type: 教法
title: 电荷 · 低于/年级水平：static 不等于静止
status: 有效
author: "@hpleapfrog"
created: 2026-10-23
updated: 2026-10-23
scope:
  学科: 物理
  学段: 高中
  水平档: 低于年级水平（BL）至 年级水平（OL）
  适用: 刚接触「静电」、会把它理解成「电荷不动」的学生
  条件: 无（这是本章的第一课）
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[电荷](../concepts/电荷.md)"]
evidence: [ev-083]
license: CC-BY-SA-4.0
---

## 做法

教材在章首做的第一件事是**拆掉「静电＝静止」这个字面理解**：

> `Ask students what they know about static electricity and about electric charge.`

先让他们说，然后教材直接给出反例：

> `Although the word static implies that nothing is moving, this is often not the case. For example, separating positive from negative charges involves charges in motion but creates static electricity. Likewise, a lightning strike is a huge electric current but is created by static electricity.`

**两个反例方向相反**：
- 分离正负电荷——**过程在动**，结果叫静电
- 闪电——**本身是大电流**，起因是静电

### 再给一句可操作的定义

> `static electricity is a field of study that focuses on the forces and electrical pressure between objects that have an imbalance of electric charge.`

注意 `imbalance`（不平衡）才是关键词，不是 `static`（不动）。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **BL / OL**（教材这段是全体适用的开场） |
| 先修 | 无 |
| 认知负荷 | 低——只需接受「名字与含义不一致」 |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| 已经把「静电」理解为「电荷分布不随时间变」的学生 | 他们不需要拆这个误解，可直接进入电荷守恒 | **中** |
| 只想做摩擦起电实验、不打算讲定义的课堂 | 本做法的产出是**定义与反例**，不做实验 | **中** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 把 `static` 直译成「静止」就过去 | 教材整段就是为了拦住这个直译 |
| 只讲摩擦起电，不讲「分离过程要移动电荷」 | 少了这一条，「在动却叫静电」这个矛盾就消失，定义又回到字面 |
| 用闪电当唯一的反例 | 闪电同时是「电流」与「静电产物」，容易被读成「静电=电流」，**教材用两个方向相反的例子就是为了防这个** |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-083 | 教材（全文） | 低 | OpenStax《Physics》第 18 章 · Introduction，[m54417](https://github.com/openstax/osbooks-physics/blob/main/modules/m54417/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材指定的开场（尚无攻击）

- **主张**：教材用「先问已知 → 给两个反向反例 → 给不平衡的定义」开场
- **前提**：m54417 的 Teacher Support 明写 `Although the word static implies that nothing is moving, this is often not the case`，并给出分离电荷与闪电两个例子（ev-083）
- **推理**：三个动作与顺序都取自原文
- **证据**：ev-083
- **被攻击**：
  - **教材没标 [BL]/[OL]**：这段是章首通用提示，我把它归到 BL/OL 是**我的判断**（低负荷、无先修）
  - **「教材指定」≠「实测有效」**
- **署名**：@hpleapfrog · 2026-10-23

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-23 | 建立条目：从 m54417 章首提示摘出「static ≠ 静止」 | `tools/os_source.py 电荷` 取原文（ev-083） | @hpleapfrog |
