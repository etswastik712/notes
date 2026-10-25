---
title: Virtual Temperature
subject: climate
type: concept
scope: [taught, extra-beyond]
by: [suhas-pre]
status: draft
tags: [subject/climate, type/concept, taught, extra/beyond, src/suhas-pre, status/draft]
---
# Virtual Temperature

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** $T_v=T/[1-(e/p)(1-\varepsilon)]$ and its meaning (Suhas pre-midsem; W&H §3.1.1) · 🔵 **extra:** the exact form $T_v=T(1+0.608\,q)$, buoyancy use

> [!intuition] In one picture
> Water vapour molecules (18) replace heavier N₂/O₂ (28–32), so humid air is **lighter** than dry air at the same $p$ and $T$. $T_v$ is the temperature dry air would need to be that light.

> [!key] Definition
> $T_v$ is the temperature that dry air would need to have in order to have the density of the actual moist air at the same pressure, so that $p=\rho R_dT_v$:
> $$T_v=\frac{T}{1-\dfrac ep(1-\varepsilon)}=T(1+0.608\,q),\qquad\varepsilon=\frac{M_w}{M_d}=0.622.$$

- $T_v\ge T$, equal only for dry air. $R_m=R_d(1+0.608\,q)$.
- Saturated tropical air at 30 °C, 1000 hPa: $q=26.8$ g kg⁻¹ ⇒ $T_v-T=4.95$ K, density 1.6 % lower than dry.
- **Buoyancy** depends on $T_v$: a 1 K virtual-temperature excess ⇒ $0.033$ m s⁻². Convection and stability must use $T_v$ ([[Atmospheric Stability]], [[Convection]]).
- It is a bookkeeping device, not a thermometer reading; liquid-water loading is handled by the "density temperature".

Chapters: [[CL05 Thermodynamic State of the Atmosphere]], [[CL06 Hydrostatic Balance and Vertical Structure]]. Related: [[Mixing Ratio and Humidity]], [[Ideal Gas Law]], [[Atmospheric Composition]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
