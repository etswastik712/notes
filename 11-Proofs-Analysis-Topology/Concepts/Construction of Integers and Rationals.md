---
title: Construction of Integers and Rationals
aliases: ["Z as a quotient", "Q as a quotient", "fractions"]
subject: analysis
type: concept
scope: [extra-book]
by: [ai-notes]
status: draft
tags: [subject/analysis, type/concept, extra/book, src/ai-notes, status/draft]
---
# Construction of Integers and Rationals

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[proofs-prems-topo.pdf#page=64|AI notes ch. 14]].

> [!intuition] In one picture
> Integers are differences $a-b$ and rationals are fractions $a/b$, with different pairs naming the same number.

> [!key] Definition
> $\mathbb Z=(\mathbb N\times\mathbb N)/{\sim}$, $(a,b)\sim(c,d)\iff a+d=c+b$. $\mathbb Q=\{(a,b):b\ne0\}/{\sim}$, $(a,b)\sim(c,d)\iff ad=bc$. Operations are defined on representatives and checked to be well defined.

With $a,b\in\{0,\dots,5\}$ there are $11=2\cdot5+1$ integer classes (the values $-5..5$); numerators and denominators in $1..6$ give 36 pairs but only 23 distinct fractions. $\mathbb R$ then comes from cuts of $\mathbb Q$.

Used in: [[PA05 Induction and the Number Systems]]. Related: [[Equivalence Relation]] · [[Congruence Modulo n]] · [[Dedekind Cut]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
