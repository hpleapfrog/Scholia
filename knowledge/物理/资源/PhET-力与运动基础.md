---
id: kb:physics:resource-phet-forces-and-motion-basics
type: 资源
title: PhET 模拟「力与运动：基础」
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  资源类型: 交互式模拟（浏览器内运行）
  适用: 讲平衡/不平衡的力与摩擦力
  条件: 需要能打开网页的设备
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-029]
license: CC-BY-SA-4.0
---

## 定位

| 项 | 值 |
|---|---|
| 资源名 | PhET Interactive Simulations — **Forces and Motion: Basics** |
| 直达链接 | <https://phet.colorado.edu/sims/html/forces-and-motion-basics/latest/forces-and-motion-basics_en.html> |
| 教材内的入口 | `https://openstax.org/l/forcesandmotion`（短链，实测解析到上面那个直达链接） |
| 教材出处 | OpenStax《Physics》第 4 章 · Newton's First Law: Inertia，模块 [m54138](https://github.com/openstax/osbooks-physics/blob/main/modules/m54138/index.cnxml) |
| 运行方式 | 浏览器内运行，**无需安装** |
| 归属学科 | [惯性](../知识点/惯性.md) |

### 许可（**重要**）

> [!CAUTION]
> **本资源是 `CC BY-NC 4.0`（NonCommercial），不是 `CC BY`。**
>
> 从模拟文件自身的头部核实（权威来源——产物自带声明）：
>
> > `This file is licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).`
> >
> > `COMMERCIAL USE REQUIRES A COMMERCIAL LICENSE AGREEMENT FROM THE UNIVERSITY OF COLORADO BOULDER.`
>
> **另外三个 PhET 模拟抽查结果相同**（my-solar-system / bending-light / color-vision），
> 说明这是统一政策，不是个例。

> [!IMPORTANT]
> **许可不随教材传播。**
>
> 教材 OpenStax《Physics》是 **CC BY 4.0**，但它**内嵌**的 PhET 模拟仍是 **CC BY-NC 4.0**。
> 「教材可以自由复用」**不能推出**「教材里嵌的东西也可以」。
>
> 这是一个**真实的许可陷阱**：照抄教材结构的再发布者会踩到。

### 引用时必须写的归属

模拟文件自带的推荐措辞（**要求在「使用处附近」标注**）：

> Simulation by PhET Interactive Simulations, University of Colorado Boulder,
> licensed under CC BY-NC 4.0 (<https://phet.colorado.edu>)

> [!NOTE]
> **本条目不是该资源的副本，只是定位与用法说明。**
> 本库的 `CC-BY-SA-4.0` 适用于**本条目我们写下的文字**，
> **不适用于**被链接的 PhET 模拟。

## 用法

教材正文里有一整段 `virtual-physics` 说明（短引用 + 归纳）：

**第一屏：拔河**
> `placing blue people on the left side of a tug-of-war rope and red people on the right side`

改变两侧人数与体型，观察对**净力**的影响，按 `Go!` 开始。**这是「平衡 / 不平衡的力」的具身演示。**

**第二屏：摩擦（`Friction` 标签页）**
> `Slide the applied force button … See the arrow representing friction change in magnitude and direction`

拖动力的大小，观察**摩擦箭头随外力的变化**；再调整摩擦系数看运动如何改变。

> [!TIP]
> **第二屏与本库一条误解直接对应。**
>
> [运动物体自然慢下来](../误解/运动物体自然慢下来.md) 的要害在于：
> 学生把**摩擦的效应当成了物体自身的属性**。
>
> 这个模拟让学生**把摩擦当成一个可以调大调小的量**，而不是背景条件——
> 摩擦一调小，物体就滑得更远。**误解赖以成立的「物体自己会停」在这个界面上站不住。**

## 论证

### R1 · 为什么这条资源值得收录（存活）

- **主张**：该模拟的教学价值**超过**「一个可以点的动画」
- **前提**：教材把它的两屏分别对准了**净力**与**摩擦力**两个概念；
  而本库已记录一条与之直接相关的误解（ev-028）
- **推理**：能让学生**亲手改变**干扰变量（摩擦）的资源，
  比只能观察的解释更可能拆掉「物体自己会停」这一归因错误
- **证据**：ev-029、ev-025（该节的教材教学提示）、ev-028（误解来源）
- **被攻击**：
  - **「更可能」是我的推断，没有课堂数据**——本库没有该模拟的使用效果测量
  - 教材把它排在该节，**不等于**它比讲授更有效
- **署名**：@hpleapfrog · 2026-10-05
- **待补**：使用该模拟前后的归因测试

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目：本库**第一条 `资源` 条目**，实测该对象类型 | 采集扩展 | @hpleapfrog |
