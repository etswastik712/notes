---
title: Legendre Transform
aliases: ["Legendre transformation", "change of natural variables"]
subject: thermo
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, src/lecture-notes, status/draft]
---
# Legendre Transform

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[df0c4e121858c0be246b496dd8c39d2c_MIT8_333F13_Lec3.pdf#page=3|MIT L3 (after Table 2)]].

> [!intuition] In one picture
> Swap a variable for its slope, keeping all the information: a way to choose the energy appropriate to what you hold fixed.

> [!key] Definition
> From $E(S,x,N)$ subtract the product of a variable with its conjugate: $H=E-J\!\cdot\!x$, $F=E-TS$, $G=E-TS-J\!\cdot\!x$, $\tilde G=E-TS-\mu N$; each has its own natural variables and differential.

## Pattern
Remove $S$ for $T$ (subtract $TS$); remove $x$ for $J$ (subtract $J\!\cdot\!x$); remove $N$ for $\mu$. Inequalities: $\delta S\ge0$, $\delta H\le0$, $\delta F\le0$, $\delta G\le0$ under the matching constraints.

> [!pitfall] Not just notation
> The potential is useful only in its natural variables: $H(S,J)$, $F(T,x)$, $G(T,J)$; $G(S,x)$ would lose the Maxwell structure.

Used in: [[TH05 Potentials Maxwell Relations Stability and the Third Law]]. Related: [[Enthalpy]] · [[Helmholtz Free Energy]] · [[Gibbs Free Energy]] · [[Grand Potential]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Continued in Part II (added 2026-10-30)
- Two statistical-mechanics appearances: the rate function $I(s)=\sup_t[ts-K(t)]$ ([[Large Deviation Principle]], [[SM01 Probability Large Numbers and Information]] §6.2) and $F=\min_E(E-TS)$ ([[Equivalence of Ensembles]], [[SM03 The Canonical Ensemble]] §3.1).
