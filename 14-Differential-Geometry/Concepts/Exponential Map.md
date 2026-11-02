---
title: Exponential Map
aliases: ["exp", "exponential of a Lie algebra", "exp: g to G", "Proposition 20.8", "normal coordinates"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Exponential Map

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG26 via [[mt3184-differential-geometry-and-lie-groups/2026-10-24-october-19-24|Oct 19–24 note]]; HW9 Q3–Q5.
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=537|Lee Prop. 20.8, p. 519]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=539|Lee Prop. 20.9, p. 521]].

> [!intuition] In one picture
> Follow the infinitesimal symmetry $X$ for one unit of time: the dictionary from the Lie algebra to the group.

> [!key] Definition
> $\exp X=\gamma_X(1)$; $\exp sX=\gamma_X(s)$. Smooth; $\exp(s+t)X=\exp sX\exp tX$; $(\exp X)^{-1}=\exp(-X)$; $d\exp_0=\mathrm{id}$ so $\exp$ is a **local diffeomorphism** near $0$; natural: $\Phi\circ\exp=\exp\circ\Phi_*$; flow of $\tilde X$ is $R_{\exp tX}$. $\mathrm{Lie}(H)=\{X:\exp tX\in H\ \forall t\}$.

**Not** additive ($\exp(X+Y)=\exp X\exp Y$ for all $X,Y$ iff $G_0$ abelian), not injective ($\mathbb R\to S^1$), not onto ($\mathfrak{sl}(2,\mathbb R)\to SL(2,\mathbb R)$: $\operatorname{tr}e^A\ge-2$). $[X,Y]=0\iff$ exps commute. $\exp X\exp Y$ as coordinates (HW9 Q3).

Used in: [[DM14 One-Parameter Subgroups and the Exponential Map]], [[DM15 Closed Subgroups and the Lie Correspondence]]. Related: [[One-Parameter Subgroup]] · [[Matrix Exponential]] · [[Lie Algebra of a Lie Group]] · [[Trotter Product Formula]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Spinor]] (Quantum Mechanics): $\exp\big(-\tfrac i2\theta\,\hat n\!\cdot\!\sigma\big)\in SU(2)$ rotates spinors by $\theta$ about $\hat n$, and $\theta=2\pi$ gives $-I$: $SU(2)\to SO(3)$ is $2:1$.
