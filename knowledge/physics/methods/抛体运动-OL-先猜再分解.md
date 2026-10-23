---
id: kb:physics:method-projectile-all-guess-then-split
type: 教法
title: 抛体运动 · 不分档：先让学生猜，再拆两个方向
status: 有效
author: "@hpleapfrog"
created: 2026-10-23
updated: 2026-10-23
scope:
  学科: 物理
  学段: 高中
  水平档: 不分档（教材在同一段标了 BL/OL/AL）
  适用: 刚要学平抛、习惯「一个公式套到底」的学生
  条件: 学生已学过矢量合成与运动学公式
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[抛体运动](../concepts/抛体运动.md)"]
evidence: [ev-163]
license: CC-BY-SA-4.0
---

## 做法

教材给三档的动作是一样的，只有深度不同：

> `[BL] [OL] [AL] Explain the term projectile motion. Ask students to guess what the motion of a projectile might depend on? Is the initial velocity important? Is the angle important? How will these things affect its height and the distance it covers?`

**「猜」是第一步，不是热身**——它把「抛体运动取决于什么」变成学生自己的问题。
教材紧接着提出空气阻力，作为**待排除的变量**：

> `Introduce the concept of air resistance.`

### 核心结论只有一句

> `The most important concept in projectile motion is that when air resistance is ignored, horizontal and vertical motions are independent, meaning that they don't influence one another.`

### 用「同时下落」证它

> `compares a cannonball in free fall … to a cannonball launched horizontally in projectile motion … the cannonball in free fall falls at the same rate as the cannonball in projectile motion.`

**同高度同时落地**——这是独立性最直观的证据，也是教材选这个图的原因。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **不分档**（同段标 `[BL] [OL] [AL]`） |
| 先修 | 矢量合成、运动学公式；空气阻力概念（作为对照） |
| 认知负荷 | 中——负荷在「把一条曲线拆成两条直线」 |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **还不会分解矢量**的学生 | 独立性讲完也没法用；教材在 `[BL] [OL]` 里先要求 `Review addition of vectors` | **强** |
| 已经熟练解抛体题的学生 | 他们要的是斜抛与极值，不是这条主线 | **中** |
| 需要处理空气阻力的课堂 | 本做法的前提就是「忽略空气阻力」 | **中** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 跳过「猜」，直接讲独立性 | 猜这一步是在为「哪些量有用」建档；跳过它，独立性变成一条要背的话 |
| 用「重的落得快」当反例而不做同时下落对比 | 教材靠**同一张图里两个球同时落地**来立论；只讲不画，学生会回退到直觉 |
| 不提「初速有竖直分量时对不齐」 | 教材专门加了 `if the cannon launched the ball with any vertical component … the vertical displacements would not line up`——这是对结论的**边界** |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-163 | 教材（全文） | 低 | OpenStax《Physics》第 5 章 · Projectile Motion，[m54162](https://github.com/openstax/osbooks-physics/blob/main/modules/m54162/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为三档同时指定（尚无攻击）

- **主张**：教材用「猜 → 排除空气阻力 → 独立性 → 同时下落」这一串讲抛体
- **前提**：m54162 的 `[BL] [OL] [AL]` 段要求先猜、再引入空气阻力，正文给出独立性与对照图（ev-163）
- **推理**：顺序与关键句都取自原文
- **证据**：ev-163
- **被攻击**：
  - **「教材指定」≠「实测有效」**
  - **「跳过猜就失去意义」是我的判断**：教材只说 `Ask students to guess`，没解释这一步的作用
- **署名**：@hpleapfrog · 2026-10-23

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-23 | 建立条目：从 m54162 摘出「猜 + 独立性 + 同时下落」 | `tools/os_source.py 抛体运动`（ev-163） | @hpleapfrog |
