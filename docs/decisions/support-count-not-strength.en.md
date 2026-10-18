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
