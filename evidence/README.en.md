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
> that row was therefore hit by an adversarial review ([attack entry](../knowledge/物理/命题/攻击/攻击-教材内建分组教学变体.en.md)'s `A4`).
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
| ev-054 | 官方文件 | 高 | 全文 | *HTTP Semantics*, IETF, **STD 97 · RFC 9110** (Obsoletes: 2818, 7230–7235, 7538, 7615, 7694; Updates: 3864), published 2022-06, [full text at rfc-editor.org](https://www.rfc-editor.org/rfc/rfc9110.txt) (**this repo verified four sections verbatim**: §2.2 requirements-notation clause, §9.2.1 safe methods, §9.2.2 idempotent methods, and **the status-code rules in the preamble to §15** — first digit defines the class, an unrecognized code is treated as the class's x00, values outside 100..599 are invalid, reason phrases are recommendations only; the document is 10,785 lines and **the definitions of the individual codes in §15.2–§15.6 were not checked one by one**, nor were the remaining sections) | 2022 | official public specification · **cite section numbers and short quotes only; no full text reproduced** | HTTP method safety and idempotency · the status-code extensibility rules |
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
