---
title: Marginal Distribution
aliases: ["marginal pmf", "marginals"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Marginal Distribution

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=25|class notes 2 Sep (proof of linearity)]].

> [!intuition] In one picture
> Forget one variable: sum the joint table along the other.

> [!key] Definition
> $P[X_1=a_i]=\sum_jp(a_i,b_j)$, $P[X_2=b_j]=\sum_ip(a_i,b_j)$ (third axiom, since $\{X_2=b_j\}$ partition the space).

The marginals do not determine the joint: the sum and max of two dice and an independent pair with the same marginals share row and column totals but differ in the cells. Independence is exactly "joint = product of marginals".

Used in: [[PR04 Joint Distributions Expectation and Variance]]. Related: [[Joint Distribution]] · [[Law of Total Probability]] · [[Independence of Random Variables]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
