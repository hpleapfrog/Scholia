---
id: kb:med:prop-recovery-dexamethasone-by-respiratory-support
type: 命题
title: "In hospitalized patients with Covid-19, dexamethasone stratified by respiratory-support level at randomization: lower 28-day mortality among those receiving invasive ventilation or oxygen, no benefit and possible harm among those needing no respiratory support"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-13
updated: 2026-10-13
scope:
  学科: 医学 · 临床证据
  学段: 不限
  适用: hospitalized patients with Covid-19 (176 NHS organisations in the UK, 2020-03 to 2020-06) stratified by respiratory-support level at randomization
  条件: "**applies only to the trial's population, dose and setting**; **not operating guidance**, see the disclaimer below. This is the **preliminary report** (published 2020-07-17); the final version is noted under `依据`"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-063]
license: CC-BY-SA-4.0
---

> **English version of [`COVID地塞米松按呼吸支持水平分层.md`](COVID地塞米松按呼吸支持水平分层.md).**

> [!CAUTION]
> **This is not medical advice.** This entry records **what one trial concluded**; it is not about any specific patient.
> Whether to give glucocorticoids to a particular patient, at what dose and for how long, requires clinical judgment and qualified personnel.
> The conclusion **applies only to the hospitalized Covid-19 patients enrolled in this trial** and **cannot be extrapolated to outpatients, other viral pneumonias or other inflammatory states** (see `scope.条件` and Argument A3).

## Statement

**A multicentre randomized controlled trial** compared "usual care + dexamethasone" with "usual care alone".
Overall 28-day mortality was lower with dexamethasone, but **the direction of effect flipped with the level of respiratory support at randomization**:

| | Usual care | **Dexamethasone** | Rate ratio (95% CI) |
|---|---|---|---|
| **Overall** | 25.7% | **22.9%** | **0.83** (0.75–0.93), P<0.001 |
| **Invasive mechanical ventilation** | 41.4% | **29.3%** | **0.64** (0.51–0.81) |
| **Oxygen only** (no invasive ventilation) | 26.2% | **23.3%** | **0.82** (0.72–0.94) |
| **No respiratory support** | 14.0% | **17.8%** | **1.19** (0.91–1.55) |

- **N = 6425** (dexamethasone 2104 · usual care 4321), 176 NHS organisations in the UK
- Dose: **6 mg once daily, oral or intravenous, for up to 10 days** (or until discharge)
- Age-adjusted absolute reduction: invasive ventilation **12.3 percentage points** (95% CI 6.3–17.6); oxygen only **4.2 percentage points** (95% CI 1.4–6.7)
- Trend test across respiratory-support strata: **χ² = 11.5**
- Trend by duration of symptoms: **benefit in those symptomatic >7 days; no benefit in recent onset** (trend χ² = 12.3)
- Secondary outcomes: alive discharge within 28 days RR **1.10** (1.03–1.17); progression to invasive ventilation RR **0.77** (0.62–0.95)

> [!IMPORTANT]
> **Three details worth remembering on their own, because they cut against intuition:**
>
> | Detail | Why it cuts against intuition |
> |---|---|
> | **The same drug saves lives in the sickest and may harm those not on oxygen** | "dexamethasone treats Covid-19" is literally true, but **dropping the population qualifier turns it into a misdirection** — the direction flips with severity |
> | **Benefit grows with duration of symptoms; it is not "the earlier the better"** | Opposite to the "earlier the better" pattern of antivirals: benefit >7 days, none in recent onset; the paper's explanation is **late disease is inflammation-dominated, early disease is virus-replication-dominated** |
> | **8% of the usual-care arm actually received dexamethasone** | The trial was open-label; **crossover dilutes the effect** — the true effect may be larger than measured |

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-063 | **Randomized controlled trial (RCT)** | **High** (top tier of this repo's ladder) | The RECOVERY Collaborative Group. *Dexamethasone in Hospitalized Patients with Covid-19 — Preliminary Report.* **N Engl J Med. 2020 Jul 17 (online); final: N Engl J Med. 2021;384(8):693-704.** PMID [32678530](https://pubmed.ncbi.nlm.nih.gov/32678530/) · DOI [10.1056/NEJMoa2021436](https://doi.org/10.1056/NEJMoa2021436) · [PMC7383595](https://pmc.ncbi.nlm.nih.gov/articles/PMC7383595/) (**open access; this repo read the full text**: methods, results, Tables 1–2, Figures 2–3, discussion) | External literature · **cite only the abstract and conclusions; no full text reproduced** |

> **What this repo did with ev-063**: opened the PMC open-access full text and checked every number and confidence interval above against the article, paragraph by paragraph.
> **This entry cites the preliminary report of 2020-07-17** (the PMC version); the final version was published in 2021 under the same DOI and the core numbers are identical.

## Argument

### A1 · The direction of effect flips with respiratory-support level, and the trend test is significant (not yet attacked)

- **Claim**: **the direction of dexamethasone's effect is not constant** — it lowers mortality among those receiving invasive ventilation or oxygen, and shows **no benefit, with a point estimate consistent with possible harm, among those needing no respiratory support**
- **Premise**: a prespecified stratified analysis by respiratory-support level at randomization, trend χ² = 11.5 (ev-063)
- **Reasoning**:
  1. This is a **prespecified subgroup analysis** (respiratory support was recorded at randomization), not a post-hoc split — **the most common failure mode of subgroup analyses (post-hoc grouping) does not apply here**
  2. The three strata's point estimates move monotonically with severity: **0.64 → 0.82 → 1.19**, absolute reductions **12.3 → 4.2 → 0 (possibly negative)**
  3. The no-support stratum's rate ratio of 1.19 **has a confidence interval crossing 1** (0.91–1.55) — so the paper says "**consistent with possible harm**", **not "proven harmful"**
  4. The paper's mechanistic explanation: **late disease is dominated by immune-mediated inflammatory injury, early disease by virus replication** — suppressing inflammation with glucocorticoids is rational late and may impede viral clearance early
- **Evidence**: ev-063
- **Attacked by**: **the no-support stratum's CI crosses 1** — "possible harm" is a point-estimate direction, not a statistical conclusion. **This entry must not be written as "proven harmful in those not on oxygen".**
- **Author**: @hpleapfrog · 2026-10-13

### A2 · Benefit grows with symptom duration, opposite to the "earlier the better" intuition (not yet attacked)

- **Claim**: **benefit appears in those symptomatic >7 days; no benefit in recent onset**
- **Premise**: a prespecified subgroup analysis by symptom duration, trend χ² = 12.3 (ev-063)
- **Reasoning**:
  1. The common pattern for antivirals (e.g. remdesivir) is "earlier is better" — dexamethasone's benefit distribution **runs the other way**
  2. The paper reads the two side by side: **antivirals target the early virus-replication phase; glucocorticoids target the late inflammation phase** — **not "steroids are better", but "different phases"**
  3. This explains why invasively ventilated patients had a **median of 13 days of symptoms** (about 7 days longer than the no-support stratum) — **severity itself means longer illness**
- **Evidence**: ev-063
- **Attacked by**: **symptom duration was self-reported**, so the stratified analysis depends on patient recall; and whether the >7-day vs ≤7-day cut-off was set **before or after looking at the data, this repo could not find stated in the abstract or full text**
- **Author**: @hpleapfrog · 2026-10-13

### A3 · This entry states only what the trial said, not "today's standard of care" (not yet attacked)

- **Claim**: this repo **states only this trial's conclusion**; it does not state "how current guidelines read"
- **Premise**: this repo holds **this one paper only** — no WHO / NIH / Chinese guideline texts (ev-063)
- **Reasoning**:
  1. The paper notes that "guidelines issued by the U.K. chief medical officers and by the National Institutes of Health in the United States have already been updated" — **but this repo has not read any of those guideline texts**
  2. There is also a **dose-comparison RECOVERY trial** (higher vs lower dose dexamethasone) — **this repo has no text for it either**, so it cannot speak to "should the dose be higher"
  3. Writing "a 2020 UK hospitalized-population trial" as "the current standard" would be **beyond the evidence** (same class of error as the `ev-002` incident)
- **Evidence**: ev-063
- **Attacked by**: **this self-limitation may understate the conclusion's weight** — glucocorticoids for Covid-19 are widely accepted today, and calling it "just one 2020 trial" makes it sound weaker than it is.
- **Response**: **what this repo can state is bounded by the primary texts it holds, not by the conclusion's actual weight.** To state more, it needs more sources (subsequent guideline texts, the dose-comparison trial, a systematic review) — **that is exactly the next step**.
- **Author**: @hpleapfrog · 2026-10-13
- **To be added**: WHO / NIH / Chinese Covid-19 treatment guideline texts; the RECOVERY dose-comparison trial text; evidence on glucocorticoids in other viral pneumonias

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Before 2020, most Covid-19 guidelines listed glucocorticoids as "contraindicated or not recommended."**
>
> **After this trial, "dexamethasone treats Covid-19" quickly became common knowledge — but common knowledge dropped the most critical part in transmission: the population qualifier.**
> "Steroids treat Covid-19" saves lives in the sickest and may harm those not on oxygen — **the direction flips with severity** — yet in public memory the two versions are the same sentence.
>
> **This library's mission is to remove noise and store real information.**
> "Dexamethasone treats Covid-19" is noise (a half-sentence stripped of its qualifier);
> **"stratified by respiratory-support level at randomization, those on ventilation/oxygen benefit and those not on oxygen may be harmed, and benefit grows with symptom duration" is real information** — it writes the direction flip and the time window together, and those are exactly what public transmission drops first.
>
> This entry is the latter — **the sentence that says what the trial actually said, not the compressed one.**

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-13 | Entry created; **the repo's second proposition using top-tier evidence (RCT)**, and the first to present "the direction of effect flips across subgroups" | ev-063 registered; topic selected against the subject boundary after this repo opened the PMC open-access full text and checked it paragraph by paragraph | @hpleapfrog |
