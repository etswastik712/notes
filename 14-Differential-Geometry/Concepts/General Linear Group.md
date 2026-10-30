---
title: General Linear Group
aliases: ["GL(n)", "GL(n,R)", "GL(n,C)"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# General Linear Group

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slides DG10–DG11 (examples); HW4–HW6.

> [!intuition] In one picture
> All invertible linear maps of $\mathbb R^n$ (or $\mathbb C^n$): the largest matrix group, from which the classical groups are cut out.

> [!key] Definition
> $GL(n,\mathbb R)=\{\det\ne0\}$, an open subset of $M(n,\mathbb R)\cong\mathbb R^{n^2}$, so an $n^2$-manifold; multiplication is polynomial, inversion $\operatorname{adj}A/\det A$ is smooth. $\dim_{\mathbb R}GL(n,\mathbb C)=2n^2$. Two components for $\mathbb R$ ($\det\gtrless0$), connected for $\mathbb C$. $T_IGL(n)=M(n,\mathbb R)$ with $[A,B]=AB-BA$ ([[DM11 The Lie Algebra of a Lie Group]]).

Subgroups: $SL(n)=\ker\det$, $O(n)$, $SO(n)$, $U(n)$, $SU(n)$ ([[Special Linear Group]], [[Orthogonal Group]], [[Unitary Group]]). $GL(n,\mathbb C)\cong SL(n,\mathbb C)\rtimes\mathbb C^\times$ (HW6 Q3c).

Used in: [[DM08 Lie Groups]]. Related: [[Special Linear Group]] · [[Orthogonal Group]] · [[Lie Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
