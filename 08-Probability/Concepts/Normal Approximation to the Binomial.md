---
title: Normal Approximation to the Binomial
aliases: ["de Moivre-Laplace", "continuity correction"]
subject: probability
type: concept
scope: [extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, extra/book, src/lecture-notes, status/draft]
---
# Normal Approximation to the Binomial

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Ross Ch. 5, 8; follows from the CLT.

> [!intuition] In one picture
> A binomial with many trials is a bell curve, provided you treat the integer steps as intervals.

> [!key] Definition
> $X\sim$ Bin$(n,p)\approx N(np,npq)$; $P[X\le k]\approx\Phi\Big(\frac{k+\frac12-np}{\sqrt{npq}}\Big)$ (continuity correction).

Bin$(30,0.3)$, $P[X\le10]$: exact $0.7304$, corrected $0.7250$, uncorrected $0.6548$. Bin$(100,0.5)$, $P[X\le45]$: exact $0.18410$, corrected $0.18406$, uncorrected $0.1587$; $P[X\ge60]$: exact $0.0284$, corrected $0.0287$. Poisson$(100)$, $P[X\le90]$: $0.1714$ vs $0.1711$. Poor when $np$ or $nq$ is small: use the Poisson.

Used in: [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Central Limit Theorem]] · [[Binomial Distribution]] · [[Poisson Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
