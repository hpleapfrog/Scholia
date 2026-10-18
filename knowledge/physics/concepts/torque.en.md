---
id: kb:physics:kp-torque
type: 知识点
title: "Torque"
status: 待审
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  适用: students who have done "force (HS)" and uniform circular motion and want to answer "how does a force change how fast something spins"
  条件: covers the definition of torque (magnitude and direction), the lever arm and net torque; no moment of inertia or static-equilibrium systems (not built)
edges:
  先修: ["[Force (HS)](force.en.md)", "[Angular acceleration and rotational kinematics](rotational-kinematics.en.md)"]
  支持: []
  攻击: []
evidence: [ev-088]
license: CC-BY-SA-4.0
---

> **English version of [`力矩.md`](力矩.md).**

> [!TIP]
> **After reading this entry you should** be able to compute the "turning effectiveness" of a force with `τ = r F sin θ`, and explain why you push a door far from its hinges

## Definition

**Torque** is the rotational version of force — it measures a force's **effectiveness in changing how fast something rotates**:

```
τ = r F sin θ
```

- `r`: the distance from the pivot point (hinge / fulcrum) to the point where the force is applied — this vector is the **lever arm**
- `F`: the magnitude of the force; `θ`: the angle between the force and the lever arm
- unit `N·m`; torque is a **vector**, with the same direction as the angular acceleration it produces
- the two ways to **maximise torque**: apply the force **perpendicular to the lever arm** (`sin 90° = 1`) and **as far from the pivot as possible**

When the net torque is zero there is no angular acceleration; a system spinning at constant angular velocity with zero net torque **keeps spinning that way** — Newton's first law in rotational form.

> [!IMPORTANT]
> **Opening a door is not just about how hard you push, but where and in which direction.**
>
> The textbook's example is a door: `a door opens slowly if you push too close to its hinge, but opens easily if you push far from the hinges`.
>
> The common intuition is "bigger force, faster rotation" — only half true: in `τ = r F sin θ` **all three factors** can drive it to zero.
> If the point of application sits on the pivot (`r = 0`) or the force runs along the lever arm (`θ = 0`), no amount of force will turn it.
> The textbook's suggested demonstration uses **levers of different lengths**, so students observe first and match the formula after (ev-088).

> [!NOTE]
> **Torque and Newton's second law: alike, with one recorded gap.**
>
> The textbook defines torque as `the angular version of force`, `the effectiveness of a force to change the rotational speed` (ev-088).
> The likeness to Newton's second law is structural: force ↔ torque, mass ↔ "rotational inertia".
> **But this textbook never introduces moment of inertia**, and no `α = τ / I` appears in the source — **a recorded gap** (see Relations).

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Force (HS)](force.en.md) — torque is "force × lever arm"; the concept of force appears directly in the definition |
| Prerequisite | [Angular acceleration and rotational kinematics](rotational-kinematics.en.md) — net torque determines `α`, and torque's direction is that of `α` |
| Structural analogy | [Newton's second law](newtons-second-law.en.md) — "force ↔ torque, mass ↔ rotational inertia"; **moment of inertia is not built** |
| Recorded gap | **moment of inertia and rotational dynamics (`τ = Iα`)** and **static equilibrium (the lever problem sets)** are not built |

## Argument

### K1 · Why the prerequisites point at "force" and "angular acceleration" (no attack yet)

- **Claim**: the cognitive prerequisites of torque are the concept of force and angular acceleration
- **Premise**: the textbook calls torque `the angular version of force`, the `effectiveness of a force to change the rotational speed` (ev-088) —
  "rotational version of force" requires "force" first; "changing how fast it rotates" requires a description of how fast it rotates (`ω`, `α`)
- **Reasoning**: `F` appears directly in the definition of `τ`; `α` appears directly in "zero net torque ⇒ zero `α`" — both are **dependencies at the level of definition**
- **Evidence**: ev-088
- **Attacked**: **the textbook never writes `Review force` or the like** — the basis is the defining sentence and the section's position in the chapter, weaker than a "Review …" style hook. Recorded as is.
- **Attribution**: @hpleapfrog · 2026-10-18

### K2 · "Perpendicular + farthest" is just sin and r at their maximum (no attack yet)

- **Claim**: the two operations that maximise τ — apply perpendicular, apply as far from the pivot as possible — need no new principle
- **Premise**: the textbook gives `τ = r F sin θ` and states `torque is maximized when the force is applied perpendicular to the lever arm because sin θ = 1 for θ = 90 degrees` (ev-088)
- **Reasoning**: `sin θ = 1` at `θ = 90°`; `r` is largest at the point of application farthest from the pivot — both are trivial consequences of the expression itself
- **Evidence**: ev-088
- **Attacked**: no attacks yet
- **Attribution**: @hpleapfrog · 2026-10-18

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-18 | Entry created; fourth node of the "circular motion" chapter, answering "how a force changes α" | written after reading m54180 in full (ev-088) | @hpleapfrog |
