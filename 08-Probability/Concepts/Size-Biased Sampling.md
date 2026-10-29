---
title: Size-Biased Sampling
aliases: ["inspection paradox", "length-biased sampling"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Size-Biased Sampling

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=21|class notes 27 Aug, buses]], [[Practice problems 4th September 2026.pdf#page=2|sheet 4 Sep, problem 8]].

> [!intuition] In one picture
> Picking a person (or child) rather than a group favours the big groups.

> [!key] Definition
> If a group of size $k$ is chosen with probability proportional to $k$ (an element picked uniformly), $P[\text{size}=k]\propto k\,P_{\rm group}(k)$ and the mean is $E[K^2]/E[K]\ge E[K]$.

Buses of 36, 40, 44: random bus $40$; random student's bus $40.27$. Town of 100 families (30, 50, 20 with 1, 2, 3 children): a child's birth rank, family first: $E=1.45$; child first (190 children): $\frac{100}{190},\frac{70}{190},\frac{20}{190}$, $E=1.579$. Same effect: classes look larger to students, friends have more friends than you do.

Used in: [[PR03 Discrete Random Variables and Distributions]], [[PR04 Joint Distributions Expectation and Variance]]. Related: [[Expectation]] · [[08-Probability/Concepts/Variance|Variance]] · [[Linearity of Expectation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
