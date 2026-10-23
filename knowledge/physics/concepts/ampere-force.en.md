---
id: kb:physics:ampere-force
type: 知识点
title: "Ampere force"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know "Magnetic field" and need to compute the force on a current-carrying wire and its direction
  条件: covers the force on a straight wire in a uniform field, F = IℓBsinθ, its direction, and motors; bent wires, magnetic moment, and coil torque are not built
edges:
  先修: ["[Magnetic field](magnetic-field.en.md)"]
  支持: []
  攻击: []
evidence: [ev-160]
license: CC-BY-SA-4.0
---

> **English version of [`安培力.md`](安培力.md).**

> [!TIP]
> **After reading this entry you should** be able to compute the force on a straight wire with `F = IℓBsinθ`, find its direction with the right-hand rule, and explain why a current parallel to the field feels no force

## Definition

The **Ampere force** is the force on a current-carrying wire in a magnetic field. For a **straight** segment in a uniform field:

`F = IℓBsinθ`

- `I` is the current, `ℓ` is the length of the wire **inside the field**, and `B` is the magnetic flux density
- `θ` is the angle between the **current direction** and the magnetic field
- the force is largest at `θ = 90°` and **zero at `θ = 0°`** (current parallel to the field)
- **direction**: curl the fingers of the right hand from the current `I` toward the field `B`; the thumb gives the force. The force is perpendicular to both the current and the field
- this force is the basis of **all electric motors**. The textbook: `The force on a current-carrying wire in a magnetic field is the basis of all electrical motors`
- the textbook's worked example: 1.5 A through 4.0 cm of wire in a 2.0 T field, perpendicular, gives `F = 0.12 N`

> [!IMPORTANT]
> **The direction is found from the current, not from the motion of electrons.**
>
> The textbook's current `I` is conventional current, and the right-hand rule uses `I`.
> In a metal wire the moving charges are electrons, which travel opposite to `I`;
> **judging by the electron flow reverses the force once, so it must be reversed back**.
> The textbook does not warn about this at the Ampere force — this repo's
> [current-direction misconception](../misconceptions/conventional-current.en.md) records the same confusion.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Magnetic field](magnetic-field.en.md) — without a field there is no "force in a field"; `B` and field lines are the inputs to the formula |
| Follow-up | [Lorentz force](lorentz-force.en.md) — the Ampere force is the macroscopic sum of the Lorentz forces on the charge carriers; the textbook derives the former from the latter |
| Recorded gap | **Force on a bent wire**, **magnetic moment and torque on a coil**, and **moving-coil meters** are not built in this repo |

## Argument

### K1 · The Ampere force is the macroscopic result of the Lorentz force (no attack yet)

- **Claim**: `F = IℓBsinθ` is not an independent force law; it is the sum of the Lorentz forces on the charge carriers in the wire
- **Premise**: the textbook first gives the single-charge force `F = qvBsinθ`, then lets the charges move a distance `ℓ` in time `t`, so `v = ℓ/t`, giving `F = q(ℓ/t)Bsinθ = (q/t)ℓBsinθ`; it notes `The factor q/t in this equation is nothing more than the current in the wire` (ev-160)
- **Reasoning**: current is the charge passing per unit time, so `q/t = I`; multiplying the single-charge force by the charge passing per second gives the force on the whole segment. The `sinθ` factor is inherited from the single-charge case
- **Evidence**: ev-160
- **Attacked**: the derivation assumes all carriers move along the wire at one speed and ignores thermal motion; `ℓ` must be the length **inside the field**, which the textbook stresses after the formula (`ℓ is the length of wire that is in the magnetic field`). It does not discuss bent wires or non-uniform fields
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · The direction comes from the right-hand rule and is perpendicular to both vectors (no attack yet)

- **Claim**: the Ampere force is perpendicular to both the current and the field, and the right-hand rule fixes its direction
- **Premise**: the textbook writes `The direction of the force is determined in the same way as for a single charge. Curl your right fingers from the vector for I to the vector for B, and your right thumb will point in the direction of the force on the wire.`; the wire example points the same way as the proton example (ev-160)
- **Reasoning**: if the current and the field are not parallel they span a plane, and the force is perpendicular to that plane; swapping the order of `I` and `B` reverses the force. The `sinθ` factor makes the force zero when they are parallel
- **Evidence**: ev-160
- **Attacked**: the textbook gives only one wire example at `θ = 90°`; general angles appear only in the formula. "Swapping the order reverses the direction" is this repo's reading of the right-hand rule, not a statement in the text. Also, the force on the wire is not the direction of the force on an individual electron in it (the electron is negative)
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; attached after "Magnetic field", the macroscopic counterpart of "Lorentz force" | written after reading m54465 in full (ev-160) | @hpleapfrog |
