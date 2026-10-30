---
title: Josephus Problem
aliases: ["Josephus permutation", "every second person"]
subject: analysis
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/analysis, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Josephus Problem

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** [[PA09 Strong Induction and Recursion]] §3.

> [!intuition] In one picture
> People in a circle; every second one is removed until one is left. Who survives?

> [!key] Result
> $J(1)=1$, $J(2n)=2J(n)-1$, $J(2n+1)=2J(n)+1$, so for $n=2^m+\ell$ ($0\le\ell<2^m$): $J(n)=2\ell+1$. Proved by strong induction on $n$ (the recursion calls $\lfloor n/2\rfloor$). $J(41)=19$, $J(100)=73$; $J=1$ exactly at powers of $2$ (binary: move the leading $1$ to the end).

Used in: [[PA09 Strong Induction and Recursion]]. Related: [[Strong Induction]] · [[Recursion Theorem]] · [[Fibonacci Numbers]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
