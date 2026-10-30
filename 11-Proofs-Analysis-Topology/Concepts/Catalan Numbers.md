---
title: Catalan Numbers
aliases: ["Catalan sequence", "parenthesisations", "full binary trees"]
subject: analysis
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/analysis, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Catalan Numbers

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** [[PA09 Strong Induction and Recursion]] §3 and §5.

> [!intuition] In one picture
> The number of ways to bracket a product, or to draw a full binary tree: split into a left part and a right part in every possible way.

> [!key] Facts
> $C_0=1$, $C_{n+1}=\sum_{k=0}^nC_kC_{n-k}$ (a strong recursion): $1,1,2,5,14,42,132,429,\dots$; $C_n=\frac1{n+1}\binom{2n}n$. Counts fully parenthesised products of $n+1$ factors ($C_3=5$), full binary trees with $n$ internal nodes (checked by enumeration for $n\le7$), and more.

Used in: [[PA09 Strong Induction and Recursion]]. Related: [[Structural Induction]] · [[Strong Induction]] · [[Recursion Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Drainage Density and Horton's Laws]] (Landscapes): the number of full binary tree shapes with $m$ internal nodes is $C_m$, from the recursion $C_{n+1}=\sum C_kC_{n-k}$; this is the counting behind the random-topology model of stream networks, where Horton's bifurcation ratio comes out near 4.
