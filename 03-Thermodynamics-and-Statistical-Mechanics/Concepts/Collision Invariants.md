---
title: Collision Invariants
aliases: ["summational invariants", "conserved quantities of a collision"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Collision Invariants

> [!info] Source
> Kardar §3.5, §3.7 (pp. 72, 78–82); [[SM04 Kinetic Theory and the Boltzmann Equation]] §5.

> [!intuition] In one picture
> Whatever a collision conserves, the collision integral cannot change in total: $1$, $\mathbf p$ and the energy.

> [!key] Key facts
> $\chi$ with $\chi_1+\chi_2=\chi_1'+\chi_2'$ in every collision; $\int\mathrm d^3p\,\chi\,C[f]=\tfrac14\int w\,[\chi_1+\chi_2-\chi_1'-\chi_2'][f_1'f_2'-f_1f_2]$. Exactly five: $1$, $p_x,p_y,p_z$, $p^2/2m$. Taking moments of the Boltzmann equation gives continuity, momentum and energy balance (exact, not closed).

> [!example] Balance laws
> $D_tn=-n\nabla\cdot\mathbf u$; $mn\,D_t\mathbf u=-\nabla\cdot P+n\mathbf F$; $\tfrac32nk_B\,D_tT=-\nabla\cdot\mathbf h-P_{\alpha\beta}\partial_\alpha u_\beta$. If $\ln f$ is a collision invariant then the collision term vanishes identically: Maxwell.

Used in: [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[Boltzmann Equation]] · [[H-Theorem]] · [[Euler Equations]] · [[Navier-Stokes Equations]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
