# Evidence Index

Shared by the whole repo. Each `知识点`'s `front-matter` cites entries here by number.

> **English version of [`README.md`](README.md).**

## Threshold

**Discussion may say anything, but only evidence past the threshold enters the judgment.**

A verifiable locator is required: ISBN + edition + page / DOI / official-document clause / public dataset / a re-runnable script with its data.

> [!CAUTION]
> **Never upload textbook originals or scan pages.**
> Store only page locators, short quotations, original summaries, and conclusions. Facts and data are not copyrightable; **expression** is.

### The locator must be **verifiable**, not something that "looks like a locator"

> The full story (why those section numbers were invented, how two conventions contradicted each other) is in
> [decision record: the evidence incidents](../docs/decisions/evidence-history.en.md).

**All now written verifiably**: `Chapter N · module title`, plus the module id (clickable to the original).

| Not verifiable | Verifiable |
|---|---|
| `§16.1 Reflection` | `第 16 章 · Reflection` + module [m54357](https://github.com/openstax/osbooks-physics/blob/main/modules/m54357/index.cnxml) |

> [!IMPORTANT]
> **Matching ≠ exact.** The **printed** textbook does have section numbers,
> but they are **not in the source file we read**.
> **Writing a number we cannot verify is forging a locator** — even if it happens to be right.
>
> If section numbers are ever to be written, they must be **checked against the print or official web edition**, and the basis noted in the evidence row.

### Is the source itself real: **three questions**

**A legal locator ≠ true content.** Someone can **build a website, write the fake knowledge onto it, and wait for others to cite it** —
that page has a well-formed DOI, a plausible document number and a link that opens;
**only the content was manufactured for this very citation**. So before registering an evidence row, three questions must all be answerable:

| # | Question | What counts as answered | Not answered |
|---|---|---|---|
| 1 | **Who publishes it** | an accountable body: publisher · journal · standards organisation · government agency · university | personal sites, attribution-free repost pages |
| 2 | **Which version, and when did it take effect** | the publication / effective date and the version (amendment number, document number, issue) are all recorded | the page carries no version; or "was true once" is treated as "is still true" |
| 3 | **Was it made up for this citation** | it exists for **reasons independent of the claim** (a statute is issued to govern, a standard to interoperate, statistics to be published), and a second source can be found at **a different publishing body** | a page that exists only to assert this one sentence; several same-origin reposts |

> [!IMPORTANT]
> **Question 2 is about *version*, not about *who came first*.**
> **Knowledge changes** — statutes get amended, standards get revised, pages get rewritten.
> "This page predates this repo" neither shows the content is true nor that it **still holds now**.
> So the question answered here is **which version the claim applies to**; the entry scopes itself
> via `scope.条件` and **claims only that version**.

> [!IMPORTANT]
> **Question 3 guards against two things at once: fabrication, and the illusion of "cross-corroboration".**
> It does not ask "does it predate us", but **"would this source still exist if the claim were false"** —
> a page born only to assert one sentence is exactly the shape of `ev-002`.
> Separately: three sites copying the same false sentence at each other are still one source.
> **Independence is counted by publishing body, not by number of domains or links.**

**Identifiers must be reverse-checked**: the title a DOI resolves to, and the name a document number yields on the publisher's official site,
**must match what we registered**. Well-formed but not resolvable = **stop** —
that is exactly the shape of `ev-002`: **everything looked right except that it wasn't true.**

> [!CAUTION]
> **Mechanical backstop (`R-EVID-03`)**: evidence whose `核验深度` is `未核验` (never opened) or `仅定位`
> (opened, but the body never read) **cannot alone** lift an entry to `暂定确认` / `已确证`.
>
> **If you haven't read it, you cannot say you confirmed it.** A well-formed locator
> only proves **that it is there**; it does not prove **what it says**.

## An incident of our own: registering **constructed** data as "experimental data"

> The full story is in [decision record: the evidence incidents](../docs/decisions/evidence-history.en.md) —
> including **why it fooled an adversarial review**: **it was the repo itself that excluded "verifying whether the evidence exists" from the adversarial scope.**

### Two rules established as a result

| # | Rule |
|---|---|
| 1 | **Data the repo produces itself must be marked "constructed" or "measured".** The words "experimental data" claim a measurement happened — **no measurement, no such words** |
| 2 | **Quantitative evidence must register significant figures / uncertainty / repetitions.** Without them, that evidence **supports only the precision it declares**; if the conclusion needs better precision than the data, **the evidence counts as "illustrative", not evidence** |

> **Deleting the trace really does lose information** — the `ev-002` number is kept, the file renamed to
> [`构造数据-欧姆定律演示.csv`](构造数据-欧姆定律演示.csv) (its **demonstration value** remains:
> it does show what an Ohmic relation looks like, **it just cannot support any proposition about the real world**).

> [!IMPORTANT]
> **For a claim of the form "the official document stipulates X", the official original is the primary source — it does not queue on the ladder.**
> So `ev-043` is registered as "high", for a different reason than `ev-002` (recomputable ≠ evidence strength). Full explanation in
> [decision record: the evidence incidents](../docs/decisions/evidence-history.en.md).

> [!IMPORTANT]
> **The evidence ladder is designed for "empirical propositions about populations" — it is unfair to physics** (an `F = ma` in a textbook falls to the lowest tier,
> which is not the same thing as "a teaching suggestion in a textbook"). This is a known issue, not changed. Full discussion in
> [decision record: the evidence incidents](../docs/decisions/evidence-history.en.md).

## Index

> [!NOTE]
> **Header meanings** (machine-parsed by `tools/kbcheck.py`):
>
> - **类别 (category)**: `教材` · `论文` · `指南` · `官方文件` · `交互式模拟` · `出版社勘误表` · `本库数据` (voided rows marked `已作废`);
> - **等级 (grade)**: `高` / `中` / `低` — **for that kind of claim**, not absolutely (see "Grade notes" at the end);
> - **核验深度 (verification depth)**: what the repo **actually read** — `全文` / `摘要` / `仅定位` / `未核验`.
>   **This column makes "how far we actually checked" visible**, instead of relying on a sentence in the body.

| 编号 | 类别 | 等级 | 核验深度 | 定位 | 时间 | 许可 | 引用处 |
|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
| ev-001 | 教材 | 低 | 仅定位 | 《义务教育教科书·物理》九年级全一册，人教版，2013，P.79 | 2013 | 外部来源 · 仅引用定位 | 欧姆定律 · 电压符号差异 |
| ev-002 | ⚠️ **已作废** | — | — | 原登记为「实验数据」的 `导体U-I数据.csv`。**从未有任何测量发生**——数值由本库作者构造（`U = 10 × I`，R 精确等于 10.000） | — | — | 引用它的条目已重写 |
| ev-009 | ⚠️ **已作废** | — | — | 本库**构造的示例数据**（「某校初三 2 个班对照观察」），**从未真实存在** | — | — | 无（原引用条目已重写） |
| ev-010 | ⚠️ **已作废** | — | — | 本库**构造的示例数据**（「本科物理课观察」），**从未真实存在** | — | — | 无（原引用条目已重写） |
| ev-011 | ⚠️ **已作废** | — | — | 本库**构造的示例数据**（「初三学完后测」），**从未真实存在** | — | — | 无（原引用条目已删除） |
| ev-012 | ⚠️ **已作废** | — | — | 本库**构造的示例数据**（「高中生测评」），**从未真实存在** | — | — | 无（原引用条目已删除） |
| ev-014 | 出版社勘误表 | 高 | 全文 | OUP《高中活學地理（第三版）》勘誤表，重印兼訂正 2024，[PDF](https://eresources.oupchina.com.hk/debundling/corrigenda/ssgeog3e_re_corrigenda_core_c_2024.pdf) | 2024 | 外部来源 · 仅引用定位 | 地理勘误 ×6 |
| ev-015 | 出版社勘误表 | 高 | 全文 | 雅集《科學新世紀 1A》勘誤表，[ZIP](https://e-aristo.hk/t/downloads/science/scicent_amendments_2024_c.zip) | 2024 | 外部来源 · 仅引用定位 | 科学勘误 ×1 |
| ev-016 | 教材 | 低 | 全文 | OpenStax《College Physics 2e》§20.3 Ohm's Law: Resistance and Simple Circuits，[m42344](https://raw.githubusercontent.com/openstax/osbooks-college-physics-bundle/main/modules/m42344/index.cnxml) | 2020 | **CC BY-NC-SA 4.0** · 仅引用定位与短引用 | 摩擦类比 · 局限性位置 · 电压符号差异 |
| ev-017 | 教材 | 低 | 全文 | OpenStax《College Physics 2e》§20.1 Current，[m42341](https://raw.githubusercontent.com/openstax/osbooks-college-physics-bundle/main/modules/m42341/index.cnxml) | 2020 | **CC BY-NC-SA 4.0** · 仅引用定位与短引用 | 电流（备用） |
| ev-018 | 教材 | 低 | 全文 | OpenStax《Physics》第 19 章 · Ohm's law，[m54437](https://github.com/openstax/osbooks-physics/blob/main/modules/m54437/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 欧姆定律 · 水管类比 · 电流方向误解 · 类比选择与学段相关 |
| ev-019 | 教材 | 低 | 全文 | OpenStax《Physics》第 19 章 · Series Circuits，[m54435](https://github.com/openstax/osbooks-physics/blob/main/modules/m54435/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 水管类比（做法与禁忌） |
| ev-020 | 教材 | 低 | 全文 | OpenStax《Physics》**全 23 章 / 98 模块**的 Teacher Support。**脚本** [`os-teacher-markers.py`](os-teacher-markers.py) · **明细** [`os-teacher-markers.csv`](os-teacher-markers.csv) · ref `main` **commit `dfdfd7a5356ecdd42e504de3df50d9153e33ea49`** | 2020 | **CC BY 4.0** · **可自由复用** | 教材内建分组教学变体 |

> [!CAUTION]
> **ev-020 originally wrote only "580 entries, with 649 grouping markers", while the repo held neither script nor data** —
> that row was therefore hit by an adversarial review ([attack entry](../knowledge/physics/claims/attacks/tieredguidance.en.md)'s `A4`).
>
> **Script + details + commit hash are now supplied.** Current numbers:
>
> | 口径 | `os-teacher` 便签 | BL | OL | AL | EL | 合计 |
> |---|---|---|---|---|---|---|
> | **宽松**（note 里任意出现） | **582** | 207 | 245 | 191 | **5** | **648** |
> | 严格（`<para>` 开头的 `<span>`） | — | 205 | 243 | 189 | 0 | 637 |
>
> **Neither the old 649 nor the 580 is right** — it was **a snapshot of some `main`**.
> The differences in `EL` (6→5), total (649→648), and notes (580→582) come from **`main` moving forward**.
>
> **Lesson: hard-coding a drifting number turns it into an assertion.** A number must be given **with its rule + commit**.

| ev-021 | 教材 | 低 | 全文 | OpenStax《Physics》第 2 章 · Relative Motion, Distance, and Displacement，[m54108](https://github.com/openstax/osbooks-physics/blob/main/modules/m54108/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 参考系教法 ×3 · 参考系误解 |
| ev-022 | 教材 | 低 | 全文 | OpenStax《Physics》第 2 章 · Speed and Velocity，[m54104](https://github.com/openstax/osbooks-physics/blob/main/modules/m54104/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 速度与速率教法 ×2 |
| ev-023 | 教材 | 低 | 全文 | OpenStax《Physics》第 2 章 · Position vs. Time Graphs，[m54110](https://github.com/openstax/osbooks-physics/blob/main/modules/m54110/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 位置-时间图教法 ×2 |
| ev-024 | 教材 | 低 | 全文 | Utah State Board of Education《7th Grade Science》（SEEd 标准），[PDF](https://www.uen.org/emedia/resources/oer/7thGradeSEEd.pdf)，148 页 | 2020 | **CC BY-NC-SA 3.0** · **仅引用定位与短语** | 力与运动（初中）· 现象探究循环 |
| ev-025 | 教材 | 低 | 全文 | OpenStax《Physics》第 4 章 · Newton's First Law of Motion: Inertia，[m54138](https://github.com/openstax/osbooks-physics/blob/main/modules/m54138/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 惯性 · 惯性教法 ×2 · 运动物体自然慢下来 |
| ev-026 | 教材 | 低 | 全文 | OpenStax《Physics》第 16 章 · Reflection，[m54357](https://github.com/openstax/osbooks-physics/blob/main/modules/m54357/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 光的反射 · 反射教法 ×2 |
| ev-027 | 教材 | 低 | 全文 | OpenStax《Physics》第 14 章 · Speed of Sound, Frequency, and Wavelength，[m54331](https://github.com/openstax/osbooks-physics/blob/main/modules/m54331/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 声速与频率 · 声速教法 ×2 |
| ev-028 | 教材 | 低 | 全文 | OpenStax《Physics》第 9 章 · Mechanical Energy and Conservation of Energy，[m54273](https://github.com/openstax/osbooks-physics/blob/main/modules/m54273/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 机械能守恒 · 机械能教法 ×2 · 运动物体自然慢下来 |
| ev-029 | 交互式模拟 | 低 | 仅定位 | PhET「Forces and Motion: Basics」，[直达链接](https://phet.colorado.edu/sims/html/forces-and-motion-basics/latest/forces-and-motion-basics_en.html)；教材内入口为 OpenStax 短链 `openstax.org/l/forcesandmotion`（实测解析到该直达链接） | 2026 | **CC BY-NC 4.0** · **仅引用定位** | PhET 力与运动基础（本库第一条 `资源`） |
| ev-030 | 教材 | 低 | 全文 | OpenStax《Physics》第 15 章 · The Electromagnetic Spectrum，[m54342](https://github.com/openstax/osbooks-physics/blob/main/modules/m54342/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 电磁波谱 · 电磁波谱教法 ×2 · 可见光误解 |
| ev-031 | 教材 | 低 | 全文 | OpenStax《Physics》第 7 章 · Kepler's Laws of Planetary Motion，[m54192](https://github.com/openstax/osbooks-physics/blob/main/modules/m54192/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 开普勒定律 · 开普勒教法 ×2 |
| ev-032 | 交互式模拟 | 低 | 仅定位 | PhET「My Solar System」，[直达链接](https://phet.colorado.edu/sims/html/my-solar-system/latest/my-solar-system_en.html)；教材内入口为 OpenStax 短链 `openstax.org/l/28mysolar` | 2026 | **CC BY-NC 4.0** · **仅引用定位** | PhET 我的太阳系（第二条 `资源`） |
| ev-033 | 教材 | 低 | 全文 | OpenStax《Physics》第 13 章 · Types of Waves，[m54314](https://github.com/openstax/osbooks-physics/blob/main/modules/m54314/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 波（知识点）· 波教法 BL · 波把物质一起推走 |
| ev-034 | 教材 | 低 | 全文 | OpenStax《Physics》第 13 章 · Wave Properties: Speed, Amplitude, Frequency, and Period，[m54321](https://github.com/openstax/osbooks-physics/blob/main/modules/m54321/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 波（知识点）· 波教法 OL |
| ev-035 | 教材 | 低 | 全文 | OpenStax《Physics》第 22 章 · The Structure of the Atom，[m54582](https://github.com/openstax/osbooks-physics/blob/main/modules/m54582/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 原子结构 · 原子结构教法 ×3 |
| ev-036 | 教材 | 低 | 全文 | OpenStax《Physics》第 9 章 · Work, Power, and the Work–Energy Theorem，[m54271](https://github.com/openstax/osbooks-physics/blob/main/modules/m54271/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 功与功率 · 功与功率教法 ×2 |
| ev-037 | 教材 | 低 | 全文 | OpenStax《Physics》第 7 章 · Newton's Law of Universal Gravitation and Einstein's Theory of General Relativity，[m54189](https://github.com/openstax/osbooks-physics/blob/main/modules/m54189/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 万有引力定律 · 万有引力教法 ×2 · 混淆 G 与 g |
| ev-038 | 教材 | 低 | 全文 | OpenStax《Physics》第 16 章 · Refraction，[m54365](https://github.com/openstax/osbooks-physics/blob/main/modules/m54365/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 光的折射 · 折射教法 ×3 |
| ev-039 | 教材 | 低 | 全文 | OpenStax《Physics》第 3 章 · Acceleration，[m54123](https://github.com/openstax/osbooks-physics/blob/main/modules/m54123/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 加速度 · 加速度教法 ×2 |
| ev-040 | 教材 | 低 | 全文 | OpenStax《Physics》第 4 章 · Newton's Second Law of Motion，[m54142](https://github.com/openstax/osbooks-physics/blob/main/modules/m54142/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 牛顿第二定律 · 牛顿第二定律教法 ×2 |
| ev-041 | 教材 | 低 | 全文 | OpenStax《Physics》第 4 章 · Force，[m54135](https://github.com/openstax/osbooks-physics/blob/main/modules/m54135/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 力（高中）· 力教法 ×2 |
| ev-042 | 教材 | 低 | 全文 | OpenStax《Physics》第 4 章 · Newton's Third Law of Motion，[m54131](https://github.com/openstax/osbooks-physics/blob/main/modules/m54131/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 牛顿第三定律 · 牛顿第三定律教法 ×2 |
| ev-043 | 官方文件 | 高 | 仅定位 | 《北京市轨道交通乘客守则》，北京市交通委员会发布，**2021-09-28 施行**，[北京地铁官网「乘车规定」页](https://www.bjsubway.com/support/ccgd/)（同页另列 10 份票务规则文件） | 2021 | 官方公开文件 · **仅引用条款，不上传原文** | 携带物品的尺寸重量上限 |
| ev-044 | 官方文件 | 高 | 全文 | 《公共航空运输旅客服务管理规定》，**交通运输部令 2021 年第 3 号**，**2021-09-01 施行**（同时废止 1996 年《国内运输规则》等三份旧规则），[交通运输部政府信息公开](https://xxgk.mot.gov.cn/2020/jigou/fgs/202103/t20210315_3530413.html)（索引号 000019713O03/2021-00021；**本库打开该页并逐条核对全文十章**，止于第六十四条附则） | 2021 | 官方公开规章 · **仅引用条款号与短引用，不上传原文** | 非自愿退票与变更、超售处置、运输总条件的追溯禁令、投诉处理时限、托运行李同机运送与免费直送 |
| ev-045 | 教材 | 低 | 全文 | OpenStax《Physics》第 8 章 · Linear Momentum, Force, and Impulse，[m54215](https://github.com/openstax/osbooks-physics/blob/main/modules/m54215/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 动量和冲量 · 动量和冲量教法 ×1 |
| ev-046 | 教材 | 低 | 全文 | OpenStax《Physics》第 8 章 · Conservation of Momentum，[m54202](https://github.com/openstax/osbooks-physics/blob/main/modules/m54202/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 动量守恒定律 · 动量守恒教法 ×2 |
| ev-047 | 教材 | 低 | 全文 | OpenStax《Physics》第 8 章 · Elastic and Inelastic Collisions，[m54209](https://github.com/openstax/osbooks-physics/blob/main/modules/m54209/index.cnxml) | 2020 | **CC BY 4.0** · **可自由复用** | 弹性碰撞与非弹性碰撞 |
| ev-048 | 论文 | 高 | 摘要 | The Acute Respiratory Distress Syndrome Network. *Ventilation with Lower Tidal Volumes as Compared with Traditional Tidal Volumes for Acute Lung Injury and the Acute Respiratory Distress Syndrome.* **N Engl J Med. 2000 May 4;342(18):1301-8.** **PMID [10793162](https://pubmed.ncbi.nlm.nih.gov/10793162/)** · **DOI [10.1056/NEJM200005043421801](https://doi.org/10.1056/NEJM200005043421801)** | 2000 | 外部文献 · **仅引用摘要与结论，不转载全文** | ARDS 低潮气量通气 |
| ev-049 | 指南 | 高 | 全文 | Kushida CA, Chediak A, Berry RB, et al. *Clinical guidelines for the manual titration of positive airway pressure in patients with obstructive sleep apnea.* **J Clin Sleep Med. 2008;4(2):157-171.** **PMID [18468315](https://pubmed.ncbi.nlm.nih.gov/18468315/)** · [AASM 官方 PDF](https://aasm.org/resources/clinicalguidelines/040210.pdf)（**本库下载并全文抽取核对**，15 页） | 2008 | 外部文献 · **仅引用条目编号与短引用，不转载全文** | 睡眠呼吸暂停 PAP 调定 |
| ev-050 | 论文 | 高 | 摘要 | Rosen CI, Auckley DH, Benca R, et al. *Multisite Randomized Trial of Portable Sleep Studies and Positive Airway Pressure Autotitration Versus Laboratory-Based Polysomnography for the Diagnosis and Treatment of Obstructive Sleep Apnea: The HomePAP Study.* **SLEEP 2012;35(6):757-766.** [PMC3353048](https://pmc.ncbi.nlm.nih.gov/articles/PMC3353048/)（**开放获取，本库读了摘要与方法部分**） | 2012 | 外部文献 · **仅引用摘要与结论，不转载全文** | 睡眠呼吸暂停 PAP 调定 |
| ev-051 | 官方文件 | 高 | 全文 | *Road Traffic Safety Law of the People's Republic of China*, passed by the NPC Standing Committee on 2003-10-28, **amended for the third time on 2021-04-29**, **in force since 2004-05-01**; [State Administration for Market Regulation "Government Information Disclosure" page](https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/bgt/art/2023/art_79dc72ea621f4a9b8adec327abf5d0e1.html) (publication date 2021-04-29; **this repo opened the page and checked the text article by article, ending at Article 124**); the same text cross-checked at a different publishing body: [NPC gazette page, 2008](http://www.npc.gov.cn/zgrdw/wxzl/gongbao/2008-02/23/content_1462422.htm) · [Ministry of Transport law database PDF](https://big5.mot.gov.cn/gate/big5/law.mot.gov.cn:80/exportPDFLaw.action?law.id=37) | 2021 | 官方公开法律 · **cite article numbers and short quotes only; no full text uploaded** | fine receipts · late-payment surcharge · provincial execution standards · drunk-driving consequences · fine quotas |
| ev-052 | 官方文件 | 高 | 全文 | *Key words for use in RFCs to Indicate Requirement Levels*, IETF, **BCP 14 · RFC 2119**, published 1997-03, [full text at rfc-editor.org](https://www.rfc-editor.org/rfc/rfc2119.txt) (**this repo read the whole document**, including the five keyword definitions in §1–§5, the usage constraint in §6 and the security note in §7) | 1997 | official public specification · **cite section numbers and short quotes only; no full text reproduced** | RFC requirement keywords |
| ev-053 | 官方文件 | 高 | 全文 | *Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words*, IETF, **BCP 14 · RFC 8174** (Updates: 2119), published 2017-05, [full text at rfc-editor.org](https://www.rfc-editor.org/rfc/rfc8174.txt) (**this repo read the whole document**; §2 gives an OLD / NEW side-by-side of the amended text) | 2017 | official public specification · **cite section numbers and short quotes only; no full text reproduced** | RFC requirement keywords |
| ev-054 | 官方文件 | 高 | 全文 | *HTTP Semantics*, IETF, **STD 97 · RFC 9110** (Obsoletes: 2818, 7230–7235, 7538, 7615, 7694; Updates: 3864), published 2022-06, [full text at rfc-editor.org](https://www.rfc-editor.org/rfc/rfc9110.txt) (**this repo has verified**: §2.2 requirements-notation clause, §9.2.1 safe methods, §9.2.2 idempotent methods, and **all of §15** — §15.1's overview and the class preambles, then every individual-code subsection §15.2.1–§15.6.6 (including §15.3.7.1–§15.3.7.3); the document is 10,785 lines, and **the remaining sections are unchecked**) | 2022 | official public specification · **cite section numbers and short quotes only; no full text reproduced** | HTTP method safety and idempotency · the status-code extensibility rules · the §15 individual-code entries |
| ev-055 | 官方文件 | 高 | 全文 | National Bureau of Statistics, *What is the survey unemployment rate*, published **2025-02-28 10:00**, [full text on the NBS site](https://www.stats.gov.cn/zs/tjws/tjzb/202301/t20230101_1903672.html) (**this repo read the whole document**: §1 concept, §2 statistical method, §3 how to read it, including the text descriptions of Figure 1 "classification of the population aged 16 and over" and Figure 2 "national urban survey unemployment rate") | 2025 | official public statistical explainer · **cite section headings and short quotes only; no full text reproduced** | the three conditions for unemployment · the 340,000-household sample and relative error · the rate is unsuitable for assessment and for cascading down |
| ev-056 | 官方文件 | 高 | 全文 | National Bureau of Statistics, *What is the difference between the survey unemployment rate and the registered urban unemployment rate*, published **2021-02-18 16:26**, [full text on the NBS site](https://www.stats.gov.cn/zt_18555/zthd/sjtjr/d12kfr/tjzsqzs/202302/t20230216_1908907.html) (**this repo read the whole document**: three differences — statistical method / definition of employment and unemployment / statistical coverage; the whole page is under one screen) | 2021 | official public statistical explainer · **cite the names of the differences and short quotes only; no full text reproduced** | the basis difference between the survey and registered urban unemployment rates |
| ev-057 | 官方文件 | 高 | 全文 | *Hypertext Transfer Protocol (HTTP) Status Code Registry*, IANA (Internet Assigned Numbers Authority), **last updated 2025-09-15**, [full registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) (**this repo read the whole table**: registration procedure **IETF Review**, reference **RFC 9110 §16.2.1**, plus every assigned entry in 100–599 and the Unassigned ranges) | 2025 | official public registry · **cite entries and short quotes only; no full table reproduced** | the complete list of HTTP status codes · 418 and 306 as (Unused) · 104 as a temporary registration |
| ev-058 | 官方文件 | 高 | 全文 | National Bureau of Statistics, *What is the Consumer Price Index (CPI)*, **page dated 2024-09-13 10:00** (the URL path reads `202409/t20240910_1956353.html`, so **the path date and the printed date disagree and this repo cannot determine the true release date**), [full text on the NBS site](https://www.stats.gov.cn/zs/tjws/zytjzbqs/jmxxggzs/202409/t20240910_1956353.html) (**this repo read the whole document**: §1 the definition; §2 the three uses — indicating the degree of inflation/deflation, national economic accounting, computing the purchasing power of money) | 2024 | official public statistical explainer · **cite the definition, the names of the uses and short quotes only; no full text reproduced** | CPI as a relative number measuring change · CPI is not the inflation rate · CPI used to deflate current-price aggregates · the reciprocal of CPI as the purchasing power index |
| ev-059 | 官方文件 | 高 | 全文 | National Bureau of Statistics, *How is GDP accounted?*, published **2021-02-18 15:51**, [full text on the NBS site](https://www.stats.gov.cn/zt_18555/zthd/sjtjr/d12kfr/tjzsqzs/202302/t20230216_1908936.html) (**this repo read the whole document**: one paragraph each for the production, income and expenditure approaches with their accounting formulas, and a closing paragraph stating that the results should agree in theory, that differences arise in practice because the data sources differ, that this difference is called the statistical discrepancy, and that it is permitted within an acceptable range) | 2021 | official public statistical explainer · **cite the names of the approaches, the formulas and short quotes only; no full text reproduced** | the three GDP accounting approaches and their formulas · agreement in theory but a statistical discrepancy in practice · the discrepancy is permitted |
| ev-060 | 官方文件 | 高 | 全文 | National Bureau of Statistics, *Preliminary national accounts for Q3 2025*, published **2025-10-21 09:30**, [full text on the NBS site](https://www.stats.gov.cn/sj/zxfb/202510/t20251021_1961646.html) (**this repo verified four passages verbatim**: note 1 under Table 1, "levels at current prices, growth rates at constant prices"; the note under Table 3, "quarter-on-quarter growth rates are seasonally adjusted"; annex §1.1, "quarterly GDP is accounted for on the basis of the production approach"; annex §2.3.2, "the constant-price base year changes every five years; the base year for 2021–2025 is 2020"; **the figures in Table 1 and the rest of the annex were not checked one by one**) | 2025 | official public statistical release · **cite the table notes and short quotes only; no figures reproduced** | GDP levels at current prices but growth rates at constant prices · quarterly GDP based on the production approach · quarter-on-quarter growth seasonally adjusted · the constant-price base year changes every five years |
| ev-061 | 官方文件 | 高 | 全文 | National Bureau of Statistics, *How the CPI is compiled*, page-dated **2024-11-29 10:00** (the URL path reads `202411/t20241127_1957589.html`, so **the date in the path does not match the date on the page; this repo cannot determine the real publication date**), [full text on the NBS site](https://www.stats.gov.cn/zs/tjws/zytjzbqs/jmxxggzs/202411/t20241127_1957589.html) (**this repo read the whole document**: §1 basic setup; §2 the basket and the weights — the basket changes every five years, 8 major groups and 268 elementary classes, luxuries and investment goods excluded, weights drawn from the household income-and-expenditure survey; §3 how representative items are chosen — five selection principles and the selection process; §4 how price-collection points are chosen — four principles and the sampling method; §5 price data collection; §6 how the CPI is computed — definitions of the month-on-month, year-on-year, average and fixed-base indices, the fixed-base series running from 2001, and the chained Laspeyres formula) | 2024 | official public statistical explainer · **cite class counts, method names and short quotes only; no formula images or full text reproduced** | the CPI basket changes every five years · the CPI excludes luxuries and investment goods · the CPI uses the chained Laspeyres formula · the CPI fixed-base series starts in 2001 and changes base every five years |
| ev-062 | 官方文件 | 高 | 全文 | National Bureau of Statistics, *Interview with the head of the Urban Survey Department on the base-year rotation of price indices*, dated **2021-02-10** (index number `410A04-0502-202102-0002`, marked "valid"), [full text on the NBS site](https://www.stats.gov.cn/xxgk/jd/sjjd2020/202102/t20210210_1813322.html) (**this repo read the whole document**: four question-and-answer pairs — why rotate; what the rotation changed (elementary classes 262 → 268, newly added takeout meals, new-energy cars, ride-hailing fares and other emerging goods and services, the exact percentage-point rises and falls in weights, and the removal of African swine fever and pandemic distortions); the effect on the indices (about 0.03 percentage points on CPI year-on-year on average); what the new base year will do) | 2021 | official public statistical explainer · **cite class counts, percentage points and short quotes only; no full text reproduced** | the CPI base year rotates every five years on years ending in 5 and 0 · elementary classes raised from 262 to 268 · the rotation moves CPI year-on-year by about 0.03 percentage points |
| ev-063 | 论文 | 高 | 全文 | The RECOVERY Collaborative Group. *Dexamethasone in Hospitalized Patients with Covid-19 — Preliminary Report.* **N Engl J Med. 2020 Jul 17 (online); final version N Engl J Med. 2021;384(8):693-704.** **PMID [32678530](https://pubmed.ncbi.nlm.nih.gov/32678530/)** · **DOI [10.1056/NEJMoa2021436](https://doi.org/10.1056/NEJMoa2021436)** · [PMC7383595](https://pmc.ncbi.nlm.nih.gov/articles/PMC7383595/) (**open access; this repo read the full text**: methods, results, Tables 1–2, Figures 2–3, discussion; **checked the mortality rates, rate ratios and confidence intervals of all three respiratory-support strata paragraph by paragraph**) | 2020 | external literature · **cite only the abstract and conclusions; no full text reproduced** | Covid-19 dexamethasone stratified by respiratory-support level |
| ev-064 | 官方文件 | 高 | 全文 | UN News: *Testing and monitoring underway in suspected Russia plague death*, **2026-10-06**, [news.un.org](https://news.un.org/en/story/2026/10/1168533) (WHO spokesperson Christian Lindmeier, Geneva briefing; **this repo read the whole report**) | 2026 | official public release · **short quotes and conclusions only; no full text reproduced** | the Irkutsk anti-plague institute event |
| ev-065 | 官方文件 | 高 | 摘要 | Statement of Rospotrebnadzor, **2026-10-04**, via *Rossiyskaya Gazeta* (rg.ru), [rg.ru](https://rg.ru/2026/10/04/v-rospotrebnadzore-zaiavili-ob-otsutstvii-chumy-v-gorodah-irkutskoj-oblasti.html) (**this repo read a media report, not the original official page**) | 2026 | official public statement (via media) · **short quotes only; no full text reproduced** | the Irkutsk anti-plague institute event |
| ev-066 | 官方文件 | 高 | 仅定位 | Russia lifted the Irkutsk quarantine (**2026-10-08**, Russian state news agency), via [Kyiv Independent](https://kyivindependent.com/russia-lifts-quarantine-in-irkutsk-region-where-lab-worker-allegedly-died-of-plague/) (**media report only; original official page not opened**) | 2026 | official public action (via media) · **short quotes only; no full text reproduced** | the Irkutsk anti-plague institute event |
| ev-067 | 官方文件 | 高 | 全文 | World Health Organization (WHO), *Disease Outbreak News: Pneumonia of undetermined etiology – the Russian Federation*, **published 2026-10-10**, **2026-DON620**, [who.int](https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON620) (**this repo read the whole DON**: Situation at a glance / Description / Public health response / WHO risk assessment / WHO advice) | 2026 | official public release · **short quotes and conclusions only; no full text reproduced** | the Irkutsk anti-plague institute event |
| ev-068 | 官方文件 | 高 | 全文 | European Centre for Disease Prevention and Control (ECDC), *ECDC closely monitoring situation following case of pneumonia of unknown origin in Russia*, **published 2026-10-06**, [ecdc.europa.eu](https://www.ecdc.europa.eu/en/news-events/ecdc-closely-monitoring-situation-following-case-pneumonia-unknown-origin-russia) (**this repo read the whole report**; see also ECDC weekly CDTR week 41, 2026-10-09) | 2026 | official public release · **short quotes and conclusions only; no full text reproduced** | the Irkutsk anti-plague institute event |
| ev-069 | 论文 | 高 | 摘要 | C. Guérin (PROSEVA Study Group). *Prone Positioning in Severe Acute Respiratory Distress Syndrome.* **N Engl J Med. 2013 Jun 6;368(23):2159-68.** **PMID [23688302](https://pubmed.ncbi.nlm.nih.gov/23688302/)** · **DOI [10.1056/NEJMoa1214103](https://doi.org/10.1056/NEJMoa1214103)** · ClinicalTrials.gov **[NCT00527813](https://clinicaltrials.gov/study/NCT00527813)** (**this repo read only the abstract**: the full text is paywalled; the `Statement` contains only the abstract's numbers) | 2013 | external literature · **abstract and conclusions only; no full text reproduced** | ARDS prone positioning |
| ev-070 | 论文 | 高 | 摘要 | SPRINT Research Group. *A Randomized Trial of Intensive versus Standard Blood-Pressure Control.* **N Engl J Med. 2015 Nov 26;373(22):2103-16.** **PMID [26551272](https://pubmed.ncbi.nlm.nih.gov/26551272/)** · **DOI [10.1056/NEJMoa1511939](https://doi.org/10.1056/NEJMoa1511939)** · **PMC [4689591](https://pmc.ncbi.nlm.nih.gov/articles/PMC4689591/)** (open access; **this repo read only the abstract**: the `Statement` contains only the abstract's hazard ratios, P values, and mean SBP at 1 year) | 2015 | external literature · **abstract and conclusions only; no full text reproduced** | intensive BP lowering (SPRINT) |
| ev-071 | 指南 | 高 | 摘要 | World Health Organization (WHO), *Manual for plague surveillance, diagnosis, prevention and control*, **published 2024-09-25**, ISBN 978-92-4-009042-2, [who.int](https://www.who.int/publications/i/item/9789240090422) (**this repo read verbatim key passages via search**: F1RDT first-line, treat on suspicion without relying on a positive test, fluoroquinolones as first-line; **the manual runs 92 pages and was not read in full**) | 2024 | official public release · **short quotes and conclusions only; no full text reproduced** | treat before confirming plague |
| ev-072 | 指南 | 高 | 摘要 | U.S. Centers for Disease Control and Prevention (CDC), *Guidance for Responding to a Plague Bioterrorism Event*, [cdc.gov](https://www.cdc.gov/plague/hcp/emergency-guidance/index.html) (**this repo read verbatim key passages via search**: antimicrobials within 24 hours, 10–14 days, 48 hours of droplet precautions, 7-day prophylaxis for contacts; **the CDC page rejected this repo's direct fetch with 403 and was not read in full**) | 2021 | official public release · **short quotes and conclusions only; no full text reproduced** | treat before confirming plague |
| ev-073 | 指南 | 高 | 摘要 | Nelson CA, Kessel SM, Staley D, et al. *Antimicrobial Treatment and Prophylaxis of Plague: Recommendations for Naturally Acquired Infections and Bioterrorism Response.* **MMWR Recomm Rep. 2021;70(3):1-11.** **PMID [34264565](https://pubmed.ncbi.nlm.nih.gov/34264565/)** · [CDC official PDF](https://www.cdc.gov/mmwr/volumes/70/rr/pdfs/rr7003a1-H.pdf) (**this repo read verbatim key passages via search**: the FDA-approved antimicrobial list; **the PDF rejected this repo's direct fetch with 403 and was not read in full**) | 2021 | official public release · **short quotes and conclusions only; no full text reproduced** | treat before confirming plague |
| ev-074 | 教材 | 低 | 仅定位 | Longo D, Fauci AS, Kasper DL, Hauser SL, Jameson JL, Loscalzo J, Holland SM, Langford CA, eds. *Harrison's Principles of Internal Medicine*, **22nd ed.**, McGraw Hill, © 2025, published 2025-06-17, ISBN 9781265979317, [mheducation.com](https://www.mheducation.com/highered/mhp/product/harrison-s-principles-internal-medicine-twenty-second-edition-vol-1-vol-2.html) (**this repo does not own a copy and has checked no chapter or page number**) | 2025 | external source · locator only | textbook background for the hypertension-guideline claim and for the GOLD 2026 COPD claim (**both unverified; not counted as verification evidence**) |
| ev-075 | 教材 | 低 | 仅定位 | Kumar V, Abbas AK, Aster JC, eds. *Robbins and Cotran Pathologic Basis of Disease*, **10th ed.**, Elsevier, 2020-06-19, ISBN 9780323531139, 1392 pp., [elsevier.com](https://shop.elsevier.com/books/robbins-and-cotran-pathologic-basis-of-disease/kumar/978-0-323-53113-9) (**this repo does not own a copy and has checked no chapter or page number**) | 2020 | external source · locator only | textbook background for the GOLD 2026 COPD claim (**unverified; not counted as verification evidence**) |
| ev-076 | 教材 | 低 | 仅定位 | Kaushansky K, Lichtman MA, Prchal JT, Levi MM, Burns LJ, Linch DC, eds. *Williams Hematology*, **10th ed.**, McGraw Hill, © 2021, published 2021-02-24, ISBN 9781264264122, [mheducation.com](https://www.mheducation.com/highered/mhp/product/williams-hematology-10th-edition.html) (**this repo does not own a copy and has checked no chapter or page number**) | 2021 | external source · locator only | none (**a haematology claim is to be written once the book is in hand**) |
| ev-077 | 教材 | 低 | 仅定位 | 《**Practical Internal Medicine**》(*Shiyong Neikexue*), **16th ed.**, chief eds. Wang Jiyao, Ge Junbo, Zou Hejian, People's Medical Publishing House, 2022-06, ISBN 9787117324823, 2 vols., 6.061M characters, [pmphmall.com book page](https://www.pmphmall.com/gdsdetail/645494-323091) (**this repo does not own a copy and has checked no chapter or page number**) | 2022 | external source · locator only | textbook background for the hypertension-guideline claim (**unverified; not counted as verification evidence**) |
| ev-078 | 指南 | 高 | 摘要 | Chinese Hypertension guideline revision committee, Hypertension League (China), Chinese Medical Association branch et al., ***Chinese Guidelines for the Prevention and Treatment of Hypertension (2024 revision)***, *Chinese Journal of Hypertension (Chinese and English edition)* 2024, 32(7): 603-700, **DOI [10.16439/j.issn.1673-7245.2024.07.002](https://doi.org/10.16439/j.issn.1673-7245.2024.07.002)**; English version *Clinical practice guideline for the management of hypertension in China*, **Chin Med J. 2024;137(24):2907-2952**, **DOI [10.1097/CM9.0000000000003431](https://doi.org/10.1097/CM9.0000000000003431)** · **PMID [39289992](https://pubmed.ncbi.nlm.nih.gov/39289992/)** (open access) (**this repo read verbatim key passages via search**: Key Point 4 definition and Table 6 BP classification, Key Point 5C treatment targets, the recommendation classes for treatment initiation and maintenance; **the LWW page returned 403 to this repo and the 98-page guideline was not read in full**) | 2024 | official public release · **short quotes and conclusions only; no full text reproduced** | blood-pressure targets in the 2024 Chinese hypertension guideline |
| ev-079 | 指南 | 高 | 摘要 | Global Initiative for Chronic Obstructive Lung Disease (GOLD), ***Global Strategy for the Diagnosis, Management, and Prevention of COPD — GOLD 2026 Report*** (v1.2, 2025-11-20) · ***GOLD 2026 Pocket Guide*** (2025-11-11) · ***GOLD REPORT 2026 KEY CHANGES SUMMARY*** (2025-11-10), [goldcopd.org](https://goldcopd.org/2026-gold-report-and-pocket-guide/) (**this repo read verbatim key passages via search**: the pocket guide's diagnostic criteria and exacerbation medications, the key-changes summary's statement on the revised ABE grouping criteria; **the report PDF is marked `COPYRIGHT MATERIAL - DO NOT COPY OR DISTRIBUTE` and was not read in full**) | 2026 | official public release · **short quotes and conclusions only; no full text reproduced** | COPD diagnosis and treatment in GOLD 2026 |

| 编号 | 类别 | 等级 | 核验深度 | 定位 | 时间 | 许可 | 引用处 |
|---|---|---|---|---|---|---|---|
| ev-080 | 教材 | 低 | 全文 | OpenStax《Physics》 Ch 6 · Angle of Rotation and Angular Velocity, [m54176](https://github.com/openstax/osbooks-physics/blob/main/modules/m54176/index.cnxml) (**module cnxml source fetched and read in full**: rotation angle Δθ = Δs/r, angular velocity ω = Δθ/Δt, tangential speed v = rω, unit conversions and Teacher Support) | 2020 | **CC BY 4.0** · **freely reusable** | uniform circular motion |
| ev-081 | 教材 | 低 | 全文 | OpenStax《Physics》 Ch 6 · Uniform Circular Motion, [m54181](https://github.com/openstax/osbooks-physics/blob/main/modules/m54181/index.cnxml) (**module cnxml source fetched and read in full**: centripetal acceleration a_c = v²/r = rω², centripetal force F_c = mv²/r, Key Terms on centripetal versus centrifugal, Teacher Support demonstrations and the centrifugal-force confusion) | 2020 | **CC BY 4.0** · **freely reusable** | uniform circular motion · centripetal force is not a new kind of force · the centrifugal-force misconception · the cut-the-string demonstration |
| ev-082 | 教材 | 低 | 全文 | OpenStax《Physics》 Ch 6 · Introduction (chapter opener), [m54173](https://github.com/openstax/osbooks-physics/blob/main/modules/m54173/index.cnxml) (**module cnxml source fetched and read in full**: Teacher Support asking teachers to `Address any misconceptions about centrifugal force`; circular motion as the entry point of the chapter) | 2020 | **CC BY 4.0** · **freely reusable** | the centrifugal-force misconception (source of "the textbook expects it") |
| ev-083 | 教材 | 低 | 全文 | OpenStax《Physics》 Ch 18 · Introduction (chapter opener), [m54417](https://github.com/openstax/osbooks-physics/blob/main/modules/m54417/index.cnxml) (**module cnxml source fetched and read in full**: the Teacher Support note that `static` implies nothing is moving "yet this is often not the case", and the chapter-opening review list calling for universal gravitation and vectors) | 2020 | **CC BY 4.0** · **freely reusable** | electric charge · Coulomb's law |
| ev-084 | 教材 | 低 | 全文 | OpenStax《Physics》 Ch 18 · Electrical Charges, Conservation of Charge, and Transfer of Charge, [m54410](https://github.com/openstax/osbooks-physics/blob/main/modules/m54410/index.cnxml) (**module cnxml source fetched and read in full**: the two kinds of charge and like-repels/unlike-attracts, conservation of charge, the coulomb and the elementary charge, conductors/insulators/semiconductors, charging by contact/conduction/induction and polarization, the Teacher Support question on how static electricity is compatible with charge transfer) | 2020 | **CC BY 4.0** · **freely reusable** | electric charge |
| ev-085 | 教材 | 低 | 全文 | OpenStax《Physics》 Ch 18 · Coulomb's law, [m54414](https://github.com/openstax/osbooks-physics/blob/main/modules/m54414/index.cnxml) (**module cnxml source fetched and read in full**: F = kq₁q₂/r² with the sign rule, torsion-balance measurements and the inverse square, the applicability condition "not moving with respect to each other", the sphere treated as a point from outside, the [AL] question on why electrostatics was discovered after gravitation) | 2020 | **CC BY 4.0** · **freely reusable** | Coulomb's law |
| ev-086 | 教材 | 低 | 全文 | OpenStax《Physics》 Ch 18 · Electric Field, [m54428](https://github.com/openstax/osbooks-physics/blob/main/modules/m54428/index.cnxml) (**module cnxml source fetched and read in full**: E = F/q_test and the test charge, the field surviving removal of the test charge, the point-charge field E = k|Q|/r², the three field-line rules and superposition, the science-fiction multiple choice on neutral bodies) | 2020 | **CC BY 4.0** · **freely reusable** | electric field |
| ev-087 | 教材 | 低 | 全文 | OpenStax《Physics》 Ch 18 · Electric Potential, [m54426](https://github.com/openstax/osbooks-physics/blob/main/modules/m54426/index.cnxml) (**module cnxml source fetched and read in full**: potential energy and the reference point, U_E = kq₁q₂/r, potential V = U_E/q and the "same Strategy" sentence, the potential of a point charge, ΔV versus the uniform field, the Teacher Support emphasis on the difference between the two terms) | 2020 | **CC BY 4.0** · **freely reusable** | electric potential energy and electric potential |
| ev-088 | 教材 | 低 | 全文 | OpenStax《Physics》 Ch 6 · Rotational Motion, [m54180](https://github.com/openstax/osbooks-physics/blob/main/modules/m54180/index.cnxml) (**module cnxml source fetched and read in full**: angular acceleration α = Δω/Δt and the sign convention (counterclockwise positive), the θ/ω/α ↔ x/v/a mapping, the four rotational kinematic equations for constant α, tangential acceleration a = rα, torque τ = rF sinθ and the lever arm, zero net torque, the fishing-reel and merry-go-round worked examples, the tornado feature and the Teacher Support lever demonstration) | 2020 | **CC BY 4.0** · **freely reusable** | angular acceleration and rotational kinematics · torque |
| ev-089 | 官方文件 | 高 | 全文 | *Guidelines for Writing an IANA Considerations Section in RFCs*, IETF, **BCP 26 · RFC 8126** (Obsoletes: 5226; third edition), M. Cotton / B. Leiba / T. Narten, published 2017-06, [full text at rfc-editor.org](https://www.rfc-editor.org/rfc/rfc8126.txt) (**this repo verified §4.8 verbatim** — the definition of IETF Review: new values assigned only through RFCs in the IETF Stream, through IETF Last Call and approved by the IESG as having IETF consensus, any RFC type sufficient, formerly called "IETF Consensus" — and read **§4.7 RFC Required, §4.9 Standards Action and the §4.11 strictness ladder** for contrast; the document is 2,635 lines and **the remaining sections were not checked**) | 2017 | official public specification · **cite section numbers and short quotes only; no full text reproduced** | the registration bar of IETF Review |
| ev-090 | 官方文件 | 高 | 摘要 | U.S. Centers for Disease Control and Prevention (CDC), ***CDC Health Advisory: Severe Pulmonary Disease Associated with Using E-Cigarette Products***, **issued 2019-08-30 09:35 ET**, CDCHAN-00421, [CDC Stacks archive](https://stacks.cdc.gov/view/cdc/81107) (**this repo read key passages via search**: as of 2019-08-27, 25 states had reported 215 possible cases; one Illinois patient was **hospitalised on 2019-07-29 and died on 2019-08-20**; clinical identification, reporting and follow-up recommendations) | 2019 | official public release · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-091 | 官方文件 | 高 | 全文 | Schier JG, Meiman JG, Layden J, et al.; CDC 2019 Lung Injury Response Group. *Severe Pulmonary Disease Associated with Electronic-Cigarette–Product Use — Interim Guidance*, **MMWR 2019-09-13 (68(36):787–790); posted 2019-09-06 as an Early Release**, DOI [10.15585/mmwr.mm6836e2](https://doi.org/10.15585/mmwr.mm6836e2), [PMC6755818](https://pmc.ncbi.nlm.nih.gov/articles/PMC6755818/) (**open access, read in full by this repo**: "no consistent evidence of an infectious etiology has been discovered; therefore, the suspected cause is a chemical exposure"; the surveillance **case definition**'s "confirmed" category requires "negative respiratory viral panel, influenza PCR or rapid test"; the text records the 2019-08-16 Clinical Action alert) | 2019 | official public publication · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-092 | 官方文件 | 高 | 全文 | Ghinai I, Pray IW, Navon L, et al. *E-cigarette Product Use, or Vaping, Among Persons with Associated Lung Injury — Illinois and Wisconsin, April–September 2019*, **MMWR 2019-10-04 (68(39):865–869)**, DOI [10.15585/mmwr.mm6839e2](https://doi.org/10.15585/mmwr.mm6839e2), [PMC6776374](https://pmc.ncbi.nlm.nih.gov/articles/PMC6776374/) (**open access, read in full**: hospitalisations trace back to **2019-04-24**; 127 cases in the two states by 2019-09-20, 86 interviewed, of whom **87% used THC-containing products, 66% "Dank Vapes", 89% obtained them from informal sources**) | 2019 | official public publication · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-093 | 官方文件 | 高 | 全文 | Blount BC, Karwowski MP, Morel-Espinosa M, et al. *Evaluation of Bronchoalveolar Lavage Fluid from Patients in an Outbreak of E-cigarette, or Vaping, Product Use–Associated Lung Injury — 10 States, August–October 2019*, **MMWR 2019-11-15 (68(45):1040–1041)**, DOI [10.15585/mmwr.mm6845e2](https://doi.org/10.15585/mmwr.mm6845e2), [PMC6855513](https://pmc.ncbi.nlm.nih.gov/articles/PMC6855513/) (**open access, read in full**: **VEA detected in all 29 bronchoalveolar-lavage samples** from 10 states; as of 2019-10-15, **86%** of 867 patients with product-use data used THC-containing products) | 2019 | official public publication · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-094 | 官方文件 | 高 | 全文 | Pray IW, Atti SK, Tomasallo C, Meiman JG. *E-cigarette, or Vaping, Product Use–Associated Lung Injury Among Clusters of Patients Reporting Shared Product Use — Wisconsin, 2019*, **MMWR 2020-03-06 (69(9):236–240)**, DOI [10.15585/mmwr.mm6909a4](https://doi.org/10.15585/mmwr.mm6909a4), [PMC7367091](https://pmc.ncbi.nlm.nih.gov/articles/PMC7367091/) (**open access, read in full**: **2019-07-10** WDHS notified of five previously healthy adolescents; eight patients in three social clusters with onset concentrated 2019-06-18–07-21, all using illicit THC cartridges ("Dank Vapes"); the authors infer a change in illicit-cartridge composition, including the addition of VEA, **may have occurred shortly before June 2019**; control: Minnesota seizures found VEA in **none** of the 2018 products and in **all** of the 2019-09 batch) | 2020 | official public publication · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-095 | 官方文件 | 高 | 摘要 | World Health Organization (WHO) COVID-19 response timeline — Archived: *WHO Timeline — COVID-19* (**published 2020-04-27**, [who.int](https://www.who.int/news-room/detail/27-04-2020-who-timeline---covid-19)) and *Listings of WHO's response to COVID-19* (first posted 2020-06-29); WHO **DON229, *Pneumonia of unknown cause – China*** (**published 2020-01-05**, [who.int](https://www.who.int/emergencies/disease-outbreak-news/item/2020-DON229)) (**this repo checked the key entries across these pages**: 2019-12-31 China office informed; 2020-01-01 IMST activated; 01-04 social-media notice; 01-05 DON published; 01-10 interim guidance; 01-12 sequence shared; 01-13 first exported case reported by Thailand; 01-30 PHEIC declared; 03-11 assessment that COVID-19 "can be characterized as a pandemic" — all from the pages themselves) | 2020 | official public release · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-096 | 论文 | 高 | 摘要 | Basavaraju SV, Patton ME, Grimm K, et al. *Serologic Testing of U.S. Blood Donations to Identify SARS-CoV-2-Reactive Antibodies: December 2019–January 2020*, **Clinical Infectious Diseases (online 2020-11-30; issue 2021)**, DOI [10.1093/cid/ciaa1785](https://doi.org/10.1093/cid/ciaa1785), [PMC7799215](https://pmc.ncbi.nlm.nih.gov/articles/PMC7799215/) (**this repo read the abstract and conclusions**: of 7,389 donations from nine states (2019-12-13–2020-01-17), **106** were pan-Ig reactive; **84 of 90** retested samples had neutralising activity; "SARS-CoV-2 **may** have been introduced into the United States prior to January 19, 2020"); companion — American Red Cross press release, **2020-12-01**, [redcross.org](https://www.redcross.org/about-us/news-and-events/press-release/2020/study-suggests-possible-new-covid-19-timeline-in-the-us.html) (**read in full**: earliest reactive donations from **2019-12-13–16 in California, Oregon and Washington**; wording "**possible**"; cross-reactivity cannot be fully excluded at low prevalence) | 2020 | external literature · **abstract and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-097 | 论文 | 高 | 全文 | King BA, Jones CM, Baldwin GT, Briss PA. *E-cigarette, or Vaping, Product Use-Associated Lung Injury: Looking Back, Moving Forward*, **Nicotine & Tobacco Research 2020-12-15; 22(Suppl 1):S96–S99**, DOI [10.1093/ntr/ntaa186](https://doi.org/10.1093/ntr/ntaa186), [PMC7792918](https://pmc.ncbi.nlm.nih.gov/articles/PMC7792918/) (**open access, read in full**: as of **2020-02-18**, **2,807 hospitalisations and 68 deaths** nationwide; the outbreak **rose through August 2019, peaked in September** and declined; the EVALI-consistent ED-visit **baseline goes back to 2017-01–2019-06**; about **20%** of patients used nicotine-containing products only) | 2020 | external literature · **abstract and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-098 | 论文 | 高 | 摘要 | Grimm K, Saá P, Cheedarla N, et al. *Serologic Testing of US Blood Donations to Identify Severe Acute Respiratory Syndrome Coronavirus 2 and Other Coronaviruses, December 2019 to July 2020*, **Open Forum Infectious Diseases 2024; 11(7) (online 2024-06-28)**, DOI [10.1093/ofid/ofae351](https://doi.org/10.1093/ofid/ofae351), [PMC11257073](https://pmc.ncbi.nlm.nih.gov/articles/PMC11257073/) (**this repo read the abstract and key sections**: of 46,120 donations, **9 confirmed positives** among the 13,364 collected 2019-12-13–2020-01-22; "SARS-CoV-2 was **likely** present in the United States before 19 January 2020") | 2024 | external literature · **abstract and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-099 | 官方文件 | 高 | 摘要 | World Health Organization (WHO), ***Independent assessment of the origins of SARS-CoV-2*** (SAGO assessment report, **published 2025-06-27**, [report page](https://www.who.int/publications/m/item/independent-assessment-of-the-origins-of-sars-cov-2-from-the-scientific-advisory-group-for-the-origins-of-novel-pathogens); licensed CC BY-NC-SA 3.0 IGO) and the same-day news release *WHO Scientific advisory group issues report on origins of COVID-19*, [who.int](https://www.who.int/news/item/27-06-2025-who-scientific-advisory-group-issues-report-on-origins-of-covid-19) (**this repo read the news release and report highlights**: "**all hypotheses must remain on the table**"; "the weight of available evidence" supports zoonotic spillover (directly from bats or through an intermediate host); WHO's requests to China for early genetic sequences, animal-market information and laboratory biosafety information **remain unmet**) | 2025 | official public release · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |

| 编号 | 类别 | 等级 | 核验深度 | 定位 | 时间 | 许可 | 引用处 |
|---|---|---|---|---|---|---|---|
| ev-100 | 官方文件 | 高 | 摘要 | World Health Organization (WHO), *Statement on the second meeting of the International Health Regulations (2005) Emergency Committee regarding the outbreak of novel coronavirus (2019-nCoV)*, **issued 2020-01-30**, [who.int](https://www.who.int/news/item/30-01-2020-statement-on-the-second-meeting-of-the-international-health-regulations-%282005%29-emergency-committee-regarding-the-outbreak-of-novel-coronavirus-%282019-ncov%29) (**this repo read key passages**: declares a PHEIC; same-day figures — **7,711** confirmed cases (12,167 suspected) and **170 deaths** in China, 124 recovered; **83 cases in 18 countries** outside China, only 7 without travel history in China, human-to-human transmission in 3 countries, no deaths outside China) | 2020 | official public release · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-101 | 官方文件 | 高 | 摘要 | World Health Organization (WHO), *WHO calls for further studies, data on origin of SARS-CoV-2 virus, reiterates that all hypotheses remain open*, **issued 2021-03-30**, [who.int](https://www.who.int/news/item/30-03-2021-who-calls-for-further-studies-data-on-origin-of-sars-cov-2-virus-reiterates-that-all-hypotheses-remain-open) (**this repo read key passages**: the joint mission's Wuhan field visit ran **2021-01-14–02-10**; "**all hypotheses remain on the table**"; "we have not yet found the source of the virus") | 2021 | official public release · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-102 | 官方文件 | 高 | 摘要 | World Health Organization (WHO), *Statement on the fifteenth meeting of the IHR (2005) Emergency Committee on the COVID-19 pandemic*, **issued 2023-05-05** (fifteenth meeting held 2023-05-04), [who.int](https://www.who.int/news/item/05-05-2023-statement-on-the-fifteenth-meeting-of-the-international-health-regulations-%282005%29-emergency-committee-regarding-the-coronavirus-disease-%28covid-19%29-pandemic) (**this repo read key passages**: "COVID-19 is now an established and ongoing health issue which **no longer constitutes a public health emergency of international concern (PHEIC)**") | 2023 | official public release · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-103 | 官方文件 | 高 | 摘要 | UN News (Chinese service), two reports: "[Special report] 新冠病毒溯源专家组：实验室泄漏「极不可能」 冷链传播「值得探索」" (**2021-02-09**, [news.un.org](https://news.un.org/zh/story/2021/02/1077632)); "新冠病毒溯源专家组发表初步研究报告 世卫组织总干事表示「所有的假定仍然都在考虑范围之内」" (**2021-03-30**, [news.un.org](https://news.un.org/zh/story/2021/03/1081102)) (**this repo read both reports in full**: the 02-09 press conference — laboratory leak "extremely unlikely", intermediate host "remains the most likely pathway", cold chain "needs further exploration", 17 Chinese + 17 international experts, field visit 2021-01-14–02-10; the 03-30 report — about **28%** of early cases linked to the Huanan market, **23%** to other Wuhan markets, **45%** no market exposure, "the role of the Huanan market … cannot be determined conclusively") | 2021 | official media release · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-104 | 官方文件 | 高 | 摘要 | Italian government decree (DPCM, **2020-03-09**), *Ulteriori disposizioni attuative del decreto-legge 23 febbraio 2020, n. 6, recante misure urgenti in materia di contenimento e gestione dell'emergenza epidemiologica da COVID-19, applicabili sull'intero territorio nazionale*, Gazzetta Ufficiale No. 62, act no. **20A01558**, [gazzettaufficiale.it](https://www.gazzettaufficiale.it/eli/id/2020/03/09/20A01558/sg) (**this repo read the key phrase on the original page**: measures "applicabili sull'intero territorio nazionale" — applicable to the **entire national territory**) | 2020 | official public release · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-105 | 官方文件 | 高 | 摘要 | United States, *Proclamation on Declaring a National Emergency Concerning the Novel Coronavirus Disease (COVID-19) Outbreak* (presidential proclamation, **signed 2020-03-13**, No. 9994), **published 2020-03-18 at 85 FR 15337**, document no. **2020-05794**, [White House text](https://www.whitehouse.gov/presidential-actions/proclamation-declaring-national-emergency-concerning-novel-coronavirus-disease-covid-19-outbreak/); [Federal Register](https://www.federalregister.gov/documents/2020/03/18/2020-05794/declaring-a-national-emergency-concerning-the-novel-coronavirus-disease-covid-19-outbreak) (**this repo read the key sentence**: "the COVID-19 outbreak in the United States constitutes a national emergency, **beginning March 1, 2020**"; volume/page and document number checked via the Federal Register API) | 2020 | official public release · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-106 | 官方文件 | 高 | 摘要 | UK government, *Prime Minister's statement on coronavirus (COVID-19): 23 March 2020* (address to the nation), **issued 2020-03-23**, [gov.uk](https://www.gov.uk/government/speeches/pm-address-to-the-nation-on-coronavirus-23-march-2020) (**this repo read the key sentences**: "**you must stay at home**"; the police are given powers to enforce "including through fines and dispersing gatherings") | 2020 | official public release · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-107 | 官方文件 | 高 | 摘要 | Press Information Bureau (PIB), Government of India, *PM calls for complete lockdown of entire nation for 21 days*, **issued 2020-03-24**, release ID **PRID 1608009**, [pib.gov.in](https://pib.gov.in/PressReleasePage.aspx?PRID=1608009) (**this repo read the key sentence**: "complete lockdown of the entire nation for the next 21 days **beginning at midnight tonight**") | 2020 | official public release · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-108 | 官方文件 | 高 | 摘要 | (Wuhan) *武汉市新型冠状病毒感染的肺炎疫情防控指挥部通告（第1号）* [Command Notice No. 1 of the Wuhan Epidemic Prevention and Control Command], **issued in the small hours of 2020-01-23**, Xinhua repost, [新华网](http://www.xinhuanet.com/politics/2020-01/23/c_1125495557.htm) (**this repo read the key sentences of the repost**: "自1月23日10时起，武汉全市城市公交、地铁、轮渡、长途客运暂停运营；无特殊原因，市民不要离开武汉；机场、火车站离汉通道暂时关闭" — from 10:00 on 23 January all city buses, metro, ferries and long-distance coaches suspended; citizens told not to leave Wuhan without special reason; outbound channels via airport and railway stations temporarily closed) | 2020 | official notice via official news agency · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-109 | 官方文件 | 高 | 摘要 | Archives of Jianghan District, Wuhan, *2020年武汉市江汉区大事记* [Chronicle of major events of Jianghan District, Wuhan, 2020], **published 2022-08-26**, [jianghan.gov.cn](https://www.jianghan.gov.cn/ztzl/jlxkgc/dsj/202301/t20230103_2123259.shtml) (**this repo read the key sentence on the original page**: "1月1日中共江汉区委、区人民政府果断决策，华南海鲜市场闭市" — on 1 January the district committee and government decided to close the Huanan Seafood Market; the same page records "1月23日10时起，武汉全市离汉通道关闭") | 2022 | official public release · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-110 | 论文 | 高 | 摘要 | Apolone G, Montomoli E, Manenti A, et al. *Unexpected detection of SARS-CoV-2 antibodies in the prepandemic period in Italy*, **Tumori Journal 2021; 107(5):446–451 (online 2020-11-11)**, DOI [10.1177/0300891620974755](https://doi.org/10.1177/0300891620974755), [PMC8529295](https://pmc.ncbi.nlm.nih.gov/articles/PMC8529295/) (open access, CC BY; **this repo read the abstract**: among **959 asymptomatic** participants of a lung-cancer screening cohort (2019-09–2020-03), **111 (11.6%)** samples were RBD-antibody positive, earliest from **2019-09** (14% that month), with a **>30%** cluster in the second week of February 2020 and up to **53.2%** in Lombardy; **three commentary articles followed in the same journal (2021); this repo did not read them all**) | 2020 | external literature · **abstract and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-111 | 论文 | 高 | 摘要 | Deslandes A, Berti V, Tandjaoui-Lambotte Y, et al. *SARS-CoV-2 was already spreading in France in late December 2019*, **International Journal of Antimicrobial Agents 2020; 55(6):106006 (online 2020-05-03)**, DOI [10.1016/j.ijantimicag.2020.106006](https://doi.org/10.1016/j.ijantimicag.2020.106006), [PMC7196402](https://pmc.ncbi.nlm.nih.gov/articles/PMC7196402/) (**this repo read the abstract and checked key passages**: records of ILI patients admitted to an ICU in a hospital north of Paris **2019-12-02–2020-01-16**; 14 of 58 patients included; one sample from a 42-year-old man seen on **2019-12-27** positive by RT-PCR; his last foreign travel was 2019-08; the authors state the epidemic "started much earlier in France") | 2020 | external literature · **abstract and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-112 | 论文 | 高 | 摘要 | La Rosa G, Mancini P, Bonanno Ferraro G, et al. *SARS-CoV-2 has been circulating in northern Italy since December 2019: Evidence from environmental monitoring*, **Science of the Total Environment 2021; 750:141711 (online 2020-08-15)**, DOI [10.1016/j.scitotenv.2020.141711](https://doi.org/10.1016/j.scitotenv.2020.141711), [PMC7428442](https://pmc.ncbi.nlm.nih.gov/articles/PMC7428442/) (**this repo read the abstract and key passages**: of 40 composite influent samples (2019-10–2020-02) from five WWTPs in three cities — Milan/Lombardy, Turin/Piedmont, Bologna/Emilia-Romagna — 15 were positive by two methods, the **earliest collected on 2019-12-18 in Milan and Turin** (Bologna 2020-01-29); all **24 control samples from 2018-09–2019-06 were negative**; Italy's first autochthonous case was 2020-02-21) | 2020 | external literature · **abstract and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-113 | 论文 | 高 | 摘要 | Althoff KN, et al. *Antibodies to Severe Acute Respiratory Syndrome Coronavirus 2 (SARS-CoV-2) in All of Us Research Program Participants, 2 January to 18 March 2020*, **Clinical Infectious Diseases 2022; 74(4):584–590 (online 2021-06)**, DOI [10.1093/cid/ciab519](https://doi.org/10.1093/cid/ciab519), [PMC8384413](https://pmc.ncbi.nlm.nih.gov/articles/PMC8384413/); companion — NIH news release *NIH study offers new evidence of early SARS-CoV-2 infections in U.S.* (**2021-06-15**, [nih.gov](https://www.nih.gov/news-events/news-releases/nih-study-offers-new-evidence-early-sars-cov-2-infections-us), read via a web.archive.org snapshot) (**this repo read the abstract and the news release**: of **24,079 participants** (samples 2020-01-02–03-18), **9** were positive on two sequential serology platforms — earliest 01-07 (Illinois) and 01-08 (Massachusetts), across five states (IL/MA/WI/PA/MS), **7 before their state's first confirmed case**; "SARS-CoV-2 infections **weeks prior to the first recognized cases** in 5 US states") | 2021 | external literature · **abstract and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-114 | 官方文件 | 中 | 全文 | Containment Laboratory Community Advisory Committee (CLCAC), Frederick, Maryland, *Report on USAMRIID and Fort Detrick Incidents to Frederick Mayor, Board of Aldermen, and County Council*, **report dated 2020-01-23**, [cityoffrederickmd.gov (PDF archive)](https://www.cityoffrederickmd.gov/DocumentCenter/View/17648/CLCAC-Report-to-Mayor-Board-of-Aldermen-and-County-Council-January-2019) (**this repo extracted the text of the PDF and read it in full**: a CDC letter of **2019-07-15** ordered USAMRIID to cease select-agent research, the committee was told on **2019-08-02**; a public meeting on **2019-10-08**; issues included training, standard operating procedures and the steam-sterilisation plant (damaged by heavy rain in 2018-05); the committee's conclusion inclines to "little risk to the community" while stating it cannot independently confirm this; **the CDC never published the letter itself**) | 2020 | official public record (local committee) · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |
| ev-115 | 官方文件 | 高 | 摘要 | U.S. Army Public Affairs, *U.S. Army medical research institute continues work on coronavirus*, **published 2020-04-01**, [army.mil](https://www.army.mil/article/234182/u_s_army_medical_research_institute_continues_work_on_coronavirus) (**direct fetch returns 403; this repo read it via a web.archive.org snapshot**: a CDC **letter dated 2020-03-27** fully restored USAMRIID's registration under the Federal Select Agent Program; the **2019-07** suspension stemmed from biosafety-program issues; "Many of the problems stemmed from the failure of Fort Detrick's steam sterilization plant"; states there was no risk to employee health, public health or the environment) | 2020 | official public release · **short quotes and conclusions only; no full text reproduced** | Timeline and origins of the COVID-19 pandemic |

> [!CAUTION]
> **`ev-009` ~ `ev-012` are voided.** They are **constructed example data** the repo made early on to demo the format;
> the classroom observations and assessments they describe never happened.
>
> The numbers are **not recycled** (the trace is kept), but **no entry may cite them again**.
> The 3 entries that cited them were all rewritten or deleted on 2026-10-05.

> [!NOTE]
> **The non-contiguous numbering is intentional.** An `ev-xxx` number, once assigned, never changes — deleting an entry does not recycle its number,
> because other entries have cited it. Same idea as the `id` field.

> [!IMPORTANT]
> **When citing an external source, you must comply with its original license.**
> The repo stores only **locators, short quotations, original summaries, and conclusions** — never the copyrighted expression.

## Grade notes

| Assertion type | Grade ladder (high → low) |
|---|---|
| 命题 | systematic review / meta-analysis > RCT > cohort > case report > expert opinion > **the textbook itself** |
| 教法 | reproducible classroom experiment > quasi-experiment > large-sample classroom data > single classroom experience > expert intuition |

> [!IMPORTANT]
> **The textbook sits low in the evidence pyramid for 命题, yet students treat it as the highest authority.**
> That is exactly why this project exists.
>
> At the same time, **a single classroom experience is legitimate evidence for 教法** — pedagogy is conditional and poorly transferable,
> and forcing the medical standard through would filter out all the valid local experience.

### A real asymmetry: junior-secondary open textbooks are almost all NC

A pattern found while collecting, recorded here so it is not hit again:

| 学段 | 来源 | 许可 |
|---|---|---|
| **高中** | OpenStax《Physics》（`osbooks-physics`） | **CC BY 4.0** ✅ 可自由复用 |
| **初中** | Utah State Board of Education 6 / 7 / 8 年级科学 | **CC BY-NC-SA 3.0** ❌ 仅可引用 |
| 初中（上游） | CK-12 Foundation（Utah 教材的内容来源） | **CC BY-NC** ❌ 仅可引用 |

> [!WARNING]
> **高中级能自由复用，初中级只能引用。**
>
> US secondary OER is largely built on CK-12, and CK-12 is **NC**.
> So "expanding to junior-secondary 知识点" is **more restricted** than senior-secondary on licensing —
> entries may only write **our own summary + phrase-level quotation**, not reuse the textbook's wording.

### Another limitation: junior-secondary textbooks have no teaching guidance

| 来源 | 有结构化教学指导吗 |
|---|---|
| OpenStax《Physics》 | ✅ **580 条 Teacher Support**，含 649 个分组标记 |
| Utah 7 年级 | ❌ 学生用书，**没有** Teacher Support / misconception 标注 |

**含义**：初中源能提供**知识内容与学段边界**（如"矢量推迟到高中"），
但**提供不了分档教法**。初中级的 `教法` 需要另找来源，或由教师贡献。

### A real license trap: the license does not travel with the textbook

OpenStax textbooks **embed PhET simulations** (`<iframe>` + an OpenStax short link,
with the outer `<media class="os-embed">` carrying a description).

Measured (reading **the simulation's own header**, the authoritative source):

| 层 | 内容 | 许可 |
|---|---|---|
| 教材 | OpenStax《Physics》 | **CC BY 4.0** ✅ |
| 教材内嵌的模拟 | PhET「Forces and Motion: Basics」 | **CC BY-NC 4.0** ❌ |
| 抽查的另外三个模拟 | my-solar-system / bending-light / color-vision | **CC BY-NC 4.0** ❌ |

> [!CAUTION]
> **"The textbook is freely reusable" does not imply "what it embeds is too".**
>
> The PhET simulation file header reads:
> `COMMERCIAL USE REQUIRES A COMMERCIAL LICENSE AGREEMENT FROM THE UNIVERSITY OF COLORADO BOULDER.`
>
> And it **requires attribution "near the place of use"**, with the recommended wording:
> `Simulation by PhET Interactive Simulations, University of Colorado Boulder, licensed under CC BY-NC 4.0`
>
> **Re-publishers who copy the textbook's structure will hit this.**
>
> This also shows: **checking a license item by item cannot rely on impression** — I originally thought PhET was CC BY, **and measurement overturned that**.

### A special class of high-grade evidence: publisher errata

`ev-014` and `ev-015` are **errata the publisher itself released**. For a proposition like "a certain textbook is defective somewhere",
they are stronger than the textbook itself — because they are **an authoritative statement about that textbook's content**, needing no third-party inference.

But you must distinguish what a given piece of evidence can support:

| 命题 | 需要什么 | 勘误表够吗 |
|---|---|---|
| 「出版社声明 p.13 漏字」 | 读勘误表 | ✅ **够** |
| 「教材 p.13 真的漏字」 | 翻开教材 | ❌ 不够（勘误表可能滞后，新印次或已修正） |

### Open-textbook licenses come in two tiers — don't mix them

`ev-016`~`ev-018` all come from OpenStax, but the licenses differ:

| 教材 | 许可 | 能做什么 |
|---|---|---|
| OpenStax《Physics》 | **CC BY 4.0** | 可自由复用正文（署名即可） |
| OpenStax《College Physics 2e》 | **CC BY-NC-SA 4.0** | **只能引用定位与短引用**，不可复用正文 |

**筛查结果**：OpenStax 的 55 个教材仓库中，只有 **13 个是 CC BY**，其余 **41 个含 NC**。

> [!IMPORTANT]
> **本库是 CC BY-SA 4.0（无 NC），与 NC 内容不兼容。**
> **同一出版社的书，许可可能不同，必须逐本查**——本例中《Physics》是 CC BY，
> 而同社的《College Physics 2e》和《University Physics》都是 CC BY-NC-SA。

## Raw data

| 文件 | 内容 | 可复算 | 是证据吗 |
|---|---|---|---|
| [`构造数据-欧姆定律演示.csv`](构造数据-欧姆定律演示.csv) | `U = 10 × I` 的**构造**数据。**没有任何测量发生**，也没有温度记录 | ✅ 算术可复算 | ❌ **不是证据**——仅示范欧姆关系长什么样 |
| [`os-teacher-markers.csv`](os-teacher-markers.csv) | OpenStax《Physics》段落级受众标记明细（419 行，含 commit 哈希） | ✅ [脚本](os-teacher-markers.py) 可重跑 | ✅ 是（对源文件的统计） |

> [!IMPORTANT]
> **"Recomputable" and "is evidence" are two different things.**
>
> The first row above is **arithmetically fully recomputable** (`5.0 / 10.00 = 0.50`),
> yet it **cannot support any proposition about the real world** — because **no one measured anything**.
>
> `ev-002` was once registered as **grade "high"** precisely because it was "recomputable".
