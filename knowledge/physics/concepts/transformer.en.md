---
id: kb:physics:transformer
type: 知识点
title: "Transformer"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done "Electromagnetic induction" and "Alternating current" and need to understand why a transformer needs AC and how to use the turns ratio
  条件: covers the construction, principle, and voltage ratio of the ideal transformer only; the power/current relations, leakage flux, core losses, and eddy-current losses are not built (self- and mutual inductance are a separate entry); power transmission is a separate entry
edges:
  先修: ["[Electromagnetic induction](electromagnetic-induction.en.md)", "[Alternating current](alternating-current.en.md)"]
  支持: []
  攻击: []
evidence: [ev-162]
license: CC-BY-SA-4.0
---

> **English version of [`变压器.md`](变压器.md).**

> [!TIP]
> **After reading this entry you should** be able to explain why a transformer needs a time-varying flux, compute step-up and step-down voltages with `V_S/V_P = N_S/N_P`, and tell which assumptions are idealisations

## Definition

A **transformer** changes one voltage into another. The textbook's glossary: `device that transforms voltages from one value to another`.

- **Construction**: two coils wound on a ferromagnetic core, called the **primary** and **secondary** coils; the input is applied to the primary and the output is taken from the secondary
- **The core**: the textbook says it **traps** the field created by the primary and its magnetisation **increases** the field strength, analogous to how a dielectric increases the electric field in a capacitor
- **Principle**: with AC on the primary, a time-varying magnetic flux is set up in the core, passes through the secondary, and induces an emf. The textbook: `Since the input voltage is AC, a time-varying magnetic flux is sent through the secondary coil, inducing an AC output voltage.`
- **Transformer equation** (textbook equation 3.07): `V_S/V_P = N_S/N_P`
- **Step-up**: `N_S > N_P`; **step-down**: `N_S < N_P`. The textbook's exercise: with 12 turns on the primary, 6 turns on the secondary give half the input voltage
- the textbook says **voltage** rather than emf: `the term voltage is used rather than emf because transformers have internal resistance`

> [!IMPORTANT]
> **The transformer equation is derived under idealised assumptions.**
>
> The textbook first writes `V_S = −N_S ΔΦ/Δt` for the secondary and `V_P = −N_P ΔΦ/Δt` for the primary, then assumes the **cross-sectional areas are the same and so is the magnetic field strength**, so `ΔΦ/Δt` is the same on both sides; it also assumes the coil resistance is small enough that `V_S = ε_S`. Dividing the two equations gives `V_S/V_P = N_S/N_P`. Leakage flux, core losses, and coil resistance are not in this equation.

> [!IMPORTANT]
> **This module gives no power or current relation.**
>
> The textbook uses `P = IV` only when discussing transmission; it never writes `P_P = P_S` or `I_S/I_P = N_P/N_S`. Those are standard corollaries in Chinese textbooks, but **this entry does not add them** — this module contains no evidence for them.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Electromagnetic induction](electromagnetic-induction.en.md) — the secondary emf comes straight from `ε = −NΔΦ/Δt`; without Faraday's law there is no transformer equation |
| Prerequisite | [Alternating current](alternating-current.en.md) — a transformer needs a **changing** flux; a constant current gives a constant flux and no sustained output |
| Related | [Self-inductance and mutual inductance](self-and-mutual-inductance.en.md) — the coupling between primary and secondary is mutual inductance, `ε₂ = −M ΔI₁/Δt`; the ideal transformer assumes strong coupling and negligible leakage |
| Follow-up | [Power transmission](power-transmission.en.md) — step-up and step-down transformers are the two ends of the transmission chain |
| Recorded gap | **Power and current relations**, **leakage flux, core losses, eddy-current losses, and core saturation** are not built in this repo; self- and mutual inductance now have their own entry |

## Argument

### K1 · The transformer equation comes from dividing two equations (no attack yet)

- **Claim**: under the idealised assumptions, the secondary-to-primary voltage ratio equals the turns ratio, `V_S/V_P = N_S/N_P`
- **Premise**: the textbook writes `V_S = −N_S ΔΦ/Δt` and `V_P = −N_P ΔΦ/Δt`, states that `ΔΦ/Δt` is the same on both sides and that the coil resistance is small enough that `V_S = ε_S`, and divides the two equations to obtain equation 3.07 (ev-162)
- **Reasoning**: one core makes both coils share the flux, so each turn has the same induced emf; the voltage is proportional to the number of turns, and the unknown `ΔΦ/Δt` cancels in the ratio. Step-up and step-down differ only in which coil has more turns
- **Evidence**: ev-162
- **Attacked**: "the cross-sectional area and magnetic field strength are the same on each side" is an **idealisation**; real transformers have leakage and losses, so the equation is approximate, and the textbook gives no experimental check. The text is also inconsistent: it first says it uses "voltage" because transformers **have internal resistance**, then assumes the coil resistance is **small enough** that `V_S = ε_S`. This entry uses the equation in the small-resistance idealisation and records the inconsistency here
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · A transformer works only with a changing flux (no attack yet)

- **Claim**: sustained output from the secondary requires a time-varying flux in the primary; steady direct current produces no sustained secondary voltage
- **Premise**: the textbook writes `Since the input voltage is AC, a time-varying magnetic flux is sent through the secondary coil, inducing an AC output voltage`, and builds the entire derivation on `ΔΦ/Δt` (ev-162)
- **Reasoning**: the numerator in Faraday's law is a **rate of change**; a constant current gives a constant flux, `ΔΦ/Δt = 0`, and no secondary emf. That is also why every application in the textbook is on an AC supply
- **Evidence**: ev-162
- **Attacked**: the textbook only states that the input is AC and **does not analyse a DC input**; "no output on DC" is a direct consequence of Faraday's law, not the textbook's wording. Strictly, at the instant a DC supply is switched on or off the flux is still changing, so the secondary sees a brief emf — the textbook does not discuss this transient, and this entry records it only as a boundary case, not as an exam point
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; second node of the 选必二 chapter 3 "alternating current", attached after "Alternating current" | written after reading m54467 in full (ev-162) | @hpleapfrog |
| 2026-10-21 | Added a Related link to "Self-inductance and mutual inductance"; removed self- and mutual inductance from the gap table and added eddy-current losses; updated the scope condition | batch 33 created self- and mutual inductance (ev-192) | @hpleapfrog |
