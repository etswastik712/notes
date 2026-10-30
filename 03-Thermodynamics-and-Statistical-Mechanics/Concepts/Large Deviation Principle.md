---
title: Large Deviation Principle
aliases: ["rate function", "Cramér theorem", "large deviations"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Large Deviation Principle

> [!info] Source
> Kardar §2.6–2.7 (as exponentials of $N$); [[SM01 Probability Large Numbers and Information]] §6.

> [!intuition] In one picture
> The chance of a sizeable deviation from the mean is not a power of $N$ but $e^{-N\times\text{something}}$, and the something is an entropy deficit.

> [!key] Key facts
> $P(\bar x\approx s)\sim e^{-NI(s)}$ with $I(s)=\sup_t[ts-K(t)]$ (Legendre transform of the cumulant generating function). Fair coin: $I(m)=\ln2+m\ln m+(1-m)\ln(1-m)=\ln2-s(m)$, parabolic ($2(m-\tfrac12)^2$) only near $\tfrac12$.

> [!example] Tails (recomputed)
> $P(\ge60\%\text{ heads})$: $N=100$ exact $2.84\times10^{-2}$, Gaussian $2.87\times10^{-2}$, $e^{-NI}=0.134$; $N=1000$ exact $1.36\times10^{-10}$, Gaussian $1.56\times10^{-10}$, $e^{-NI}=1.8\times10^{-9}$ (prefactor and tail sum missing). $P(\text{all in left half})=2^{-N}$.

Physical meaning: $P=e^{-\Delta S/k_B}$ (Einstein's fluctuation formula): $I$ is the entropy deficit per particle.

Used in: [[SM01 Probability Large Numbers and Information]]. Related: [[Legendre Transform]] · [[Cumulant]] · [[Stirling's Approximation]] · [[Saddle Point Method]] · [[Binomial Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
