---
title: Matching Problem
aliases: ["derangements", "hat-check problem", "coat problem"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Matching Problem

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=9|class notes 12 Aug]].

> [!intuition] In one picture
> Shuffle $n$ coats back at random: the chance nobody gets their own is about $1/e$, almost regardless of $n$.

> [!key] Definition
> $P[\text{no match}]=\sum_{k=0}^n\dfrac{(-1)^k}{k!}\to e^{-1}=0.3679$; the number of derangements is $D_n=n!\sum_{k=0}^n\frac{(-1)^k}{k!}$.

## Derivation
$A_i$ = person $i$ gets their coat. $P[A_{i_1}\cap\dots\cap A_{i_k}]=\frac{(n-k)!}{n!}$ and there are $\binom nk$ intersections, so $P[\cup A_i]=\sum_{k\ge1}(-1)^{k+1}\binom nk\frac{(n-k)!}{n!}=\sum_{k\ge1}\frac{(-1)^{k+1}}{k!}$.

## Numbers
No match: $n=3$: $0.3333$; $n=4$: $0.375$; $n=5$: $0.3667$; $n=10$: $0.367879$. At least one match is $\approx0.632$. Simulation agrees (Figure PR1.1).

> [!connection] The mean is exactly 1
> The expected number of fixed points is $n\cdot\frac1n=1$ for every $n$ by [[Linearity of Expectation]], and the number of fixed points is close to Poisson$(1)$.

Used in: [[PR01 Counting and the Axioms of Probability]]. Related: [[Inclusion-Exclusion Principle]] · [[Counting Principles]] · [[Linearity of Expectation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
