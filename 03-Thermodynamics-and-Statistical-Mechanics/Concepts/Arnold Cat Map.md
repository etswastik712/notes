---
title: Arnold Cat Map
aliases: ["cat map", "mixing toy model", "hyperbolic toral automorphism"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Arnold Cat Map

> [!info] Source
> Arnold and Avez (1968), recalled; simulated in [[SM02 Phase Space Liouville and the Microcanonical Ensemble]] §3.1.

> [!intuition] In one picture
> The simplest area-preserving map that stretches in one direction and squeezes in the other: an exactly solvable model of mixing and of coarse-grained entropy growth.

> [!key] Key facts
> $(x,y)\mapsto(2x+y,\,x+y)\bmod1$; $\det=1$; eigenvalues $(3\pm\sqrt5)/2$; Lyapunov exponent $\lambda=\ln\frac{3+\sqrt5}2=0.9624$; mixing, ergodic, periodic orbits dense. Coarse-grained entropy grows at rate $\lambda$ until saturation at $\ln(\text{cells})$.

> [!example] Coarse-graining (recomputed)
> $0.05\times0.05$ square, 40×40 cells: $S_{cg}=1.386,\ 2.186,\ 2.963,\ 3.885,\ 4.838,\ 5.799,\ 6.753,\ 7.337$ for $t=0\ldots7$ (saturation $\ln1600=7.378$); fine-grained entropy constant.

Used in: [[SM02 Phase Space Liouville and the Microcanonical Ensemble]]. Related: [[Liouville's Theorem]] · [[Ergodic Hypothesis]] · [[H-Theorem]] · [[Poincare Recurrence]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
