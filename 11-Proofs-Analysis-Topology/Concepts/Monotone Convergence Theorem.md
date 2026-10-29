---
title: Monotone Convergence Theorem
aliases: ["bounded monotone sequences converge"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Monotone Convergence Theorem

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=70|AI notes ch. 16.2]].

> [!intuition] In one picture
> A sequence that only rises and cannot escape upward must settle.

> [!key] Definition
> A bounded increasing sequence converges to its supremum; a bounded decreasing one to its infimum.

$a_{n+1}=\sqrt{2+a_n}$, $a_1=1$: increasing, bounded by 2, limit solves $L^2=L+2$, $L=2$ ($a_9=1.99998$). $(1+\frac1n)^n$ increases to $e$ ($2,2.25,2.488,2.594,2.705,2.718,\dots$).

Used in: [[PA06 The Real Numbers and Sequences]]. Related: [[Least Upper Bound Property]] · [[Nested Interval Property]] · [[Bolzano-Weierstrass Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Continuity of Probability]] (Probability): continuity from below, $P(\cup A_n)=\lim P(A_n)$, is the monotone convergence theorem for indicator functions.
