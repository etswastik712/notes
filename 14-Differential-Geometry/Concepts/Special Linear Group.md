---
title: Special Linear Group
aliases: ["SL(n)", "SL(n,R)", "unimodular group"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Special Linear Group

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[mt3184-differential-geometry-and-lie-groups/2026-09-03-august-31-september-4|Aug 31–Sep 4 note]] (Prop 7.16: $SL(n)=\ker\det$ is an embedded Lie subgroup of dimension $n^2-1$); HW5 Q3, HW6 Q7.

> [!intuition] In one picture
> Matrices that preserve volume and orientation: determinant $1$.

> [!key] Definition
> $SL(n,\mathbb R)=\det^{-1}(1)$; $d(\det)_X(B)=\det X\operatorname{tr}(X^{-1}B)$ is onto $\mathbb R$ at every $X\in GL(n)$, so $SL(n,\mathbb R)$ is an embedded submanifold of dimension $n^2-1$, with $T_ISL(n)=\ker\operatorname{tr}$ ($\mathfrak{sl}(n)$, closed under the commutator).

$GL(n,\mathbb C)\cong SL(n,\mathbb C)\rtimes\mathbb C^\times$ (HW6 Q3c). Kernel of the homomorphism $\det$ ([[DM08 Lie Groups]]).

Used in: [[DM06 Submanifolds]]. Related: [[Orthogonal Group]] · [[Regular Level Set Theorem]] · [[Lie Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
