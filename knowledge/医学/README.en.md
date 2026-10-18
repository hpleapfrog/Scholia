# Medicine · Clinical evidence

> [!CAUTION]
> **This subject does one thing: record "what a study/guideline concluded and stipulated" and its source.**
>
> **It gives no medical advice for any specific patient.** How to set a ventilator for a particular patient
> is **outside what this repo can answer** — that needs confirmed data, bedside judgment, and qualified personnel.
>
> **Note**: since 2026-10-12, this subject **allows recording the operating parameters a guideline prescribes** —
> but only if all three hold: **verifiable source**, **population limit**, **explicit disclaimer** (see "a correction to the boundary" below).
> They are recorded as **"the guideline prescribes X"**, never as **"you should do X"**.
>
> The repo's stance from the start: **❌ does not decide "what is true" · ✅ makes every claim carry its evidence**.
> In medicine this stance is enforced **more strictly**, because the cost of being wrong is different.

> **English version of [`README.md`](README.md).**

## Current state

| Entry | Type | Status | Evidence grade |
|---|---|---|---|
| [For ARDS patients, low-tidal-volume ventilation reduces mortality](命题/ardsnet-low-tidal-volume.en.md) | Proposition | Provisionally confirmed | **High (randomized controlled trial)** |
| [For obstructive sleep apnea, adult PAP titration has guideline-prescribed starting pressures, escalation rules, and target criteria](命题/osa-pap-titration.en.md) | Proposition | Provisionally confirmed | **High (guideline primary text + randomized controlled trial)** |
| [In hospitalized patients with Covid-19, dexamethasone stratified by respiratory-support level at randomization: lower 28-day mortality among those receiving invasive ventilation or oxygen, no benefit and possible harm among those needing no respiratory support](命题/recovery-dexamethasone-by-respiratory-support.en.md) | Proposition | Provisionally confirmed | **High (randomized controlled trial)** |
| [In severe ARDS, early prone positioning reduces mortality](命题/proseva-prone-positioning.en.md) | Proposition | Provisionally confirmed | **High (randomized controlled trial)** |
| [In high-cardiovascular-risk adults without diabetes, intensive BP lowering reduces major CV events and all-cause death, but raises some adverse events](命题/sprint-intensive-bp.en.md) | Proposition | Provisionally confirmed | **High (randomized controlled trial)** |
| [For suspected plague, WHO/CDC guidelines prescribe starting treatment without waiting for confirmation, and set explicit time limits for medication, isolation, and contact prophylaxis](命题/plague-treat-on-suspicion.en.md) | Proposition | Provisionally confirmed | **High (guideline primary text)** |
| [The 2024 Chinese hypertension guideline prescribes ≥140/90 mmHg in the clinic for diagnosis, and <140/90 mmHg (further to <130/80 mmHg if tolerated) for general patients](命题/hypertension-cn-2024.en.md) | Proposition | Provisionally confirmed | **High (guideline primary text)** |
| [GOLD 2026 prescribes post-bronchodilator FEV1/FVC < 0.7 to confirm COPD, and sets "≥1 moderate or severe exacerbation in the previous year" as the E-group and treatment-escalation threshold](命题/copd-gold-2026.en.md) | Proposition | Provisionally confirmed | **High (guideline primary text)** |

**8 entries.** Evidence: `ev-048` `ev-049` `ev-050` `ev-063` `ev-069` `ev-070` `ev-071` `ev-072` `ev-073` `ev-074` `ev-075` `ev-077` `ev-078` `ev-079`.
(`ev-076` *Williams Hematology* is registered but **cited by no proposition yet** — a haematology claim will follow once the book is in hand.)

> [!NOTE]
> **From 2026-10-16, this subject registers a batch of textbooks and Chinese/foreign treatment guidelines for the first time.**
>
> `ev-074` *Harrison's* (22nd ed.) · `ev-075` *Robbins and Cotran* (10th ed.) ·
> `ev-076` *Williams Hematology* (10th ed.) · `ev-077` *Practical Internal Medicine* (16th ed.) —
> **four textbooks** — entered together with `ev-078` (Chinese hypertension guideline, 2024 revision)
> and `ev-079` (GOLD 2026).
>
> **All four textbooks are at `仅定位` (locator only) — this repo owns no copy and has checked no chapter or page number.**
> In propositions they serve **only as background pointers**, **supporting no claim**; making them carry
> verification weight requires obtaining the books and upgrading the depth (to be added).
> **Both guidelines are at `摘要` (key passages)**: the key passages were read sentence by sentence, the full text was not.

> [!NOTE]
> **From 2026-10-13, this subject holds its first proposition presenting "the direction of effect flips across subgroups".**
> "Dexamethasone treats Covid-19" saves lives in the sickest and may harm those not on oxygen — **the direction flips with severity** — and the qualifier is exactly what public transmission drops. This entry writes the direction flip and the time window together.

## How this subject came about

It began with a question: **"how is a ventilator adjusted"**.

I handled it the repo's usual way — **find a real source first, then decide whether it fits**. Two things resulted:

## I. What doesn't fit: **"how to adjust"**

Adjusting a ventilator is **procedural knowledge** (set parameters → read feedback → adjust again),
and the repo already ruled in [Issue #43](https://github.com/hpleapfrog/Scholia/issues/43):

> **The repo does not hold "how to do a thing".** `路径` is "an arrangement of 知识点", not operation steps.

**This is the third sample** (the first two were "taking the subway" and "flying"), **but it brought a new dimension**:

| Probe | Content | Consequence of error |
|---|---|---|
| taking the subway | enter → exit | wrong direction |
| flying | check-in → arrival | missed flight |
| **ventilator** | **adjust parameters** | **patient death** |

> [!IMPORTANT]
> **The first two boundaries rested on "procedures are everywhere; repeating them only adds noise" (the scarcity criterion).**
>
> **This time there is a stronger reason: high risk.**
>
> **The repo dares not hold high-risk procedural content** — not because it isn't real,
> but because **the repo cannot make the reader know "who this applies to"**.
> A "tidal volume 6 mL/kg" written here, followed by someone without bedside data —
> **the repo can neither prevent it nor answer for it.**

**So this boundary now has two reasons: scarcity (don't repeat what's everywhere) and risk (don't hold procedures that can kill).**
The "what the repo does **not** hold" section of `FORMAT.md` has been given the second criterion (risk); see that document.

### A correction to the boundary (2026-10-12)

In the same week the user asked a second question ("how should the ventilator be adjusted in sleep apnea syndrome"), and explicitly requested:
**provide clinically-sourced operating guidance, with references and a disclaimer.**

This exposed that "no clinical operating guidance at all" was **too broad a cut**:

| Layer | Content | Hold? | Reason |
|---|---|---|---|
| 1 | **sourceless procedures** ("an online remedy says set the pressure to X") | ❌ still not held | risk + scarcity, reason unchanged |
| 2 | **operating parameters the guideline prescribes** (starting pressure, escalation threshold, target criteria) | ✅ **can hold** | it is a **verifiable regulation**: has a source, a population limit, and can be checked item-by-item against the original entry numbers — exactly what the repo is best at recording |
| 3 | **an adjustment decision for a specific patient** | ❌ still not held | beyond the repo's ability: no patient data, no qualification |

> [!IMPORTANT]
> **What was corrected is not "whether we dare hold it", but "how to phrase it".**
>
> A layer-2 entry must be stated as **"the guideline prescribes X (entry N, population limit Y)"**,
> never as **"you should do X"**; and the **disclaimer block must be at the very top of the body**,
> stating the population exclusion, the setting requirement, and "the repo cannot judge applicability".
> The reader gets **a list of sourced regulations**, not a prescription.

**This correction would not have happened without the second question** — it came from a real information need,
and surfaced the three-layer structure inside "operating guidance". It is written into the change log of [OSA PAP titration](命题/osa-pap-titration.en.md).

> [!NOTE]
> This boundary, together with the overall criterion for "not holding procedures" (scarcity + risk), is in
> [decision record: the boundary of procedural knowledge](../../docs/decisions/procedural-knowledge-boundary.en.md);
> the medicine-specific "guideline prescriptions may be held, with source and disclaimer" is above on this page.

## II. What fits: **"what evidence there is"**

With "how to adjust" removed, what remains is **exactly what the repo is best at**:

| What remains | Why it fits |
|---|---|
| **the target value of a parameter** | has a true value, checkable item-by-item against the original |
| **which study gave that target** | has a source, verifiable |
| **how much the outcome changed under a different strategy** | **has numbers, statistics, p-values** |

**And this brought something that had never happened in the repo**:

> **`ev-048` is the repo's first top-grade evidence (a randomized controlled trial).**
>
> Before it, of 40 evidences **37 were textbooks, 3 were official documents** — **the top four tiers had never been used.**
>
> **And it exposed a problem with the ladder**: this ladder is designed for "empirical propositions about populations",
> **unfair to physics** — an `F = ma` in a textbook falls to the lowest tier,
> which is nothing like "a teaching suggestion in a textbook".
> Recorded in [`evidence/README.en.md`](../../evidence/README.en.md).

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the subject (from a question); also recorded the **third sample** of the #43 boundary and the **new dimension (risk)** | user asked "how is a ventilator adjusted" | @hpleapfrog |
| 2026-10-12 | added [OSA PAP titration](命题/osa-pap-titration.en.md) (`ev-049` guideline full-text check + `ev-050` multicenter RCT); **boundary corrected to three layers**: guideline-prescribed operating parameters may be held, with source, population limit, and disclaimer | user asked "how should the ventilator be adjusted in sleep apnea syndrome" and requested "provide sourced clinical operating guidance + references + disclaimer" | @hpleapfrog |
| 2026-10-13 | added [Covid-19 dexamethasone by respiratory-support level](命题/recovery-dexamethasone-by-respiratory-support.en.md) (`ev-063` RECOVERY trial, PMC open-access full text checked paragraph by paragraph); **this subject's first proposition presenting "the direction of effect flips across subgroups"** | ev-063 registered; topic selected against the subject boundary after the PMC full text was checked | @hpleapfrog |
| 2026-10-14 | added [ARDS prone positioning](命题/proseva-prone-positioning.en.md) (`ev-069` PROSEVA trial, abstract checked); filled the "prone positioning" gap named in the body of [ARDS low-tidal-volume ventilation](命题/ardsnet-low-tidal-volume.en.md) | ev-069 registered; topic selected against the subject boundary | @hpleapfrog |
| 2026-10-14 | added [intensive BP lowering (SPRINT)](命题/sprint-intensive-bp.en.md) (`ev-070` SPRINT trial, abstract checked); **the subject's first cardiovascular proposition**, broadening beyond the earlier four that were all respiratory/critical-care | ev-070 registered; topic selected against the subject boundary | @hpleapfrog |
| 2026-10-14 | added [treat before confirming plague](命题/plague-treat-on-suspicion.en.md) (`ev-071` WHO manual, `ev-072` CDC emergency guidance, `ev-073` CDC MMWR recommendation report - all checked at abstract level); originating question: "when plague comes back, what is needed?"; **the discipline's 6th proposition and its first one led by guideline text rather than trials** | `ev-071` · `ev-072` · `ev-073` registered, then topic selected within the discipline boundary | @hpleapfrog |
| 2026-10-16 | registered `ev-074`–`ev-077`, **four standard textbooks** (all `仅定位`: no copy in hand), and `ev-078` · `ev-079`, **one Chinese and one foreign treatment guideline** (both `摘要`); added [blood-pressure targets in the 2024 Chinese hypertension guideline](命题/hypertension-cn-2024.en.md) (`ev-078` guideline text + existing `ev-070` SPRINT + two textbook backgrounds) and [COPD diagnosis and treatment in GOLD 2026](命题/copd-gold-2026.en.md) (`ev-079` pocket guide and key-changes summary + two textbook backgrounds); **the discipline's 7th and 8th propositions, extending coverage from respiratory/critical-care/cardiovascular to hypertension and COPD, and the first time textbook evidence enters the ledger** | arose from the task of collecting foreign and Chinese medical treatment guidelines and four standard textbooks; `ev-074`–`ev-079` registered, then topic selected within the discipline boundary; key passages of the guidelines read and checked sentence by sentence | @hpleapfrog |
