---
id: kb:physics:method-newton2-al-three-vars
type: 教法
title: "Newton's second law · advanced: solving for the three variables separately, and two confusions"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: students who can already substitute into F = ma but cannot read it as a relational statement
  条件: has studied unit conversion; knows the concept of gravity
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/textbook-tiered-guidance.en.md#a3)"]
  攻击: []
knowledge_point: ["[Newton's second law](../知识点/newtons-second-law.en.md)"]
evidence: [ev-040]
license: CC-BY-SA-4.0
---

> **English version of [`牛顿第二定律-AL-三个变量与单位.md`](牛顿第二定律-AL-三个变量与单位.md).**

## Method

### 1 · Solve the equation for each of the three variables in turn

> `Write the equation for Newton's second law and show how it can be solved for all three`
> `variables, F, m, and a. Explain the practical implications for each case.`
> `Ask students how the other two variables would behave if one quantity is held constant.`

**The key is the last sentence**: "how would the other two variables behave if one quantity is held constant" —
**this step turns an equation into a relation**.

### 2 · Point out the difference between "equal" and "proportional"

> `Students might confuse the terms equal and proportional.`

**This is not merely a matter of wording**:

| Statement | Does it hold? |
|---|---|
| `F` **equals** `ma` | ✅ always holds **for the same object** (this is a defining equation) |
| `a` **is proportional to** `F` | ⚠️ **holds only when `m` is unchanged** |
| `a` **is inversely proportional to** `m` | ⚠️ **holds only when `F` is unchanged** |

**Writing "`F = ma`, therefore `a` is proportional to `F`" without stating that `m` is unchanged is wrong.**

### 3 · Use the astronaut question to draw out "weight is a force"

> `Ask students if they think an astronaut weighs the same on the moon as they do on Earth.`
> `Talk about the difference between mass and weight.`

**The textbook ties this question to the confusion named in another hint**:

> `Students might confuse weight, which is a force, and g, which is the acceleration due to gravity.`

| | What it is | On the Moon |
|---|---|---|
| **mass** `m` | the measure of inertia | **unchanged** |
| **weight** `mg` | **a force** | **smaller** (`g` is smaller) |
| `g` | **acceleration due to gravity** | **smaller** |

**The astronaut's "body weight" changed, the mass did not** — and the `m` in `F = ma` is **mass**.

### 4 · Review unit conversion first

> `Review how to convert between units.`

(This is exactly what the `[BL]` tier gets — **the AL-tier method also rests on it**.)

## Conditions of use

| Dimension | Value |
|---|---|
| Level tier | **AL** (textbook tag `[AL]`) |
| Prerequisites | unit conversion; the distinction between mass and weight (**this is precisely what this entry covers** — the textbook treats it as AL content) |
| Cognitive load | medium — the difficulty lies in **reading an equation as a relation** |

## Contraindications

| Who or situation it does not apply to | Basis | Strength |
|---|---|---|
| students **not yet fluent in unit conversion** | the textbook places this in the `[BL]` tier, showing **it is not a prerequisite of AL but something earlier** | **strong** (the textbook tiered it) |
| students who have not yet established the **vector** meaning of the concept of "force" | the direction of the net force determines the direction of the acceleration, and this `[AL]` hint **does not handle vectors** | **medium** |
| students **outside** this tier (AL) | the textbook tags exactly that passage `[AL]`; the OL tier gets different suggestions | **medium** — the tag clearly draws the scope, but "not tagged" still ≠ "does not apply", it is merely **untested** |

## Risks

| Where it can go wrong | Why |
|---|---|
| "`a` is proportional to `F`" stated without the condition | **this is exactly the confusion the textbook names**. `a ∝ F` must hang on "`m` unchanged" |
| weight and mass explained only once | the textbook **appears twice within the same section at the AL tier** (the confusion hint plus the astronaut follow-up), showing it expects students to confuse them |
| solving for the three variables turning into three separate formulas | the textbook's landing point is `Ask students how the other two variables would behave if one quantity is held constant` — **the relation among the variables**, not three isolated equations |
| also muddling `g` together with `G` | this entry handles **weight (a force) and `g` (an acceleration)**; `G` (the gravitational constant) is another matter (see [confusing G with g](../误解/g-vs-g.en.md)). **Teaching both together easily gets blended into one pot by students** |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-040 | textbook (full text) | low | OpenStax《Physics》Chapter 4 · Newton's Second Law of Motion, [m54142](https://github.com/openstax/osbooks-physics/blob/main/modules/m54142/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · Designated by the textbook for the AL tier (no attack yet)

- **Claim**: this is the method the textbook specifies for advanced students
- **Premise**: the Teacher Support of m54142 tags the above content with `[AL]` (ev-040)
- **Reasoning**: a tier tag is the textbook's designation for that passage
- **Evidence**: ev-040
- **Attacked**: **"the textbook specifies it" ≠ "measured to be effective"**;
  and the textbook's AL hints **are only three paragraphs**, while this entry's `Method` section organizes content scattered across hints and adjacent modules —
  **this layer of organization is this repo's addition, not the textbook's** — readers must be made to see this
- **Attribution**: @hpleapfrog · 2026-10-05

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 5) | Issue #8 | @hpleapfrog |
