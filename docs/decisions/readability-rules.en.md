# The three learner-facing rules: origin

> Rules: [FORMAT.md](../../FORMAT.en.md) "Learner-facing readability".

**These three were added 2026-10-05, prompted by one piece of criticism: "This repo can be seen by beginners, and they can easily learn what they want."**

## "What you'll know" was in the wrong place

The first line of a `知识点` body must be `> [!TIP]` (what you'll know). This sentence **used to live in `front-matter`'s `scope.目标`**.

- `kbcheck.py` **never parsed `目标`** (it only uses `scope.学段`);
- in other words: **a sentence purely for humans, and one that decides "whether you can get through it", sat in the "for the machine" half** —
  violating [FORMAT.md §1](../../FORMAT.en.md) hard rule #2 "the same fact is not written twice".

**Moved out of front-matter into the first body line on 2026-10-05.** 20 `知识点` were changed; **the `scope.目标` key is no longer used**.

## A self-test that nearly became an assertion

**First measurement**: the script scanned "English lines with no Chinese anywhere in a learner-facing section" and reported **196 lines across 43 files**.
I wrote "this is a problem" into the spec on that basis.

**Spot-checking showed the number was an overestimate.** Take `万有引力-AL` (it reported 13 lines, among the most):

```
教材的 [AL] 提示走一条跟「天体」相反的路：……      ← Chinese lead-in
### 一、先让人犹豫，再让人算                        ← Chinese heading
> `Ask the students what the attraction would be…`  ← English quotation (counted)
**顺序是设计好的**：先猜，后算。                     ← Chinese explanation
```

**The Chinese is there.** And among the three types students read directly (`知识点` / `误解` / `路径`), such lines number **only 5** —
the vast majority of the 196 are in `教法`, which is **for teachers**.

**"No Chinese on the whole line" = "no Chinese explanation" is a wrong inference.** Writing the quotation and the explanation on separate lines is already the natural Chinese-with-quotations format.

> This is the **same class of error** as `ev-002` (treating "recomputable" as evidence strength) and the section numbers invented across 40 files:
> **treating a measurement directly as a conclusion**.

**So the rule is not "translate every sentence" but those three — and they describe what the repo already does.**

## Rule 1 is still not mechanized

A check for "many English characters, few Chinese characters" is feasible but **will false-positive** (code blocks, formulas, proper nouns, quotation lines).
**The 196 above took a false positive for truth** — so no check is written yet, to avoid another "check that gives wrong advice"
(see the deleted one in [status-and-liveness.md](status-and-liveness.en.md)).
