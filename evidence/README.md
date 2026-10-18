# 证据索引

> **English: [README.en.md](README.en.md)**

全库共享。每条知识点的 `front-matter` 用编号引用这里的条目。

## 门槛

**讨论可以随便说，但只有过门槛的证据进入判定。**

必须提供可核验定位：ISBN + 版次 + 页码 / DOI / 官方文档条款 / 公开数据集 / 可复算的脚本与数据。

> [!CAUTION]
> **绝不上传教材原文或扫描页。**
> 只存页码定位、短引用、原创摘要与结论。事实与数据不受版权保护，**表达**受版权保护。

### 定位必须**可核验**，不能是「看起来像定位」的东西

> 完整经过（那些节号为什么是编的、两处约定怎么互相矛盾）见
> [决策记录：证据事故](../docs/decisions/evidence-history.md)。

**已全部改为可核验的写法**：`第 N 章 · 模块标题`，外加模块 id（可点开原文）。

| 不可核验 | 可核验 |
|---|---|
| `§16.1 Reflection` | `第 16 章 · Reflection` + 模块 [m54357](https://github.com/openstax/osbooks-physics/blob/main/modules/m54357/index.cnxml) |

> [!IMPORTANT]
> **能对上 ≠ 精确。** 教材的**印刷版**确实有节号，
> 但它**不在我们读的这份源文件里**。
> **写一个我们核不了的数字，等于伪造定位**——哪怕它碰巧是对的。
>
> 若日后要写节号，必须**对到印刷版或官方网页版**，并在证据行注明依据。

### 来源本身是不是真的：**三问**

**定位合法 ≠ 内容为真。** 有人可以**造一个网站，上面写好假知识，再让别人来引用**——
那个页面 DOI 格式对、文号齐、链接能开，**唯独内容是为这次引用现造的**。
所以登记一条证据前，三个问题必须都能答上：

| # | 问 | 怎么算答上了 | 答不上来 |
|---|---|---|---|
| 1 | **谁发布** | 能问责的主体：出版社 · 期刊 · 标准组织 · 政府部门 · 大学 | 个人站点、无署名转载页 |
| 2 | **是哪个版本、什么时候生效** | 公布 / 施行日期与版本（修正次、文号、期号）都记下来 | 页面无版本；或把「曾经如此」当成「仍然如此」 |
| 3 | **它是为这次引用现造的吗** | 它有**独立于本主张而存在的理由**（法规为管事而立、标准为互通而立、统计为发布而立），且能在**不同发布主体**处找到第二来源 | 只为支撑这一句而存在的页面；多个同源转载 |

> [!IMPORTANT]
> **第 2 问管的是「版本」，不是「谁更早」。**
> **知识会变**——法规有修正版、标准会改版、网页会被重写。
> 「这个页面比本库早存在」既不说明内容真，也不说明它**现在还成立**。
> 所以这一问答的是**这条主张适用于哪个版本**；条目据此在 `scope.条件` 里限定，
> **只声明该版本如此**。

> [!IMPORTANT]
> **第 3 问同时防两件事：伪造，和「交叉印证」的假象。**
> 它问的不是「比我们早」，而是**「这条主张是假的时候，这个来源还存在吗」**——
> 一页只为断言某句话而生的东西，就是 `ev-002` 的形状。
> 另外：三个站互相抄同一句假话，仍然只有一份来源。
> **独立性按发布主体算，不按域名数、链接数算。**

**标识符必须反查**：DOI 解析出的标题、文号在发布主体官网上查到的名字，
**必须与我们登记的一致**。格式对而查不到 = **停手**——
这正是 `ev-002` 的形状：**一切看起来都对，只有它不是真的。**

> [!CAUTION]
> **机械兜底（`R-EVID-03`）**：`核验深度` 为 `未核验`（没打开过）或 `仅定位`
> （打开了但没读正文）的证据，**不能单独**把条目推到 `暂定确认` / `已确证`。
>
> **没读过就不能说「确认过」。** 一个格式完全合法的定位，
> 只能证明**它在那儿**，证明不了**它说了什么**。

## 本库自己犯过的一次：把**构造的数据**登记成「实验数据」

> 完整经过见 [决策记录：证据事故](../docs/decisions/evidence-history.md)——
> 包括「为什么它骗过了一次对抗审查」：**是本库自己把「核实证据是否存在」排除在对抗范围之外的**。

### 由此立下的两条规矩

| # | 规矩 |
|---|---|
| 1 | **本库自产的数据必须写明「构造」还是「实测」。** 「实验数据」四个字等于声称发生了一次测量——**没有测量就没有这句话** |
| 2 | **定量证据必须登记有效位数 / 不确定度 / 重复次数。** 没有它们，该证据**只能支撑到它自己声明的精度**；结论所需精度若优于数据精度，**该证据只能算「示意」，不算证据** |

> **删掉痕迹才是真的丢信息**——`ev-002` 编号保留，文件改名为
> [`构造数据-欧姆定律演示.csv`](构造数据-欧姆定律演示.csv)（它的**示范价值**还在：
> 它确实展示了欧姆关系长什么样，**只是不能支撑任何关于真实世界的命题**）。


> [!IMPORTANT]
> **「官方文件规定了什么」这类主张，官方原文就是一手来源——不需要在阶梯上排队。**
> 所以 `ev-043` 这类登记为「高」，理由与 `ev-002` 那次不同（可复算 ≠ 证据强度）。完整说明见
> [决策记录：证据事故](../docs/decisions/evidence-history.md)。


> [!IMPORTANT]
> **证据阶梯是为「关于人群的实证主张」设计的，对物理不公平**（一本教材里的 `F = ma` 落最低档，
> 与「教材里的一条教学建议」不是一回事）。这是已知问题，未改。完整讨论见
> [决策记录：证据事故](../docs/decisions/evidence-history.md)。

## 索引

> [!NOTE]
> **表头含义**（机器解析见 `tools/kbcheck.py`）：
>
> - **类别**：`教材` · `论文` · `指南` · `官方文件` · `交互式模拟` · `出版社勘误表` · `本库数据`（作废行标 `已作废`）；
> - **等级**：`高` / `中` / `低`——**对「该类主张」而言**，不是绝对高低（见文末「等级说明」）；
> - **核验深度**：本库**实际读了什么**——`全文` / `摘要` / `仅定位` / `未核验`。
>   **这一列让「我们到底核对到什么程度」可见**，不再只靠正文里的一句话。

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
> **ev-020 原先只写「580 条，含 649 个分组标记」，而库里既无脚本也无数据**——
> 那一栏因此被一次对抗审查击中（[攻击条目](../knowledge/physics/claims/attacks/攻击-教材内建分组教学变体.md) 的 `A4`）。
>
> **现已补上脚本 + 明细 + commit 哈希。** 现行数字：
>
> | 口径 | `os-teacher` 便签 | BL | OL | AL | EL | 合计 |
> |---|---|---|---|---|---|---|
> | **宽松**（note 里任意出现） | **582** | 207 | 245 | 191 | **5** | **648** |
> | 严格（`<para>` 开头的 `<span>`） | — | 205 | 243 | 189 | 0 | 637 |
>
> **旧声称的 649 / 580 两者都不是**——它是**某次 `main` 的快照**。
> 差的 `EL`(6→5)、合计(649→648)、便签(580→582) 来自 **`main` 前移**。
>
> **教训：写死一个会漂移的数字，等于把它变成断言。** 数字要连同**规则 + commit** 一起给。
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
| ev-051 | 官方文件 | 高 | 全文 | 《中华人民共和国道路交通安全法》，全国人大常委会 2003-10-28 通过，**2021-04-29 第三次修正**，**2004-05-01 起施行**，[国家市场监督管理总局「政府信息公开」页](https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/bgt/art/2023/art_79dc72ea621f4a9b8adec327abf5d0e1.html)（公布日期 2021-04-29；**本库打开该页并逐条核对全文，止于第一百二十四条**）；同一文本在不同发布主体处交叉核对：[中国人大网 2008 年公报页](http://www.npc.gov.cn/zgrdw/wxzl/gongbao/2008-02/23/content_1462422.htm) · [交通运输部法规查询系统 PDF](https://big5.mot.gov.cn/gate/big5/law.mot.gov.cn:80/exportPDFLaw.action?law.id=37) | 2021 | 官方公开法律 · **仅引用条款号与短引用，不上传原文** | 罚款收据 · 逾期加处罚款 · 省级执行标准 · 醉驾后果 · 罚款指标 |
| ev-052 | 官方文件 | 高 | 全文 | 《Key words for use in RFCs to Indicate Requirement Levels》，IETF，**BCP 14 · RFC 2119**，1997-03 发布，[rfc-editor.org 全文](https://www.rfc-editor.org/rfc/rfc2119.txt)（**本库通读全文**，§1–§5 五条关键词定义、§6 使用约束、§7 安全考量） | 1997 | 官方公开规范 · **仅引用章节号与短引用，不转载全文** | RFC 要求关键词 |
| ev-053 | 官方文件 | 高 | 全文 | 《Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words》，IETF，**BCP 14 · RFC 8174**（Updates: 2119），2017-05 发布，[rfc-editor.org 全文](https://www.rfc-editor.org/rfc/rfc8174.txt)（**本库通读全文**，§2 给出 OLD / NEW 两版原文对照） | 2017 | 官方公开规范 · **仅引用章节号与短引用，不转载全文** | RFC 要求关键词 |
| ev-054 | 官方文件 | 高 | 全文 | 《HTTP Semantics》，IETF，**STD 97 · RFC 9110**（Obsoletes: 2818, 7230–7235, 7538, 7615, 7694；Updates: 3864），2022-06 发布，[rfc-editor.org 全文](https://www.rfc-editor.org/rfc/rfc9110.txt)（**本库已核**：§2.2 需求关键词引用条款、§9.2.1 安全方法、§9.2.2 幂等方法、**§15 全节**——§15.1 总则与各类别前言、§15.2.1–§15.6.6 全部具体码小节（含 §15.3.7.1–§15.3.7.3）；全文 10785 行，**其余章节未核**） | 2022 | 官方公开规范 · **仅引用章节号与短引用，不转载全文** | HTTP 方法的安全性与幂等性 · 状态码的可扩展性规则 · §15 各具体码系列条目 |
| ev-055 | 官方文件 | 高 | 全文 | 国家统计局《什么是调查失业率》，**2025-02-28 10:00 发布**，[统计局官网全文](https://www.stats.gov.cn/zs/tjws/tjzb/202301/t20230101_1903672.html)（**本库通读全文**：一、概念；二、统计方法；三、如何看待调查失业率，含图 1「16 周岁及以上人口分类」与图 2「全国城镇调查失业率」的文字说明） | 2025 | 官方公开统计解读 · **仅引用小节标题与短引用，不转载原文** | 失业人口的三个条件 · 34 万户抽样与相对误差 · 失业率不宜作考核依据也不宜层层分解 |
| ev-056 | 官方文件 | 高 | 全文 | 国家统计局《调查失业率与城镇登记失业率有何区别？》，**2021-02-18 16:26 发布**，[统计局官网全文](https://www.stats.gov.cn/zt_18555/zthd/sjtjr/d12kfr/tjzsqzs/202302/t20230216_1908907.html)（**本库通读全文**：统计方法 / 就业失业定义 / 统计范围三项差异，全文不到一屏） | 2021 | 官方公开统计解读 · **仅引用差异项名称与短引用，不转载原文** | 调查失业率与城镇登记失业率的口径差异 |
| ev-057 | 官方文件 | 高 | 全文 | *Hypertext Transfer Protocol (HTTP) Status Code Registry*，IANA（Internet Assigned Numbers Authority），**Last Updated 2025-09-15**，[注册表全文](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml)（**本库通读整张表**：注册程序 **IETF Review**、参考 **RFC 9110 §16.2.1**，以及 100–599 全部已分配条目与 Unassigned 区间） | 2025 | 官方公开注册表 · **仅引用条目与短引用，不转载整表** | HTTP 状态码的完整清单 · 418 与 306 为 (Unused) · 104 为临时注册 |
| ev-058 | 官方文件 | 高 | 全文 | 国家统计局《什么是居民消费价格指数（CPI）》，**页面标注 2024-09-13 10:00 发布**（URL 路径为 `202409/t20240910_1956353.html`，**路径中的日期与页面标注不一致，本库无法判断真实发布时间**），[统计局官网全文](https://www.stats.gov.cn/zs/tjws/zytjzbqs/jmxxggzs/202409/t20240910_1956353.html)（**本库通读全文**：一、基本定义；二、主要用途三条——反映通胀（紧缩）程度、用于国民经济核算、计算货币购买力） | 2024 | 官方公开统计解读 · **仅引用定义、用途名称与短引用，不转载原文** | CPI 是变动的相对数 · CPI 不等于通货膨胀率 · CPI 用于现价总量的缩减 · CPI 倒数为货币购买力指数 |
| ev-059 | 官方文件 | 高 | 全文 | 国家统计局《GDP是如何进行核算的？》，**2021-02-18 15:51 发布**，[统计局官网全文](https://www.stats.gov.cn/zt_18555/zthd/sjtjr/d12kfr/tjzsqzs/202302/t20230216_1908936.html)（**本库通读全文**：生产法 / 收入法 / 支出法三种方法各一段及其核算公式，末段说明三法结果差异称为统计误差、原因是资料来源不同、在可接受范围内允许存在） | 2021 | 官方公开统计解读 · **仅引用方法名称、公式与短引用，不转载原文** | GDP 三种核算方法及公式 · 理论一致而实际有统计误差 · 统计误差允许存在 |
| ev-060 | 官方文件 | 高 | 全文 | 国家统计局《2025年三季度国内生产总值初步核算结果》，**2025-10-21 09:30 发布**，[统计局官网全文](https://www.stats.gov.cn/sj/zxfb/202510/t20251021_1961646.html)（**本库核到四处原文**：表 1 注 1「绝对额按现价计算，增长速度按不变价计算」、表 3 注「环比增长速度为经季节调整后」、附件 1.1「季度 GDP 以生产法为基础核算」、附件 2.3.2「不变价每 5 年换一次基期，2021–2025 年基期是 2020 年」；**表 1 具体数值与附件其余章节未逐条核**） | 2025 | 官方公开统计发布 · **仅引用表注与短引用，不转载具体数值** | GDP 绝对额按现价、增长速度按不变价 · 季度 GDP 以生产法为基础 · 环比增速为季节调整后 · 不变价基期每 5 年换一次 |
| ev-061 | 官方文件 | 高 | 全文 | 国家统计局《CPI 的编制方法》，**页面标注 2024-11-29 10:00 发布**（URL 路径为 `202411/t20241127_1957589.html`，**路径中的日期与页面标注不一致，本库无法判断真实发布时间**），[统计局官网全文](https://www.stats.gov.cn/zs/tjws/zytjzbqs/jmxxggzs/202411/t20241127_1957589.html)（**本库通读全文**：一、基本情况；二、篮子和权数的确定（篮子每 5 年更换一次、8 大类 268 个基本分类、不含奢侈品与投资品、权数来自住户收支与生活状况调查）；三、代表规格品的确定（五条选取原则与选取流程）；四、价格调查点的确定（四项原则与抽选方法）；五、价格数据的采集；六、CPI 的计算过程（环比 / 同比 / 平均 / 定基四种指数定义、定基指数自 2001 年起编、采用链式拉氏公式）） | 2024 | 官方公开统计解读 · **仅引用分类数、方法名称与短引用，不转载公式图与原文** | CPI 篮子每五年换一次 · CPI 不含奢侈品与投资品 · CPI 用链式拉氏公式 · CPI 定基指数 2001 年起编每五年换基期 |
| ev-062 | 官方文件 | 高 | 全文 | 国家统计局《国家统计局城市司负责人就价格指数基期轮换接受中国信息报专访》，**成文日期 2021-02-10**（索引号 `410A04-0502-202102-0002`，有效性标为「有效」），[统计局官网全文](https://www.stats.gov.cn/xxgk/jd/sjjd2020/202102/t20210210_1813322.html)（**本库通读全文**：四个问答——为何轮换、轮换调了什么（基本分类 262→268、新增外卖 / 新能源小汽车 / 网约车费用等、权数升降的具体百分点、剔除非洲猪瘟与疫情影响）、对指数的影响（CPI 同比平均约 0.03 个百分点）、新基期的举措） | 2021 | 官方公开统计解读 · **仅引用分类数、百分点与短引用，不转载原文** | CPI 基期每五年轮换且逢 5 和 0 · 基本分类由 262 增至 268 · 基期轮换对 CPI 同比影响约 0.03 个百分点 |
| ev-063 | 论文 | 高 | 全文 | The RECOVERY Collaborative Group. *Dexamethasone in Hospitalized Patients with Covid-19 — Preliminary Report.* **N Engl J Med. 2020 Jul 17 (online); 终版 N Engl J Med. 2021;384(8):693-704.** **PMID [32678530](https://pubmed.ncbi.nlm.nih.gov/32678530/)** · **DOI [10.1056/NEJMoa2021436](https://doi.org/10.1056/NEJMoa2021436)** · [PMC7383595](https://pmc.ncbi.nlm.nih.gov/articles/PMC7383595/)（**开放获取，本库读了全文**：方法、结果、表 1 / 表 2、图 2 / 图 3、讨论；**逐段核对了三个呼吸支持亚组的死亡率、率比与置信区间**） | 2020 | 外部文献 · **仅引用摘要与结论，不转载全文** | COVID 地塞米松按呼吸支持水平分层 |
| ev-064 | 官方文件 | 高 | 全文 | 联合国新闻（UN News）：*Testing and monitoring underway in suspected Russia plague death*，**2026-10-06**，[news.un.org](https://news.un.org/en/story/2026/10/1168533)（WHO 发言人 Christian Lindmeier 日内瓦记者会；**本库通读该报道全文**） | 2026 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 伊尔库茨克反瘟疫研究所事件 |
| ev-065 | 官方文件 | 高 | 摘要 | 俄罗斯联邦消费者权益及公民平安保护监督局（Rospotrebnadzor）**2026-10-04** 声明，经《俄罗斯报》（rg.ru）报道，[rg.ru](https://rg.ru/2026/10/04/v-rospotrebnadzore-zaiavili-ob-otsutstvii-chumy-v-gorodah-irkutskoj-oblasti.html)（**本库读的是媒体报道，非官方原始发布页**） | 2026 | 官方公开声明（经媒体报道） · **仅引用短句，不转载全文** | 伊尔库茨克反瘟疫研究所事件 |
| ev-066 | 官方文件 | 高 | 仅定位 | 俄方解除伊尔库茨克隔离（**2026-10-08**，俄国家通讯社），经 [Kyiv Independent](https://kyivindependent.com/russia-lifts-quarantine-in-irkutsk-region-where-lab-worker-allegedly-died-of-plague/) 报道（**本库仅见媒体报道，未打开官方原始发布页**） | 2026 | 官方公开行动（经媒体报道） · **仅引用短句，不转载全文** | 伊尔库茨克反瘟疫研究所事件 |
| ev-067 | 官方文件 | 高 | 全文 | 世界卫生组织（WHO）《Disease Outbreak News: Pneumonia of undetermined etiology – the Russian Federation》，**2026-10-10 发布**，**2026-DON620**，[who.int](https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON620)（**本库通读该 DON 全文**：Situation at a glance / Description / Public health response / WHO risk assessment / WHO advice） | 2026 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 伊尔库茨克反瘟疫研究所事件 |
| ev-068 | 官方文件 | 高 | 全文 | 欧洲疾病预防与控制中心（ECDC）《ECDC closely monitoring situation following case of pneumonia of unknown origin in Russia》，**2026-10-06 发布**，[ecdc.europa.eu](https://www.ecdc.europa.eu/en/news-events/ecdc-closely-monitoring-situation-following-case-pneumonia-unknown-origin-russia)（**本库通读该报道全文**；另见 ECDC 周报 CDTR 第 41 周，2026-10-09） | 2026 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 伊尔库茨克反瘟疫研究所事件 |
| ev-069 | 论文 | 高 | 摘要 | C. Guérin（PROSEVA Study Group）. *Prone Positioning in Severe Acute Respiratory Distress Syndrome.* **N Engl J Med. 2013 Jun 6;368(23):2159-68.** **PMID [23688302](https://pubmed.ncbi.nlm.nih.gov/23688302/)** · **DOI [10.1056/NEJMoa1214103](https://doi.org/10.1056/NEJMoa1214103)** · ClinicalTrials.gov **[NCT00527813](https://clinicaltrials.gov/study/NCT00527813)**（**本库只读了摘要**：全文在付费墙后；`陈述` 只写摘要给出的数字） | 2013 | 外部文献 · **仅引用摘要与结论，不转载全文** | ARDS 俯卧位通气 |
| ev-070 | 论文 | 高 | 摘要 | SPRINT Research Group. *A Randomized Trial of Intensive versus Standard Blood-Pressure Control.* **N Engl J Med. 2015 Nov 26;373(22):2103-16.** **PMID [26551272](https://pubmed.ncbi.nlm.nih.gov/26551272/)** · **DOI [10.1056/NEJMoa1511939](https://doi.org/10.1056/NEJMoa1511939)** · **PMC [4689591](https://pmc.ncbi.nlm.nih.gov/articles/PMC4689591/)**（开放获取；**本库只读了摘要**：`陈述` 只写摘要给出的风险比、P 值与 1 年时平均收缩压） | 2015 | 外部文献 · **仅引用摘要与结论，不转载全文** | 强化降压（SPRINT） |
| ev-071 | 指南 | 高 | 摘要 | 世界卫生组织（WHO）《*Manual for plague surveillance, diagnosis, prevention and control*》，**2024-09-25 发布**，ISBN 978-92-4-009042-2，[who.int](https://www.who.int/publications/i/item/9789240090422)（**本库经检索读取关键段落原文**：F1RDT 一线、疑似即治不依赖阳性检测、氟喹诺酮一线；**手册共 92 页，本库未通读全文**） | 2024 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 鼠疫不等确诊即治疗 |
| ev-072 | 指南 | 高 | 摘要 | 美国疾病控制与预防中心（CDC）《*Guidance for Responding to a Plague Bioterrorism Event*》，[cdc.gov](https://www.cdc.gov/plague/hcp/emergency-guidance/index.html)（**本库经检索读取关键段落原文**：24 小时内给药、10–14 天、飞沫隔离 48 小时、接触者 7 天预防；**CDC 页面对本库直接抓取返回 403，未通读全文**） | 2021 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 鼠疫不等确诊即治疗 |
| ev-073 | 指南 | 高 | 摘要 | Nelson CA, Kessel SM, Staley D, et al. *Antimicrobial Treatment and Prophylaxis of Plague: Recommendations for Naturally Acquired Infections and Bioterrorism Response.* **MMWR Recomm Rep. 2021;70(3):1-11.** **PMID [34264565](https://pubmed.ncbi.nlm.nih.gov/34264565/)** · [CDC 官方 PDF](https://www.cdc.gov/mmwr/volumes/70/rr/pdfs/rr7003a1-H.pdf)（**本库经检索读取关键段落原文**：FDA 批准药物清单；**PDF 对本库直接抓取返回 403，未通读全文**） | 2021 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 鼠疫不等确诊即治疗 |
| ev-074 | 教材 | 低 | 仅定位 | Longo D, Fauci AS, Kasper DL, Hauser SL, Jameson JL, Loscalzo J, Holland SM, Langford CA, eds. *Harrison's Principles of Internal Medicine*，**第 22 版**，McGraw Hill，© 2025，2025-06-17 出版，ISBN 9781265979317，[mheducation.com](https://www.mheducation.com/highered/mhp/product/harrison-s-principles-internal-medicine-twenty-second-edition-vol-1-vol-2.html)（**本库未取得原书，未核对任何章节页码**） | 2025 | 外部来源 · 仅引用定位 | 中国高血压指南命题 · GOLD2026 慢阻肺命题（**两者均作教材背景，未核验，不作核验证据**） |
| ev-075 | 教材 | 低 | 仅定位 | Kumar V, Abbas AK, Aster JC, eds. *Robbins and Cotran Pathologic Basis of Disease*，**第 10 版**，Elsevier，2020-06-19，ISBN 9780323531139，1392 页，[elsevier.com](https://shop.elsevier.com/books/robbins-and-cotran-pathologic-basis-of-disease/kumar/978-0-323-53113-9)（**本库未取得原书，未核对任何章节页码**） | 2020 | 外部来源 · 仅引用定位 | GOLD2026 慢阻肺命题的教材背景（**未核验，不作核验证据**） |
| ev-076 | 教材 | 低 | 仅定位 | Kaushansky K, Lichtman MA, Prchal JT, Levi MM, Burns LJ, Linch DC, eds. *Williams Hematology*，**第 10 版**，McGraw Hill，© 2021，2021-02-24 出版，ISBN 9781264264122，[mheducation.com](https://www.mheducation.com/highered/mhp/product/williams-hematology-10th-edition.html)（**本库未取得原书，未核对任何章节页码**） | 2021 | 外部来源 · 仅引用定位 | 无（**血学命题待取得原书后出**） |
| ev-077 | 教材 | 低 | 仅定位 | 王吉耀、葛均波、邹和建主编《**实用内科学**》**第 16 版**，人民卫生出版社，2022-06，ISBN 9787117324823，全 2 册，606.1 万字，[人卫商城书目页](https://www.pmphmall.com/gdsdetail/645494-323091)（**本库未取得原书，未核对任何章节页码**） | 2022 | 外部来源 · 仅引用定位 | 中国高血压指南命题的教材背景（**未核验，不作核验证据**） |
| ev-078 | 指南 | 高 | 摘要 | 中国高血压防治指南修订委员会、高血压联盟（中国）、中国医疗保健国际交流促进会高血压病学分会等《**中国高血压防治指南（2024年修订版）**》，《中华高血压杂志（中英文）》2024, 32(7): 603-700，**DOI [10.16439/j.issn.1673-7245.2024.07.002](https://doi.org/10.16439/j.issn.1673-7245.2024.07.002)**；英文版 *Clinical practice guideline for the management of hypertension in China*，**Chin Med J. 2024;137(24):2907-2952**，**DOI [10.1097/CM9.0000000000003431](https://doi.org/10.1097/CM9.0000000000003431)** · **PMID [39289992](https://pubmed.ncbi.nlm.nih.gov/39289992/)**（开放获取）（**本库经检索读取关键段落原文**：要点 4 定义与表 6 血压分类、要点 5C 降压目标、起始与维持药物治疗的推荐级别；英文版 LWW 页面对本库返回 403，**指南全文 98 页未通读**） | 2024 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 中国高血压指南 2024 降压目标 |
| ev-079 | 指南 | 高 | 摘要 | Global Initiative for Chronic Obstructive Lung Disease（GOLD）《**Global Strategy for the Diagnosis, Management, and Prevention of COPD — GOLD 2026 Report**》（v1.2，2025-11-20）·《**GOLD 2026 Pocket Guide**》（2025-11-11）·《**GOLD REPORT 2026 KEY CHANGES SUMMARY**》（2025-11-10），[goldcopd.org](https://goldcopd.org/2026-gold-report-and-pocket-guide/)（**本库经检索读取关键段落原文**：口袋指南的诊断标准与急性加重期用药、关键变化摘要的 ABE 分组标准调整说明；**报告 PDF 自标 `COPYRIGHT MATERIAL - DO NOT COPY OR DISTRIBUTE`，未通读全文**） | 2026 | 官方公开发布 · **仅引用短句与结论，不转载全文** | GOLD2026 慢阻肺诊疗 |

| 编号 | 类别 | 等级 | 核验深度 | 定位 | 时间 | 许可 | 引用处 |
|---|---|---|---|---|---|---|---|
| ev-080 | 教材 | 低 | 全文 | OpenStax《Physics》第 6 章 · Angle of Rotation and Angular Velocity，[m54176](https://github.com/openstax/osbooks-physics/blob/main/modules/m54176/index.cnxml)（**抓取该模块 cnxml 源文件通读**：转角 Δθ = Δs/r、角速度 ω = Δθ/Δt、切向速度 v = rω、单位换算与 Teacher Support） | 2020 | **CC BY 4.0** · **可自由复用** | 匀速圆周运动 |
| ev-081 | 教材 | 低 | 全文 | OpenStax《Physics》第 6 章 · Uniform Circular Motion，[m54181](https://github.com/openstax/osbooks-physics/blob/main/modules/m54181/index.cnxml)（**抓取该模块 cnxml 源文件通读**：向心加速度 a_c = v²/r = rω²、向心力 F_c = mv²/r、Key Terms 对向心力与离心力的定义、Teacher Support 的 `[BL][OL][AL]` 演示建议与离心力混淆说明） | 2020 | **CC BY 4.0** · **可自由复用** | 匀速圆周运动 · 向心力不是一种新的力 · 离心力误解 · 剪断绳子教法 |
| ev-082 | 教材 | 低 | 全文 | OpenStax《Physics》第 6 章 · Introduction（章首导言），[m54173](https://github.com/openstax/osbooks-physics/blob/main/modules/m54173/index.cnxml)（**抓取该模块 cnxml 源文件通读**：Teacher Support 要求教师 `Address any misconceptions about centrifugal force`，并指出圆周运动是本章入口） | 2020 | **CC BY 4.0** · **可自由复用** | 离心力误解（「教材预期会出现」这一条的出处） |
| ev-083 | 教材 | 低 | 全文 | OpenStax《Physics》第 18 章 · Introduction（章首导言），[m54417](https://github.com/openstax/osbooks-physics/blob/main/modules/m54417/index.cnxml)（**抓取该模块 cnxml 源文件通读**：Teacher Support 关于 `static` 一词「暗示不动，但常常并非如此」的提醒、章首复习清单要求万有引力与矢量） | 2020 | **CC BY 4.0** · **可自由复用** | 电荷 · 库仑定律 |
| ev-084 | 教材 | 低 | 全文 | OpenStax《Physics》第 18 章 · Electrical Charges, Conservation of Charge, and Transfer of Charge，[m54410](https://github.com/openstax/osbooks-physics/blob/main/modules/m54410/index.cnxml)（**抓取该模块 cnxml 源文件通读**：两种电荷与同号斥异号吸、电荷守恒、元电荷与单位、导体/绝缘体/半导体、接触/传导/感应带电与极化、Teacher Support 关于「静电如何与电荷转移相容」的提问） | 2020 | **CC BY 4.0** · **可自由复用** | 电荷 |
| ev-085 | 教材 | 低 | 全文 | OpenStax《Physics》第 18 章 · Coulomb's law，[m54414](https://github.com/openstax/osbooks-physics/blob/main/modules/m54414/index.cnxml)（**抓取该模块 cnxml 源文件通读**：F = kq₁q₂/r² 与符号判据、扭秤与平方反比、适用条件「相对彼此静止」、球外当球心、[AL] 关于静电被发现晚于引力的提问） | 2020 | **CC BY 4.0** · **可自由复用** | 库仑定律 |
| ev-086 | 教材 | 低 | 全文 | OpenStax《Physics》第 18 章 · Electric Field，[m54428](https://github.com/openstax/osbooks-physics/blob/main/modules/m54428/index.cnxml)（**抓取该模块 cnxml 源文件通读**：E = F/q_test 与试探电荷、「撤走试探电荷场仍存在」、点电荷场 E = k|Q|/r²、场线三规则与叠加、中性物体只可被吸引的科幻选择题） | 2020 | **CC BY 4.0** · **可自由复用** | 电场强度 |
| ev-087 | 教材 | 低 | 全文 | OpenStax《Physics》第 18 章 · Electric Potential，[m54426](https://github.com/openstax/osbooks-physics/blob/main/modules/m54426/index.cnxml)（**抓取该模块 cnxml 源文件通读**：电势能与参考点、U_E = kq₁q₂/r、电势 V = U_E/q 与「同一 Strategy」原话、点电荷电势、ΔV 与匀强场的关系、Teacher Support 对「电势能与电势」之别的强调） | 2020 | **CC BY 4.0** · **可自由复用** | 电势能与电势 |
| ev-088 | 教材 | 低 | 全文 | OpenStax《Physics》第 6 章 · Rotational Motion，[m54180](https://github.com/openstax/osbooks-physics/blob/main/modules/m54180/index.cnxml)（**抓取该模块 cnxml 源文件通读**：角加速度 α = Δω/Δt 与符号约定（逆时针为正）、θ/ω/α ↔ x/v/a 对照、恒定 α 的四条转动运动学方程、切向加速度 a = rα、力矩 τ = rF sinθ 与杠杆臂、净力矩为零、渔轮与旋转木马例题、龙卷风专栏与 Teacher Support 的杠杆演示） | 2020 | **CC BY 4.0** · **可自由复用** | 角加速度与转动运动学 · 力矩 |
| ev-089 | 官方文件 | 高 | 全文 | 《Guidelines for Writing an IANA Considerations Section in RFCs》，IETF，**BCP 26 · RFC 8126**（Obsoletes: 5226；第三版），M. Cotton / B. Leiba / T. Narten，2017-06 发布，[rfc-editor.org 全文](https://www.rfc-editor.org/rfc/rfc8126.txt)（**本库核到 §4.8 原文**——IETF Review 的定义：新值只通过 IETF Stream 的 RFC 分配、经 IETF Last Call 并由 IESG 批准为「具有 IETF 共识」，任何 RFC 类型均可，旧名「IETF Consensus」；并对照读毕 **§4.7 RFC Required、§4.9 Standards Action、§4.11 严格度阶梯**；全文 2635 行，**其余章节未核**） | 2017 | 官方公开规范 · **仅引用章节号与短引用，不转载全文** | IETF Review 的注册门槛 |
| ev-090 | 官方文件 | 高 | 摘要 | 美国疾病控制与预防中心（CDC）《**CDC Health Advisory: Severe Pulmonary Disease Associated with Using E-Cigarette Products**》，**2019-08-30 09:35 ET 发布**，文号 **CDCHAN-00421**，[CDC Stacks 存档](https://stacks.cdc.gov/view/cdc/81107)（**本库经检索读取关键段落**：截至 2019-08-27 全美 25 州报告 215 例可能病例；伊利诺伊州一名患者 **2019-07-29 住院、2019-08-20 死亡**；给出临床识别、上报与随访建议） | 2019 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-091 | 官方文件 | 高 | 全文 | Schier JG, Meiman JG, Layden J, et al.; CDC 2019 Lung Injury Response Group. *Severe Pulmonary Disease Associated with Electronic-Cigarette–Product Use — Interim Guidance*，**MMWR 2019-09-13（68 卷 36 期，787–790 页）；2019-09-06 提前发布（Early Release）**，DOI [10.15585/mmwr.mm6836e2](https://doi.org/10.15585/mmwr.mm6836e2)，[PMC6755818](https://pmc.ncbi.nlm.nih.gov/articles/PMC6755818/)（**开放获取，本库通读全文**：「**未发现一致的感染性病原证据**，因此怀疑原因为**化学暴露**」；监测**病例定义**的确诊项要求「呼吸道病毒检测面板阴性、流感 PCR 或快速检测阴性」等；含 2019-08-16 临床行动警报的转引） | 2019 | 官方公开出版物 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-092 | 官方文件 | 高 | 全文 | Ghinai I, Pray IW, Navon L, et al. *E-cigarette Product Use, or Vaping, Among Persons with Associated Lung Injury — Illinois and Wisconsin, April–September 2019*，**MMWR 2019-10-04（68 卷 39 期，865–869 页）**，DOI [10.15585/mmwr.mm6839e2](https://doi.org/10.15585/mmwr.mm6839e2)，[PMC6776374](https://pmc.ncbi.nlm.nih.gov/articles/PMC6776374/)（**开放获取，本库通读全文**：患者住院日期最早可溯至 **2019-04-24**；截至 2019-09-20 两州 127 例、86 例完成访谈，其中 **87% 使用含 THC 产品、66% 使用「Dank Vapes」、89% 从非正规渠道获得**） | 2019 | 官方公开出版物 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-093 | 官方文件 | 高 | 全文 | Blount BC, Karwowski MP, Morel-Espinosa M, et al. *Evaluation of Bronchoalveolar Lavage Fluid from Patients in an Outbreak of E-cigarette, or Vaping, Product Use–Associated Lung Injury — 10 States, August–October 2019*，**MMWR 2019-11-15（68 卷 45 期，1040–1041 页）**，DOI [10.15585/mmwr.mm6845e2](https://doi.org/10.15585/mmwr.mm6845e2)，[PMC6855513](https://pmc.ncbi.nlm.nih.gov/articles/PMC6855513/)（**开放获取，本库通读全文**：10 州 **29 份支气管肺泡灌洗液样本全部检出维生素 E 醋酸酯（VEA）**；截至 2019-10-15，报告物质使用信息的 867 例患者中 **86% 使用含 THC 产品**） | 2019 | 官方公开出版物 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-094 | 官方文件 | 高 | 全文 | Pray IW, Atti SK, Tomasallo C, Meiman JG. *E-cigarette, or Vaping, Product Use–Associated Lung Injury Among Clusters of Patients Reporting Shared Product Use — Wisconsin, 2019*，**MMWR 2020-03-06（69 卷 9 期，236–240 页）**，DOI [10.15585/mmwr.mm6909a4](https://doi.org/10.15585/mmwr.mm6909a4)，[PMC7367091](https://pmc.ncbi.nlm.nih.gov/articles/PMC7367091/)（**开放获取，本库通读全文**：**2019-07-10** 威斯康星州卫生服务部获报 5 名既往健康青少年；三个社交集群 8 例症状发作集中于 2019-06-18–07-21、全部使用黑市 THC 烟弹（含「Dank Vapes」）；推断黑市烟弹成分变化（含加入 VEA）**可能发生在 2019-06 之前不久**；对照：明尼苏达 2018 年缴获的烟弹**均未**检出 VEA、2019-09 缴获的**全部**检出） | 2020 | 官方公开出版物 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-095 | 官方文件 | 高 | 摘要 | 世界卫生组织（WHO）COVID-19 响应时间线——Archived: *WHO Timeline — COVID-19*（**2020-04-27 发布**，[who.int](https://www.who.int/news-room/detail/27-04-2020-who-timeline---covid-19)）与 *Listings of WHO's response to COVID-19*（2020-06-29 首版）；WHO **DON229《Pneumonia of unknown cause – China》**（**2020-01-05 发布**，[who.int](https://www.who.int/emergencies/disease-outbreak-news/item/2020-DON229)）（**本库逐页核对关键条目**：2019-12-31 WHO 中国办公室获报；2020-01-01 IMST 启动；01-04 社媒通报；01-05 DON 发布；01-10 临时指南；01-12 基因序列公开；01-13 泰国报告首例输出病例；01-30 宣布 PHEIC；03-11 评估「COVID-19 can be characterized as a pandemic」——均为页面原文） | 2020 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-096 | 论文 | 高 | 摘要 | Basavaraju SV, Patton ME, Grimm K, et al. *Serologic Testing of U.S. Blood Donations to Identify SARS-CoV-2-Reactive Antibodies: December 2019–January 2020*，**Clinical Infectious Diseases（2020-11-30 在线发表；2021 年刊出）**，DOI [10.1093/cid/ciaa1785](https://doi.org/10.1093/cid/ciaa1785)，[PMC7799215](https://pmc.ncbi.nlm.nih.gov/articles/PMC7799215/)（**本库读了摘要与结论**：**2019-12-13–2020-01-17** 九州的 7,389 份献血中 **106 份**全长刺突蛋白 pan-Ig 反应性、90 份复检中 **84 份具中和活性**；结论「SARS-CoV-2 **可能**在 2020-01-19 之前已引入美国」）；美国红十字会 **2020-12-01** 新闻稿，[redcross.org](https://www.redcross.org/about-us/news-and-events/press-release/2020/study-suggests-possible-new-covid-19-timeline-in-the-us.html)（**本库通读全文**：最早反应性样本来自 **2019-12-13–16 的加州、俄勒冈、华盛顿州**；提示低流行率下**无法完全排除交叉反应**） | 2020 | 外部文献 · **仅引用摘要与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-097 | 论文 | 高 | 全文 | King BA, Jones CM, Baldwin GT, Briss PA. *E-cigarette, or Vaping, Product Use-Associated Lung Injury: Looking Back, Moving Forward*，**Nicotine & Tobacco Research 2020-12-15；22(Suppl 1):S96–S99**，DOI [10.1093/ntr/ntaa186](https://doi.org/10.1093/ntr/ntaa186)，[PMC7792918](https://pmc.ncbi.nlm.nih.gov/articles/PMC7792918/)（**开放获取，本库通读全文**：截至 **2020-02-18** 全美 EVALI 住院 **2,807 例、死亡 68 例**；疫情 **2019-08 激增、09 月达峰**后回落；一致的急诊就诊**基线可溯至 2017-01–2019-06**；约 **20%** 患者仅使用含尼古丁产品） | 2020 | 外部文献 · **仅引用摘要与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-098 | 论文 | 高 | 摘要 | Grimm K, Saá P, Cheedarla N, et al. *Serologic Testing of US Blood Donations to Identify Severe Acute Respiratory Syndrome Coronavirus 2 and Other Coronaviruses, December 2019 to July 2020*，**Open Forum Infectious Diseases 2024；11(7)（2024-06-28 在线）**，DOI [10.1093/ofid/ofae351](https://doi.org/10.1093/ofid/ofae351)，[PMC11257073](https://pmc.ncbi.nlm.nih.gov/articles/PMC11257073/)（**本库读了摘要与关键段**：46,120 份献血样本中，**2019-12-13–2020-01-22** 采集的 13,364 份里 **9 份确诊阳性**；结论「SARS-CoV-2 **很可能**在 2020-01-19 之前已存在于美国」） | 2024 | 外部文献 · **仅引用摘要与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-099 | 官方文件 | 高 | 摘要 | 世界卫生组织（WHO）《**Independent assessment of the origins of SARS-CoV-2**》（SAGO 溯源评估报告，**2025-06-27 发布**，[报告页](https://www.who.int/publications/m/item/independent-assessment-of-the-origins-of-sars-cov-2-from-the-scientific-advisory-group-for-the-origins-of-novel-pathogens)；报告以 CC BY-NC-SA 3.0 IGO 授权）及同日新闻稿 *WHO Scientific advisory group issues report on origins of COVID-19*，[who.int](https://www.who.int/news/item/27-06-2025-who-scientific-advisory-group-issues-report-on-origins-of-covid-19)（**本库读了新闻稿与报告要点**：「**所有假说仍在桌上**」；「现有证据权重」支持动物溢出（直接来自蝙蝠或经中间宿主）；WHO 请求中方分享疫情早期数百条基因序列、武汉市场动物信息与实验室生物安全信息，**迄今未获提供**） | 2025 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |

| 编号 | 类别 | 等级 | 核验深度 | 定位 | 时间 | 许可 | 引用处 |
|---|---|---|---|---|---|---|---|
| ev-100 | 官方文件 | 高 | 摘要 | 世界卫生组织（WHO）《**Statement on the second meeting of the International Health Regulations (2005) Emergency Committee regarding the outbreak of novel coronavirus (2019-nCoV)**》，**2020-01-30 发布**，[who.int](https://www.who.int/news/item/30-01-2020-statement-on-the-second-meeting-of-the-international-health-regulations-%282005%29-emergency-committee-regarding-the-outbreak-of-novel-coronavirus-%282019-ncov%29)（**本库读取原文关键段**：宣布构成「国际关注的突发公共卫生事件」（PHEIC）；当日数字——中国确诊 **7,711 例**（疑似 12,167 例）、死亡 **170 人**、124 人治愈出院；中国以外 **18 国 83 例**，其中仅 7 例无中国旅行史、3 国已出现人传人、无死亡） | 2020 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-101 | 官方文件 | 高 | 摘要 | 世界卫生组织（WHO）《**WHO calls for further studies, data on origin of SARS-CoV-2 virus, reiterates that all hypotheses remain open**》，**2021-03-30 发布**，[who.int](https://www.who.int/news/item/30-03-2021-who-calls-for-further-studies-data-on-origin-of-sars-cov-2-virus-reiterates-that-all-hypotheses-remain-open)（**本库读取原文关键段**：联合研究国际团队武汉实地考察期为 **2021-01-14–02-10**；「**all hypotheses remain on the table**」「we have not yet found the source of the virus」） | 2021 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-102 | 官方文件 | 高 | 摘要 | 世界卫生组织（WHO）《**Statement on the fifteenth meeting of the IHR (2005) Emergency Committee on the COVID-19 pandemic**》，**2023-05-05 发布**（第十五次会议 2023-05-04 举行），[who.int](https://www.who.int/news/item/05-05-2023-statement-on-the-fifteenth-meeting-of-the-international-health-regulations-%282005%29-emergency-committee-regarding-the-coronavirus-disease-%28covid-19%29-pandemic)（**本库读取原文关键段**：「COVID-19 is now an established and ongoing health issue which **no longer constitutes a public health emergency of international concern (PHEIC)**」） | 2023 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-103 | 官方文件 | 高 | 摘要 | 联合国新闻（UN News）中文版两篇报道：〈**［专题报道］新冠病毒溯源专家组：实验室泄漏「极不可能」 冷链传播「值得探索」**〉（**2021-02-09**，[news.un.org](https://news.un.org/zh/story/2021/02/1077632)）；〈**新冠病毒溯源专家组发表初步研究报告 世卫组织总干事表示「所有的假定仍然都在考虑范围之内」**〉（**2021-03-30**，[news.un.org](https://news.un.org/zh/story/2021/03/1081102)）（**本库通读两篇报道**：02-09 发布会——实验室泄漏「极为不可能」、经中间宿主传播「仍是最有可能的感染路径」、冷链「需要进一步探索」，专家组 17 名中方 + 17 名外方、考察期 2021-01-14–02-10；03-30 报告——早期病例约 **28%** 与华南海鲜市场有关联、**23%** 与武汉市内其他市场有关联、**45%** 无市场暴露史，「有关华南市场在疫情起源过程中所扮演的角色，以及病毒如何被引入市场，目前无法得出确定的结论」） | 2021 | 官方媒体发布 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-104 | 官方文件 | 高 | 摘要 | 意大利政府部长会议主席令（DPCM，**2020-03-09**）《**Ulteriori disposizioni attuative del decreto-legge 23 febbraio 2020, n. 6, recante misure urgenti in materia di contenimento e gestione dell'emergenza epidemiologica da COVID-19, applicabili sull'intero territorio nazionale**》，《意大利官方公报》（Gazzetta Ufficiale）总第 62 期，法令编号 **20A01558**，[gazzettaufficiale.it](https://www.gazzettaufficiale.it/eli/id/2020/03/09/20A01558/sg)（**本库读取原始页关键句**：防控措施「applicabili sull'intero territorio nazionale」——适用**全国领土**） | 2020 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-105 | 官方文件 | 高 | 摘要 | 美国《**Proclamation on Declaring a National Emergency Concerning the Novel Coronavirus Disease (COVID-19) Outbreak**》（总统公告，**2020-03-13 签署**，第 9994 号），**2020-03-18 刊登于《联邦公报》85 FR 15337**，文档号 **2020-05794**，[白宫原文](https://www.whitehouse.gov/presidential-actions/proclamation-declaring-national-emergency-concerning-novel-coronavirus-disease-covid-19-outbreak/)；[Federal Register](https://www.federalregister.gov/documents/2020/03/18/2020-05794/declaring-a-national-emergency-concerning-the-novel-coronavirus-disease-covid-19-outbreak)（**本库读取白宫原文关键句**：「the COVID-19 outbreak in the United States constitutes a national emergency, **beginning March 1, 2020**」；卷页、文档号经 Federal Register API 核对） | 2020 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-106 | 官方文件 | 高 | 摘要 | 英国政府《**Prime Minister's statement on coronavirus (COVID-19): 23 March 2020**》（首相全国讲话），**2020-03-23 发布**，[gov.uk](https://www.gov.uk/government/speeches/pm-address-to-the-nation-on-coronavirus-23-march-2020)（**本库读取原文关键句**：「**you must stay at home**」；警方获权「including through fines and dispersing gatherings」执行） | 2020 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-107 | 官方文件 | 高 | 摘要 | 印度新闻信息局（PIB）《**PM calls for complete lockdown of entire nation for 21 days**》（新闻公报，**2020-03-24 发布**），编号 **PRID 1608009**，[pib.gov.in](https://pib.gov.in/PressReleasePage.aspx?PRID=1608009)（**本库读取原文关键句**：「complete lockdown of the entire nation for the next 21 days **beginning at midnight tonight**」） | 2020 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-108 | 官方文件 | 高 | 摘要 | （武汉）《**武汉市新型冠状病毒感染的肺炎疫情防控指挥部通告（第1号）**》，**2020-01-23 凌晨发布**，新华社/新华网转载稿，[新华网](http://www.xinhuanet.com/politics/2020-01/23/c_1125495557.htm)（**本库读取转载原文关键句**：「自1月23日10时起，武汉全市城市公交、地铁、轮渡、长途客运暂停运营；无特殊原因，市民不要离开武汉；机场、火车站离汉通道暂时关闭」） | 2020 | 官方通告经官方通讯社发布 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-109 | 官方文件 | 高 | 摘要 | 武汉市江汉区档案馆《**2020年武汉市江汉区大事记**》，**发布 2022-08-26**，[江汉区人民政府网站（大事记·已归档）](https://www.jianghan.gov.cn/ztzl/jlxkgc/dsj/202301/t20230103_2123259.shtml)（**本库读取原文关键句**：「1月1日中共江汉区委、区人民政府果断决策，华南海鲜市场闭市」；同页另载「1月23日10时起，武汉全市离汉通道关闭」） | 2022 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-110 | 论文 | 高 | 摘要 | Apolone G, Montomoli E, Manenti A, et al. *Unexpected detection of SARS-CoV-2 antibodies in the prepandemic period in Italy*，**Tumori Journal 2021；107(5):446–451（2020-11-11 在线）**，DOI [10.1177/0300891620974755](https://doi.org/10.1177/0300891620974755)，[PMC8529295](https://pmc.ncbi.nlm.nih.gov/articles/PMC8529295/)（开放获取，CC BY；**本库读了摘要**：2019-09–2020-03 筛查队列 **959 名无症状者**中 **111 份（11.6%）**RBD 抗体阳性，最早自 **2019-09**（当月 14%），2020-02 第二周出现 **>30% 聚集**、伦巴第最高 **53.2%**；**该文发表后同刊另有 3 篇评论（2021），本库未逐一通读**） | 2020 | 外部文献 · **仅引用摘要与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-111 | 论文 | 高 | 摘要 | Deslandes A, Berti V, Tandjaoui-Lambotte Y, et al. *SARS-CoV-2 was already spreading in France in late December 2019*，**International Journal of Antimicrobial Agents 2020；55(6):106006（2020-05-03 在线）**，DOI [10.1016/j.ijantimicag.2020.106006](https://doi.org/10.1016/j.ijantimicag.2020.106006)，[PMC7196402](https://pmc.ncbi.nlm.nih.gov/articles/PMC7196402/)（**本库读了摘要并核对该文关键段**：巴黎北部医院 ICU **2019-12-02–2020-01-16** 收治的流感样病例回顾复检——58 例中 14 份存档样本纳入分析，一名 **2019-12-27** 急诊就诊的 42 岁男性样本 RT-PCR 阳性；其末次出国为 2019-08；作者称疫情「在法国开始得早得多」） | 2020 | 外部文献 · **仅引用摘要与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-112 | 论文 | 高 | 摘要 | La Rosa G, Mancini P, Bonanno Ferraro G, et al. *SARS-CoV-2 has been circulating in northern Italy since December 2019: Evidence from environmental monitoring*，**Science of the Total Environment 2021；750:141711（2020-08-15 在线）**，DOI [10.1016/j.scitotenv.2020.141711](https://doi.org/10.1016/j.scitotenv.2020.141711)，[PMC7428442](https://pmc.ncbi.nlm.nih.gov/articles/PMC7428442/)（**本库读了摘要与关键段**：米兰/伦巴第、都灵/皮埃蒙特、博洛尼亚/艾米利亚-罗马涅三地 5 座污水处理厂 **2019-10–2020-02** 的 40 份复合进水样本中 15 份经两套方法确认阳性，**最早阳性样本采集于 2019-12-18（米兰与都灵）**，博洛尼亚为 2020-01-29；**2018-09–2019-06 的 24 份对照样本均为阴性**；意大利首例本土病例为 2020-02-21） | 2020 | 外部文献 · **仅引用摘要与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-113 | 论文 | 高 | 摘要 | Althoff KN, et al. *Antibodies to Severe Acute Respiratory Syndrome Coronavirus 2 (SARS-CoV-2) in All of Us Research Program Participants, 2 January to 18 March 2020*，**Clinical Infectious Diseases 2022；74(4):584–590（2021-06 在线）**，DOI [10.1093/cid/ciab519](https://doi.org/10.1093/cid/ciab519)，[PMC8384413](https://pmc.ncbi.nlm.nih.gov/articles/PMC8384413/)；配套：美国国立卫生研究院（NIH）新闻稿 *NIH study offers new evidence of early SARS-CoV-2 infections in U.S.*（**2021-06-15**，[nih.gov](https://www.nih.gov/news-events/news-releases/nih-study-offers-new-evidence-early-sars-cov-2-infections-us)，本库经 web.archive.org 快照核读）（**本库读了摘要与新闻稿**：**24,079 名参与者**的 2020-01-02–03-18 血样经两套血清学方法序贯检测，**9 人阳性**——最早 01-07（伊利诺伊）、01-08（马萨诸塞），涉及 5 州（IL/MA/WI/PA/MS），其中 **7 人早于本州首例确诊**；结论「SARS-CoV-2 infections **weeks prior to the first recognized cases** in 5 US states」） | 2021 | 外部文献 · **仅引用摘要与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-114 | 官方文件 | 中 | 全文 | 美国马里兰州弗雷德里克市「隔离实验室社区咨询委员会」（CLCAC）《**Report on USAMRIID and Fort Detrick Incidents to Frederick Mayor, Board of Aldermen, and County Council**》，**报告日期 2020-01-23**，[cityoffrederickmd.gov（PDF 存档）](https://www.cityoffrederickmd.gov/DocumentCenter/View/17648/CLCAC-Report-to-Mayor-Board-of-Aldermen-and-County-Council-January-2019)（**本库对该 PDF 本地抽取文本通读**：CDC **2019-07-15** 函令 USAMRIID 暂停联邦管制病原研究，委员会 **2019-08-02** 获告知；**2019-10-08** 公开说明会；问题包括培训、标准操作程序与蒸汽灭菌设施（2018-05 暴雨受损）；委员会结论倾向「对社区风险很小」但表示无法独立确认；**CDC 未公开发布该函令原文**） | 2020 | 官方公开（地方委员会）· **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |
| ev-115 | 官方文件 | 高 | 摘要 | 美国陆军公共事务（U.S. Army Public Affairs）《**U.S. Army medical research institute continues work on coronavirus**》，**2020-04-01 发布**，[army.mil](https://www.army.mil/article/234182/u_s_army_medical_research_institute_continues_work_on_coronavirus)（**直连返回 403，本库经 web.archive.org 快照核读**：CDC **2020-03-27 函件**完全恢复 USAMRIID 的联邦管制病原登记；**2019-07** 因生物安全程序问题被暂停；「Many of the problems stemmed from the failure of Fort Detrick's steam sterilization plant」；称无人员健康、公共卫生或环境风险） | 2020 | 官方公开发布 · **仅引用短句与结论，不转载全文** | 新冠大流行时间线与溯源事件 |

> [!CAUTION]
> **`ev-009` ~ `ev-012` 已作废。** 它们是本库早期为了演示格式而**构造的示例数据**，
> 描述中的课堂观察与测评从未发生过。
>
> 编号**不回收**（保留痕迹），但**不得再被任何条目引用**。
> 引用它们的 3 个条目已于 2026-10-05 全部重写或删除。

> [!NOTE]
> **编号不连续是有意的。** `ev-xxx` 一旦分配就不再改变——删掉条目也不会回收编号，
> 因为已有条目引用过它。这跟 `id` 字段同一个道理。

> [!IMPORTANT]
> **引用外部来源时，必须遵守其原始许可协议。**
> 本库只存**定位、短引用、原创摘要与结论**，不复制受版权保护的表达。

## 等级说明

| 断言类型 | 等级阶梯（高 → 低） |
|---|---|
| 命题 | 系统综述 / 元分析 > 随机对照 > 队列 > 病例 > 专家意见 > **教材本身** |
| 教法 | 可复现的课堂实验 > 准实验 > 大样本课堂数据 > 单一课堂经验 > 专家直觉 |

> [!IMPORTANT]
> **教材在命题的证据金字塔里等级很低**，但学生把它当最高权威。
> 这正是本项目存在的理由。
>
> 同时，**单一课堂经验在教法里是合法证据**——教法条件性强、迁移性差，
> 把医学标准硬套过来会把有效的本土经验全部滤掉。

### 一个真实的不对称：初中级开放教材几乎都是 NC

采集时发现的规律，记录在此以免重复踩：

| 学段 | 来源 | 许可 |
|---|---|---|
| **高中** | OpenStax《Physics》（`osbooks-physics`） | **CC BY 4.0** ✅ 可自由复用 |
| **初中** | Utah State Board of Education 6 / 7 / 8 年级科学 | **CC BY-NC-SA 3.0** ❌ 仅可引用 |
| 初中（上游） | CK-12 Foundation（Utah 教材的内容来源） | **CC BY-NC** ❌ 仅可引用 |

> [!WARNING]
> **高中级能自由复用，初中级只能引用。**
>
> 美国中学 OER 大量基于 CK-12，而 CK-12 是 **NC**。
> 所以「扩充到初中知识点」在许可上比高中**更受限**——
> 条目只能写**我们自己的摘要 + 短语级引用**，不能搬用教材表述。

### 另一类限制：初中教材多没有教学指导

| 来源 | 有结构化教学指导吗 |
|---|---|
| OpenStax《Physics》 | ✅ **580 条 Teacher Support**，含 649 个分组标记 |
| Utah 7 年级 | ❌ 学生用书，**没有** Teacher Support / misconception 标注 |

**含义**：初中源能提供**知识内容与学段边界**（如"矢量推迟到高中"），
但**提供不了分档教法**。初中级的 `教法` 需要另找来源，或由教师贡献。

### 一个真实的许可陷阱：许可不随教材传播

OpenStax 教材正文里**内嵌 PhET 模拟**（`<iframe>` + OpenStax 短链，
外层 `<media class="os-embed">` 带一段描述）。

实测结果（读**模拟产物自身的头部**，权威来源）：

| 层 | 内容 | 许可 |
|---|---|---|
| 教材 | OpenStax《Physics》 | **CC BY 4.0** ✅ |
| 教材内嵌的模拟 | PhET「Forces and Motion: Basics」 | **CC BY-NC 4.0** ❌ |
| 抽查的另外三个模拟 | my-solar-system / bending-light / color-vision | **CC BY-NC 4.0** ❌ |

> [!CAUTION]
> **「教材可以自由复用」不能推出「教材里嵌的东西也可以」。**
>
> PhET 模拟文件头部原文：
> `COMMERCIAL USE REQUIRES A COMMERCIAL LICENSE AGREEMENT FROM THE UNIVERSITY OF COLORADO BOULDER.`
>
> 并且**要求在「使用处附近」标注归属**，推荐措辞：
> `Simulation by PhET Interactive Simulations, University of Colorado Boulder, licensed under CC BY-NC 4.0`
>
> **照抄教材结构的再发布者会踩到这一条。**
>
> 这也说明：**逐条核实许可不能靠印象**——我原先以为 PhET 是 CC BY，**实测推翻了它**。

### 一类特殊的高等级证据：出版社勘误表

`ev-014` `ev-015` 是**出版方自己发布的勘误表**。对「某教材某处有缺陷」这类命题，
它们比教材本身更有力——因为它们是**对该教材内容的权威声明**，不需要第三方推断。

但必须分清同一份证据能支持哪个命题：

| 命题 | 需要什么 | 勘误表够吗 |
|---|---|---|
| 「出版社声明 p.13 漏字」 | 读勘误表 | ✅ **够** |
| 「教材 p.13 真的漏字」 | 翻开教材 | ❌ 不够（勘误表可能滞后，新印次或已修正） |

### 开放教材的许可分两档，别混

`ev-016`~`ev-018` 都来自 OpenStax，但许可不同：

| 教材 | 许可 | 能做什么 |
|---|---|---|
| OpenStax《Physics》 | **CC BY 4.0** | 可自由复用正文（署名即可） |
| OpenStax《College Physics 2e》 | **CC BY-NC-SA 4.0** | **只能引用定位与短引用**，不可复用正文 |

**筛查结果**：OpenStax 的 55 个教材仓库中，只有 **13 个是 CC BY**，其余 **41 个含 NC**。

> [!IMPORTANT]
> **本库是 CC BY-SA 4.0（无 NC），与 NC 内容不兼容。**
> **同一出版社的书，许可可能不同，必须逐本查**——本例中《Physics》是 CC BY，
> 而同社的《College Physics 2e》和《University Physics》都是 CC BY-NC-SA。

## 原始数据

| 文件 | 内容 | 可复算 | 是证据吗 |
|---|---|---|---|
| [`构造数据-欧姆定律演示.csv`](构造数据-欧姆定律演示.csv) | `U = 10 × I` 的**构造**数据。**没有任何测量发生**，也没有温度记录 | ✅ 算术可复算 | ❌ **不是证据**——仅示范欧姆关系长什么样 |
| [`os-teacher-markers.csv`](os-teacher-markers.csv) | OpenStax《Physics》段落级受众标记明细（419 行，含 commit 哈希） | ✅ [脚本](os-teacher-markers.py) 可重跑 | ✅ 是（对源文件的统计） |

> [!IMPORTANT]
> **「可复算」与「是证据」是两件事。**
>
> 上表第一行**算术上完全可复算**（`5.0 / 10.00 = 0.50`），
> 而它**不能支撑任何关于真实世界的命题**——因为**没有人测过**。
>
> `ev-002` 当年就是凭着「可复算」被登记为**等级「高」**的。
