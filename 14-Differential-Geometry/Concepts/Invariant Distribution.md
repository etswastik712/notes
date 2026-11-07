---
title: Invariant Distribution
aliases: ["Phi-invariant distribution", "Phi-invariant foliation", "Proposition 19.23"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Invariant Distribution

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG30 via the [[mt3184-differential-geometry-and-lie-groups/2026-11-06-november-2-6|Nov 2–6 note (DG29–30)]]; HW10 Q3.
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=523|Lee Prop 19.23, p. 505]].

> [!intuition] In one picture
> A symmetry preserves the plane field exactly when it maps leaves onto leaves.

> [!key] Definition
> For a diffeomorphism $\Phi$: $D$ is **$\Phi$-invariant** if $d\Phi_p(D_p)=D_{\Phi(p)}$; a foliation is $\Phi$-invariant if $\Phi(L)$ is a leaf for every leaf $L$. For involutive $D$ with induced $\mathcal F$: **$D$ is $\Phi$-invariant iff $\mathcal F$ is** (⇒ $\Phi(L)$ is an integral manifold, maximal by applying $\Phi^{-1}$; ⇐ compare tangent spaces of $\Phi(L)$).

Horizontal-line foliation of $\mathbb R^2$: invariant under $(x,y)\mapsto(2x,y+1)$ and the shear $(x+y,y)$, not under the swap $(y,x)$. Left-invariant $D$: $L_g$ permutes leaves.

Used in: [[DM17 Foliations, Weakly Embedded Submanifolds and Lie Subgroups]]. Related: [[Foliation]] · [[Global Frobenius Theorem]] · [[Left-Invariant Distribution of a Subalgebra]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
