---
title: Separation Axioms
aliases: ["T1", "regular space", "normal space", "Urysohn's lemma", "T3", "T4"]
subject: analysis
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/book, status/draft]
---
# Separation Axioms

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Munkres §§17, 31–33.

> [!intuition] In one picture
> A ladder grading how well open sets separate points and closed sets: $T_1$, Hausdorff, regular, normal.

> [!key] Definition
> $T_1$: points are closed. Regular: a point and a closed set it avoids have disjoint neighbourhoods. Normal: so do two disjoint closed sets. Normal $\Rightarrow$ regular $\Rightarrow$ Hausdorff $\Rightarrow T_1$.

Metric spaces and compact Hausdorff spaces are normal. **Urysohn's lemma:** in a normal space disjoint closed $A,B$ admit continuous $f:X\to[0,1]$ with $f|_A=0$, $f|_B=1$ (in a metric space $f=d(x,A)/(d(x,A)+d(x,B))$). Second-countable regular spaces are metrisable (Urysohn), so every manifold is.

Used in: [[PA12 Separation, Countability and Local Compactness]]. Related: [[Hausdorff Space]] · [[Second-Countable Space]] · [[Compact Space]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
