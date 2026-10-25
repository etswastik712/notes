---
title: Heine-Borel Theorem
aliases: ["Heine–Borel", "closed and bounded is compact"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Heine-Borel Theorem

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=77|AI notes ch. 18.4]].

> [!intuition] In one picture
> In $\mathbb R$ (and $\mathbb R^n$), compact means closed and bounded.

> [!key] Definition
> $A\subseteq\mathbb R$ is compact $\iff$ closed and bounded. Key step: $[a,b]$ is compact, by taking $s=\sup\{x:[a,x]\text{ has a finite subcover}\}$ and showing $s=b$.

Compact $\Rightarrow$ bounded ($\{(-n,n)\}$) and closed (balls of half the distance to an outside point). Closed and bounded $\Rightarrow$ compact: embed in $[a,b]$ and add the open complement to a cover. Fails in infinite-dimensional spaces (closed unit ball is not compact).

Used in: [[PA07 Metric and Topological Spaces]]. Related: [[Compact Space]] · [[Least Upper Bound Property]] · [[Open and Closed Sets]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
