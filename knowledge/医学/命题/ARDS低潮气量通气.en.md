---
id: kb:med:prop-ardsnet-low-tidal-volume
type: 命题
title: "For ARDS patients, low-tidal-volume ventilation reduces mortality"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 医学 · 临床证据
  学段: 不限
  适用: mechanical ventilation strategy for acute respiratory distress syndrome (ARDS) patients
  条件: **only the population and setting of that trial**; **not operating guidance** — see the subject README
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-048]
license: CC-BY-SA-4.0
---

> **English version of [`ARDS低潮气量通气.md`](ARDS低潮气量通气.md).**

> [!CAUTION]
> **This is not medical advice.** This entry records **what one trial concluded**; it is not for any specific patient.
> How to set a ventilator for a particular patient needs bedside data and qualified personnel.
> The conclusion **applies only to ARDS patients** and **must not be extrapolated to all mechanically ventilated patients** (see `scope.条件`).

## Statement

**One multicenter randomized controlled trial** compared two ventilation strategies; **the low-tidal-volume group had lower mortality**:

| | Traditional tidal volume | **Low tidal volume** |
|---|---|---|
| Starting tidal volume | **12 mL/kg predicted body weight** | **6 mL/kg predicted body weight** |
| Plateau pressure cap | **50 cmH₂O** | **30 cmH₂O** |
| **Mortality** | **39.8%** | **31.0%** |
| Ventilator-free days within 28 days | 10 ± 11 | 12 ± 11 |

- **N = 861**, multicenter randomized trial, **stopped early because of the mortality difference**
- Mortality difference **P = 0.007**
- Actually delivered tidal volume (days 1–3): **11.8 ± 0.8** vs **6.2 ± 0.8** mL/kg predicted body weight
- Actually delivered plateau pressure: **33 ± 8** vs **25 ± 6** cmH₂O

> [!IMPORTANT]
> **Two details are worth remembering separately because they are counterintuitive:**
>
> | Detail | Why counterintuitive |
> |---|---|
> | tidal volume is computed from **predicted body weight**, **not actual weight** | an obese patient's lungs do not scale with body weight; using actual weight gives an excessive tidal volume |
> | the key constrained quantity is **plateau pressure** (measured after a 0.5 s end-inspiratory pause), not peak pressure | peak pressure includes airflow resistance; **only plateau pressure reflects alveolar distension** |

> [!CAUTION]
> **This is a trial published in 2000; it gives "the outcome difference between the two arms' settings at that time".**
>
> It is **not** today's practice guideline: more than two decades on, the practical details of lung-protective ventilation
> (how PEEP is set, prone positioning, neuromuscular blockade, and **whether it applies to non-ARDS ventilated patients**)
> **are not answered by this proposition**.
>
> **The repo only states what this one trial said** — it does not extrapolate for it.

## Basis

| Number | Type | Grade | Locator | License |
|---|---|---|---|---|
| ev-048 | **randomized controlled trial (RCT)** | **high** (top tier of the repo's ladder) | The ARDS Network. *N Engl J Med.* **2000 May 4;342(18):1301-8.** PMID [10793162](https://pubmed.ncbi.nlm.nih.gov/10793162/) · DOI [10.1056/NEJM200005043421801](https://doi.org/10.1056/NEJM200005043421801) | external literature · **abstract and conclusion only** |

> **What the repo read**: only the abstract (the full text is behind a paywall). So this entry's `Statement` **writes only the numbers given in the abstract**, nothing beyond it.

## Argument

### A1 · This is the top-tier evidence on the repo's ladder (no attack yet)

- **Claim**: the conclusion is supported by a **multicenter randomized controlled trial**, the top tier of the repo's evidence ladder
- **Premise**: the trial is multicenter and randomized, N=861, and **stopped early because the primary outcome differed** (ev-048)
- **Reasoning**:
  1. randomization + control group + a pre-set primary outcome + a stopping rule —
     a design that **excludes the main confounders**; the repo's ladder puts it at the top tier
  2. the effect size is large and statistically significant (39.8% → 31.0%, P=0.007),
     and **the actually delivered tidal volumes and plateau pressures clearly separated** (6.2 vs 11.8; 25 vs 33),
     showing **the intervention was actually executed** — not "randomized but both arms did the same"
  3. the **rest of management followed the same protocol** in both arms; the difference concentrated in tidal volume and plateau pressure
- **Evidence**: ev-048
- **Attacked**: **the sample is "ARDS patients" and cannot be extrapolated to all mechanically ventilated patients**;
  and this is **the most commonly misused point**
- **Attribution**: @hpleapfrog · 2026-10-05

### A2 · This entry only declares what the trial said (no attack yet)

- **Claim**: the repo **declares only this one trial's conclusion**, not "what the current standard practice is"
- **Premise**: the repo has only the trial's **abstract**, no follow-up guidelines, systematic reviews or updates (ev-048)
- **Reasoning**:
  1. after 2000 this field **had new evidence** (PEEP strategies, prone positioning, etc.),
     **but the repo holds none of it** — so there is nothing to "update" it with
  2. writing "a 2000 trial" as "the current guideline" is **going beyond the evidence**
     (the same class of error as the `ev-002` incident)
- **Evidence**: ev-048
- **Attacked**: **this self-limitation may make readers underweight the conclusion** —
  lung-protective ventilation is widely accepted today, and saying "just a 2000 trial" makes it sound weaker than it is.
- **Response**: **the range the repo can declare is set by the sources it holds, not by the conclusion's actual weight.**
  To say more, sources must be added (later systematic reviews / guidelines) — **that is exactly the next step to take**
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**: later systematic reviews and guidelines (the repo has no source); evidence for this strategy in non-ARDS populations

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry; **the repo's first proposition using top-tier evidence (an RCT)** | user asked "how is a ventilator adjusted" | @hpleapfrog |
