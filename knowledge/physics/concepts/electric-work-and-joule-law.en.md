---
id: kb:physics:electric-work-and-joule-law
type: 知识点
title: "Electric work and Joule's law"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have learned electric power and Ohm's law and need to compute the work done by a current and the heat produced in a resistor, and to convert electrical energy into a cost
  条件: covers electric work W = UIt, Joule's law Q = I²Rt, the equality of the two in a pure-resistance circuit, the qualitative relation W > Q in a non-resistive circuit, and kilowatt-hours and electricity cost under steady currents only; RMS values and power factor, quantitative power sharing in motors, energy storage and reactive power of capacitors and inductors, tariff structures, and energy resources and sustainability are not built
edges:
  先修: ["[Electric power](electric-power.en.md)", "[Resistance and Ohm's law](resistance-and-ohms-law.en.md)"]
  支持: []
  攻击: []
evidence: [ev-179]
license: CC-BY-SA-4.0
---

> **English version of [`电功与焦耳定律.md`](电功与焦耳定律.md).**

> [!TIP]
> **After reading this entry you should** be able to compute the work done by a current with `W = UIt`, the heat produced in a resistor with `Q = I²Rt`, distinguish the two in pure-resistance and non-resistive circuits, and convert `kW·h` into joules to work out an electricity bill

## Definition

**Electric work**: when a charge `q` passes through a potential difference `U`, the work done by the electric field is

`W = qU = UIt = Pt`

in joules (J), `1 J = 1 W·s`. For a steady current `q = It`, so the three forms are equivalent. Electric work applies to any element: a resistor, a motor, an electrolytic cell, or a battery being charged — `W = UIt` gives the total electric work done on that element.

**Joule's law**: a resistor `R` carrying a steady current `I` for a time `t` produces heat

`Q = I²Rt`

in joules. The textbook module gives `P = I²R` (valid only for resistors) and `E = Pt`, but never uses the name "Joule's law" and never combines the two into `Q = I²Rt` (ev-179); the form above is the standard statement supplied here from those two equations.

**Pure-resistance circuit**: all electric energy becomes internal energy, so electric work equals heat:

`W = Q = UIt = I²Rt = U²t/R`

The last two forms use Ohm's law `U = IR`.

**Non-resistive circuit**: a motor turns most of the electric energy into mechanical energy and an electrolytic cell turns it into chemical energy; only part becomes heat. Then

`W = Q + E_other`, i.e. `UIt = I²Rt + E_other`

so `W > Q`, and `U > IR` — `R = U/I` is no longer the resistance of the element. **The textbook module does not discuss this sharing of energy** — it mentions motors only in a fuse example and in an electric-car exercise, and every worked example in the prose is a resistor (ev-179); the relation `W > Q` and `W = Q + E_other` is a statement of scope here, not a conclusion read from that module.

**Electrical energy and cost**: a device of power `P` running for a time `t` uses

`E = Pt`

Household electricity is billed in kilowatt-hours (`kW·h`):

`1 kW·h = 1 kW × 1 h = 1000 W × 3600 s = 3.6×10⁶ J`

Cost = energy in `kW·h` × price per kilowatt-hour.

Textbook examples (ev-179):

- headlight: steady state `2.50 A × 12.0 V = 30.0 W`; cold resistance `0.350 Ω`, so at switch-on `P = 12.0²/0.350 = 411 W` and `I = √(411/0.350) = 34.3 A`
- extension cords: `5.00 A` through `0.0600 Ω` dissipates `1.50 W`; through a thinner `0.300 Ω` cord, `7.50 W`
- a 60 W incandescent bulb for 1000 h: `60 kW·h`, `$7.20` of electricity plus `$0.25` for the bulb, `$7.45` total
- a 15 W CFL with the same brightness and 10 times the lifetime: `15 kW·h`, `$1.80` of electricity plus `$0.15` of amortized bulb cost, `$1.95` total

> [!IMPORTANT]
> **Electric work is not always equal to electric heat.**
>
> `W = UIt` is the total electric work done by the current, while `Q = I²Rt` is the heat produced in a resistance. In a pure-resistance circuit they are equal; in non-resistive elements such as motors, electrolytic cells, and batteries being charged, the total work also includes mechanical or chemical energy, so `W > Q`. The textbook states that "the first equation is always valid, whereas the other two can be used only for resistors" — meaning `P = IV` always holds, while `P = V²/R` and `P = I²R` hold only for resistors. Using `Q = I²Rt` for a motor underestimates the total electric energy it consumes.

> [!IMPORTANT]
> **The resistance of a filament varies with temperature, so `R` is not a constant.**
>
> The same 12.0 V headlight draws `30.0 W` at steady state but `411 W` when cold, with the current jumping from `2.50 A` to `34.3 A` — about 14 times the steady value. The reason is that the tungsten filament's resistance rises substantially with temperature. When using `P = V²/R` or `Q = I²Rt`, if `R` changes during the interval, only instantaneous values or a piecewise approximation apply; the textbook itself uses this example to remark that "the initial power quickly decreases as the bulb's temperature increases and its resistance increases".

> [!NOTE]
> **Two exercise answers in the textbook are wrong, and there are two typesetting problems.**
>
> - **00-gauge wire exercise**: a diameter of `9.266 mm`, a length of `1 km`, and a current of `100 A` are given an answer of `25.5 W`. With the resistivity of copper `ρ ≈ 1.72×10⁻⁸ Ω·m`, the cross-sectional area is `A = π(4.633×10⁻³ m)² ≈ 6.74×10⁻⁵ m²`, the resistance is `R = ρL/A ≈ 0.255 Ω`, and the power should be `100² × 0.255 ≈ 2.55×10³ W`. The quoted `25.5 W` corresponds to `10.0 A`; the answer is off by a factor of 100.
> - **Maximum CFL price exercise**: it asks for the highest purchase price of a CFL such that the total cost over 1000 h equals that of an incandescent bulb, with electricity at `$0.10/kW·h` and the incandescent bulb at `$0.25`. The incandescent total is `60 kW·h × $0.10 + $0.25 = $6.25`; the CFL runs on `15 kW·h × $0.10 = $1.50`, so the maximum purchase price is `$6.25 − $1.50 = $4.75`. The textbook answer `$6.25` is the incandescent total, not the CFL purchase price.
> - The prose writes the kilovolt-ampere as `1 kA · V = 1 kW`; it should be `1 kV · A` (the number is the same, but `kA` is kiloamperes, not kilovolts).
> - The exercise section title is written `Problem Exercises`; the original should be `Problem & Exercises` (the `&` is missing).

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Electric power](electric-power.en.md) — `W = Pt` is power accumulated over time, and `Q = I²Rt` combines `P = I²R` with `E = Pt` |
| Prerequisite | [Resistance and Ohm's law](resistance-and-ohms-law.en.md) — the pure-resistance results `W = Q` and `W = U²t/R` both use `U = IR` |
| Follow-up | [Closed-circuit Ohm's law and internal resistance](closed-circuit-ohms-law.en.md) — the total work of the source `emf·I` splits into Joule heat `I²r` in the internal resistance and work done in the external circuit; internal heating is Joule's law |
| Related | [Power transmission](power-transmission.en.md) — the line loss `P_loss = I²R_wire` is Joule's law applied to a transmission line |
| Recorded gap | **Quantitative power sharing in non-resistive circuits (motors, electrolytic cells)**, **RMS values and power factor**, **energy storage and reactive power of capacitors and inductors**, and **tariff structures and energy resources and sustainability** are not built here |

## Arguments

### K1 · Electric work equals charge times potential difference (no attacks yet)

- **Claim**: when a charge `q` passes through a potential difference `U`, the electric work is `W = qU = UIt = Pt`
- **Premises**: the current is steady; `U` is the potential difference across the element and is constant over the interval; wire and contact resistances are neglected
- **Reasoning**: for a steady current `q = It`, and substituting into `W = qU` gives `W = UIt`; dividing by `t` gives `P = UI`, consistent with the textbook's `P = IV`. Energy is additive, so the work over an interval is the power accumulated over time, `W = Pt`. Numerical checks: the headlight `12.0 V × 2.50 A = 30.0 W` uses `30.0 × 3600 = 1.08×10⁵ J = 0.0300 kW·h` in `1.00 h`; a 60 W bulb uses `60 kW·h = 60 × 3.6×10⁶ = 2.16×10⁸ J` in `1000 h`; a lightning bolt `1.00×10² MV × 2.00×10⁴ A = 2.00×10¹² W` delivers `2.00×10⁹ J` in `1.00 ms`, matching the textbook exercise answer (ev-179)
- **Evidence**: ev-179
- **Attacked by**: holds only for steady or slowly varying currents; for AC, `U` and `I` are RMS values and a reactive element needs a power factor (not covered in this module); `W = UIt` does not say whether the energy ends up as heat, mechanical work, or chemical energy; for a source, `U` in `UIt` is the terminal voltage, not the emf
- **Author**: @hpleapfrog · 2026-10-21

### K2 · Joule's law and `W = Q` in a pure-resistance circuit (unnamed in the textbook, supplied here)

- **Claim**: a resistor carrying a steady current produces heat `Q = I²Rt`; in a pure-resistance circuit `W = Q`
- **Premises**: the element is a resistor whose `R` is approximately constant over the interval; the current is steady; the pure-resistance circuit delivers no mechanical or chemical work
- **Reasoning**: the textbook gives `P = I²R` (valid only for resistors) and `E = Pt`; combining them gives `Q = I²Rt`. In a pure resistance `U = IR`, so `W = UIt = I²Rt = Q`. Numerical check: a `0.300 Ω` extension cord carrying `5.00 A` dissipates `P = 25.0 × 0.300 = 7.50 W`, or `2.70×10⁴ J` in `1.00 h`; a `0.0600 Ω` cord gives `1.50 W`. Both match the textbook exercise answers (ev-179). The name "Joule's law" and the combination into `W = Q` are supplied here; the textbook module does not give them
- **Evidence**: ev-179 (the two equations and the numbers); the name of the law and the `W = Q` derivation are supplied here
- **Attacked by**: `R` cannot be treated as constant when it varies with temperature — the headlight's `411 W` cold and `30.0 W` hot are the same bulb; in a non-resistive element `Q = I²Rt` is only the heating part, not the total electric work; the textbook's 00-gauge answer of `25.5 W` is 100 times smaller than the correct `≈2.55×10³ W`, showing that units and orders of magnitude must be checked whenever the formula is applied
- **Author**: @hpleapfrog · 2026-10-21

### K3 · Electrical energy and cost are reckoned in kilowatt-hours (textbook example correct, exercise answer wrong)

- **Claim**: `E = Pt`, `1 kW·h = 3.6×10⁶ J`, and cost = energy × price
- **Premises**: the power is constant over the billing interval; the price does not depend on the amount used; standby power, replacement labor, and costs beyond the difference in lamp lifetime are ignored
- **Reasoning**: `1 kW·h = 1000 W × 3600 s = 3.6×10⁶ J`. The textbook CFL example: the incandescent bulb uses `60 W × 1000 h = 60 kW·h`, costing `60 × $0.12 = $7.20` plus `$0.25` for the bulb, `$7.45` total; the CFL uses `15 W × 1000 h = 15 kW·h`, costing `$1.80`, plus `$1.50/10 = $0.15` of amortized bulb cost, `$1.95` total. Both arithmetical steps check out (ev-179). Applied to the "maximum CFL price" exercise, the textbook answer `$6.25` does not match the question: `$6.25` is the incandescent total, the CFL runs on `$1.50`, so the maximum purchase price should be `$4.75`
- **Evidence**: ev-179 (the worked example); the recomputation of the maximum-price exercise is supplied here
- **Attacked by**: real tariffs are tiered and time-of-use and include fixed charges and taxes; lamp lifetime, replacement labor, and CFL start-up behavior all change the conclusion; the textbook mistakes "equal total cost" for "purchase price equal to the incandescent total", which is a conceptual error rather than rounding
- **Author**: @hpleapfrog · 2026-10-21

## Changelog

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; fills the electric-work and Joule's-law gap of "electrical energy and energy resources", completing priority 19 | ev-179 after reading m42714 in full; the name Joule's law and the combination into `W = Q` are supplied here, not given by the textbook; the 00-gauge answer off by 100× and the CFL maximum-price answer `$6.25` not matching the question are recorded in ev-179 | @hpleapfrog |
