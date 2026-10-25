---
title: Principle of Mathematical Induction
aliases: ["induction", "PMI", "inductive set"]
subject: analysis
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, taught, src/lecture-notes, status/draft]
---
# Principle of Mathematical Induction

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Assignment-8.pdf#page=1|Assignment 8]].

> [!intuition] In one picture
> If the first domino falls and each knocks the next, all fall.

> [!key] Definition
> $S\subseteq\mathbb N$ **inductive** if $k\in S\Rightarrow k+1\in S$. PMI: $S$ inductive and $1\in S\Rightarrow S=\mathbb N$. Statement form: $P(1)$ and $[P(k)\Rightarrow P(k+1)]$ for all $k$ give $P(n)$ for all $n$; extended from base $m$. Write: define $P(n)$, base, step, conclude.

$\sum_{k=1}^n(2k-1)=n^2$; $\sum k\cdot k!=(n+1)!-1$; $6\mid n^3+5n$; $2^n>n^2$ for $n\ge5$ (fails at $2,3,4$: base case must be 5). "$n=n+1$": step valid, base false. Induction fails on $\mathbb Q$ ($x\ge1$): the orbit of 1 is not all of $\mathbb Q$.

Used in: [[PA05 Induction and the Number Systems]]. Related: [[Well-Ordering Principle]] · [[Strong Induction]] · [[Recursion Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
