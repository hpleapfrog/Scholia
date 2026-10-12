# Evidence: a few incidents and inferences

> Policy and index: [`evidence/README.md`](../../evidence/README.md).
> This file holds only the **full account of the incidents and inferences** — the rules stay in evidence/README, the reasons stay here (**moved, not deleted**).

## I. The locator must be verifiable: the section numbers were invented

**The repo made this mistake once, and systematically: the section numbers were invented.**

40 files carried section numbers like `§16.1` / `§7.2` / `§22.1`. Measured against the OpenStax repo:

| Check | Result |
|---|---|
| `number=` in `collections/physics.collection.xml` | **0 occurrences** |
| same, `label` | **0 occurrences** |
| module `index.cnxml` `<title>` | **bare titles** (`Reflection`), no section numbers |

**The section numbers are not in the source files at all.** Those numbers were inferred from **module order**, and **the internal conventions contradict each other**:

| Chapter | Module order | The repo once wrote | Implied convention |
|---|---|---|---|
| 7 | Introduction · Kepler · Newton | Kepler = `§7.2` | Introduction **counts as** 7.1 |
| 16 | Introduction · Reflection · Refraction · Lenses | Reflection = `§16.1` | Introduction **does not count** |

**Two opposite conventions — which by itself proves they were guesses.**

> **Matching ≠ exact.** The **printed** textbook does have section numbers, but they are **not in the source file we read**.
> **Writing a number we cannot verify is forging a locator** — even if it happens to be right.

## II. Registering constructed data as "experimental data" (`ev-002`)

**`ev-002` is voided.** It was once the repo's **highest-graded** evidence, yet **no measurement ever took place**.

| | ev-002 as written | Actual |
|---|---|---|
| type | **experimental data** | **constructed by the repo author** |
| grade | **high** | —— |
| locator | `导体U-I数据.csv` (recomputable) | values are `U = 10 × I`, **R exactly 10.000** |
| date | 2026 | same year, same author |
| entries citing it wrote | "current **measured** across voltages for the same conductor, **temperature 20 °C**" | **no measurement, no temperature control, the CSV has no temperature column at all** |

It was meant to **replace** the earlier batch of fictional examples (`ev-009`~`ev-012`). **What went in its place was the same kind of thing, only dressed to look more like evidence.**

### Why it fooled everyone (including one adversarial review)

One AI adversarial review did examine the proposition citing it, and **accurately** pointed out:

> The data resolution is insufficient — current is recorded only to `0.01 A`, which at `I=0.10` is **5%**, so it **cannot distinguish** "Ohmic" from "4.4% drift".

**That is a symptom, not the root cause.** The root cause is **the data is not a measurement at all**.

**And the adversarial review did not check this, because the repo told it not to.** The dispatch instruction was:
"You don't need to verify whether the quotation is true (that needs the network); you may assume the quotation is true; what you attack is 'even so, does the conclusion hold'."
**I myself had excluded "verifying whether the evidence really exists" from the adversarial scope.**

**The fix (now in [FORMAT.md §6](../../FORMAT.en.md))**: the adversarial task must **explicitly include** the line
"question whether the evidence exists as described". A logic attack and truth verification **are not the same thing**; you cannot skip the latter just because the former is cheap.

## III. Why an official document is graded "high" (`ev-043`)

The repo's ladder (systematic review > RCT > cohort > case report > expert opinion > textbook) is **designed for empirical propositions**.
For a claim about "**what an official document stipulates**", the **official original is the primary source** — it does not queue on the ladder.

| | ev-002 (voided) | **ev-043** |
|---|---|---|
| reason for high grade | "**recomputable**" | "**this is the officially published original**" |
| what it actually is | **data constructed by the repo author** | **a clickable official page** |
| who asserts it | the repo itself | **Beijing Municipal Transport Commission** |

**"Recomputable" solves "can I verify it", not "what is it". And "official original" solves exactly the latter.**

## IV. The ladder is unfair to physics (`ev-048`)

**`ev-048` is the repo's first top-grade evidence, and it exposed a problem with the ladder.**

The repo's ladder reads: systematic review / meta-analysis > **randomized controlled trial** > cohort > case report > expert opinion > textbook.
**This ladder is designed for "empirical propositions about populations"** (the shape of medicine and social science).
Before it appeared, **37 of the repo's 40 evidences were textbooks, 3 were official documents** — **the top four tiers had never been used.**

**The problem is not that no one used them, but that the ladder is unfair to physics**: an `F = ma` written in a textbook falls to the **lowest tier** by this table;
yet it is **nothing like** "a teaching suggestion in a textbook".
**A physics fact needs no randomized controlled trial to support it, and this table cannot say that difference.**

**This is a known issue, not changed in this round** (the repo's rule: don't change structure on one sample).
**Remember it: `physics` needs a different standard of evidence, not a forced fit onto this table.**
