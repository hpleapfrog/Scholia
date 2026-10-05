---
id: kb:physics:method-ptgraph-al-boundary-cases
type: 教法
title: 位置-时间图 · 进阶：用边界情形逼问理想化
knowledge_point: ["[位置-时间图](../知识点/位置-时间图.md)"]
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: 已能读斜率、可质疑模型假设的学生
  条件: 学生已分析过至少一张已画好的位置-时间图
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-023]
license: CC-BY-SA-4.0
---

## 做法

**在学生已经看懂一张图之后**，用一串边界情形逼他们面对「模型是理想化的」：

教材给的三连问（短引用）：

> `Once the students have looked at and analyzed the graph, see if they can describe different
> scenarios in which the lines would be straight instead of curved? Where the lines would be
> discontinuous?`

> `Is it realistic to draw any position graph that starts at rest without some curve in it?
> Why might we be able to neglect the curve in some scenarios?`

再往上一层（同节另一条 `[AL]`）：**曲线是「斜率的斜率」**——引出下一章的加速度。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **AL**（教材标记 `[AL]`） |
| 先修 | 已能读直线斜率 = 速度；已分析过至少一张图 |
| 认知负荷 | 高——负荷放在**质疑模型假设**（为什么可以忽略那段曲线） |

## 禁忌

**对谁不适用？**

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| 本档以外的学生 | 教材为 BL / OL / AL **各给了不同做法**，未声明本做法可跨档 | **弱** —— 「教材未指定」≠「不适用」，只是**未经检验** |

> [!WARNING]
> **本条没有强证据支撑的人群禁忌。**
>
> 教材只为本档给出建议，**没有说本做法对别的档位无效**。
> 把「教材没提」当成「不适用」是**过度推断**——这里如实标为**弱**，不编造。

## 风险

| 会翻车的地方 | 为什么 | 出处 |
|---|---|---|
| **过早引入「斜率的斜率」** | 教材把加速度放在**下一章**。此处只作「预告」，展开会把本章目标带偏 | 教材同节 `[AL]` 措辞为 `a preview of acceleration` |
| 学生把「理想化」当成「假」 | 「可以忽略那段曲线」不是「曲线不存在」。若不点破，学生会走到相对主义 | — |

> [!WARNING]
> 这条做法在**没有操作过真实测量**的班级里价值很低。
> 教材的这一步建立在学生**已经做过实验、见过真实曲线的抖动**之上——
> 直接跳到哲学式的追问，学生会答不出来。

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-023 | 教材（全文） | 低 | OpenStax《Physics》§2.3，[m54110](https://github.com/openstax/osbooks-physics/blob/main/modules/m54110/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 AL 档指定（存活）

- **主张**：边界情形追问是教材为进阶学生指定的做法
- **前提**：m54110 的 Teacher Support 用 `[AL]` 标记该组问句（ev-023）
- **推理**：分档标记即教材对该水平的指定
- **证据**：ev-023
- **被攻击**：**指定 ≠ 实测有效**；且本条依赖先前实验经验这一前置条件，教材未显式声明
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录



| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（采集候选转入） | Issue #8 | @hpleapfrog |
| 2026-10-05 | 拆分 `禁忌` / `风险`：原 `禁忌` 里装的是**风险**，已移入 `风险`；并补上真正的人群禁忌（含证据强度标注） | [Issue #13](https://github.com/hpleapfrog/Scholia/issues/13) | @hpleapfrog |
