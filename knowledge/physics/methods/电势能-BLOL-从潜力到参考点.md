---
id: kb:physics:method-electric-potential-blol-daily-potential
type: 教法
title: 电势能 · 低于/年级水平：从「潜力」这个词到参考点
status: 有效
author: "@hpleapfrog"
created: 2026-10-22
updated: 2026-10-22
scope:
  学科: 物理
  学段: 高中
  水平档: 低于年级水平（BL）至 年级水平（OL）
  适用: 已经会算库仑力、正要区分「电势能」与「电势」的学生
  条件: 学生已学过重力势能
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[电势能与电势](../concepts/电势能与电势.md)"]
evidence: [ev-087]
license: CC-BY-SA-4.0
---

## 做法

教材这条路径的骨架是**一个日常词 → 一个已学概念 → 一条限制**。

### 一、先问「潜力」在日常里怎么用

> `[BL] Ask students to define how potential is used in everyday life. Draw the analogy between this and potential energy.`

中文里就是「这个人有潜力」——**现在没做，但具备做的条件**。教材要的就是这个语感。

### 二、复习势能的定义句

> `[OL] [AL] Review the concept of potential energy as being the potential an object has to do work by virtue of its position with respect to another object.`

**「by virtue of its position」**——位置，不是速度，也不是「它有什么」。这一句是后面所有类比的支点。

### 三、加限制：势能只能谈差值

> `[OL] Remind students that gravitational potential energy is only meaningful when we deal with differences in energy. In other words, a reference position is chosen, and all other potential energies are compared with the potential energy at the reference position.`

教材用的是 `Remind`（提醒）——**说明学生学过，但会忘**。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **BL / OL**（`[BL]` 与 `[OL]` 两条提示拼起来） |
| 先修 | 重力势能；会算库仑力 |
| 认知负荷 | 中——负荷在「一个词三层含义」（日常潜力 → 势能 → 电势） |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **没学过重力势能**的学生 | 第 2、3 步全建在它上面；`Remind` 对没学过的人是无效动作 | **强** |
| 要立刻算 `U = kq₁q₂/r` 的学生 | 本做法不产出计算，只建立「为什么能谈差值」 | **中** |
| 本档以外 | 教材 `[AL]` 补了「参考点常在无穷远」这一层，与本条不同 | **中** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 把「潜力」讲成「能量大小」 | 日常「潜力」= **尚未发生的能力**，正对应「取决于位置」；一改口就滑回「有多少能量」 |
| 跳过参考点 | 势能的绝对值没有意义——教材用 `Remind` 说明这是**旧账**，不是新知识 |
| 直接讲电势 `V = U/q` | 教材在本节末尾才 `Emphasize the difference`；**顺序反了，两个词会糊成一个** |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-087 | 教材（全文） | 低 | OpenStax《Physics》第 18 章 · Electric Potential，[m54426](https://github.com/openstax/osbooks-physics/blob/main/modules/m54426/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 BL/OL 档指定（尚无攻击）

- **主张**：这是教材为 BL/OL 学生指定的引入顺序
- **前提**：m54426 的 Teacher Support 依次给出 `[BL]` 日常「潜力」、`[OL] [AL]` 复习势能定义、
  `[OL]` 提醒「只能谈差值 · 要选参考位置」（ev-087）
- **推理**：三步的顺序与分档标记都取自原文
- **证据**：ev-087
- **被攻击**：
  - **「教材指定」≠「实测有效」**
  - **「中文『潜力』的语感刚好对应」是我加的**：教材只说 `used in everyday life`，没有中文例子
- **署名**：@hpleapfrog · 2026-10-22

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-22 | 建立条目：从 m54426 摘出 BL/OL 三步 | 抓取 cnxml 通读（ev-087） | @hpleapfrog |
