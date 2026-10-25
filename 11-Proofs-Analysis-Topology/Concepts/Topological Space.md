---
title: Topological Space
aliases: ["topology", "metrisable", "discrete topology", "cofinite topology", "subspace topology"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Topological Space

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=76|AI notes ch. 18.1]]; Munkres Ch. 2.

> [!intuition] In one picture
> Keep only which sets are open; that is all continuity needs.

> [!key] Definition
> A topology $\tau\subseteq\mathcal P(X)$: $\varnothing,X\in\tau$; closed under arbitrary unions and finite intersections. Discrete $\mathcal P(X)$; indiscrete $\{\varnothing,X\}$ (not metrisable for $|X|\ge2$); cofinite; subspace $\{U\cap S\}$; basis.

Topologies on $n$ points: $1,4,29,355$ (labelled), $1,3,9,33$ (up to homeomorphism) for $n=1..4$, equal to the numbers of **preorders**. Example on $\{1,2,3\}$: $\{\varnothing,\{1\},\{3\},\{1,2\},\{1,3\},X\}$ with $\mathrm{cl}\{1\}=\{1,2\}$.

Used in: [[PA07 Metric and Topological Spaces]]. Related: [[Metric Space]] · [[Continuous Function (Topological)]] · [[Partially Ordered Set]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
