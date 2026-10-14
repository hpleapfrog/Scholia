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
| [对 ARDS 患者，低潮气量通气降低死亡率](命题/ARDS低潮气量通气.md) | 命题 | 暂定确认 | **高（随机对照试验）** |
| [对阻塞性睡眠呼吸暂停，成人 PAP 调定有指南明文规定的起始压、升级规则与达标判据](命题/睡眠呼吸暂停PAP调定.md) | 命题 | 暂定确认 | **高（指南原文 + 随机对照试验）** |
| [对住院 COVID-19 患者，地塞米松按随机化时的呼吸支持水平分层：对需通气或吸氧者降低 28 天死亡率，对不需呼吸支持者未见获益且结果与可能有害一致](命题/COVID地塞米松按呼吸支持水平分层.en.md) | 命题 | 暂定确认 | **高（随机对照试验）** |
| [对重度 ARDS 患者，早期俯卧位通气降低死亡率](命题/ARDS俯卧位通气.en.md) | 命题 | 暂定确认 | **高（随机对照试验）** |
| [对高心血管风险（无糖尿病）成人，强化降压降低主要心血管事件与全因死亡，但增加部分不良事件](命题/强化降压SPRINT.en.md) | 命题 | 暂定确认 | **高（随机对照试验）** |

**5 entries.** Evidence: `ev-048` `ev-049` `ev-050` `ev-063` `ev-069` `ev-070`.

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
and surfaced the three-layer structure inside "operating guidance". It is written into the change log of [睡眠呼吸暂停 PAP 调定](命题/睡眠呼吸暂停PAP调定.md).

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
> Recorded in [`evidence/README.md`](../../evidence/README.md).

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the subject (from a question); also recorded the **third sample** of the #43 boundary and the **new dimension (risk)** | user asked "how is a ventilator adjusted" | @hpleapfrog |
| 2026-10-12 | added [睡眠呼吸暂停 PAP 调定](命题/睡眠呼吸暂停PAP调定.md) (`ev-049` guideline full-text check + `ev-050` multicenter RCT); **boundary corrected to three layers**: guideline-prescribed operating parameters may be held, with source, population limit, and disclaimer | user asked "how should the ventilator be adjusted in sleep apnea syndrome" and requested "provide sourced clinical operating guidance + references + disclaimer" | @hpleapfrog |
| 2026-10-13 | added [COVID 地塞米松按呼吸支持水平分层](命题/COVID地塞米松按呼吸支持水平分层.en.md) (`ev-063` RECOVERY trial, PMC open-access full text checked paragraph by paragraph); **this subject's first proposition presenting "the direction of effect flips across subgroups"** | ev-063 registered; topic selected against the subject boundary after the PMC full text was checked | @hpleapfrog |
| 2026-10-14 | added [ARDS 俯卧位通气](命题/ARDS俯卧位通气.en.md) (`ev-069` PROSEVA trial, abstract checked); filled the "prone positioning" gap named in the body of [ARDS 低潮气量通气](命题/ARDS低潮气量通气.en.md) | ev-069 registered; topic selected against the subject boundary | @hpleapfrog |
| 2026-10-14 | added [强化降压 SPRINT](命题/强化降压SPRINT.en.md) (`ev-070` SPRINT trial, abstract checked); **the subject's first cardiovascular proposition**, broadening beyond the earlier four that were all respiratory/critical-care | ev-070 registered; topic selected against the subject boundary | @hpleapfrog |
