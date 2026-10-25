---
title: Joint Distribution
aliases: ["joint pmf", "joint cdf"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Joint Distribution

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=23|class notes 2 Sep]].

> [!intuition] In one picture
> The table of probabilities for the pair $(X_1,X_2)$ together.

> [!key] Definition
> Discrete: $p(a_i,b_j)=P[X_1=a_i,X_2=b_j]$; general: $F(x_1,x_2)=P[X_1\le x_1,X_2\le x_2]$. Both variables must be defined on the same sample space.

## Example
Two dice, $X_1$ = sum, $X_2$ = maximum: $P[X_1=7,X_2=5]=P[\{(2,5),(5,2)\}]=\frac1{18}$ (Figure PR4.1 A). Each cell is $\frac1{36}$ or $\frac2{36}$.

Marginals are the row and column sums ([[Marginal Distribution]]); the joint table also determines every dependence between the two variables.

Used in: [[PR04 Joint Distributions Expectation and Variance]]. Related: [[Marginal Distribution]] · [[Independence of Random Variables]] · [[Linearity of Expectation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
