---
id: kb:physics:method-work-ol-what-counts
type: 教法
title: 功与功率 · 年级水平：让判据在反例上反复过一遍
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  适用: 容易把「累」当成「做功」的学生
  条件: 无
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[功与功率](../知识点/功与功率.md)"]
evidence: [ev-036]
license: CC-BY-SA-4.0
---

## 做法

**用一组反直觉例子把判据钉死，然后让学生自己继续找例子。**

教材原文（短引用）：

> `Make it clear why holding something off the ground or carrying something over a level surface
> is not work in the scientific sense.`

> `Ask the students to provide more examples until they understand the difference between
> the scientific term work and a task that is simply difficult but not literally work
> (in the scientific sense).`

**三步：**

| # | 动作 |
|---|---|
| 1 | 摆出两个反例：**举着不动**、**水平搬运** |
| 2 | 让学生**用能量方程解释**为什么这两个不算功 |
| 3 | **让学生自己继续举例子**，直到分清「科学意义上的功」与「只是很累的事」 |

教材同节还有一条配套要求：**讲清功、能量、力、距离的各自单位**，
并用机械能方程与功的方程**当场过一遍哪些是功、哪些不是**。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **OL**（教材标记 `[OL]`） |
| 先修 | 已知道机械能方程与 `W = F·d` |
| 认知负荷 | 中——负荷放在**用判据否掉直觉** |

## 禁忌

**对谁不适用？**

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| 还没有机械能方程的学生 | 教材的第 2 步是「**用机械能方程解释**」，没有它就只能靠记住结论 | **中** —— 教材明示 |
| 本档以外的学生 | 教材为各档**另给了不同做法**，未声明本做法可跨档 | **弱** —— 未经检验 |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 学生得出**「累的事都不做功」** | 判据是**力与位移**，不是累不累。跑步当然累，但**跑步是做功的**（有位移、有受力）。把反例推成通则就错了 |
| 「举着不动不做功」被当成「没有能量消耗」 | **肌肉确实在消耗化学能**（肌纤维反复微收缩）。科学意义上的『功』为零，**不等于身体没消耗** |
| 只讲两个反例就收 | 教材明确要求 `provide more examples **until** they understand`——**「直到」意味着两个例子不够** |

> [!IMPORTANT]
> **最后一条风险是本条目的要害。**
>
> 「举着不动不做功」会让学生的直觉和物理打起架来，因为**肌肉真的在烧能量**。
> 若不点破这层，学生要么否定物理，要么否定自己的感受。
>
> **正确的收口是**：物理上的功看**外力的作用效果**；
> 肌肉内部消耗的能量去向是**生理问题**，不是本判据的反例。

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-036 | 教材（全文） | 低 | OpenStax《Physics》第 9 章 · Work, Power, and the Work–Energy Theorem，[m54271](https://github.com/openstax/osbooks-physics/blob/main/modules/m54271/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 OL 档指定（尚无攻击）

- **主张**：这是教材为年级水平学生指定的做法
- **前提**：m54271 的 Teacher Support 用 `[OL]` 标记上述各条（ev-036）
- **推理**：分档标记即教材对该水平的指定
- **证据**：ev-036
- **被攻击**：**「教材指定」≠「实测有效」**；且教材**没有**处理「肌肉确实在耗能」这一层（我在 `风险` 里补上），
  说明教材的做法**可能不足以消除学生的抵触**
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（#8 批量转换 · 第 3 批） | Issue #8 | @hpleapfrog |
