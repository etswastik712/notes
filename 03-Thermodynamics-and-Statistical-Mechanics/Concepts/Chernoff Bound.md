---
title: Chernoff Bound
aliases: ["exponential Markov inequality", "Chernoff-Cramer bound"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Chernoff Bound

> [!info] Source
> [[SM01 Probability Large Numbers and Information]] §6.3; a standard consequence of Markov's inequality.

> [!intuition] In one picture
> A rigorous, every-$N$ upper bound on a large deviation: the exponent is exactly the rate function.

> [!key] Key facts
> $P(\bar x\ge s)\le\inf_{t>0}e^{-N[ts-K(t)]}=e^{-NI(s)}$. Poisson: $P(X\ge k)\le e^{-\lambda}(e\lambda/k)^k$.

> [!example] Coin (recomputed)
> $P(\ge60\%)$: exact $0.0284$ vs bound $0.134$ ($N=100$); $1.36\times10^{-10}$ vs $1.80\times10^{-9}$ ($N=1000$); the ratio grows like $\sqrt N$ (missing prefactor).

Used in: [[SM01 Probability Large Numbers and Information]]. Related: [[Large Deviation Principle]] · [[Cumulant]] · [[Markov and Chebyshev Inequalities]] · [[Moment Generating Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
