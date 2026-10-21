---
id: kb:physics:projectile-motion
type: 知识点
title: "Projectile motion"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done "Speed and velocity" and "Acceleration" and need to compute the height, time, and range of a projectile
  条件: covers the horizontal/vertical split, maximum height, and level-ground range when air resistance is ignored; the conditions for curved motion and the composition of motions (vectors) are not built
edges:
  先修: ["[Speed and velocity](speed-and-velocity.en.md)", "[Acceleration](acceleration.en.md)"]
  支持: []
  攻击: []
evidence: [ev-163]
license: CC-BY-SA-4.0
---

> **English version of [`抛体运动.md`](抛体运动.md).**

> [!TIP]
> **After reading this entry you should** be able to split projectile motion into uniform horizontal motion and uniformly accelerated vertical motion, use `h = v₀y²/(2g)` and `R = v₀²sin2θ₀/g`, and state their conditions of validity

## Definition

**Projectile motion** is the motion of an object after it is thrown, when air resistance is negligible and gravity is the only force. The object is called a **projectile** and its path is its **trajectory**. The textbook: `Projectile motion is the motion of an object thrown (projected) into the air when, after the initial force that launches the object, air resistance is negligible and the only other force that object experiences is the force of gravity.`

- horizontal: `a_x = 0`, `v_x = v₀cosθ₀` is constant, `x = v_x t`
- vertical: taking **up as positive**, `a_y = −g = −9.80 m/s²`; `v_y = v₀y − gt`, `y = v₀y t − ½gt²`
- the two directions are **independent**; the only shared quantity is the time `t`
- maximum height: `h = v₀y²/(2g)`, set by the vertical component alone
- level-ground range: `R = v₀² sin2θ₀ / g`; complementary angles give the same range (textbook figure note), and `θ₀ = 45°` gives the maximum (the repo derives this, see K2)
- textbook examples: fireworks `v₀ = 70.0 m/s` at `θ₀ = 75°` → `v₀y = 67.6 m/s`, `h = 233 m`, `t = 6.90 s`, `x = 125 m`; volcano rock `v₀ = 25.0 m/s` at `θ₀ = 35°`, landing 20.0 m lower → `t = 3.96 s`
- air resistance: the textbook defines it as `a frictional force that slows the motion` and states that introductory physics treats only cases where the deviation is negligible and air resistance can be ignored

> [!IMPORTANT]
> **"Independence" is an approximation that ignores air resistance, and the two balls line up strictly only for a horizontal launch.**
>
> The textbook: `when air resistance is ignored, horizontal and vertical motions are independent`, and it compares a free-falling ball with a horizontally launched one — their vertical positions agree in time. It also notes that if the launch has a vertical component, the vertical displacements no longer line up. A real projectile feels air resistance in both directions, and then "independence" no longer holds strictly.

> [!IMPORTANT]
> **The range formula has conditions.**
>
> The textbook: `the range doesn't apply to problems where the initial and final y position are different, or to cases where the object is launched perfectly horizontally.` The volcano-rock example is the counter-example: the landing point is 20.0 m below the start, the range formula does not apply, and only the vertical quadratic can be solved.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Speed and velocity](speed-and-velocity.en.md) — the components `v₀x = v₀cosθ₀`, `v₀y = v₀sinθ₀` and the direction of the resultant velocity come from here |
| Prerequisite | [Acceleration](acceleration.en.md) — splitting the motion requires constant acceleration along each axis: `a_x = 0`, `a_y = −g` |
| Recorded gap | **The conditions for curved motion** (velocity tangent to the path, net force not collinear with velocity) are not covered by this module; **composition of motions and vector algebra belong to mathematics** and are not built here — [Force (HS)](force.en.md) records the same vector prerequisite gap |

## Argument

### K1 · Horizontal and vertical motions are independent (no attack yet)

- **Claim**: with air resistance ignored, a projectile's horizontal and vertical motions do not affect each other; `a_x = 0`, `a_y = −g`, and the two directions share only the time `t`
- **Premise**: the textbook writes `when air resistance is ignored, horizontal and vertical motions are independent, meaning that they don't influence one another`, compares a free-falling ball with a horizontally launched one, and writes `the only common variable between the motions is time t` (ev-163)
- **Reasoning**: gravity points vertically down, so it changes only `v_y`; with no horizontal force, `v_x` stays constant. A two-dimensional problem therefore splits into two one-dimensional problems, each solved with constant-acceleration formulas, and the total displacement and velocity are recombined as vectors. This also explains why a dropped object and a horizontally launched one land at the same time
- **Evidence**: ev-163
- **Attacked**: the textbook takes "independence" as a starting point and **does not derive it from Newton's second law** — it simply states `a_x = 0` and `a_y = −g`, and "gravity only" is where the independence comes from. Independence is also only an approximation when **air resistance is ignored**: drag acts in both directions and couples them. The textbook itself notes, when comparing the two balls, that the displacements line up strictly only when the launch has no vertical component. There is also a sign defect in the source: the fireworks example's Strategy says `a_y = g`, while the same solution takes up as positive and uses `a_y = −g` throughout, and its numbers agree with `−g`
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · Maximum height depends only on the vertical component; range also depends on the angle (no attack yet)

- **Claim**: `h = v₀y²/(2g)` depends only on the vertical component; on level ground `R = v₀²sin2θ₀/g`, complementary angles give equal ranges, and `45°` gives the maximum range
- **Premise**: the textbook gives `h = v₀y²/(2g)` and `R = v₀²sin2θ₀/g`, notes in a figure caption that `any combination of trajectories that add to 90 degrees will have the same range`, and states that the range formula does not apply when the start and end heights differ or the launch is horizontal (ev-163)
- **Reasoning**: at the top `v_y = 0`, so `v_y² = v₀y² − 2gh` gives `h`. On level ground the flight time is `t = 2v₀y/g = 2v₀sinθ₀/g`, so `R = v_x t = v₀cosθ₀ · 2v₀sinθ₀/g = v₀²sin2θ₀/g`; `sin2θ₀` is largest when `2θ₀ = 90°`, i.e. `θ₀ = 45°`. Eliminating `t` gives the trajectory `y = x tanθ₀ − gx²/(2v₀²cos²θ₀)`, a parabola (the trajectory equation and the parabolic shape are the repo's addition)
- **Evidence**: ev-163
- **Attacked**: the textbook **does not derive** either formula (the maximum height comes from simplifying the example, the range is stated outright), and it **never says "45° gives the maximum range"** — it only says complementary angles give equal ranges; "45° is maximal" and the trajectory equation are the repo's inferences. The range formula applies to level ground only, and the textbook explicitly excludes unequal heights and horizontal launches; with air resistance the trajectory is no longer symmetric and all of these conclusions must be rechecked
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; first node of the 必修二 chapter 5 "projectile motion", attached after "Speed and velocity" and "Acceleration" | written after reading m54162 in full (ev-163) | @hpleapfrog |
