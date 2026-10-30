---
title: Orthogonal Group
aliases: ["O(n)", "SO(n)", "orthogonal matrices"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Orthogonal Group

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[mt3184-differential-geometry-and-lie-groups/2026-10-10-october-5-9|Oct 5–9 note]] (DG19–DG20: $O(n)$ embedded, $SO(n)$ its identity component, $\mathrm{Lie}(O(n))$ skew); HW6 Q1–Q3, HW7 Q3.

> [!intuition] In one picture
> Rotations and reflections of $\mathbb R^n$: the linear maps preserving lengths.

> [!key] Definition
> $O(n)=\{A:AA^T=I\}=\Phi^{-1}(I)$, $\Phi(A)=AA^T$. $d\Phi_A(B)=BA^T+AB^T$ is onto $\operatorname{Sym}(n)$ for every invertible $A$, so $O(n)$ is an embedded submanifold of dimension $n(n-1)/2$ ($1,3,6,10$ for $n=2,\dots,5$, checked), compact, with $T_IO(n)=\{B+B^T=0\}$ (skew matrices). $SO(n)=O(n)_0$.

$\det:O(n)\to\{\pm1\}$ shows $SO(n)$ is open and closed in $O(n)$. $O(n)\cong SO(n)\rtimes O(1)$ (HW6 Q3b). A Lie group ([[DM08 Lie Groups]]); $\mathrm{Lie}(SO(3))\cong(\mathbb R^3,\times)$ ([[DM11 The Lie Algebra of a Lie Group]]).

Used in: [[DM06 Submanifolds]]. Related: [[Special Linear Group]] · [[Regular Level Set Theorem]] · [[Lie Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
