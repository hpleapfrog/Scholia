---
id: kb:physics:damped-and-forced-oscillation
type: 知识点
title: "Damped and forced oscillation"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know the phase and energy of simple harmonic motion and need to distinguish underdamped, critically damped, and overdamped motion and to explain natural frequency and resonance
  条件: covers the three damping regimes, forced oscillation, natural frequency, and resonance only; the damping differential equation, the exponential time constant, the quality factor, and the resonance-curve formula are not built
edges:
  先修: ["[Phase and energy of simple harmonic motion](phase-and-energy-of-shm.en.md)"]
  支持: []
  攻击: []
evidence: [ev-191]
license: CC-BY-SA-4.0
---

> **English version of [`阻尼振动与受迫振动.md`](阻尼振动与受迫振动.md).**

> [!TIP]
> **After reading this entry you should** be able to say why damping reduces the amplitude, distinguish underdamped, critically damped, and overdamped motion, explain why a forced oscillation has its largest amplitude when the driving frequency equals the natural frequency, and say how the amount of damping changes the height and width of the resonance peak

## Definition

**Damped oscillation** is oscillation with a non-conservative force (friction, viscous drag, and so on). The textbook describes it with the work–energy relation (ev-191):

`W_nc = Δ(KE + PE)`

For damping, `W_nc < 0`: mechanical energy decreases, becomes thermal energy, and the **amplitude gradually decreases**. For small damping the period and frequency are nearly the same as without damping; only when damping becomes appreciable do the period and frequency change noticeably.

The textbook distinguishes three cases by how the system returns to equilibrium:

- **underdamped**: the object crosses equilibrium once or more, with the amplitude decreasing
- **critically damped**: the object returns to equilibrium as quickly as possible
- **overdamped**: the object does not oscillate and returns more slowly than the critically damped case

The textbook uses critical damping for car suspensions and needle scales: the needle or the car body should settle quickly without swinging back and forth.

**Forced oscillation** is oscillation under a periodic driving force. The textbook's paddle ball illustrates it: when the finger moves up and down slowly, the ball follows; as the driving frequency approaches the ball's natural frequency the amplitude grows, and at the natural frequency it is largest; above that frequency the amplitude falls again. A steady forced oscillation runs at the driving frequency — the textbook conveys this with the ball following the finger but does not write the sentence out (see the callout below).

The **natural frequency** `f0` is the frequency at which the system would oscillate with no driving and no damping (textbook definition). **Resonance** is driving at the natural frequency (textbook definition); the textbook writes `The phenomenon of driving a system with a frequency equal to its natural frequency is called resonance.`

Damping changes the shape of the resonance curve: less damping gives a higher and narrower peak; more damping gives a lower and broader response (the textbook's figure caption and Section Summary). The textbook's examples include piano strings, a swing, radio tuning, MRI (about `100 MHz`), the Tacoma Narrows Bridge (1940), the London Millennium Bridge, car suspensions, and corrugated roads. When the driving force does work that replaces the energy dissipated by damping, a forced oscillation can keep a constant amplitude — the textbook's AP answer states this.

Recomputed here:

- friction example: `m = 0.200 kg`, `μ_k = 0.0800`, `X = 0.100 m`, `k = 50.0 N/m`, textbook `f = 0.157 N`, `d = 1.59 m`. Recompute `f = μ_k mg = 0.1568 N`, `d = k/(2f)(X² − (f/k)²) = 1.593 m`
- textbook exercise: the amplitude falls by `3.0%` per cycle, so the mechanical energy falls by `1 − 0.97² ≈ 5.9%` (no answer given; recomputed here)
- shock-absorber exercise: `m = 1200 kg`, `v = 0.800 m/s`, must dissipate `½mv² = 384 J` (agrees with the textbook answer)
- bridge exercise: `k = 1.00×10⁸ N/m`, `X = 0.100 m`, stored energy `½kX² = 5.00×10⁵ J`; growing from `0.100 m` to `0.500 m` needs `½k(0.500² − 0.100²) = 1.20×10⁷ J`, which at `1.00×10⁴ J/s` takes `1.20×10³ s` (agrees with the textbook answer)
- suspension exercise: `k = 5.00×10⁴ N/m`, `X = 0.0750 m`, stored energy `½kX² = 141 J` (no answer given; recomputed here)

> [!IMPORTANT]
> **The textbook states critical damping in two contradictory ways.**
>
> The body writes `The critically damped system may overshoot the equilibrium position, but if it does, it will do so only once.`
> The figure caption and glossary in the same module say `without overshooting` / `without oscillating back and forth`.
> This entry follows the caption and glossary ("does not overshoot") and records the body's "may overshoot once" as an internal contradiction.

> [!IMPORTANT]
> **"A steady forced oscillation runs at the driving frequency" is a library completion.**
>
> The textbook says only that the ball follows the finger and that the amplitude grows near the natural frequency; it does not write that the steady forced oscillation has the driving frequency.
> This entry marks that sentence as a completion; the textbook gives no forced-oscillation equation, amplitude–frequency formula, phase lag, or quality factor.

> [!NOTE]
> **Four problems in the source.**
>
> 1. The body says `With less-than critical damping, the system will return to equilibrium faster`, which conflicts with the definition of critical damping as the fastest return: an underdamped system may cross equilibrium sooner, but its envelope decays more slowly and it does not settle sooner.
> 2. The AP exercise gives `d = 1.698 m`; the textbook's own formula with the stated `k = 50 N/m`, `μ_k = 0.06`, `m = 0.5 kg`, `X = 0.2 m`, `f = 0.294 N` gives `3.40 m`, about twice the printed answer. This entry does not use `1.698 m`.
> 3. The Tacoma Narrows Bridge is presented as a case of wind driving the bridge at its resonant frequency; this library has not read the primary engineering investigation and does not treat the cause as established.
> 4. The textbook defines resonance as driving exactly at the natural frequency and says all three resonance curves peak there; it gives no amplitude formula, so whether and how far the peak moves with damping cannot be decided from the material examined — recorded as a gap.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Phase and energy of simple harmonic motion](phase-and-energy-of-shm.en.md) — damping starts from "mechanical energy is no longer conserved"; the energy equation and `v(x)` are the baseline here |
| Related | [Simple harmonic motion](simple-harmonic-motion.en.md) — undamped simple harmonic motion is the limit of the three damping regimes as damping goes to zero; `F = −kx` and `T = 2π√(m/k)` remain the undamped baseline |
| Related | [Simple pendulum](simple-pendulum.en.md) — a swing is a forced-oscillation example; the pendulum entry covers only small-angle motion without damping |
| Recorded gap | **The damping differential equation and exponential time constant**, **the quality factor `Q`**, **the quantitative resonance curve and its half-width**, and **the primary engineering report on the Tacoma Narrows Bridge** are not built in this repo; the textbook gives only qualitative descriptions and graphs |

## Argument

### K1 · Damping turns mechanical energy into heat, and the three regimes are distinguished by how the system returns to equilibrium

- **Claim**: a non-conservative damping force does negative work, so mechanical energy and amplitude decrease; for small damping the period is nearly unchanged; underdamped motion crosses equilibrium, critically damped motion returns fastest, and overdamped motion does not oscillate and is slower
- **Premise**: the textbook gives `W_nc = Δ(KE + PE)` with `W_nc < 0` for damping, defines the three regimes, and gives the car-suspension and needle-scale applications (ev-191)
- **Reasoning**: `W_nc < 0` ⇒ `KE + PE` falls ⇒ the amplitude falls; when damping reaches the critical value, the restoring force brings the object back as quickly as possible without reaching the other side; with more damping the return is slower; with less damping the restoring force carries the object across equilibrium, but every crossing loses energy. For small damping the period is set by the restoring force and the mass, and damping only slowly removes energy, so the period hardly changes
- **Evidence**: ev-191
- **Attacked**: the textbook states critical damping in two contradictory ways (body "may overshoot once" against caption and glossary "without overshooting"); the body says underdamped motion returns faster, conflicting with the definition of critical damping as the fastest return; there is no damping equation, no exponential envelope, and no criterion separating the three regimes
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · A forced oscillation resonates when the driving frequency equals the natural frequency, and less damping gives a higher, narrower peak

- **Claim**: a periodic driving force makes the system oscillate at the driving frequency; as the driving frequency approaches the natural frequency `f0` the amplitude grows, and at `f0` the system resonates; less damping gives a higher and narrower peak, more damping a lower and broader response
- **Premise**: the textbook's paddle-ball, piano-string, swing, radio, and MRI examples, its definitions of natural frequency and resonance, and its account of how damping changes the resonance curve (ev-191)
- **Reasoning**: the driving force does work every cycle; when its frequency matches the system's natural frequency, the energy input accumulates most effectively in step with the motion and the amplitude is largest; damping removes energy, so with less damping more energy accumulates near resonance and the peak is sharper; away from resonance the driving force is out of step with the motion, the input is less efficient, and the amplitude is smaller
- **Evidence**: ev-191
- **Attacked**: the textbook gives no forced-oscillation equation, amplitude–frequency formula, phase lag, or quality factor; it does not write out that a steady forced oscillation runs at the driving frequency; "accumulates in step" is this library's reading of the textbook's qualitative graph, not a textbook sentence; the position and height of the resonance peak with damping cannot be judged quantitatively from the material examined
- **Attribution**: @hpleapfrog · 2026-10-21

### K3 · Resonance can be used or must be prevented; the textbook's bridge examples include an unverified causal account

- **Claim**: resonance can be used for frequency selection and energy input (radio, MRI, a swing) and must be avoided when it produces harmful amplitudes (car suspensions, bridges, soldiers breaking step); the textbook uses the Tacoma Narrows and Millennium bridges as warnings, but this library could not verify the claim that wind drove the Tacoma Narrows Bridge at its resonant frequency
- **Premise**: the textbook's engineering examples and its account of the 1940 Tacoma Narrows Bridge and the London Millennium Bridge (ev-191)
- **Reasoning**: if the driving frequency can be tuned, designing the system to stay away from resonance in its operating band, or increasing damping to lower and broaden the peak, limits the amplitude; conversely, a frequency-selective device wants little damping and a sharp response. The textbook's bridge examples show the consequence of uncontrolled amplitude but give no design criterion
- **Evidence**: ev-191
- **Attacked**: the textbook gives no safety factor, damping ratio, or design standard; the cause of the Tacoma Narrows failure can be judged only from the primary engineering investigation, which this library has not read, so the textbook's causal account is not treated as established; the Millennium Bridge gets only one sentence
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; closes the damping, forced-oscillation, and resonance gaps recorded in "Simple harmonic motion" and "Simple pendulum", attached after "Phase and energy of simple harmonic motion" | written after reading m42246/m42247 in full (ev-191); critical damping is used in the "does not overshoot" sense, and the body's contradiction, the underdamped "faster" error, and the factor-of-two AP answer are recorded | @hpleapfrog |
