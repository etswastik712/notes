---
title: Memoryless Property
aliases: ["memorylessness"]
subject: probability
type: concept
scope: [extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, extra/book, src/lecture-notes, status/draft]
---
# Memoryless Property

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Blitzstein and Hwang Ch. 4–5; follows from the geometric tail $q^n$ in the class notes.

> [!intuition] In one picture
> Having waited a while tells you nothing about how much longer you must wait.

> [!key] Definition
> $P[X>s+t\mid X>s]=P[X>t]$ for all $s,t\ge0$. Only the geometric (discrete) and exponential (continuous) distributions have it.

Exponential: $\frac{e^{-\lambda(s+t)}}{e^{-\lambda s}}=e^{-\lambda t}$. For $\lambda=0.5$, $s=2$, $t=3$: $0.2231$. Geometric: $P[X>m+n\mid X>m]=q^n$.

> [!pitfall] Not for a bus timetable
> A bus that runs every 10 minutes is not memoryless: the longer you have waited, the sooner it comes.

Used in: [[PR05 Continuous Random Variables]]. Related: [[Geometric Distribution]] · [[Exponential Distribution]] · [[Conditional Probability]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
