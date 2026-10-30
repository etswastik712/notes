---
title: Edgeworth Expansion
aliases: ["Gram-Charlier / Edgeworth series", "skewness correction to the CLT"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Edgeworth Expansion

> [!info] Source
> [[SM01 Probability Large Numbers and Information]] §4.4; standard asymptotic statistics.

> [!intuition] In one picture
> The central limit theorem plus its first corrections, in powers of $N^{-1/2}$, with Hermite polynomials multiplying the cumulants.

> [!key] Key facts
> $p(y)=\phi(y)\big[1+\frac{\gamma_1}{6\sqrt N}He_3(y)+\frac1N\big(\frac{\gamma_2}{24}He_4+\frac{\gamma_1^2}{72}He_6\big)+\dots\big]$; CDF: $\Phi-\frac{\gamma_1}{6\sqrt N}(y^2-1)\phi$. Berry–Esseen: $\sup|F_N-\Phi|\le0.48\rho/(\sigma^3\sqrt N)$.

> [!example] Poisson(10) (recomputed)
> CDF at $k=5$: exact $0.0671$, Gaussian $0.0774$, Edgeworth $0.0695$; worst error over the table $0.020\to0.0025$.

Used in: [[SM01 Probability Large Numbers and Information]]. Related: [[Central Limit Theorem]] · [[Cumulant]] · [[Probabilists' Hermite Polynomials]] · [[Poisson Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
