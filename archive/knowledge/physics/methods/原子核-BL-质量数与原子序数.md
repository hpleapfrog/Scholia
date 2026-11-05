---
id: kb:physics:method-nucleus-bl-mass-vs-atomic-number
type: 教法
title: 原子核 · 低于年级水平：质量数不是原子序数
status: 有效
author: "@hpleapfrog"
created: 2026-10-23
updated: 2026-10-23
scope:
  学科: 物理
  学段: 高中
  水平档: 低于年级水平（BL）
  适用: 刚学分项符号、会混淆质量数与原子序数的学生
  条件: 学生已知道质子、中子与元素符号
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[原子核](../concepts/原子核.md)"]
evidence: [ev-158]
license: CC-BY-SA-4.0
---

## 做法

教材把这条混淆当成**默认会发生的事**，用的是 `Remind`：

> `[BL] Students may confuse the terms mass number and atomic number. Remind them that the mass is based on both protons and neutrons and so mass number is a measure of both combined. The atomic number differentiates between two different atoms, which only protons can do.`

一句话给了两个判据：

| 量 | 由谁决定 | 用来区分什么 |
|---|---|---|
| 质量数 `A` | 质子 **+** 中子 | 同位素（同一元素的变体） |
| 原子序数 `Z` | 只有质子 | **元素种类** |

### 接着用「看图数」来固化

> `A few examples showing pictures of nuclei and having students identify the mass and atomic numbers of each should help.`

教材的办法很朴素：**给出核的图，让学生自己数**。

### 最后追问一句，把区别钉住

> `If each atom of carbon has an atomic number of 6, then what is the value of including the mass number at all?`

答案就是同位素：`carbon-13`、`carbon-14` 的区别只在质量数。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **BL** |
| 先修 | 质子、中子、元素符号 |
| 认知负荷 | 低——两个量的分工 |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **还没学元素符号与质子数**的学生 | 「原子序数区分元素」这句话无处落脚 | **强** |
| 要做衰变方程配平的学生 | 本条只解决命名混淆，不教配平 | **中** |
| 本档以外 | 教材 `[AL]` 另问「质量数守恒，质量守恒吗」 | **中** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 只讲「A = Z + N」这个等式 | 教材给的是**判据**（谁决定、区分什么），不是代数关系；只背等式，混淆照旧 |
| 不纠正「原子序数也由中子决定」 | 教材原话是 `which only protons can do`——这是专门用来打断这个误解的 |
| 不追问「那质量数还有什么用」 | 这一问把学生推到「同位素」上；不追问，质量数就成了多余的量 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-158 | 教材（全文） | 低 | OpenStax《Physics》第 31 章 · The Nucleus，[m54580](https://github.com/openstax/osbooks-physics/blob/main/modules/m54580/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 BL 档指定（尚无攻击）

- **主张**：教材用「提醒 → 看图数 → 追问同位素」处理这组混淆
- **前提**：m54580 的 `[BL]` 段明写 `Students may confuse the terms mass number and atomic number`（ev-158）
- **推理**：三步动作与判据都取自原文
- **证据**：ev-158
- **被攻击**：
  - **「教材指定」≠「实测有效」**
  - **「只背 A = Z + N 会照旧混淆」是我的判断**：教材没这么说，是从它用 `Remind` + 追问推出来的
- **署名**：@hpleapfrog · 2026-10-23

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-23 | 建立条目：从 m54580 的 `[BL]` 段摘出三处判据 | `tools/os_source.py 原子核`（ev-158） | @hpleapfrog |
