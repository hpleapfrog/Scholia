---
id: kb:physics:method-waves-ol-same-speed
type: 教法
title: "Waves · on grade level: the speed of sound is the same in the same medium, so a change in frequency means a change in wavelength"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  适用: students who know frequency and wavelength but treat them as independently adjustable quantities
  条件: `v = f λ` must already be established
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[Waves](../知识点/波.md)"]
evidence: [ev-034]
license: CC-BY-SA-4.0
---

> **English version of [`波-OL-频率变则波长变.md`](波-OL-频率变则波长变.md).**

## Method

**Present "the speed is determined by the medium" as a constraint, then bind frequency and wavelength to each other.**

Textbook original (short quotation):

> `Since sound at all frequencies has the same speed in air, a change in frequency means a change in wavelength.`

**Key point**: the causal direction of this sentence is—

```
the medium determines the wave speed v  →  with v fixed, f and λ must be inversely proportional (v = fλ)
```

**So frequency is not something you can freely adjust on its own.** Raise the frequency and the wavelength necessarily shortens.

A `[Figure Support]` that the textbook pairs with this **grounds the conclusion in a physical object**:

> The same speaker can reproduce high and low frequencies; but **high frequencies have short wavelengths**, and are best reproduced by a **small, hard, taut cone (tweeter)**;
> low frequencies are best reproduced by a large-diameter cone.

**This is the engineering-visible consequence of "a change in frequency means a change in wavelength".**

The same section's `[BL]` also gives a correspondence set for sound (tagged by the textbook as BL; teach it first if needed):

| Physical quantity | Auditory counterpart |
|---|---|
| frequency | **pitch** (high / low) |
| amplitude | **loudness** |

## Conditions of use

| Dimension | Value |
|---|---|
| Level tier | **OL** (textbook tag `[OL]`) |
| Prerequisites | `v = f λ`; knows that "the speed of sound is determined by the medium" |
| Cognitive load | medium — the load sits in **reading the formula as a constraint, not as an equality** |

## Contraindications

**Who does it not apply to?**

| Who or situation it does not apply to | Basis | Strength |
|---|---|---|
| students who have not yet established `v = f λ` | this method rests entirely on that equation; without the premise the conclusion cannot be derived | **medium** — derived from the method |
| students who do not yet know that "wave speed is determined by the medium" | the textbook's reasoning starts from `sound at all frequencies has the same speed in air` | **medium** — stated explicitly by the textbook |
| students outside this tier | the textbook **gives a different method for each tier** and does not state that this method works across tiers | **weak** — untested |

## Risks

| Where it can go wrong | Why |
|---|---|
| "a change in frequency means a change in wavelength" generalized to **changing the medium** | the premise of that sentence is **the same medium** (`in air`). Change the medium and the wave speed changes too, so the conclusion does not apply |
| students treat both f and λ as independent variables | this is exactly what must be prevented. **It must be stressed that v is determined by the medium**, otherwise the formula is just a pile of letters |
| the tweeter example taken with the causal arrow reversed | it is not "the wavelength is short so a small cone must be used", but **a small cone suits reproducing short wavelengths**. Reverse the direction and it becomes a strange physics conclusion |
| confusion with "the speed of sound does not depend on frequency" | this knowledge point is about **the speed of sound being independent of frequency** (within the same medium), which is exactly what [Speed of sound and frequency](../知识点/声速与频率.md) covers. **The two must be consistent** |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-034 | textbook (full text) | low | OpenStax《Physics》Chapter 13 · Wave Properties: Speed, Amplitude, Frequency, and Period, [m54321](https://github.com/openstax/osbooks-physics/blob/main/modules/m54321/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · Designated by the textbook for the OL tier (no attack yet)

- **Claim**: this is the method the textbook specifies for on-grade-level students
- **Premise**: the Teacher Support of m54321 tags this suggestion with `[OL]` (ev-034)
- **Reasoning**: a tier tag is the textbook's designation for that level
- **Evidence**: ev-034
- **Attacked**: **"the textbook specifies it" ≠ "measured to be effective"**; the tiered content of this section is likewise thin
- **Attribution**: @hpleapfrog · 2026-10-05

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (added a teaching method for the "wave" node) | extension of Issue #8 | @hpleapfrog |
