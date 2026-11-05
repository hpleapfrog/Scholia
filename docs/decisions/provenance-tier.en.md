# Provenance tier: why `status` needed a second ruler beside it

> 2026-11-05. This did not start as a design. It started as a **reading accident**.

## 1. The bad news first: the library's most important number was unreadable

Run `python tools/kbcheck.py` and the status table tells you two things:

```
已确证 / Confirmed      0
待审 / pending review   573
```

Both are true. Together they get read as something false: **"nobody has checked any of this."**

On 2026-11-05 I audited the whole library, taking every object's cited evidence and reducing it to
its **weakest link** by `核验深度` (verification depth):

| How far it was read | Objects | Share |
|---|---:|---:|
| `全文` (every cited source read end to end) | 733 | 98.3% |
| `摘要` (abstract) | 5 | 0.7% |
| `仅定位` (checked that the passage exists, not read) | 8 | 1.1% |
| `未核验` / no basis | 0 | 0 |

**738 of 746 objects (99%) rest on sources that were actually read.** That number existed all along;
**nothing displayed it.** The `status` column holds "is there an argument that survives attack",
which needs a human — and there is only one.

So the library was doing something self-harming: **hiding its strongest evidence (the reading) and
reporting only its weakest conclusion (nobody reviewed).**

## 2. Why not a seventh `status`

The cheap move is `status: 来源已核` (source verified). **No** — for the same reason voting was
rejected as a truth mechanism:

- `status` is a **truth tier**: "does this claim currently stand?" A human must give it, and
  `已确证` explicitly requires **non-author** review (`R-SCHEMA-19`).
- "the source was read" is a **verifiability tier**: "can you follow this to the end?" A machine
  can compute it.

Folding both into one field makes a computed value look like a human judgement — exactly the
confusion this library exists to avoid (see [status-zero-is-auditable.md](status-zero-is-auditable.en.md)).
So it is a **second, parallel ruler** called the provenance tier, written into `index.json` and
`citations.json`, **never into front-matter** (a hand-written derived value drifts, and being correct
is the entire point of this dimension).

## 3. Why the weakest link

| Aggregation | Result | Problem |
|---|---|---|
| **best** cited source | 733 at full marks | five sources, four read, one merely located — still full marks; the reader who follows the thin one hits a wall |
| **average** | 3.9 / 4 library-wide | same, with the wall smeared out of sight |
| **weakest** | 733 / 5 / 8 | matches what a reader actually experiences: **a chain is as strong as its thinnest link** |

This is the other half of `R-GRAPH-06`: that one says "the same source repeated 42 times is not 42
pieces of evidence"; this one says "four of five sources read is not read".

## 4. Boundaries: it endorses nobody

- **T4 ≠ correct.** It says the source was read, not that the conclusion holds. Attack, review and
  `已确证` never pass through it.
- **T2 ≠ fabrication.** "Located only" is an **honest record**, not an accusation — many entries only
  need "this page really says this".
- **It cannot be obtained by editing a field.** It is recomputed from `核验深度` in
  `evidence/README.md`, and only someone who read the source can write that (the three source
  questions in `M-11` are still answered by a human).

## 5. Cost

| Item | Change |
|---|---|
| `index.json` | `schema_version` 5 → 6, one `溯源` per object (4 bytes) |
| `citations.json` | `schema_version` 2 → 3, one `溯源` in the citation kit |
| `docs/GAPS.md` | one more group: "provenance below T4", listing **which evidence** drags it down |
| Rules | **none added.** It is derived; `R-INDEX-01/02` already guarantee it cannot go stale |

**No new human labour.** That is why it can stay.

## 6. What this means for "does the project still deserve to exist"

As of 2026-11-05: 1 star · 0 forks · 1 contributor · **0 confirmed** · the "5 minutes per bilingual
entry" gate measured at 12–13 minutes ([entry-cost-phases.md](entry-cost-phases.en.md)).

Measured by **entry count**, the project is losing: authoring cannot outrun the gap, and a 570-item
review queue only grows.

Measured by **verifiability**, it holds something nobody else has: **746 entries where 99% of
sources were read, each recording how far.** That is not "yet another knowledge base"; it is a
**checkable citation contract**. It also explains why `已确证 = 0` is not a failure: **the missing
link is a human, not the reading.**

So the conclusion is not "keep piling up entries". It is two things:

1. **Turn what exists into something others can use**: export the 515 textbook errata as one table
   (`exports/errata.csv`) — teachers and textbook editors need no Git and no spec to use it.
2. **Make a stranger understand it in 60 seconds**: one generated page (`tools/build_site.py`) that
   puts `status` and `溯源` side by side on every entry — **both rulers must be visible; either one
   alone misleads.**

**The metric that decides whether this project continues is not entry 747. It is the first
non-author.** Until then, "add another subject" and "add 300 more errata" only push the problem back.

> [!NOTE]
> **Later the same day (2026-11-05)**: "0 confirmed" above is the reading **at the moment of the
> audit**. A few hours later the reviewer no longer had to be human, and the first `已确证` was signed
> by an agent (`复核者: agent` in the index) — see [agent-review.md](agent-review.en.md).
> **The conclusion is unchanged**: what is missing is people, not reading; what changed is that
> "no third person means nothing reaches the top" is no longer true.
