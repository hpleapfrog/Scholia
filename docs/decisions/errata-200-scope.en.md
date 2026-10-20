# Why the 200 errata are not "one chapter"

> 中文：[errata-200-scope.md](errata-200-scope.md)

## Conclusion

On 2026-10-20 the repository ingested **200** Approved / Textbook errata from Chapters 1–5 of
OpenStax *University Physics Volume 1*. The scale target "0 → 200" was reached for the first time.

**But "200 in one chapter" was not reached.** In the public OpenStax errata data, **no chapter in a
registered subject has 200 entries**. The repository chose **not to fake it**: it did not relabel a
calculus textbook as physics, did not count `Not An Error` / `Duplicate`, and did not quietly rewrite
"one chapter" as "one book".

## The data (snapshot of 2026-10-20)

OpenStax public errata API: `https://openstax.org/apps/cms/api/errata/?format=json`
(115 books, 30,155 records; 20,169 `Approved`). With
`resolution = Approved` and `resource = Textbook`, the largest single chapter is:

| Textbook | Largest chapter | Note |
|---|---|---|
| Calculus Volume 3 | **308** (Chapter 6) | mathematics; **not used for this batch** (adopted the same day in a separate structural change, see the [follow-up record](calc3-ch6-errata.en.md)) |
| Biology 2e | 55 (Chapter 29) | science; still below 200 in one chapter |
| University Physics Volume 1 | 51 (Chapters 2 and 3) | physics; the source of this batch |
| Chemistry 2e | 46 (Chapter 1) | science |
| College Physics 2e | 32 (Chapter 13) | physics |

> **Why not simply use Calculus Volume 3, Chapter 6 for this batch?**
> It does have 308 entries, but it is a mathematics textbook; at the time the repository's subject
> registry had no "mathematics" entry (`SUBJECT_SLUGS` in `tools/kbcheck.py`), and changing the
> registry was outside this content batch. Filing calculus under "physics" or "science" would
> falsify both the subject statistics and the `id` prefixes — worse than missing the number.
>
> **On the same day, 2026-10-20, the repository added a mathematics subject in a separate structural
> change and ingested those 308 entries**; see [calc3-ch6-errata.en.md](calc3-ch6-errata.en.md).
> This batch remains recorded as spanning five chapters.

## What this batch actually is

- **Scope**: **all** Approved / Textbook errata in Chapters 1–5 of *University Physics Volume 1*
  (31 + 51 + 51 + 48 + 19 = 200).
- **Source**: every entry has a public permalink `https://openstax.org/errata/<id>`; the sanitised
  snapshot is [`evidence/openstax-up1-errata-200.json`](../../evidence/openstax-up1-errata-200.json),
  SHA-256 `2cdba573f779d571cbc34e500fbbc96d61b6e75c3d97c1b365c6e399c1f89da7`.
- **Evidence**: `ev-150` (publisher errata list · high · full text).
- **Composition**: typo 75 · answer/calculation 49 · accepted pedagogical suggestion 42 ·
  factual inaccuracy 25 · unclassified 5 · other 4. **42 are teaching suggestions**, not
  "wrong text"; each entry's Nature section states this.
- **Status**: all 200 are Completed / Approved; **196 are archived** (no longer listed in the
  public filtered view, but their permanent pages and the API remain verifiable), and 193 have
  a corrected_date.
- **Spot check**: on 2026-10-20 the archived records #3502 and #28659 were opened in a browser;
  their permanent pages resolved and matched the location, type and description of the generated
  entries. This checks reachability, not independent content review.
- **Process**: snapshot → [`tools/import_openstax_errata.py`](../../tools/import_openstax_errata.py)
  → 200 bilingual entries + subject README rows. `--verify` checks quoted text, zh/en pairing and
  README registration offline (currently 200/200). The step is **reproducible**, not hand-copied.

## Consequences

1. **This batch spans five chapters and is not passed off as "one chapter".** The project-level
   "200 in one chapter" was reached the same day by the mathematics batch
   ([calc3-ch6-errata.en.md](calc3-ch6-errata.en.md)); the true scope of this batch is kept here
   rather than used to pad the target.
2. **"Five-minute entry cost" is still unanswered.** Batch import bypasses per-entry human argument;
   it suits source-authority errata, not ordinary knowledge points.
3. **Each entry claims only that "the publisher recorded and accepted this erratum".** 196 of the 200
   are archived and no longer appear in the public filtered list, but their permanent pages and the API
   remain verifiable; the entries do not claim that the current web text still shows the error.
4. **Nothing non-errata was used to pad the count.** `Not An Error` (3,789), `Duplicate` (3,345) and
   Tutor / assessment records were excluded.

## Follow-up (completed the same day, 2026-10-20)

Following the recommendation below, the repository added a "mathematics" subject in a **separate
structural change** (`SUBJECT_SLUGS` / `SUBJECT_DIRS` / docs / `RULES` / `new_entry`) and imported
all 308 entries from Calculus Volume 3, Chapter 6 with the same importer's `calc3` profile. The
change, regression and verification are recorded in
[calc3-ch6-errata.en.md](calc3-ch6-errata.en.md); the 200 files in this batch were unaffected
(regenerating with `up1` left all 400 files byte-identical).
