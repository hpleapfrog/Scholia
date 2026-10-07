---
id: kb:physics:method-refraction-al-prism
type: 教法
title: 折射 · 进阶：棱镜分光，窗玻璃为什么不分
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: 已经会用 n = c/v 与折射定律、正要理解色散的学生
  条件: 已能用正弦 / 反正弦做简单计算
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[光的折射](../知识点/光的折射.md)"]
evidence: [ev-038]
license: CC-BY-SA-4.0
---

## 做法

### 一、抛出一个用同一套公式才能回答的对比

> `Ask students to try to explain why a prism separates white light into a rainbow of colors,`
> `but a window pane does not.`
> `If they cannot explain it, show them a ray diagram of light transmitted through a flat`
> `sheet of glass.`

**注意教材给的后手**：如果学生答不出，**不是直接讲答案，而是给一张光路图**。

| | 棱镜 | 窗玻璃 |
|---|---|---|
| 两个界面 | **不平行**（成角） | **平行** |
| 各色光偏折 | 每经过一个界面就**再分开一点**，两次偏折**方向叠加** | 第二次偏折**抵消**第一次 |
| 出去以后 | 各色光**分开** | **合成一束**，与入射方向平行 |

**同一个 `n` 与同一个折射定律，两块玻璃的行为不同——差别只在几何。**

### 二、先在直角三角形的层面上把正弦说清

> `The trigonometric function sine (sin) for a given angle is the ratio of the side of a right`
> `triangle opposite that angle to the hypotenuse of that triangle.`

**这是教材为 AL 档补的**——说明在 OL 档它**假定**学生已经会了。

### 三、把五个特殊角排成规律

> `Show why the values sin 0°, sin 30°, sin 45°, sin 60°, and sin 90° can be expressed in the`
> `form ½√0, ½√1, ½√2, ½√3, ½√4.`
> `Show that the numerical values of these expressions are 0, 0.5, 0.707, 0.866, and 1.00.`

**这个形式的用处**：学生不必单独记五个数，只要记住**根号里依次填 0 到 4**。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **AL**（教材标记 `[AL]`） |
| 先修 | 折射定律；正弦与反正弦；**光路图的读法** |
| 认知负荷 | 高——要同时握住**两界面几何**与**逐色偏折** |

## 禁忌

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **还不会用折射定律做两界面计算**的学生 | 棱镜的答案是**两次偏折的叠加**——只会算一次就不够 | **强**——由做法性质推出 |
| 还没建立「白光是混合光」概念的学生 | 本做法解释的是**为什么各色会分开**，前提是它们**本来就不同** | **中** |
| 本档（AL）**以外**的学生 | 教材为该段落标的就是 `[AL]`；BL 与 OL 档另给了不同建议 | **中**——标签明确划了范围，但「未标」仍不等于「不适用」，只是**未经检验** |

## 风险

| 会翻车的地方 | 为什么 |
|---|---|
| 把答案直接讲了 | 教材的写法是**先让学生试着解释**，答不出才给光路图——**那张图是提示，不是答案** |
| 说成「棱镜能让光变色」 | 棱镜**不改变任何一色光**，只是**让本来混在一起的分开**。这是色散最常见的错误说法 |
| 「窗玻璃不折射」 | 窗玻璃**照样折射**，只是**两次偏折方向相反、互相抵消**。讲成「不折射」会把已学的定律推翻 |
| 五个特殊角变成纯记忆负担 | 教材给的是**结构**（`½√n`），不是五个孤立的值 |

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-038 | 教材（全文） | 低 | OpenStax《Physics》第 16 章 · Refraction，[m54365](https://github.com/openstax/osbooks-physics/blob/main/modules/m54365/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 AL 档指定（尚无攻击）

- **主张**：这是教材为进阶学生指定的做法
- **前提**：m54365 的 Teacher Support 用 `[AL]` 标记上述各条（ev-038）
- **推理**：分档标记即教材对该段落的指定
- **证据**：ev-038
- **被攻击**：**「教材指定」≠「实测有效」**；
  且教材原文的 `show them a ray diagram` **指向正文里的一张图**，
  本条目**没有复制那张图**（版权红线，见 `CONTRIBUTING.md`）——
  实施者需要自己去教材对应位置取
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（#8 批量转换 · 第 4 批） | Issue #8 | @hpleapfrog |
