---
title: Helmholtz Free Energy
aliases: ["Helmholtz energy", "F = E - TS"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# Helmholtz Free Energy

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[df0c4e121858c0be246b496dd8c39d2c_MIT8_333F13_Lec3.pdf#page=2|MIT L3 eqs. I.34–I.37]].

> [!intuition] In one picture
> The energy available for work at constant temperature after you pay the entropy toll $TS$.

> [!key] Definition
> $F=E-TS$; $\mathrm dF=-S\,\mathrm dT+J\!\cdot\!\mathrm dx$; $\delta F\le0$ at constant $T$ with no work; $J_i=(\partial F/\partial x_i)_T$, $S=-(\partial F/\partial T)_x$, $E=-T^2\partial_T(F/T)$. Statistical: $F=-k_BT\ln Z$.

## Use
Maxwell relation $-(\partial S/\partial x)_T=(\partial J/\partial T)_x$ comes from it. Fluid: $-(\partial F/\partial V)_T=P$ (checked for the ideal gas).

> [!pitfall] Constant volume, not constant pressure
> At fixed $T$ **and** $P$ the minimised potential is $G$, not $F$.

Used in: [[TH05 Potentials Maxwell Relations Stability and the Third Law]], [[TH06 From Kinetic Theory to Statistical Mechanics]]. Related: [[Legendre Transform]] · [[Partition Function]] · [[Gibbs Free Energy]] · [[Maxwell Relations]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
