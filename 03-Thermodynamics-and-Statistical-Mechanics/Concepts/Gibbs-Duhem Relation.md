---
title: Gibbs-Duhem Relation
aliases: ["Gibbs–Duhem"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# Gibbs-Duhem Relation

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[df0c4e121858c0be246b496dd8c39d2c_MIT8_333F13_Lec3.pdf#page=5|MIT L3 eq. I.49]].

> [!intuition] In one picture
> Intensive variables cannot all be varied independently.

> [!key] Definition
> Extensivity gives $E=TS+J\!\cdot\!x+\mu\!\cdot\!N$; varying it and comparing with $\mathrm dE$: $S\,\mathrm dT+x\!\cdot\!\mathrm dJ+N\!\cdot\!\mathrm d\mu=0$.

## Use
Ideal gas at fixed $T,N$: $-V\mathrm dP+N\mathrm d\mu=0\Rightarrow\mathrm d\mu=k_BT\,\mathrm dP/P$. Per mass: $\mathrm d\mu=-s\,\mathrm dT+v\,\mathrm dP$, used to derive Clausius–Clapeyron.

> [!pitfall] Needs homogeneity
> It follows from $E(\lambda S,\lambda x,\lambda N)=\lambda E$, which fails for systems with surfaces or long-range forces.

Used in: [[TH05 Potentials Maxwell Relations Stability and the Third Law]]. Related: [[Chemical Potential]] · [[Fundamental Thermodynamic Relation]] · [[Gibbs Free Energy]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
