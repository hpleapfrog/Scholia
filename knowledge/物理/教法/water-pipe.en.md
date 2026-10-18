---
id: kb:physics:method-water-pipe
type: 教法
title: "Water-pipe analogy"
knowledge_point: ["[Resistance and Ohm's law](../知识点/resistance-and-ohms-law.en.md)"]
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 初中至高中
  水平档: 不分档
  适用: students with life experience of water flow who have not yet formed the abstract concept of charge
  条件: students have not studied electromagnetic fields
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-018]
license: CC-BY-SA-4.0
---

> **English version of [`水管类比.md`](水管类比.md).**

## Method

Map the circuit onto a water circuit:

| Circuit | Water circuit |
|---|---|
| battery | water pump |
| voltage | water pressure |
| current | water flow |
| resistance | sand filter / pipe thickness |
| capacitance | a pressure vessel with a membrane |

**Source**: the Teacher Support of OpenStax《Physics》§19.3 gives the full mapping (battery = water pump, resistance = sand filter),
and requires the teacher to **review the analogy to make sure students understand it** (`Review the analogy … to ensure that students understand it`).

## Conditions of use

| Dimension | Value |
|---|---|
| Prerequisite level | has not studied electromagnetic fields; has life experience of water flow |
| School stage | junior high to senior high |
| Equipment | unrestricted; hands-on experiments work better (peas + straws) |

## Contraindications

**Who does it not apply to?**

| Who or situation it does not apply to | Basis | Strength |
|---|---|---|
| students outside this tier | the textbook **gives a different method for each of** BL / OL / AL and does not state that this method works across tiers | **weak** — "the textbook does not specify it" ≠ "it does not apply", it is merely **untested** |

> [!WARNING]
> **This entry has no population-level contraindication supported by strong evidence.**
>
> The textbook only offers advice for this tier and **does not say this method is ineffective for other tiers**.
> Treating "the textbook did not mention it" as "it does not apply" is **over-inference** — here it is honestly marked **weak**, not invented.

## Risks

> [!CAUTION]
> **All the cautions below come from the textbook's own teaching guidance**, not my speculation.
> While adopting this analogy, the textbook **annotates point by point where it can go wrong**.

| Where it can go wrong | Why | Source |
|---|---|---|
| **the meaning of "open" is reversed** | a water-pipe valve **"open" = water flows**; an electrical switch **"open" = current is cut**. The same word means opposite things in the two contexts | §19.3 TS |
| **the mechanism differs** | water and peas push each other by **mechanical squeezing**; electrons push each other by **electrostatic repulsion** | §19.2 experiment note |
| **capacitance has no counterpart** | in the water model the pressure difference is held up by a "membrane" — this is an **extra assumption**, not something the analogy yields naturally | §19.3 TS |
| **the charge carrier gets confused** | the analogy implies that "the thing that flows" is like water; whereas in metal the charge carriers are electrons, whose direction is **opposite** to the conventional direction of current | §19.2 TS |

## Evidence

| ID | Type | Grade | Locator |
|---|---|---|---|
| ev-018 | textbook (full text) | low | OpenStax《Physics》§19.2–19.3 (CC BY 4.0) |

## Argument

### M1 · Adopted by the textbook, with a dedicated failure-mode note (no attack yet)

- **Claim**: this analogy is a usable teaching device, and its failure boundaries are publicly recorded
- **Premise**: OpenStax《Physics》§19.2–19.3 uses the water/pipe analogy and states in Teacher Support, point by point, what to review and where things differ (ev-018)
- **Reasoning**: the textbook does not merely adopt the analogy, it **explicitly marks the failure points** — showing that it is treated as a **"tool that needs teaching intervention"**, not as a **self-evident explanation**
- **Evidence**: ev-018
- **Attacked**: textbook adoption **does not equal** teaching effectiveness; **classroom measurement data is currently missing**
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**: classroom measurement (the classroom data this entry previously cited has been voided, see the change log)

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | **rewrote** the entry: deleted the fabricated author @carol and the constructed evidence ev-009/ev-010; `Contraindications` is now backed by **the textbook's own Teacher Support**; status changed from "有效（含伪造数据）" to "有效（证据仅教材采用）" | clean-up of the sample entry | @hpleapfrog |
| 2026-10-05 | split `Contraindications` / `Risks`: what the original `Contraindications` held was **risk**, and has been moved into `Risks`; also added the real population-level contraindications (with evidence-strength labels) | [Issue #13](https://github.com/hpleapfrog/Scholia/issues/13) | @hpleapfrog |
