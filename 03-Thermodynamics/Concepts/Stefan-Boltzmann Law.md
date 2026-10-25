---
title: Stefan-Boltzmann Law
subject: thermo
type: concept
scope: [taught, extra-beyond]
by: [argha, suhas-pre]
status: draft
tags: [subject/thermo, type/concept, taught, extra/beyond, src/argha, src/suhas-pre, status/draft]
---
# Stefan-Boltzmann Law

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** $F=\sigma T^4$ (Argha L3, Suhas) · 🔵 **extra:** derivation of $\sigma$, thermodynamic route

> [!intuition] In one picture
> Heat a body and it glows brighter *and* bluer. Peak height grows as $T^5$ and the width shrinks as $1/T$, so the total (area) grows as $T^4$: doubling $T$ gives 16× the power.

> [!key] Statement
> The total power per unit area emitted by a blackbody is $F=\sigma T^{4}$, with
> $$\sigma=\frac{2\pi^{5}k_B^{4}}{15\,h^{3}c^{2}}=5.670\times10^{-8}\ \mathrm{W\,m^{-2}K^{-4}}.$$

Examples: 316 W m⁻² at 273 K; 390 W m⁻² at 288 K; $6.3\times10^{7}$ W m⁻² at the Sun's surface (5772 K).

> [!extra-beyond]- Extra (beyond): the thermodynamic route
> For isotropic radiation the pressure is $p=u/3$ ($u$ = energy density, $U=uV$). The thermodynamic identity $(\partial U/\partial V)_T=T(\partial p/\partial T)_V-p$ gives $u=\tfrac T3\,\mathrm du/\mathrm dT-\tfrac u3$, i.e. $\mathrm du/u=4\,\mathrm dT/T$ so $u=aT^{4}$ (Boltzmann, 1884). The emitted flux is $F=uc/4=\sigma T^4$ with $\sigma=ac/4$. The Planck integral $\int_0^\infty x^3/(e^x-1)\,\mathrm dx=\pi^4/15$ fixes $a=8\pi^5k_B^4/15h^3c^3$.

Climate: sets the emission term in every energy balance; the $T^4$ dependence gives the stabilising [[Planck Sensitivity]] and the convexity problem of [[Jensen Inequality]]. See [[CL03 Radiation and Planetary Energy Balance]], [[Planck Law]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
