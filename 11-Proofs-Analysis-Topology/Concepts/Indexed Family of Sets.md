---
title: Indexed Family of Sets
aliases: ["indexed union", "indexed intersection", "infinite product of sets"]
subject: analysis
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, taught, src/lecture-notes, status/draft]
---
# Indexed Family of Sets

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Assignment-prems_merged.pdf#page=3|Assignment 3, Q7–Q12]].

> [!intuition] In one picture
> A sequence of sets $A_1,A_2,\dots$ and what you get by taking all of them together.

> [!key] Definition
> $\bigcup_nA_n=\{x:\exists n\ x\in A_n\}$, $\bigcap_nA_n=\{x:\forall n\ x\in A_n\}$, $\prod_nA_n=\{(a_n):a_n\in A_n\ \forall n\}$ (whole sequences).

$A_n=(-\frac1n,\frac1n)$: $\bigcup=(-1,1)$, $\bigcap=\{0\}$. $A_n=[-n,1-\frac1n)$: $\bigcup=(-\infty,1)$, $\bigcap=[-1,0)$. $H_n=\{y\ge-n\}$: $\bigcup=\mathbb R^2$, $\bigcap=H_1$. An empty $A_k$ makes $\bigcap$ and $\prod$ empty. $\prod_n\{0,1\}$ is uncountable ([[Cantor's Diagonal Argument]]); infinite intersections of open sets need not be open.

Used in: [[PA02 Sets Families and the ZFC Foundations]]. Related: [[Cartesian Product]] · [[Set Operations and De Morgan's Laws]] · [[Open and Closed Sets]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
