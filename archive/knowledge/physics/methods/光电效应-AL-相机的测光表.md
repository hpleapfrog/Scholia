---
id: kb:physics:method-photoelectric-al-light-meter
type: 教法
title: 光电效应 · 进阶：相机测光表为什么需要它
status: 有效
author: "@hpleapfrog"
created: 2026-10-23
updated: 2026-10-23
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶水平（AL）
  适用: 已理解光电效应基本规律、想把它接到器件上的学生
  条件: 学生知道光电流与光强的关系
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[光电效应](../concepts/光电效应.md)"]
evidence: [ev-169]
license: CC-BY-SA-4.0
---

## 做法

教材给 `[AL]` 的是一个**从器件反推原理**的任务：

> `[AL] Ask students why a light meter would be useful in a camera. How could the number of electrons emitted from the light meter control the camera's iris? Have students draw a diagram of the camera that may demonstrate this effect.`

三步：**为什么有用 → 电子数如何控制光圈 → 画出装置**。

注意第二步的落点：**控制光圈的是「电子数」，不是「电子的能量」**。
这一句话把「光强 → 电流大小」与「频率 → 最大动能」两条规律分开了。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **AL** |
| 先修 | 光电效应的两条规律；电路基本概念（电流） |
| 认知负荷 | 中——要把规律映射到器件功能 |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **还没学过光电效应两条规律**的学生 | 任务要求区分「数目」与「能量」，没有规律无法区分 | **强** |
| 只用光电效应讲量子性的课堂 | 本做法偏应用，不推进量子论本身 | **中** |
| 无法画图的环境 | 第三步明确要求 `draw a diagram` | **中** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 说成「测光表测的是光的能量」 | 教材问的是**电子数**怎么控制光圈，即光强 → 电流 |
| 与「光越强电子越快」混淆 | 这一步正是拆这条误解的机会：强度影响数目，频率才影响动能 |
| 只讲原理不画图 | 教材要求 `draw a diagram`，图是这条做法的产物 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-169 | 教材（全文） | 低 | OpenStax《Physics》第 29 章 · The Photoelectric Effect，[m54559](https://github.com/openstax/osbooks-physics/blob/main/modules/m54559/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 AL 档指定（尚无攻击）

- **主张**：教材用「相机测光表」这一器件情境要求 AL 学生把规律用起来
- **前提**：m54559 的 `[AL]` 提示三句（ev-169）
- **推理**：三问的顺序与落点都取自原文
- **证据**：ev-169
- **被攻击**：
  - **「教材指定」≠「实测有效」**
  - **「控制光圈的是电子数」这句强调是我加的**：教材原文只问 `How could the number of electrons … control`，
    我把它读成「数目→光强→光圈」，这一步是我的解释
- **署名**：@hpleapfrog · 2026-10-23

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-23 | 建立条目：从 m54559 的 `[AL]` 提示摘出三步 | `tools/os_source.py 光电效应`（ev-169） | @hpleapfrog |
