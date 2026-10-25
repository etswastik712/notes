---
title: Well-Ordering Principle
aliases: ["WOP", "least element principle"]
subject: analysis
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/analysis, type/concept, taught, src/lecture-notes, status/draft]
---
# Well-Ordering Principle

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Assignment-7.pdf#page=1|Assignment 7, Q4]].

> [!intuition] In one picture
> Every non-empty collection of positive integers has a smallest member.

> [!key] Definition
> Every non-empty subset of $\mathbb N$ has a least element. Equivalent to PMI and strong induction.

WOP $\Rightarrow$ PMI: if $S$ is inductive, $1\in S$, $S\ne\mathbb N$, take the least $m\notin S$; then $m-1\in S$ so $m\in S$. Used for: a subset of $\mathbb N$ is countable; density of $\mathbb Q$; $\sqrt2\notin\mathbb Q$ (least denominator $q$, then $\frac{2q-p}{p-q}$ has a smaller one). There is no integer in $(0,1)$.

Used in: [[PA05 Induction and the Number Systems]]. Related: [[Principle of Mathematical Induction]] · [[Countable Set]] · [[Natural Numbers]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
