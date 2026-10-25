---
title: Conditional Probability
aliases: ["conditioning", "reduced sample space"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Conditional Probability

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=12|class notes 13 Aug]].

> [!intuition] In one picture
> Learn that $F$ happened and shrink the world to $F$; the conditional probability of $E$ is the share of $F$ that lies in $E$.

> [!key] Definition
> $P[E\mid F]=\dfrac{P[E\cap F]}{P[F]}$ for $P[F]>0$. For fixed $F$, $A\mapsto P[A\mid F]$ satisfies the three [[Axioms of Probability]].

## Reduced sample space
With equally likely outcomes, $P[E\mid F]=|E\cap F|/|F|$. North and South hold 8 spades; East has 3 of the remaining 5 in the other 26 cards: $\frac{\binom53\binom{21}{10}}{\binom{26}{13}}=0.339$.

> [!pitfall] $P[E\mid F]\ne P[F\mid E]$
> $P[+\mid\text{ill}]=0.95$ does not mean $P[\text{ill}\mid+]=0.95$ (it is $0.323$ for the class example): the prosecutor's fallacy. See [[Bayes' Theorem]].

> [!example] Children
> $P[\text{both boys}\mid\text{at least one boy}]=\tfrac13$ but $P[\text{both boys}\mid\text{the elder is a boy}]=\tfrac12$: different information, different reduced spaces.

Used in: [[PR02 Conditional Probability Bayes Rule and Independence]]. Related: [[Multiplication Rule]] · [[Law of Total Probability]] · [[Bayes' Theorem]] · [[Independence of Events]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
