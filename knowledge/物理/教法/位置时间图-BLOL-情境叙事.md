---
id: kb:physics:method-ptgraph-bl-ol-narrative
type: 教法
title: 位置-时间图 · 低于/年级水平：情境叙事 → 学生画图
knowledge_point: ["[位置-时间图](../知识点/位置-时间图.md)"]
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 低于年级水平 / 年级水平（BL / OL）
  适用: 尚未建立图像与运动对应关系的学生
  条件: 有一个具体、可想象的运动情境
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a1)"]
  攻击: []
evidence: [ev-023]
license: CC-BY-SA-4.0
---

## 做法

**不从坐标轴讲起，从一个故事讲起。**

教材给的叙事：发射一枚水火箭，升到 150 ft，停一下，然后落回地面。然后依次问：

1. **零点放哪里**？
2. **正方向是哪边**？负方向呢？
3. 让一名学生**把情境画在黑板上**
4. 再带全班一起画**位置-时间图**
5. 追问：线是直的吗？是弯的吗？会改变方向吗？**看图能看出什么**？

教材原文（短引用）：

> `Describe a scenario, for example, in which you launch a water rocket into the air.
> It goes up 150 ft, stops, and then falls back to the earth. Have the students assess the situation.
> Where would they put their zero? ... Have a student draw a picture of the scenario on the board.
> Then draw a position vs. time graph describing the motion.`

**顺序是关键**：先**画情境**，再**画图**。情境图是图像与物理之间的桥梁。

## 适用条件

| 维度 | 取值 |
|---|---|
| 水平档 | **BL / OL**（教材标记 `[BL][OL]`） |
| 先修 | 知道「位置」与「方向」；**不需要**会读斜率 |
| 认知负荷 | 中——负荷放在**从情境到图形的转换** |

## 禁忌

**对谁不适用？**

| 不适用对象 / 情形 | 依据 | 强度 |
|---|---|---|
| **哪些档位** | 该段落的标记是 `[BL][OL]` —— **教材明确把它标给了两档**，不是只给一档 | —— （这是标签的**跨度**，不是禁忌） |
| 本档（BL / OL）**以外**的学生 | 教材**为该段落标的就是这两档**；AL 档另给了不同建议 | **中** —— 标签明确划了范围，但「未标」仍不等于「不适用」——只是**未经检验** |

> [!WARNING]
> **本条没有强证据支撑的人群禁忌。**
>
> 教材只为本档给出建议，**没有说本做法对别的档位无效**。
> 把「教材没提」当成「不适用」是**过度推断**——这里如实标为**弱**，不编造。

## 风险

| 会翻车的地方 | 为什么 | 出处 |
|---|---|---|
| **学生以为零点的选择不影响图** | 教材在同一节的 `[OL]` 专门追问：`Ask if the place that they take as zero affects the graph.`——说明这是需要点破的地方 | 教材同节 `[OL]` |
| 跳过「画情境」直接画图 | 教材的顺序是**先情境后图形**。直接给坐标轴，学生失去可对应的实物 | — |

> [!NOTE]
> 教材把「零点是否影响图像」放在 `[OL]` 而不是 `[BL]`——**说明它认为这一步对 BL 档偏难**。
> 使用时应按水平裁掉或延后这一步。

## 证据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-023 | 教材（全文） | 低 | OpenStax《Physics》§2.3 Position vs. Time Graphs，[m54110](https://github.com/openstax/osbooks-physics/blob/main/modules/m54110/index.cnxml) | **CC BY 4.0** |

## 论证

### M1 · 教材为 BL/OL 档指定（存活）

- **主张**：情境叙事→画图是教材为低档与常档指定的做法
- **前提**：m54110 的 Teacher Support 用 `[BL][OL]` 标记（ev-023）
- **推理**：分档标记即教材对该水平的指定
- **证据**：ev-023
- **被攻击**：**指定 ≠ 实测有效**；水火箭情境对没有相关经验的学生可能不直观
- **署名**：@hpleapfrog · 2026-10-05

## 变更记录





| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-05 | 建立条目（采集候选转入） | Issue #8 | @hpleapfrog |
| 2026-10-05 | 拆分 `禁忌` / `风险`：原 `禁忌` 里装的是**风险**，已移入 `风险`；并补上真正的人群禁忌（含证据强度标注） | [Issue #13](https://github.com/hpleapfrog/Scholia/issues/13) | @hpleapfrog |
| 2026-10-05 | **修正 `禁忌` 措辞**：原写「未声明本做法可跨档」是错的——该段落的标记 `[BL][OL]`（或分段的 `[OL]`/`[AL]`）**恰恰声明了跨度** | [Issue #29](https://github.com/hpleapfrog/Scholia/issues/29) | @hpleapfrog |
