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
