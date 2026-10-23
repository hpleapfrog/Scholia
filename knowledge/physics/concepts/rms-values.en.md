---
id: kb:physics:rms-values
type: 知识点
title: "RMS values"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done "Alternating current" and need to understand that mains 220 V/120 V means rms, and to compute average AC power and peak values
  条件: covers rms and peak values of sinusoidal AC and average power in a pure-resistance circuit only; rms of non-sinusoidal waveforms, true-rms measurement, power factor, and three-phase power are not built (power factor and impedance are handled by "Reactance and impedance")
edges:
  先修: ["[Alternating current](alternating-current.en.md)"]
  支持: []
  攻击: []
evidence: [ev-194]
license: CC-BY-SA-4.0
---

> **English version of [`有效值.md`](有效值.md).**

> [!TIP]
> **After reading this entry you should** be able to convert between peak and rms with `I_rms = I0/√2` and `V_rms = V0/√2`, explain why `P_ave = I_rms V_rms = I_rms²R = V_rms²/R` has the same form as the DC formulas, and explain why the ordinary average cannot replace the rms value

## Definition

The **root mean square (rms)** value of a periodically varying current or voltage is the DC value that would produce the same heating effect. The textbook defines it as: square the quantity, average over one period, then take the square root. For sinusoidal AC:

`I_rms = I0/√2 ≈ 0.707 I0`, `V_rms = V0/√2 ≈ 0.707 V0`

where `I0` and `V0` are the peak values. The textbook writes the instantaneous values `V = V0 sin 2πft` and `I = I0 sin 2πft`, in phase in a pure resistor; the instantaneous power is `P = I0V0 sin² 2πft` and the average power is

`P_ave = ½ I0 V0`

Substituting `I0 = √2 I_rms` and `V0 = √2 V_rms` gives the three DC-shaped formulas:

- `P_ave = I_rms V_rms`
- `P_ave = I_rms² R`
- `P_ave = V_rms²/R`
- the AC Ohm's law for a pure resistor: `I_rms = V_rms/R`

Everyday ratings are rms: the textbook writes `most household electricity is 120 V AC, which means that V_rms is 120 V`, a 10 A breaker limits `I_rms`, and a 1.0 kW microwave is rated by `P_ave`. Since `V0 = √2 V_rms`, the peak of 120 V mains is

`V0 = 1.414 × 120 V = 170 V`

For a pure resistor the peak and average powers are related by

`P0 = I0 V0 = 2 P_ave`

so a 60.0 W bulb swings between 0 and 120 W at `2f`, while its average remains 60.0 W.

Orders of magnitude: a 25 W, 120 V bulb has hot resistance `R = V_rms²/P_ave = 576 Ω`, `I_rms = 0.208 A`, `I0 = 0.294 A`, and `P0 = 50 W`; 60 Hz has period `T = 1/f = 16.7 ms`, the voltage crosses zero twice per cycle, and the bulb flickers at 120 Hz (covered by "Alternating current").

> [!IMPORTANT]
> **"Average" and "rms" are not the same thing.**
>
> The textbook writes `average or rms current`, yet in the same passage says the average of a sinusoid is zero — if it were truly the average, an ammeter would read zero. The rms value follows "square → average → square root", not a direct average. The full-wave rectified sine has average `2V0/π ≈ 0.637 V0`, still not `0.707 V0`: one is a DC component, the other a heating-equivalent value. This library uses `rms` in the latter sense.

> [!IMPORTANT]
> **`√2` is a result for sinusoids, not the definition of rms.**
>
> The textbook gives `I_rms = I0/√2` without derivation. This library supplies it in K1: the average of `sin²ωt` over one period is `½`, so the root-mean-square is `1/√2`. For a square wave the rms equals the peak; for a triangle wave it is `V0/√3`. Treating `√2` as the definition will give wrong answers for non-sinusoidal waveforms.

> [!NOTE]
> **Four source problems and how this entry handles them.**
>
> 1. **`average` and `rms` are conflated**: see the IMPORTANT callout above; this entry uses rms only.
> 2. **No derivation of `√2`**: K1 supplies the mean-square derivation and marks it as a library addition.
> 3. **"AC shocks are often more harmful than similar DC shocks" is uncited**: the textbook states it in a historical passage without an experiment or standard; this entry does not adopt it as a quantitative conclusion.
> 4. **120 V is treated as exact**: the textbook uses it in the `√2` conversion, but mains has a voltage tolerance; the numbers here reproduce textbook examples only and are not claimed as guaranteed grid values.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Alternating current](alternating-current.en.md) — the sinusoidal emf `ε = ε0 sinωt`, peak `ε0 = NABω`, and period/frequency `T = 1/f` are the starting point; that entry explicitly leaves rms as a gap, which this entry fills |
| Follow-up | [Reactance and impedance](reactance-and-impedance.en.md) — `X_L = 2πfL`, `X_C = 1/(2πfC)`, and `I_rms = V_rms/X` all use rms; phase difference and power factor `cosφ` are there |
| Related | [Electric power](electric-power.en.md) — the DC formulas `P = IV = I²R = V²/R` have the same form in AC, with rms values substituted; the gap "AC rms and power factor" in that entry is filled by this entry and "Reactance and impedance" |
| Related | [Power transmission](power-transmission.en.md) — transmission calculations use `P_ave = I_rms V_rms` and `P_loss = I_rms²R_wire`; higher voltage lowers current and lowers line loss by the current squared |
| Recorded gap | **rms and crest factor of non-sinusoidal waveforms (square, triangle, PWM)**, **true-rms (TRMS) meter bandwidth and form factor**, **three-phase power**, **separation of active and reactive power** are not built |

## Argument

### K1 · The rms value is the DC value with the same heating effect (no attack yet)

- **Claim**: for a sinusoidal current `I_rms = I0/√2`; in a resistor it produces the same average power as a DC current of that size
- **Premise**: the textbook defines rms as "square, mean, square root" and gives `P_ave = ½I0V0`, `I_rms = I0/√2`, `V_rms = V0/√2` (ev-194); the derivation is supplied by this library
- **Reasoning**: over one period a resistor dissipates `W = ∫I0²R sin²ωt dt = I0²R·T/2`. A DC current `I_rms` dissipating the same energy in the same resistor and time satisfies `I_rms²R·T = I0²R·T/2`, hence `I_rms = I0/√2`. Equivalently, the mean of `sin²ωt` over a period is `½`, so its root-mean-square is `1/√2`. The same holds for voltage
- **Evidence**: ev-194
- **Attacked by**: the textbook does not derive it and does not say that `√2` holds only for sinusoids; this entry puts "sinusoids only" in the TIP and K1. Non-sinusoidal waveforms must return to the "square—mean—root" definition; `√2` cannot be applied
- **Author**: @hpleapfrog · 2026-10-21

### K2 · Average power written with rms has the same form as the DC formulas (no attack yet)

- **Claim**: in a pure-resistance AC circuit `P_ave = I_rms V_rms = I_rms²R = V_rms²/R`; peak power is twice the average
- **Premise**: the textbook derives `P_ave = ½I0V0` from `P = I0V0 sin²2πft`, substitutes the rms definitions to get the three formulas, and gives a 60 W bulb's peak power `P0 = 2P_ave = 120 W` (ev-194)
- **Reasoning**: `I0V0 = (√2I_rms)(√2V_rms) = 2I_rmsV_rms`, so `½I0V0 = I_rmsV_rms`; the peak power `P0 = I0V0` is therefore twice the average. Power fluctuates at `2f`, but meters and appliance ratings use the average
- **Evidence**: ev-194
- **Attacked by**: `P0 = 2P_ave` holds **only for a pure resistor**. With inductance or capacitance there is a phase difference, `P_ave = I_rmsV_rms cosφ`, and peak power is no longer simply twice the average; the textbook does not stress this premise. This entry restricts the claim to pure resistance and leaves phase to "Reactance and impedance"
- **Author**: @hpleapfrog · 2026-10-21

### K3 · Using rms in transmission shows why high voltage saves line loss (no attack yet)

- **Claim**: for the same average power, raising the voltage by a factor `k` lowers the line current to `1/k` and the line loss to `1/k²`
- **Premise**: the textbook uses `P_ave = I_rmsV_rms` to find 500 A for 100 MW at 200 kV and 250 kW lost in 1.00 Ω (0.250%); at 25 kV it finds 4000 A and 16.0 MW (16.0%) (ev-194)
- **Reasoning**: `I_rms = P_ave/V_rms`, so `P_loss = I_rms²R = P_ave²R/V_rms²`. Raising the voltage from 25 kV to 200 kV is a factor of 8, so the loss falls to `1/64`: `16.0%/64 = 0.250%`, matching the two textbook examples
- **Evidence**: ev-194
- **Attacked by**: the textbook attributes AC's victory to transformers and low high-voltage losses; that is a historical and engineering narrative, not a result of this reconstruction. The same `P = IV` and `P_loss = I²R` hold for high-voltage DC, which the textbook does not discuss. This entry keeps the calculation and does not treat "AC is necessary" as a physical law
- **Author**: @hpleapfrog · 2026-10-21

## Changelog

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-21 | Created; fills the rms node of elective-2 chapter 3 "Alternating current", after "Alternating current" | Written after reading m42348 in full (ev-194); the `√2` derivation and the average/rms distinction are library additions | @hpleapfrog |
