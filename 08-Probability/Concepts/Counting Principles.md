---
title: Counting Principles
aliases: ["combinatorics", "permutations and combinations", "stars and bars", "binomial theorem"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Counting Principles

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=1|class notes 5–6 Aug]], [[Practice problems 7th August 2026.pdf#page=1|sheet 7 Aug]].

> [!intuition] In one picture
> Counting is multiplication for independent choices, division by symmetries you do not want to count, and a bijection when nothing else works.

> [!key] Definition
> **Multiplication principle:** $m_1m_2\cdots m_r$. **Permutations:** $n!$; with $k_i$ identical of kind $i$: $\frac{n!}{k_1!\cdots k_r!}$. **Combinations:** $\binom nr=\frac{n!}{r!(n-r)!}$. **Pascal:** $\binom nr=\binom{n-1}r+\binom{n-1}{r-1}$. **Stars and bars:** $n$ identical balls into $k$ labelled boxes: $\binom{n+k-1}{k-1}$, each non-empty: $\binom{n-1}{k-1}$.

## Story proofs
Count the same set in two ways. Pascal: the $r$-subsets of $\{1,\dots,n\}$ either contain $n$ ($\binom{n-1}{r-1}$) or do not ($\binom{n-1}r$).

> [!example] Antennas
> $n$ antennas, $m$ defective, no two defectives adjacent: place the $n-m$ working ones, then choose $m$ of the $n-m+1$ gaps: $\binom{n-m+1}m$. For $n=10$, $m=3$: $56$ of $\binom{10}3=120$.

> [!pitfall] A factor of $k!$
> Decide whether order matters and whether the groups or balls are distinguishable. Teams of $4,4,4$ from 12: $\frac{12!}{(4!)^3}=34\,650$ if the teams are labelled, $5775$ if not.

Used in: [[PR01 Counting and the Axioms of Probability]]. Related: [[Multinomial Coefficient]] · [[Naive Definition of Probability]] · [[Binomial Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Burnside's Lemma]] (Group Theory): Burnside's lemma counts distinct arrangements up to symmetry as the average number of fixed points, a counting tool used for isomers, colourings and necklaces.
