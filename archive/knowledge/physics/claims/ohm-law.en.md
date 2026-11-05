---
id: kb:physics:ohm-law
type: 命题
title: "Ohm's law"
status: 失据
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 初中至高中
  适用: ohmic materials
  条件: constant temperature
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-018]
license: CC-BY-SA-4.0
---

> **English version of [`欧姆定律.md`](欧姆定律.md).**

## Statement

At constant temperature, the current in a conductor is proportional to the voltage across it, with the proportionality constant being the resistance: `U = I × R` (written `V = IR` in English textbooks).

**Ohmic materials only** — i.e. materials whose resistance does not change with voltage and current.

## Basis

| Number | Type | Grade | Locator | Recomputable |
|---|---|---|---|---|
| ~~ev-002~~ | ~~experimental data~~ **voided** | — | was [`构造数据-欧姆定律演示.csv`](../../../evidence/构造数据-欧姆定律演示.csv) — **there never was any measurement** | arithmetic recomputable, but **not evidence** |
| ev-018 | textbook (full text) | low | OpenStax《Physics》Chapter 19 · Ohm's law, m54437 (CC BY 4.0) | — |

> [!CAUTION]
> **This entry's only "experimental evidence" has been judged constructed data (2026-10-05).**
> See [the section in the evidence index](../../../evidence/README.en.md#an-incident-of-our-own-registering-constructed-data-as-experimental-data).

## Argument

### A1 · ~~experimental data support~~ (**knocked down**)

- **Claim (original)**: the statement agrees with controllable experimental data
- **Premise (original)**: for the same conductor at different voltages, **the current was measured** (ev-002, **temperature 20 °C**)
- **Reasoning**: at constant temperature, the U-I graph is a line through the origin ⇒ `U ∝ I`; a constant slope ⇒ the proportionality constant is the resistance
- **Evidence**: ~~ev-002~~
- **Reasons for knocking it down**:
  1. **`ev-002` was never experimental data.** The values were constructed by the repo's author (`U = 10 × I`, R exactly `10.000`);
     **there was no measurement, no temperature control, and not even a temperature column in the CSV**. So both "**measured**" and "**temperature 20 °C**"
     are **statements about things that never happened**.
  2. Even taken as data, it **cannot achieve the resolution the conclusion needs**: the current is recorded only to `0.01 A`,
     which at `I=0.10` is **5%** ⇒ **cannot distinguish** "ohmic" from a "4.4% drift".
  3. The original line "**no need to trust this entry**" is backwards here — **the problem is precisely with the data itself**,
     and "recomputable" only guarantees arithmetic, **not that anyone measured**.
- **Status**: **knocked down**
- **To revive it needs**: **real measurement** data, registered with **significant figures / uncertainty / number of repetitions / temperature-control method**
- **Attribution**: @hpleapfrog · 2026-10-05

### A2 · Textbook statement agrees (does not self-support truth)

- **Claim (current)**: the statement in OpenStax《Physics》§19.2 agrees with this entry
- **Premise**: that textbook gives the relation and introduces the terms `ohmic` / `nonohmic` (ev-018)
- **Reasoning**: a textbook is **very low** in this repo's evidence grade. This argument **serves only to show "the notation is uncontroversial", not to support truth**
- **Evidence**: ev-018
- **Attacked**: **the original wording said "open textbooks' statements agree" — a quantifier overreach** (evidence is one book).
  Narrowed to "that textbook".
  A heavier point: this entry's `scope` ("ohmic materials only") **has its only source in ev-018**,
  while A2 itself declares ev-018 **does not take part in truth determination** — **the two cannot hold at once**.
  A2 has been explicitly downgraded to a **non-truth-supporting** note.
- **Attribution**: @hpleapfrog · 2026-10-05

> [!IMPORTANT]
> **So this entry now has no surviving argument supporting truth.**
> Status changed from `待审` to **`失据`** — the claim remains (`U = I × R` holds for ohmic materials at constant temperature,
> a textbook-level consensus), **but the repo holds not one piece of evidence able to support it.**

## Scope of application

> [!IMPORTANT]
> This entry presupposes **constant temperature** and **ohmic materials**.
>
> Applying `U = I × R` to nonlinear elements such as a small bulb (whose filament temperature varies sharply) is a common misuse.
> The OpenStax original explicitly states the law "is not universally valid" and provides the term `nonohmic`.

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | **rewrite**: removed fictional authors (@alice/@bob/@carol) and unverifiable citations; evidence changed to recomputable data + CC BY textbook; status downgraded from "已确证" to "待审" | cleaning up example entries | @hpleapfrog |
| 2026-10-05 | **A1 knocked down**: `ev-002` judged **constructed data** (never any measurement); also fixed A2's quantifier overreach and its "non-truth-supporting" self-contradiction; status `待审` → **`失据`** | [evidence index: a mistake the repo itself made](../../../evidence/README.en.md#an-incident-of-our-own-registering-constructed-data-as-experimental-data) | @hpleapfrog |
