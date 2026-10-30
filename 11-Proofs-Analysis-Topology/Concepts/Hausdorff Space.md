---
title: Hausdorff Space
aliases: ["T2", "T2 space", "Hausdorff"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Hausdorff Space

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Munkres §17; [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=21|Lee Ch. 1, p. 3]].

> [!intuition] In one picture
> Any two distinct points can be put in separate open 'rooms': disjoint neighbourhoods.

> [!key] Definition
> $X$ is **Hausdorff** if for $x\neq y$ there are disjoint open sets $U\ni x$, $V\ni y$. Equivalent: the diagonal $\Delta\subseteq X\times X$ is closed.

Consequences: limits of sequences are unique, compact sets are closed, continuous maps into $X$ have closed graphs. Metric spaces and compact subsets of Hausdorff spaces are Hausdorff. Fails for the cofinite topology and the [[Line with Two Origins]]; the manifold definition requires it ([[DM01 Smooth Manifolds]]).

Used in: [[PA12 Separation, Countability and Local Compactness]]. Related: [[Separation Axioms]] · [[Compact Space]] · [[Quotient Topology]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
