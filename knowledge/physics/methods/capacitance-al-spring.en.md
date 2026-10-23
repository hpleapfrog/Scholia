---
id: kb:physics:method-capacitance-al-spring
type: 教法
title: "Capacitance · AL: what sets a spring's capacity"
status: 有效
author: "@hpleapfrog"
created: 2026-10-23
updated: 2026-10-23
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶水平（AL）
  适用: students who can use C = Q/U and ask what capacitance itself depends on
  条件: they know a spring stores elastic potential energy
edges:
  先修: []
  支持: []
  攻击: []
knowledge_point: ["[capacitance](../concepts/capacitance.en.md)"]
evidence: [ev-175]
license: CC-BY-SA-4.0
---

> **English version of [`电容-AL-弹簧的容量.md`](电容-AL-弹簧的容量.md).**

## What the method does

The `[AL]` prompt is a **three-question chain**:

> `[AL] Discuss how a spring has a capacity to store mechanical energy. Discuss which properties of the spring would increase its capacity to store energy. Point out that these properties are intrinsic to the spring.`

| Question | Job |
|---|---|
| what "storing energy" means for a spring | builds the container intuition |
| which properties increase it | turns capacity into **changeable parameters** |
| those properties are **intrinsic** | the landing point: **capacity does not depend on how much is stored** |

`Point out` marks the third as a conclusion to be **stated explicitly**, not left to discovery.

## Conditions

| Dimension | Value |
|---|---|
| Level | **AL** |
| Prerequisite | `C = Q/U`; elastic potential energy |
| Load | medium to high — three ideas at once |

## Contraindications

| Not suitable for | Basis | Strength |
|---|---|---|
| students without `C = Q/U` | the landing point needs the formula to be sayable | **strong** |
| students meeting capacitance for the first time | that is the `[BL]/[OL]` entry (dictionary → storage analogy) | **strong** |
| students who need series/parallel calculations | produces no calculation | **medium** |

## Risks

| Where it goes wrong | Why |
|---|---|
| stopping at "it's like a spring" | the third question is the point; without it students infer "more charge → bigger capacitance" |
| reading "intrinsic" as "constant" | intrinsic means **not depending on charge**; changing the dielectric or geometry does change it — the rest of this section is about dielectrics |
| replacing geometry and dielectric with "stiffness" | the spring is the analogy; the physical parameters are plate area, separation, dielectric constant |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-175 | textbook (full text) | low | OpenStax *Physics* ch. 18 · Capacitors and Dielectrics, [m63179](https://github.com/openstax/osbooks-physics/blob/main/modules/m63179/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · Specified by the textbook for AL (no attack yet)

- **Claim**: the three-question chain is the textbook's practice for advanced students
- **Premise**: m63179 contains `[AL] Discuss … Discuss … Point out …` (ev-175)
- **Reasoning**: order and landing point are quoted
- **Evidence**: ev-175
- **Attacked**:
  - **"specified" ≠ "proven effective"**
  - **the "intrinsic ≠ constant" clarification is mine** — the textbook says only `intrinsic to the spring`
- **Attribution**: @hpleapfrog · 2026-10-23

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-23 | Entry created from m63179's `[AL]` chain | `tools/os_source.py` read of the source (ev-175) | @hpleapfrog |
