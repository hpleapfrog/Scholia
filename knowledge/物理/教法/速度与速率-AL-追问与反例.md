---
id: kb:physics:method-speed-al-socratic
type: 教法
title: 速度与速率 · 进阶：苏格拉底式追问 + 平均速度反例
knowledge_point: ["[速度与速率](../知识点/速度与速率.md)"]
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: 能自主推理、可接受反直觉结论的学生
  条件: 学生愿意先猜再检验
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-022]
license: CC-BY-SA-4.0
---

## 做法

两部分：**先让学生猜，再用一个反例打掉直觉。**

### 一、追问式对比

点明速度与位移一样是**矢量**，然后让学生**先猜**速度与速率差在哪，再用追问加深：

> `Why do you think that? What is an example? How might you apply these terms to motion that you see every day?`

教材原文（短引用）：

> `Explain to students that velocity, like displacement, is a vector quantity.
> Ask them to speculate about ways that speed is different from velocity.
> After they share their ideas, follow up with questions that deepen their thought process`

### 二、平均速度反例（教材自带数字）

> `Caution students that average speed is not always the average of an object's initial and final speeds.`

教材给的例子：一辆车行 100 km，前 50 km 用 30 km/h，后 50 km 用 60 km/h。

- **等距离**时平均速度 = **40 km/h**（不是 (30+60)/2 = 45）
- 若改成**等时间**分别以 30 和 60 km/h 行驶，平均才是 **45 km/h**

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **AL**（教材标记 `[AL]`） |
| 先修 | 已接触矢量与位移；能算加权平均 |
| 认知负荷 | 高——负荷放在**反直觉的算术**与**概念区分** |

## 禁忌

| 会翻车的地方 | 为什么 | 出处 |
|---|---|---|
| **把「平均」当成算术平均** | 教材明确指出这是要防的错误：`average speed is not always the average of an object's initial and final speeds` | 教材同节 `[OL][AL]` |
| 只给反例不给一般式 | 学生记住了 40 这个数，换个距离/速度就又不成立。必须回到 `总路程 / 总时间` | — |

> [!TIP]
> 这个反例的价值在**同时**展示两种情形（等距离 40 vs 等时间 45）。
> 只给一种，学生会以为「平均速度永远不等于算术平均」——**那就变成了另一个误解**。

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-022 | 教材（全文） | 低 | OpenStax《Physics》§2.2，[m54104](https://github.com/openstax/osbooks-physics/blob/main/modules/m54104/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 AL 档指定（存活）

- **主张**：追问式对比与平均速度反例是教材为进阶学生指定的做法
- **前提**：m54104 的 Teacher Support 用 `[AL]` 与 `[OL][AL]` 标记（ev-022）
- **推理**：分档标记即教材对该水平的指定
- **证据**：ev-022
- **被攻击**：**指定 ≠ 实测有效**；反例的算术负担可能对边界学生过重
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（采集候选转入） | Issue #8 | @hpleapfrog |
