---
id: kb:physics:kp-position-time-graph
type: 知识点
title: "Position-time graph"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  范围: kinematics

edges:
  先修: ["[速度与速率](speed-and-velocity.en.md)"]
  支持: []
  攻击: []
evidence: [ev-023]
license: CC-BY-SA-4.0
---

> **English version of [`位置-时间图.md`](位置-时间图.md).**

> [!TIP]
> **After reading this entry you should** be able to draw a position-time graph of a simple motion, and read displacement, distance and velocity off it

## Definition

A **position-time graph** plots the continuous change of position over time as a polyline or curve.

- the horizontal axis usually carries **time** (the independent variable), the vertical axis **position** (the dependent variable) — in physics time is usually the independent variable
- the straight line `y = m x + b` becomes `d = d₀ + v t` for position and time: **the intercept `b` becomes the initial position `d₀`**, **the slope `m` becomes the velocity `v`**
- so: where the graph meets the position axis is **where the motion started**; **the slope is the velocity**

Key to reading it:

- **slope = velocity** (steeper → faster), **slope sign = direction of motion**
- constant slope → uniform motion, and the slope is the **average velocity** `v = Δd / Δt`; for a piecewise-straight graph take the slope of each segment, and weight by the time of each for the whole trip
- a curve → varying speed: the **instantaneous velocity** at a moment equals the slope of the **tangent** at that point (a line that touches the curve at exactly one point)
- the **net displacement** on the graph is the difference between first and last vertical coordinates; **total distance** requires adding every reversal

> [!NOTE]
> **The textbook's jet-car example — two readings, a straight segment and a curve** (ev-023)
>
> - straight segment: pick two points on the line, `(0.50 s, 525 m)` and `(6.4 s, 2000 m)`,
>   giving `v = (2000 − 525) ÷ (6.4 − 0.50) = 250 m/s` (about 900 km/h, far above a highway limit)
> - curved segment: draw the tangent at `t = 25 s` and take its slope: instantaneous velocity `140 m/s`
> - what the tangent buys you: seeing whether the velocity is **increasing, decreasing, positive, negative, or zero**
>
> A there-and-back motion gives a V shape: positive slope out, negative slope back.
> For "leave home and return the same way", **net displacement is 0 but total distance is not**
> (the textbook's hockey-puck problem: net displacement 0, total distance 40 m, average velocity 0).

> [!IMPORTANT]
> **A curve getting steeper is acceleration announcing itself.**
> The textbook's note for advanced students: the slope of the curve itself changes — "a slope of the slope" —
> which is next chapter's acceleration (ev-023).

## Relations

| Object | Entry | Note |
|---|---|---|
| teaching method · BL/OL | [position-time graph · situational narrative](../methods/ptgraph-bl-ol-narrative.en.md) | draw the situation first, then the graph |
| teaching method · AL | [position-time graph · boundary-case probing](../methods/ptgraph-al-boundary-cases.en.md) | force the idealization with boundary cases |

## Prerequisite note

**Prerequisite: [speed and velocity](speed-and-velocity.en.md)**

The **core act** of reading the graph is **reading the slope**, and the slope is velocity.
Without first establishing the quantity "velocity = displacement / time", the line on the graph is only a shape, with no physical meaning to read off.

## Argument

### K3 · Grounds for the prerequisite relation (no attack yet)

- **Claim**: speed and velocity are prerequisites of the position-time graph
- **Premise**: the core act of reading the graph (reading the slope) uses the concept of velocity; the textbook's §2.2 speed and velocity precedes §2.3 position-time graph
- **Reasoning**: in §2.3 the textbook directly equates "slope" with "velocity", showing the latter is treated as already known
- **Evidence**: ev-022 (§2.2), ev-023 (§2.3)
- **Attacked**:
  - the same issue exists: **section order ≠ cognitive prerequisite**
  - this entry's grounds are slightly stronger than K2: in the §2.3 text the textbook **explicitly uses** the velocity concept, rather than merely placing it later
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**: learning data

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (plan A: add the knowledge-point layer) | Issue #11 | @hpleapfrog |
| 2026-10-18 | learner half expanded: `d = d₀ + vt` and the axis conventions, instantaneous velocity via the tangent, the jet car's two readings, the V-shaped there-and-back graph | weak-entry expansion · m54110 re-read (ev-023) | @hpleapfrog |
