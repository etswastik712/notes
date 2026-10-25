---
title: Axioms of Probability
aliases: ["Kolmogorov axioms", "probability axioms"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Axioms of Probability

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=4|class notes 6 Aug, pp.4–6]], [[ilovepdf_merged-1.pdf#page=7|12 Aug]].

> [!intuition] In one picture
> Probability is a way of assigning non-negative weights to events so that the whole space weighs 1 and disjoint pieces add.

> [!key] Definition
> A probability assigns to each event $E$ a number $P(E)$ with (1) $0\le P(E)\le1$; (2) $P(S)=1$; (3) for pairwise disjoint $E_1,E_2,\dots$: $P\big(\bigcup_iE_i\big)=\sum_iP(E_i)$.

## What follows from them
- $P(\varnothing)=0$: $1=P(S\cup\varnothing)=1+P(\varnothing)$. Hence finite additivity.
- $P(E^c)=1-P(E)$.
- $E\subset F\Rightarrow P(F)=P(E)+P(F\setminus E)\ge P(E)$ (monotonicity).
- $P(E\cup F)=P(E)+P(F)-P(E\cap F)$ ([[Inclusion-Exclusion Principle]]).

## Why axioms
The frequentist definition $P(E)=\lim n(E)/n$ leaves open whether the limit exists and is the same for every sequence of trials; the **naive** definition needs equally likely outcomes. The axioms (Kolmogorov, 1933) say only what any consistent assignment must satisfy; $P(\cdot\mid F)$ satisfies them too ([[Conditional Probability]]).

> [!example] Complement
> Ten slots, three courses placed at random: $P(\text{some two share})=1-\frac{10\cdot9\cdot8}{10^3}=0.28$.

Used in: [[PR01 Counting and the Axioms of Probability]]. Related: [[Sample Space and Events]] · [[Conditional Probability]] · [[Continuity of Probability]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
