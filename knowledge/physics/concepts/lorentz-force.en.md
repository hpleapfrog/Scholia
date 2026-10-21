---
id: kb:physics:lorentz-force
type: 知识点
title: "Lorentz force"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know "Magnetic field" and "Uniform circular motion" and need the force on a moving charge and its circular path
  条件: covers F = qvBsinθ, its direction, zero work, and the radius of the circle only; mass spectrometers and cyclotrons now have their own entry, and relativistic corrections are not built
edges:
  先修: ["[Magnetic field](magnetic-field.en.md)", "[Uniform circular motion](uniform-circular-motion.en.md)"]
  支持: []
  攻击: []
evidence: [ev-160]
license: CC-BY-SA-4.0
---

> **English version of [`洛伦兹力.md`](洛伦兹力.md).**

> [!TIP]
> **After reading this entry you should** be able to compute the Lorentz force with `F = qvBsinθ`, find its direction, and explain why a charge entering a uniform field perpendicularly moves in a uniform circle and what sets its radius

## Definition

The **Lorentz force** is the force on a moving charge in a magnetic field:

`F = qvBsinθ`

- `q` is the charge, `v` the speed, `B` the magnetic flux density, and `θ` the angle between the **velocity** and the field
- the force is largest at `θ = 90°` and **zero at `θ = 0°`** (motion along the field)
- **direction**: curl the fingers of the right hand from the velocity `v` toward the field `B`; the thumb gives the force on a **positive** charge. For a negative charge the force is opposite
- the Lorentz force is always **perpendicular to the velocity**, so it **does no work**: it changes the direction of the velocity but not the speed
- a charge entering a uniform field perpendicularly moves in a **uniform circle**: combining `F = mv²/r` with `F = qvB` gives

`r = mv / (qB)`

- the textbook's example: a proton with `v = 3.0×10⁶ m/s` in `B = 2.0 T`, perpendicular, gives `F = 9.6×10⁻¹³ N`; then `a = F/m = 5.7×10¹⁴ m/s²` and `r = v²/a` give `r = 1.6 cm`

> [!IMPORTANT]
> **The right-hand rule applies to positive charge only.**
>
> The textbook writes `The direction in which the right thumb points is the direction of the force`, and the example that follows is a **proton** (`q = 1.60×10⁻¹⁹ C`).
> For an electron the result must be **reversed**, or the direction will be wrong.
>
> The source is also internally inconsistent here: the worked example is titled `Trajectory of Electron in Magnetic Field`,
> one sentence of the stem says `If the electron is moving at 3.0×10⁶ m/s`, and the next asks
> `what is the magnitude and direction of the force on the proton?`; the solution uses `+1.60×10⁻¹⁹ C`.
> **This entry follows the prose and the solution (proton) and records the inconsistency in K2.**

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Magnetic field](magnetic-field.en.md) — the Lorentz force needs `B`; field lines set the second vector of the right-hand rule |
| Prerequisite | [Uniform circular motion](uniform-circular-motion.en.md) — a force perpendicular to the velocity with constant magnitude gives uniform circular motion; the centripetal formula supplies `r` |
| Related | [Ampere force](ampere-force.en.md) — the Ampere force is the macroscopic sum of the Lorentz forces on the carriers; the textbook derives the former from the latter |
| Follow-up | [Mass spectrometers and cyclotrons](mass-spectrometer-and-cyclotron.en.md) — use this entry's `r = mv/(qB)` and `T = 2πm/(qB)` to measure mass-to-charge ratios and accelerate particles repeatedly |
| Follow-up | [Eddy currents and motional emf](eddy-currents-and-motional-emf.en.md) — carriers in a moving rod feel `F = qvB`, and charge separation to `qE = qvB` gives `ε = Bℓv` |

## Argument

### K1 · The Lorentz force does no work and only turns the velocity (no attack yet)

- **Claim**: the Lorentz force does no work; a perpendicularly entering charge keeps its speed and moves in a uniform circle
- **Premise**: the textbook writes `This force is nothing more than a centripetal force: It has a constant magnitude and is always perpendicular to the velocity. Thus, the magnitude of the velocity does not change, and the proton executes circular motion.`; it also computes a radius of `1.6 cm` for the proton (ev-160)
- **Reasoning**: work is the force times the displacement along the force; the Lorentz force is always perpendicular to the velocity and hence to the instantaneous displacement, so the work of every small step is zero and the speed does not change. With a constant magnitude `qvB` always pointing to the centre, the path is a circle whose radius follows from `mv²/r = qvB`
- **Evidence**: ev-160
- **Attacked**: the sentence "does no work" is not in the textbook; it is this repo's inference from "perpendicular to the velocity". The textbook only says the speed does not change. The reasoning also assumes no other forces (gravity negligible, no electric field), which the textbook example does not discuss
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · Radius and period, and the sign of the charge (no attack yet)

- **Claim**: a perpendicularly entering charge has radius `r = mv/(qB)`; the period `T = 2πm/(qB)` is independent of speed; a negative charge feels the opposite force
- **Premise**: the textbook gives only `F = qvBsinθ` and one numerical example (compute `F`, then `a = F/m`, then `r = v²/a = 1.6 cm`); it never writes the algebraic `r`. Its right-hand rule and example both use a proton (ev-160)
- **Reasoning**: substituting `F = qvB` into `F = mv²/r` and eliminating `v` gives `r = mv/(qB)`; then `T = 2πr/v` gives `T = 2πm/(qB)`, with `v` cancelled, so the period depends only on `m`, `q`, and `B`. For direction, the right-hand rule gives the direction of `qv × B`, which reverses when `q` is negative
- **Evidence**: ev-160
- **Attacked**: the algebraic `r` and `T` are this repo's derivation from the textbook's numerical example; the textbook never states them and never mentions that `T` is independent of speed. The worked example is titled "Electron" but its prose and solution compute a proton, and this entry follows the proton. `mv/(qB)` needs relativistic momentum near the speed of light, which the textbook does not cover
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; attached after "Magnetic field" and "Uniform circular motion", the microscopic counterpart of "Ampere force" | written after reading m54465 in full (ev-160) | @hpleapfrog |
| 2026-10-21 | Replaced the "period, cyclotron, mass spectrometer, velocity selector" gap with a link to "Mass spectrometers and cyclotrons"; the period was already derived in K2, so the old gap record was wrong | ev-182 | @hpleapfrog |
| 2026-10-21 | Added a Follow-up link to "Eddy currents and motional emf" | batch 33 created that entry (ev-193) | @hpleapfrog |
