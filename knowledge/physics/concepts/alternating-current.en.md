---
id: kb:physics:alternating-current
type: 知识点
title: "Alternating current"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done "Electromagnetic induction" and "Uniform circular motion" and need to understand why a generator produces a sinusoidal AC emf
  条件: covers the generation of sinusoidal AC, peak value, period and frequency only; RMS values and the effect of inductors and capacitors on AC are handled by other entries, and three-phase power is not built
edges:
  先修: ["[Electromagnetic induction](electromagnetic-induction.en.md)", "[Uniform circular motion](uniform-circular-motion.en.md)"]
  支持: []
  攻击: []
evidence: [ev-162]
license: CC-BY-SA-4.0
---

> **English version of [`交变电流.md`](交变电流.md).**

> [!TIP]
> **After reading this entry you should** be able to write `ε = NABω sin ωt` for a rotating coil, explain where the peak `ε₀ = NABω` comes from, and explain why 60 Hz AC makes a bulb switch at 120 Hz

## Definition

**Alternating current** is a current whose magnitude and direction vary periodically with time. The textbook does not give a formal definition in this module: it describes the `AC voltage` and `AC current` produced by a generator and writes the emf as swinging between a positive and a negative peak. The opening sentence above is this repo's paraphrase. The textbook's defining contrast is between three energy-conversion devices:

| Device | Energy conversion | Textbook wording |
|---|---|---|
| Electric motor | electrical → mechanical | `convert electrical energy into mechanical energy` |
| Generator | mechanical → electrical | `converts mechanical energy into electrical energy` |
| Transformer | voltage → voltage | `transforms voltages from one value to another` |

- **Generator**: a coil rotates at constant angular velocity `ω` in a uniform field, giving `ε = NABω sin ωt`
- **Peak value**: `ε₀ = NABω`; the instantaneous emf swings between `+ε₀` and `−ε₀`
- **Period and frequency**: `T = 2π/ω = 1/f`; in the United States the AC frequency is 60 Hz
- the emf crosses zero twice per cycle, so a bulb on the generator switches on and off at `2f` (120 Hz in the United States)
- the device runs in reverse too: mechanically driving the motor's shaft makes a generator — the textbook writes `run the motor in reverse`

> [!IMPORTANT]
> **Every factor in `ε₀ = NABω` has a history; it is not a formula to memorise.**
>
> The textbook starts from the motional emf `ε = Bℓv`: the forces on the top and bottom segments are perpendicular to the wire and drive no current, so only the two side segments contribute. The side velocity makes an angle `θ = ωt` with the field, its perpendicular component is `v sinθ`, and the two sides add in the same direction, giving `ε = 2Bℓv sinωt`. Then `v = (w/2)ω` and `A = ℓw` turn `2Bℓ(w/2)ω` into `BAω`, and the factor `N` comes from the turns in series. So `ω` comes from the rotation, `A` from the loop area, and `N` from the series connection.

> [!IMPORTANT]
> **The RMS value is not in this module, but it now has its own entry.**
>
> The textbook gives only the peak `ε₀`, the instantaneous value `ε = ε₀ sinωt`, and the period and frequency. The "description of alternating current" — RMS and average values — is built separately in [RMS values](rms-values.en.md): everyday 220 V/120 V means rms, and the peak is `√2` times larger. This entry covers generation and peak value only.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Electromagnetic induction](electromagnetic-induction.en.md) — a generator's emf is ultimately a changing flux; the textbook starts from `ε = Bℓv`, another entrance to Faraday's law |
| Prerequisite | [Uniform circular motion](uniform-circular-motion.en.md) — `ω`, `v = rω`, and `T = 2π/ω` are the tools used to derive `ε = NABω sinωt` |
| Follow-up | [RMS values](rms-values.en.md) — a sinusoid is converted to an equivalent DC value by "square—mean—root"; `I_rms = I0/√2`, `P_ave = I_rms V_rms`, and peak power are there |
| Follow-up | [Reactance and impedance](reactance-and-impedance.en.md) — `X_L = 2πfL` and `X_C = 1/(2πfC)` connect directly to this entry's frequency `f`; phase difference, series RLC, and resonance are there |
| Follow-up | [Transformer](transformer.en.md) — a transformer needs a time-varying flux; without alternating current there is no changing `Φ` |
| Recorded gap | **Three-phase power** is not built (the available CC BY textbooks have no corresponding module); RMS values and the effect of inductors and capacitors are handled by the entries above |

## Argument

### K1 · Uniform rotation produces a sinusoidal emf (no attack yet)

- **Claim**: a coil rotating uniformly in a uniform field has `ε = NABω sinωt`, with peak `ε₀ = NABω`
- **Premise**: the textbook writes `ε = Bℓv`, `ε = 2Bℓv sinθ`, `θ = ωt`, `v = (w/2)ω`, reaches `ε = Bℓwω sinωt`, multiplies by `N` to get `ε = NABω sinωt`, and writes `ε₀ = NABω` as the maximum (peak) emf (ev-162)
- **Reasoning**: the side segments' velocity direction turns with the coil, so only the component `v sinωt` perpendicular to the field contributes; the two sides add because their emfs point the same way; `v = (w/2)ω` converts linear speed to angular velocity. A flux check: `Φ = BA cosωt`, so `|ε| = N|ΔΦ/Δt| = NABω sinωt`, matching the textbook's result (this step is the repo's, see "Attacked")
- **Evidence**: ev-162
- **Attacked**: the textbook derives the result from motional emf only and **never differentiates `Φ = BAcosωt`**; "the two routes agree" is this repo's check, not the textbook's argument. The derivation also assumes constant `ω`; the textbook does not discuss accelerated rotation, where the emf is no longer just `NABω sinωt`
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · The bulb switches at twice the frequency (no attack yet)

- **Claim**: an alternating emf crosses zero twice per cycle, so a bulb switches at `2f`; 60 Hz AC in the United States means 120 Hz
- **Premise**: the textbook writes `the light bulb actually flickers on and off at a frequency of 2f, because there are two zero crossings per period`, and `In the United States, the frequency of alternating current is 60 Hz, so the lights flicker on and off at a frequency of 120 Hz` (ev-162)
- **Reasoning**: `ε = ε₀ sinωt` is zero twice per period (`ωt = 0, π`), so the instantaneous power is also zero; the brightness modulation therefore has fundamental frequency `2f`, not `f`. The textbook gives two reasons the flicker is not seen: it is faster than the eye, and different bulbs smooth the light output
- **Evidence**: ev-162
- **Attacked**: the textbook says "faster than the refresh rate of the human eye" without giving a number or a source; the same passage gives a second reason (bulbs smoothing the output), so the conclusion does not depend on the first. This entry does not treat "the eye's refresh rate" as a quantitative basis
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; first node of the 选必二 chapter 3 "alternating current", attached after "Electromagnetic induction" | written after reading m54467 in full (ev-162) | @hpleapfrog |
| 2026-10-21 | Added follow-up nodes "RMS values" and "Reactance and impedance"; the old "RMS is not answered here" note now points to the new entries, and the only remaining gap is three-phase power | backfilled after reading ev-194 / ev-195 | @hpleapfrog |
