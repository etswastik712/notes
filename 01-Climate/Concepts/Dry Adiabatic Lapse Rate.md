---
title: Dry Adiabatic Lapse Rate
subject: climate
type: concept
scope: [taught, extra-book]
by: [suhas-pre, book]
status: draft
tags: [subject/climate, type/concept, taught, extra/book, src/suhas-pre, src/book, status/draft]
---
# Dry Adiabatic Lapse Rate

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!key] Definition
> The **dry adiabatic lapse rate** is the rate at which an unsaturated air parcel cools as it rises without exchanging heat:
> $$\Gamma_d=-\Big(\frac{\mathrm dT}{\mathrm dz}\Big)_{\rm parcel}=\frac{g}{c_p}=\frac{9.81}{1004}=9.8\ \mathrm{K\,km^{-1}}.$$

- **Taught as a reference value** (Suhas pre-midsem notes: "used, not derived"): a layer whose environmental lapse rate exceeds $\Gamma_d$ is statically unstable and convects ([[CL09 Radiative-Convective Equilibrium]], §2.1).
- **Derivation** (W&H §3.4.2): $\mathrm dq=0$, $c_p\,\mathrm dT=\alpha\,\mathrm dp$ and $\mathrm dp=-\rho g\,\mathrm dz$ give $c_p\,\mathrm dT=-g\,\mathrm dz$ ([[First Law of Thermodynamics]]). Equivalent: dry static energy $c_pT+gz$ is conserved.
- Constant (independent of $T$ and $p$), unlike the saturated lapse rate $\Gamma_s$ (4–9 K km⁻¹).
- Other planets: $\Gamma_d=g/c_p$ with their own $g$ and $c_p$.

> [!intuition] Climbing costs heat
> Lifting 1 kg by 1 km costs $g\times1000\approx9.8$ kJ of potential energy; the parcel pays it from internal energy, cooling by $9.8\ \mathrm{kJ}/c_p\approx9.8$ K.

Compare with the observed mean tropospheric $\Gamma\approx6.5$ K km⁻¹ ([[Lapse Rate]]); the difference decides stability ([[Atmospheric Stability]]). See also [[Adiabatic Process and Potential Temperature]], [[Convective Adjustment]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
