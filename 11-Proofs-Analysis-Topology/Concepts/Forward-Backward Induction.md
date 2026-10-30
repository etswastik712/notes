---
title: Forward-Backward Induction
aliases: ["backward induction", "Cauchy induction", "downward induction"]
subject: analysis
type: concept
scope: [extra-book, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, extra/beyond, src/own-notes, status/draft]
---
# Forward-Backward Induction

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Tao *Analysis I* Exercise 2.2.6 (backwards induction). 🔵 the AM–GM proof is Cauchy's, written out in [[PA08 Mathematical Induction]] §2.

> [!intuition] In one picture
> Climb up a **sparse** ladder (the powers of $2$), then walk **down** from each rung to fill in every integer below it.

> [!key] Statement
> If $P(n_0)$ holds and $P(k+1)\Rightarrow P(k)$ for all $k$, then $P(m)$ holds for all $m\le n_0$. Combined with a forward proof $P(n)\Rightarrow P(2n)$ this gives all $n\ge2$: AM–GM for $2^j$ numbers by doubling, then for $n$ numbers by adding their geometric mean as an extra term.

Used in: [[PA08 Mathematical Induction]]. Related: [[Principle of Mathematical Induction]] · [[Strong Induction]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
