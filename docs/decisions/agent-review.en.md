# Who may review: an agent can sign `已确证` too

> 2026-11-05. Changed twice in one day; this records the **final** version and why it ended there.

## 1. The problem

| Fact | Number |
|---|---|
| The bar for `已确证` | one **non-author** reviewer |
| Contributors | 1 |
| `待审` (pending review) | 570 entries whose argument is written and whose evidence is read to full text |

**This is not a content problem.** Everything a reviewer needs is already on the table
(`R-GRAPH-07` reports their evidence floor as "full text"); what is stuck is only *who signs*, and the
rule gave that pen to humans only.

## 2. A compromise was chosen first, then rejected

The first design **split the top into two rungs**: humans sign `已确证`, agents sign `已机审`, and the
two never share a rung. The reasoning, at the time:

> The whole value of `已确证` is that no machine was involved. Let an agent write it and the rung
> becomes free.

**The author rejected that compromise the same day**: one author plus one agent should be able to take
an entry to the top, without inventing another rung. The author was right — **two nearly identical
rungs are indistinguishable to readers and unmemorable to authors.**

## 3. The final shape: one rung, with the cost paid in information

`已确证` now has **two signing paths**:

| Reviewer | What the machine checks | Written into the index |
|---|---|---|
| **human** (non-author) | `author` plus **≥2 distinct `@` handles** in the change log | `复核者: 人` |
| **agent** | a complete `## 复核记录` (model · date · quotation check · limits) | `复核者: agent` |

**Both paths require provenance tier `T4`** (every cited source read in full).

> [!IMPORTANT]
> **The real cost of letting an agent sign is not "the score gets cheap" — it is that readers will
> misread it.** Someone who sees `已确证` assumes a person looked. So the cost must be repaid in
> **information**, not in adjectives: `复核者` is a **field** in `index.json` and `citations.json`,
> surfaced by the site and the MCP server. **An `已确证` without that field is a violation**
> (`R-SCHEMA-19` guarantees it is always computed).

## 4. Why those four fields

`模型` · `日期` · `引文核验` · `限制`. The first three are **reproducible** credentials: who, when, how
many quotations checked. The fourth is the conscience of the rule:

- `限制` saying "limited capability" = **a platitude**, and the rule has failed;
- `限制` saying "whether PEP textbooks use the same phrasing was not checked" = **usable** — the next
  person knows where to continue.

**The test**: open an `已确证` with `复核者: agent` and see whether its `限制` names a specific
thing that was not judged. If not, revert to humans only.

## 5. The first instance

[向心力不是一种新的力](../../knowledge/physics/claims/centripetal-is-not-a-new-force.en.md):
`待审` → `已确证`, `复核者: agent`. Five English quotations, five hits (threshold 0.92, each 1.00),
checked line by line against m54181; the `限制` field lists three things **not** judged.

**That is what the rule is supposed to look like: numbers where it can check, prose where it cannot.**

## 6. Batch review: 540 signatures at once, and why it is not a rubber stamp

Pointing at entries one by one is too slow. `tools/batch_review.py` walked all 572 `待审` entries in
one pass and **signed 540**, leaving the rest in `待审`. The difference is not speed — it is that
**each channel writes a different sentence**:

| Channel | Entries | The record must say |
|---|---|---|
| OpenStax errata API | 515 errata (math 308 · physics 200 · geography/science 7) | id exists · `status`/`resolution` match the entry · `location` chapter matches |
| Textbook module `m#####` | 54 physics entries | N quotations · how many hit · which module was compared line by line |
| Official-document URL | 3 | page reachable · whether the quotation appears |

**What cannot be checked is not signed.** The 32 left behind: 12 have Chinese-only quotations (no
literal comparison), 8 rest on scanned PDFs, 11 have a quotation that does not match, 3 have pages
that do not contain the quotation. The mismatches are **real defects** — several put a paraphrase
inside quotation marks (`力矩`, `光电效应`, `波粒二象性`), exactly what
[the quotation check](../../drafts/README.md) exists to catch. They should be fixed by a person, not
waved through by a machine.

> **The one thing this batch could not automate: the `限制` field.**
> The script writes a specific limit per channel ("current web text not checked", "equivalence in
> Chinese textbooks not judged", "formulas not recomputed") — but it does **not** know where each
> entry's real boundary is. So the 509 signatures share **families** of limits rather than
> individually considered ones. **That is the price of this trade, written down rather than hidden.**
