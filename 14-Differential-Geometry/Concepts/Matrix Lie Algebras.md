---
title: Matrix Lie Algebras
aliases: ["so(n)", "sl(n)", "su(n)", "u(n)", "so(3) and the cross product", "su(2)"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Matrix Lie Algebras

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slides DG19–DG20 via [[mt3184-differential-geometry-and-lie-groups/2026-10-10-october-5-9|Oct 5–9 note]]; HW5 Q3, HW7 Q3.
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=215|Lee Ex. 8.47, p. 197]].

> [!intuition] In one picture
> Lie algebras of the classical groups: the matrices $A$ with $I+tA$ preserving the defining condition to first order.

> [!key] Definition
> $\mathfrak{sl}(n)=\ker\operatorname{tr}$ ($n^2-1$), $\mathfrak{so}(n)=\{A+A^T=0\}$ ($n(n-1)/2$), $\mathfrak u(n)=\{A+A^*=0\}$ ($n^2$), $\mathfrak{su}(n)$ ($n^2-1$), all with the commutator. $\mathfrak{so}(3)\cong(\mathbb R^3,\times)$ via $\hat\omega v=\omega\times v$: $[\hat\omega,\hat\eta]=\widehat{\omega\times\eta}$; $\mathfrak{su}(2)$ has basis $\tau_k=-\tfrac i2\sigma_k$ with $[\tau_1,\tau_2]=\tau_3$.

Computed as kernels of $d\det_I=\operatorname{tr}$, $B\mapsto B+B^T$, $B\mapsto B+B^*$ (dimensions checked numerically for $n=2,3,4$). Physics: angular momentum $[L_j,L_k]=i\hbar\epsilon_{jkl}L_l$ and spin $S_k=\tfrac\hbar2\sigma_k$ ([[QM09 The Stern-Gerlach Experiment and Spin]]).

Used in: [[DM11 The Lie Algebra of a Lie Group]]. Related: [[Lie Algebra of a Lie Group]] · [[Special Linear Group]] · [[Orthogonal Group]] · [[Unitary Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
