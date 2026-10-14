---
id: kb:med:prop-proseva-prone-positioning
type: 命题
title: "In severe ARDS, early prone positioning reduces mortality"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-14
updated: 2026-10-14
scope:
  学科: 医学 · 临床证据
  学段: 不限
  适用: "positional strategy for mechanical ventilation in **severe ARDS** (PaO₂/FiO₂ < 150 mmHg)"
  条件: "**refers only to this trial's population and settings**; **not an operating guide** — see the subject README"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-069]
license: CC-BY-SA-4.0
---

> **English version of [`ARDS俯卧位通气.md`](ARDS俯卧位通气.md).** The front-matter keys stay in Chinese by convention; only `title` is translated.

> [!CAUTION]
> **This is not medical advice.** This entry records **what one trial concluded**; it is not about any individual patient.
> Whether a given patient should be proned, and for how long, needs bedside data and qualified staff.
> The conclusion **applies only to the "severe ARDS" the trial defined** and **cannot be extrapolated to all ARDS or all ventilated patients** (see `scope.条件`).

## Statement

**A multicenter randomized controlled trial** assigned patients with **severe ARDS** to
**prone** or **supine** positioning; **mortality was lower in the prone group**:

| | Supine | **Prone** |
|---|---|---|
| n | 229 | **237** |
| **28-day mortality** (primary outcome) | **32.8%** (75/229) | **16.0%** (38/237) |
| Hazard ratio for death | ref | **0.39** (95% CI 0.25–0.63) |
| **90-day mortality** | 41.0% | **23.6%** |
| 90-day HR | ref | **0.44** (95% CI 0.29–0.67) |

- **N = 466**, multicenter, prospective, randomized, controlled trial
- 28-day and 90-day mortality differences both **P < 0.001**
- **Complication rates did not differ significantly**; only **cardiac arrests** were **more frequent in the supine group**

**How the trial defined "severe ARDS"** (entry criteria):

- PaO₂/FiO₂ **< 150 mmHg**
- FiO₂ **≥ 0.6**
- PEEP **≥ 5 cmH₂O**
- tidal volume close to **6 mL/kg predicted body weight**

**Intervention**: prone sessions of **≥ 16 hours**; the control group stayed supine.

> [!IMPORTANT]
> **The trial's own background is part of the message:**
>
> The abstract states that **earlier prone-positioning trials in ARDS "failed to show a beneficial effect."**
> This trial **restricted the population to "severe"** (severe hypoxemia) and **started prolonged
> proning early (≥ 16 hours)** — and that is what turned the result positive.
> **The same lesson as "low tidal volume in ARDS": the conclusion is bound to its population and protocol.**

> [!CAUTION]
> **This is a 2013 trial; it reports the outcome difference between two settings at that time.**
>
> It is **not** a practice guideline: how to actually prone (when to start, how long each session,
> when to stop, how to handle complications, and **whether it applies to non-severe ARDS**)
> **are not answered by this proposition.**
>
> **This repo states only what this trial said**, and does not extrapolate for it.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-069 | **randomized controlled trial (RCT)** | **High** (top tier of this repo's ladder) | C. Guérin (PROSEVA Study Group). *N Engl J Med.* **2013 Jun 6;368(23):2159-68.** PMID [23688302](https://pubmed.ncbi.nlm.nih.gov/23688302/) · DOI [10.1056/NEJMoa1214103](https://doi.org/10.1056/NEJMoa1214103) · ClinicalTrials.gov **NCT00527813** | External literature · **abstract and conclusions only** |

> **This repo read only the abstract** (the full text is paywalled). So the `Statement` **contains only
> the numbers given in the abstract**, nothing beyond it.

## Argument

### A1 · Top-tier evidence on this repo's ladder (no attack yet)

- **Claim**: the conclusion is supported by a **multicenter RCT**, the top tier of this repo's evidence ladder
- **Premise**: multicenter, prospective, randomized design, N = 466, with 28-day mortality as the pre-specified primary outcome (ev-069)
- **Reasoning**:
  1. Randomization + control group + pre-specified primary outcome — a design **that rules out major confounding**; this repo's ladder places it at the top tier
  2. The effect is large and significant (32.8% → 16.0%, HR 0.39, P < 0.001), and **90-day mortality is in the same direction and significant** (41.0% → 23.6%, HR 0.44) — **not a single-time-point fluke**
  3. **Complication rates were similar** (only cardiac arrests, higher in the supine group), so the **survival benefit was not bought at the cost of more complications**
- **Evidence**: ev-069
- **Attacked**: **the sample is "severe ARDS" (PaO₂/FiO₂ < 150); it cannot be extrapolated to all ARDS, let alone all ventilated patients** — which is exactly where it is most often misused
- **Signed**: @hpleapfrog · 2026-10-14

### A2 · Why this trial succeeded where earlier ones did not (no attack yet)

- **Claim**: the benefit comes from **the choice of population and protocol**, not from "prone positioning works for ARDS in general"
- **Premise**: the abstract's own background says earlier prone trials in ARDS "failed to show a beneficial effect"; this trial restricted to severe ARDS and used early, prolonged proning (≥ 16 hours) (ev-069)
- **Reasoning**:
  1. Earlier trials enrolled broader populations, so the severely hypoxemic subgroup was only part of the sample — **diluting the effect**
  2. This trial's intervention was **early + ≥ 16 hours per session** of prolonged proning, on top of lung-protective ventilation (~6 mL/kg predicted body weight)
  3. So this conclusion **applies only to ARDS of the same severity as the trial's**; for milder patients, this repo has **no source** that says proning helps
- **Evidence**: ev-069
- **Attacked**: **this repo holds no systematic review or guideline on "proning in non-severe ARDS"** — so this entry **cannot answer "should mild ARDS be proned?"**, which is exactly the most common clinical question
- **Response**: **what this repo can state is bounded by the sources it holds.** To answer mild ARDS, later systematic reviews / guidelines must be registered — **which is the right next step**
- **Signed**: @hpleapfrog · 2026-10-14
- **To be added**: later systematic reviews and guidelines (no source in this repo); evidence on proning in non-severe ARDS

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-14 | Entry created; **the subject's 4th proposition**, filling the "prone positioning" gap named in the body of [ARDS 低潮气量通气](ARDS低潮气量通气.en.md) | ev-069 registered; topic selected against the subject boundary; PROSEVA abstract checked | @hpleapfrog |
