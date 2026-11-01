---
title: Semidirect Product of Lie Groups
aliases: ["semidirect product", "N semidirect H", "internal semidirect product", "split exact sequence of Lie groups"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Semidirect Product of Lie Groups

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG16 and handout 'DG Semidirect products' via [[mt3184-differential-geometry-and-lie-groups/2026-09-10-september-7-12|Sep 7–12 note]]; HW6 Q3.
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=186|Lee Prop. 7.33, p. 168]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=187|Lee Thm 7.35, p. 169]].

> [!intuition] In one picture
> Two groups glued with a twist: $H$ acts on $N$ by automorphisms and the product law remembers it.

> [!key] Definition
> $N\rtimes_\theta H$ is the manifold $N\times H$ with $(n_1,h_1)(n_2,h_2)=(n_1\theta_{h_1}(n_2),h_1h_2)$. $N=N\times\{e\}$ is normal (kernel of the projection), $H=\{e\}\times H$ a complement. **Criterion (HW6 Q3a):** $G\cong N\rtimes H$ iff $\varphi:G\to H$, $\psi:H\to G$ with $\varphi\psi=\mathrm{id}$, $\ker\varphi\cong N$. Internal form: Thm 7.35.

$O(n)=SO(n)\rtimes O(1)$, $GL(n,\mathbb C)=SL(n,\mathbb C)\rtimes\mathbb C^\times$, $E(n)=\mathbb R^n\rtimes O(n)$ ([[Euclidean Group]]), $\mathrm{Aff}(1)=\mathbb R\rtimes\mathbb R^\times$. $SU(2)\to SO(3)$ does **not** split ($S^3$ is connected, $\{\pm1\}\times SO(3)$ is not). Abstract version: [[Semidirect Product]], [[Complement of a Normal Subgroup]].

Used in: [[DM09 Group Actions and Semidirect Products]]. Related: [[Euclidean Group]] · [[Lie Group]] · [[Lie Group Homomorphism]] · [[Special Linear Group]] · [[Orthogonal Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
