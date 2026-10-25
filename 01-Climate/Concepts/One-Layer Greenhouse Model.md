---
title: One-Layer Greenhouse Model
subject: climate
type: concept
scope: [taught, extra-book, extra-beyond]
by: [argha, suhas-pre]
status: draft
tags: [subject/climate, type/concept, taught, extra/book, extra/beyond, src/argha, src/suhas-pre, status/draft]
---
# One-Layer Greenhouse Model

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** $\varepsilon=1$ (Argha L6 sl. 67) and $\varepsilon<1$ (sl. 65–66), Suhas Models 1–2 · 🟡 **extra book:** W&H Exercise 4.8 · 🔵 **extra:** the greenhouse flux $G$, $\Delta\varepsilon$ for CO₂

> [!intuition] In one picture
> A ceiling above a heated floor: it intercepts the floor's infrared and returns half to the floor, so the floor must run hotter to push the same power out. A leaky ceiling lets a fraction $1-\varepsilon$ straight through.

> [!key] Result
> One isothermal layer, transparent to shortwave, longwave absorptivity = emissivity $\varepsilon$. Balances (top, surface, layer): $Q=\varepsilon\sigma T_a^4+(1-\varepsilon)\sigma T_s^4$, $Q+\varepsilon\sigma T_a^4=\sigma T_s^4$, $2\varepsilon\sigma T_a^4=\varepsilon\sigma T_s^4$ with $Q=S(1-\alpha)/4=238$ W m⁻². Then
> $$T_a=2^{-1/4}T_s,\qquad T_s=\frac{T_e}{(1-\varepsilon/2)^{1/4}},\qquad\mathrm{OLR}=\sigma T_s^4\,(1-\varepsilon/2).$$

- **Limits:** $\varepsilon=0$: $T_s=T_e=254.6$ K; $\varepsilon=1$: $T_s=2^{1/4}T_e=302.8$ K (+48 K, too warm).
- **Earth:** $\varepsilon=0.78$ gives 288 K, $T_a=242$ K, $\varepsilon_{\rm eff}=1-\varepsilon/2=0.61$ (the 0.6 of [[CL04 Feedback and Multiple Steady States]]); greenhouse flux $G=\sigma T_s^4\varepsilon/2=152$ W m⁻²; leak $1-\varepsilon=0.22$. Mars $\varepsilon=0.15$; Venus would need 1.98 (> 1: impossible).
- **CO₂ doubling:** forcing 3.7 W m⁻² $\Leftrightarrow\Delta\varepsilon=0.019$; no-feedback $\Delta T=1.1$ K.
- **Limits of the model:** no convection, no clouds, back-radiation only 152 (not 340) W m⁻².

Derived in [[CL08 Greenhouse Models]]; absorptivity from optical depth: [[Beer-Lambert Law and Optical Depth]]. See [[Multi-Layer Greenhouse Model]], [[Greenhouse Effect]], [[Planck Sensitivity]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
