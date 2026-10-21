---
id: kb:physics:phase-and-energy-of-shm
type: 知识点
title: "Phase and energy of simple harmonic motion"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know simple harmonic motion and Hooke's law and need to write the equation of motion, compare the timing of two oscillations, and compute kinetic and potential energy
  条件: covers phase, phase difference, and the energy of a spring oscillator or pendulum only; damping, forced oscillation, and resonance have their own entry; experimental measurement of phase difference and the superposition of different frequencies are not built
edges:
  先修: ["[Simple harmonic motion](simple-harmonic-motion.en.md)"]
  支持: []
  攻击: []
evidence: [ev-190]
license: CC-BY-SA-4.0
---

> **English version of [`简谐运动的相位与能量.md`](简谐运动的相位与能量.md).**

> [!TIP]
> **After reading this entry you should** be able to write simple harmonic motion as `x = X cos(ωt + φ)`, read off the phase and the initial phase, explain how the phase difference between two oscillations of the same frequency becomes a time difference, and compute kinetic and potential energy at any position with `E = ½kX²` and `v = ±ω√(X² − x²)`

## Definition

**Phase** is the angle that says where in its cycle an oscillation is. The textbook treats the projection of uniform circular motion as simple harmonic motion (ev-190):

`x = X cos θ`, where `θ = ωt`, `ω = 2π/T`

so `x(t) = X cos(2πt/T)`. The angle `θ` grows at the constant angular frequency `ω`, and every increase of `2π` completes one full oscillation — the phase is the "position within the cycle".

The more general form is

`x = X cos(ωt + φ)`

where `θ = ωt + φ` is the phase and `φ` is the phase at `t = 0`, called the **initial phase**. The textbook gives only the special case `φ = 0` (released from maximum displacement at `t = 0`); the general form with `φ` is a **library addition**, not a textbook sentence. Phase is an angle in radians (rad), not a displacement. For given `X` and `ω`, the phase fixes both the displacement ratio `x/X` and the direction of velocity.

For two oscillations of the same frequency,

`x₁ = X cos(ωt + φ₁)`, `x₂ = X cos(ωt + φ₂)`

the **phase difference** `Δφ = φ₂ − φ₁` does not change with time. `Δφ = 2kπ` is called in phase, `Δφ = (2k+1)π` antiphase. The conversion to a time difference is `Δt = |Δφ|/ω` (library addition): the oscillation with the lagging phase reaches the same state `Δt` later.

`ω = 2π/T = 2πf` is the **angular frequency**, in rad/s.

### Energy

For an undamped spring oscillator the elastic potential energy and kinetic energy are

`PE_el = ½kx²`, `KE = ½mv²`

The textbook writes `KE + PE_el = constant`, that is

`½mv² + ½kx² = ½kX²`

The right-hand side is the total energy at `t = 0`, `x = X`, `v = 0`. Solving for the speed,

`v = ±√(k/m)√(X² − x²) = ±ω√(X² − x²)`, `ω = √(k/m)`

- at equilibrium `x = 0`: `|v| = v_max = ωX`, all energy kinetic
- at the extremes `x = ±X`: `v = 0`, all energy elastic potential
- anywhere: `KE = ½k(X² − x²)`, `PE_el = ½kx²`
- from `a = −(k/m)x = −ω²x`, `a_max = ω²X` (derived here from Newton's second law and `ω² = k/m`; not given by the textbook)

The small-angle energy of a pendulum follows from the same equation by substitution (textbook):

`v = Lω`, `k = mg/L`, `x = Lθ` ⇒ `½mL²ω² + ½mgLθ² = constant`

Here `ω` is the pendulum's angular velocity `dθ/dt`, not the angular frequency `ω = 2π/T` of the circular-motion projection (see the callout below).

Textbook example: a 900 kg car, `k = 6.53×10⁴ N/m`, `X = 0.100 m`, gives `v_max = 0.852 m/s`. Recomputation: `√(6.53×10⁴/900) × 0.100 = 8.518 × 0.100 = 0.852 m/s`. Textbook AP question: `m = 1 kg`, `X = 1 m`, `T = 1 s`, gives `k = 4π²m/T² = 39.48 N/m`, `E = ½kX² = 19.74 J` (the text's answer is `19.7 J`). When `v = v_max/2`, `x/X = √3/2 ≈ 0.866` (textbook exercise, recomputed here).

> [!IMPORTANT]
> **The initial phase `φ` in the general form is a library addition, not textbook content.**
>
> Module m42245 gives only `x = X cos(2πt/T)`, equivalent to `φ = 0`; it defines neither initial phase, phase difference, nor time difference.
> The addition follows from the definition of phase, `θ = ωt + φ`; wherever this entry uses `φ` or `Δφ`, it is treating them as additions.

> [!IMPORTANT]
> **The same `ω` has two meanings in the textbook.**
>
> In the circular-motion projection and `T = 2π/ω`, `ω` is the **angular frequency** (constant, `2π/T`);
> in the pendulum energy expression `v = Lω`, `ω` is the pendulum's **angular velocity** `dθ/dt` (changing as it swings).
> The textbook uses one letter and gives no warning.

> [!NOTE]
> **Three problems in the source.**
>
> 1. An AP question calls `½kX²` the `internal energy`; this is the mechanical energy of the spring oscillator, not the thermodynamic internal energy — same name, different quantity.
> 2. The Section Summary renders `v_max` as `Xkm`; the body's expression is `X√(k/m)`.
> 3. The textbook writes the energy equation only for the spring oscillator; the pendulum is a direct substitution of `k = mg/L` and `x = Lθ`, without saying that it relies on the small-angle approximation `sinθ ≈ θ`.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Simple harmonic motion](simple-harmonic-motion.en.md) — both the equation and the energy rest on `F = −kx` and `T = 2π√(m/k)`; this entry connects `ω = 2π/T` with `√(k/m)` |
| Related | [Simple pendulum](simple-pendulum.en.md) — the pendulum's energy uses the same `½kx² + ½mv²` equation with `k = mg/L`, `x = Lθ`; the pendulum entry covers the period only, not the energy |
| Follow-up | [Damped and forced oscillation](damped-and-forced-oscillation.en.md) — damping starts from "mechanical energy is no longer conserved"; this entry's energy equation is its starting point |
| Recorded gap | **Experimental measurement of phase difference (Lissajous figures)**, **superposition of oscillations of different frequencies (beats)**, **energy decay under damping**, and **phase difference in AC circuits** are not built in this repo; the textbook gives only the zero-initial-phase projection |

## Argument

### K1 · Phase encodes "where it is and which way it moves" as one angle (projection from the textbook; initial phase and phase difference added here)

- **Claim**: simple harmonic motion can be written `x = X cos(ωt + φ)`; the phase `θ = ωt + φ`, together with the amplitude, fixes the displacement ratio `x/X` and the direction of velocity; for two oscillations of the same frequency the phase difference is constant, and `Δφ` corresponds to a time difference `Δt = |Δφ|/ω`
- **Premise**: the textbook treats the projection of uniform circular motion as simple harmonic motion and gives `x = X cos θ`, `θ = ωt`, `ω = 2π/T` (ev-190)
- **Reasoning**: the projected point moves round the circle at constant `ω`, with `x = X cos θ`; every increase of `2π` in `θ` completes one oscillation, so `θ` marks "where in the cycle". For two oscillations of equal frequency `θ₂ − θ₁` does not change with time; substituting `θ = ωt + φ`, at `t = 0` we have `θ = φ`, so `φ` is the initial phase. The textbook takes only `φ = 0` (released from maximum displacement at `t = 0`); the general form is added here from the definition of phase
- **Evidence**: ev-190
- **Attacked**: the textbook gives no `φ`, no phase difference, no time difference, and no proof that every simple harmonic motion can be written as a cosine; the projection is a kinematic correspondence, not a dynamical derivation from `F = −kx`. The general form added here is not in the textbook examined
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · An undamped simple harmonic oscillator conserves mechanical energy, which moves between kinetic and elastic potential energy

- **Claim**: `½mv² + ½kx² = ½kX²`; anywhere `KE = ½k(X² − x²)`, `PE_el = ½kx²`; `v_max = ωX` at equilibrium
- **Premise**: the textbook gives `PE_el = ½kx²` and `KE + PE_el = constant`, solves `v = ±√(k/m)√(X² − x²)` from `x = X`, `v = 0`, and writes that the energy `oscillates back and forth between kinetic and potential, going completely from one to the other` (ev-190)
- **Reasoning**: without dissipation the total energy equals the initial potential energy `½kX²`; substituting into `½mv² + ½kx² = ½kX²` gives `v(x)`. At `x = 0` the potential energy is zero and the kinetic energy is largest; at `x = ±X` the kinetic energy is zero and the potential energy is largest. With `ω = √(k/m)`, `v_max` becomes `ωX`
- **Evidence**: ev-190
- **Attacked**: the textbook writes the energy equation only for the spring oscillator; the pendulum is a direct substitution without the small-angle condition; there is no potential-energy curve or energy–time graph; damping is assumed absent. An AP question calls `½kX²` the `internal energy`, which is not the thermodynamic internal energy
- **Attribution**: @hpleapfrog · 2026-10-21

### K3 · A phase difference gives two same-frequency oscillations a "time difference" reading (library addition)

- **Claim**: for two oscillations of the same frequency and amplitude, if `x₂` lags `x₁` in phase by `Δφ`, then `x₂` reaches the same state `Δt = Δφ/ω` later; `Δφ = 0` means they move in step and `Δφ = π` means antiphase
- **Premise**: the textbook gives `x = X cos θ` and `θ = ωt` (ev-190); the phase-difference–time-difference conversion is added here
- **Reasoning**: let `x₁ = X cos(ωt)` and `x₂ = X cos(ωt + Δφ)`. With `t′ = t + Δφ/ω`, `x₂(t) = x₁(t′)`: the state of `x₂` at `t` equals the state of `x₁` at `t + Δφ/ω`, so `x₂` lags by `Δφ/ω`. At `Δφ = π`, `x₂ = −x₁`
- **Evidence**: ev-190 (the projection relation only; the conversion is added here)
- **Attacked**: the textbook has no phase difference, no time-difference conversion, and no discussion of superposing two oscillations; this entry does not cover the superposition of different frequencies (beats) or the experimental measurement of phase difference, both recorded as gaps
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; closes the phase and energy gaps recorded in "Simple harmonic motion" and attaches after that entry | written after reading m42244/m42245 in full (ev-190); the initial phase, phase difference, time difference, and `a_max` are marked as library additions | @hpleapfrog |
