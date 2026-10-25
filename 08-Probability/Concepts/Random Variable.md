---
title: Random Variable
aliases: ["rv", "discrete random variable"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Random Variable

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=17|class notes 20 Aug]].

> [!intuition] In one picture
> A number attached to the outcome of an experiment, so that you can ignore details you do not care about (the sum of the dice, not the dice).

> [!key] Definition
> A **random variable** is a real-valued function $X:S\to\mathbb R$ on the sample space. It is **discrete** if it takes at most countably many values, **continuous** if its cdf is continuous (with a density).

## Same distribution is not equality
Two dice $X_1,X_2$ have the same distribution (uniform on $\{1,\dots,6\}$) but $X_1\neq X_2$ as functions on the 36-point space. Several random variables must live on one sample space to have a **joint** distribution ([[Joint Distribution]]).

> [!example] Binomial as a function
> Toss a coin $n$ times; $X$ = number of heads is a function of the sequence, taking values $0,\dots,n$ ([[Binomial Distribution]]).

Used in: [[PR03 Discrete Random Variables and Distributions]]. Related: [[Probability Mass Function]] · [[Cumulative Distribution Function]] · [[Indicator Random Variable]] · [[Continuous Random Variable]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
