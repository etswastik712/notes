---
title: Left Translation
aliases: ["right translation", "conjugation", "L_g", "R_g", "c_g"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Left Translation

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG10; [[mt3184-differential-geometry-and-lie-groups/2026-08-27-august-24-28|Aug 24–28 note]].

> [!intuition] In one picture
> Shift the whole group by multiplying by a fixed element: a diffeomorphism that carries the identity to any chosen point.

> [!key] Definition
> $L_g(h)=gh$, $R_g(h)=hg$, $c_g(h)=ghg^{-1}$ are diffeomorphisms of $G$ ($L_g^{-1}=L_{g^{-1}}$). Hence $d(L_g)_e:T_eG\to T_gG$ is an isomorphism and the geometry near $g$ equals that near $e$.

A vector $v\in T_eG$ defines the left-invariant field $X_g=d(L_g)_e(v)$ ([[DM11 The Lie Algebra of a Lie Group]]). For a homomorphism $F\circ L_g=L_{F(g)}\circ F$ ($\Rightarrow$ constant rank).

Used in: [[DM08 Lie Groups]]. Related: [[Lie Group]] · [[Lie Group Homomorphism]] · [[Diffeomorphism]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
