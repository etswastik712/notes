---
title: Response Functions
aliases: ["response coefficients", "compressibility", "expansivity"]
subject: thermo
type: concept
scope: [taught, extra-book]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, extra/book, src/lecture-notes, status/draft]
---
# Response Functions

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[0d0ec730e8e02ed0399d39ff05054a72_MIT8_333F13_Lec1.pdf#page=5|MIT L1 §I.C]]. · 🟡 **extra · book:** $\beta$, $\kappa_T$ (Zemansky Ch. 2).

> [!intuition] In one picture
> How much a coordinate moves when you poke the system: the measurable derivatives of the equation of state.

> [!key] Definition
> Heat capacities $C_V=(\partial E/\partial T)_V$, $C_P=(\partial H/\partial T)_P$; force constants $\kappa_T=-V^{-1}(\partial V/\partial P)_T$, $\chi_T=V^{-1}(\partial M/\partial B)_T$; thermal responses $\alpha_P=V^{-1}(\partial V/\partial T)_P$.

## Relations and numbers
Ideal gas: $\kappa_T=1/P$, $\alpha_P=1/T$. General: $(\partial P/\partial T)_V=\alpha_P/\kappa_T$ (water at 20 °C: $4.5$ bar K$^{-1}$) and $C_P-C_V=TV\alpha_P^2/\kappa_T\ge0$ (water: $0.49$ J mol$^{-1}$K$^{-1}$). Stability demands $C_V\ge0$, $\kappa_T\ge0$.

> [!pitfall] Signs
> $\kappa_T$ is positive by stability; a negative value signals an unstable (spinodal) state, not a response.

Used in: [[TH01 Temperature and the Zeroth Law]], [[TH02 Work Heat and the First Law]], [[TH05 Potentials Maxwell Relations Stability and the Third Law]]. Related: [[Heat Capacity]] · [[Equation of State]] · [[Thermodynamic Stability]] · [[Mayer Relation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
