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
**746** objects · **744** citable as fact · **2** not citable · **188** evidence records · **2** events
**526 confirmed** · 43 provisional · 157 valid · 15 awaiting review
**17** paths · all **73** learning outcomes covered · **67** (92%) taught exactly once
T4 733 · T3 5 · T2 8 — provenance tier (**weakest link** over cited evidence)

| Gap | Count | Why it counts as a gap |
|---|---|---|
| **Three-minute review** | 12 | Status is `待审`, the argument is written and the evidence has been read — only one review is missing: by a human (signature) or an agent (four-field `## 复核记录`) — either can write `已确证`. |
| **Awaiting review, evidence unread** | 3 | Status is `待审`, but at least one cited source is only located, not read (or the argument is missing, or nothing is cited) — a reviewer has nothing to compare against. This is the **precondition** for review, not another kind of review. |
| **Provenance below T4** | 13 | The **weakest** cited source was not read in full (`T3` summary / `T2` located only / `T1` unverified / `T0` no basis). This does not mean the content is wrong — it means a reader following the chain hits a place nobody has read. |
| **Missing English edition** | 0 | No `path_en`: an English reader lands on a Chinese page. |
| **Concepts without a method** | 37 | A concept answers *what it is*; a method answers *how to teach it*. The coverage page counts only the former, so this gap is invisible elsewhere. |
| **Out-of-library prerequisites** | 2 | The same `外部先修` key appears in ≥2 objects — it recurs in front of several chains. |
| **Outcomes covered by a single step** | 17 | A learning outcome is covered by exactly one step: if that step fails, the student gets no second chance. |
| **Coverage not backed by read evidence** | 0 | The entries covering this outcome have evidence at most at `仅定位`/`未核验` — the slot is scheduled, the basis has not been read. |
| **Gaps the entries wrote themselves** | 110 | The author left `**待补**:` in the body — a gap the entry admits to, not one inferred from outside. |
| **Physics chapters still 🔴** | 2 | Against the PEP catalogue, the whole chapter has no concept entry in this library. |

> One object can appear in several rows — **do not add the counts up**.
> **The one exact partition:** review 12 + review-blocked 3 = every `待审` entry (15).

### Three-minute review (12)

> Open a “review one entry” issue; no writing needed. Sorted by downstream dependents: editing it affects the most other entries.

- `kb:physics:self-and-mutual-inductance` · Self-inductance and mutual inductance — 2 other entries list it as a prerequisite
- `kb:physics:electric-work-and-joule-law` · Electric work and Joule's law — 1 other entries list it as a prerequisite
- `kb:physics:analogy-stage-attribution-invalid` · With n=2 one cannot attribute among several equally varying variables
- `kb:physics:ionizing-radiation-in-medicine` · Ionizing radiation in medicine
- `kb:physics:charged-particle-in-electric-field` · Motion of a charged particle in an electric field
- `kb:physics:reactance-and-impedance` · Reactance and impedance
- `kb:physics:eddy-currents-and-motional-emf` · Eddy currents and motional emf
- `kb:physics:energy-resources-and-sustainability` · Energy resources and sustainability
- `kb:life:prop-oversale-volunteer-first` · When oversold, no passenger may be denied boarding without the volunteer-solicitation process
- `kb:physics:velocity-time-graph-area` · Area under a velocity–time graph equals displacement
- …and 2 more — full list: `python tools/make_tasks.py --json`

### Awaiting review, evidence unread (3)

> Open the source at its locator, read it, raise `核验深度` to `摘要`/`全文`; or cite a source that has already been read.

- `kb:life:prop-carried-item-limits` · Beijing subway sets hard size and weight limits on items passengers carry — evidence unread: `ev-043`
- `kb:physics:ohm-law-scope-placement` · Where textbooks place the limitations of Ohm's law — evidence unread: `ev-001`
- `kb:physics:voltage-symbol-u-v` · The U vs V voltage-symbol difference between Chinese and English textbooks — evidence unread: `ev-001`

### Provenance below T4 (13)

> Open that source at its locator, read it, raise `核验深度` to `全文`; or cite a source that has already been read in full.

- `kb:med:prop-hypertension-cn-2024` · The 2024 revision of the Chinese Hypertension Guidelines prescribes ≥140/90 mmHg in the clinic for diagnosis, and <140/90 mmHg (further down to <130/80 mmHg if tolerated) as the target for general patients — T2, weakest: `ev-070`, `ev-074`, `ev-077`, `ev-078`
- `kb:med:prop-copd-gold-2026` · GOLD 2026 prescribes post-bronchodilator FEV1/FVC < 0.7 to confirm COPD, and lowers the E-group and treatment-escalation threshold to "≥1 moderate or severe exacerbation in the previous year — T2, weakest: `ev-074`, `ev-075`, `ev-079`
- `kb:physics:resource-phet-forces-and-motion-basics` · PhET simulation 'Forces and Motion: Basics' — T2, weakest: `ev-029`
- `kb:physics:resource-phet-my-solar-system` · PhET simulation 'My Solar System' — T2, weakest: `ev-032`
- `kb:life:resource-bj-subway-passenger-rules` · 《北京市轨道交通乘客守则》 (official document) — T2, weakest: `ev-043`
- `kb:life:prop-carried-item-limits` · Beijing subway sets hard size and weight limits on items passengers carry — T2, weakest: `ev-043`
- `kb:physics:ohm-law-scope-placement` · Where textbooks place the limitations of Ohm's law — T2, weakest: `ev-001`
- `kb:physics:voltage-symbol-u-v` · The U vs V voltage-symbol difference between Chinese and English textbooks — T2, weakest: `ev-001`
- `kb:med:prop-plague-treat-on-suspicion` · For suspected plague, WHO/CDC guidelines prescribe starting treatment without waiting for confirmation, and set explicit time limits for medication, isolation, and contact prophylaxis — T3, weakest: `ev-071`, `ev-072`, `ev-073`
- `kb:med:prop-ardsnet-low-tidal-volume` · For ARDS patients, low-tidal-volume ventilation reduces mortality — T3, weakest: `ev-048`
- …and 3 more — full list: `python tools/make_tasks.py --json`

### Concepts without a method (37)

> Find a marked classroom practice in a textbook ([BL]/[OL]/[AL]), create a 教法 entry and point its `knowledge_point` at the concept.

- `kb:physics:alternating-current` · Alternating current
- `kb:physics:polarization` · Polarization of light
- `kb:physics:light-interference-and-diffraction` · Light interference and diffraction
- `kb:physics:total-internal-reflection` · Total internal reflection
- `kb:physics:kp-torque` · Torque
- `kb:physics:ionizing-radiation-in-medicine` · Ionizing radiation in medicine
- `kb:physics:simple-pendulum` · Simple pendulum
- `kb:physics:transformer` · Transformer
- `kb:physics:ampere-force` · Ampere force
- `kb:physics:charged-particle-in-electric-field` · Motion of a charged particle in an electric field
- …and 27 more — full list: `python tools/make_tasks.py --json`

### Out-of-library prerequisites (2)

> First judge whether the prerequisite is really required (M-12); if you build a node, migrate the declarations to `edges.先修`.

- `angle` — 4 objects
- `vector` — 2 objects

### Outcomes covered by a single step (17)

> Add a second step for these outcomes (another explanation or entry point), or split them into smaller outcomes.

- Intro electrostatics (high school) —— o1, o2, o3, o4, o5, o6, o7
- Intro circuits (high school) —— o1, o2, o3, o4, o5, o6
- Alternating current (high school) —— o1, o2, o3, o4, o5
- Nucleus and radiation (high school) —— o1, o2, o3, o4, o5
- Mechanical oscillations (high school) —— o1, o2, o3, o4, o5
- Magnetism and electromagnetic induction (high school) —— o1, o2, o3, o5, o7
- Work, power and mechanical energy (high school) —— o1, o2, o3, o4
- Momentum and collisions (high school) —— o1, o2, o3, o4
- Thermodynamics (high school) —— o1, o2, o3, o4
- Quantum ideas and atoms (high school) —— o1, o2, o3, o4
- …and 7 more — full list: `python tools/make_tasks.py --json`

### Gaps the entries wrote themselves (110)

> Fill in what that sentence asks for, then delete the marker.

- `kb:computing:prop-http-1xx-interim-responses` · HTTP 1xx responses are interim: they MUST NOT be… — body: **待补**：§10.1.1（Expect）与 §7.8（Upgrade）的核读；主流代理转发 1xx 的实测
- `kb:computing:prop-http-202-no-async-status-resend` · HTTP 202 does not promise the request will ever … — body: **待补**：RFC 7231 §6.3.3 的对照；主流任务 API 的 202 + 轮询模式实测（只登记模式，不评优劣）
- `kb:computing:prop-http-204-cannot-contain-content-or-trailers` · An HTTP 204 response may contain neither content… — body: **待补**：RFC 7230–7235 对 204 的表述；主流客户端对 204 缓存行为的实测
- `kb:computing:prop-http-205-reset-document-view-no-content` · HTTP 205 requires the user agent to reset the 'd… — body: **待补**：RFC 7231 §6.3.6 的对照；主流浏览器对 205 重置行为的实测
- `kb:computing:prop-http-206-partial-content-header-duties` · An HTTP 206's Content-Length is not the complete… — body: **待补**：§14.2 / §14.6（Range 与 multipart/byteranges）的核读；主流 CDN 与静态服务器 206 头实测
- `kb:computing:prop-http-301-302-post-to-get-is-historical-307-forbids-method-change` · HTTP 301/302 changing POST to GET is a MAY 'for … — body: **待补**：[CACHING] §4.2.2 的可缓存状态码清单；RFC 7230–7235 对 301/302/303 的表述；「历史原因」的具体所指
- `kb:computing:prop-http-304-must-carry-cache-headers-and-no-body` · An HTTP 304 response MUST carry the cache header… — body: **待补**：[CACHING] §4.3.4；RFC 7230–7235 对 304 的表述；主流服务端 304 响应带 `ETag` 的实测
- `kb:computing:prop-http-400-vs-422-syntax-vs-semantics` · An HTTP 400 is a client error at the syntax or r… — body: **待补**：[RFC 4918]；RFC 7230–7235 对 400 的表述；主流 API 用 400 还是 422 的实测
- `kb:computing:prop-http-401-vs-403-must-carry-www-authenticate` · An HTTP 401 response MUST carry a WWW-Authentica… — body: **待补**：RFC 9110 §11.6.1；RFC 7230–7235 对 401/403 的表述；主流框架 401 响应是否带 `WWW-Authenticate` 的实测
- `kb:computing:prop-http-reserved-deprecated-codes` · HTTP 402 is 'reserved for future use', 305 is de… — body: **待补**：RFC 7231 Appendix B（305 旧语义）的核读；402 的启用状态（以注册表最新版为准）
- …and 100 more — full list: `python tools/make_tasks.py --json`

### Physics chapters still 🔴 (2)

> Collect the chapter's core concepts first, then write concept entries; the coverage page updates itself.

- 1 分子动理论
- 2 气体、固体和液体
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
