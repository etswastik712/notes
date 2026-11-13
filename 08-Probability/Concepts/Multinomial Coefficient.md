---
title: Multinomial Coefficient
aliases: ["multinomial theorem"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft, quiz/probability, quiz/pr-hw5]
---
# Multinomial Coefficient

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=2|class notes 5–6 Aug]].

> [!intuition] In one picture
> The number of ways to split $n$ different things into labelled groups of prescribed sizes.

> [!key] Definition
> $\dbinom n{m_1,\dots,m_r}=\dfrac{n!}{m_1!\cdots m_r!}$ with $\sum m_i=n$; the **multinomial theorem** is $(x_1+\dots+x_r)^n=\sum\binom n{m_1,\dots,m_r}x_1^{m_1}\cdots x_r^{m_r}$.

## Why
Choose which $m_1$ items go in group 1 ($\binom n{m_1}$), then which $m_2$ of the rest, and so on: $\binom n{m_1}\binom{n-m_1}{m_2}\cdots=\frac{n!}{m_1!\cdots m_r!}$. It also counts the arrangements of a word with repeated letters.

> [!example] A dozen people
> Teams of $2,5,5$: $\frac{12!}{2!5!5!}=16\,632$ if all three teams are labelled; divide by $2$ when the two 5-teams are interchangeable: $8316$.

Used in: [[PR01 Counting and the Axioms of Probability]]. Related: [[Counting Principles]] · [[Binomial Distribution]].


## Continued in the vault (added 2026-11-07)
- The multinomial *distribution* built on this coefficient: [[Multinomial Distribution]], [[Multinomial Covariance Matrix]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Continued in Part II (added 2026-10-30)
- $\ln g\approx-N\sum p_i\ln p_i$ and typical sequences: [[SM01 Probability Large Numbers and Information]] §7.1 ([[Shannon Entropy]], [[Stirling's Approximation]]).

## Across subjects
- [[Multiplicity]] (Thermodynamics): the number of ways to distribute $N$ distinguishable particles over levels with occupations $N_i$ is the multinomial coefficient $N!/\prod N_i!$, whose maximisation under constraints gives the Boltzmann distribution.
