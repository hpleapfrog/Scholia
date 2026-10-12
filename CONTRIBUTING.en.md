# Contributing Guide

> 中文 → [**CONTRIBUTING.md**](CONTRIBUTING.md)

> Read [README](README.md) and [FORMAT.md](FORMAT.md) first.

---

## 0. Rule architecture: which layer each rule lives in

| Layer | File | Answers | Enforced by |
|---|---|---|---|
| Entry | [README](README.md) | what this is, who it's for | people |
| Spec | [FORMAT.md](FORMAT.md) | how to write a file, how status is set | `kbcheck.py` |
| Evidence | [evidence/README.md](evidence/README.md) | what may be cited, grades & licenses | `kbcheck.py` |
| Process | this file + `.github/` templates | how to submit, who may change status | template checkboxes · people |
| Decisions | [`docs/decisions/`](docs/decisions/README.md) | **why** a rule is set this way (cases · incidents · inferences) | people (append-only) |
| Rule registry | [`docs/RULES.md`](docs/RULES.md) (**generated**) | which rules exist, mechanical or manual | `--write-index` |
| AI contract | [llms.txt](llms.txt) + [index.json](index.json) (**generated**) | how machines read and cite | `--write-index` |
| Enforcement | [tools/kbcheck.py](tools/kbcheck.py) | violate → fail | local / CI |

**Principle**: every rule has only three homes — **mechanical** (kbcheck), **template checkbox**,
or **human review**. **If it can't be mechanized, say it's a manual item — never pretend it's
enforced** (FORMAT's header now says exactly this).

> [!IMPORTANT]
> **Admission threshold for a new rule** (isomorphic to the evidence threshold; all required):
> 1. a **failing** injection sample — verified in a **temporary copy**, never polluting the repo;
> 2. the repo **passes**, or the violations are fixed in the same PR;
> 3. a written **false-positive policy** — **a check that gives wrong advice is worse than none**
>    (this library deleted one such check, see FORMAT.md §6).

> [!NOTE]
> **Never hand-write numbers in human docs.** The stats in `README.md` / `knowledge/README.md`
> are generated from `index.json` (between `<!-- kbcheck:begin -->` / `<!-- kbcheck:end -->`).
> Hand-written numbers drift, **and a drifting number is an assertion** (this library was attacked over this once).

---

## 1. Three channels — don't pick the wrong one

| You want to | Where | Affects conclusions? |
|---|---|---|
| Ask, discuss method, share **rough** ideas | **Discussions** | ❌ **No** |
| Report a suspected error, submit a method | **Issue** (template) | Indirectly |
| Actually change the knowledge | **PR** | ✅ **The only channel that can** |

> [!IMPORTANT]
> Any claim in Discussions has **zero effect on conclusions until it becomes an Issue + PR**.
> This is a gate against long threads diluting judgement, not a dismissal of discussion.

**Discussion categories**: `📣 Announcements` `💬 Methodology` `❓ Q&A` `🧪 Exploratory hypotheses` `🗳️ Governance proposals`

---

## 2. Minimal workflow

```bash
git clone https://github.com/hpleapfrog/Scholia.git
cd Scholia
git checkout -b fix/ohm-law-temperature
# edit knowledge/物理/命题/欧姆定律.md
python tools/kbcheck.py          # ← must pass
git commit -am "补充温度条件与实验证据"
git push origin fix/ohm-law-temperature
# then open a PR on GitHub
```

Format rules: see [FORMAT.md](FORMAT.md). Four key points:

1. **One concept = one `.md` file** (don't merge or split)
2. **Never write the same fact twice**
3. **Fixed section order**; `## 论证` must exist (may be empty under draft)
4. **Relative links only**; no `[[wikilinks]]` (GitHub won't render them)

---

## 3. Evidence threshold

**Discussion is free, but only evidence past the threshold enters judgement.**

| Kind | Locator form |
|---|---|
| Textbook / monograph | ISBN + edition + page |
| Paper | DOI |
| Guideline / standard | official clause number |
| Data | public dataset id, or a file under this repo's `evidence/` |
| Experiment | a reproducible script + raw data |

Comments that don't clear the threshold stay in the thread and **do not affect conclusions**.

> [!CAUTION]
> **Never upload textbook text or scanned pages.** Store only page locators, short quotes, and
> original summaries.

**Two claim types use different ladders — don't mix them up:**

| Claim type | Ladder (high → low) |
|---|---|
| 命题 (claims) | systematic review > RCT > cohort > case > expert opinion > **the textbook itself** |
| 教法 (methods) | reproducible classroom experiment > quasi-experiment > large-scale classroom data > single-classroom experience > expert intuition |

**Single-classroom experience is legitimate evidence for methods** — methods are strongly
conditional and transfer poorly. Don't impose medical standards here.

---

## 4. Status and power

### Rules (dead)

See [FORMAT.md §6](FORMAT.md). The core asymmetry:

> **Make "disputed" easy and "confirmed" hard.**

A textbook error must be easier to expose than to confirm.

### Power (minimal start)

| # | Rule |
|---|---|
| 1 | **Anyone may open a PR**, no permission needed |
| 2 | `status` **may only be written by the PR author, by the rules** |
| 3 | Writing `已确证` needs **at least one independent non-author review** |
| 4 | **No reviewer → stays `待审`. Long suspension is honest, not failure** |
| 5 | `争议` **needs no one's approval** |
| 6 | **No one may declare a dispute's winner** |
| 7 | **`失据` and `争议` are normal states**, not garbage to clean up |

**No domain maintainers, no adjudication power** — a decision method *is* power allocation; fixing
it before participants exist is the founder legislating in advance.

### AI may attack (welcome), not review

**AI-generated attacks are legitimate contributions**, and **especially fitting** — the attacker's
burden is low (find one flaw).

| Role | OK for AI? |
|---|---|
| **Raise an attack** (`攻击` edge + an attack entry) | ✅ **yes, and welcome** |
| **Be the independent review for `已确证`** | ❌ **no, no exception** |

**Reason**: AI tends to agree; its "agreement" with the author may be **false independence**
(shared training bias); and it has **no accountable subject to question**. Independent review
needs exactly that subject.

**Three things to do when submitting an AI attack:**

1. **You reviewed it yourself** — state in the body who reviewed and what. **AI saying so ≠ it holds.**
2. **Disclose model and date** — `author` as `AI（model name）· 经 @someone 复核 · date`
3. **Accept counter-attack** — an AI attack has the **same standing** as a human one; it is itself attackable

> [!TIP]
> **Submit an attack even if it doesn't hold.**
> Record it as "a defeated attack" with **why it fails**, so the next person (or AI) won't repeat
> it. Same reason voided evidence keeps its id: **erasing traces is the real information loss.**

### Three easily-confused statuses

| Status | Meaning |
|---|---|
| `待审` | **no one has built arguments yet** |
| `争议` | surviving arguments **conflict** |
| `失据` | once argued, **then defeated**; the claim stands but nothing supports it now |

> [!IMPORTANT]
> **`待审` and `失据` must be separate.** The rules first lumped both into "empty surviving set",
> which made **an attack's consequence invisible in `status`** — and attacking is this library's core mechanism.

### An attack is also an entry

`攻击` **is not a comment, it is an independent entry**:

- it has its own `## 论证`, its own `status`, its own way of being defeated
- its `支持` / `攻击` edges **must carry argument anchors** (e.g. `#a1`), or you can't locate which argument is attacked
- **defeating an attack and the attacked argument surviving are two different things**

### Escalation triggers

| Trigger | Condition | Escalates to |
|---|---|---|
| **A** | a subject reaches ≥ 30 `已确证` **and** ≥ 3 active contributors | domain maintainers (may sign off status, **may not edit rules**) |
| **B** | ≥ 5 `争议` unconverged for 90 days | rotating adjudication (appealable) |
| **C** | any instance of `status` being illegally rewritten | **immediately introduce CI enforcement** (rules as code) |

Trigger C is hard: **once rules are bypassed once, social enforcement has proven insufficient — switch to machine enforcement.**

> [!NOTE]
> **CI is already enabled** ([`.github/workflows/kbcheck.yml`](.github/workflows/kbcheck.yml),
> read-only, zero-dependency, no secrets) — not waiting for trigger C. **There are enough rules now
> that remembering to run them by hand costs more than running them by machine.**

### Labels are for triage, not object status

Issue labels use the `type:*` and `triage:*` prefixes — **never confuse them with an object's
`status`**: an object's `status` may only be changed by a PR per the rules; Issue labels are just
triage and **don't affect conclusions**. (`triage:*` / `type:*` must exist in Settings → Labels.)

### Two guardrails

1. **Status can't be hand-edited.** Changing `status` requires stating in the PR which surviving
   arguments justify it.
2. **👍 reactions are not a basis for judgement.**

> [!WARNING]
> **Likes only rank attention, never decide right or wrong.**
> Conclusions are decided by "evidence grade + rebuttal structure", not by headcount.

---

## 5. Pre-submit self-check

- [ ] I ran `python tools/kbcheck.py` and it **passes**
- [ ] I changed only what needed changing, without reformatting others' content
- [ ] `front-matter` has all 11 fields
- [ ] Every piece of evidence has a verifiable locator, is registered in the [evidence index](evidence/README.md), and states its **verification depth** (full text / abstract / locator-only)
- [ ] New evidence passed the **three source questions** (see the [evidence threshold](evidence/README.md)): **who publishes it** (an accountable body) · **earliest verifiable date** (a third-party archive predates our citation) · **can a second source be found outside that publisher** —
      self-built sites, attribution-free repost pages and identifiers that don't resolve are **not registered**; several same-origin reposts **do not count as independent corroboration**
- [ ] A new `知识点`'s first body line is `> [!TIP]` (what you'll be able to do)
- [ ] A new method filled in **水平档** (BL / OL / AL, or `不分档` for cross-level)
- [ ] A new medical entry filled `scope.条件` and has a `> [!CAUTION]` block at the top of the body
- [ ] `scope.学段` uses the enum (小学/初中/高中/大学/不限, joined with 「至」, **not `/`**)
- [ ] A new method filled **禁忌** (who it's not for) and **stated its evidence strength**; failure modes go in `## 风险`, **not mixed together**
- [ ] A new method filled `knowledge_point` pointing to a `知识点`
- [ ] A new path declares **`outcomes`** and marks **coverage** on every row of the ordering table
- [ ] If I wrote `支持` / `攻击` edges, they **carry argument anchors** that actually exist
- [ ] If I argued strength by count, **I checked the sources are independent** — **15 instances from one book are not 15 pieces of evidence**
- [ ] I did not upload textbook text or scanned pages
- [ ] I checked the **license of newly cited resources** (not from memory) — **a CC BY textbook doesn't make what it embeds CC BY**
- [ ] **I did not hand-write stats in human docs** (leave it to `--write-index`)
- [ ] I recorded this change's grounds and PR number in the 变更记录 table
- [ ] I wrote `status` by the rules, not by feeling

---

## 6. What if I disagree with a conclusion

In order:

1. **Read its argument graph** — is there a surviving attack you hadn't considered?
2. **Open an evidence-backed PR** — the most effective route
3. **Open an Issue** (suspected error / new method / prerequisite dispute) — if you don't yet have evidence
4. **Go to Discussions → Methodology** — if you think the **rules themselves** are wrong
5. **Fork and leave** — take all history and maintain your own copy. **This is your right; no one's permission needed.**

> A knowledge base you can't exit is not a decentralized knowledge base.
