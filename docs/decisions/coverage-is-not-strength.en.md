# Coverage measured "is it there": then two more dimensions of "is it enough"

> Open item: [README](../../README.en.md), second half of item 4 of "Open questions that matter".
> Rules: [FORMAT.md](../../FORMAT.en.md); path structure: [knowledge/README.md](../../knowledge/README.en.md).
> Recorded 2026-10-20.

Paths used to be checked on one dimension only: **whether each declared learning outcome `o1…on` is covered
by at least one row of `## 编排`** (`R-GRAPH-03`). That catches "the goal is written but the lesson never
teaches it". It cannot catch **"the lesson teaches it once"** — and once is exactly the pedagogically risky
case: if that one step misfires, there is no second attempt. Two dimensions of "enough" **are** computable,
and both were added (`R-GRAPH-07`):

| Dimension | How it is computed | What remains a human judgement |
|---|---|---|
| **Redundancy** | how many 编排 rows cover each outcome; `≤1` is reported | whether two passes are enough |
| **Whether it was read** | the **maximum verification depth** of the evidence behind the covering entries; `仅定位` / `未核验` is reported | whether this source was the right one |

## Measured across the library (4 paths · 15 outcomes)

| Path | Coverage | Outcomes covered by a single step |
|---|---|---|
| [Gravitation and the sky (high school)](../../knowledge/physics/paths/gravitation.en.md) | 3/3 | `o1` `o3` |
| [Forces and motion (high school)](../../knowledge/physics/paths/forces-and-motion-hs.en.md) | 4/4 | `o3` `o4` |
| [Work, power and mechanical energy (high school)](../../knowledge/physics/paths/energy-work.en.md) | 4/4 | `o1` `o2` `o3` `o4` |
| [Kinematics intro (below grade level)](../../knowledge/physics/paths/kinematics-intro-bl.en.md) | 4/4 | `o2` `o3` `o4` |

**All 15 outcomes are "covered", and 11 of them (73%) are taught exactly once.** The gap between "is it
there" and "is it enough" is not wording — it is 73% of the sequencing.

The second dimension currently reports **nothing**: behind the 11 single-step outcomes, the maximum
evidence depth is `全文` in every case. That is a genuinely clean result, not an unchecked one — but it
also exposes how little resolving power that dimension currently has: `全文` says **the source was read**,
not **the outcome was taught well**.

## The first implementation was **falsely clean** — that is the point of this record

The first version read outcome ids **only from the last column** of the table. Three of the four paths do
have 覆盖 as the last column, so they reported single-step coverage normally.
[Kinematics intro](../../knowledge/physics/paths/kinematics-intro-bl.en.md) uses
`| # | 环节 | 条目 | 覆盖 | 时长 |` — **its last column is duration**. Those rows never yielded an `o\d+`,
`steps` stayed empty, and so did `thin`.

> [!WARNING]
> **A path was reported as "no redundancy problem" because the checker could not read its table.**
> After fixing the column handling it reports `o2` `o3` `o4` as single-step — **the check's original
> conclusion was wrong, and it was wrong on the "all clear" side.**
> This is not an abstract lesson: **any positional column parser silently degrades to zero warnings the
> moment the parsed document reorders its columns.** The fix here scans **all** cells, and the reason is
> written into the code comment: *a false all-clear is worse than no check*.

> [!CAUTION]
> **`sample_graph07` did not catch this bug.** The injected sample tests the evidence-depth dimension,
> and the table it uses happens to be one of the three with the correct column order.
> **This bug was found by a human reading all four tables.**
> So: injected samples prove **that a check can fail**; they do not prove **that the check understands
> every input shape**. The first is machine-checkable and is the floor; the second is still human work.

This is the third error of the same family in this repository (the previous two: an invented section
number, and an example entry mistaken for evidence — see [evidence-history.md](evidence-history.md)).
What all three share is a **silent** failure mode. Hence the acceptance criterion for a new check here is
not "it ran" but **"someone verified that it fails"** — an injected sample in
[`tools/verify_rules.py`](../../tools/verify_rules.py), visible in [docs/RULES.md](../RULES.en.md) as the
difference between ✅ and `—`.

## A sample that watches the *input shape*, plus the measured blast radius

The WARNING above admits that injected samples missed the column bug. Admitting it is not enough — the
rule here is "every machine-checked rule ships with a sample that fails", so **that branch** now has one
too: `sample_graph07b` finds a path whose 覆盖 column really is last, **appends a column** to the whole
table (pushing it off the end), and inserts an outcome `o9` covered by exactly one new step. The assertion
is `'o9']`, not a bare `o9`: what must be proven is "*o9* appears at the **end of the single-step list**",
not "these two characters appear somewhere in the output".

**And it was not just written and counted as done.** On 2026-10-20 the outcome-extraction in
`kbcheck.py` was **reverted to the first version** (scan `cells[-1]` only) and the same sample was run
against a throwaway copy:

| Implementation | Sample result | Paths reporting single-step coverage |
|---|---|---|
| Current (scans all cells) | **PASS** | 4 / 4 |
| Reverted to positional | **FAIL** | **2 / 4** |

> [!IMPORTANT]
> **The blast radius is larger than the first version of this record stated.** It said "one path —
> kinematics-intro-bl — was read as clean". The revert experiment shows that **the moment the column order
> changes, the number of silent paths goes from 1 to 2** (the injected gravitation path also went silent).
> So the accurate description of the bug is not "one unusual table" but
> **"every path whose last column is not 覆盖 reports all-clear"**. Only 1 of 4 paths qualified at the time,
> which is why reading the tables by hand was just barely enough. And appending a column after 覆盖 is the
> **natural** way to widen a table (add a duration, add a note): **each such edit silences one more path**.
> In this experiment a single edit took the count from 1 of 4 to 2 of 4.

## Still open

- [ ] Redundancy counts **rows**, not real second exposures: a repeated reference to the same step inflates it
- [ ] "Maximum evidence depth" takes the **union maximum** over covering entries — one `全文` source hides the
      other outcome's `仅定位` bases
- [ ] `sample_graph07b` guards only **this** shape. Other positional reads inside the self-test harness were
      converted to scan-all-cells for the same reason, but a shape sample per parser is not how this scales —
      the durable fix is "never index a Markdown column by position"
- [ ] The front door to pedagogical "enough" is **pre/post test data**, which this library does not have
      (see the matching gap in [textbook built-in tiered variants](../../knowledge/physics/claims/textbook-tiered-guidance.en.md))
