---
title: Strengthening the Induction Hypothesis
aliases: ["stronger statement", "inductive loading", "generalise before inducting"]
subject: analysis
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/analysis, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Strengthening the Induction Hypothesis

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** my own, from the worked example of [[PA08 Mathematical Induction]] §3.

> [!intuition] In one picture
> The step needs room: if the hypothesis is too weak to absorb the new term, prove something **stronger**; its stronger hypothesis does the absorbing.

> [!key] The standard example
> $\sum_{k\le n}\frac1{k^2}<2$ cannot be pushed through directly ($s_k<2$ gives only $s_{k+1}<2+\frac1{(k+1)^2}$). Prove $s_n\le2-\frac1n$ instead: base $1\le1$, step $\frac1{(k+1)^2}\le\frac1{k(k+1)}=\frac1k-\frac1{k+1}$. The same idea: prove the chessboard tiling for **every** position of the hole, not one.

> [!pitfall] Watch out
> The stronger statement must still be true (check small $n$ first), and it must imply the original.

Used in: [[PA08 Mathematical Induction]]. Related: [[Principle of Mathematical Induction]] · [[Common Induction Errors]] · [[Proof Techniques]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
