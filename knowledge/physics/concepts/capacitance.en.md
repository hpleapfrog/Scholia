---
id: kb:physics:capacitance
type: 知识点
title: "Capacitance"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have learned electric potential energy and potential and electric field strength and need to understand capacitors, the definition of capacitance, the parallel-plate formula, and how a dielectric changes capacitance
  条件: covers only the definition `C = Q/V`, the parallel-plate capacitance `C = κε₀A/d`, the stored energy `U = ½CV²`, a qualitative account of dielectric polarization, and common applications; motion of charged particles in an electric field, series and parallel combinations of capacitors, RC transients, breakdown, and leakage are not built here
edges:
  先修: ["[Electric potential energy and potential](electric-potential-energy.en.md)", "[Electric field strength](electric-field.en.md)"]
  支持: []
  攻击: []
evidence: [ev-175]
license: CC-BY-SA-4.0
---

> **English version of [`电容.md`](电容.md).**

> [!TIP]
> **After reading this entry you should** be able to compute capacitance with `C = Q/V` and `C = κε₀A/d`, compute stored energy with `U = ½CV²`, and explain why the energy conclusions for inserting a dielectric are opposite when the battery stays connected and when it has been disconnected

## Definition

A **capacitor** is a device made of two conductors (plates) with an insulating layer between them. When two metal plates face each other and are connected to the positive and negative terminals of a battery, they carry equal and opposite charges and a **uniform electric field** forms between them. This arrangement is a **parallel-plate capacitor**.

**Charging requires work against repulsion**: placing the first pair of positive and negative charges on the plates takes almost no work; the second pair must overcome the repulsion of the first; the third must overcome the first two, and so on. The work comes from the battery's chemical energy and ends up **stored in the electric field between the plates**. After the battery is disconnected, the charge and the energy remain on the capacitor; connect the plates to a lightbulb and it lights until the energy is used up.

**Capacitance** is defined as the magnitude of the charge on each plate `Q` divided by the potential difference `V` between the plates:

`C = Q/V`

`Q` is the magnitude of the charge on **each** plate and `V` is the potential difference from the negative to the positive plate; both are positive, so `C` is always positive. The unit of capacitance is `C/V`, called the **farad** (F); common subunits are `µF`, `nF`, and `pF`.

> [!IMPORTANT]
> **Capacitance is not determined by `Q` or `V`.**
>
> For a given capacitor, doubling `V` doubles `Q`, so the ratio `Q/V` is unchanged. Capacitance depends only on **geometry and materials**. The textbook's parallel-plate formula
>
> `C₀ = ε₀A/d`
>
> expresses this: `A` is the plate area, `d` the separation, and `ε₀ = 8.85×10⁻¹² F/m` the vacuum permittivity. The subscript 0 means the space between the plates is vacuum (or approximately air).

**Dielectric**: an insulating material inserted between the plates. It becomes **polarized** in the field — negative charge in its molecules shifts toward the positive plate and positive charge toward the negative plate, bound charge appears on its surfaces, the field between the plates weakens, the potential difference falls, and the capacitance rises for the same charge:

`C = κ ε₀A/d = κ C₀`

`κ` (kappa) is the **relative permittivity** (dielectric constant), dimensionless and greater than 1 for dielectrics. Values from the textbook's table: vacuum `1.00000`, air `1.00059`, Teflon `2.1`, polystyrene `2.56`, nylon `3.4`, paper `3.7`, fused quartz `3.78`, Pyrex glass `5.6`, neoprene rubber `6.7`, water `80`, strontium titanate `233`.

**Stored energy**: with voltage `V` across a capacitor of capacitance `C`, the stored electric potential energy is

`U_E = ½ C V²`

Using `Q = CV`, this can also be written `U_E = Q²/(2C) = ½ Q V`. Its form is analogous to the kinetic energy `½mv²`.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Electric potential energy and potential](electric-potential-energy.en.md) — `V` is the potential difference in the definition, and `U = qV` is the origin of the stored-energy formula |
| Prerequisite | [Electric field strength](electric-field.en.md) — the uniform field between the plates, `V = Ed`, and `E = σ/ε₀` are the premises for deriving the parallel-plate formula |
| Recorded gap | **Motion of charged particles in an electric field**, **series and parallel combinations of capacitors**, **RC charging and discharging transients**, **breakdown voltage and leakage**, **fringing fields (ignored by the parallel-plate formula)**, **the derivation of the energy density `u = ½ε₀E²`**, **microscopic models of dielectric polarization**, and **supercapacitors and capacitive sensors** are not built in this library |
| Related technology | Camera flashes, energy storage and filtering in circuits, and capacitors as components that store charge and energy |

## Arguments

### K1 · Parallel-plate capacitance is fixed by geometry (no attacks yet)

- **Claim**: the capacitance of a vacuum parallel-plate capacitor is `C₀ = ε₀A/d`, independent of the applied voltage
- **Premises**: the field between the plates is approximately uniform with `E = σ/ε₀`; the potential difference is `V = Ed`; the charge on each plate is `Q = σA`; the textbook's definition and formula (ev-175)
- **Reasoning**: substituting `Q = σA` and `V = Ed = (σ/ε₀)d` into the definition gives `C = Q/V = σA / [(σ/ε₀)d] = ε₀A/d`. The surface charge density `σ` cancels, showing that capacitance does not depend on the stored charge. Numerical check: for `A = 1.00 m²` and `d = 0.0010 m`, `C₀ = 8.85×10⁻¹² × 1.00 / 0.0010 = 8.85×10⁻⁹ F ≈ 8.9 nF`; at `V = 3.00×10³ V`, `Q = CV = 2.66×10⁻⁵ C`, matching the textbook's `2.7×10⁻⁵ C`
- **Evidence**: ev-175
- **Attacked**: the formula ignores fringing fields and holds only when `d` is much smaller than the plate dimensions; real capacitors have leakage, dielectric loss, and a breakdown voltage; it is also wrong to take "capacitance depends only on geometry" absolutely — the material (dielectric) also determines capacitance, which the textbook later corrects with `κ`
- **Signed by**: @hpleapfrog · 2026-10-21

### K2 · The effect of inserting a dielectric depends on the circuit condition (no attacks yet)

- **Claim**: inserting a dielectric of relative permittivity `κ` changes the capacitance to `κC₀`; if the capacitor was charged and then **disconnected** (`Q` fixed), the stored energy becomes `1/κ` of its previous value; if the battery **remains connected** (`V` fixed), the stored energy becomes `κ` times its previous value
- **Premises**: `C = κC₀`; `U = Q²/(2C)` and `U = ½CV²`; the textbook's two passages, one saying that for the same charge a dielectric reduces the energy stored and the other saying that adding a dielectric before charging allows more energy to be stored (ev-175)
- **Reasoning**: when disconnected, `Q` is fixed and `U = Q²/(2C)`, so increasing `C` by a factor `κ` makes `U` a factor `1/κ` of its old value; the energy difference is released during insertion as polarization work and mechanical work pulling the dielectric in. When the battery stays connected, `V` is fixed and `U = ½CV²`, so increasing `C` by `κ` increases `U` by `κ`; the battery also supplies extra charge `ΔQ = (κ−1)C₀V`, doing work `VΔQ = 2ΔU`, of which half becomes stored energy and the other half is dissipated or radiated in the charging circuit
- **Evidence**: ev-175
- **Attacked**: the textbook's concept item "how does inserting a dielectric affect the stored energy" and its two true/false items **do not say whether the battery remains connected**, yet the two cases give opposite answers, so as written the question has no unique answer; the textbook discusses the energy accounting only for the disconnected case and does not compute the battery's work when connected; "molecules like tiny springs" is only a qualitative model and cannot give a numerical `κ`
- **Signed by**: @hpleapfrog · 2026-10-21

### K3 · The stored-energy formula gives testable magnitudes (no attacks yet)

- **Claim**: `U_E = ½CV²` gives the correct order of magnitude for a capacitor's stored energy; the textbook's flash example and its 10 µF example can be checked with it
- **Premises**: `U_E = ½CV²`; `Q = CV`; the textbook's three worked examples (ev-175)
- **Reasoning**: for a camera flash with `C = 200 µF` and `V = 100 V`, `U = ½ × 200×10⁻⁶ × (100)² = 1.0 J`; released in `0.001 s`, the power is `P = U/t = 1.0/0.001 = 1 kW`, matching the textbook. For the 10 µF, 120 µC example, `U = Q²/(2C) = (120×10⁻⁶)² / (2 × 10×10⁻⁶) = 7.2×10⁻⁴ J = 0.72 mJ`, whereas the textbook prints `72 mJ`, a factor of 100 too large
- **Evidence**: ev-175
- **Attacked**: `½CV²` assumes the capacitance does not change during operation; real capacitors have equivalent series resistance, leakage, and dielectric loss, so discharge is not ideal; the 1 kW in the flash example is an average power and the instantaneous power is higher; the textbook's order-of-magnitude error in the 10 µF example means it cannot be used to check `U`
- **Signed by**: @hpleapfrog · 2026-10-21

> [!IMPORTANT]
> **The textbook computes the energy of the 10 µF, 120 µC example as `72 mJ`; the correct value is `0.72 mJ`.**
>
> The source reads `U_E = ½CV² = ½(10×10⁻⁶ F)(12 V)² = 72 mJ`. The actual value is `½ × 10⁻⁵ × 144 = 7.2×10⁻⁴ J = 0.72 mJ`, off by a factor of 100. The following sentence, that an ordinary commercial battery can easily supply this much energy, is even more true at `0.72 mJ`, but the number itself must be recorded as `0.72 mJ`.

> [!IMPORTANT]
> **"Does inserting a dielectric increase or decrease the stored energy?" must state the circuit condition.**
>
> The textbook's concept item asks only how inserting a dielectric affects the stored energy, and its two true/false items assert that inserting a dielectric increases the energy and that it reduces the electric field; **none of them says whether the capacitor remains connected to the battery**. The correct conclusions are: with the battery **disconnected** (`Q` fixed), `C` increases, `U = Q²/(2C)` decreases, and `E = Q/(κε₀A) = E₀/κ` decreases; with the battery **still connected** (`V` fixed), `C` increases, `U = ½CV²` increases, and `E = V/d` is unchanged. The textbook's Critical Thinking item discusses only the disconnected case; this entry separates the two cases.

> [!IMPORTANT]
> **The 12 µF attractive-force problem has no correct option.**
>
> The problem gives `C = 12 µF`, `V = 12 V`, and a surface charge density `σ = 7.2 mC/m²` on each plate, and asks for the attractive force of one plate on the other. From `Q = CV = 1.44×10⁻⁴ C` and `A = Q/σ = 0.020 m²`, `d = ε₀A/C ≈ 1.48×10⁻⁸ m` and the field between the plates is `E = σ/ε₀ ≈ 8.1×10⁸ V/m`. The force on one plate is produced only by the field of **the other plate**, `E/2`: `F = QE/2 = Qσ/(2ε₀) ≈ 5.9×10⁴ N`. None of the options `0.81×10⁵`, `0.81×10⁶`, `1.2×10⁵`, or `1.2×10⁶ N` is correct; `1.2×10⁵ N` is exactly the error obtained by dropping the `½` and using the full `E`.

> [!IMPORTANT]
> **Several further errors and mismatches in the textbook are worth noting.**
>
> The definition sentence omits a preposition and reads `can store energy an electric field` (it should be `in an electric field`); one capacitance multiple-choice item labels its options in `nC` rather than `nF` (the correct value is `2.3 nF`); the dielectric table spells `silicone oil` as `Silicon oil`; a teacher note says the prefix `di` means `two or double` and that a dielectric "can have two electric charges", which is wrong both etymologically and physically (`dielectric` comes from the Greek `dia-`, "through", plus `electric`); and the Performance Task at the end of the module is about Newtonian gravitation and Coulomb's law, not capacitors. This entry does not carry these statements over.

## Changelog

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-21 | Entry created; fills in the capacitance part of Compulsory-3 "energy in an electrostatic field", completing item 16 | Written after reading m63179 in full for ev-175 | @hpleapfrog |
