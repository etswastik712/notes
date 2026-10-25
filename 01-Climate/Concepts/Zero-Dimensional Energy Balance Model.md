---
title: Zero-Dimensional Energy Balance Model
subject: climate
type: concept
scope: [taught]
by: [argha, suhas-pre]
status: draft
tags: [subject/climate, type/concept, taught, src/argha, src/suhas-pre, status/draft]
---
# Zero-Dimensional Energy Balance Model

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the whole model (Argha L3–L4) · 🔵 **extra:** heat-capacity/time-scale form

> [!intuition] In one picture
> A one-number planet: keep only 'sunlight in' and 'heat out' and ignore *where* things happen. Like judging a house's temperature from the heater and the insulation alone, without knowing the room layout.

> [!key] The model
> Treat the planet as one point with temperature $T$ and heat capacity $C$:
> $$C\frac{\mathrm dT}{\mathrm dt}=\underbrace{\tfrac14S\,[1-\alpha(T)]}_{\text{absorbed shortwave}}-\underbrace{\varepsilon\,\sigma T^4}_{\text{emitted longwave}}+F .$$

- **Assumptions:** global and time average, horizontal transport only redistributes heat, geothermal heat negligible, single temperature for the emitting surface.
- **Steady state** ($\mathrm dT/\mathrm dt=0$): with constant $\alpha$ and $\varepsilon=1$ it gives $T_e=255$ K.
- **Sensitivity** to forcing: [[Planck Sensitivity]] $\Lambda_P=1/4\sigma T^3$; with $T$-dependent $\alpha$ it gives feedbacks, multiple steady states and hysteresis ([[CL04 Feedback and Multiple Steady States]]).
- **Time scale:** $\tau=C/(4\sigma T^3)$ ([[Relaxation Time]]).
- **Limits:** no latitude (poleward transport: [[CL10 Global Energy Balance and Meridional Structure]]); no vertical structure (greenhouse: [[CL08 Greenhouse Models]]); $\langle T^4\rangle\ne\langle T\rangle^4$ ([[Jensen Inequality]]).

Climate-model hierarchy: this is the bottom rung; one-dimensional (latitude) energy-balance models of Budyko and Sellers sit above it, then radiative-convective models, then general circulation models.

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
