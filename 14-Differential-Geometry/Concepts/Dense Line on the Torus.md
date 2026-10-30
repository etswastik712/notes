---
title: Dense Line on the Torus
aliases: ["irrational winding", "dense curve on the torus", "Lie subgroup that is not closed"]
subject: diff-geometry
type: concept
scope: [taught]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, src/lecture-notes, src/book, status/draft]
---
# Dense Line on the Torus

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG12 (injective immersion with non-embedded image); [[mt3184-differential-geometry-and-lie-groups/2026-09-03-august-31-september-4|Aug 31–Sep 4 note]]; HW9 Q6 (closure of a Lie subgroup).

> [!intuition] In one picture
> Wind a line around a doughnut with an irrational slope: it never closes up, never repeats, and comes arbitrarily close to every point.

> [!key] Definition
> $F(t)=(e^{it},e^{i\alpha t})$, $\alpha$ irrational: an injective immersion $\mathbb R\to T^2$ with dense image, hence not an embedding. By Dirichlet, $F(2\pi q)\to F(0)$ along integers $q\to\infty$.

$\alpha=\sqrt2$: smallest distance to $F(0)$ for $t\le10,10^2,10^3,10^4$ is $1.50,0.107,0.0183,0.00153$; at $t=2\pi\cdot985$ it is $2.3\times10^{-3}$. It is a one-parameter subgroup of $T^2$ whose image is a **non-closed Lie subgroup** ([[DM15 Closed Subgroups and the Lie Correspondence]]).

Used in: [[DM05 Immersions, Embeddings, Submersions and Coverings]]. Related: [[Smooth Embedding]] · [[Immersion and Submersion]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
