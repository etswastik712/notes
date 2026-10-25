---
title: Poisson Limit Theorem
aliases: ["law of rare events", "Poisson approximation"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Poisson Limit Theorem

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[ilovepdf_merged-1.pdf#page=21|class notes 27 Aug, 'derived in class']].

> [!intuition] In one picture
> Many tiny chances add up to a Poisson count.

> [!key] Definition
> For fixed $c>0$ and $k$: $\binom nk(\tfrac cn)^k(1-\tfrac cn)^{n-k}\to e^{-c}\frac{c^k}k!$ as $n\to\infty$.

## Proof
$\frac{c^k}{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k}\cdot(1-\tfrac cn)^n\cdot(1-\tfrac cn)^{-k}\to\frac{c^k}{k!}\cdot1\cdot e^{-c}\cdot1$. Via MGFs: $(1+\tfrac cn(e^t-1))^n\to e^{c(e^t-1)}$.

## How good
Total-variation distance to Poisson$(3.2)$: $0.0080$ ($n=100$), $0.00079$ ($n=1000$), $0.00008$ ($n=10^4$): falling like $1/n$, within Le Cam's bound $\le c^2/n$.

Used in: [[PR03 Discrete Random Variables and Distributions]], [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Poisson Distribution]] · [[Binomial Distribution]] · [[Moment Generating Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
