---
title: Beer-Lambert Law and Optical Depth
subject: climate
type: concept
scope: [taught, extra-book, extra-beyond]
by: [argha]
status: draft
tags: [subject/climate, type/concept, taught, extra/book, extra/beyond, src/argha, status/draft]
---
# Beer-Lambert Law and Optical Depth

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** $\mathrm dI=-IKN\sigma\,\mathrm ds\Rightarrow I=I_0e^{-\tau}$ (Argha L5 sl. 56) · 🟡 **extra book:** mass-absorption form, W&H §4.5.1 · 🔵 **extra:** survival-probability reading, $\varepsilon=1-e^{-\tau}$

> [!intuition] In one picture
> A corridor full of people who each catch any ball that comes near: every metre removes the same *fraction* of the balls still flying, so the number left falls exponentially. $\tau$ counts the e-foldings you have crossed.

> [!key] Definition
> The intensity of a monochromatic beam crossing a medium falls as $I_\lambda=I_{\lambda,0}\,e^{-\tau_\lambda}$, where the **optical depth** is the path integral of the extinction coefficient, $\tau_\lambda=\int K_\lambda N\sigma\,\mathrm ds$ ($N$ targets per volume, cross-section $\sigma$, efficiency $K_\lambda$).

| $\tau$ | 0.1 | 0.5 | 1 | 2 | 3 | 5 |
|---|---|---|---|---|---|---|
| transmitted $e^{-\tau}$ | 0.905 | 0.607 | 0.368 | 0.135 | 0.050 | 0.0067 |

- **Slant path:** $\tau=\tau_0\sec\theta$ in a plane-parallel atmosphere; air mass ≈ 38 at the horizon (with curvature and refraction).
- **Mass form:** $\mathrm dI=-I\,\rho\,r\,k\,\mathrm ds$ with $k$ in m² kg⁻¹ and $r$ the mixing ratio (W&H Eq. 4.17); extinction = absorption + scattering; different species add.
- **Mean free path** $=1/N\sigma$; $e^{-\tau}$ is the **survival probability** of a photon (exponential distribution, [[Probability - Course Map]]).
- **Link to emissivity:** for an isothermal layer the absorptivity (= emissivity, Kirchhoff) is $\varepsilon=1-e^{-\tau}$ ($\varepsilon=0.78\Leftrightarrow\tau=1.5$), the parameter of [[One-Layer Greenhouse Model]].
- **Other fields:** light in lakes and canopies, $I(z)=I_0e^{-k_dz}$ (clear vs turbid lakes: [[Bistability and Tipping Points]]).

Derived and illustrated in [[CL07 Optical Properties of the Atmosphere]]; used in [[CL08 Greenhouse Models]]. See [[Rayleigh Scattering]], [[Atmospheric Window]], [[Greenhouse Gases and Absorption Bands]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
