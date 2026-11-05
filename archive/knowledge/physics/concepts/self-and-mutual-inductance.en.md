---
id: kb:physics:self-and-mutual-inductance
type: 知识点
title: "Self-inductance and mutual inductance"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know "Electromagnetic induction" and need to compute the self-induced emf, the mutually induced emf, and the energy stored in an inductor
  条件: covers self-inductance, mutual inductance, the solenoid formula, and the magnetic energy `½LI²` only; RL transients, inductive reactance, series and parallel inductors, magnetic energy density, eddy-current losses, and geometric calculations of mutual inductance are not built (eddy currents and motional emf are a separate entry)
edges:
  先修: ["[Electromagnetic induction](electromagnetic-induction.en.md)"]
  支持: []
  攻击: []
evidence: [ev-192]
license: CC-BY-SA-4.0
---

> **English version of [`自感与互感.md`](自感与互感.md).**

> [!TIP]
> **After reading this entry you should** be able to compute self-induced and mutually induced emfs with `ε = −L ΔI/Δt` and `ε₂ = −M ΔI₁/Δt`, estimate a solenoid's self-inductance with `L = μ0N²A/ℓ`, and explain that an inductor "opposes changes in current" by storing magnetic energy, not by dissipating it

## Definition

**Self-inductance** is Faraday's effect of a device **on itself**: when the current through it changes, the flux it produces changes, and an emf is induced in the same device.

`ε = −L ΔI/Δt`

- `L` is the **self-inductance**, measured in **henries**: `1 H = 1 Ω·s = 1 T·m²/A`
- the minus sign comes from Lenz's law: the induced emf **opposes the change in current**, not the current itself
- for a device of fixed geometry, `L = N ΔΦ/ΔI`; strictly, take the limit `L = N dΦ/dI`
- **solenoid** (cross-sectional area `A`, length `ℓ`, `N` turns): `L = μ0N²A/ℓ`, fixed by geometry and medium alone, independent of the current
- stored energy: `E_ind = ½LI²`, held in the magnetic field

**Mutual inductance** is Faraday's effect of one device **on another**:

`ε₂ = −M ΔI₁/Δt`, `ε₁ = −M ΔI₂/Δt`

- `M` is the **mutual inductance**, the same when the two coils are exchanged (the textbook writes `Nature is symmetric here`)
- a transformer wants a large `M`; **counter-winding** the coils cancels their fields and reduces `M`
- the textbook's example: a solenoid with `N = 200`, diameter `4.00 cm`, length `10.0 cm` has `L = 0.632 mH`; at `30.0 A` it stores `0.284 J`

> [!IMPORTANT]
> **`L` is a geometric quantity, not "bigger current, bigger inductance".**
>
> The numerator of `L = NΔΦ/ΔI` is the **change of flux with current**, not the flux itself. The solenoid formula `L = μ0N²A/ℓ` makes this explicit: once `N`, `A`, and `ℓ` are fixed, `L` is fixed. The textbook notes that `A 1 H inductor is a large inductor` — 1 H is already large in the laboratory, while ordinary coils sit in the μH to mH range.

> [!IMPORTANT]
> **"An inductor opposes changes in current" does not dissipate energy.**
>
> The work done by the source while the current builds up becomes magnetic energy `½LI²`, and the field returns that energy when the current falls. This is essentially different from resistance: a resistor turns electric energy into heat, while an inductor only **stores it temporarily**. The textbook's example of switching off 10 A through a 1 H inductor in 1.0 ms gives `ε = 1.0×10 A / 1.0 ms = 1.0×10⁴ V`, enough to arc and damage switchgear. A camera flash uses the same effect in reverse, switching rapidly to boost a battery to over a thousand volts and charge a capacitor.

> [!NOTE]
> **Three source problems and how this entry handles them.**
>
> 1. **The Section Summary and glossary define `inductance` as "how efficiently a device induces an emf in another device"** — that describes mutual inductance; the body defines self-inductance separately. This entry follows the body and keeps the two distinct.
> 2. **The sign in the 1 H example**: the textbook first computes `10,000 V` as a magnitude and then says "the positive sign means this voltage is in the same direction as the current, opposing its decrease". The formula carries a minus sign; this entry uses `L|ΔI/Δt|` as the magnitude and leaves direction to Lenz's law.
> 3. **The formulas use finite differences `ΔI/Δt`**: this equals the derivative only when the current changes linearly. The textbook is algebraic and does not treat nonlinear inductors.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Electromagnetic induction](electromagnetic-induction.en.md) — `ε = −NΔΦ/Δt` and Lenz's law are the whole source of self- and mutual inductance; self-inductance only replaces "the circuit" with "the device itself" |
| Related | [Transformer](transformer.en.md) — the coupling between a transformer's primary and secondary is mutual inductance; the ideal transformer ignores leakage and core losses, and this entry does not repeat its voltage ratio |
| Related | [Alternating current](alternating-current.en.md) — an inductor presents inductive reactance in an AC circuit, which is not built here; this entry covers only the instantaneous emf and stored energy when the current changes |
| Recorded gap | **RL transients**, **inductive reactance `X_L = ωL`**, **series and parallel inductors**, **magnetic energy density `u = B²/(2μ0)`**, **geometric calculations of mutual inductance**, and **core saturation and eddy-current losses** are not built in this repo |

## Argument

### K1 · Self-inductance is Lenz's law acting on the device itself (no attack yet)

- **Claim**: when the current changes, the device induces an emf in itself that opposes the change; `ε = −L ΔI/Δt`
- **Premise**: the textbook starts from Faraday's law `ε = −NΔΦ/Δt`, notes that for a fixed geometry the flux changes entirely because the current changes, replaces `ΔΦ` by `ΔI`, defines `L = NΔΦ/ΔI`, and obtains `ε = −L ΔI/Δt` (ev-192)
- **Reasoning**: as the current grows the field strengthens, and the induced emf acts against the increase; as the current falls the induced emf keeps the original direction and opposes the decrease. Both cases are direct consequences of Lenz's law
- **Evidence**: ev-192
- **Attacked**: the textbook's anthropomorphic `opposition` is easily read as resistance-like blocking. The TIP states that an inductor's opposition comes from the time needed to store and release energy, not from dissipation; the textbook gives `½LI²` with only `It can be shown`, not a derivation
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · Mutual inductance is a symmetric coupling fixed by geometry and medium (no attack yet)

- **Claim**: a changing current in coil 1 induces `ε₂ = −M ΔI₁/Δt` in coil 2; exchanging the coils leaves `M` unchanged
- **Premise**: the textbook defines `M`, writes `emf2 = −M ΔI1/Δt` and `emf1 = −M ΔI2/Δt`, and says `Nature is symmetric here`; counter-winding cancels the fields and reduces `M` (ev-192)
- **Reasoning**: `M` measures how strongly the two coils are coupled magnetically; the stronger the coupling, the larger the emf induced by the same `ΔI₁/Δt`. A transformer wants a large `M`, whereas a dangerous `M` between an appliance's coils and its case is reduced by counter-winding
- **Evidence**: ev-192
- **Attacked**: the textbook **only asserts** the symmetry and does not prove it; reciprocity requires linear media and negligible losses, which the transformer discussion assumes. The textbook also gives no geometric formula for `M`, only the concept and the unit
- **Attribution**: @hpleapfrog · 2026-10-21

### K3 · Magnetic energy `½LI²` and switching overvoltage (no attack yet)

- **Claim**: an inductor stores `½LI²`; interrupting the current abruptly produces a very large induced emf
- **Premise**: the textbook gives `E_ind = ½LI²` and computes the interruption of 10 A through a 1 H inductor in 1.0 ms as about `10,000 V`; its solenoid example with `0.632 mH` at `30.0 A` gives `0.284 J` (ev-192)
- **Reasoning**: the magnetic energy in an inductor can only be established or released through a current. When the current is forced to zero quickly, `ΔI/Δt` is large, and so is `L|ΔI/Δt|`. The energy does not disappear; it leaves as an arc or spark across the switch contacts
- **Evidence**: ev-192
- **Attacked**: the textbook treats the energy formula as known and does not derive it from `∫εI dt`. A real inductor also has winding resistance; `½LI²` is the magnetic energy alone and excludes Joule heat, which the textbook's examples neglect
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; new node in the 选必二 "electromagnetic induction" chapter, attached after "Electromagnetic induction" | written after reading m42420 in full (ev-192) | @hpleapfrog |
