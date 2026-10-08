---
id: kb:physics:method-acceleration-al-rate
type: 教法
title: 加速度 · 进阶：用「变化率的变化率」读一句绕口的话
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: 已能算加速度、但把「增大 / 减小」当成一层概念的学生
  条件: 已接触矢量与标量的区分
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[加速度](../知识点/加速度.md)"]
evidence: [ev-039]
license: CC-BY-SA-4.0
---

## 做法

### 一、先查矢量还在不在

> `See how much students remember about vectors. What does a vector arrow represent?`
> `Ask them to name some quantities that are vectors and some that are scalars.`

**这是本节 AL 的第一条**——教材把「矢量/标量」当成一个**需要回头检查**的前提，
而不是已经过去的事。

### 二、拿一句绕口的日常话当靶子

> `See if students can use the concept of acceleration to understand confusing statements such`
> `as "a decrease in the rate of increase."`
> `For example, use the concept of acceleration to analyze the statement "the rate of increase`
> `in the cost of health care is decreasing." If the increase in the cost is defined as positive,`
> `then the acceleration in the cost of health care would be negative.`

**这条做法的价值在于：它把两层变化率搬到物理之外，让学生用刚学的工具去解一句汉语。**

| 那句话说的是 | 对应到物理 |
|---|---|
| 「医疗费用**在增长**」 | 速度为正 |
| 「**增长的速率在下降**」 | **加速度为负** |
| 「费用**仍然在涨**」 | 速度**仍然为正** |

**结论是反直觉的**：**费用还在涨，但加速度已经是负的。**
学生必须把「涨/跌」与「涨得快/涨得慢」分成两层，才能读懂这句话。

### 三、顺带把基本单位串一遍

> `Review all the base units of the metric system. Explain how these units are interrelated.`
> `For example, show how length is defined by time.`

**「长度由时间定义」在现代计量里是真的**（米的定义基于光速与秒）——
教材用它说明**单位不是各自独立的**。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **AL**（教材标记 `[AL]`） |
| 先修 | 矢量与标量；加速度的定义 |
| 认知负荷 | 中高——难点是**把物理量映射到日常语言的两层结构上** |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **还没分清矢量与标量**的学生 | 教材把「查矢量」放在本节 AL 的第一条——**它是前提** | **强**（教材把它列为第一条） |
| 还没掌握基本单位、只靠公式记忆的学生 | 第二条做法要调动单位之间的关系 | **中** |
| 本档（AL）**以外**的学生 | 教材为该段落标的就是 `[AL]`；BL 与 OL 档另给了不同建议 | **中**——标签明确划了范围，但「未标」仍不等于「不适用」，只是**未经检验** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 那个经济学的例子被当成物理题 | **它的作用是语言分析**，落点是「两层变化率」。套数值算一遍就把它的功能丢了 |
| 讲成「增长率下降就是下降了」 | **恰恰相反**：费用**仍在涨**。这一条做法的全部意义就在这个反差上 |
| 矢量检查跳过 | 教材把它放在第一条，说明**它预期学生会忘**。跳过就等于把后面的分析建在沙上 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-039 | 教材（全文） | 低 | OpenStax《Physics》第 3 章 · Acceleration，[m54123](https://github.com/openstax/osbooks-physics/blob/main/modules/m54123/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 AL 档指定（尚无攻击）

- **主张**：这是教材为进阶学生指定的做法
- **前提**：m54123 的 Teacher Support 用 `[AL]` 标记上述各条（ev-039）
- **推理**：分档标记即教材对该段落的指定
- **证据**：ev-039
- **被攻击**：**「教材指定」≠「实测有效」**；
  且**那条经济学例句是美国的语境**（医疗费用），**换成中国学生的语境需要改写**——
  这是本库[覆盖度对照](../覆盖度/README.md) 里记的「教法来源是一本美国教材」的一个**具体实例**
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（#8 批量转换 · 第 5 批） | Issue #8 | @hpleapfrog |
