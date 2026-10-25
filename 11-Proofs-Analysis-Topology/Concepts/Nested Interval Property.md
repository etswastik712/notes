---
title: Nested Interval Property
aliases: ["nested intervals", "Cantor intersection theorem"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Nested Interval Property

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=71|AI notes ch. 16.2]].

> [!intuition] In one picture
> Shrinking closed intervals trap at least one point.

> [!key] Definition
> If $[a_1,b_1]\supseteq[a_2,b_2]\supseteq\cdots$ then $\bigcap_n[a_n,b_n]\ne\varnothing$ ($\sup a_n$ lies in every interval). **Closed** is essential: $\bigcap(0,\frac1n)=\varnothing$.

Bisection for $\sqrt2$: widths $0.5,0.25,0.125,\dots=2^{-n}$ (Figure PA6.1 B). Proof that $\mathbb R$ is uncountable: choose $I_n\subset I_{n-1}$ (a third) missing $x_n$; the point in $\bigcap I_n$ is not in the list.

Used in: [[PA06 The Real Numbers and Sequences]]. Related: [[Monotone Convergence Theorem]] · [[Cantor's Diagonal Argument]] · [[Compact Space]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
