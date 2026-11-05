# Agent review: why the top splits in two instead of handing `已确证` to a machine

> 2026-11-05, the author decided: **a third person is no longer required.** One author plus one
> agent must be able to take an entry all the way. This record says how far, and why not all the way.

## 1. The problem: an unreachable ceiling, and a queue with no exit

| Fact | Number |
|---|---|
| `已确证` (confirmed) | **0** — it requires a non-author human, and the library has one contributor |
| `待审` (pending review) | 570 entries whose argument is written and whose evidence is read to full text; only a review is missing ([GAPS](../GAPS.en.md)) |

This is not a content problem. **`R-GRAPH-07` reports those entries' evidence floor as "full text"** —
everything the reviewer needs is already on the table. What is stuck is only *who signs*, and the rule
gave that pen to humans only.

## 2. Three options

| Option | Outcome | Why not / why |
|---|---|---|
| A. Let an agent write `已确证` | 570 confirmations tomorrow | **Worst.** The entire value of `已确证` is that no machine was involved. Let an agent grant it and it becomes indistinguishable from model output — a free top score is no score |
| B. Keep humans only | stays honest | Admits the library sits at 0 forever and the queue is dead weight. **Honest but useless** |
| C. **Add a separate rung, `已机审`** | machine review reachable and distinguishable | **Chosen.** Stronger than `暂定确认`, reproducible; weaker than `已确证` in exactly one thing — judgement. So it is not called confirmed |

## 3. Hard conditions for `已机审` (all machine-checked)

1. `## 机审记录` with **all four fields**: `模型` · `日期` · `引文核验` · `限制`;
2. **provenance tier = `T4`**: every cited source read in full (claiming "reviewed" without reading is
   reviewing your own memory of it);
3. an `## 论证` section (`R-SCHEMA-17`);
4. the `限制` field **must not be empty**: a review that cannot say what it could not judge is not a
   review. This is not a moral requirement — it is what makes the record usable to the next reviewer.

`R-SCHEMA-19` enforces 1–2 (and the argument requirement), with an injected failing sample in
`tools/verify_rules.py` ("writes 已机审 without a record").

## 4. What it does not do

- **No judgement.** A machine review answers only "does the source say this" and "does the conclusion
  exceed that passage". Discipline-specific applicability, textbook-system differences and teaching
  effectiveness go into `限制`, never into a conclusion.
- **No impersonation.** `llms.txt` requires `已机审` to be reported as "agent review, not human review".
- **No automatic promotion.** Turning an `已机审` entry into `已确证` still requires a second `@`
  signature; there is no automatic path between the rungs.

## 5. The first instance

[向心力不是一种新的力](../../knowledge/physics/claims/centripetal-is-not-a-new-force.en.md): `待审` → `已机审`.
Five English quotations, five hits (threshold 0.92, each 1.00), checked line by line against m54181;
the `限制` field lists three things **not** judged (whether PEP textbooks phrase it the same way,
whether Chinese teaching already treats centripetal force as a force kind, and the boundary of the
non-inertial-frame paragraph). **That is what the rule is supposed to look like: numbers where it can
check, prose where it cannot.**

## 6. When to roll this back

If `已机审` becomes a one-click pass — `限制` filled with platitudes, `引文核验` reduced to a number
with nothing to compare against — **the rule has failed and should revert to humans only**.
The test is simple: **open an `已机审` entry and see whether its `限制` names a specific thing that
was not judged.**
