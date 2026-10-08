---
id: kb:physics:method-acceleration-ol-sign
type: 教法
title: 加速度 · 年级水平：正负与那个不用的词
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  适用: 刚接触 a = Δv/Δt、正把「负加速度」读成「减速」的学生
  条件: 已学过位移与速度
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[加速度](../知识点/加速度.md)"]
evidence: [ev-039]
license: CC-BY-SA-4.0
---

## 做法

教材的 `[OL]` 提示**不先给公式**，而是先处理两个词。

### 一、从学生自己的例子开始

> `Begin a general discussion about acceleration and deceleration. Ask for examples of both.`
> `Lead students to their topics of interest, such as motor vehicles or sports.`

**注意它要的例子是「加速与减速两种」**——先让学生把日常用法全部倒出来。

### 二、然后说「减速」这个词在物理里不用

> `Explain that deceleration is not used in physics because acceleration is either`
> `positive or negative.`

**这一步的作用是让「-2 m/s²」不再是「减速」的同义词。**
教材在后面的提示里**又说了一遍**（见第四条），说明只讲一次不够。

### 三、`Δ` 与下标的对应关系要可视化

> `Explain that the capital Greek letter delta always means final minus initial and that the net`
> `change may be zero, positive, or negative.`
> `Use the equation a ¯ = Δv Δt = v f − v 0 t f − t 0 to emphasize the relationship between`
> `Δ and the subscripts f and 0.`

**教材用书写形式本身来讲**：把 `Δv` 与 `v_f − v_0` 并排写，让对应关系自己显出来。

### 四、再讲一遍那个词，并把「负」归给坐标方向

> `Be sure students understand that the word deceleration is not used in physics and that`
> `acceleration may be either positive or negative.`

**同一条提示里还带了另外两件事**：

> `Distinguish between constant and variable acceleration. There could be confusion here,`
> `especially in the case of increasing acceleration.`

（「越来越大的加速度」最容易混——**变的是加速度本身，不是速度**。）

> `Verify that the students know the SI units ... Explain the meaning of seconds squared`
> `in the denominator of the units of acceleration.`

（`m/s²` 的分母**不是面积**。）

### 五、最后，也是最重要的一条：箭头反向的图像解释

> `The arrow for acceleration that points opposite to the arrow for velocity may be confusing.`
> `Explain that the acceleration arrow points in the direction opposite the velocity because`
> `the velocity is getting smaller, i.e., the velocity arrow is getting shorter.`

**教材不给新的公式，给的是一个可以看见的动作**——**速度箭头在变短**。

### 六、算之前先查三件事

> `Before beginning the calculations, verify that students understand the equation for`
> `acceleration. Do they understand what it means when quantities have a plus or minus sign?`
> `Do they understand the units for each variable?`

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **OL**（教材标记 `[OL]`） |
| 先修 | 位移、速度；能带入公式做一步除法 |
| 认知负荷 | 中——难点不在算，在**符号与方向的对应** |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **还没建立「速度有方向」**的学生 | 本做法第五条的全部力气在**两个箭头的方向关系**上；只把速度当数字看，这一条无从讲起 | **强**——由做法性质推出 |
| 只想快点代公式算题的学生 | 本做法**先花时间处理用词**，不产出解题速度 | **中** |
| 本档（OL）**以外**的学生 | 教材为该段落标的就是 `[OL]`；BL 与 AL 档另给了不同建议 | **中**——标签明确划了范围，但「未标」仍不等于「不适用」，只是**未经检验** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 把「减速」当成不严谨的口语而随便用 | 教材的措辞是 `is not used in physics`——**这是一个术语规定，不是风格偏好**。老师自己用「减速」就把这一节毁了 |
| 「负加速度 = 减速」 | 这正是教材要破的等式。**负号取决于坐标方向**，向前运动配向后加速度是减速，向后运动配向后加速度是加速 |
| 「加速度变大」讲成「速度变大」 | 教材专门点了 `especially in the case of increasing acceleration`。**变的是变化率** |
| 箭头反向用公式解释 | 教材给的是 `the velocity arrow is getting shorter`——**图像说法**。换回公式回答就把简单问题复杂化了 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-039 | 教材（全文） | 低 | OpenStax《Physics》第 3 章 · Acceleration，[m54123](https://github.com/openstax/osbooks-physics/blob/main/modules/m54123/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 OL 档指定（尚无攻击）

- **主张**：这是教材为年级水平学生指定的做法
- **前提**：m54123 的 Teacher Support 用 `[OL]` 标记上述各条（ev-039）
- **推理**：分档标记即教材对该段落的指定
- **证据**：ev-039
- **被攻击**：**「教材指定」≠「实测有效」**；本条没有任何课堂数据
- **署名**：@hpleapfrog · 2026-10-05
- **待补**：**这条教法在中国课堂上是否同样有效，本库没有数据**——
  见 [覆盖度对照](../覆盖度/README.md) 里记的那个问题

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（#8 批量转换 · 第 5 批） | Issue #8 | @hpleapfrog |
