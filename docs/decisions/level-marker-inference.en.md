# The expansion of `水平档` is inference, not quotation

> Rule: [FORMAT.md](../../FORMAT.en.md) "What `水平档` records".

## The four abbreviations have no legend in the textbook

Measured (script and details in [`evidence/os-teacher-markers.py`](../../evidence/os-teacher-markers.py)):

- `Below Level` appears **only once** in the whole book (and in prose);
- `Advanced Learners` **never**;
- only `English Learners` has corroboration (in m54057, `[BL][EL]` is immediately followed by `English learners may need…`).

> **So "`[BL]` = below grade level" is an inference about common educational abbreviations, not a quotation.**
> **The repo's `(知识点 × 水平档)` model rests on this inference.**

## `[EL]` is not a level marker

**`[EL]` (English Learners) is a language identity, not a level marker** — do not list it alongside the other three as a "leveling marker".

## The statistical measure must be given with the rule and the commit

The same source file gives different results under two measures:

| Measure | Meaning | Result |
|---|---|---|
| **loose** | the string appears in `os-teacher` note text | 648 (BL 207 / OL 245 / AL 191 / EL 5) |
| **strict** | the markers are consecutive `<span>` starting a `<para>` | 637 (EL **0** — it is often bare text) |

> Same lesson as `ev-020`: **hard-coding a drifting number turns it into an assertion.** Give the number together with rule + commit.
