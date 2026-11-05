---
id: kb:physics:closed-circuit-ohms-law
type: 知识点
title: "Closed-circuit Ohm's law and internal resistance"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have learned Ohm's law, series and parallel circuits, and electric power, and need to understand that a source has internal resistance, that terminal voltage changes with current, and how to compute currents and powers in a closed circuit
  条件: covers emf, internal resistance, terminal voltage, and the closed-circuit Ohm's law for steady currents, plus series and parallel combinations of identical sources; non-resistive loads (motors, electrolytic cells), capacitor transients, quantitative models of how internal resistance varies with temperature and aging, and general networks treated with Kirchhoff's laws are not built here
edges:
  先修: ["[Resistance and Ohm's law](resistance-and-ohms-law.en.md)", "[Series and parallel circuits](series-and-parallel-circuits.en.md)", "[Electric power](electric-power.en.md)"]
  支持: []
  攻击: []
evidence: [ev-178]
license: CC-BY-SA-4.0
---

> **English version of [`闭合电路欧姆定律与内阻.md`](闭合电路欧姆定律与内阻.md).**

> [!TIP]
> **After reading this entry you should** be able to compute the current and terminal voltage of a closed circuit with `I = emf/(R+r)`, explain why the terminal voltage falls as the current rises but can exceed the emf while charging, and know that the output power is largest at `R = r` while the efficiency there is only 50%

## Definition

**Electromotive force**: the potential difference between the terminals of a source when no current is flowing is called its electromotive force (emf), measured in volts. It is not a force; the textbook states "Emf is not a force at all; it is a special type of potential difference." The emf is fixed by the source itself (the chemistry of a battery, the construction of a generator) and does not depend on the external circuit.

**Internal resistance**: the resistance inside the source to the flow of current, written `r`. Dry cells and storage batteries all have it; a 12 V truck battery has a smaller internal resistance than a 12 V motorcycle battery and can therefore deliver a larger current.

**Terminal voltage**: when a current `I` flows out of the positive terminal, the voltage across the source's terminals is

`V = emf − Ir`

with `I` positive when flowing away from the positive terminal. While charging, the current reverses, `I` is negative, and `V = emf + |I|r`, so the terminal voltage is **higher** than the emf.

**Closed-circuit Ohm's law**: when the external circuit is a pure resistance `R`, treat the internal resistance as in series with it:

`I = emf/(R + r)`

Equivalently,

`emf = IR + Ir = V + Ir`

The terminal voltage varies with the external resistance:

`V = IR = emf·R/(R + r)`

With an open circuit (`R → ∞`), `V → emf`; with a short circuit (`R → 0`), `I → emf/r` and the terminal voltage tends to zero.

For a pure-resistance external circuit, the power delivered to the external circuit is

`P = I²R = emf²R/(R + r)²`

which is largest at `R = r`, where `P_max = emf²/(4r)`; the efficiency there is `P/(emf·I) = R/(R + r) = 50%`. The power and efficiency results are derived here from `I = emf/(R+r)`; the textbook module does not give them (ev-178).

**Multiple sources**: in series, `emf_total = emf₁ + emf₂ + …` and `r_total = r₁ + r₂ + …`; with opposing polarities the emfs subtract. With `n` identical sources in parallel, the total emf is unchanged and the internal resistance becomes `r/n`, so the combination can deliver a larger current.

**The electric eel**: 140 rows of 5,000 electroplaques at 0.15 V each. One row in series gives `0.15 × 5000 = 750 V`, and 140 such rows in parallel still give 750 V. If each electroplaque has an internal resistance of 0.25 Ω (the textbook exercise's data), a row has 1250 Ω and the parallel combination has `1250/140 ≈ 8.93 Ω`; into 800 Ω of water, `I = 750/(800 + 8.93) ≈ 0.93 A`.

> [!NOTE]
> **The textbook's eel numbers contradict each other.**
>
> The prose says these electroplaques "can yield an emf of approximately 600 V", but from its own data — 140 rows × 5,000 cells × 0.15 V — each row gives 750 V, and putting 140 rows in parallel does not lower the emf, so the result should be 750 V, not 600 V. 600 V would need 4,000 cells per row. With 750 V and 800 Ω of water the current is about 0.93 A, slightly below the prose's 1 A. This entry uses the computed 750 V and records the inconsistency in ev-178.

> [!IMPORTANT]
> **The emf is not a force.**
>
> The "force" in the name is historical. The emf has the unit of volts: it is the **work done by the source per unit charge around a complete circuit**, and it describes the source's ability to convert other forms of energy into electrical energy, not a force in the Newtonian sense. When comparing "emf" with "terminal voltage", remember that the former is a property of the source and the latter is how it behaves once a load is connected.

> [!IMPORTANT]
> **The terminal voltage can exceed the emf.**
>
> While a battery is being charged, current enters the positive terminal, so `I` is negative in `V = emf − Ir` and `V = emf + |I|r > emf`. The textbook's example: a 12.0 V automobile battery charged at 8.00 A with a terminal voltage of 15.0 V gives `r = (15.0 − 12.0)/8.00 = 0.375 Ω`. Decide the sign from the current direction first, then substitute; do not assume `V` is always smaller than `emf`.

> [!IMPORTANT]
> **`I = emf/(R+r)` holds only for a pure-resistance external circuit.**
>
> The derivation uses `V = IR` for the external circuit. If the external circuit contains a motor, an electrolytic cell, or another non-resistive element, the terminal voltage is no longer `IR`, and one must return to energy conservation: `emf·I = I²r + P_ext`, where `P_ext` includes mechanical or chemical work done on the outside. The textbook module does not discuss this restriction; this entry records it as a condition of use (ev-178 does not cover non-resistive circuits).

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Resistance and Ohm's law](resistance-and-ohms-law.en.md) — both the external circuit and the internal resistance obey `U = IR`; the closed-circuit law adds the source |
| Prerequisite | [Series and parallel circuits](series-and-parallel-circuits.en.md) — the internal resistance is in series with the external resistance, and identical sources in parallel reduce the internal resistance by the parallel rule |
| Prerequisite | [Electric power](electric-power.en.md) — the output power `P = I²R`, the total power `P = emf·I`, and the efficiency |
| Recorded gap | **Non-resistive loads (motors, electrolytic cells)**, **capacitor transients and RC circuits**, **quantitative models of internal resistance versus temperature and aging**, **Kirchhoff's laws and general networks**, and **battery management systems and AC measurement of internal resistance** are not built here |
| Applications | Battery testers, automobile starting circuits, solar-cell arrays and inverters, the electric organs of the electric eel |

## Arguments

### K1 · The closed-circuit law follows from energy conservation (no attacks yet)

- **Claim**: for a pure-resistance external circuit, `I = emf/(R+r)` and the terminal voltage is `V = emf − Ir`
- **Premises**: the external circuit is a pure resistance; `emf` and `r` are constant over the range considered; the current is steady; wire resistance is neglected
- **Reasoning**: as one unit of positive charge goes once around the closed circuit, the source does work `emf`, while the potential drops across the external resistance and the internal resistance are `IR` and `Ir`. Energy conservation gives `emf = IR + Ir`, hence `I = emf/(R+r)` and `V = IR = emf − Ir`. Numerical check: `12.0 V`, `r = 0.100 Ω`, `R = 10.0 Ω` → `I = 1.188 A`, `V = 11.9 V`; `R = 0.500 Ω` → `I = 20.0 A`, `V = 10.0 V`, `P = 200 W`; with `r` grown to `0.500 Ω`, `I = 12.0 A`, `V = 6.00 V`, `P = 72.0 W` — all three match the textbook (ev-178)
- **Evidence**: ev-178
- **Attacked by**: fails for non-resistive external circuits; `r` varies with temperature, aging, and current direction; wire resistance matters at large currents; the textbook's "terminal voltage equals emf when no current flows" assumes an ideal voltmeter of infinite resistance
- **Author**: @hpleapfrog · 2026-10-21

### K2 · Output power is largest at `R = r` (derived here)

- **Claim**: for a pure-resistance external circuit, `P = emf²R/(R+r)²` reaches its maximum `P_max = emf²/(4r)` at `R = r`, where the efficiency is 50%
- **Premises**: `emf` and `r` are constant; the external circuit is a pure resistance; only power dissipated in the external circuit is counted
- **Reasoning**: `P = I²R = emf²R/(R+r)²`. Since `(R+r)² ≥ 4Rr`, `P ≤ emf²/(4r)`, with equality at `R = r`. Numerical check: `emf = 12.0 V`, `r = 0.500 Ω`, `R = 0.500 Ω` → `I = 12.0 A`, `P = 72.0 W`, exactly `12²/(4×0.500)`, matching worked example (d) of the textbook (ev-178). The efficiency `P/(emf·I) = R/(R+r)` is 50% at `R = r`
- **Evidence**: ev-178 (the numbers); the maximum-power derivation is supplied here and is not in the textbook module
- **Attacked by**: `r` is not constant — the internal resistance of a real battery rises at large currents; the maximum-power point is not the maximum-efficiency point, since `R ≫ r` gives nearly 100% efficiency with very little output power; failing to distinguish "maximum power" from "maximum efficiency" leads to wrong conclusions in teaching
- **Author**: @hpleapfrog · 2026-10-21

### K3 · Series and parallel combinations of sources can be checked (no attacks yet)

- **Claim**: in series, the emfs and internal resistances of sources add; with `n` identical sources in parallel, the emf is unchanged and the internal resistance becomes `r/n`
- **Premises**: each source's `emf` and `r` are constant; series connections have consistent polarity (opposing sources subtract); parallel sources have identical emfs
- **Reasoning**: in series the current is the same and the emfs and internal-resistance drops add; in parallel the terminal voltages are the same and the currents add, so the equivalent internal resistance satisfies `1/r_total = Σ1/r_i`, which for `n` identical sources is `r/n`. Numerical check: the electric eel's 140 rows of 5,000 electroplaques at `0.15 V` — each row 750 V and 1250 Ω, the parallel combination 750 V and 8.93 Ω, giving about 0.93 A into 800 Ω. The textbook prose says "approximately 600 V, 1 A", which does not follow from its own data (ev-178)
- **Evidence**: ev-178
- **Attacked by**: parallel sources with different emfs drive circulating currents between the sources, so the "identical sources" formula does not apply; real internal resistances vary with current and temperature; the eel numbers are internally inconsistent in the textbook itself
- **Author**: @hpleapfrog · 2026-10-21

## Changelog

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; fills the shared gap of Compulsory-3 "circuits and their applications" and "electrical energy and energy resources", completing priority 18 | ev-178 after reading m42357 in full; the maximum-power and efficiency results are derived here, not given by the textbook; the eel's "approximately 600 V" inconsistency is recorded in ev-178 | @hpleapfrog |
