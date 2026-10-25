---
title: Hypsometric Equation
subject: climate
type: concept
scope: [taught, extra-book]
by: [suhas-pre]
status: draft
tags: [subject/climate, type/concept, taught, extra/book, src/suhas-pre, status/draft]
---
# Hypsometric Equation

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** derivation, $\overline{T_v}$, thickness, sea-level reduction, warm- and cold-core lows (Suhas pre-midsem) · 🟡 **extra book:** thickness examples (W&H §3.2.3)

> [!intuition] In one picture
> Warm air is fluffy: heat a column and the same mass stands taller. So the pressure surfaces are farther apart in warm air, and the 500 hPa surface bulges over warm regions.

> [!key] Statement
> Between pressure levels $p_1>p_2$ the geopotential thickness is
> $$Z_2-Z_1=\frac{R_d\overline{T_v}}{g_0}\ln\frac{p_1}{p_2},\qquad\overline{T_v}=\frac{\int T_v\,\mathrm d\ln p}{\ln(p_1/p_2)}.$$

- Derived by integrating $\mathrm d\Phi=-R_dT_v\,\mathrm d\ln p$ with a $\ln p$-weighted mean virtual temperature.
- **1000–500 hPa thickness** $=20.29\,\overline{T_v}$ m: 4910 m at 242 K (polar winter), **5400 m at 266 K** (the rain/snow rule of thumb), 5800 m at 286 K (tropics).
- **Sea-level reduction:** $p_0=p_g\exp(g_0Z_g/R_d\overline{T_v})$; Pune (560 m, 950 hPa, 300 K) ⇒ 1012.6 hPa.
- **Consequences:** warm-core systems weaken with height; thickness gradients produce the thermal wind and the jets ([[CL14 Observed Winds - Jets, Trades and the ITCZ]]).

Chapter: [[CL06 Hydrostatic Balance and Vertical Structure]]. Related: [[Geopotential]], [[Scale Height]], [[Virtual Temperature]], [[Standard Atmosphere]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
