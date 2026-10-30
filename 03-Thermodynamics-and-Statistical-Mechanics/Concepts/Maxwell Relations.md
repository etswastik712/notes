---
title: Maxwell Relations
aliases: ["Maxwell relation"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# Maxwell Relations

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[df0c4e121858c0be246b496dd8c39d2c_MIT8_333F13_Lec3.pdf#page=5|MIT L3 eqs. I.52–I.59]].

> [!intuition] In one picture
> Mixed second derivatives of a potential do not depend on order: a relation for free.

> [!key] Definition
> $-(\partial S/\partial x)_T=(\partial J/\partial T)_x$ (from $F$); $(\partial S/\partial J)_T=(\partial x/\partial T)_J$ (from $G$); $(\partial T/\partial x)_S=(\partial J/\partial S)_x$ (from $E$). Fluid: $(\partial S/\partial V)_T=(\partial P/\partial T)_V$, $(\partial S/\partial P)_T=-(\partial V/\partial T)_P$.

## Uses
$(\partial E/\partial V)_T=T(\partial P/\partial T)_V-P$ ($0$ for ideal gas, $a/V^2$ for van der Waals); $C_P-C_V=TV\alpha^2/\kappa_T$; $\alpha_J\to0$ at $T\to0$ via the third law.

> [!pitfall] Pick the right potential
> A potential whose natural variables don't include the two held fixed gives nothing; remember $\mathrm dE=T\mathrm dS+J\mathrm dx$ and manipulate it (the lecture's advice).

Used in: [[TH05 Potentials Maxwell Relations Stability and the Third Law]]. Related: [[Helmholtz Free Energy]] · [[Gibbs Free Energy]] · [[Response Functions]] · [[Joule Expansion]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
