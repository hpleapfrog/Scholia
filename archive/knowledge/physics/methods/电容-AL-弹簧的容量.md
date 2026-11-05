---
id: kb:physics:method-capacitance-al-spring
type: 教法
title: 电容 · 进阶：弹簧的容量由什么决定
status: 有效
author: "@hpleapfrog"
created: 2026-10-23
updated: 2026-10-23
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶水平（AL）
  适用: 已经会用 C = Q/U、想追问「电容由什么决定」的学生
  条件: 学生知道弹簧能储弹性势能
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[电容](../concepts/电容.md)"]
evidence: [ev-175]
license: CC-BY-SA-4.0
---

## 做法

教材给 `[AL]` 的是一条**完整的三问链**：

> `[AL] Discuss how a spring has a capacity to store mechanical energy. Discuss which properties of the spring would increase its capacity to store energy. Point out that these properties are intrinsic to the spring.`

三问各管一件事：

| 问 | 干什么 |
|---|---|
| 弹簧「存机械能」是什么 | 建立「容器有容量」这个直觉 |
| 哪些性质会让它存得更多 | 把容量**拆成可变的参数** |
| 这些性质是弹簧**自身**的 | 落点：**容量与「充了多少」无关** |

第三问是整条的落点。教材用的是 `Point out`（指出），说明它是**要被明确说出的结论**，
不是留给学生自己悟的。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **AL**（教材标 `[AL]`） |
| 先修 | 会用 `C = Q/U`；知道弹性势能 |
| 认知负荷 | 中到高——要同时握住「容器」「参数」「固有」三件事 |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **还没学过 `C = Q/U`** 的学生 | 三问链的落点（电容是固有量）要挂在公式上才说得清 | **强** |
| 刚接触电容、需要先建立「存什么」的学生 | 这属于 `[BL]/[OL]` 那条（查词典 → 储能类比），不是本条 | **强** |
| 需要做电容串并联计算的学生 | 本做法不产出计算 | **中** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 只讲「像弹簧」，不讲第三问 | 「容量是固有性质」才是落点；停在类比，学生会以为「充得多 → 电容大」 |
| 把「固有」说成「不变」 | 固有指**不随电荷变**，但换介质、改几何会变——教材本节后半就在讲介质 |
| 用弹簧的「硬软」代替「几何与介质」 | 弹簧性质只是**类比物**，对应的物理量是板间距、面积、介质常数 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-175 | 教材（全文） | 低 | OpenStax《Physics》第 18 章 · Capacitors and Dielectrics，[m63179](https://github.com/openstax/osbooks-physics/blob/main/modules/m63179/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 AL 档指定（尚无攻击）

- **主张**：这条三问链是教材为进阶学生指定的做法
- **前提**：m63179 的 Teacher Support 有 `[AL] Discuss … Discuss … Point out …` 三句（ev-175）
- **推理**：三问的顺序与落点都取自原文
- **证据**：ev-175
- **被攻击**：
  - **「教材指定」≠「实测有效」**
  - **「固有 ≠ 不变」这一层是我加的澄清**：教材只说 `intrinsic to the spring`，
    没有讨论「换介质会变」；那是我把本节后半（介质）拉进来补的
- **署名**：@hpleapfrog · 2026-10-23

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-23 | 建立条目：从 m63179 摘出 `[AL]` 三问链 | `tools/os_source.py 电容` 取原文通读（ev-175） | @hpleapfrog |
