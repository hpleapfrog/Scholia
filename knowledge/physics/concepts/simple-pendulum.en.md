---
id: kb:physics:simple-pendulum
type: 知识点
title: "Simple pendulum"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know simple harmonic motion and need to decide when a pendulum is simple harmonic and to use it to measure g
  条件: covers the small-angle simple pendulum, its restoring force and period only; pendulum energy is in "Phase and energy of simple harmonic motion", and damping and forced oscillation have their own entry; the conical pendulum, physical pendulum, and large-angle period corrections are not built
edges:
  先修: ["[Simple harmonic motion](simple-harmonic-motion.en.md)", "[Force (HS)](force.en.md)"]
  支持: []
  攻击: []
evidence: [ev-164]
license: CC-BY-SA-4.0
---

> **English version of [`单摆.md`](单摆.md).**

> [!TIP]
> **After reading this entry you should** be able to explain why a small-angle pendulum is approximately simple harmonic, write `T = 2π√(L/g)`, and explain why the period does not depend on the bob's mass or the amplitude

## Definition

A **simple pendulum** is a small bob hanging from a light, inextensible string. Its equilibrium position is the string hanging straight down, `θ = 0`; when the bob is displaced, the displacement is the arc length `s`.

Two forces act on the bob: its weight `mg` and the string's tension `T`. Resolve the weight along the string and along the tangent:

- the component `mg cosθ` along the string is cancelled by the tension
- the tangential component `mg sinθ` points toward equilibrium and is the **restoring force**, written `−mg sinθ`

For angles below about 15° the textbook treats the pendulum as simple harmonic and gives the period

`T = 2π√(L/g)`

where `L` is the length and `g` the acceleration due to gravity. The textbook writes `The only things that affect the period of a simple pendulum are its length and the acceleration due to gravity.` and stresses `The period is completely independent of other factors, such as mass or amplitude.`

- solving for `g` gives `g = 4π²L/T²`; the worked example uses `L = 75.000 cm` and `T = 1.7357 s` to get `g = 9.8281 m/s²`
- the student experiment uses about 1 m of string, a small dense object, and a stopwatch, releasing from less than 10° and timing 10 oscillations before computing the period

> [!IMPORTANT]
> **Tension and period share the symbol `T`, and the textbook warns about it.**
>
> It writes `Tension is represented by the variable T, and period is represented by the variable T. It is important not to confuse the two, since tension is a force and period is a length of time.`
> This entry writes tension as "tension" in words and keeps `T` for the period; when solving problems the two must be kept apart.

> [!IMPORTANT]
> **"Below 15° is simple harmonic" is an approximation, not a strict result.**
>
> The exact restoring force `−mg sinθ` is not proportional to `θ`; only `sinθ ≈ θ` (in radians) at small angles makes it proportional.
> The textbook states that a pendulum below 15° `experiences simple harmonic oscillation` without showing the approximation or giving the error at 15°.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Simple harmonic motion](simple-harmonic-motion.en.md) — the pendulum is a small-angle special case; the section prompts `[BL] Review simple harmonic motion` |
| Prerequisite | [Force (HS)](force.en.md) — resolving the weight into `mg cosθ` and `mg sinθ` and deciding which component the tension cancels; the resolution itself needs **vectors**, a mathematics node not built in this repo |
| Related | [Phase and energy of simple harmonic motion](phase-and-energy-of-shm.en.md) — the pendulum's energy uses the same `½kx² + ½mv²` equation with `k = mg/L`, `x = Lθ` |
| Related | [Damped and forced oscillation](damped-and-forced-oscillation.en.md) — a swing is a forced-oscillation example; this entry covers only small-angle motion without damping |
| Recorded gap | **Large-angle period corrections (elliptic integrals)**, **the conical pendulum**, and **the physical pendulum** are not built in this repo; pendulum energy is in "Phase and energy of simple harmonic motion", and damping and forced oscillation have their own entry |

## Argument

### K1 · At small angles the pendulum is approximately simple harmonic (no attack yet)

- **Claim**: below about 15° the pendulum's restoring force is approximately proportional to displacement, so the motion is simple harmonic
- **Premise**: the textbook resolves the forces to get the tangential restoring force `−mg sinθ` and writes `For small displacements of less than 15 degrees, a pendulum experiences simple harmonic oscillation, meaning that its restoring force is directly proportional to its displacement.` (ev-164)
- **Reasoning**: the arc displacement is `s = Lθ`, so `sinθ ≈ θ = s/L` and the restoring force is `−mg sinθ ≈ −(mg/L)s` — proportional and opposite to displacement, which meets the simple-harmonic test, with effective force constant `mg/L`
- **Evidence**: ev-164
- **Attacked**: the textbook asserts that the restoring force is proportional below 15° but does not show the `sinθ ≈ θ` step or justify the 15° threshold and its error; the exact force `−mg sinθ` is nonlinear, so "simple harmonic" is only an approximation
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · The pendulum period is independent of mass and amplitude (no attack yet)

- **Claim**: `T = 2π√(L/g)`; neither the bob's mass nor the amplitude (within small angles) changes the period
- **Premise**: the textbook gives the period formula and writes `The period is completely independent of other factors, such as mass or amplitude.`; the same page notes that `T` depends on `g`, so a pendulum can measure the acceleration due to gravity (ev-164)
- **Reasoning**: from K1 the effective force constant is `k = mg/L`; substituting into the spring period `T = 2π√(m/k)` cancels the mass `m` and leaves `T = 2π√(L/g)`. Amplitude changes the maximum displacement and speed but not the period
- **Evidence**: ev-164
- **Attacked**: independence from mass and amplitude holds only inside the model "small angle + light string + no air resistance + point bob"; the textbook does not discuss how the period changes as the amplitude approaches or exceeds 15°, nor does it state the model's limits
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; second node of the 选必一 "mechanical vibration" chapter, attached after "Simple harmonic motion" | written after reading m54154 in full (ev-164) | @hpleapfrog |
| 2026-10-21 | Gap table updated: pendulum energy is in "Phase and energy of simple harmonic motion", damping and forced oscillation have their own entry; condition and relations updated | synced after reading ev-190/ev-191 | @hpleapfrog |
