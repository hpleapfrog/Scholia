---
id: kb:physics:kp-uniform-circular-motion
type: 知识点
title: "Uniform circular motion"
status: 待审
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  适用: students who know acceleration and are starting on why the direction of velocity keeps changing
  条件: covers only the **description** of circular motion and its link to centripetal acceleration/force; not angular acceleration or torque (separate entries)
edges:
  先修: ["[acceleration](acceleration.en.md)"]
  支持: []
  攻击: []
evidence: [ev-080, ev-081]
license: CC-BY-SA-4.0
---

> **English version of [`匀速圆周运动.md`](匀速圆周运动.md).**

> [!TIP]
> **After reading this entry you should** be able to say what stays constant in "uniform" circular motion, and compute speed and acceleration with v = rω and a = v²/r

## Definition

**Uniform circular motion** is motion along a circular path **at constant speed**:

> `the motion of an object in a circular path at constant speed`

"Uniform" here is about **speed**, not **velocity**. Velocity is a vector whose direction is
**tangent to the circle**, so it changes every instant — the object is therefore **always
accelerating**, even though the magnitude of its velocity never changes.

| Quantity | Relation | Note |
|---|---|---|
| Angle of rotation | `Δθ = Δs / r` | arc length over radius; radians |
| Angular velocity | `ω = Δθ / Δt` | radians per second |
| Tangential speed | `v = r ω` | same ω; larger r means larger v |
| Period | `T = 2π / ω` | time for one revolution |
| Units | `1 revolution = 2π rad = 360°` | `1 rad ≈ 57.3°` |

The acceleration points at the centre and is called **centripetal acceleration**:

```
a_c = v² / r = r ω²
```

The corresponding component of the net force is the **centripetal force** `F_c = m a_c = m v² / r`.

> [!IMPORTANT]
> **The word "uniform" is the trap.**
>
> Students read "uniform" as "nothing changes", and conclude that acceleration is zero.
> The textbook's teacher note asks the question outright:
>
> > `[AL] Ask students whether or not velocity changes in uniform circular motion. What about speed? What about acceleration?`
>
> The three answers are: **yes**, **no**, and **not zero** (it points at the centre).
> Skip that question and every centripetal-force calculation afterwards stands on "a = 0".

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [acceleration](acceleration.en.md) — "velocity changes" includes a change of **direction** |
| Method | [uniform circular motion · cut the string](../methods/ucm-cut-string.en.md) |
| Misconception | [centrifugal force is a real force](../misconceptions/centrifugal-force-is-real.en.md) |
| Gap | **the vector direction of ω (right-hand rule) is not developed here**; rotational kinematics (angular acceleration, torque) is a separate entry |

## Argument

### K1 · "Speed constant, velocity changing" is the textbook's own wording, not our inference (no attack yet)

- **Claim**: in uniform circular motion "uniform" means constant speed; velocity keeps changing
  because its direction changes, hence there is an acceleration pointing at the centre
- **Premise**: the textbook defines the motion as `at constant speed` (ev-080) and defines
  centripetal acceleration as the component perpendicular to velocity, pointing at the centre (ev-081)
- **Reasoning**: velocity is a vector; a change of direction is a change of velocity; a change of
  velocity is an acceleration — all three steps are definitional
- **Evidence**: ev-080 · ev-081
- **Attacked**: **the textbook never states "uniform circular motion has acceleration" as a
  sentence** — it gives three guiding questions (`What about acceleration?`). Strictly, the
  conclusion follows from the *definition* of acceleration, not from a quoted assertion.
  Said plainly here rather than dressed up as a quotation.
- **Attribution**: @hpleapfrog · 2026-10-18

### K2 · When v = rω holds (no attack yet)

- **Claim**: `v = rω` holds only when angular velocity is in **radians per second**
- **Premise**: the textbook defines the angle of rotation as `Δθ = Δs / r` and derives `v = rω` (ev-080)
- **Reasoning**: the definition is a pure ratio (arc over radius); in "degrees per second" the
  ratio needs a factor of π/180, and `v = rω` fails
- **Evidence**: ev-080
- **Attacked**: no attacks yet
- **Attribution**: @hpleapfrog · 2026-10-18

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-18 | Entry created; first node of the circular-motion chapter | written after reading m54176 and m54181 in full (ev-080 / ev-081) | @hpleapfrog |
