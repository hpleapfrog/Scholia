---
id: kb:physics:method-capacitance-blol-dictionary
type: 教法
title: 电容 · 低于/年级水平：先查词典里的 capacity
status: 有效
author: "@hpleapfrog"
created: 2026-10-23
updated: 2026-10-23
scope:
  学科: 物理
  学段: 高中
  水平档: 低于年级水平（BL）至 年级水平（OL）
  适用: 第一次接触「电容」、容易把它读成「电量」的学生
  条件: 学生已学过电势差
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[电容](../concepts/电容.md)"]
evidence: [ev-175]
license: CC-BY-SA-4.0
---

## 做法

教材这一节的第一句就定了调子：

> `To present capacitors, this section emphasizes their capacity to store energy.`

**不是先讲 `C = Q/U`，而是先讲「能存多少」。**

### 一、先去查词，而不是先给定义

> `[BL] Have students define how the word capacity is used in everyday life. Have them look up the definition in the dictionary. Compare and contrast the everyday meaning with the meaning of the term in physics.`

教材给的是**三步动作**：先说 → 查词典 → **比较**。比较这一步是重点，
因为日常 `capacity`（容量、能力）与物理 `capacitance` 只差一层：**存的是电荷与能量，不是「装得下多少东西」**。

### 二、把「储能」摆到别的装置旁边

> `To introduce the idea of energy storage, discuss with students other mechanisms of storing energy, such as dams or batteries. Ask which have greater capacity.`

**问「哪个容量更大」而不是「哪个更先进」**——这一问把「容量」变成可比的量。

### 三、指名一个已经在用的词

> `[OL] Ask students whether they have heard the word capacitor used in conjunction with electricity, such as in power stations or electric circuits.`

教材承认这个词**学生可能听过**（变电站、电路），只是不知道它指什么。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **BL / OL**（`[BL]` 与 `[OL]` 两条提示） |
| 先修 | 电势差；知道能量可以储存 |
| 认知负荷 | 低——负荷在「同一个词的两个含义」上，不在公式上 |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **没学过电势差**的学生 | 「存的是电荷与能量」要靠 `U` 才说得清；没有它，只能停在比喻 | **强** |
| 要立刻算 `C = Q/U` 或串并联电容的学生 | 本做法不产出计算 | **中** |
| 本档以外 | 教材 `[AL]` 用弹簧储能，与本条不同 | **中** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 把 `capacity` 直接译成「容量」就过 | 教材要的是**比较日常义与物理义**；只给译文，比较这一步就没了 |
| 用「水桶装水」讲电容 | 水桶装的是水（物质），电容存的是**电荷与能量**——比喻会把「存什么」偷换掉 |
| 一上来写 `C = Q/U` | 教材的顺序是「储能 → 电容」，公式在最后；倒过来讲，「电容与电压无关」这条会讲不清 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-175 | 教材（全文） | 低 | OpenStax《Physics》第 18 章 · Capacitors and Dielectrics，[m63179](https://github.com/openstax/osbooks-physics/blob/main/modules/m63179/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 BL/OL 档指定（尚无攻击）

- **主张**：教材为 BL/OL 学生指定了「查词典 → 比较 → 储能类比」这条路径
- **前提**：m63179 的 Teacher Support 明写 `emphasizes their capacity to store energy`，
  并给出 `[BL]` 查词典与 `[OL]` 「你听过电容这个词吗」（ev-175）
- **推理**：三步动作与顺序都取自原文；分档标记即指定
- **证据**：ev-175
- **被攻击**：
  - **「教材指定」≠「实测有效」**
  - **「水桶比喻会偷换存什么」是我补的风险**，教材没有点名水桶
- **署名**：@hpleapfrog · 2026-10-23

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-23 | 建立条目：从 m63179 摘出 BL/OL 做法 | `tools/os_source.py 电容` 取原文通读（ev-175） | @hpleapfrog |
