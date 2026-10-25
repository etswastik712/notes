---
title: Markov and Chebyshev Inequalities
aliases: ["Markov inequality", "Chebyshev inequality"]
subject: probability
type: concept
scope: [extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, extra/book, src/lecture-notes, status/draft]
---
# Markov and Chebyshev Inequalities

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Ross Ch. 8; Blitzstein and Hwang Ch. 10.

> [!intuition] In one picture
> Even knowing only a mean (or mean and variance) you can bound how much probability lies far away.

> [!key] Definition
> **Markov:** $X\ge0$: $P[X\ge a]\le\frac{E[X]}a$. **Chebyshev:** $P[|X-\mu|\ge k\sigma]\le\frac1{k^2}$.

Markov follows from $a\mathbf 1\{X\ge a\}\le X$; Chebyshev is Markov applied to $(X-\mu)^2$. They are loose: $k=2$: bound $0.25$ against $0.0455$ (normal) and $0.0498$ (Exp$(1)$); Markov for Exp$(1)$, $a=3$: $\frac13$ vs $0.0498$. They are used to prove the [[Law of Large Numbers]].

Used in: [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Law of Large Numbers]] · [[Variance]] · [[Expectation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
