---
title: Inclusion-Exclusion Principle
aliases: ["inclusion exclusion", "sieve formula"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Inclusion-Exclusion Principle

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=8|class notes 12 Aug]], [[Practice problems 14th August 2026.pdf#page=1|sheet 14 Aug, problems 1–2]].

> [!intuition] In one picture
> Add the events, subtract the pairwise overlaps you counted twice, add back the triple overlaps, and so on.

> [!key] Definition
> $P\Big(\bigcup_{i=1}^nE_i\Big)=\sum_iP(E_i)-\sum_{i<j}P(E_i\cap E_j)+\sum_{i<j<k}P(E_i\cap E_j\cap E_k)-\dots+(-1)^{n-1}P\Big(\bigcap_iE_i\Big).$

## Counting proof
A sample point in exactly $r\ge1$ events is counted $\binom r1-\binom r2+\dots+(-1)^{r-1}\binom rr=1-(1-1)^r=1$ time on the right; a point in none is counted 0 times. So both sides agree point by point.

> [!example] Three events
> $P(A)=0.5$, $P(B)=0.4$, $P(C)=0.3$, pairs $0.2,0.1,0.1$, triple $0.05$: $P(A\cup B\cup C)=1.2-0.4+0.05=0.85$.

Applications: the [[Matching Problem]] and the tail of the [[Coupon Collector Problem]]: $P[T>n]=\sum_i(-1)^{i+1}\binom Ni(1-\tfrac iN)^n$.

Used in: [[PR01 Counting and the Axioms of Probability]]. Related: [[Matching Problem]] · [[Axioms of Probability]] · [[Coupon Collector Problem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
