---
id: kb:physics:method-momentum-al-two-forms
type: 教法
title: "Momentum and impulse · advanced: two ways of writing Newton's second law"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: students who can already use F = ma and are about to study the chapter on momentum
  条件: have already studied Newton's three laws
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/textbook-tiered-guidance.en.md#a3)"]
  攻击: []
knowledge_point: ["[Momentum and impulse](../知识点/momentum-impulse.en.md)"]
evidence: [ev-045]
license: CC-BY-SA-4.0
---

> **English version of [`动量和冲量-AL-两种写法.md`](动量和冲量-AL-两种写法.md).**

## Method

### 1 · Put the old form on the table first

> `Review the equation of Newton's second law of motion.`
> `Point out the two different equations for the law.`

**The textbook's `[OL]` hint does one thing only**: it tells students **this law has two ways of writing**.
It does not explain; it lays the fact out first.

### 2 · Write out both forms, and show how one is derived from the other

> `Show the two different forms of Newton's second law and how one can be derived from the other.`

| Way of writing | Form | What is known |
|---|---|---|
| the familiar form | `F = m·a` | the relation between force and **acceleration** |
| the new form | `F = Δp / Δt` | the relation between force and the **rate of change of momentum** |

**The derivation takes only two steps** (the `[AL]` hint asks for it to be worked out):

```
F = m·a            (the old form)
a = Δv / Δt        (the definition of acceleration, from this repo's existing "acceleration" node)
⇒ F = m·Δv/Δt
    = Δ(mv)/Δt     (with mass constant, move m inside the Δ)
    = Δp / Δt      (the definition p = mv)
```

**Note that the last step uses "mass constant"** — so the equivalence of the two forms **has a precondition**.
(In the variable-mass case, such as a rocket, you must use the `F = Δp/Δt` side.)

### 3 · Force "direction" out with an everyday collision

> `Start a discussion about movement and collision. Using the example of football players,`
> `point out that both the mass and the velocity of an object are important considerations in`
> `determining the impact of collisions. The direction as well as the magnitude of velocity`
> `is very important.`

**The textbook's two colliding players carry three things in a single sentence**:

| Point | The textbook's exact words |
|---|---|
| mass counts | `both the mass and the velocity` |
| velocity counts | the same line |
| **direction counts too** | `The direction as well as the magnitude of velocity is very important` |

### 4 · A comparison of magnitude

> `Explain that a large, fast-moving object has greater momentum than a smaller, slower object.`
> `This quality is called momentum.`

**The textbook names "momentum" only here** — after the comparison has been done.

## Conditions of use

| Dimension | Value |
|---|---|
| Level tier | **AL** (both hints of this entry are tagged `[AL]`; `[OL]` only asks to "point out that there are two forms") |
| Prerequisites | Newton's second law (`F = ma`); the **definition of acceleration** (needed by the derivation) |
| Cognitive load | medium — **the algebra is only two steps, but students must accept "one law has two ways of writing"** |

## Contraindications

| Who or situation it does not apply to | Basis | Strength |
|---|---|---|
| students who **are not yet fluent with `F = ma`** | this method is built on "the old form is already familiar"; the first sentence of the textbook's `[OL]` hint is `Review the equation` | **strong** (the textbook lists it first) |
| students who do not know `a = Δv/Δt` | the second step of the derivation uses it directly — that is the content of this repo's [acceleration](../知识点/acceleration.en.md) | **strong** — follows from the nature of the derivation |
| students **outside** this tier (AL) | the textbook tags exactly that passage `[AL]`; the `[OL]` tier only asks to "point out that there are two forms" and **does not require the derivation** | **medium** — the tag clearly draws the scope, but "not tagged" still ≠ "does not apply", it is merely **untested** |

## Risks

| Where it can go wrong | Why |
|---|---|
| presenting `F = Δp/Δt` as the more advanced way of writing | **they are the same law**. The textbook's wording is `Show … how one can be derived from the other` — **they can be derived from each other**, not a replacement of old by new |
| **skipping the "mass is constant" step** in the derivation | that step is the only precondition. Skip it and students will not be able to derive anything when they later meet rockets, jets and other **variable-mass** problems |
| telling the football-player example only as "it hurts" | the textbook wants **three factors** (mass, magnitude of velocity, direction of velocity). Talking only about "pain" drops the direction |
| demanding the derivation at the `[OL]` tier | the textbook **keeps `[OL]` and the derivation separate**: `[OL]` only says "point out that there are two forms" |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-045 | textbook (full text) | low | OpenStax《Physics》Chapter 8 · Linear Momentum, Force, and Impulse, [m54215](https://github.com/openstax/osbooks-physics/blob/main/modules/m54215/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · Designated by the textbook for the AL tier (no attack yet)

- **Claim**: this is the method the textbook specifies for advanced students
- **Premise**: the Teacher Support of m54215 tags "two forms + deriving from each other" as `[AL]` (ev-045)
- **Reasoning**: a tier tag is the textbook's designation for that passage
- **Evidence**: ev-045
- **Attacked**: **"the textbook specifies it" ≠ "measured to be effective"**; moreover **the `[OL]` hint about "two forms" and the `[AL]` hint about the derivation are two separate sentences in the textbook**, while this entry organizes them into one four-step method — **that layer of organization was added by this repo**
- **Attribution**: @hpleapfrog · 2026-10-05

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 7) | Issue #8 | @hpleapfrog |
