---
title: Regular Level Set Theorem
aliases: ["regular value theorem", "implicit function theorem for manifolds", "submersion level set theorem"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Regular Level Set Theorem

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[mt3184-differential-geometry-and-lie-groups/2026-08-27-hw4|HW4]] Q1.
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=124|Lee Cors. 5.13–5.14, pp. 105–106]].

> [!intuition] In one picture
> Solutions of a system of equations whose derivative has full rank form a manifold of the expected dimension: the manifold version of the implicit function theorem.

> [!key] Definition
> $q$ regular value of $F:M^m\to N^n$ $\Rightarrow$ $S=F^{-1}(q)$ is an embedded submanifold of dimension $m-n$ with $T_pS=\ker dF_p$. Proof: surjectivity of $dF$ is an open condition $\Rightarrow$ $F$ is a submersion near $S$ $\Rightarrow$ rank theorem gives slice charts.

$S^n=|x|^{-2}(1)$; $SL(n,\mathbb R)=\det^{-1}(1)$ (dim $n^2-1$); $O(n)=\Phi^{-1}(I)$, $\Phi=AA^T$ (dim $n(n-1)/2$). Euclidean version: [[Implicit Function Theorem]].

Used in: [[DM06 Submanifolds]]. Related: [[Regular Value]] · [[Embedded Submanifold]] · [[Implicit Function Theorem]] · [[Orthogonal Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
