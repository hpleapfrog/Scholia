---
id: kb:physics:textbook-tiered-guidance
type: 命题
title: "Textbooks' built-in teaching variants tiered by learner level"
status: 需复审
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  适用: textbook authors · teaching-method researchers · path arrangers
  条件: using OpenStax《Physics》as the sample
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-020]
license: CC-BY-SA-4.0
---

> **English version of [`教材内建分组教学变体.md`](教材内建分组教学变体.md).**

## Statement

> [!CAUTION]
> **This entry's A1 was once knocked down (2026-10-05).**
> **Scripts and data have now been supplied, and after narrowing it is re-asserted (see `A3`), status `需复审`.**
>
> **The three sentences knocked down were**: ~~"note-level tiering"~~ · ~~"anyone can re-run and get the same statistics"~~ · ~~the expansions of those four abbreviations~~.
> See the [attack entry](攻击/tieredguidance.en.md).

OpenStax《Physics》 (high school, CC BY 4.0) has **Teacher Support teaching hints** outside the main text,
and some **paragraphs** among them begin with `[BL]`/`[OL]`/`[AL]`/`[EL]` markers.

**These numbers are now recomputable** — the script [`evidence/os-teacher-markers.py`](../../../evidence/os-teacher-markers.py),
the detail [`os-teacher-markers.csv`](../../../evidence/os-teacher-markers.csv),
OpenStax repo ref `main` · **commit `dfdfd7a5356ecdd42e504de3df50d9153e33ea49`**:

| Marker | Strict (`<span>` at paragraph start) | **Loose (any occurrence in a note)** |
|---|---|---|
| `[OL]` | 243 | **245** |
| `[BL]` | 205 | **207** |
| `[AL]` | 189 | **191** |
| `[EL]` | **0** | **5** |
| | 637 | **648** |
| total `os-teacher` notes | **582** | |

> [!IMPORTANT]
> **The difference between the two columns is the difference of "counting convention", and the repo had never written down its convention.**
>
> The old entry's "649 / 580" is neither — it is **a snapshot of some `main`**.
> Now `main` has moved on, and the same rule would give a different number.
> **This is the price of "no commit anchor": a drifting number was written as an assertion.**

> [!WARNING]
> **The expansions of the four abbreviations still have no source.**
>
> Measured: `Below Level` appears **only once** in the whole book (and in prose: `a student that is at or below level`),
> and `Advanced Learners` **not once**. **There is no legend in the textbook.**
>
> So "`[BL]` = below grade level" is **an inference from common educational abbreviations**, not a quotation.
> For "`[EL]` = English Learners" there is **circumstantial evidence** — in m54057 `[BL][EL]` is immediately followed by
> `English learners may need …`.
>
> **The repo's `(knowledge point × level)` model rests on this inference**, and should be labeled as such honestly.

> [!IMPORTANT]
> **Markers hang on `<para>`, not on `note` — and can be multiple.**
>
> Source form (`m54108`):
>
> > ```xml
> > <para><span>[BL]</span><span>[OL]</span> You may want to introduce the concept of a reference point...</para>
> > <para><span>[AL]</span> Explain that the reference frames considered in this chapter are inertial...</para>
> > ```
>
> **So the correct granularity is "paragraph", not "note"**:
>
> - one **suggestion** (= one `<para>`) carries one or more audience tags
> - `[BL][OL]` means **this suggestion is for two groups at once** ⇒ **the reading "each tier is exclusive" is wrong**
> - but **the same batch of data cannot distinguish "for these two groups" from "do this first, then that"** —
>   **`A3` asserts only the verifiable part of the former**

## Basis

| Number | Type | Grade | Locator | License |
|---|---|---|---|---|
| ev-020 | textbook (full text) | low | Teacher Support of all 23 chapters / 98 modules of OpenStax《Physics》 | **CC BY 4.0** |

> [!CAUTION]
> **The original text here said "the extraction method is recomputable … anyone can re-run and get the same statistics". That sentence has been knocked down.**
>
> `evidence/README.md`'s threshold is "recomputable **scripts and data**",
> and **ev-020 has neither script nor data**; its locator is the repo front page, **with no commit anchor**.
> Nor is the convention unique: the rule writes a `<note>` element, but `m54108` has **23 `<note>`, only 11 of which are `os-teacher`** —
> **580 can only be the result of filtering by `os-teacher`, and this filter is not written in the method.**
>
> **A literal implementation will necessarily give a number different from 580.** For the remedy see the [attack entry](攻击/tieredguidance.en.md) (script + detail + commit hash).

## Example: one concept, three tiers of teaching

Module `m54108` "Relative Motion, Distance, and Displacement" gives, for **one knowledge point**
(reference frames and relative motion), three tiers of different practices:

| Tier | Textbook original (short quotation) |
|---|---|
| `[BL]` | `Have students practice describing simple examples of motion in the class from different reference frames. For example, slide a book across a desk.` |
| `[OL]` | `Start by asking what position is and how it is defined. You can use a toy car or other object.` |
| `[AL]` | `Ask the students to form pairs, and ask each pair to come up with their own definition of motion. Then compare and discuss definitions as a class.` |

**The three practices differ in the allocation of cognitive load**:

- `[BL]`: **hands-on operation + juxtaposing multiple reference points** (slide a book, describe from another viewpoint)
- `[OL]`: **question-led** (first ask "what is position", then introduce "an origin is needed")
- `[AL]`: **generative task** (students define it themselves → pair up → whole-class comparison)

## Argument

### A3 · Markers are **paragraph-level audience labels**, and the count is now recomputable (**no attack yet**)

- **Claim (after narrowing)**: in that textbook's Teacher Support, **some `<para>` carry one or more audience markers**;
  these markers **point to different suggestions**; the counting convention is now written down and the results recomputable
- **Premise**:
  1. in the source file the marker is a contiguous `<span>[XX]</span>` at the start of a `<para>` (not an attribute of `note`)
  2. script + detail + commit hash are committed with the repo (`dfdfd7a5356ecdd42e504de3df50d9153e33ea49`)
  3. numbers under both conventions are given (strict 637 / loose 648)
- **Reasoning**:
  - since markers **hang on paragraphs**, they are **audience labels for a suggestion**, not a classification of the whole note
  - **multiple markers** (`[BL][OL]`) show one suggestion can serve multiple groups ⇒ **"each tier exclusive" is wrong**
- **Evidence**: [ev-020](../../../evidence/README.en.md), script and detail
- **Attacked**: **none** — **`A3` is newly raised this round and has no attack edge yet**
- **Explicitly not asserted** (where the old `A1` overreached):
  - ❌ not asserting "note-level tier cards"
  - ❌ not asserting "tiers are mutually exclusive"
  - ❌ not asserting the four abbreviations' **expansions** have textbook grounds (that is inference, and there is no legend)
  - ❌ not asserting "`649` is the number of tier markers" — those two numbers (637/648) are **string-hit counts**,
    among which `[EL]` is a **language identity**, not the same dimension as "level"
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**: textbook legend (if any); and **adversarial review is invited to attack it**

### A1 · The count is recomputable (**knocked down**)

- **Claim (original)**: the textbook does label teaching hints tiered by learner level
- **Premise**: full extraction over 98 modules yields 649 markers (ev-020)
- **Reasoning (original)**: the source is raw files in a public repo, the extraction rule is clear, **anyone can re-run and check**
- **Evidence**: ev-020
- **Attacked**: **see the [attack entry](攻击/tieredguidance.en.md) — its A1–A4, all four hold**
- **Status**: **knocked down**
- **Attribution**: @hpleapfrog · 2026-10-05

> [!CAUTION]
> **A1 was knocked down as an "argument", not because the phenomenon it describes is false, but because its reasoning chain broke in two places:**
>
> 1. **"Recomputable" has no fulcrum in the repo** — ev-020 has neither script nor data, and
>    the filter "count only `os-teacher`" **is not written into the method**; a literal implementation necessarily gives a different number
> 2. **The domain of "649 tier markers" is not "level tiers"** — `[EL]` is a language identity;
>    and the four expansions **have no source in the repo**
>
> **The remaining part (re-asserted after narrowing, not yet argued):**
>
> > In the textbook's Teacher Support there **exist** `[BL]`/`[OL]`/`[AL]`/`[EL]` markers,
> > and they **point to different suggestions**.
>
> **This differs greatly from the original**: it does not assert "each tier exclusive", nor "the count is recomputable".
> **To make it an argument, one must add: the textbook legend original + extraction script + detail data + commit hash.**

> [!IMPORTANT]
> **The earlier callout originally wrote "A1 now has 15 `支持` edges" — the number is wrong.**
>
> Measured: **26** (during review it grew from 23 to 26, **still growing**).
> "**now has**" + a drifting number = **writing a snapshot as an assertion**.
> And that passage's assertion about the nature of the instances ("manually checked") hung on the base of 15 — **the extra 11 are not covered by it**.
>
> **`FORMAT.md` §6 even cited "kbcheck reports 15 supports" as a normative example — the normative document also carried a stale number.**
> Fixed together.

### A2 · ~~whether "tiering labels" equal "effective teaching"~~ → changed to a limitation note (not an argument)

> [!CAUTION]
> **This section was originally registered as `### A2` (an argument); that was a registration error.**
>
> Its "claim" said "these tiered suggestions are validated effective teaching",
> while its "reasoning" said "**one cannot infer that**" — **the reasoning negated its own claim**.
> As an argument it has **zero force**; nor does it form a valid rebuttal, because that claim was **never raised** in the body.

**Its reasoning itself is right and should be kept as a limitation note:**

These markers are **authoring suggestions** for teachers, **not conclusions of teaching experiments**.
Judging teaching effectiveness needs classroom-measured data — **the repo has none**.

## Why this entry matters to the repo

> [!CAUTION]
> **This section originally read**: "it turns 'different teaching for different people' from an idea into an **existing data structure** …
> **someone has already organized teaching content along the same dimension in a textbook**."
>
> **That sentence no longer stands.** Fact 1 shows the markers are **inline separators within a note**
> (79% of notes contain 2 or more markers), not a "data structure cut by dimension".
>
> **It does show the textbook writes different suggestions for different groups (this part holds)**;
> but it does **not** show the textbook organized its content into a "knowledge point × level" grid.

The repo's `教法` entries have two fields, `conditions` (audience) and `contraindications` (for whom it does not apply).
**The reasonableness of these two fields does not depend on this proposition** — they come from the repo's own design.
This entry **once** served as evidence that "the textbook already does this"; **that evidence is now gone**.

One point still holding: this is a **CC BY, freely reusable** corpus of teaching methods, usable as a source for `教法` entries.

## Limitations (must be stated clearly)

| Limitation | Note |
|---|---|
| **sample = 1 publisher** | this is one OpenStax practice, **not necessarily universal**; third-party textbooks are needed to generalize |
| **suggestion ≠ measurement** | the markers are authoring suggestions, with no effect size, no sample size |
| **coarse tiering granularity** | BL/OL/AL are coarse by "grade level"; the gap from real learner profiles is unmeasured |
| **very few EL samples** | only 5–6, insufficient to support any conclusion about English learners |

## To-do

- [ ] check whether third-party textbooks (人教版, or another publisher) have a similar tiering mechanism
- [ ] sample several modules and assess the practical operability of these suggestions
- [ ] if classroom-measured data can be found, supplement A2 with evidence beyond `ev-020`

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (statistical finding after full extraction of 580 teaching hints) | expanded collection | @hpleapfrog |
| 2026-10-05 | **A1 knocked down** (no fulcrum for recomputability, `[EL]` not a level tier, co-occurrence cannot yield attribution); **A2 re-registered as a limitation note**; removed the sourceless "meaning" column and "849 terms"; fixed "15 supports" → measured 26; status `待审` → **`失据`** | [AI adversarial review](攻击/tieredguidance.en.md) | AI subagent proposed · @hpleapfrog reviewed and re-ran three facts |
| 2026-10-05 | **supplied scripts, detail and commit hash** (`evidence/os-teacher-markers.py` + `.csv`); **added `A3`** (narrowed to "paragraph-level audience labels"); **numbers under two conventions** (strict 637 / loose 648) **both differ from the old claim 649, cause found to be `main` drift + written convention absent**; status `失据` → **`需复审`** | filling in the fulcrum hit by `A4` | @hpleapfrog |
