---
title: Set of Measure Zero
aliases: ["measure zero", "null set", "measure zero in a manifold"]
subject: diff-geometry
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/diff-geometry, type/concept, extra/book, src/book, status/draft]
---
# Set of Measure Zero

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=144|Lee Lemma 6.2, Props. 6.3–6.8, pp. 126–128]].

> [!intuition] In one picture
> A set so thin it can be covered by countably many cubes of arbitrarily small total volume: curves in the plane, points on a line.

> [!key] Definition
> $A\subseteq\mathbb R^n$ has measure zero if for every $\varepsilon>0$ countably many cubes of total volume $<\varepsilon$ cover it. Countable unions are null; null sets have empty interior; $C^1$ maps preserve null sets (Lipschitz estimate), so the notion is chart independent on manifolds.

If $\dim M<\dim N$, $F(M)$ is null in $N$ (apply the previous fact to $F(x,y)=F(x)$ on $U\times\mathbb R^{n-m}$). The parabola arc $\{(t,t^2)\}$: $\varepsilon$-neighbourhood area $\approx2\varepsilon L\to0$.

Used in: [[DM07 Sard Whitney and Transversality]]. Related: [[Sard's Theorem]] · [[Whitney Embedding Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
