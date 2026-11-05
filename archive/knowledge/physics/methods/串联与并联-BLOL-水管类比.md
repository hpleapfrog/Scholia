---
id: kb:physics:method-series-parallel-blol-water-analogy
type: 教法
title: 串联与并联 · 低于/年级水平：把水管类比讲完整
status: 有效
author: "@hpleapfrog"
created: 2026-10-23
updated: 2026-10-23
scope:
  学科: 物理
  学段: 高中
  水平档: 低于年级水平（BL）至 年级水平（OL）
  适用: 刚画第一张电路图、需要先把符号认全的学生
  条件: 学生知道电流与电压
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[串联与并联](../concepts/串联与并联.md)"]
evidence: [ev-166, ev-167]
license: CC-BY-SA-4.0
---

## 做法

教材不假设学生记得水管类比，而是**要求教师先复习一遍，并逐项对到电路符号上**：

> `Review the analogy between water flow and electric current to ensure that students understand it.`

对照的**四组**，教材一条条点名：

| 水 | 电 |
|---|---|
| 高压下挤在一起的水分子 | 高电压下挤在一起的电荷 |
| 水泵提高水压 | 电池提高电压 |
| **滤沙器**（阻碍流动） | **电阻** |
| **水库**（水位基准） | **接地**（`V_ground ≡ 0`） |

> `Explain that the water pump increases the water pressure and that the battery increases the voltage. Other comparisons to discuss include the resistor versus the sand filter, and the ground versus the reservoir.`

接着才落到四个基本符号：导线、电池、电阻、接地。**优先级是反的**：
教材先类比再讲符号，因为它默认符号本身没有意义。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **BL / OL**（这段是符号教学的铺垫） |
| 先修 | 电流、电压 |
| 认知负荷 | 低——全是熟事物映射 |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **已经能读写电路图**的学生 | 类比是入场券，不是内容 | **中** |
| 需要做串并联等效电阻计算的学生 | 本做法不产出计算，只建立符号意义 | **中** |
| 本档以外 | 教材此段未分档；`[AL]` 另在别处 | **弱**（未标不等于不适用） |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 类比讲到「水用完了」就停 | 水会流光，**电荷不会**——「电流被消耗」是这套类比最常见的误带 |
| 只对「水泵↔电池」这一组 | 教材点了四组；少一组（尤其**接地↔水库**），`V=0` 这个约定就没由来 |
| 先讲符号再补类比 | 符号在教材里是**类比的产物**，顺序反了，学生只能靠背 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-166 | 教材（全文） | 低 | OpenStax《Physics》第 19 章 · Series Circuits，[m54435](https://github.com/openstax/osbooks-physics/blob/main/modules/m54435/index.cnxml) | **CC BY 4.0** |
| ev-167 | 教材（全文） | 低 | OpenStax《Physics》第 19 章 · Parallel Circuits，[m54442](https://github.com/openstax/osbooks-physics/blob/main/modules/m54442/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材指定先复习类比（尚无攻击）

- **主张**：教材要求先复习水管类比、逐项对到符号，再讲符号
- **前提**：m54435 的 Teacher Support 用 `Review the analogy … to ensure that students understand it`，
  并列出水泵/滤沙器/水库三组对应（ev-166）
- **推理**：顺序与四组对应都取自原文
- **证据**：ev-166 · ev-167
- **被攻击**：
  - **「教材指定」≠「实测有效」**
  - **「电流被消耗」这个误带是我补的风险**：教材没点名它
  - **接地↔水库**这一组在原文里是 `ground versus the reservoir`，我把它接到 `V_ground ≡ 0` 上，
    这一步跨了两段，属于我的连接
- **署名**：@hpleapfrog · 2026-10-23

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-23 | 建立条目：从 m54435 摘出水管类比四组对应 | `tools/os_source.py 串联与并联` 取原文（ev-166/167） | @hpleapfrog |
