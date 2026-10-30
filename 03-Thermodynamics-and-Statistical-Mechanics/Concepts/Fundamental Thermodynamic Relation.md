---
title: Fundamental Thermodynamic Relation
aliases: ["dE = T dS + J dx", "combined first and second law"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# Fundamental Thermodynamic Relation

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[1a131e225246d9749a298f49675c5fe5_MIT8_333F13_Lec2.pdf#page=5|MIT L2 eq. I.28]], [[df0c4e121858c0be246b496dd8c39d2c_MIT8_333F13_Lec3.pdf#page=4|L3 eq. I.45]].

> [!intuition] In one picture
> One equation that ties heat, work and state: the master identity from which all thermodynamic relations are derived.

> [!key] Definition
> $\mathrm dE=T\,\mathrm dS+\sum_iJ_i\,\mathrm dx_i+\sum_\alpha\mu_\alpha\,\mathrm dN_\alpha$ (fluid: $T\mathrm dS-P\mathrm dV+\mu\mathrm dN$). Valid between equilibrium states, reversible or not.

## Consequences
$T=(\partial E/\partial S)_x$, $J_i=(\partial E/\partial x_i)_S$, $\mu=(\partial E/\partial N)_{S,x}$; mixed second derivatives give the Maxwell relations; extensivity gives $E=TS+J\!\cdot\!x+\mu N$ and Gibbs-Duhem.

> [!pitfall] Reversible derivation, general result
> It was derived for reversible changes ($\bar\mathrm dQ=T\mathrm dS$, $\bar\mathrm dW=J\mathrm dx$) but connects state functions only, so it holds between any two equilibrium states.

Used in: [[TH04 The Second Law Carnot Engines and Entropy]], [[TH05 Potentials Maxwell Relations Stability and the Third Law]]. Related: [[Entropy]] · [[Legendre Transform]] · [[Maxwell Relations]] · [[Generalised Force and Displacement]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
