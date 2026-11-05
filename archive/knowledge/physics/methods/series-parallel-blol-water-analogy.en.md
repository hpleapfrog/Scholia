---
id: kb:physics:method-series-parallel-blol-water-analogy
type: 教法
title: "Series and parallel · BL/OL: finish the water analogy properly"
status: 有效
author: "@hpleapfrog"
created: 2026-10-23
updated: 2026-10-23
scope:
  学科: 物理
  学段: 高中
  水平档: 低于年级水平（BL）至 年级水平（OL）
  适用: students drawing their first circuit diagram and still learning the symbols
  条件: they know current and voltage
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[series and parallel](../concepts/series-and-parallel-circuits.en.md)"]
evidence: [ev-166, ev-167]
license: CC-BY-SA-4.0
---

> **English version of [`串联与并联-BLOL-水管类比.md`](串联与并联-BLOL-水管类比.md).**

## What the method does

The textbook does not assume students remember the water analogy — it asks for a **review, item by item**:

> `Review the analogy between water flow and electric current to ensure that students understand it.`

Four correspondences, all named in the source:

| Water | Electricity |
|---|---|
| molecules squeezed under high pressure | charges compressed under high voltage |
| a pump raises pressure | a battery raises voltage |
| a **sand filter** obstructs flow | a **resistor** |
| a **reservoir** sets the level | **ground**, with `V_ground ≡ 0` |

Only then the four symbols: wire, battery, resistor, ground. **The order is deliberate** — symbols mean
nothing until the analogy has given them meaning.

## Conditions

| Dimension | Value |
|---|---|
| Level | **BL / OL** |
| Prerequisite | current, voltage |
| Load | low — familiar objects mapped onto new ones |

## Contraindications

| Not suitable for | Basis | Strength |
|---|---|---|
| students who can already read circuit diagrams | the analogy is an entry ticket, not content | **medium** |
| students who need equivalent-resistance practice | produces no calculation | **medium** |
| students outside this band | the source gives no level tag here | **weak** (untagged ≠ inapplicable) |

## Risks

| Where it goes wrong | Why |
|---|---|
| stopping at "the water gets used up" | water flows away; **charge does not** — "current is consumed" is the classic leftover |
| mapping only pump↔battery | the source names four; without **ground↔reservoir**, `V = 0` has no origin |
| symbols first, analogy later | in the source the symbols are the *product* of the analogy |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-166 | textbook (full text) | low | OpenStax *Physics* ch. 19 · Series Circuits, [m54435](https://github.com/openstax/osbooks-physics/blob/main/modules/m54435/index.cnxml) | **CC BY 4.0** |
| ev-167 | textbook (full text) | low | OpenStax *Physics* ch. 19 · Parallel Circuits, [m54442](https://github.com/openstax/osbooks-physics/blob/main/modules/m54442/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · The textbook asks for the review first (no attack yet)

- **Claim**: the source requires reviewing the analogy before the symbols
- **Premise**: `Review the analogy … to ensure that students understand it`, with three explicit pairs (ev-166)
- **Reasoning**: order and pairs are quoted
- **Evidence**: ev-166 · ev-167
- **Attacked**:
  - **"specified" ≠ "proven effective"**
  - **the "current is consumed" risk is mine** — the source never names it
  - **linking ground↔reservoir to `V_ground ≡ 0` spans two passages**; the connection is mine
- **Attribution**: @hpleapfrog · 2026-10-23

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-23 | Entry created from m54435's water-analogy prompt | `tools/os_source.py` read of the source (ev-166/167) | @hpleapfrog |
