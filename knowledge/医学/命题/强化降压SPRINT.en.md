---
id: kb:med:prop-sprint-intensive-bp
type: 命题
title: "In high-cardiovascular-risk adults without diabetes, intensive BP lowering reduces major CV events and all-cause death, but raises some adverse events"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-14
updated: 2026-10-14
scope:
  学科: 医学 · 临床证据
  学段: 不限
  适用: "choice of systolic-BP target in **high-cardiovascular-risk adults without diabetes, prior stroke, or heart failure**"
  条件: "**refers only to this trial's population and settings**; **not an operating guide** — see the subject README"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-070]
license: CC-BY-SA-4.0
---

> **English version of [`强化降压SPRINT.md`](强化降压SPRINT.md).** The front-matter keys stay in Chinese by convention; only `title` is translated.

> [!CAUTION]
> **This is not medical advice.** This entry records **what one trial concluded**; it is not about any individual patient.
> What systolic target a given patient should aim for needs bedside data and qualified staff.
> The conclusion **applies only to the trial's population** (high CV risk, **no diabetes**) and
> **cannot be extrapolated to patients with diabetes, prior stroke, or heart failure** (see `scope.条件`).

## Statement

**A multicenter randomized controlled trial** compared two systolic-BP targets:

| | Standard | **Intensive** |
|---|---|---|
| SBP target | **< 140 mmHg** | **< 120 mmHg** |
| Mean SBP at 1 year | 136.2 mmHg | **121.4 mmHg** |
| **Primary composite** (MI, other ACS, stroke, heart failure, CV death) | ref | **HR 0.75** (95% CI 0.64–0.89), **P < 0.001** |
| **All-cause death** | ref | **HR 0.73** (95% CI 0.60–0.90), **P = 0.003** |

- **N = 9361**, age ≥ 50, SBP ≥ 130 mmHg, **high CV risk but no diabetes**
- "High CV risk" = one of: clinical or subclinical CVD (**excluding stroke and HF**), CKD (eGFR 20–<60), 10-year Framingham risk ≥ 15%, or age ≥ 75
- **Excluded**: diabetes, prior stroke
- **Adverse events**: hypotension, syncope, electrolyte abnormalities, AKI/renal failure **more frequent**; **injurious falls not more frequent**

> [!IMPORTANT]
> **This is a "target" trial, not a "drug" trial.**
> Both groups used clinician-chosen antihypertensives; **the only difference was the SBP target**
> (< 120 vs < 140). So this entry is about the **net effect of setting a lower target**, not of any drug.

> [!CAUTION]
> **This is a 2015 trial; it reports the outcome difference between two targets at that time.**
>
> It is **not** a practice guideline: which target a given patient should choose, and how to monitor
> (especially in **diabetes, prior stroke, or heart failure** — not enrolled here) **are not answered by this proposition**.
>
> **This repo states only what this trial said**, and does not extrapolate for it.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-070 | **randomized controlled trial (RCT)** | **High** (top tier of this repo's ladder) | SPRINT Research Group. *N Engl J Med.* **2015 Nov 26;373(22):2103-16.** PMID [26551272](https://pubmed.ncbi.nlm.nih.gov/26551272/) · DOI [10.1056/NEJMoa1511939](https://doi.org/10.1056/NEJMoa1511939) · **PMC [4689591](https://pmc.ncbi.nlm.nih.gov/articles/PMC4689591/)** (open access) | External literature · **abstract and conclusions only** |

> **This repo read only the abstract** (the full text is open access, but this entry's `Statement`
> still contains only the abstract's numbers: the hazard ratios, P values, and mean SBP at 1 year).
> **Absolute event rates and the contribution of each composite component are in the full text**, not listed here.

## Argument

### A1 · Top-tier evidence on this repo's ladder (no attack yet)

- **Claim**: the conclusion is supported by a **multicenter RCT**, the top tier of this repo's evidence ladder
- **Premise**: multicenter, randomized design, N = 9361, with a pre-specified primary composite outcome (ev-070)
- **Reasoning**:
  1. Randomization + control group + pre-specified primary outcome — a design **that rules out major confounding**; this repo's ladder places it at the top tier
  2. The effect is significant and consistent in direction: primary composite HR 0.75 (P < 0.001) and all-cause death HR 0.73 (P = 0.003) — **not a single-endpoint fluke**
  3. Mean SBP at 1 year actually separated (121.4 vs 136.2 mmHg), showing **the intervention was delivered** — not "randomized but both groups had the same BP"
- **Evidence**: ev-070
- **Attacked**: **the sample is "high CV risk without diabetes"; it cannot be extrapolated to patients with diabetes, prior stroke, or heart failure** — which is exactly where it is most often misused
- **Signed**: @hpleapfrog · 2026-10-14

### A2 · Benefit and risk coexist; this entry hides neither (no attack yet)

- **Claim**: intensive BP lowering carries **benefit and harm together** — it is not a one-way "lower is better"
- **Premise**: the abstract's conclusion is "lower fatal and nonfatal major CV events and all-cause death, **though significantly higher rates of some adverse events**" (ev-070)
- **Reasoning**:
  1. Benefit: the primary composite and all-cause death both fell significantly
  2. Harm: hypotension, syncope, electrolyte abnormalities, AKI/renal failure were more frequent — **but injurious falls were not**
  3. So "should BP be intensified?" is a **trade-off between benefit and harm**; this entry writes both sides and does not make the trade-off for the reader
- **Evidence**: ev-070
- **Attacked**: **the abstract gives hazard ratios but not absolute rates, and does not break down the composite's components (MI, stroke, HF, CV death)** — yet *which component drove the benefit* changes the clinical reading; this repo holds only the abstract
- **Response**: **what this repo can state is bounded by the sources it holds.** The full text is open access (PMC4689591) — to answer the component contributions and absolute risks, the full text should be read, **which is the right next step**
- **Signed**: @hpleapfrog · 2026-10-14
- **To be added**: the composite components' contributions and absolute event rates (full text, PMC4689591); evidence in diabetes, prior stroke, and heart failure (not enrolled in this trial)

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-14 | Entry created; **the subject's 5th proposition**, and its **first cardiovascular** one (the earlier four are all respiratory/critical-care) | ev-070 registered; topic selected against the subject boundary; SPRINT abstract checked | @hpleapfrog |
