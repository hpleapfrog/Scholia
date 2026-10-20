# Why "15 supporting edges" is the wrong way to write it

> Rule: [FORMAT.md](../../FORMAT.en.md) §6 "The number of `支持` edges does **not** indicate strength".

The body of the proposition "教材内建分组教学变体" once wrote "A1 **now has 15** supporting edges",
while the measurement showed **26 and still growing**. **"now has" + a drifting number = writing a snapshot as an assertion.**
That proposition's A1 was therefore hit by [an attack](../../knowledge/physics/claims/attacks/tieredguidance.en.md).
**The spec itself once quoted this number as an example — also fixed.**

| Looks like | Actually |
|---|---|
| 26 supporting edges ⇒ strong evidence | ❌ **the same source repeated 26 times** |
| 3 supporting edges ⇒ weaker evidence | ✅ if from 3 different countries/publishers, **stronger than those 26** |

**The criterion for independence is the source, not the count.** `kbcheck.py` reports the in-edge count with a reminder —
**but it cannot compute independence** (source attribution is free text). **This must be judged by a human.**

## 2026-10-20: half of that sentence was wrong

The line above stayed untouched for too long, long enough to start looking like **an exemption that
nobody audits**. Split apart, it contains two halves — one genuinely needs human judgement, the other was
**pretending to be uncomputable all along**.

| The half | Machine-checkable? | How it works now |
|---|---|---|
| **Same source identifier** (several `支持` edges whose evidence sits inside one identifiable source) | ✅ **yes** | `R-GRAPH-06`: for arguments with ≥2 inbound edges, take the union of evidence ids and the set of source identifiers |
| **Whether different sources are truly independent** (do two publishers' books count as independent?) | ❌ still human | belongs to `M-03`; the machine only lays out the **composition** |

A "source identifier" is **not** a judgement about content; it is **one way of cutting the locator string**:
take the 《title》 part, otherwise fall back to the leading token before the first separator, otherwise
record `（未识别）`. So its output must be read literally: **`（未识别）` does not mean "independent"** — that
half returns to a human (`M-03`).

Run over the whole library, the result is worse than expected:

```
! 教材内建分组教学变体.md: argument a3 has 42 支持 edges, 21 pieces of evidence,
  but only 1 source identifier (OpenStax《Physics》) —
  they are 21 positions in the same material, not 21 independent sources (R-GRAPH-06)
```

**After this library wrote the sentence "26 supporting edges is the same source repeated 26 times", the
count grew to 42 edges over 21 positions — still all from one book.** That warning used to require a human
to notice. Now it is computed for every such anchor, and someone has verified the check fails
(`sample_graph06` in [`tools/verify_rules.py`](../../tools/verify_rules.py)).

> [!IMPORTANT]
> **Still do not put the count in the body** — it drifts. If anything goes in the body, put the
> **composition**: "how many edges · how many pieces of evidence · how many source identifiers".
> The last two are the newly checkable quantities.

