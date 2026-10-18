---
id: kb:physics:kp-newtons-second-law
type: 知识点
title: "Newton's second law"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  范围: relation between motion and force

edges:
  先修: ["[知识点：惯性](inertia.en.md)"]
  支持: []
  攻击: []
evidence: [ev-040]
license: CC-BY-SA-4.0
---

> **English version of [`牛顿第二定律.md`](牛顿第二定律.md).**

> [!TIP]
> **After reading this entry you should** be able to solve for the net force, mass or acceleration with F_net = ma, and to distinguish "equals" from "is proportional to"

## Definition

**Newton's second law**: the magnitude of an object's acceleration is **directly proportional** to the **net force** on it, inversely proportional to its mass, and in the same direction as the net force.

```
F_net = m · a
```

- `F_net` is the **net force**, not any single force
- `m` is **mass** (the measure of inertia)
- the unit of force is defined by this: `1 N = 1 kg·m/s²`

> [!IMPORTANT]
> **Two confusions the textbook names (both at the `[AL]` tier, ev-040):**
>
> | # | Confusion | Key textbook wording |
> |---|---|---|
> | 1 | **"equal" vs "proportional"** | `Students might confuse the terms equal and proportional.` |
> | 2 | **weight (a force) vs `g` (an acceleration)** | `Students might confuse weight, which is a force, and g, which is the acceleration due to gravity.` |
>
> **Item 1 is not pedantry.** In `F = ma`, `F` and `a` really are equal **on the same object**;
> but "proportional" is about the relation **when you switch to another object, another mass**. Writing `a ∝ F` **requires declaring `m` constant first**.
>
> **Item 2 is related to but different from another misconception in this repo**:
> [confusing G with g](../misconceptions/g-vs-g.en.md) confuses the **constant `G`** with `g`;
> here the confusion is between **the force of weight** and `g` as an **acceleration**.
>
> **The follow-up question the textbook gives right after**: `Ask students if they think an astronaut weighs the same on`
> `the moon as they do on Earth. Talk about the difference between mass and weight.`

> [!NOTE]
> **Its relation to [inertia](inertia.en.md), stated very directly by the textbook:**
>
> > `Review the concepts of inertia and Newton's first law. Explain that, according to`
> > `Newton's first law, a change in motion is caused by an external force.`
>
> **The first law says "no external force, no change in motion"; the second law says "how much it changes when there is".**
> Hence the `先修` edge is **inertia → Newton's second law**, and when teaching the second law **one must go back and review the first law first**.

## Relations

| Object | Entry | Note |
|---|---|---|
| prerequisite · knowledge point | [inertia](inertia.en.md) | the first law is a **prerequisite** of the second (the textbook requires reviewing it first) |
| teaching method · OL | [Newton's second law · OL: return to inertia and external forces](../methods/newton2-ol-first-law.en.md) | start from "what changed the motion" |
| teaching method · AL | [Newton's second law · AL: solving for three variables separately](../methods/newton2-al-three-vars.en.md) | solve for `F`, `m`, `a` separately |
| misconception | weight vs `g` confusion (**not yet built**) | the textbook names it, but the repo has no corresponding entry |

## Argument

### K19 · Why listed separately (no attack yet)

- **Claim**: Newton's second law deserves to be a separate knowledge point
- **Premise**: the textbook gives it a section with **5 teaching hints** (4 of them tiered) and 14 terms (ev-040)
- **Reasoning**:
  1. it is **the only quantitative relation in mechanics** — the first law only says "what would happen", it says "how much"
  2. it also **defines the unit of force** (`1 N = 1 kg·m/s²`), which is an independent layer
  3. the textbook names **two concrete confusions** here ("equal / proportional", weight vs `g`),
     and both at the `[AL]` tier — showing it expects **advanced students to be more prone to the confusion**
- **Evidence**: ev-040
- **Attacked**: **its teaching hints number only 5, one of the fewest among the repo's built nodes**;
  and it connects directly to [inertia](inertia.en.md) in the same chapter — **splitting it may sever the main chain "first law → second law"**
- **Response**: do not merge. **The textbook itself asks, in the second law's hint, to "review the first law"** —
  that is evidence for **two nodes with an order**, not one node. **But the low hint count really is this entry's weakness**:
  the textbook puts the content in worked examples, and **examples are not teaching hints**; the repo does not treat examples as a `教法` source (that would require a different collection pass).
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**:
  - **force (high school)** — the repo only has **junior-high** "forces and motion", **no high-school "force" node**,
    yet `F_net` needs it. **This is a real gap in the repo's `先修` graph**
  - **Newton's third law** (the textbook has a section; the repo has not built it)
  - **weight vs `g` confusion** (textbook names it; no entry yet)

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 5: "complete through Chinese high school") | user request · Issue #8 | @hpleapfrog |
