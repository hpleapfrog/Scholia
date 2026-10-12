---
id: kb:physics:method-newton3-al-rubber-band
type: 教法
title: "Newton's third law · advanced: two rubber bands, and inside vs. outside the system"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: students who can already use F = ma but treat "system" as an abstract word
  条件: have already studied Newton's first and second laws
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[Newton's third law](../知识点/牛顿第三定律.md)"]
evidence: [ev-042]
license: CC-BY-SA-4.0
---

> **English version of [`牛顿第三定律-AL-橡皮筋与系统内外力.md`](牛顿第三定律-AL-橡皮筋与系统内外力.md).**

## Method

### 1 · Talk about action and reaction through examples first, then introduce "system"

> `Start a discussion about action and reaction by giving examples.`
> `Introduce the concepts of systems and systems of interest.`
> `Explain how forces can be classified as internal or external to the system of interest.`
> `Give examples of systems. Ask students which forces are internal and which are external`
> `in each scenario.`

**Note the order**: **action and reaction first, system second** —
the concept of a system is a tool for **classifying forces**, not an a priori framework.

**The "system" is chosen by the student** (`system of interest`),
so the same force **is external in one system and may be internal in another**.

### 2 · Two rubber bands: one hangs something, one hangs nothing

> `Demonstrate the concept of tension by using physical objects.`
> `Suspend an object such as an eraser from a peg by using a rubber band.`
> `Hang another rubber band beside the first but with no object attached.`
> `Ask students what the difference is between the two.`

**The control condition is the key to this demonstration**: **two rubber bands that look alike, yet only one is stretched.**
Students have to explain **why** — and the answer lies in "is something pulling it or not".

### 3 · Ask out loud how the connector transmits force

> `What are the forces acting on the first peg?`
> `Explain how the rubber band (i.e., the connector) transmits force.`

The textbook points out directly that **the rubber band is the "connector"** —
its role is to **transmit** force, not to produce it.

### 4 · Then separate external from internal forces

> `Now ask students what the direction of the external forces acting on the connector is.`
> `Also, ask what internal forces are acting on the connector.`

**The same rubber band: ask the direction of the external forces first, then the internal forces** —
students must **draw the system boundary first** before they can answer.

### 5 · The final step: remove the rubber band and ask which way it moves

> `If you remove the eraser, in which direction will the rubber band move?`
> `This is the direction of the force the rubber band applied to the eraser.`

**This is where the whole demonstration closes, and the most elegant step.**

The direction the rubber band **springs back** is the direction of the force it **was just applying to the eraser** —
**the reaction force has been "seen"**.

## Conditions of use

| Dimension | Value |
|---|---|
| Level tier | **AL** (this demonstration is tagged **`[BL][OL][AL]`** in the textbook — shared by all three tiers; this entry organizes it at AL depth) |
| Prerequisites | Newton's first and second laws |
| Equipment | **two rubber bands + one eraser (or a similar small object) + one hook point** — low cost |
| Cognitive load | high — **it must hold four layers at once: "system", internal/external forces, "connector", reaction force** |

## Contraindications

| Who or situation it does not apply to | Basis | Strength |
|---|---|---|
| **which tiers** | this demonstration is tagged **`[BL][OL][AL]`** — **the textbook explicitly tags it for three tiers**, not for just one | — (this is the **spread** of the tag, not a contraindication) |
| students who **have not yet studied the first and second laws** | the first sentence of the textbook's `[OL]` hint is to review them; the AL builds on the same foundation | **medium** |
| having no rubber band that can be hung | the **control experiment** of this method (one hangs something, one hangs nothing) is where all its force comes from | **medium** — follows from the method itself |
| a class that does no demonstration at all and only talks | every step of this entry asks "**what is the difference between the two**" and "**which way does it move**" — **without physical objects there is no observable answer** | **strong** — follows from the nature of the method |

## Risks

| Where it can go wrong | Why |
|---|---|
| hanging only one rubber band | **the control group is the method itself**. The textbook specifically requires `Hang another rubber band beside the first but with no object attached` |
| skipping step 5 | that is the only step that turns the "reaction force" into **something you can see**. **Without it, the whole demonstration is just about tension** |
| telling "system" as something fixed and unchanging | the textbook uses `systems of interest` — **the system is chosen by the student**. Telling it as fixed loses the layer that "the same force can be internal or external" |
| treating the rubber band as something that "produces force" | the textbook states that it is **`the connector`** — it **transmits** force. Students easily slide past this distinction |
| substituting a spring scale for the rubber band | you can, but **a spring scale pulls attention onto the reading**; the textbook chose the rubber band because **it springs back on its own**, which is exactly what step 5 needs |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-042 | textbook (full text) | low | OpenStax《Physics》Chapter 4 · Newton's Third Law of Motion, [m54131](https://github.com/openstax/osbooks-physics/blob/main/modules/m54131/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · A demonstration the textbook tags as shared by all three tiers (no attack yet)

- **Claim (narrowed)**: this rubber-band demonstration is tagged **`[BL][OL][AL]`** in the textbook,
  i.e. **the textbook gives it to all three tiers**; this entry organizes it at AL depth
- **Premise**: in the Teacher Support of m54131, the demonstration carries the consecutive tag `[BL][OL][AL]` (ev-042)
- **Reasoning**: **multiple tags** mean the textbook considers it **not tier-differentiating**
- **Evidence**: ev-042
- **Attacked**: **"the textbook gives it to all three tiers" ≠ "using it at all three tiers is effective"**;
  the textbook only marked the scope of applicability and **supplied no measured data at all**.
  The "Method" section of this entry breaks the demonstration into five steps and spells out what each step does —
  **that layer of decomposition was added by this repo**; the textbook itself is **one continuous passage**
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**: **should multi-tagged demonstrations become a category of their own?** This entry is the first teaching method shared by all three tiers;
  this repo's `水平档` field says "进阶（AL）", **which is not equivalent to "shared by three tiers"** —
  this is a **new schema question**, recorded in `## Relations` and in the PR description

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 6); **this repo's first teaching method shared by all three tiers** | Issue #8 | @hpleapfrog |
