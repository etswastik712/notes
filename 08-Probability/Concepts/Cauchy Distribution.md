---
title: Cauchy Distribution
aliases: ["Cauchy", "Lorentz distribution"]
subject: probability
type: concept
scope: [extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, extra/book, src/lecture-notes, status/draft]
---
# Cauchy Distribution

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** the AI notes on moments (§1.4); Blitzstein and Hwang Ch. 7.

> [!intuition] In one picture
> A bell shape with tails so heavy that the average of many samples is no better than one sample.

> [!key] Definition
> $f(x)=\frac1{\pi(1+x^2)}$; $E|X|=\infty$, so there is no mean, no variance, no MGF; the mean of $n$ iid Cauchy variables is again Cauchy.

$E|X|=\frac2\pi\int_0^\infty\frac{x}{1+x^2}dx=\frac1\pi[\ln(1+x^2)]_0^\infty=\infty$. $P[|X|>3]=0.205$. Running sample means keep jumping (Figure PR6.1 B): five runs of $10^5$ draws gave means $-0.04,0.12,9.11,-0.60,-24.12$.

Used in: [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Law of Large Numbers]] · [[Central Limit Theorem]] · [[Moments of a Random Variable]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
