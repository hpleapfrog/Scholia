# English filenames: from "same name" to "derived from `id`"

> **中文 → [english-filenames-from-id.md](english-filenames-from-id.md)**

> Decided **2026-10-18**; 142 files renamed, enforced by `R-BILING-01` in
> `tools/kbcheck.py`. The rule itself lives in [FORMAT.en.md](../../FORMAT.en.md) §0;
> this page records **why** it changed.

## The old rule

`FORMAT.md` §0 used to say: Chinese original `<name>.md`, English translation **same name**
`<name>.en.md`.

```
knowledge/physics/concepts/参考系.md
knowledge/physics/concepts/参考系.en.md   ← the English page
```

That convention carried a hidden assumption: **"same name" expresses "these are a pair"**.

## What went wrong

**1. English content sat under Chinese filenames.**

The English page's address was `knowledge/physics/concepts/参考系.en.md`. An English reader arriving
from `START.en.md` landed on a page **named in Chinese**; paste that link elsewhere and the
recipient sees Chinese too. The content is English — **the name says nothing about it**.

**2. "Same name" is a character-level coincidence, not a pairing relation.**

The checker could only ask "does `X.en.md` exist?", never "does `X.en.md` translate `X.md`". So:

| Situation | Could the old rule catch it? |
|---|---|
| The English page gets renamed (no longer matching) | ❌ No — the check only looked at that one same-named candidate |
| Two translations of the same entry | ❌ No |
| The English page translates a *different* entry but happens to share the name | ❌ No (different `id` would still pass) |
| An entry has no translation at all | ❌ No (`M-10` was manual, and nobody checks CI for it) |

**The pairing key already existed and was already written: the `id`.** It is unique, stable, and
survives renames (`FORMAT.md` §3 defines it exactly that way) — yet it was never used for pairing.

## What it is now

**English filename = last segment of the `id`, minus the type prefix, plus `.en.md`, in the same
folder as the Chinese original.**

```
id:  kb:physics:kp-frame-of-reference
zh:  knowledge/physics/concepts/参考系.md
en:  knowledge/physics/concepts/frame-of-reference.en.md
```

| Benefit | Why |
|---|---|
| The name is English | `frame-of-reference.en.md` says what it is; links make sense out of context |
| Renames don't matter | The Chinese file can be renamed freely; the English name follows the `id` |
| **Pairing is machine-checked** | `R-BILING-01`: a filename not derived from the `id` **fails**; an English page linking to a Chinese one **fails** |
| One translation per location | A single `id` yields a single derived name; duplicates collide loudly |

## The cost (stated plainly)

1. **Chinese and English files no longer sit side by side with matching names**, so pairing is not
   visible at a glance. Mitigation: the first line of every English page is
   `> **English version of [`参考系.md`](参考系.md).**`, and pairing is checked by the script,
   not by eye.
2. **An `id` can never be changed now** — it is the source of the filename. That was already true
   (`id` is defined as the rename-proof identifier), but it now has an external dependency.
3. **The migration had a cost**: 142 files renamed, links in 119 files rewritten. That is a
   **one-off**; leaving it alone would keep manufacturing the same problem with every new entry.

## What was deliberately not done

**A missing translation is a notice, not a failure.** "Bilingual" is a promise, but turning it into
a hard gate adds a translation step to every Chinese entry — **that is a separate policy** and has
to be decided on its own, not slipped in with a naming fix. The gap is listed on every run.

## Follow-up (same day): folders anglicised as well

After the filenames were fixed, `knowledge/物理/命题/` was still in the path. **The same argument**
(paths get copied, pasted into terminals, parsed as URLs) applies to it, so on 2026-10-18 **31 folders**
were renamed to English:

```
knowledge/physics/claims/     knowledge/physics/concepts/   knowledge/physics/methods/
knowledge/physics/misconceptions/  knowledge/physics/paths/ knowledge/physics/resources/
knowledge/physics/coverage/   knowledge/physics/claims/attacks/
```

Subject folders: `physics` `life` `medicine` `geography` `science` `transport` `computing`
`economics` `law`.

**Chinese filenames stay** — folders must work as URLs, names must be readable by people; two
different jobs.

> **Subject folder names and `id` prefixes are two namespaces**: folders must read well
> (`medicine/`), prefixes must be short (`kb:med:`). Both are registered exactly once, in
> `tools/kbcheck.py` (`SUBJECT_DIRS` / `SUBJECT_SLUGS`).

## Still not done

**Chinese entries keep Chinese filenames** (`欧姆定律.md`). A fully English filename set is one more
rename under the same `id`-derived rule — but it would **remove one more layer of readability**
(a Chinese reader scanning a folder would no longer recognise entries), so it is out of scope here.
