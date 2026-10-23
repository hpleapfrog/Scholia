---
id: kb:physics:power-transmission
type: 知识点
title: "Power transmission"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done "Transformer" and "Resistance and Ohm's law" and need to explain why high-voltage transmission reduces line losses
  条件: covers the transmission chain, P = IV, P_loss = I²R_wire, and the voltage levels only; reactive power, power factor, HVDC, and grid stability are not built
edges:
  先修: ["[Transformer](transformer.en.md)", "[Resistance and Ohm's law](resistance-and-ohms-law.en.md)"]
  支持: []
  攻击: []
evidence: [ev-162]
license: CC-BY-SA-4.0
---

> **English version of [`远距离输电.md`](远距离输电.md).**

> [!TIP]
> **After reading this entry you should** be able to use `P = IV` and `P_loss = I²R_wire` to explain that raising the transmission voltage means **lowering the current**, and to say where the step-up and step-down stages sit

## Definition

**Power transmission** is the chain that carries electrical energy from a power station to users over high-voltage lines:

generation (textbook: `greater than 10 kV`) → **step-up transformer** → high-voltage line (`120 to 700 kV`) → substation **step-down** → user (`120, 240, or 480 V`)

- transmitted power: `P_transmitted = I_transmitted V_transmitted`
- line loss: `P_lost = I_transmitted² R_wire`, where `R_wire` is the resistance of the line
- for a fixed transmitted power: `I = P/V`, so `P_lost = P²R_wire / V²` — the loss falls as the square of the voltage
- the textbook's conclusion: `This is why the transmitted current must be as small as possible and, consequently, the voltage must be large to transmit the power P_transmitted.`
- step-up is for transmission; step-down is for distribution and safety; the textbook writes `Each step-up and step-down transformation is done with a transformer designed based on Faradays law of induction.`

> [!IMPORTANT]
> **"High voltage cuts losses" works by lowering the current, not by putting voltage across the wire.**
>
> The current in `P_loss = I²R_wire` is the current in the line; for a fixed transmitted power, a larger `V` makes `I = P/V` smaller, and only then does the loss drop. If `P_loss` is written as `V²/R_wire`, that `V` must be the **voltage drop across the wire's resistance** `ΔV = I R_wire`, not the line-to-ground transmission voltage. The textbook writes the two formulas but does not spell out this distinction — the paragraph above is the repo's clarification (see K1, "Attacked").

> [!IMPORTANT]
> **The textbook gives inconsistent substation voltages.**
>
> One passage says `Local power distribution ... at voltages ranging from 5 to 13 kV`; another says `the voltage is stepped down at a substation to between 5 and 30 kV`. This entry records both and does not choose one for the textbook (see K2, "Attacked").

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Transformer](transformer.en.md) — both the step-up and the step-down use `V_S/V_P = N_S/N_P`; without transformers there is no high-voltage transmission |
| Prerequisite | [Resistance and Ohm's law](resistance-and-ohms-law.en.md) — the source of `R_wire` and of the Joule heat `I²R`; the loss comes from the line's resistance |
| Related | [RMS values](rms-values.en.md) — transmission calculations use `P_ave = I_rms V_rms` and the line loss `I_rms²R_wire`; peak-rms conversion is there |
| Related | [Reactance and impedance](reactance-and-impedance.en.md) — the definition of power factor `cosφ` and average power in a series RLC circuit are there; inductive loads and reactive-power compensation on a real grid are not built |
| Recorded gap | **Reactive power, power-factor correction, and grid reactive-power dispatch**, **HVDC transmission**, and **grid stability and dispatch** are not built in this repo |

## Argument

### K1 · High-voltage transmission cuts line loss as the square of the voltage (no attack yet)

- **Claim**: for a fixed transmitted power, `P_loss = P²R_wire/V²`, so raising the transmission voltage sharply reduces the loss
- **Premise**: the textbook writes `P_transmitted = I_transmitted V_transmitted` and `P_lost = I_transmitted² R_wire`, and says `the voltage must be large to transmit the power`; its voltage range is `120 to 700 kV` (ev-162)
- **Reasoning**: substituting `I = P/V` into `P_loss = I²R_wire` gives `P_loss = P²R_wire/V²`. Doubling the voltage quarters the loss. The line resistance is fixed by material and length and cannot be reduced indefinitely by thicker conductors, so raising the voltage is the cheaper route
- **Evidence**: ev-162
- **Attacked**: the textbook **never combines the two formulas** into `P²R_wire/V²`; that substitution is the repo's. It also does not distinguish two different voltages: if `P_loss = V²/R_wire` is used, `V` is the voltage drop across the wire `ΔV = I R_wire`, not the transmission voltage; without that distinction one obtains the opposite conclusion. The textbook only warns in words that `the transmitted current must be as small as possible`
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · Why the chain transforms the voltage at both ends (no attack yet)

- **Claim**: generation, transmission, and distribution need different voltages, so the chain steps up at the plant and steps down at the substation and at the user
- **Premise**: the textbook writes generation `greater than 10 kV`, transmission `120 to 700 kV`, local distribution `5 to 13 kV`, and user `120, 240, or 480 V`; it says high-voltage transmission is to `limit energy losses` and the low user voltage is `for safety` (ev-162)
- **Reasoning**: long-distance transmission needs a small current, hence a high voltage; the user end needs a low voltage for safety; transformers link the stages. The three voltage levels correspond to three different constraints: line loss, distribution reach, and personal safety
- **Evidence**: ev-162
- **Attacked**: the textbook explains "high voltage for transmission" and "low voltage for users" but **does not explain why the generation voltage is of order 10 kV** (insulation and generator-design limits are outside this module); its substation voltage is also inconsistent (5–13 kV vs 5–30 kV), and this entry records both and marks it as a source defect. The textbook also gives no worked example for any line
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; third node of the 选必二 chapter 3 "alternating current", attached after "Transformer" | written after reading m54467 in full (ev-162) | @hpleapfrog |
| 2026-10-21 | Added related edges to "RMS values" and "Reactance and impedance"; the gap "power factor" became "power-factor correction and reactive-power dispatch" | backfilled after reading ev-194 / ev-195 | @hpleapfrog |
