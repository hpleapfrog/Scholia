---
id: kb:physics:method-momentum-al-two-forms
type: 教法
title: 动量和冲量 · 进阶：牛顿第二定律的两种写法
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: 已经会用 F = ma、正要学动量这一章的学生
  条件: 已学过牛顿三定律
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../claims/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[动量和冲量](../concepts/动量和冲量.md)"]
evidence: [ev-045]
license: CC-BY-SA-4.0
---

## 做法

### 一、先把旧形式摆出来

> `Review the equation of Newton's second law of motion.`
> `Point out the two different equations for the law.`

**教材的 `[OL]` 提示只做一件事**：告诉学生**这条定律有两种写法**。
它不解释，先把这个事实摆出来。

### 二、写出两种形式，并说明一种怎么推出来

> `Show the two different forms of Newton's second law and how one can be derived from the other.`

| 写法 | 形式 | 已知什么 |
|---|---|---|
| 熟悉的形式 | `F = m·a` | 力与**加速度**的关系 |
| 新的形式 | `F = Δp / Δt` | 力与**动量变化率**的关系 |

**推导只有两步**（`[AL]` 提示要求做出来）：

```
F = m·a            （旧形式）
a = Δv / Δt        （加速度的定义，来自本库已有的「加速度」节点）
⇒ F = m·Δv/Δt
    = Δ(mv)/Δt     （质量不变时，把 m 放进 Δ 里）
    = Δp / Δt      （p = mv 的定义）
```

**注意最后一步用到了「质量不变」**——所以两种形式的等价**有前提**。
（变质量情形，如火箭，就必须用 `F = Δp/Δt` 那一侧。）

### 三、用一个日常的碰撞把「方向」逼出来

> `Start a discussion about movement and collision. Using the example of football players,`
> `point out that both the mass and the velocity of an object are important considerations in`
> `determining the impact of collisions. The direction as well as the magnitude of velocity`
> `is very important.`

**教材选的两个球员相撞**，一句话里带上三件事：

| 要点 | 教材原话 |
|---|---|
| 质量算数 | `both the mass and the velocity` |
| 速度算数 | 同上 |
| **方向也算数** | `The direction as well as the magnitude of velocity is very important` |

### 四、量级上的对比

> `Explain that a large, fast-moving object has greater momentum than a smaller, slower object.`
> `This quality is called momentum.`

**教材在这里才给「动量」命名**——在讲完比较之后。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **AL**（本条的两条提示都标 `[AL]`；`[OL]` 只要求「指出有两种形式」） |
| 先修 | 牛顿第二定律（`F = ma`）；**加速度的定义**（推导要用） |
| 认知负荷 | 中——**代数只有两步，但要求学生接受「同一个定律有两种写法」** |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **还没把 `F = ma` 用熟**的学生 | 本做法建立在「旧形式已经熟了」之上；教材的 `[OL]` 提示第一句就是 `Review the equation` | **强**（教材把它列为第一条） |
| 不知道 `a = Δv/Δt` 的学生 | 推导的第二步直接用它——那是本库 [加速度](../concepts/加速度.md) 的内容 | **强**——由推导性质推出 |
| 本档（AL）**以外**的学生 | 教材为该段落标的就是 `[AL]`；`[OL]` 档只要求「指出有两种形式」，**不要求推导** | **中**——标签明确划了范围，但「未标」仍不等于「不适用」，只是**未经检验** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 讲成「`F = Δp/Δt` 是更高级的写法」 | **它们是同一个定律**。教材的措辞是 `Show … how one can be derived from the other`——**互相推得出来**，不是新旧替换 |
| 推导里**跳过「质量不变」这一步** | 那一步是唯一的前提。跳过它，学生以后遇到火箭、喷气这类**变质量**问题会推不出来 |
| 足球运动员的例子只讲「撞得疼」 | 教材要的是**三个因素**（质量、速度大小、速度方向）。只讲「疼」就把方向那一条丢了 |
| 在 `[OL]` 档要求推导 | 教材把 `[OL]` 与推导**分开了**：`[OL]` 只说「指出有两种形式」 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-045 | 教材（全文） | 低 | OpenStax《Physics》第 8 章 · Linear Momentum, Force, and Impulse，[m54215](https://github.com/openstax/osbooks-physics/blob/main/modules/m54215/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 AL 档指定（尚无攻击）

- **主张**：这是教材为进阶学生指定的做法
- **前提**：m54215 的 Teacher Support 把「两种形式 + 互相推导」标为 `[AL]`（ev-045）
- **推理**：分档标记即教材对该段落的指定
- **证据**：ev-045
- **被攻击**：**「教材指定」≠「实测有效」**；
  且**「两种形式」这条 `[OL]` 与推导那条 `[AL]` 在教材里是分开的两句**，
  本条目把它们组织成一条四步做法——**那层组织是本库加的**
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（#8 批量转换 · 第 7 批） | Issue #8 | @hpleapfrog |
