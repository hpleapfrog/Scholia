---
id: kb:physics:method-refraction-ol-equation
type: 教法
title: 折射 · 年级水平：这个规律用方程说比用文字说容易
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  适用: 已经学过反射定律、正要学折射定律的学生
  条件: 已接触过正弦函数
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[光的折射](../知识点/光的折射.md)"]
evidence: [ev-038]
license: CC-BY-SA-4.0
---

## 做法

### 一、把「反射说得清、折射说不清」这件事讲出来

> `Explain that, unlike the law of reflection, the law of refraction is most easily expressed`
> `as an equation, rather than in words.`

**教材主动做了这个对比。** 它的作用有两个：

1. **解释为什么这里必须出现正弦**——不是老师偏爱公式，是**这件事用话说不了**
2. **把反射与折射区别开**——它们是**性质不同的两个规律**，不是同一件事的两个例子

### 二、用割草机推一遍

> `Walk students through the lawnmower analogy in .`
> `Suggest other wheeled vehicles with which they may be more familiar, and other surfaces,`
> `such as sand.`

（教材正文里给出的类比：一台割草机**斜着**从水泥地开上草地，
一侧轮子先进入草地而减速，整台机器就会**转向**。）

**教材要求把这个类比再往前推**：让学生换别的带轮子的东西、别的表面（如沙地）。

### 三、钉死那个最容易错的记号

> `The superscript in sin−1 is not a power. It indicates arcsine, which is an inverse`
> `trigonometric function. It means, "that angle whose sine equals (in this case) (n2/n1)."`

**教材用一整条提示处理这一个上标。** 并给出了可直接说出口的读法——
「**正弦等于 `n₂/n₁` 的那个角**」。

### 四、把正弦与反正弦的区别、以及「无量纲」讲清

> `Explain the difference between sine and arcsine. Explain why sin 90° = 1.`
> `Note that the index of refraction is a dimensionless number.`

### 五、一个该背的值

> `Remind students that the maximum speed of light is its speed in a vacuum.`
> `This is a fundamental constant of physics. The maximum speed of light is equal to`
> `3.00 × 10⁸ m/s. Have your students memorize this value.`

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **OL**（教材标记 `[OL]`） |
| 先修 | 反射定律；正弦函数；知道光在真空中的速度 |
| 教具 | 无（割草机是语言类比，可换成任何带轮子的东西） |
| 认知负荷 | 中高——**同时处理三角函数记号与物理规律** |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **还没学过正弦函数**的学生 | 本条的做法建立在「正弦是什么」之上；教材另有一条 `[AL]` 提示才讲正弦的定义——**说明它不是默认已知** | **强**——由做法性质推出 |
| 还没学过反射定律的学生 | 教材的第一句就是 `**unlike** the law of reflection`——**对照是本做法的支点** | **中**（教材把反射放在同一章的前面） |
| 本档（OL）**以外**的学生 | 教材为该段落标的就是 `[OL]`；BL 与 AL 档另给了不同建议 | **中**——标签明确划了范围，但「未标」仍不等于「不适用」，只是**未经检验** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| `sin⁻¹` 讲成「正弦的负一次方」 | **这是教材专门用一条提示防的错误**。而且 `sin⁻¹(x)` 与 `1/sin(x)` 数值完全不同 |
| 割草机类比只讲不推 | 教材明确要求 `Suggest other wheeled vehicles … and other surfaces`——**要让学生自己把它推广出去** |
| 「折射只能用方程说」被讲成「折射更难」 | 教材说的是**表述方式**，不是难度。反射也有三线共面、角相等这些可陈述的规律 |
| 忘了 `n` 是无量纲的 | `n = c/v` 是两个速度相除——学生会想给它加个单位 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-038 | 教材（全文） | 低 | OpenStax《Physics》第 16 章 · Refraction，[m54365](https://github.com/openstax/osbooks-physics/blob/main/modules/m54365/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 OL 档指定（尚无攻击）

- **主张**：这是教材为年级水平学生指定的做法
- **前提**：m54365 的 Teacher Support 用 `[OL]` 标记上述各条（ev-038）
- **推理**：分档标记即教材对该段落的指定
- **证据**：ev-038
- **被攻击**：**「教材指定」≠「实测有效」**；割草机类比的实际效果没有任何数据
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（#8 批量转换 · 第 4 批）；同时答了 [光的反射](../知识点/光的反射.md) `K7` 的合并问题 | Issue #8 | @hpleapfrog |
