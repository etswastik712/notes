---
title: Whitney Embedding Theorem
aliases: ["Whitney embedding", "Whitney immersion theorem", "every manifold embeds in R^N"]
subject: diff-geometry
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, src/book, status/draft]
---
# Whitney Embedding Theorem

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=152|Lee Thm 6.15, p. 134]]; Thms 6.18–6.20 (immersion, strong forms).

> [!intuition] In one picture
> Every abstract manifold can be realised as a surface in some Euclidean space; in fact $2n+1$ (even $2n$) dimensions always suffice.

> [!key] Definition
> Every smooth $n$-manifold embeds in $\mathbb R^{2n+1}$ (Thm 6.15; proof: partition of unity gives an embedding in some $\mathbb R^N$, then project along a direction avoiding the secant ($\dim2n$) and tangent ($\dim2n-1$) directions, possible when $N-1>2n$ by Sard-type measure arguments). Strong: $\mathbb R^{2n}$; immersions: $\mathbb R^{2n}$ ($\mathbb R^{2n-1}$ for $n>1$).

Sharp: $\mathbb{RP}^2$ embeds in $\mathbb R^4$, not $\mathbb R^3$. The trefoil's secant directions fill $S^2$ (648/648 bins), so projection to a plane always creates crossings.

Used in: [[DM07 Sard Whitney and Transversality]]. Related: [[Smooth Embedding]] · [[Partition of Unity]] · [[Sard's Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
