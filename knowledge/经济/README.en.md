# Economics

> [!IMPORTANT]
> **This subject holds "how an indicator is defined, what its statistical basis is, what figure the authorities published" — no forecasts, no advice.**
>
> The commonest error in economic material is not arithmetic but **picking the wrong basis**:
> year-on-year read as month-on-month, current prices read as constant prices, one survey
> unemployment rate taken for another. **A figure whose basis is not stated does not enter this
> repo** — when two numbers disagree, the first move is to check whether they share a basis,
> not to check who miscalculated.

> **English version of [`README.md`](README.md).**

## Current state

| Entry | Type | Status | Source |
|---|---|---|---|
| [National Bureau of Statistics, What is the survey unemployment rate](资源/国家统计局什么是调查失业率.en.md) | 资源 | 有效 | `ev-055` |
| [Being unemployed is defined by three conditions that must hold at once](命题/失业人口由三个条件界定.en.md) | 命题 | 暂定确认 | `ev-055` |
| [The survey and the registered urban unemployment rate are two different bases and cannot be compared or subtracted](命题/调查失业率与城镇登记失业率是两个不同口径.en.md) | 命题 | 暂定确认 | `ev-056` |
| [The urban survey unemployment rate is unsuitable as a basis for assessing employment work, and should not be cascaded down](命题/城镇调查失业率不宜作为考核依据也不宜层层分解.en.md) | 命题 | 暂定确认 | `ev-055` |
| [Taking the CPI to be the inflation rate](误解/把CPI当成通货膨胀率.en.md) | 误解 | 有效 | `ev-058` |
| [The three GDP accounting approaches should agree in theory; the difference in practice is called the statistical discrepancy and is permitted](命题/GDP三种核算方法理论一致但允许统计误差.en.md) | 命题 | 暂定确认 | `ev-059` |
| [GDP levels are at current prices and growth rates at constant prices; the two use different price bases](命题/GDP绝对额按现价计算增长速度按不变价计算.en.md) | 命题 | 暂定确认 | `ev-060` |

**All seven come from five official NBS documents** (`ev-055`—`ev-060`, verification depth full
text or four passages within the full text).

Coverage has widened from a single indicator to **three: the unemployment rate, the CPI and GDP**.
The existing entries **are still not** the same as the subject's boundary. See "What is still
missing".

### What is still missing

| Gap | Why it matters | Source needed |
|---|---|---|
| **The basis of other indicators** | for the CPI there is only "what it is not" — **the compilation method, basket, weights and base period are all absent**; there is **not one entry** on the PMI's 50 threshold; house prices, retail sales and other common indicators are likewise blank | the NBS's methodology notes for each indicator, with version and release date |
| **An actual release for any period** | all three GDP propositions rest on **table notes**, and **not one actual figure has been stored**; the same holds for the unemployment rate. This repo can currently answer "what is the basis" but not "what did release N say" | the NBS monthly release pages; the annual statistical communiqué |
| **The GDP revision rules** | §3 of the annex to `ev-060` states plainly that preliminary figures are revised afterwards, **and this repo checks no revision trigger, frequency or magnitude**. That bears directly on whether "comparing last period's figure with this period's" is legitimate | the full text of that annex §3, plus the release notes for the final figures |
| **The original ILO / IMF / OECD standards** | both explainers retell the ILO's classification, **and not a single ILO document is registered here**. Whether the retelling matches the original, this repo cannot judge | the ILO standard on employment and unemployment statistics; the relevant chapter of the IMF *Manual* |
| **The Ministry's own basis document for the registered rate** | `ev-056` is only the NBS's retelling of the Ministry's basis; **this repo has not read the Ministry's own definition** | the relevant rules and notes of the Ministry of Human Resources and Social Security |

> [!NOTE]
> This subject's pre-existing section "**Data changes; timeliness is the main point of attack**"
> remains in force, and **this round added a new way it can trigger**:
> for `ev-058` (the CPI) **the printed release date and the date in the URL path disagree**, so
> this repo can determine neither the true release date nor whether the page has been re-published.
> **This is not "the page is too old" but "even when it was posted cannot be checked"** — timeliness
> attack here is not expiry but **an unverifiable release date**.
> **This repo has no version-detection mechanism**; that limitation is in the section below.

## Boundary

| | Holds | Does not hold |
|---|---|---|
| content | indicator definitions and statistical bases, the original wording of official releases | forecasts, directional calls, allocation or policy advice |
| source | **formal releases** by statistical agencies, central banks or international organisations, with a period and release date | second-hand retellings, summaries of institutional opinion |
| phrasing | "indicator X has basis Y (publisher · period · to be verified)" | "this year will …" |

**This repo does not judge "which way the economy goes"** — that cannot be checked clause by
clause against a source, and it is exactly where opinion creeps in. What can be held is a
definition or figure that has **already been released, is clickable, and carries a period**.

### Data changes; timeliness is the main point of attack

The next release can overturn or supersede a single economic entry. This repo handles it the
same way as the two rules in [Daily life](../生活/README.en.md): **an entry records "what release
N said", not "what the economy is like now"**; when a newer release arrives, the old entry moves
to `已失效` (expired) rather than being rewritten in place.

> [!NOTE]
> This repo has **no version-detection mechanism**, and `已失效` has never actually been
> triggered — that limitation is noted in [Daily life](../生活/README.en.md) ("two things still
> noted, not yet changed"), and this subject is bound by it too.

### Relation to medical guidelines

**Medical guidelines are not a separate subject.** Operating parameters stipulated by clinical
guidelines belong to [Medicine](../医学/README.en.md); the admission rule and the disclaimer
requirement are set out in that page's "a correction to the boundary". This subject covers only
economic statistics and economic texts.

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-12 | second batch of 3 entries registered (1 `误解` + 2 `命题`), sources `ev-058` / `ev-059` / `ev-060`; coverage widened from the unemployment rate to the CPI and GDP; "What is still missing" rewritten against the gaps this round exposed | topic chosen against the subject boundary after ev-058/059/060 were registered | @hpleapfrog |
| 2026-10-12 | first batch of 4 entries registered (1 `资源` + 3 `命题`), sources `ev-055` / `ev-056`; "Current state" changed from "no entries yet" to an entry table, and "What is still missing" added | topic chosen against the subject boundary after ev-055/056 were registered | @hpleapfrog |
| 2026-10-12 | established the subject; added `econ` to `SUBJECT_SLUGS` | user asked to expand the knowledge domains (transport / computing / medical guidelines / economics) | @hpleapfrog |
| 2026-10-12 | stated that **medical guidelines get no separate subject** and belong to [Medicine](../医学/README.en.md) | the threshold and disclaimer rules already exist for guidelines; a second set would drift | @hpleapfrog |
