# Decision record: `事件` (events) kept apart from `命题` (propositions)

> **中文: [events-are-not-propositions.md](events-are-not-propositions.md)**

**The rule lives in [FORMAT.md §4 "事件"](../../FORMAT.md)**; this file records the **why**.

## Origin

A real need: **record events as they happen** (the first being the October 2026 death of a worker at the
Irkutsk Anti-Plague Institute), and **have the record maintained and updated over time**.

My first attempt was to **force it into `命题`** — on the reasoning that "of the existing types,
a proposition is closest".

## Why forcing it into a proposition is wrong

A proposition's core structure is `陈述` + `依据` + **`论证`** + `变更记录`, with a `status` of
`已确证` / `已推翻` / `失据` — all built around **a claim that can be attacked**.

An event **has no attackable claim**. Writing "body X published notice Y on date D" as a proposition:

- its `论证` section **has no attack point** — "it really was published" holds by **date and source**, not by argument;
- its `status` has no sensible value — it is neither "confirmed" nor "overturned";
- the result is **a fake argument with no attack points**. **That is exactly the noise this repo filters out.**

More fundamentally: **a proposition answers "what is true" (truth value, attacked/defended, converges);
an event answers "what happened" (a time-indexed fact, evidence only). They are different things.**

> [!IMPORTANT]
> **Writing an event as a proposition manufactures fake structure to fit the existing machinery.**
> Once a single source holds both "attackable claims" and "facts that happened", compressing them into one
> type mixes real arguments with fake structure, and **the reader can no longer tell which part is attackable.**

## Decision

**`事件` is not a seventh object type; it is a second kind of record, parallel to `objects`, top-level in `events/`.**

| Item | `事件` | `命题` (for contrast) |
|---|---|---|
| Location | top-level `events/` | `knowledge/<subject>/命题/` |
| Answers | "what happened" | "what is true" |
| `status` | `持续更新` / `已封存` | `已确证` / `已推翻` / `失据` … |
| Required sections | `陈述` · `依据` · `变更记录` | `陈述` · `依据` · **`论证`** · `变更记录` |
| Edges | **none at all** | `先修` / `支持` / `攻击` |
| `evidence` | **must be non-empty** (an event needs only evidence) | must be non-empty |
| `index.json` | its own `事件[]` section, **not in `objects`** | in `objects[]` |

**Why top-level and not under `knowledge/<subject>/`**: events are often **cross-disciplinary**
(a plague event is both medical and political), and their organising axis is **time**, not subject.
Filing one under a subject would force it to pick a side and detach it from the update-by-time workflow.

## Red lines (verified by failing injection samples)

- missing `陈述` → fails
- empty `evidence` → fails
- `status` using a proposition status (e.g. `已确证`) → fails
- carrying `edges` → fails
- `id` prefix not `kb:event:` → fails

Samples are verified in a **temp copy**, not committed (see [CONTRIBUTING "rule admission threshold"](../../CONTRIBUTING.md)).

## Unavoidable costs

1. **A second status vocabulary.** `持续更新` / `已封存` sit alongside the proposition statuses;
   readers must remember two more words — **in exchange, "review status" and "event status" are no longer
   squeezed into one field.**
2. **`事件` enters no subject statistics.** The subject table in `knowledge/README.md` gets one extra row
   "事件（顶层）" at the end, while `对象总数` still counts knowledge objects only. **The two numbers sit
   side by side; neither swallows the other.**
3. **No version detection.** Events are extended by hand in time order; the repo still has no
   "warn when a source changes" mechanism (a known gap, not introduced by this decision).
