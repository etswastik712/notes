---
title: Blackbody Radiation
subject: thermo
type: concept
scope: [taught, extra-beyond]
by: [argha, suhas-pre]
status: draft
tags: [subject/thermo, type/concept, taught, extra/beyond, src/argha, src/suhas-pre, status/draft]
---
# Blackbody Radiation

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** Planck spectrum, shortwave/longwave (Argha L3) · 🟡 **extra book:** Kirchhoff's law · 🔵 **extra:** cavity radiation, history

> [!intuition] In one picture
> Heat a metal poker: dull red, then orange, then white. The *colour depends only on temperature*, whatever the metal: that universality is the blackbody spectrum.

> [!key] Definition
> A **blackbody** absorbs all incident radiation; in thermal equilibrium at temperature $T$ it emits the universal **Planck spectrum**, which depends only on $T$ (not on material or shape). A real surface emits $\varepsilon\,\sigma T^4$ with emissivity $\varepsilon\le1$ and, by **Kirchhoff's law**, absorptivity $a_\lambda=\varepsilon_\lambda$.

Laws: [[Planck Law]] (spectrum) → [[Wien Displacement Law]] (peak) and [[Stefan-Boltzmann Law]] (total power).

**Cavity radiation.** The field inside an isothermal cavity is a gas of photons with zero chemical potential, in equilibrium with the walls. A small hole radiates the same spectrum.

**History.** Classical equipartition gave the Rayleigh–Jeans law $\propto T/\lambda^4$, diverging at short wavelength (the "ultraviolet catastrophe"); Planck (1900) resolved it by quantising the exchange of energy, $E=h\nu$, the birth of quantum theory.

Climate use: the Sun ($T\approx5772$ K) and Earth (255–288 K) are approximate blackbodies, which separates shortwave from longwave ([[CL03 Radiation and Planetary Energy Balance]]). Planets are *not* perfect: gases are selective absorbers ([[CL07 Optical Properties of the Atmosphere]]).

Connections: [[Quantum Mechanics - Course Map]] · [[Thermodynamics - Course Map]].

## Emission by a layer: Kirchhoff and optical depth
<span class="scope-extra-beyond">extra · beyond</span> *derived in [[CL07 Optical Properties of the Atmosphere]]*

A gas layer of optical depth $\tau$ at temperature $T$ absorbs the fraction $1-e^{-\tau}$ of the radiation incident on it ([[Beer-Lambert Law and Optical Depth]]) and, by **Kirchhoff's law**, emits $(1-e^{-\tau})B(T)$: its emissivity equals its absorptivity, $\varepsilon=1-e^{-\tau}$. The equation of transfer is Schwarzschild's, $\mathrm dI/\mathrm d\tau=-I+B(T)$. This is the bridge from blackbody radiation to the layer models of [[CL08 Greenhouse Models]] (one layer: $T_s=T_e(1-\varepsilon/2)^{-1/4}$): the absorption bands of [[Greenhouse Gases and Absorption Bands]] decide *where* $\varepsilon$ is large.

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
