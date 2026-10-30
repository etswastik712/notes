---
title: Common Induction Errors
aliases: ["induction fallacies", "false induction proofs"]
subject: analysis
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Common Induction Errors

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Assignment-8.pdf#page=2|Assignment 8 Q7]] ($n=n+1$; induction on $\mathbb Q$). 🔵 the other cases are mine ([[PA08 Mathematical Induction]] §4).

> [!intuition] In one picture
> Every wrong proof breaks exactly one link: base, step, quantifier, or the set the claim lives in.

> [!key] The four breaks
> No base case ($n=n+1$). A step false at the smallest $k$ (horses; "all integers equal": $(2,1)\to(1,0)$). A correct step with the wrong bases ("all Fibonacci numbers are even"). A statement not about $\mathbb N$ ($x\ge1$ on $\mathbb Q$; "true for all finite $n$" is not "true at $\infty$": $\bigcap(0,\frac1n)=\varnothing$).

Patterns are not proofs: Moser's circle $1,2,4,8,16,31$; $n^2+n+41$ composite at $n=40$; $2^{32}+1=641\cdot6700417$.

Used in: [[PA08 Mathematical Induction]], [[PA05 Induction and the Number Systems]]. Related: [[Principle of Mathematical Induction]] · [[Counterexample]] · [[Strengthening the Induction Hypothesis]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
