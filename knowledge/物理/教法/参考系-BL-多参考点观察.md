---
id: kb:physics:method-frame-bl-multi-viewpoint
type: 教法
title: 参考系 · 低于年级水平：多个参考点并置观察
knowledge_point: ["[参考系](../知识点/参考系.md)"]
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 低于年级水平（BL）
  适用: 能描述方向与位置，但未建立坐标概念的学生
  条件: 有可操作的实物
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a1)"]
  攻击: []
evidence: [ev-021]
license: CC-BY-SA-4.0
---

## 做法

**不先给定义**，而是让学生从多个位置描述同一个运动：

1. 把一本书从课桌一端推到另一端
2. 让不同学生分别从**自己的位置**、**书的位置**、**另一位同学的位置**描述它的运动方向
3. 三个描述互相矛盾 → 引出「描述运动必须先说明从哪看」

教材原文（短引用）：

> `slide a book across a desk. Ask students to describe its motion from their reference point,
> from the book's reference point, and from another student's reference point.`

**要点**：矛盾是**故意制造的**。学生不是被告知「需要参考系」，而是**自己撞上**这个需求。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **BL**（教材标记 `[BL]`） |
| 先修 | 能描述方向与位置；**不需要**坐标或矢量概念 |
| 设备 | 一本书即可 |
| 认知负荷 | 低——负荷放在**观察与表达**，不在符号 |

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
| **学生把参考系理解成「背景」** | 教材明确列出这个误解：`Students may assume that a reference frame is a background of motion instead of the frame from which motion is viewed` | 教材同节 Misconception 标注 |
| 只演示、不点破 | 三个描述不一致**不会自动**产生「参考系」概念，必须由教师明确收口 | — |

> [!IMPORTANT]
> 教材**没有**声明此做法对 OL / AL 学生不适用——它为那些水平**另给了不同做法**。
> **「未标注禁忌」不等于「已确认适用」**，两者不能混。

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-021 | 教材（全文） | 低 | OpenStax《Physics》§2.1 Relative Motion, Distance, and Displacement，[m54108](https://github.com/openstax/osbooks-physics/blob/main/modules/m54108/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 BL 档指定（存活）

- **主张**：该做法是教材为低于年级水平学生指定的教学路径
- **前提**：m54108 的 Teacher Support 用 `[BL]` 标记该建议（ev-021）
- **推理**：教材按水平分档给出建议，`[BL]` 即为其对低水平档的指定做法
- **证据**：ev-021
- **被攻击**：**「教材为 BL 档指定」≠「实测对 BL 档有效」**。没有效果量、没有样本量
- **署名**：@hpleapfrog · 2026-10-05
- **待补**：课堂实测数据

## 变更记录



| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（采集候选转入） | Issue #8 | @hpleapfrog |
| 2026-10-05 | 拆分 `禁忌` / `风险`：原 `禁忌` 里装的是**风险**，已移入 `风险`；并补上真正的人群禁忌（含证据强度标注） | [Issue #13](https://github.com/hpleapfrog/Scholia/issues/13) | @hpleapfrog |
