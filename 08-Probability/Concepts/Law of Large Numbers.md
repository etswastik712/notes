---
title: Law of Large Numbers
aliases: ["LLN", "weak law of large numbers"]
subject: probability
type: concept
scope: [extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, extra/book, src/lecture-notes, status/draft]
---
# Law of Large Numbers

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Ross Ch. 8.

> [!intuition] In one picture
> Averages of many independent measurements settle down to the mean.

> [!key] Definition
> If $X_i$ are independent with mean $\mu$ and variance $\sigma^2$, $P[|\bar X_n-\mu|>\varepsilon]\le\frac{\sigma^2}{n\varepsilon^2}\to0$ (Chebyshev with $\mathrm{Var}[\bar X_n]=\sigma^2/n$).

Dice, $n=100$, $\varepsilon=0.25$: Chebyshev $0.467$; true $0.135$ (simulation). The Cauchy distribution has no mean, so the law fails (the mean of $n$ Cauchy variables is Cauchy).

Used in: [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Markov and Chebyshev Inequalities]] · [[Central Limit Theorem]] · [[Cauchy Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
