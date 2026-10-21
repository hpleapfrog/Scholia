---
id: kb:physics:magnetic-flux
type: 知识点
title: "Magnetic flux"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know "Magnetic field" and need "the number of field lines through a loop" before induction
  条件: covers Φ = BAcosθ, its unit, and the three ways to change it only; Faraday's law and Lenz's law are a separate entry
edges:
  先修: ["[Magnetic field](magnetic-field.en.md)"]
  支持: []
  攻击: []
evidence: [ev-161]
license: CC-BY-SA-4.0
---

> **English version of [`磁通量.md`](磁通量.md).**

> [!TIP]
> **After reading this entry you should** be able to compute magnetic flux with `Φ = BAcosθ`, explain how a non-zero field can give zero flux, and list the three ways to change the flux

## Definition

The **magnetic flux** `Φ` describes how many field lines pass through a surface:

`Φ = BAcosθ`

- `B` is the magnetic flux density, `A` the area, and `θ` the angle between the **field** and the **normal** to the surface (the area vector)
- the unit is the **weber** (Wb). `1 Wb = 1 T·m²`, which also equals `1 V·s`
- only the component **perpendicular** to the surface, `Bcosθ`, contributes; a field lying in the surface gives `θ = 90°`, `cos90° = 0`, and zero flux
- the flux can be changed in three ways: **change `B`**, **change the area `A`**, or **change the angle `θ`**. The textbook's examples cover the first two directly; a rotating coil covers the third
- the textbook uses a sail analogy: `Think of the conducting loop as the sail and the magnetic field as the wind.` A sail facing the wind catches the most; edge-on it catches none — `θ = 0°` versus `θ = 90°`

> [!IMPORTANT]
> **The weber is `T·m²`, not `T/m²`.**
>
> The textbook writes `The unit of magnetic flux is the weber (Wb), which is magnetic field per unit area, or T/m2`.
> `Φ = BAcosθ` multiplies the field by an area, so its unit is `T·m²`; `T/m²` contradicts the formula.
> The sentence right after, `The weber is also a volt second (Vs)`, is correct.
> **This entry uses `T·m²` and records the source's error here (ev-161).**
>
> One more point: flux is a **scalar**, but it can be negative — the sign depends on which way the area vector points.
> The textbook uses a minus sign in Faraday's law to express "opposing the change", but never discusses the sign convention of `Φ` on its own.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Magnetic field](magnetic-field.en.md) — `B` and field lines are the inputs; "lines through a surface" is the field-line picture |
| Follow-up | [Electromagnetic induction](electromagnetic-induction.en.md) — the **rate of change** of the flux sets the induced emf; a constant flux induces nothing |
| Recorded gap | **The sign convention linking flux to the area vector**, and **the fluxmeter**, are not built in this repo |

## Argument

### K1 · Only the perpendicular component contributes (no attack yet)

- **Claim**: the `cosθ` in `Φ = BAcosθ` is not a correction term; it is what "through" means
- **Premise**: the textbook states `magnetic field lines that lie in the plane of the wire loop do not actually pass through the loop`, calls `Bcosθ` `the component of the magnetic field that is perpendicular to the plane of the loop`, and uses the sail analogy for the same point (ev-161)
- **Reasoning**: a surface can only be passed through by the component perpendicular to it; a parallel component merely slides along the surface. Splitting `B` into perpendicular and parallel parts, only the perpendicular part times the area gives the flux, hence `Φ = BAcosθ`
- **Evidence**: ev-161
- **Attacked**: "field lines passing through" is a picture, not a definition; the strict definition is the integral of the normal component of `B` over the surface. The textbook treats only uniform fields and flat areas, and so does this entry
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · Three ways to change the flux (no attack yet)

- **Claim**: changing `B`, `A`, or `θ` changes the flux; a constant flux induces no emf
- **Premise**: the textbook gives three kinds of example — a magnet moving relative to a coil, a coil whose area changes (the slider circuit), and a coil rotated to change `θ` — and writes `Experiments show that changing the area of a conducting loop in a stable magnetic field induces an emf in the loop` (ev-161)
- **Reasoning**: `Φ = BAcosθ` is a product of three quantities; if any one changes with time, `Φ` changes and `ΔΦ/Δt ≠ 0`. With a stationary magnet, fixed area, and fixed angle, all three are constant, the flux is constant, and there is no emf
- **Evidence**: ev-161
- **Attacked**: "three ways" is this repo's grouping by the three factors; the textbook shows them through three examples rather than stating the trichotomy. It also does not discuss how to split the contributions when `B`, `A`, and `θ` change together
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; fills the "magnetic flux missing" gap recorded on the coverage page, as the prerequisite of the induction law | written after reading m54456 in full (ev-161) | @hpleapfrog |
