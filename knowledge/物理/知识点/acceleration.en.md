---
id: kb:physics:kp-acceleration
type: 知识点
title: Acceleration
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  范围: description of motion

edges:
  先修: ["[知识点：速度与速率](speed-and-velocity.en.md)"]
  支持: []
  攻击: []
evidence: [ev-039]
license: CC-BY-SA-4.0
---

> **English version of [`加速度.md`](加速度.md).**

> [!TIP]
> **After reading this entry you should** be able to compute acceleration with a = Δv/Δt, and explain how signs relate to direction

## Definition

**Acceleration** is the **rate of change of velocity**:

```
a = Δv / Δt = (v_f − v_0) / (t_f − t_0)
```

- `Δ` (capital Greek delta) **always means "final minus initial"** — the textbook points this out specifically (ev-039)
- Unit `m/s²`. **The "seconds squared" in the denominator means "per second, per second"**, not an area
- **It is a vector**: magnitude and direction

> [!IMPORTANT]
> **The word "deceleration" is not used in physics.**
>
> The textbook says this once in each of two different hints (ev-039):
>
> > `Explain that deceleration is not used in physics because acceleration is either`
> > `positive or negative.`
>
> **Acceleration has only positive and negative; there is no category called "deceleration."** Because what decides the sign is **the coordinate direction chosen** —
> for the same motion, picking the opposite direction as positive yields the opposite sign.

> [!WARNING]
> **Three places the textbook names where students get stuck:**
>
> | # | Where | Key textbook wording |
> |---|---|---|
> | 1 | **the acceleration arrow points opposite the velocity arrow** | "students may be confused. Explain: because **the speed is decreasing**, i.e. **the velocity arrow is getting shorter**" |
> | 2 | **distinguishing constant from variable acceleration** | `Distinguish between constant and variable acceleration. There could be confusion here, especially in the case of increasing acceleration.` |
> | 3 | **meaning of signs and units** | before computing, confirm students "understand what a quantity with a plus or minus sign means, and the unit of each quantity" |
>
> **Item 1 is the most counterintuitive part of this section**: the object is **moving forward**, while **the acceleration points backward**.
> The textbook gives no formula-based explanation; what it gives is a **visualization you can say out loud** —
> "the velocity arrow is getting shorter".

## Relations

| Object | Entry | Note |
|---|---|---|
| prerequisite · knowledge point | [speed and velocity](speed-and-velocity.en.md) | acceleration is the **rate of change of** velocity; without velocity there is no change to speak of |
| teaching method · OL | [acceleration · OL: signs and the word "deceleration"](../教法/acceleration-ol-sign.en.md) | the textbook handles one word in two hints |
| teaching method · AL | [acceleration · AL: using acceleration to analyze "growth rate is declining"](../教法/acceleration-al-rate.en.md) | applying "rate of change of a rate of change" to language |

> [!NOTE]
> **This node's relation to [position-time graph](position-time-graph.en.md).**
>
> `position-time graph` covers the graph of **position vs time**, while acceleration needs the graph of **velocity vs time**
> (the textbook has a separate section for that, which this repo has not built).
>
> So this entry's `先修` **only links to [speed and velocity](speed-and-velocity.en.md)** —
> adding an edge to `position-time graph` would make people think "position-time graphs must be learned first",
> whereas in the textbook that section and this one are **parallel directions of travel**, not predecessors.

## Argument

### K18 · Why listed separately (no attack yet)

- **Claim**: acceleration deserves to be a separate knowledge point
- **Premise**: the textbook gives it a section with **10 teaching hints** (6 of them tiered) and 10 terms (ev-039)
- **Reasoning**:
  1. it has an **independent defining equation** and an **independent unit**, and that unit's meaning is itself a teaching point
     (what does "squared seconds" mean)
  2. the textbook **repeats the same wording issue in two hints within the same section** (the word "deceleration" is not used),
     showing this is a **recurring sticking point**, not a one-off reminder
  3. it is the **entry point to much of the rest of the volume**: uniformly accelerated motion, Newton's second law,
     circular motion (centripetal acceleration) all presuppose it
- **Evidence**: ev-039
- **Attacked**: it connects directly to [speed and velocity](speed-and-velocity.en.md),
  **separating them may lead students to treat "describing motion" as two unrelated quantities**
- **Response**: do not merge. **The reason is their "objects" differ**: velocity describes a **state**,
  acceleration describes the **rate of change of that state**. Merging would rob the phrase "uniform acceleration" of its anchor
  (the "uniform" modifies acceleration, not velocity).
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**:
  - **uniformly accelerated linear motion** (not yet built) — it is this node's most direct downstream
  - **velocity-time graph** (not yet built; the textbook has a separate section)

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 5: "complete through Chinese high school") | user request · Issue #8 | @hpleapfrog |
