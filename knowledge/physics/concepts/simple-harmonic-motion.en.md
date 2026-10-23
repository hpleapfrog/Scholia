---
id: kb:physics:simple-harmonic-motion
type: 知识点
title: "Simple harmonic motion"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know Newton's second law and need to decide whether an oscillation is simple harmonic and to compute the period and frequency of a spring oscillator
  条件: covers Hooke's law, the restoring force, amplitude/period/frequency, and the spring oscillator only; phase, the energy of simple harmonic motion, damped oscillation, forced oscillation, and resonance have their own entries
edges:
  先修: ["[Newton's second law](newtons-second-law.en.md)"]
  支持: []
  攻击: []
evidence: [ev-164]
license: CC-BY-SA-4.0
---

> **English version of [`简谐运动.md`](简谐运动.md).**

> [!TIP]
> **After reading this entry you should** be able to decide whether an oscillation is simple harmonic by checking that the restoring force is proportional and opposite to the displacement, write `T = 2π√(m/k)` for a spring oscillator, and tell amplitude, period, and frequency apart

## Definition

**Oscillation** is back-and-forth motion between two points; **periodic motion** repeats itself at regular time intervals. The time for one complete oscillation is the **period** `T` (seconds); the number of oscillations per unit time is the **frequency** `f`, with `f = 1/T`, in hertz (Hz). The **amplitude** `X` is the maximum displacement from equilibrium; the **equilibrium position** is where the object would rest in the absence of a net force.

**Simple harmonic motion** is the simplest oscillation: its net force can be described by Hooke's law.

`F = −k x`

- `x` is the deformation (displacement from equilibrium), `k` the force constant, in N/m
- the **restoring force** brings the object back to equilibrium; the minus sign says it points opposite to the displacement
- a larger `k` means a stiffer system that needs a larger restoring force for the same deformation
- the textbook's figure note: the spring oscillator's **maximum speed occurs at equilibrium**; a stiffer spring gives a smaller period and a larger mass gives a larger period

For a spring oscillator the period and frequency are

`T = 2π√(m/k)`, `f = (1/2π)√(k/m)`

The textbook writes `The mass m and the force constant k are the only factors that affect the period and frequency of simple harmonic motion.`

> [!IMPORTANT]
> **The minus sign in Hooke's law fixes direction, not magnitude.**
>
> The body writes `F = −kx` and explains `the minus sign is there because the restoring force acts in the direction opposite to the displacement`.
> The same module's glossary, however, writes Hooke's law as `F = kΔL` — no minus sign, and `ΔL` instead of `x`.
> The two agree only on "magnitude is proportional"; this entry uses the body's vector form and records the glossary as an internal inconsistency.

> [!IMPORTANT]
> **The period formula holds only for Hooke-type systems such as the spring oscillator.**
>
> `T = 2π√(m/k)` is not "the formula for every oscillation": it assumes a restoring force exactly proportional to displacement, a massless spring, and no damping.
> Next to the formula the textbook says only that mass and force constant are the only factors; it does not list these assumptions.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Newton's second law](newtons-second-law.en.md) — `F = −kx` explains "the acceleration always points toward equilibrium" only through `a = F/m`; the textbook's `[BL]` also asks students to review the concept of force |
| Follow-up | [Simple pendulum](simple-pendulum.en.md) — at small angles the pendulum is a special case of simple harmonic motion; the textbook's pendulum section prompts `[BL] Review simple harmonic motion` |
| Follow-up | [Phase and energy of simple harmonic motion](phase-and-energy-of-shm.en.md) — phase, the general form `x = X cos(ωt + φ)`, and energy conservation |
| Follow-up | [Damped and forced oscillation](damped-and-forced-oscillation.en.md) — the undamped idealisation assumed here is dropped there |
| Recorded gap | **Experimental measurement of phase difference (Lissajous figures)**, **superposition of oscillations of different frequencies (beats)**, and **the damping equation and quality factor** are not built in this repo; phase, energy, damping, and forced oscillation now have their own entries |

## Argument

### K1 · The test for simple harmonic motion is a restoring force proportional and opposite to displacement (no attack yet)

- **Claim**: an oscillation is simple harmonic if and only if its net force satisfies `F = −kx`
- **Premise**: the textbook uses a plastic ruler to show that the restoring force always points toward equilibrium, writes `The simplest oscillations occur when the restoring force is directly proportional to displacement.`, and defines simple harmonic motion by `F = −kx` (ev-164)
- **Reasoning**: by Newton's second law, `a = F/m = −(k/m)x`: the acceleration is proportional and opposite to the displacement, so the object reaches maximum speed at equilibrium and turns back at the extremes. The figure note states the "maximum speed at equilibrium" consequence
- **Evidence**: ev-164
- **Attacked**: the textbook does not prove that only a proportional restoring force qualifies as simple harmonic motion; it treats the condition as a definition. In the pendulum section the same module also calls the small-angle `−mg sinθ` simple harmonic motion, so "proportional" is used both as a strict definition and as an approximation — this entry keeps the two uses apart
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · A spring oscillator's period depends only on mass and force constant (no attack yet)

- **Claim**: `T = 2π√(m/k)`; amplitude and initial speed do not change the period
- **Premise**: the textbook gives the period and frequency formulas and writes `The mass m and the force constant k are the only factors that affect the period and frequency of simple harmonic motion.`; the figure note adds that a stiffer spring gives a smaller period and a larger mass a larger period (ev-164)
- **Reasoning**: dimensionally `√(kg/(N/m)) = √(kg·m/N) = √(s²) = s`; combining `a = −(k/m)x` with the back-and-forth structure gives a period containing only `m` and `k`. Amplitude sets the maximum displacement and maximum speed, not this time scale
- **Evidence**: ev-164
- **Attacked**: the textbook states the formula without deriving it and without naming the assumptions "ideal spring, no damping, small deformation"; "only factors" holds inside that ideal model, and the module does not discuss what happens when spring mass or damping cannot be neglected
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; first node of the 选必一 "mechanical vibration" chapter, attached after "Newton's second law" | written after reading m54154 in full (ev-164) | @hpleapfrog |
| 2026-10-21 | Gap table updated: phase and energy now in "Phase and energy of simple harmonic motion", damping and forced oscillation in "Damped and forced oscillation"; condition and relations updated | synced after reading ev-190/ev-191 | @hpleapfrog |
