---
id: kb:physics:kp-rotational-kinematics
type: 知识点
title: "Angular acceleration and rotational kinematics"
status: 待审
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  适用: students who understand angular velocity in uniform circular motion and are starting on rotation whose rate changes
  条件: covers angular acceleration and the rotational kinematic equations (constant α); no torque or rotational dynamics (separate entries)
edges:
  先修: ["[Acceleration](acceleration.en.md)", "[Uniform circular motion](uniform-circular-motion.en.md)"]
  支持: []
  攻击: []
evidence: [ev-088]
license: CC-BY-SA-4.0
---

> **English version of [`角加速度与转动运动学.md`](角加速度与转动运动学.md).**

> [!TIP]
> **After reading this entry you should** be able to translate the linear kinematic equations "word for word" into their rotational versions, and compute the angular acceleration of a spinning wheel and the time it takes to stop

## Definition

**Angular acceleration** is the rate of change of angular velocity — the rotational version of `a = Δv / Δt`:

```
α = Δω / Δt
```

- unit `(rad/s)/s`, i.e. `rad/s²`
- **sign convention**: **counterclockwise positive**, clockwise negative; the sign of `α` describes a direction relation and **does not directly mean "speeding up / slowing down"** (see below)
- the **tangential acceleration** of a point on the circle is proportional to it: `a = r α`
  - **tangential acceleration** is parallel to the tangential velocity (same or opposite direction); **centripetal acceleration** is perpendicular to it
- examples where angular velocity is not constant: a skater pulling in her arms, a child pushing a merry-go-round, a CD slowing to a halt when switched off

The three rotational variables `θ`, `ω`, `α` are the rotational versions of `x`, `v`, `a`:

| Rotational | Linear | Relation |
|---|---|---|
| `θ` rotation angle | `x` position | `θ = x / r` |
| `ω` angular velocity | `v` velocity | `ω = v / r` |
| `α` angular acceleration | `a` acceleration | `α = a / r` |

**Rotational kinematics** describes the relationships between `θ`, `ω`, `α` and time — it **only describes motion**; no forces or masses appear (those belong to dynamics).
For constant `α`, the linear kinematic equations carry over one for one:

| Rotational | Linear |
|---|---|
| `ω = ω₀ + α t` | `v = v₀ + a t` |
| `θ = ω̄ t`, average `ω̄ = (ω₀ + ω) / 2` | `x = v̄ t` |
| `θ = ω₀ t + ½ α t²` | `x = v₀ t + ½ a t²` |
| `ω² = ω₀² + 2 α θ` | `v² = v₀² + 2 a x` |

> [!IMPORTANT]
> **"Deceleration" and "accelerating in the negative direction" are two different things.**
>
> The textbook warns teachers: `Students may get confused between deceleration and increasing acceleration in the negative direction.`
>
> The key is the sign convention: counterclockwise is positive. A counterclockwise object **slowing down** has negative `α`;
> a **clockwise** object **speeding up** also has negative `α` — **one sign, two entirely different motions**.
> The sign of `α` is not "speeding up / slowing down" but "relation to the positive direction"; to tell which, check whether `α` and `ω` have the same sign.

> [!NOTE]
> **Why are tornado winds fastest at the bottom of the funnel?**
>
> The textbook closes with tornadoes: `They blow houses away … particularly at the bottom where the funnel is narrowest
> because the rate of rotation increases as the radius decreases.` (ev-088)
>
> "Smaller radius, faster rotation" — rotational kinematics **only describes** rotation, it does not explain this;
> the explanation needs **conservation of angular momentum**, which this repo has not built (see Relations).

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Acceleration](acceleration.en.md) — angular acceleration is its word-for-word rotational version; the meaning of "rate of change" carries over unchanged |
| Prerequisite | [Uniform circular motion](uniform-circular-motion.en.md) — `Δθ` and `ω` are defined there; this entry handles "`ω` no longer constant" |
| Structural analogy | the table of linear kinematic equations (`v = v₀ + at`, etc.) — all four equations correspond one for one; the textbook calls them `identical to the linear version` |
| Follow-up | [Torque](torque.en.md) — what changes `α` is torque, the rotational version of force |
| Recorded gap | **conservation of angular momentum** (the tornado explanation) and **the vector direction of angular velocity (right-hand rule)** are not built |

## Argument

### K1 · "The whole equation table corresponds word for word" is the textbook's own statement (no attack yet)

- **Claim**: the rotational kinematic equations are not new content but a word-for-word substitution into the linear table (`x→θ`, `v→ω`, `a→α`)
- **Premise**: the textbook writes `Notice that the equation is identical to the linear version, except with angular analogs of the linear variables. In fact, all of the linear kinematics equations have rotational analogs` (ev-088), and supplies a "rotational ↔ linear" table
- **Reasoning**: precisely because it is a word-for-word substitution, the bottleneck is not the new equations but whether the **old** ones are solid — hence the prerequisites point back to linear kinematics via acceleration
- **Evidence**: ev-088
- **Attacked**: **"the bottleneck is the old equations" is this repo's inference** — the textbook gives the correspondence but says nothing about transfer difficulty. Recorded as is, not presented as a quotation.
- **Attribution**: @hpleapfrog · 2026-10-18

### K2 · The sign convention is "counterclockwise positive" (no attack yet)

- **Claim**: the sign of `α` describes only a direction relation; the test is whether it has the same sign as `ω`
- **Premise**: the textbook states `by convention, counterclockwise is the positive direction and clockwise is the negative direction`, and warns teachers about the "deceleration vs negative acceleration" confusion (ev-088)
- **Reasoning**: same sign as `ω` means `|ω|` grows, opposite sign means it shrinks — an algebraic restatement of the textbook's verbal rule ("ω increases, so α is positive"), convenient for calculation
- **Evidence**: ev-088
- **Attacked**: **the "same sign as ω" formulation is this repo's tidying, not the textbook's words** — the textbook uses prose. Equivalent, but recorded here so it is not mistaken for a quotation.
- **Attribution**: @hpleapfrog · 2026-10-18

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-18 | Entry created; third node of the "circular motion" chapter, extending "uniform" to rotation whose rate changes | written after reading m54180 in full (ev-088) | @hpleapfrog |
