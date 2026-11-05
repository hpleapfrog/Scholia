# Gap report

> **This page is generated.** The tables and lists are computed by
> [`tools/gaps.py`](../tools/gaps.py) and written by [`tools/kbcheck.py`](../tools/kbcheck.py)
> whenever you run `python tools/kbcheck.py --write-index`.
> **Hand edits fail the check** (`R-INDEX-02`).
>
> 中文 → [GAPS.md](GAPS.md)

## What this page answers

“What is this library still missing, and what should I do first?”

It lists only the gaps a **machine can count**. Mixing in the ones it cannot would make
this page look more authoritative than it is — and the first rule of this library is
**not to pretend to know**. Every row therefore states *why it counts as a gap*, and
“the half machines don't judge” is a separate table below.

<!-- kbcheck:begin -->
**8** objects · **8** citable as fact · **0** not citable · **188** evidence records · **2** events
**1 confirmed** · 7 provisional · 0 valid · 0 awaiting review
**0** paths · all **0** learning outcomes covered · **0** (0%) taught exactly once
T4 2 · T3 5 · T2 1 — provenance tier (**weakest link** over cited evidence)

| Gap | Count | Why it counts as a gap |
|---|---|---|
| **Three-minute review** | 0 | Status is `待审`, the argument is written and the evidence has been read — only one review is missing: by a human (signature) or an agent (four-field `## 复核记录`) — either can write `已确证`. |
| **Awaiting review, evidence unread** | 0 | Status is `待审`, but at least one cited source is only located, not read (or the argument is missing, or nothing is cited) — a reviewer has nothing to compare against. This is the **precondition** for review, not another kind of review. |
| **Provenance below T4** | 6 | The **weakest** cited source was not read in full (`T3` summary / `T2` located only / `T1` unverified / `T0` no basis). This does not mean the content is wrong — it means a reader following the chain hits a place nobody has read. |
| **Missing English edition** | 0 | No `path_en`: an English reader lands on a Chinese page. |
| **Concepts without a method** | 0 | A concept answers *what it is*; a method answers *how to teach it*. The coverage page counts only the former, so this gap is invisible elsewhere. |
| **Out-of-library prerequisites** | 0 | The same `外部先修` key appears in ≥2 objects — it recurs in front of several chains. |
| **Outcomes covered by a single step** | 0 | A learning outcome is covered by exactly one step: if that step fails, the student gets no second chance. |
| **Coverage not backed by read evidence** | 0 | The entries covering this outcome have evidence at most at `仅定位`/`未核验` — the slot is scheduled, the basis has not been read. |
| **Gaps the entries wrote themselves** | 8 | The author left `**待补**:` in the body — a gap the entry admits to, not one inferred from outside. |
| **Physics chapters still 🔴** | 0 | Against the PEP catalogue, the whole chapter has no concept entry in this library. |

> One object can appear in several rows — **do not add the counts up**.

### Provenance below T4 (6)

> Open that source at its locator, read it, raise `核验深度` to `全文`; or cite a source that has already been read in full.

- `kb:med:prop-hypertension-cn-2024` · The 2024 revision of the Chinese Hypertension Guidelines prescribes ≥140/90 mmHg in the clinic for diagnosis, and <140/90 mmHg (further down to <130/80 mmHg if tolerated) as the target for general patients — T2, weakest: `ev-070`, `ev-074`, `ev-077`, `ev-078`
- `kb:med:prop-plague-treat-on-suspicion` · For suspected plague, WHO/CDC guidelines prescribe starting treatment without waiting for confirmation, and set explicit time limits for medication, isolation, and contact prophylaxis — T3, weakest: `ev-071`, `ev-072`, `ev-073`
- `kb:med:prop-ardsnet-low-tidal-volume` · For ARDS patients, low-tidal-volume ventilation reduces mortality — T3, weakest: `ev-048`
- `kb:med:prop-proseva-prone-positioning` · In severe ARDS, early prone positioning reduces mortality — T3, weakest: `ev-069`
- `kb:med:prop-osa-pap-titration` · For obstructive sleep apnea, adult PAP titration has guideline-prescribed starting pressures, escalation rules, and target criteria — T3, weakest: `ev-050`
- `kb:med:prop-sprint-intensive-bp` · In high-cardiovascular-risk adults without diabetes, intensive BP lowering reduces major CV events and all-cause death, but raises some adverse events — T3, weakest: `ev-070`

### Gaps the entries wrote themselves (8)

> Fill in what that sentence asks for, then delete the marker.

- `kb:med:prop-ardsnet-low-tidal-volume` · For ARDS patients, low-tidal-volume ventilation … — body: **待补**：后续系统综述与指南（本库无来源）；该策略在非 ARDS 人群中的证据
- `kb:med:prop-proseva-prone-positioning` · In severe ARDS, early prone positioning reduces … — body: **待补**：后续系统综述与指南（本库无来源）；俯卧位在非重度 ARDS 人群中的证据
- `kb:med:prop-recovery-dexamethasone-by-respiratory-support` · In hospitalized patients with Covid-19, dexameth… — body: **待补**：WHO / NIH / 中国 COVID-19 治疗指南的原文；RECOVERY 剂量比较试验（高剂量 vs 低剂量）原文；糖皮质激素在其他病毒性肺炎中的证据
- `kb:med:prop-copd-gold-2026` · GOLD 2026 prescribes post-bronchodilator FEV1/FV… — body: **待补**：GOLD 2026 报告全文通读与版本时效核对；**A、B、E 三组的症状侧分界值
- `kb:med:prop-hypertension-cn-2024` · The 2024 revision of the Chinese Hypertension Gu… — body: **待补**：指南全文 98 页的通读与版本时效核对；取得 `ev-074` · `ev-077` 原书后升级核验深度
- `kb:med:prop-sprint-intensive-bp` · In high-cardiovascular-risk adults without diabe… — body: **待补**：复合结局各组分的贡献与绝对发生率（全文 PMC4689591）；在糖尿病、既往卒中、心衰人群中的证据（本试验未纳入）
- `kb:med:prop-plague-treat-on-suspicion` · For suspected plague, WHO/CDC guidelines prescri… — body: **待补**：三份指南的版本核对（是否仍为当前有效版本）；
- `kb:med:prop-osa-pap-titration` · For obstructive sleep apnea, adult PAP titration… — body: **待补**：AASM 后续的 PAP 临床实践指南与自动调压专项指南原文；中枢性呼吸暂停的对应记录
<!-- kbcheck:end -->

## Reviewing one entry: three yes/no questions, 3 minutes

| # | Question | What counts as “no” |
|---|---|---|
| 1 | Can you open the source it cites? | 404 / dead link / paywalled |
| 2 | Does that page really say this sentence? | different wording, broader meaning, not there at all |
| 3 | Does its conclusion go beyond that page? | the source limits a population / version / condition, the entry states it universally |

> **The three questions ask only “does the source say this”, never “is the conclusion correct”.**
> Submit with [`.github/ISSUE_TEMPLATE/复核一条.yml`](../.github/ISSUE_TEMPLATE/复核一条.yml);
> three “yes” answers move an entry from `待审` to `暂定确认` — which **requires a non-author reviewer**,
> so an AI cannot answer these three for you (`M-07`).

## The half machines don't judge

| Question | Who judges | Where it lives |
|---|---|---|
| Does this argument hold? | A human (`M-07`; an AI may only attack) | the entry's `## Argument` |
| Is this prerequisite really required? | A human (`M-12`) | the `外部先修` declaration |
| Does this method work in a real classroom? | A human (`M-04`) | the method's `Taboo` / `Risk` sections |
| Are two sources really independent? | A human (`M-03`) | the evidence make-up of `Support` edges |
| Is a path pedagogically sufficient? | A human | the path's `Self-check` section |
| Is this content worth writing at all? | A human | topic selection |

## How to use it

| You want | Use |
|---|---|
| to start right now | `python tools/make_tasks.py --limit 3` (add `--gh` to open issues) |
| the full list / machine-readable | `python tools/make_tasks.py --json` |
| to review one entry without hunting for material | `python tools/review_packet.py --id <id>` — **formats only; it does not answer** the three questions |
| an agent to pick the next step | the MCP tool `scholia_gaps` — same `compute()`, no need to read the index |
| to confirm these tools still work | `python tools/selftest.py` — MCP handshake + 9 tools + `--json` + scaffold generation + review packet |
| the rules themselves | [RULES.en.md](RULES.en.md) |
