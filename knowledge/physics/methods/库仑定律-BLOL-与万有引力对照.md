---
id: kb:physics:method-coulomb-blol-compare
type: 教法
title: 库仑定律 · 低于/年级水平：和万有引力逐项对照
status: 有效
author: "@hpleapfrog"
created: 2026-10-22
updated: 2026-10-22
scope:
  学科: 物理
  学段: 高中
  水平档: 低于年级水平（BL）至 年级水平（OL）
  适用: 已经知道万有引力定律、正要学库仑定律的学生
  条件: 学生已学过 F = Gm₁m₂/r²
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[库仑定律](../concepts/库仑定律.md)"]
evidence: [ev-085]
license: CC-BY-SA-4.0
---

## 做法

教材在这个模块的 `[BL]` / `[OL]` 提示**不先讲公式，先讲「像什么」**。

### 一、先把两件事并排放

> `This section presents Coulomb's law and points out its similarities and differences with respect to Newton's law of universal gravitation.`

教材明确要求**逐项对照**，而且给好了两张清单：

| 相同 | 不同 |
|---|---|
| 都是平方反比 | **质量只能为正；电荷可正可负** |
| 「质量」与「电荷」在各自定律里扮演同一种角色 | — |

> `The similarities include the inverse-square nature of the two laws and the analogous roles of mass and charge. The differences include the restriction of positive mass versus positive or negative charge.`

### 二、再做一次时间上的对照

> `[BL] [OL] Discuss how Coulomb described this law long after Newton described the law of universal gravitation.`

**注意教材要的是「讨论」，不是「讲述」。** 它把「晚」这件事当成一个**可以问的问题**，
而不是一条要背的年代信息（`[AL]` 档把这个问句直接写出来了，见另一条教法）。

### 三、顺手点掉一个读法陷阱

> `Point out how the subscripts 1, 2 means the force on object 1 due to object 2 (and vice versa).`

下标不是编号顺序，是**「谁受谁施」**。教材把它当默认会被读错的东西，所以要求 `Point out`。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **BL / OL**（教材同一条提示同时标了这两档） |
| 先修 | 已学万有引力定律；知道平方反比 |
| 认知负荷 | 低到中——负荷在**对照表**上，不在代数上 |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **没学过万有引力定律**的学生 | 本做法的全部结构是「与万有引力对照」——**没有对照物，它就只剩一句公式** | **强**（由做法性质推出） |
| 要立刻练库仑力计算的学生 | 本做法不产出计算熟练度，只建立「像哪个」 | **中** |
| 本档（BL/OL）**以外**的学生 | 教材 `[AL]` 另给了问句（「为什么更晚」），与本条不同 | **中** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 只讲「都是平方反比」，不讲**差别** | 教材给的两栏里，**差别那一栏才是易错点**（质量恒正、电荷可负 → 引力只有吸引，库仑力可吸可斥） |
| 把「库仑比牛顿晚」讲成年代故事 | 教材用的是 `Discuss how…`，落点是**为什么晚**这个疑问，不是年份 |
| 下标一带而过 | 教材专门要求 `Point out`，说明它默认会被读成「第 1 个和第 2 个」 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-085 | 教材（全文） | 低 | OpenStax《Physics》第 18 章 · Coulomb's Law，[m54414](https://github.com/openstax/osbooks-physics/blob/main/modules/m54414/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 BL/OL 档指定（尚无攻击）

- **主张**：这是教材为低于年级水平与年级水平学生指定的做法
- **前提**：m54414 的 Teacher Support 用 `[BL] [OL]` 标记「讨论库仑比牛顿晚」这一条，
  并显式要求逐项列出与万有引力定律的异同（ev-085）
- **推理**：分档标记即教材对该段落的指定；两栏清单是教材原文，不是我的归纳
- **证据**：ev-085
- **被攻击**：
  - **「教材指定」≠「实测有效」**：本条没有任何课堂数据
  - **对照表的两栏是教材原话的直译**，但「质量恒正→只能吸引」这一步是我补的推论，
    教材只写到 `restriction of positive mass versus positive or negative charge`
- **署名**：@hpleapfrog · 2026-10-22

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-22 | 建立条目：从 m54414 的 Teacher Support 摘出 BL/OL 做法 | 抓取 OpenStax 源仓库 cnxml 通读（ev-085） | @hpleapfrog |
