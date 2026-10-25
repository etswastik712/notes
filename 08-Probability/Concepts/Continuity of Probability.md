---
title: Continuity of Probability
aliases: ["continuity from below", "limits of events"]
subject: probability
type: concept
scope: [extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, extra/book, src/lecture-notes, status/draft]
---
# Continuity of Probability

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** [[ilovepdf_merged-1.pdf#page=9|class notes 12 Aug §2, 'not necessary for this course']].

> [!intuition] In one picture
> Probability of a growing (or shrinking) sequence of events is the limit of their probabilities.

> [!key] Definition
> If $E_1\subset E_2\subset\cdots$ then $P(\bigcup E_n)=\lim P(E_n)$; if $E_1\supset E_2\supset\cdots$ then $P(\bigcap E_n)=\lim P(E_n)$.

## Proof for increasing sequences
Put $F_1=E_1$, $F_n=E_n\setminus\bigcup_{i<n}E_i$: pairwise disjoint, $E_n=\bigcup_{i\le n}F_i$. Countable additivity gives $P(\bigcup E_n)=\sum_nP(F_n)=\lim P(E_n)$. For decreasing sequences apply this to complements.

> [!example] Uniform
> $E_n=(0,\tfrac1n)$ decreases to $\varnothing$ under $U(0,1)$ and $P(E_n)=\tfrac1n\to0$.

Consequence: a cdf is right-continuous ([[Cumulative Distribution Function]]), since $\{X\le x_n\}\downarrow\{X\le a\}$ when $x_n\downarrow a$.

Used in: [[PR01 Counting and the Axioms of Probability]]. Related: [[Axioms of Probability]] · [[Cumulative Distribution Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
