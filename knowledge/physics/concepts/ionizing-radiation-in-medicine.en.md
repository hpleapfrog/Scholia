---
id: kb:physics:ionizing-radiation-in-medicine
type: 知识点
title: "Ionizing radiation in medicine"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done "Radioactive decay" and need to explain medical imaging and radiotherapy and to separate activity, absorbed dose, and equivalent dose
  条件: covers tracers and radiopharmaceuticals, the gamma camera / SPECT / PET, absorbed and equivalent dose, background and diagnostic doses, radiotherapy, and protection only; X-ray production, radioimmunoassay, food irradiation, quantitative MRI, radiobiology, treatment protocols, and nuclear accidents are out of scope
edges:
  先修: ["[Radioactive decay](radioactive-decay.en.md)"]
  支持: []
  攻击: []
evidence: [ev-187, ev-188, ev-189]
license: CC-BY-SA-4.0
---

> **English version of [`医学中的电离辐射.md`](医学中的电离辐射.md).**

> [!TIP]
> **After reading this entry you should** be able to explain why a radiopharmaceutical works as a tracer, how PET localizes a source with two oppositely directed photons, separate activity in `Bq` from absorbed dose in `Gy` and equivalent dose in `Sv`, and use the therapeutic ratio to explain why radiotherapy uses several beam directions and many fractions

## Definition

**Ionizing radiation in medicine** means using X-rays or the radiation from radionuclides for diagnosis and treatment. There are two main lines:

- **Diagnosis**: attach a small amount of a radionuclide to a drug (a **radiopharmaceutical**) and detect from outside the body where it concentrates; or pass X-rays through the body to form an image
- **Treatment**: deliver a large enough dose to a tumour while sparing normal tissue

**Why tracing works**: the textbook gives two reasons — gamma rays penetrate tissue easily, and **decay depends only on the nuclide, not on the compound it is in**. Attaching a radionuclide to a compound that a particular organ takes up is called **tagging**. Detecting the position and intensity of gamma rays outside the body then reveals the drug's distribution.

| Study | Nuclide | Typical activity | Note |
|---|---|---|---|
| Thyroid scan | `131I` | `0.05 mCi` | The thyroid concentrates iodine, cancerous cells even more; low uptake indicates hypothyroidism |
| Bone scan | `99mTc` | `10 mCi` | Technetium-99m can be attached to many compounds |
| Brain / whole-body PET | `18F`, `11C`, `13N`, `15O` | `10–50 mCi` | β⁺ emitters, see below |

- `99mTc` is the workhorse: the textbook estimates that about **80%** of radiopharmaceutical procedures use it. Its metastable state emits a single `0.142 MeV` gamma ray, with a `6.0 h` half-life, and it is produced by neutron activation of molybdenum to `99Mo`, which then undergoes β− decay
- Activity conversion: `1 mCi = 3.7×10^7 Bq`
- Other examples: thallium-201 follows the blood for heart studies; gallium-67 concentrates where cells grow rapidly or where there is infection

**Three imaging devices**:

- **Gamma camera (Anger camera)**: a lead collimator admits gamma rays from one direction only into an array of detectors, and a computer reconstructs the image; it is **two-dimensional and has no depth information**
- **SPECT**: detectors rotate around the patient to give a three-dimensional distribution; spatial resolution is about `1 cm`, but contrast is good
- **PET**: uses β⁺ emitters. The positron soon meets an electron and the two **annihilate**, emitting two `0.511 MeV` gamma photons in nearly opposite directions. When detectors on opposite sides receive a pair **simultaneously**, the annihilation point must lie on the line between them; several such lines intersect at the source. Resolution is about `0.5 cm`
- **MRI** is not nuclear-radiation imaging: it manipulates hydrogen nuclear spins with a strong magnetic field and radio-frequency pulses and uses no ionizing radiation. The textbook mentions it only in a sidebar, and this entry does not develop it

> [!IMPORTANT]
> **Activity is not dose.**
>
> Activity `R = λN` describes how many decays per second happen in the **source** (unit Bq); dose describes how much energy **human tissue** absorbs and what biological effect that produces. A source of high activity can deliver a small dose if it is far away and the exposure is short. Conversely, an alpha emitter is stopped by skin outside the body but is more dangerous once inhaled, because its range is short and its ionization is concentrated. Being exposed is also not the same as being contaminated: external exposure stops when you leave the source, while contamination means radioactive material has entered the body or sits on a surface.

**How dose is booked**:

- **Absorbed dose** `D = E/m`: the ionizing energy absorbed per kilogram of tissue. `1 Gy = 1 J/kg = 100 rad`
- **Equivalent dose** `H = D × RBE`: the same 1 Gy produces different biological effects for different radiations. `1 Sv = 1 Gy × RBE = 100 rem`
- **RBE (relative biological effectiveness, also called the quality factor)** is approximate:

| Radiation | RBE |
|---|---|
| X-rays, γ, β above `32 keV` | 1 |
| β below `32 keV` | 1.7 |
| Thermal to slow neutrons | 2–5 |
| Fast neutrons, protons | 10 (body) / 32 (eyes) |
| α, accelerator heavy ions | 10–20 |

- Example: 2 rad of gamma rays is 2 rem; 2 rad of alpha particles is `2 × 20 = 40 rem` — the same absorbed energy, with a twentyfold difference in biological effect
- A 50 kg person absorbing 1 J over the whole body: `1 J / 50 kg = 0.02 Gy = 2 rad`

**Background and diagnostic doses** (textbook table, world averages):

| Source | Dose |
|---|---|
| Cosmic rays | `0.39 mSv/y` |
| Soil and building materials | `0.48 mSv/y` |
| Radon gas | `1.2 mSv/y` |
| Internal nuclides (`40K`, `14C`, `226Ra`) | `0.29 mSv/y` |
| Medical and dental | `0.40 mSv/y` |
| **Total** | **`2.8 mSv/y`** |

| Examination | Effective dose |
|---|---|
| Chest X-ray | `0.02 mSv` |
| Dental X-ray | `0.01 mSv` |
| Mammogram | `0.40 mSv` |
| Head CT | `2.0 mSv` |
| Abdomen CT | `10.0 mSv` |

- The textbook notes that CT accounts for less than 20% of X-ray procedures but about 50% of the annual medical dose
- Recomputation: one abdomen CT at `10 mSv` is about `10 / 2.8 ≈ 3.6` years of the world-average background; one chest X-ray at `0.02 mSv` is about `0.02 / 2.8 × 365 ≈ 2.6` days

**Radiotherapy**:

- Cancer cells divide rapidly and are more radiation-sensitive, but normal tissue is damaged too. The **therapeutic ratio** = abnormal cells killed / normal cells killed
- **Geometric convergence**: several narrow beams pass through the patient from different directions and cross at the tumour. Each beam gives a modest dose to normal tissue, and the doses add up at the crossing point
- **Fractionation**: the textbook's typical protocol is three to five treatments per week, `200 rem` each, for several weeks; normal tissue has time to repair between treatments
- Other methods: implant radioactive seeds in the prostate; treat thyroid cancer with radioactive iodine (the thyroid concentrates iodine); tag antibodies and return them to the patient so the radioactivity concentrates in the tumour
- The textbook's dose table (selected): lung `10–20 Sv`, breast `50–80+ Sv`, brain/neck/bone/soft tissue/thyroid `80+ Sv`. These are **localized, fractionated** tumour doses, not whole-body doses

**Protection**: shielding, greater distance, and shorter exposure time. The textbook gives an occupational whole-body limit of `20–50 mSv/y`, with the public limit at 1/10 of that; the public limit for nuclear power is `0.05 mSv/y`.

> [!NOTE]
> **Source problems and library additions** (ev-187/ev-188/ev-189)
>
> 1. m42654 gives the prostate seed nuclides as `135I` (6 months) and `103Pd` (3 months). That isotope/half-life pairing cannot be verified within the material cited here, so this entry keeps only the seed mechanism and **does not use those numbers**; it is recorded as unchecked.
> 2. m42652 says "about `5 mSv` (0.5 rem) per dental X-ray", while its own table gives `0.01 mSv` for a dental X-ray — a difference of about 500×. This entry uses the table value, not the 5 mSv in the body text.
> 3. m42652 defines a low dose as "less than `100 mSv`" and a moderate dose as "`0.1 Sv` to `1 Sv`"; since `0.1 Sv = 100 mSv`, the two bands overlap at the boundary. This entry uses the low/moderate/high labels qualitatively and does not treat the boundary as a sharp threshold.
> 4. m42654's dose table lists `80+ Sv` directly for the brain, neck, bone, and other sites without saying that these are fractionated, localized values under a specific technique; it also mixes "200 rem" with Gy, which agree numerically only when RBE = 1.
> 5. m42649 says the annihilation energy comes from "the destruction of an electron or positron mass"; in fact the **two** rest masses of an electron and a positron (`1.022 MeV` in total) annihilate into two `0.511 MeV` photons. The number is right, the wording is not precise.
> 6. The textbook introduces MRI only through a sidebar analogy, "tiny radio transmitters" (hydrogen nuclear spins); the strong field, radio-frequency pulses, relaxation, and gradient encoding are background supplied here and do not come from these three modules.
>
> **Library additions not given by the textbook**: how many years or days of background `10 mSv` and `0.02 mSv` represent; the fiftyfold gap between `0.75 Sv` and `15 mSv`; the conversion of `50–80 Sv` into 25–40 fractions at `2 Sv` each; and the distinctions "activity is not dose" and "exposure is not contamination". The textbook supplies the unit definitions, the RBE table, the background and diagnostic tables, and the radiotherapy protocol, but does not put these quantities on one common scale.

> [!WARNING]
> This entry explains physics and dose bookkeeping. It is **not medical advice**; actual examinations, treatments, and protection plans are decided by physicians and radiation-protection staff.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Radioactive decay](radioactive-decay.en.md) — half-life and activity are what make `99mTc`'s `6.0 h` and PET's short-lived nuclides intelligible |
| Related | [Binding energy and mass defect](binding-energy-and-mass-defect.en.md) — PET's `0.511 MeV` is the energy corresponding to the electron rest mass, and annihilation turns two rest masses into two photons |
| Recorded gap | **X-ray production (bremsstrahlung and characteristic X-rays)**, **quantitative radioimmunoassay**, **MRI spins, relaxation, and gradient encoding**, **ultrasound versus nuclear medicine**, **radiobiological mechanisms and repair kinetics**, **specific treatment protocols and fractionation**, **nuclear accidents and emergency response**, **food irradiation**, **medical-isotope production and radioactive waste** are not built in this repo |

## Argument

### K1 · Tracing works because decay depends on the nuclide, not the compound (no attack yet)

- **Claim**: attaching a gamma emitter to a drug lets external gamma detection read out the drug's distribution; to a good approximation the tag does not change the carrier's chemistry
- **Premises**: the textbook gives two reasons (gamma rays penetrate tissue; decay depends only on the nuclide, not the compound), defines tagging and radiopharmaceuticals, and lists thyroid iodine, thallium heart studies, and gallium tumours (ev-187)
- **Reasoning**: the nuclide's half-life and photon energy are set by the nucleus, while the compound determines which organ takes it up and how fast it is cleared. Attach `99mTc` to different carriers and the same gamma camera can image bone, heart, or kidney. The detector count rate is proportional to local activity, and collimation plus reconstruction gives the distribution. The thyroid is the clearest case: iodine is concentrated by the thyroid, cancerous cells take up even more, so a "hot" region corresponds to active tissue
- **Attacked by**: the textbook gives only the qualitative principle and no detector efficiency, attenuation correction, partial-volume effect, or pharmacokinetic model; "the tag does not change the chemistry" is only approximate — the textbook's own exercise mixes radioiodine with stable iodine as a carrier, showing that chemical quantity affects distribution; the gamma camera has no depth information and SPECT resolution is about 1 cm. This entry explains "why it can be seen", not "how to quantify it"
- **Evidence**: ev-187
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · PET localizes with the direction and simultaneity of annihilation photons (the `1.022 MeV` bookkeeping is a library addition)

- **Claim**: PET uses the two oppositely directed `0.511 MeV` photons from β⁺ annihilation, detects them in coincidence to fix the line containing the annihilation point, and intersects several lines to localize it
- **Premises**: the textbook says a β⁺ annihilates with an electron and emits two equal `0.511 MeV` gamma rays in opposite directions, detected simultaneously on both sides; it lists `11C`/`13N`/`15O`/`18F` and `0.5 cm` resolution (ev-187). The binding-energy module gives `E = mc²` and the `0.511 MeV` electron rest energy (ev-186)
- **Reasoning**: an electron and a positron each have a rest mass, `2 × 0.511 = 1.022 MeV` in total; annihilation turns this mass-energy into two photons. Momentum conservation requires the photons to go in opposite directions, and energy conservation gives `0.511 MeV` each. Receiving both photons at once places the annihilation point on the line between the two detectors; many detector pairs at different angles give many lines whose intersection is the source. Coincidence detection uses "simultaneous" as the filter, so no mechanical collimator is needed
- **Attacked by**: the textbook gives no coincidence time window, random coincidences, scatter, or attenuation correction, and no `18F` half-life or production; "simultaneous" is a nanosecond-scale experimental window, not mathematical simultaneity; the `1.022 MeV` here is obtained by adding two electron rest masses, while the textbook gives only the single `0.511 MeV`; the full β⁺ equation and threshold remain in the gap table of [radioactive decay](radioactive-decay.en.md)
- **Evidence**: ev-187, ev-186
- **Attribution**: @hpleapfrog · 2026-10-21

### K3 · Dose has two layers: energy absorbed and biological effect produced (no attack yet)

- **Claim**: absorbed dose `D = E/m` (Gy) describes energy deposition; equivalent dose `H = D × RBE` (Sv) describes biological effect. The two must not be mixed, and activity is not dose at all
- **Premises**: the textbook defines `1 rad = 0.01 J/kg`, `1 Gy = 100 rad`, `rem = rad × RBE`, and `1 Sv = 100 rem`, gives the RBE table and the 2 rad gamma versus 2 rad alpha example, and uses a misconception box to separate activity from dose (ev-188)
- **Reasoning**: the same 1 J gives 0.02 Gy when spread over a 50 kg body but 0.5 Gy when absorbed by a 2 kg forearm — a dose must name the tissue. At the same absorbed dose, alpha tracks are short and densely ionizing, so the damage is harder to repair and RBE is 10–20; for gamma rays it is 1. `H = D × RBE` combines the two into one comparable quantity. Since `1 Sv = 100 rem`, 2 rad of alpha particles is 40 rem = 0.4 Sv
- **Attacked by**: RBE is approximate and depends on radiation energy, dose rate, and biological endpoint; Sv is not a directly measurable physical quantity but a quantity weighted by RBE; the linear hypothesis (low-dose risk proportional to high-dose risk) is controversial, and the textbook itself says the evidence for hormesis is weak; the textbook's low/moderate dose boundary overlaps at 100 mSv; the `5 mSv` dental X-ray contradicts the table's `0.01 mSv`
- **Evidence**: ev-188
- **Attribution**: @hpleapfrog · 2026-10-21

### K4 · Radiotherapy works through the therapeutic ratio: concentrate dose in the tumour and let normal tissue repair between fractions (no attack yet)

- **Claim**: radiotherapy is feasible because of the therapeutic ratio — high dose in the tumour, with normal tissue repairing between fractions
- **Premises**: the textbook says cancer cells divide rapidly and are more sensitive; the therapeutic ratio is abnormal cells killed / normal cells killed; it describes geometric convergence, three to five 200-rem treatments per week, seeds, radioactive iodine, and tagged antibodies (ev-189)
- **Reasoning**: a single beam also doses the normal tissue it crosses; several beams from different directions give each path only a fraction of the dose and add up at the crossing point. Fractionation splits the total dose so normal tissue repairs between treatments, while tumour cells, being more radiation-sensitive, accumulate damage more readily. Radioactive iodine for thyroid cancer is chemical targeting: the thyroid (including cancerous cells) actively concentrates iodine, so the radiation is released on site
- **Attacked by**: the textbook gives no TCP/NTCP models, no fractionation radiobiology (reoxygenation, redistribution, repopulation, repair), and no proton or heavy-ion dosimetry; the `135I`/`103Pd` numbers are not used; "benefits far outweigh long-term risks" is uncited; the `80+ Sv` column lacks fractionation and localization context; 200 rem is mixed with Gy
- **Evidence**: ev-189
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; fills the medical-applications gap in 选必三 chapter 5 "Atomic nucleus", following "Radioactive decay" | Written after reading m42649/m42652/m42654 in full (ev-187/ev-188/ev-189) | @hpleapfrog |
