---
id: kb:physics:series-and-parallel-circuits
type: 知识点
title: "Series and parallel circuits"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know resistance and Ohm's law and need to decide whether elements are in series or in parallel and to compute equivalent resistances
  条件: covers the current and voltage rules for series and parallel connections, equivalent resistance, identical resistors in parallel, and stepwise series-parallel reduction only; the closed-circuit Ohm's law with internal resistance and electric work and Joule's law are not expanded here; capacitor charging and discharging, networks such as bridges that cannot be reduced to series-parallel combinations, and Kirchhoff's laws are not built
edges:
  先修: ["[Resistance and Ohm's law](resistance-and-ohms-law.en.md)"]
  支持: []
  攻击: []
evidence: [ev-166, ev-167]
license: CC-BY-SA-4.0
---

> **English version of [`串联与并联.md`](串联与并联.md).**

> [!TIP]
> **After reading this entry you should** be able to decide whether two resistors are in series or in parallel, compute the equivalent resistance of a series-parallel combination, and explain why a parallel equivalent resistance is always below the smallest branch resistance

## Definition

**Series**: the elements are connected one after the other in the same branch. A series circuit has the **same current everywhere**; the voltage drops across the elements add up to the source voltage, and the equivalent resistance is

`R_eq = R1 + R2 + … + RN`

**Parallel**: both ends of each element are connected directly together. The branches of a parallel circuit have the **same voltage**; the total current is the sum of the branch currents, and the equivalent resistance is given by

`1/R_eq = 1/R1 + 1/R2 + … + 1/RN`

so `R_eq` is always below the smallest branch resistance. For N identical resistors R in parallel, `R_eq = R/N`.

Worked examples:

- series: `1.0 + 6.0 + 13 Ω = 20 Ω`; at `12 V` the current is `I = 0.60 A`, and the drops `0.60 + 3.6 + 7.8 = 12 V`; with `R_eq = 150 Ω`, `R3 = 150 − 10 − 25 − 15 = 100 Ω`
- parallel: `10 / 25 / 15 Ω` give `R_eq = 4.84 Ω`; at `3 V` the total current is `0.62 A`, and the branch currents `0.30 + 0.12 + 0.20 = 0.62 A`; the smaller the branch resistance, the larger its share of the current
- the seven-resistor `10 Ω` network reduces to `160/11 Ω ≈ 14.5 Ω`
- another mixed circuit reduces to `104.09 Ω`, giving `0.096 A` at `10 V`; a messy diagram redrawn and reduced to `8.6 Ω` carries branches of `0.80 A` and `0.60 A`, for a total of `1.4 A`

> [!IMPORTANT]
> **"The voltage is the same at every point in a given wire" is an ideal-wire assumption, not a conclusion about real wires.**
>
> Both modules treat wires as `perfect conductors`, and use that to conclude that parallel branches share the same voltage. Real wires have resistance, so a current produces a potential difference along them; the textbook formulas hold only when the wire resistance is negligible. This entry keeps the assumption but states it.

> [!IMPORTANT]
> **The textbook's equivalent-resistance formulas assume a battery with no internal resistance.**
>
> The textbook treats the battery voltage as fixed, and its examples and reductions set the external terminal voltage equal to the battery's rated voltage. A real battery has internal resistance, so its terminal voltage falls under load — exactly the part covered by "closed-circuit Ohm's law with internal resistance", which is not built. The `R_eq` in this entry describes the external circuit only.

> [!IMPORTANT]
> **The sources contain several typesetting and wording defects; this entry does not carry them over.**
>
> In m54435 the second learning objective repeats `and apply Ohm's law to resistors in series` twice, and a multiple-choice option prints `5V` as `5V4`; in m54442 the complex-circuit example writes the equivalent resistance as `25.71 Ω R.` (a stray `R`), and describes the current as `across` a branch where it should be through. None of these defects changes the formulas or the numerical examples.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Resistance and Ohm's law](resistance-and-ohms-law.en.md) — `V = IR` on each resistor is the starting point for the series voltage division and the parallel current division; an "equivalent resistance" is defined as the single resistor with the same `V–I` relation as the whole group |
| Related | [Electric power](electric-power.en.md) — the branch example in the electric-power entry has three branches in parallel sharing `12 V`, and the branch powers add up to the power supplied by the battery |
| Recorded gap | **Capacitor charging and discharging with a time constant**, **networks such as bridges that cannot be reduced to series-parallel combinations**, and **a separate statement of Kirchhoff's laws** are not built in this repo; the two textbook modules also give no reduction method beyond series-parallel networks |

## Argument

### K1 · Series: same current, voltages add, and the equivalent resistance is the sum (no attack yet)

- **Claim**: for a series circuit, `R_eq = R1 + R2 + … + RN`
- **Premise**: the textbook first writes `V_i = I R_i` for each resistor by Ohm's law, uses the "hill walk" analogy that the potential change around a closed loop is zero to obtain `V_battery = V1 + V2 + V3`, and compares this with `V_battery = I R_eq` to obtain the series formula; the `12 V` example with `1.0/6.0/13 Ω` gives `R_eq = 20 Ω` and `I = 0.60 A`, checked by `0.60 + 3.6 + 7.8 = 12 V` (ev-166)
- **Reasoning**: a series branch has no split, so charge conservation requires the same current everywhere; the potential drops across the resistors add up to the potential rise across the source; factoring out the common `I` leaves the sum of the resistances in the parentheses
- **Evidence**: ev-166
- **Attacked**: the derivation uses "the potential change around a loop is zero" in place of Kirchhoff's voltage law without stating it as a law; that conclusion fails when the flux through the loop changes (electromagnetic induction), and the textbook does not mark this boundary. Treating the source voltage as constant also assumes zero internal resistance
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · Parallel: same voltage, currents add, and the reciprocal of the equivalent resistance is the sum of the reciprocals (no attack yet)

- **Claim**: for a parallel circuit, `1/R_eq = Σ 1/R_i`, so `R_eq` is below the smallest branch resistance; N identical resistors R in parallel give `R/N`
- **Premise**: the textbook notes that both ends of each parallel resistor are connected to the same pair of wires, so the voltages are equal; it then writes `I = I1 + I2 + I3` from charge conservation, substitutes `I_i = V/R_i` to obtain `I = V(1/R1 + 1/R2 + 1/R3)`, and compares this with `V = I R_eq`; the `10/25/15 Ω` example gives `R_eq = 4.84 Ω` and a total current of `0.62 A`, with branch currents `0.30 + 0.12 + 0.20 = 0.62 A`; three identical resistors in parallel give `R/3` both from the "three identical paths" argument and from the formula (ev-167)
- **Reasoning**: a parallel connection gives charge several branches; each branch current is set by its own resistance and the common voltage, and the total current is the sum of the branches; for the same `V`, adding the `I/V` values adds the conductances, so the equivalent conductance grows and the equivalent resistance falls
- **Evidence**: ev-167
- **Attacked**: the formula depends on "the voltage across every branch is identical", which in turn depends on ideal wires and a source with no internal resistance; the textbook uses the intuition "more paths make it easier to pass" to argue that `R_eq` is below the smallest resistance, but the formula itself is what proves it, and intuition cannot replace the proof. The textbook also does not discuss the drop along wires shared by parallel branches
- **Attribution**: @hpleapfrog · 2026-10-21

### K3 · Stepwise series-parallel reduction handles "any" resistor combination (no attack yet)

- **Claim**: the textbook presents "find a group that is only in series or only in parallel, replace it by its equivalent, redraw, repeat" as a general method for the equivalent resistance of `any arbitrary combination of resistors`
- **Premise**: the textbook demonstrates the four-step reduction on a network of seven `10 Ω` resistors, obtaining `160/11 Ω ≈ 14.5 Ω`; it reduces a complex circuit driven by `10 V` to `104.09 Ω` and a current of `0.096 A`, and redraws a messy diagram before reducing it to `8.6 Ω` (ev-167)
- **Reasoning**: each replacement preserves the terminal `V–I` relation, so repeated replacement leaves the equivalent resistance of the whole network unchanged; for a purely series-parallel network the process must end at a single resistor
- **Evidence**: ev-167
- **Attacked**: **not every resistor network can be reduced to a series-parallel combination**. A bridge (Wheatstone bridge) or a Y–Δ network has no subgroup that is only in series or only in parallel, so the four-step method finds nothing to reduce at its first step; such networks need Kirchhoff's laws or a Y–Δ transform. The textbook's `any arbitrary combination` is an overgeneralization, and this entry keeps only the part that holds for series-parallel networks
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; completes series and parallel circuits in the Compulsory-3 "circuits and their applications" chapter, attached after "Resistance and Ohm's law" | written after reading m54435 and m54442 in full (ev-166, ev-167) | @hpleapfrog |
