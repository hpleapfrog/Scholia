# Why all six types must have `## 论证`

> Rule: [FORMAT.md](../../FORMAT.en.md) §5 "Required sections".

The table above (§5) **previously listed `论证` only for `命题` and `教法`**, while `kbcheck.py` has always enforced
"all types must have it" — **and noted "FORMAT.md §5" in its own error message**.

> **In other words: the code claims the spec says so, but the spec didn't. The spec is narrower than the code.**

**How it was found**: while writing the "taking the subway" probe, `路径` was reported
"missing required section `论证` (all types must have it)", and checking the table showed `路径` didn't list it.
**The inconsistency only surfaced when a `路径` no one had ever written was written for the first time.**

**Why all types need `论证`**: every piece of content in the repo should be able to answer "**why do I say so**".
`资源` too — "why this resource is worth including" is itself a claim
(see the `R1` of the [PhET resource](../../knowledge/物理/资源/phet-forces-and-motion-basics.en.md)).
