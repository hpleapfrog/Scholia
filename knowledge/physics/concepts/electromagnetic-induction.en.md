---
id: kb:physics:electromagnetic-induction
type: 知识点
title: "Electromagnetic induction"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know "Magnetic flux" and "Resistance and Ohm's law" and need to compute an induced emf and its direction
  条件: covers Faraday's law, Lenz's law, and the energy balance of the slider circuit only; self-inductance, mutual inductance, and eddy currents are separate entries (AC generators are a separate entry)
edges:
  先修: ["[Magnetic flux](magnetic-flux.en.md)", "[Resistance and Ohm's law](resistance-and-ohms-law.en.md)"]
  支持: []
  攻击: []
evidence: [ev-161]
license: CC-BY-SA-4.0
---

> **English version of [`电磁感应定律.md`](电磁感应定律.md).**

> [!TIP]
> **After reading this entry you should** be able to compute an induced emf with `ε = −NΔΦ/Δt`, find the current direction with Lenz's law, and explain why a large flux alone induces nothing

## Definition

**Electromagnetic induction** is the production of an emf (and a current) in a circuit by a changing magnetic flux. Faraday's law:

`ε = −N ΔΦ/Δt`

- `N` is the number of turns, `ΔΦ/Δt` is the **rate of change** of the flux, and the minus sign comes from **Lenz's law** (direction)
- **Lenz's law**: the induced current flows so that its own field **opposes** the change in flux that caused it. The textbook: `the current flows in the direction that creates a magnetic field that tries to keep the flux constant in the loop`
- the current follows from Ohm's law: `I = ε/R`
- special case (slider circuit): `ε = Bvℓ`, where `v` is the rod's speed and `ℓ` its length in the field
- the textbook's example: a 16-turn coil of diameter 2.0 cm, `B` falling from 0.020 T to 0.010 T in 34 s, `R = 0.1 Ω`, gives `I = 15 μA`; the slider example gives `I = 25 μA`

> [!IMPORTANT]
> **emf is not a force, and the textbook explains the misleading name.**
>
> It writes `This interpretation turned out to be incorrect; instead, the external source doing the work of moving the magnet adds energy to the charges in the coil.`
> and `The emf may be defined as the rate at which energy is drawn from a source per unit current flowing through a circuit.`
> So emf is the **energy added per unit charge by the source**; voltage is the energy **released** as charge flows through a circuit.
> The textbook therefore avoids the full name and uses only the abbreviation `emf` and the symbol `ε`.

> [!IMPORTANT]
> **Induction depends on "change", not on "size".**
>
> With a magnet resting beside a coil the flux through the coil can be large, yet **no current is induced**:
> `He found that current is induced only when the magnet moves with respect to the coil.`
> Conversely, a weak field changing quickly can produce a sizeable emf. What matters is `ΔΦ/Δt`, not `Φ`.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Magnetic flux](magnetic-flux.en.md) — the numerator of `ΔΦ/Δt`; without the flux concept Faraday's law cannot be written |
| Prerequisite | [Resistance and Ohm's law](resistance-and-ohms-law.en.md) — `I = ε/R` turns the emf into a current; every textbook example passes through this step |
| Follow-up | [Alternating current](alternating-current.en.md) — a coil rotating uniformly in a field has `Φ = BAcosωt`, so the emf varies sinusoidally; generators and transformers attach here |
| Follow-up | [Self-inductance and mutual inductance](self-and-mutual-inductance.en.md) — a coil's own flux changes with its current, giving `ε = −L ΔI/Δt`; coupling between two coils gives `ε₂ = −M ΔI₁/Δt` |
| Follow-up | [Eddy currents and motional emf](eddy-currents-and-motional-emf.en.md) — the slider circuit's `ε = Bvℓ` is developed here into the Lorentz-force explanation and eddy currents; flux cutting is a special case of Faraday's law |
| Recorded gap | **Electromagnetic driving (induction motors, linear motors)**, **quantitative eddy-current loss**, and **transient circuits containing inductance** are not built in this repo; self-inductance, mutual inductance, eddy currents, and motional emf now have their own entries |

## Argument

### K1 · The emf is set by the rate of change of flux (no attack yet)

- **Claim**: the induced emf is proportional to `N` and `ΔΦ/Δt`; a constant flux gives zero emf
- **Premise**: the textbook starts from the experiments (current only while moving, larger when faster, reversed when reversed) and writes `ε ∝ N ΔBcosθ/Δt A`, then introduces the minus sign through Lenz's law to get `ε = −N ΔΦ/Δt`; its example combines `Φ = BAcosθ` with `I = ε/R` to get `15 μA` (ev-161)
- **Reasoning**: the emfs of the `N` turns add in series, hence the factor `N`; `ΔΦ/Δt` is the time rate of change of the flux, which is zero while the magnet is at rest. The minus sign fixes direction only, not magnitude
- **Evidence**: ev-161
- **Attacked**: "only relative motion induces a current" is a **condition of the experiments**, not the statement of the law: a stationary coil with a time-varying field (the textbook's own 16-turn example) also has an induced emf. The derivation first writes a proportionality and then adds the minus sign, whose source is Lenz's law rather than mathematics
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · Lenz's law is energy conservation (no attack yet)

- **Claim**: the induced current always opposes the change in flux, and that opposition conserves energy
- **Premise**: the textbook checks the energy in the slider circuit: the pulling power `P_pull` and the dissipated power `P_dissipated` satisfy `P_pull + P_dissipated = 0`, and it writes `power is conserved in the system consisting of the circuit and the agent that pulls the rod` (ev-161)
- **Reasoning**: if the induced current helped the flux change, the field would do positive work on the moving rod while the circuit heated up — energy from nothing. Lenz's law makes the magnetic force oppose the relative motion, so an external agent must do work, and that work equals the energy dissipated
- **Evidence**: ev-161
- **Attacked**: the textbook's `P_pull + P_dissipated = 0` depends on its own sign convention (`P_pull` carries a minus sign); the physics is that the **magnitudes** are equal, and this entry reads it that way. The textbook does not state "Lenz's law ⇔ energy conservation" as a general theorem; it checks it in the slider example only
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; first node of the 选必二 "electromagnetic induction" chapter, attached after "Magnetic flux" | written after reading m54456 in full (ev-161) | @hpleapfrog |
| 2026-10-21 | Relations: "Alternating current" changed from a gap to a link; the scope condition no longer lists AC generators as unbuilt | batch 12 created alternating current (ev-162) | @hpleapfrog |
| 2026-10-21 | Relations: "Self-inductance and mutual inductance" and "Eddy currents and motional emf" changed from gaps to links; the scope condition updated accordingly | batch 33 created the two entries (ev-192/ev-193) | @hpleapfrog |
