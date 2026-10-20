# A mathematics subject, and "200 in one chapter" reached

> 中文：[calc3-ch6-errata.md](calc3-ch6-errata.md)

## Conclusion

On 2026-10-20 the repository added a "mathematics" subject (`id` prefix `math`, directory
`knowledge/mathematics/`) and ingested **all 308** Approved / Textbook errata in **Chapter 6**
(Vector Calculus) of OpenStax *Calculus Volume 3*. The project's minimal goal — "one chapter of
one textbook: 200 errata, the full path from 0 to 200" — is met here: **308 entries in a single
chapter, ≥ 200**.

This is a **structural change**, recorded separately from the 200-entry batch from Chapters 1–5 of
*University Physics Volume 1* (see [errata-200-scope.en.md](errata-200-scope.en.md)). The repository
did not relabel calculus as physics or science, did not edit the target, and did not count
`Not An Error` / `Duplicate` records.

## The data (snapshot of 2026-10-20)

- **Book**: *Calculus Volume 3* (OpenStax, book id 76); **Chapter 6**, Vector Calculus.
- **API**: `https://openstax.org/apps/cms/api/errata/?book_title=Calculus%20Volume%203&format=json`
  (public filtered view: `https://openstax.org/errata/?book=Calculus%20Volume%203`).
- **Filter**: `resolution = Approved` and `resource = Textbook` and `location` contains
  `Chapter 6`; the 308 records are every matching entry in that chapter.
- **Snapshot**: [`evidence/calc3-ch6-errata-308.json`](../../evidence/calc3-ch6-errata-308.json),
  SHA-256 `180047c8a52ff3944e04e4791638ff46609d6b7fbb1e3be00ca14439542671d3`.
- **Evidence**: `ev-152` (publisher errata list · high · full text).
- **Composition**: typo 138 · answer/calculation 78 · factual inaccuracy 53 · accepted pedagogical
  suggestion 36 · Other 2 · broken link 1. **36 are teaching suggestions**, not "wrong text"; each
  entry's Nature section states this.
- **Status**: all 308 Approved; Completed 306 / Reviewed 2; **298 are archived** (no longer shown in
  the public filtered list, but their permanent pages and the API remain verifiable), and 305 have a
  `corrected_date`. Records were created between 2016-12-08 and 2026-05-04.
- **License**: the textbook is **CC BY-NC-SA 4.0**
  ([`osbooks-calculus-bundle/LICENSE`](https://github.com/openstax/osbooks-calculus-bundle/blob/main/LICENSE));
  the repository stores locators and short quotes only, never the textbook text or scans.

## The structural change

1. [`tools/kbcheck.py`](../../tools/kbcheck.py): `SUBJECT_SLUGS` (`math`), `SUBJECT_DIRS`
   (`mathematics`), `SUBJECT_NOTES` / `SUBJECT_NOTES_EN`, `SUBJECT_ORDER`, `SUBJECT_EN`.
2. [`tools/new_entry.py`](../../tools/new_entry.py): subject registries and help text.
3. [`docs/RULES.md`](../RULES.en.md): the `id`-prefix table in `R-SCHEMA-11` gains
   「数学→math」 ([Chinese](../RULES.md)).
4. New `knowledge/mathematics/` directory with bilingual READMEs and 308 entry pairs
   (616 files).
5. [`tools/import_openstax_errata.py`](../../tools/import_openstax_errata.py): hard-coded physics
   replaced by `up1` / `calc3` profiles; added the `Broken link → 链接失效` mapping.
6. Evidence registration `ev-152` and the snapshot.

**Regression**: regenerating the existing 200 entries with the `up1` profile produced
**byte-identical** SHA-256 hashes for all 400 Chinese/English files; `--verify` is still 200/200.
**Check**: `calc3 --verify` is 308/308 (bilingual entries, quotes matching the snapshot, README
registration); see "Reproducible" below.

## What each entry claims

Each entry claims only that "the publisher recorded and accepted this erratum" and gives the
correction the publisher says should be made. It does **not** claim that the current web text still
shows the error, nor that this repository independently reviewed the text. Of the 308, 36 are
teaching suggestions, 2 are Other and 1 is a broken link — not the same kind of "error"; each entry's
Nature section keeps them apart.

## Reproducible

```bash
python tools/import_openstax_errata.py --profile calc3 \
    --snapshot evidence/calc3-ch6-errata-308.json --verify
```

Output: `校验 308 条：中英条目 308/308 · 引用与快照一致 308/308 · README 登记 308/308`.
The importer defaults to dry-run; `--write` is idempotent by filename and can be rerun. The
correspondence between snapshot, entries and README rows is not hand-copied.

## Consequences

1. **The minimal goal is met**: 308 entries in one chapter, and the 0→200 path (snapshot → import →
   bilingual entries → evidence registration → subject README → `kbcheck`) is reproducible. The
   earlier five-chapter 200-entry batch remains recorded as it was.
2. **"Five-minute entry cost" is still unanswered.** Batch import bypasses per-entry human argument;
   it suits source-authority errata, not ordinary knowledge points.
3. **`已确证` is still 0.** It requires an independent review by a non-author and cannot be produced
   honestly by a single contributor.
4. **The mathematics subject currently covers this one chapter only.** Both the subject note and the
   README state the scope; do not read "a mathematics subject exists" as coverage of all calculus, and
   still less as a general claim about textbook quality.
