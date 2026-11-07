---
title: Frobenius Theorem
aliases: ["involutive distribution", "integrable distribution", "integral manifold", "Theorem 19.12", "foliation", "flat chart"]
subject: diff-geometry
type: concept
scope: [extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, src/lecture-notes, src/book, status/draft]
---
# Frobenius Theorem

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=515|Lee Thm 19.12, p. 497]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=524|Lee Thms 19.25–19.26, p. 506]].

> [!intuition] In one picture
> A field of planes is tangent to a family of surfaces exactly when the bracket of two fields in the planes stays in the planes.

> [!key] Definition
> A rank-$k$ distribution $D\subseteq TM$ is **involutive** if $[X,Y]\in\Gamma(D)$ for $X,Y\in\Gamma(D)$; **Frobenius:** involutive $\iff$ integrable $\iff$ locally $D=\mathrm{span}\{\partial_1,\dots,\partial_k\}$ in a flat chart. Necessity: Cor 8.32; sufficiency: involutive $\Rightarrow$ locally spanned by independent commuting fields (Thm 9.46).

$\mathrm{span}\{\partial_x,\partial_y\}$ is involutive (planes $z=$ const); $\mathrm{span}\{\partial_x,\partial_y+x\partial_z\}$ has $[X_1,X_2]=\partial_z\notin D$ (contact). Application: a Lie subalgebra $\mathfrak h\le\mathfrak g$ gives a left-invariant involutive distribution whose leaf through $e$ is the connected Lie subgroup with algebra $\mathfrak h$ (Thm 19.26).

Used in: [[DM15 Closed Subgroups and the Lie Correspondence]]. Related: [[Commuting Frame]] · [[Lie Bracket of Vector Fields]] · [[Lie Subgroup]] · [[Lie Correspondence]].

**Continued (2026-11-07):** now taught (slides DG29–DG30): the full treatment with the proof is [[DM16 Distributions, Involutivity and the Frobenius Theorem]] (local theorem, flat charts, forms) and [[DM17 Foliations, Weakly Embedded Submanifolds and Lie Subgroups]] (global theorem, foliations, Lie subgroups). Concept notes: [[Distribution]] · [[Integral Manifold]] · [[Involutive Distribution]] · [[Flat Chart for a Distribution]] · [[Global Frobenius Theorem]] · [[Foliation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
