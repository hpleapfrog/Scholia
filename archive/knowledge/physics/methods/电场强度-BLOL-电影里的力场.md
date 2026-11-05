---
id: kb:physics:method-electric-field-blol-force-field
type: 教法
title: 电场强度 · 低于/年级水平：从电影里的「力场」切进去
status: 有效
author: "@hpleapfrog"
created: 2026-10-22
updated: 2026-10-22
scope:
  学科: 物理
  学段: 高中
  水平档: 低于年级水平（BL）至 年级水平（OL）
  适用: 第一次接触「场」这个概念、还习惯用「力」说话的学生
  条件: 学生已学过库仑定律；知道万有引力
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[电场强度](../concepts/电场强度.md)"]
evidence: [ev-086]
license: CC-BY-SA-4.0
---

## 做法

教材在这个模块的处理是**先把「场」当成一个已经见过的词**，再把它换成物理含义。

### 一、先问电影

> `Ask students whether they have seen movies that use the concept of fields as in force fields. Have them describe how such fields work.`

**先让学生用自己的话说「力场怎么运作」**——他们一定会说成「某个区域里会被推/被挡」。

### 二、换成引力的版本

> `Describe how gravity can be thought of as a field that surrounds a mass and with which other masses interact. Explain that electric fields are very similar to gravitational fields.`

教材的顺序是：**电影的力场 → 引力场 → 电场**。中间那一步是关键，它把「虚构的场」接到
「你已经承认存在的场」上。

### 三、场线只从一个地方出发

> `[BL] [OL] Point out that all electric field lines originate from the charge.`

教材用 `Point out`（指出），说明这是**学生看图时最容易看漏的一条**：
线画在电荷周围，容易被读成「空间自己长出来的」。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **BL / OL**（教材这条提示同时标两档） |
| 先修 | 已学库仑定律；知道万有引力 |
| 认知负荷 | 低到中——负荷在「同一个词换了含义」上 |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **没学过万有引力**的学生 | 类比链的第二环断了，「场」就只剩电影印象 | **强**（由做法性质推出） |
| 已经能熟练用 `E = F/q` 计算的学生 | 本做法不产出计算能力，只换概念 | **中** |
| 本档（BL/OL）**以外**的学生 | 教材 `[AL]` 另给了一条（数场线推平方反比），与本条不同 | **中** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 把电影力场当成「场」的定义 | 教材紧接着就说 `it differs somewhat from what you see in movies`——**电影只是入口，不是答案** |
| 只画场线，不强调「从电荷出发」 | 教材专门 `Point out` 这一条，说明它默认会被误读 |
| 跳过引力场那一步 | 少了这步，电场就变成「又一个要背的概念」，而不是「同一件事换了个源」 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-086 | 教材（全文） | 低 | OpenStax《Physics》第 18 章 · Electric Field，[m54428](https://github.com/openstax/osbooks-physics/blob/main/modules/m54428/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 BL/OL 档指定（尚无攻击）

- **主张**：这是教材为低于年级水平与年级水平学生指定的引入方式
- **前提**：m54428 的 Teacher Support 依次给出「问电影 → 引力场 → 电场」与 `[BL] [OL] Point out …`（ev-086）
- **推理**：三段顺序是教材原文的次序；分档标记即指定
- **证据**：ev-086
- **被攻击**：
  - **「教材指定」≠「实测有效」**：本条无课堂数据
  - **「电影的力场会被误当真」**是我从教材那句 `differs somewhat` 推出的风险，不是教材明写的课堂结论
- **署名**：@hpleapfrog · 2026-10-22

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-22 | 建立条目：从 m54428 摘出 BL/OL 引入序列 | 抓取 cnxml 通读（ev-086） | @hpleapfrog |
