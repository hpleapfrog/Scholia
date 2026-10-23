---
id: kb:physics:electric-power
type: 知识点
title: "Electric power"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know resistance and Ohm's law and need to compute the power consumed or dissipated in a circuit and to decide which elements heat up
  条件: covers electric power P = IV, its two rearrangements, which elements dissipate power, and the power balance of a branch circuit only; electric work W = UIt, Joule's law, and the closed-circuit Ohm's law with internal resistance are handled by other entries and are not expanded here
edges:
  先修: ["[Resistance and Ohm's law](resistance-and-ohms-law.en.md)"]
  支持: []
  攻击: []
evidence: [ev-165]
license: CC-BY-SA-4.0
---

> **English version of [`电功率.md`](电功率.md).**

> [!TIP]
> **After reading this entry you should** be able to compute electric power with `P = IV`, switch to `P = V²/R` or `P = I²R` when the voltage or current is known, and explain why a capacitor does not dissipate power

## Definition

**Electric power** is the rate at which electric energy is transferred in a circuit:

`P = IV`

Its unit is the watt (W), `1 W = 1 J/s`. The textbook derives it dimensionally: voltage `V = J/C` and current `I = C/s`, so `V × I = J/s = W`.

Substituting Ohm's law `V = IR` gives two equivalent forms:

- `P = V²/R` (voltage and resistance known)
- `P = I²R` (current and resistance known)

The textbook stresses that **only resistance dissipates electric power**; a capacitor does not dissipate it — it stores electric energy or releases it back to the circuit.

Worked examples:

- `12 V` across `100 Ω`: `I = 0.12 A`, `P = 1.4 W`
- a `60 W` bulb at `120 V`: `I = P/V = 0.50 A`
- boot warmers: two 9 V batteries in series (18 V) for 10 W give `R = V²/P = 32 Ω`; the current is about `0.56 A`, so `1130 mA·h` of batteries last about `2.0 h`
- a branch circuit: the middle branch dissipates `P = 12²/60 = 2.4 W`, the three branches total `2.4 + 3.2 + 4.8 = 10.4 W`, equal to the battery's `0.87 A × 12 V = 10.4 W` — the textbook uses this as an energy-conservation check

> [!IMPORTANT]
> **The textbook calls household 120 V "time-averaged power"; that is an error.**
>
> It writes `The 120 V is actually the time-averaged power provided by such sockets.`
> 120 V is a voltage, not a power; the time-averaged AC voltage should be called an **RMS voltage**.
> The module never introduces RMS; this library now builds it in [RMS values](rms-values.en.md), where the average AC power `P_ave = I_rms V_rms` is handled. This entry uses `P = IV` for DC and does not repeat the sentence.

> [!IMPORTANT]
> **The "heat 1 L of water" exercise is inconsistent with its options.**
>
> The exercise reads `Warming 1 g of water requires 4.18 J of energy per °C. How long would it take to warm 1 L of water from 20 to 40 °C if you immerse in the water a 1-kW resistor connected across a 9.0-V battery?`, with options 10 / 20 / 30 / 40 min.
> Heating 1 L of water by 20 °C needs about `1 kg × 4.18 kJ/(kg·°C) × 20 °C = 83.6 kJ`; 1 kW delivers that in about 84 s, and a resistor rated 1 kW at 9 V would deliver even less. None of the four options is correct, so this entry does not use the exercise.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Resistance and Ohm's law](resistance-and-ohms-law.en.md) — `P = V²/R` and `P = I²R` come from substituting `V = IR` into `P = IV`; without Ohm's law neither form exists |
| Follow-up | [RMS values](rms-values.en.md) — average AC power `P_ave = I_rms V_rms = I_rms²R = V_rms²/R` has the same form as the three DC formulas; the gap "AC rms and power factor" is filled by that entry and this one |
| Follow-up | [Reactance and impedance](reactance-and-impedance.en.md) — a circuit with reactance has `P_ave = I_rms V_rms cosφ`; power factor and power distribution in a series RLC circuit are there |
| Follow-up | [Power transmission](power-transmission.en.md) — transmitted power `P = IV` and the line loss `P_loss = I²R_wire` build directly on this entry |
| Related | [Series and parallel circuits](series-and-parallel-circuits.en.md) — the three branches in the branch-power example are in parallel and share `12 V` |
| Follow-up | [Electric work and Joule's law](electric-work-and-joule-law.en.md) — `W = Pt` and `Q = I²Rt` are this entry's power formulas accumulated over time |
| Follow-up | [Closed-circuit Ohm's law and internal resistance](closed-circuit-ohms-law.en.md) — the source's output power, total power, and terminal voltage all build on `P = IV` |
| Follow-up | [Energy resources and sustainability](energy-resources-and-sustainability.en.md) — the macroscopic view of the energy mix and efficiency builds on electric work and Joule heat |
| Recorded gap | The module also does not discuss non-ohmic loads such as motors |

## Argument

### K1 · Electric power equals voltage times current (no attack yet)

- **Claim**: `P = IV` — electric power is the product of the voltage drop and the current
- **Premise**: the textbook replaces units using `1 W = 1 J/s`, `V = J/C`, and `I = C/s` to obtain `P = IV`, and writes `This equation gives the electric power consumed by a circuit with a voltage drop of V and a current of I.`; the `12 V/100 Ω` example gives `1.4 W` (ev-165)
- **Reasoning**: each coulomb of charge crossing a potential difference `V` releases `V` joules, and `I` coulombs cross each second, so `IV` joules are released per second. Dimensionally `V·I = (J/C)(C/s) = J/s`
- **Evidence**: ev-165
- **Attacked**: dimensional analysis fixes only the product form; it cannot prove that power is `IV`. The textbook substitutes units instead of giving a physical derivation. `P = IV` holds for DC or instantaneous values, and AC requires instantaneous or average values — the textbook's remark that household 120 V is "time-averaged power" shows it does not separate these levels
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · Ohm's law gives `P = V²/R` and `P = I²R` (no attack yet)

- **Claim**: for a resistor, `P = V²/R` and `P = I²R` are equivalent to `P = IV`
- **Premise**: the textbook substitutes `I = V/R` into `P = IV` to get `P = V²/R`, and `V = IR` to get `P = I²R`, writing `only resistance (not capacitance or anything else), current, and voltage enter into the expressions for electric power.`; the branch example uses `P = V²/R` and checks that the total power balances (ev-165)
- **Reasoning**: both forms are algebraic eliminations using `P = IV` and `V = IR`, so they inherit Ohm's law's conditions: the resistance `R` is approximately constant at a given temperature
- **Evidence**: ev-165
- **Attacked**: the textbook says "only resistance, current, and voltage enter the power expressions" without separating ohmic from non-ohmic loads. For a motor, `V = IR` does not hold, and `P = I²R` is the heating power only, not the total power. Every branch in the textbook example is a resistor, so the boundary never appears
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; first node of the 必修三 "electrical energy and energy resources" chapter, attached after "Resistance and Ohm's law" | written after reading m54446 in full (ev-165) | @hpleapfrog |
| 2026-10-21 | Added follow-up nodes "RMS values" and "Reactance and impedance"; the old "the module never introduces RMS" note now points to the new entries | backfilled after reading ev-194 / ev-195 | @hpleapfrog |
