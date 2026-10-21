# Coverage against Chinese senior-high physics

> 中文 → [**README.md**](README.md)

> [!CAUTION]
> **The "target" column on this page is the author's own working list, with no citable source.**
>
> The authoritative source should be the *Physics Curriculum Standard for Senior High School
> (2017 edition, revised 2020)* and the **table of contents** of the PEP textbooks
> (ISBN + edition + page). **This library has neither**, so the table is **a gap list, not a standard**.
>
> **An issue tracks this.** Until the sources are in hand, **do not treat this page as a restatement
> of the curriculum standard.**

## What the table is for

The requirement was "**extend it to what Chinese senior-high students are taught**". That requirement
has one easy way to go wrong:

> **This library's `concepts` are cut by "concept", not by "textbook chapter".**
> (See [`FORMAT.en.md`](../../../FORMAT.en.md) §2, and an
> [adversarial review](../claims/attacks/tieredguidance.en.md) criticising the use
> of chapter boundaries as node boundaries.)

So the table is **not** "how many sections short of the PEP contents list we are", but:

**"Of the concepts Chinese senior-high physics asks students to build, which exist here and which are missing."**

> [!NOTE]
> **The row-by-row mapping (25 chapter-level topics) is maintained only in the Chinese page**
> ([`README.md`](README.md)). It is a hand-curated working list whose rows change whenever an entry is
> added, and duplicating it in two languages would guarantee the two copies drift apart. The
> **generated numbers below are shared** by both pages.

## Overview (generated)

<!-- kbcheck:begin -->
| | 章级主题数 | 占比 |
|---|---|---|
| 🟢 有覆盖 | **6** | 24% |
| 🟡 部分覆盖 | **11** | 44% |
| 🔴 完全缺 | **8** | 32% |
| **合计** | **25** | 100% |
<!-- kbcheck:end -->

## A problem worth recording more than the gaps: every method comes from one US textbook

Across **all `methods`** in this library, the overwhelming majority of evidence is
**OpenStax *Physics*** — a **CC BY US high-school textbook**.

**It records "how a US textbook teaches this", not "how it works in a Chinese classroom".**
At least three differences are already known:

| Aspect | Known difference here |
|---|---|
| **Notation** | Chinese textbooks write `U` for voltage; the US book writes `V` — one [claim](../claims/voltage-symbol-u-v.en.md) records this |
| **Order** | Chinese compulsory-1 teaches **force** before **motion and force**; OpenStax puts vectors in chapter 5 (before projectiles) |
| **Maths** | OpenStax *Physics* uses **no calculus**, and Chinese elective-1 does not require it either — **this one happens to agree** |

> [!WARNING]
> **"Would this method work in a Chinese classroom?" — this library has no data.**
> Every existing `method` says only "**the textbook specifies it**"; **not one says "tested in a Chinese classroom"**.
>
> That cannot be filled in by reading textbooks — **it needs classroom data.** **This page records it as a gap.**

## Suggested priority (the author's view, not a standard)

Ranked by "downstream nodes × size of the gap":

| # | What to add | Why first |
|---|---|---|
| ~~1~~ | ~~Force (HS) + Newton's 2nd + Newton's 3rd~~ | **✅ done** — `force → inertia → Newton's 2nd → Newton's 3rd` is connected |
| ~~2~~ | ~~Conservation of momentum~~ | **✅ done** — `Newton's 2nd → momentum & impulse → conservation → collisions` |
| ~~3~~ | ~~Electrostatics (charge · field strength · potential energy)~~ | **✅ started (2026-10-18)** — charge · Coulomb's law · electric field · electric potential energy and potential (one node more than planned); **capacitance and charged particles in fields still missing** |
| ~~4~~ | ~~Circular motion + centripetal force~~ | **✅ complete (2026-10-18)** — uniform circular motion · centripetal force · centrifugal misconception; **same day**: angular acceleration & rotational kinematics · torque |
| ~~5~~ | ~~Laws of thermodynamics~~ | **✅ started (2026-10-21)** — first law of thermodynamics · second law of thermodynamics; **heat-engine efficiency, the Carnot cycle, and the statistical interpretation of entropy still missing** |
| ~~6~~ | ~~Nuclear physics~~ | **✅ started (2026-10-21)** — atomic nucleus · radioactive decay; **binding energy/mass defect, fission and fusion, and medical applications still missing** |

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-05 | Page created (first mapping against Chinese senior-high physics) | the request to "extend it to what Chinese senior-high students are taught" | @hpleapfrog |
| 2026-10-18 | Statistics block turned into a generated block; fixed a statistics table that disagreed with its own overview table | a drift found while tidying: **the stats had two more rows than the table** | @hpleapfrog |
| 2026-10-18 | **Compulsory-2 "circular motion" 🔴 → 🟡**: four new entries (ev-080–082) | OpenStax *Physics* ch. 6, modules m54173 / m54176 / m54181 read in full | @hpleapfrog |
| 2026-10-18 | **Compulsory-3 "electrostatics and its applications" / "energy in electrostatic fields" 🔴 → 🟡**: four new concepts — charge · Coulomb's law · electric field · electric potential energy and potential (ev-083–087) | OpenStax *Physics* ch. 18, modules m54417 / m54410 / m54414 / m54428 / m54426 read in full | @hpleapfrog |
| 2026-10-18 | **Compulsory-2 "circular motion" 🟡 → 🟢**: filled in angular acceleration & rotational kinematics · torque (ev-088) | OpenStax *Physics* ch. 6, module m54180 read in full | @hpleapfrog |
| 2026-10-18 | English edition added; row-by-row table stays in the Chinese page (two copies would drift) | bilingual completeness (`R-BILING-03`) | @hpleapfrog |
| 2026-10-21 | **Elective-3 "laws of thermodynamics" 🔴 → 🟡**: first law of thermodynamics · second law of thermodynamics added (ev-156/ev-157) | OpenStax *Physics* ch. 12, modules m54305 / m54306 read in full | @hpleapfrog |
| 2026-10-21 | **Elective-3 "atomic nucleus" 🔴 → 🟡**: atomic nucleus · radioactive decay added (ev-158/ev-159) | OpenStax *Physics* ch. 22, modules m54580 / m63183 read in full | @hpleapfrog |
