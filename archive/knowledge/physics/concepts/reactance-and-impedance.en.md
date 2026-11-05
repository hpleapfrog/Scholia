---
id: kb:physics:reactance-and-impedance
type: 知识点
title: "Reactance and impedance"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done "Alternating current", "RMS values", "Self-inductance and mutual inductance", and "Capacitance" and need to explain why inductors and capacitors oppose AC and to analyse a series RLC circuit
  条件: covers the phase relations and reactances of a pure inductor, capacitor, and resistor, plus series RLC impedance, resonance, and power factor only; parallel AC networks, complex impedance and phasors, quality factor and bandwidth, non-sinusoidal AC, three-phase power, and parasitic elements of real components are not built
edges:
  先修: ["[Alternating current](alternating-current.en.md)", "[RMS values](rms-values.en.md)", "[Self-inductance and mutual inductance](self-and-mutual-inductance.en.md)", "[Capacitance](capacitance.en.md)"]
  支持: []
  攻击: []
evidence: [ev-195]
license: CC-BY-SA-4.0
---

> **English version of [`感抗与容抗.md`](感抗与容抗.md).**

> [!TIP]
> **After reading this entry you should** be able to compute `X_L = 2πfL` and `X_C = 1/(2πfC)`, explain that voltage leads current by 90° across an inductor and lags by 90° across a capacitor, and analyse a series RLC circuit with `Z = √(R² + (X_L − X_C)²)`, `f0 = 1/(2π√(LC))`, and `cosφ = R/Z`

## Definition

A resistor, an inductor, and a capacitor behave very differently on the same sinusoidal source:

| Element | Phase of voltage and current | Opposition to AC | As frequency rises |
|---|---|---|---|
| Resistor `R` | in phase (0°) | `R`, independent of frequency | unchanged |
| Inductor `L` | voltage leads current by 90° (1/4 cycle) | inductive reactance `X_L = 2πfL` | increases |
| Capacitor `C` | voltage lags current by 90° (1/4 cycle) | capacitive reactance `X_C = 1/(2πfC)` | decreases |

**Inductive reactance** and **capacitive reactance** are both measured in ohms. For a pure inductor or capacitor the AC Ohm's law is

`I_rms = V_rms/X_L`, `I_rms = V_rms/X_C`

where `V_rms` is the rms voltage across the element. The textbook's qualitative reason: an inductor opposes changes in current through `V = −L(ΔI/Δt)`, so the faster the current changes, the greater the opposition; a capacitor stops current when fully charged, and at higher frequency there is less time to charge it, so it impedes less.

In a **series RLC circuit** the same current flows through all three elements, but the voltages are out of phase and cannot simply be added. The textbook gives

`V0 = √(V0R² + (V0L − V0C)²)`

Substituting `V0R = I0R`, `V0L = I0X_L`, and `V0C = I0X_C` gives the **impedance**

`Z = √(R² + (X_L − X_C)²)`

and `I0 = V0/Z`, `I_rms = V_rms/Z`. The phase angle satisfies

`cosφ = R/Z`

and the average power is

`P_ave = I_rms V_rms cosφ`

`cosφ` is the **power factor**. When `X_L = X_C` the two cancel, `Z = R` is minimum, and the current is maximum; this frequency is the **resonant frequency**:

`f0 = 1/(2π√(LC))`

The textbook's example (`R = 40.0 Ω`, `L = 3.00 mH`, `C = 5.00 μF`, `V_rms = 120 V`):

- 60 Hz: `X_L = 1.13 Ω`, `X_C = 531 Ω`, `Z = 531 Ω`, `I_rms = 0.226 A`
- 10 kHz: `X_L = 188 Ω`, `X_C = 3.18 Ω`, `Z = 190 Ω`, `I_rms = 0.633 A`
- resonance: `f0 = 1.30 kHz`, `Z = R = 40.0 Ω`, `I_rms = 3.00 A`
- 60 Hz: `cosφ = 0.0753`, `φ = 85.7°`, `P_ave = 2.04 W`; at resonance `P_ave = 360 W`

At low frequency the capacitive reactance dominates; at high frequency the inductive reactance dominates. The textbook uses this to explain filtering: a series inductor blocks high frequencies, a series capacitor blocks low frequencies.

> [!IMPORTANT]
> **Reactance is not resistance.**
>
> The textbook calls `X_L` and `X_C` an `effective resistance`, but that is only a metaphor for "opposition to current". A resistor turns electric energy into heat; a reactance only stores energy back and forth between the electric and magnetic fields: an inductor stores `½LI²`, a capacitor stores `½CV²`, and an ideal reactance dissipates no power. So `I_rms = V_rms/X` looks like Ohm's law, but `P_ave` cannot be written as `I_rms²X`: in an RLC circuit the average power is dissipated by `R` alone and equals `I_rms²R`.

> [!IMPORTANT]
> **The sign of the phase difference must be judged separately; the textbook gives only `cosφ`.**
>
> `cosφ = R/Z` gives only the magnitude of the phase difference and cannot distinguish current leading from current lagging. This library supplies the criterion: when `X_C > X_L` the circuit is capacitive and current leads voltage; when `X_L > X_C` it is inductive and current lags voltage; when they are equal the circuit is resonant and in phase. In the textbook's 60 Hz example `X_C` is far larger than `X_L`, so the circuit is capacitive and current leads; the 10 kHz example is the opposite. The textbook states only that voltage leads across an inductor and lags across a capacitor.

> [!NOTE]
> **Five source problems and how this entry handles them.**
>
> 1. **The `effective resistance` phrase** conflates a non-dissipating reactance with a resistor; this entry calls it reactance and states that it dissipates no average power.
> 2. **The explanation that `X_L` is proportional to frequency** is written as "large f means small Δt and large ΔI/Δt", conflating frequency with rate of change; the exact relation comes from `V = L dI/dt`, as derived in K1.
> 3. **An m42431 exercise states `f = 7.50 Hz`**, but its answers `cosφ = 0.159`, `φ = 80.9°` correspond to about 1.0 kHz (at 7.50 Hz `cosφ ≈ 1.18×10⁻³`; at 7.50 kHz `cosφ ≈ 0.765`); its (c) `26.4 W` is the apparent power `V_rms²/Z`, whereas `P_ave = I_rms²R` gives about `4.2 W`. This entry does not use that answer set.
> 4. **The glossary defines power factor as "the amount by which the power ... is less"**, turning a ratio into an amount; the power factor is `cosφ`, between 0 and 1 and dimensionless.
> 5. **"At very high frequencies a capacitor acts like a simple wire" is too strong**: an ideal capacitor has `X_C → 0`, but a real component has lead inductance and equivalent series resistance; "an efficient motor needs a power factor near 1" also falls outside a series RLC circuit. This entry keeps the latter only as an application of power factor and does not develop a motor model.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Alternating current](alternating-current.en.md) — a sinusoidal source, frequency, and phase are the premises of reactance; without periodic change an inductor has no sustained back emf and a capacitor charges only once |
| Prerequisite | [RMS values](rms-values.en.md) — `I_rms = V_rms/X` and `P_ave = I_rms V_rms cosφ` are built on rms values; peak-rms conversion is there |
| Prerequisite | [Self-inductance and mutual inductance](self-and-mutual-inductance.en.md) — `V = −L ΔI/Δt` is the microscopic origin of inductive reactance; `L` is set by geometry, while `X_L` also depends on frequency |
| Prerequisite | [Capacitance](capacitance.en.md) — `Q = CV` and `I = ΔQ/Δt` are the origin of capacitive reactance; `X_C` falls with frequency because the charging time is shorter |
| Related | [Damped and forced oscillation](damped-and-forced-oscillation.en.md) — RLC resonance and forced mechanical resonance are the same kind of phenomenon: the response peaks when the driving frequency approaches the natural frequency, and resistance acts as damping; m42431 explicitly uses a car shock absorber as an analogy |
| Recorded gap | **parallel and general AC networks**, **complex impedance and phasors**, **quality factor `Q`, passband and half-width**, **impedance of non-sinusoidal AC**, **three-phase power**, **parasitic elements and self-resonance of real inductors and capacitors**, **power-factor correction and motor equivalent circuits** are not built |

## Argument

### K1 · Reactance comes from the calculus relation between voltage and current (no attack yet)

- **Claim**: across an inductor voltage leads current by 90° and `X_L = ωL`; across a capacitor voltage lags current by 90° and `X_C = 1/(ωC)`
- **Premise**: the textbook gives `V_L = −L(ΔI/Δt)`, `V_C = Q/C`, and `I = ΔQ/Δt`, and says `X_L = 2πfL` and `X_C = 1/(2πfC)` follow from Kirchhoff's rules and calculus, but does not write the derivation (ev-195); the derivation is supplied by this library
- **Reasoning**: let the inductor voltage be `V = V0 cosωt`. From `V = L dI/dt`, `dI/dt = (V0/L)cosωt`, so `I = (V0/(ωL)) sinωt = I0 cos(ωt − 90°)`; current lags voltage by 90° and the amplitude ratio is `V0/I0 = ωL`. Let the capacitor voltage be `V = V0 cosωt`. From `I = C dV/dt`, `I = −ωCV0 sinωt = I0 cos(ωt + 90°)`; current leads voltage by 90° and the amplitude ratio is `V0/I0 = 1/(ωC)`
- **Evidence**: ev-195
- **Attacked by**: the textbook does not derive the result and treats the calculus result as known; what this entry supplies is the **steady-state sinusoidal solution**, without the switching transient (which needs initial conditions and the general solution of a differential equation and is not built here). The derivation also uses derivatives, while high-school textbooks usually require only the result and the qualitative reason
- **Author**: @hpleapfrog · 2026-10-21

### K2 · The impedance of a series RLC circuit is the Pythagorean sum of resistance and net reactance (no attack yet)

- **Claim**: `Z = √(R² + (X_L − X_C)²)`; at resonance `X_L = X_C`, `Z = R`, the current is maximum, and `f0 = 1/(2π√(LC))`
- **Premise**: the textbook obtains `Z` from `V0² = V0R² + (V0L − V0C)²` with `V0R = I0R`, `V0L = I0X_L`, and `V0C = I0X_C`, then solves `X_L = X_C` for `f0` (ev-195)
- **Reasoning**: the series current is common; the voltage across `R` is in phase with it, the voltage across `L` leads by 90°, and the voltage across `C` lags by 90°. The last two point in opposite directions, so they subtract first and then combine at a right angle with the in-phase voltage across `R` — hence the Pythagorean sum. At resonance `X_L = X_C`, the two reactance voltages are equal and opposite and cancel completely, leaving only `R`; then `I_rms = V_rms/R` is maximum. Solving `2πf0L = 1/(2πf0C)` gives `f0`
- **Evidence**: ev-195
- **Attacked by**: the textbook gives only the result and never draws a phasor diagram or explains "subtract first, then Pythagorean sum"; this entry supplies that geometric argument. At resonance the voltages across the inductor and capacitor can each exceed the source voltage (equal in magnitude, opposite in direction); the textbook does not discuss the quality factor `Q`, which is recorded as a gap
- **Author**: @hpleapfrog · 2026-10-21

### K3 · Average power is set by the resistance, and the power factor corrects for the phase difference (no attack yet)

- **Claim**: in a series RLC circuit `P_ave = I_rms V_rms cosφ = I_rms²R`; only the resistance dissipates energy, while the inductor and capacitor only exchange it
- **Premise**: the textbook writes `cosφ = R/Z` and `P_ave = I_rmsV_rms cosφ`, stresses that the inductor and capacitor have energy input and output but do not dissipate it and that the resistor dissipates exactly what the source supplies, and gives `P_ave = 2.04 W` at 60 Hz and `360 W` at resonance (ev-195)
- **Reasoning**: `I_rmsV_rms cosφ = I_rmsV_rms(R/Z) = I_rms(V_rms/Z)R = I_rms²R`, so the average power equals the Joule heating in the resistance. The larger the phase difference, the smaller `cosφ`, and the smaller the fraction of `I_rmsV_rms` that is actually dissipated; at resonance `φ = 0`, `cosφ = 1`, and the average power is maximum
- **Evidence**: ev-195
- **Attacked by**: the textbook uses "a power factor near 1 is good for an efficient motor" as an example, but a motor is not a series RLC circuit and `cosφ = R/Z` cannot be applied directly; this entry keeps only "average power is set by R and the phase difference lowers the power factor" and does not treat a motor model as built. Also, `cosφ` gives only the magnitude; the leading/lagging criterion is in the IMPORTANT callout above
- **Author**: @hpleapfrog · 2026-10-21

## Changelog

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-21 | Created; fills the node on the effect of inductors and capacitors on AC and on series RLC in elective-2 chapter 3 "Alternating current", after "RMS values" | Written after reading m42427 and m42431 in full (ev-195); the calculus derivations of `X_L` and `X_C`, the phase-sign criterion, and the phasor explanation are library additions | @hpleapfrog |
