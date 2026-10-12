---
id: kb:med:prop-osa-pap-titration
type: 命题
title: "For obstructive sleep apnea, adult PAP titration has guideline-prescribed starting pressures, escalation rules, and target criteria"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 医学 · 临床指南
  学段: 不限
  适用: positive airway pressure (PAP) titration for adults (≥12 y) with obstructive sleep apnea (OSA)
  条件: **records only what the guideline prescribes and one randomized trial's conclusion**; **not operating guidance for any specific patient** — see the disclaimer below
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-049, ev-050]
license: CC-BY-SA-4.0
---

> **English version of [`睡眠呼吸暂停PAP调定.md`](睡眠呼吸暂停PAP调定.md).**

> [!CAUTION]
> **Read this block first. This is not medical advice — it is a record of a guideline's prescriptions plus one trial's conclusion.**
>
> 1. **Not for any specific patient.** How to set the pressure, choose a mask, or when to follow up for a given person
>    needs diagnostic data, bedside judgment and **clinicians with prescribing authority** — the repo cannot do this and does not take it on.
> 2. **The guideline limits its own population.** The original states: applies to OSA patients **≥12 y and <12 y**,
>    **not applicable to neuromuscular disease or intrinsic lung disease** (ev-049).
> 3. **"Sleep apnea syndrome" ≠ "obstructive sleep apnea".** Central sleep apnea,
>    hypoventilation syndrome, heart failure and similar groups are **outside this entry's coverage** — their management is entirely different,
>    and this entry says **nothing** about them.
> 4. **The guideline requires titration in a proper setting by qualified personnel**: an AASM-accredited sleep center,
>    performed by a registered technologist, with pressure selection reviewed by a sleep specialist; and it explicitly warns
>    **against executing it mechanically like a "recipe"** (ev-049).
> 5. **PAP is a prescription treatment**: it needs a diagnosis before use (polysomnography or a technically adequate home monitor).
>    No number here replaces a diagnosis.
> 6. **The repo only records what this guideline and this trial say** — it does not extrapolate for them, nor judge whether they are still the latest version.

## Statement

### I. Guideline-prescribed adult CPAP / BPAP titration parameters

Each row below corresponds to a **numbered item of the original** of the [AASM 2008 *Clinical guidelines for the manual titration of positive airway pressure in patients with obstructive sleep apnea*](https://aasm.org/resources/clinicalguidelines/040210.pdf) (ev-049):

| Step | Guideline prescription (adult / ≥12 y) | Original item |
|---|---|---|
| **Starting CPAP** | **4 cmH₂O** (same for adults and children; consensus-level) | §4.2.1.2 |
| **Escalation step and interval** | **at least +1 cmH₂O** per step, **no less than 5 minutes** between adjustments, targeting elimination of obstructive respiratory events | Recommendation (6) |
| **Event thresholds that trigger escalation** | **≥2 obstructive apneas**, or **≥3 hypopneas**, or **≥5 RERAs**, or **≥3 min of loud/clear snoring** | adult titration algorithm figure |
| **Maximum CPAP** | **20 cmH₂O** (15 for <12 y) | Recommendation (4) |
| **When to switch to BPAP** | patient cannot tolerate high pressure; **or CPAP at 15 cmH₂O still has persistent obstructive events** | Recommendation (12) |
| **BPAP start and difference** | start **IPAP 8 / EPAP 4 cmH₂O**; IPAP−EPAP difference **4–10 cmH₂O**; adult maximum IPAP **30 cmH₂O** | §4.3.1.3 · §4.3.1.4 · §4.3.1.6 |
| **Criteria for the "optimal" titration** | **RDI < 5 for ≥15 minutes**, including **supine REM sleep**, with no repeated spontaneous awakenings | Recommendation (14) |
| **Other grades** | good: RDI ≤10, or (when baseline RDI<15) a 50% drop from baseline; acceptable: a 75% drop from baseline; unacceptable: neither | Recommendations (15)–(17) |

> **Why the guideline writes these as rules**: titration is "a balance between eliminating respiratory events (wants high pressure) and reducing pressure side-effects (wants low pressure)",
> and **the optimal pressure varies widely between individuals** — formulas predicting the prescription pressure from AHI or BMI **failed validation in two independent studies** (ev-049).

### II. The other path: home auto-titration has one multicenter randomized trial

The **HomePAP trial** (7 AASM-accredited sleep centers, randomized controlled) compared two complete paths (ev-050):

| | Laboratory path (LAB) | Home path (HOME) |
|---|---|---|
| Diagnosis | laboratory polysomnography (PSG) | portable home monitor |
| Titration | one-night manual titration in lab | **home auto-titrating device for 1 week**, fixed pressure prescribed at the 90th percentile |
| Usage per night at 3 months | 3.7 ± 2.4 h | **4.7 ± 2.1 h** |
| Adherence (nights used ≥4 h) | 49.4 ± 36.1% | **62.8 ± 29.2%** |

- Enrolled: adults with clinically suspected **moderate-to-severe OSA** (AHI ≥15 and ESS ≥12) referred in
- Trial conclusion: **the home path was non-inferior on acceptance, adherence, time to treatment start, and functional improvement**
- Note: the home path was managed by a sleep-specialist team; **auto-titration is not unmanaged**

> [!NOTE]
> **Do not conflate the two**: Part I is the guideline **prescribing** "how manual titration should be done";
> Part II is a trial saying **"another complete path is no worse"**.
> They answer different questions.

## Basis

| Number | Type | Grade | Locator | License |
|---|---|---|---|---|
| ev-049 | **clinical practice guideline original** | **high** (for "what the guideline stipulates" — the original is the primary source) | Kushida CA, Chediak A, Berry RB, et al. *Clinical guidelines for the manual titration of positive airway pressure in patients with obstructive sleep apnea.* **J Clin Sleep Med. 2008;4(2):157-171.** PMID [18468315](https://pubmed.ncbi.nlm.nih.gov/18468315/) · [AASM official PDF](https://aasm.org/resources/clinicalguidelines/040210.pdf) | external literature · **item numbers and short quotations only, no reproduction** |
| ev-050 | **randomized controlled trial (RCT)** | **high** (top tier of the repo's ladder) | Rosen CI, Auckley DH, Benca R, et al. *Multisite Randomized Trial of Portable Sleep Studies and Positive Airway Pressure Autotitration Versus Laboratory-Based Polysomnography…: The HomePAP Study.* **SLEEP 2012;35(6):757-766.** [PMC3353048](https://pmc.ncbi.nlm.nih.gov/articles/PMC3353048/) (open access) | external literature · **abstract and conclusion only, no reproduction** |

> **What the repo did for ev-049**: downloaded the AASM official public PDF (15 pages), extracted the full text, and checked every number in the table against its item number. **Both the numbers and the item numbers come from the original, not from a secondary source.**

## Argument

### A1 · Every number in the table traces to a numbered guideline item (no attack yet)

- **Claim**: every rule in the Part I table can be located to a specific recommendation number or algorithm figure in ev-049
- **Premise**: the repo holds the guideline's official PDF original and did a full-text extraction check (ev-049)
- **Reasoning**:
  1. for this kind of claim ("a guideline stipulates X"), **the primary source is the guideline original** —
     same as the repo's `ev-043`/`ev-044` (official regulations), it does not queue on the empirical ladder
  2. every row in the table is marked with its original item number (§4.2.1.2, Recommendation (6), etc.),
     **and the way to verify is to open the PDF to that item** — no need to trust the repo's paraphrase
- **Evidence**: ev-049
- **Attacked**: **"the guideline stipulates" ≠ "this is best"** — this entry only claims the guideline so stipulates,
  not that these numbers were validated for effect to any degree (the original marks most items as **Consensus** level, not trial-level)
- **Attribution**: @hpleapfrog · 2026-10-12

### A2 · The home auto-titration path is non-inferior to the lab path, with multicenter RCT support (no attack yet)

- **Claim**: for the moderate-to-severe OSA adults the enrollment represents, the complete path of "portable home monitor + auto-titration + P90 prescription"
  is non-inferior to "lab PSG + manual titration" on the primary outcome
- **Premise**: a randomized controlled trial at 7 AASM-accredited centers, 373 screened, about half enrolled (ev-050)
- **Reasoning**:
  1. randomization + a pre-set non-inferiority margin excludes the main confounders
  2. on 3-month adherence the home path was actually higher (62.8% vs 49.4%),
     **but the trial itself admits post-screening enrollment fell short of expectation and power was limited** — this must be recorded together
- **Evidence**: ev-050
- **Attacked**: **this trial measured a "path", not "which device algorithm is better"**;
  and the home path was managed by a sleep-specialist team throughout — reading it as "just buy a machine and titrate yourself" is
  **an extrapolation beyond the trial's population and setting**
- **Attribution**: @hpleapfrog · 2026-10-12

### A3 · This entry's timeliness and boundary are self-declared, not checked (no attack yet)

- **Claim**: this entry only records what the 2008 guideline and the 2012 trial said, **not that they are the current latest versions**
- **Premise**: the repo has **no** post-2008 titration guideline original, and no dedicated auto-titration-device guideline original (ev-049/ev-050)
- **Reasoning**:
  1. writing the 2008 guideline as "current standard practice" is the **same class of error** as the `ev-002` incident (beyond the evidence)
  2. AASM has since published updated diagnosis and treatment guidelines — **the repo has not read a single one of their originals**,
     so there is nothing to "update" to, and it can only mark timeliness honestly
- **Evidence**: ev-049 · ev-050
- **Attacked**: **this self-limitation may make readers underestimate the guideline's current force** — parts of the 2008 edition's recommendations are still used
- **Response**: **the range the repo can declare is set by the originals it holds.** To say more, the later guideline originals must be read — **that is the next step to take**
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: AASM's subsequent PAP practice guidelines and the dedicated auto-titration guidelines; a corresponding record for central sleep apnea

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-12 | established the entry; **the repo's first inclusion of guideline-prescribed operating parameters** (the boundary was previously "no operating guidance") — with source, population limit, and disclaimer | user asked "how should the ventilator be adjusted in sleep apnea syndrome", and explicitly requested "provide sourced clinical operating guidance + references + disclaimer" | @hpleapfrog |
