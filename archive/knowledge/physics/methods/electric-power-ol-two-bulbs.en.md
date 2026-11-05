---
id: kb:physics:method-electric-power-ol-two-bulbs
type: 教法
title: "Electric power · OL: a 25 W bulb and a 60 W bulb"
status: 有效
author: "@hpleapfrog"
created: 2026-10-23
updated: 2026-10-23
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  适用: students who can relate I, U and R and ask what sets power
  条件: they know Ohm's law
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[electric power](../concepts/electric-power.en.md)"]
evidence: [ev-165]
license: CC-BY-SA-4.0
---

> **English version of [`电功率-OL-两只灯泡.md`](电功率-OL-两只灯泡.md).**

## What the method does

The entry point is not a formula but **two bulbs**:

> `Let us compare a 25-W bulb with a 60-W bulb. Although both operate at the same voltage, the 60-W bulb emits more light intensity than the 25-W bulb. This tells us that something other than voltage determines power.`

One sentence does three things: show the phenomenon, **eliminate voltage**, leave a question open.

### Then turn the question into a number

> `The resistance of a 100-W, 120-V incandescent lightbulb should be around 144 Ω.`

Not a new formula — `P = U²/R` used backwards: `R = 120²/100 = 144`.

### What matters is choosing among three equivalent forms

`P = UI`, `P = I²R`, `P = U²/R` all work; **which one you use depends on what is known**.
The bulb scenario is exactly what drills "known rated voltage and power → find resistance".

## Conditions

| Dimension | Value |
|---|---|
| Level | **OL** |
| Prerequisite | Ohm's law; power as rate of energy transfer |
| Load | medium — choosing among three forms |

## Contraindications

| Not suitable for | Basis | Strength |
|---|---|---|
| students without Ohm's law | all three forms come from `U = IR` | **strong** |
| a lesson that stops at "power = how fast it drains" | this practice moves on to what sets resistance | **medium** |
| students who conclude "more watts always means more consumption" | that holds only **at the same voltage** — this practice exists to break the premise |

## Risks

| Where it goes wrong | Why |
|---|---|
| "60 W is brighter because power is bigger" | the comparison is **at equal voltage**; change the voltage and the pairing fails |
| giving only `P = UI` | three equivalent forms have different uses |
| skipping numbers like `144 Ω` | the concrete number is what makes back-substitution happen |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-165 | textbook (full text) | low | OpenStax *Physics* ch. 19 · Electric Power, [m54446](https://github.com/openstax/osbooks-physics/blob/main/modules/m54446/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · The textbook's entry point (no attack yet)

- **Claim**: the source opens with 25 W vs 60 W at equal voltage and later gives 100 W/120 V → 144 Ω
- **Premise**: both the body and the Teacher Support follow this line (ev-165)
- **Reasoning**: phenomenon → eliminate voltage → "depends on resistance too" → concrete number
- **Evidence**: ev-165
- **Attacked**:
  - **"specified" ≠ "proven effective"**
  - **"three forms, pick one" is my phrasing** — the source lists them without that label
  - **144 Ω is the source's number**; I checked `120²/100 = 144`
- **Attribution**: @hpleapfrog · 2026-10-23

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-23 | Entry created from m54446 | `tools/os_source.py` read of the source (ev-165) | @hpleapfrog |
