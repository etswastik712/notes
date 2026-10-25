---
title: Bolzano-Weierstrass Theorem
aliases: ["Bolzano–Weierstrass", "bounded sequences have convergent subsequences"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Bolzano-Weierstrass Theorem

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=71|AI notes ch. 16.2]].

> [!intuition] In one picture
> Infinitely many points in a bounded region must pile up somewhere.

> [!key] Definition
> Every bounded real sequence has a convergent subsequence. Proof: every sequence has a monotone subsequence (peaks argument), which is bounded, hence converges.

$(-1)^n(1+\frac1n)$ has subsequences with limits $+1$ and $-1$; $\sin n$ has subsequences converging to every point of $[-1,1]$. It implies Cauchy completeness and is the sequential form of compactness of $[a,b]$.

Used in: [[PA06 The Real Numbers and Sequences]]. Related: [[Monotone Convergence Theorem]] · [[Cauchy Sequence]] · [[Compact Space]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
