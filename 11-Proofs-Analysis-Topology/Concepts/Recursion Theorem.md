---
title: Recursion Theorem
aliases: ["definition by recursion", "recursive definition"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Recursion Theorem

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=59|AI notes ch. 12.2]].

> [!intuition] In one picture
> You may define a sequence by giving its start and a rule for the next term.

> [!key] Definition
> For $x_0\in X$ and $g:X\to X$ there is a **unique** sequence with $x_{n+1}=g(x_n)$. Two-step version: Fibonacci $F_{n+2}=F_{n+1}+F_n$.

Factorial, powers, finite sums, iterates of a map (a discrete-time population model $N_{t+1}=g(N_t)$) are defined this way. Uniqueness is proved by induction; existence uses the Axiom of Infinity. $x_{n+1}=\sqrt{2+x_n}$ and Newton's iteration for $\sqrt2$ are recursive sequences.

Used in: [[PA05 Induction and the Number Systems]]. Related: [[Principle of Mathematical Induction]] · [[Natural Numbers]] · [[Sequence and Limit]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
