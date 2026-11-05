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
**25** objects · **25** citable as fact · **0** not citable · **190** evidence records · **2** events
**2 confirmed** · 7 provisional · 0 valid · 16 awaiting review
**0** paths · all **0** learning outcomes covered · **0** (0%) taught exactly once
T4 3 · T3 21 · T2 1 — provenance tier (**weakest link** over cited evidence)

| Gap | Count | Why it counts as a gap |
|---|---|---|
| **Three-minute review** | 16 | Status is `待审`, the argument is written and the evidence has been read — only one review is missing: by a human (signature) or an agent (four-field `## 复核记录`) — either can write `已确证`. |
| **Awaiting review, evidence unread** | 0 | Status is `待审`, but at least one cited source is only located, not read (or the argument is missing, or nothing is cited) — a reviewer has nothing to compare against. This is the **precondition** for review, not another kind of review. |
| **Provenance below T4** | 22 | The **weakest** cited source was not read in full (`T3` summary / `T2` located only / `T1` unverified / `T0` no basis). This does not mean the content is wrong — it means a reader following the chain hits a place nobody has read. |
| **Missing English edition** | 17 | No `path_en`: an English reader lands on a Chinese page. |
| **Concepts without a method** | 0 | A concept answers *what it is*; a method answers *how to teach it*. The coverage page counts only the former, so this gap is invisible elsewhere. |
| **Out-of-library prerequisites** | 0 | The same `外部先修` key appears in ≥2 objects — it recurs in front of several chains. |
| **Outcomes covered by a single step** | 0 | A learning outcome is covered by exactly one step: if that step fails, the student gets no second chance. |
| **Coverage not backed by read evidence** | 0 | The entries covering this outcome have evidence at most at `仅定位`/`未核验` — the slot is scheduled, the basis has not been read. |
| **Gaps the entries wrote themselves** | 11 | The author left `**待补**:` in the body — a gap the entry admits to, not one inferred from outside. |
| **Physics chapters still 🔴** | 0 | Against the PEP catalogue, the whole chapter has no concept entry in this library. |

> One object can appear in several rows — **do not add the counts up**.
> **The one exact partition:** review 16 + review-blocked 0 = every `待审` entry (16).

### Three-minute review (16)

> Open a “review one entry” issue; no writing needed. Sorted by downstream dependents: editing it affects the most other entries.

- `kb:med:guideline-idsa-sab-catheter` · IDSA 金葡菌菌血症指南：建议尽早拔除中心静脉导管
- `kb:med:kdigo-2024-rec-1-1-2-1` · KDIGO 2024 CKD 推荐 1.1.2.1（1B）
- `kb:med:kdigo-2024-rec-2-2-1` · KDIGO 2024 CKD 推荐 2.2.1（1A）
- `kb:med:kdigo-2024-rec-3-15-1-1` · KDIGO 2024 CKD 推荐 3.15.1.1（1A）
- `kb:med:kdigo-2024-rec-3-15-1-2` · KDIGO 2024 CKD 推荐 3.15.1.2（1B）
- `kb:med:kdigo-2024-rec-3-15-1-3` · KDIGO 2024 CKD 推荐 3.15.1.3（2A）
- `kb:med:kdigo-2024-rec-3-4-1` · KDIGO 2024 CKD 推荐 3.4.1（2B）
- `kb:med:kdigo-2024-rec-3-6-1` · KDIGO 2024 CKD 推荐 3.6.1（1B）
- `kb:med:kdigo-2024-rec-3-6-2` · KDIGO 2024 CKD 推荐 3.6.2（1B）
- `kb:med:kdigo-2024-rec-3-6-4` · KDIGO 2024 CKD 推荐 3.6.4（1B）
- …and 6 more — full list: `python tools/make_tasks.py --json`

### Provenance below T4 (22)

> Open that source at its locator, read it, raise `核验深度` to `全文`; or cite a source that has already been read in full.

- `kb:med:prop-hypertension-cn-2024` · The 2024 revision of the Chinese Hypertension Guidelines prescribes ≥140/90 mmHg in the clinic for diagnosis, and <140/90 mmHg (further down to <130/80 mmHg if tolerated) as the target for general patients — T2, weakest: `ev-070`, `ev-074`, `ev-077`, `ev-078`
- `kb:med:prop-plague-treat-on-suspicion` · For suspected plague, WHO/CDC guidelines prescribe starting treatment without waiting for confirmation, and set explicit time limits for medication, isolation, and contact prophylaxis — T3, weakest: `ev-071`, `ev-072`, `ev-073`
- `kb:med:guideline-idsa-sab-catheter` · IDSA 金葡菌菌血症指南：建议尽早拔除中心静脉导管 — T3, weakest: `ev-199`
- `kb:med:kdigo-2024-rec-1-1-2-1` · KDIGO 2024 CKD 推荐 1.1.2.1（1B） — T3, weakest: `ev-200`
- `kb:med:kdigo-2024-rec-2-2-1` · KDIGO 2024 CKD 推荐 2.2.1（1A） — T3, weakest: `ev-200`
- `kb:med:kdigo-2024-rec-3-15-1-1` · KDIGO 2024 CKD 推荐 3.15.1.1（1A） — T3, weakest: `ev-200`
- `kb:med:kdigo-2024-rec-3-15-1-2` · KDIGO 2024 CKD 推荐 3.15.1.2（1B） — T3, weakest: `ev-200`
- `kb:med:kdigo-2024-rec-3-15-1-3` · KDIGO 2024 CKD 推荐 3.15.1.3（2A） — T3, weakest: `ev-200`
- `kb:med:kdigo-2024-rec-3-4-1` · KDIGO 2024 CKD 推荐 3.4.1（2B） — T3, weakest: `ev-200`
- `kb:med:kdigo-2024-rec-3-6-1` · KDIGO 2024 CKD 推荐 3.6.1（1B） — T3, weakest: `ev-200`
- …and 12 more — full list: `python tools/make_tasks.py --json`

### Missing English edition (17)

> The filename is derived from `id` (`<id tail minus type prefix>.en.md`), in the same folder as the Chinese original.

- `kb:med:guideline-gold-2026-abe` · GOLD 2026 调整 A/B/E 分组判据：一次中重度急性加重即足以改变分组
- `kb:med:guideline-idsa-sab-catheter` · IDSA 金葡菌菌血症指南：建议尽早拔除中心静脉导管
- `kb:med:kdigo-2024-rec-1-1-2-1` · KDIGO 2024 CKD 推荐 1.1.2.1（1B）
- `kb:med:kdigo-2024-rec-2-2-1` · KDIGO 2024 CKD 推荐 2.2.1（1A）
- `kb:med:guideline-kdigo-2024-egfr` · KDIGO 2024：CKD 风险人群首选基于肌酐的 eGFR（1B）
- `kb:med:kdigo-2024-rec-3-15-1-1` · KDIGO 2024 CKD 推荐 3.15.1.1（1A）
- `kb:med:kdigo-2024-rec-3-15-1-2` · KDIGO 2024 CKD 推荐 3.15.1.2（1B）
- `kb:med:kdigo-2024-rec-3-15-1-3` · KDIGO 2024 CKD 推荐 3.15.1.3（2A）
- `kb:med:kdigo-2024-rec-3-4-1` · KDIGO 2024 CKD 推荐 3.4.1（2B）
- `kb:med:kdigo-2024-rec-3-6-1` · KDIGO 2024 CKD 推荐 3.6.1（1B）
- …and 7 more — full list: `python tools/make_tasks.py --json`

### Gaps the entries wrote themselves (11)

> Fill in what that sentence asks for, then delete the marker.

- `kb:med:prop-ardsnet-low-tidal-volume` · For ARDS patients, low-tidal-volume ventilation … — body: **待补**：后续系统综述与指南（本库无来源）；该策略在非 ARDS 人群中的证据
- `kb:med:prop-proseva-prone-positioning` · In severe ARDS, early prone positioning reduces … — body: **待补**：后续系统综述与指南（本库无来源）；俯卧位在非重度 ARDS 人群中的证据
- `kb:med:prop-recovery-dexamethasone-by-respiratory-support` · In hospitalized patients with Covid-19, dexameth… — body: **待补**：WHO / NIH / 中国 COVID-19 治疗指南的原文；RECOVERY 剂量比较试验（高剂量 vs 低剂量）原文；糖皮质激素在其他病毒性肺炎中的证据
- `kb:med:prop-copd-gold-2026` · GOLD 2026 prescribes post-bronchodilator FEV1/FV… — body: **待补**：GOLD 2026 报告全文通读与版本时效核对；**A、B、E 三组的症状侧分界值
- `kb:med:prop-hypertension-cn-2024` · The 2024 revision of the Chinese Hypertension Gu… — body: **待补**：指南全文 98 页的通读与版本时效核对；取得 `ev-074` · `ev-077` 原书后升级核验深度
- `kb:med:prop-sprint-intensive-bp` · In high-cardiovascular-risk adults without diabe… — body: **待补**：复合结局各组分的贡献与绝对发生率（全文 PMC4689591）；在糖尿病、既往卒中、心衰人群中的证据（本试验未纳入）
- `kb:med:guideline-gold-2026-abe` · GOLD 2026 调整 A/B/E 分组判据：一次中重度急性加重即足以改变分组 — body: **待补**：报告正文（100+ 页）里 A/B/E 的完整判据表未录入；本条只覆盖「调整这件事」与「触发条件」
- `kb:med:guideline-idsa-sab-catheter` · IDSA 金葡菌菌血症指南：建议尽早拔除中心静脉导管 — body: **待补**：GRADE 等级需查指南全文（CID 原文），在线页未载
- `kb:med:guideline-kdigo-2024-egfr` · KDIGO 2024：CKD 风险人群首选基于肌酐的 eGFR（1B） — body: **待补**：第 1 章对「CKD 风险」的完整定义未录入；本条的适用人群暂只写「有 CKD 风险的成人」
- `kb:med:prop-plague-treat-on-suspicion` · For suspected plague, WHO/CDC guidelines prescri… — body: **待补**：三份指南的版本核对（是否仍为当前有效版本）；
- …and 1 more — full list: `python tools/make_tasks.py --json`
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
