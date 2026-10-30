---
title: Stirling's Approximation
aliases: ["Stirling formula", "ln N!"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Stirling's Approximation

> [!info] Source
> Kardar §2.6 (pp.49–50); [[SM01 Probability Large Numbers and Information]] §5.3.

> [!intuition] In one picture
> $N!$ is the area under $x^Ne^{-x}$, a sharp hump of width $\sqrt N$ at $x=N$: replace the hump by a Gaussian.

> [!key] Key facts
> $N!\simeq N^Ne^{-N}\sqrt{2\pi N}$, i.e. $\ln N!=N\ln N-N+\tfrac12\ln(2\pi N)+\tfrac1{12N}-\dots$ For thermodynamics $\ln N!\simeq N\ln N-N$ suffices.

> [!example] Accuracy (recomputed)
> $\ln N!$ against $N\ln N-N$: $N=10$: $15.104$ vs $13.026$ (13.8 % low); $N=100$: $363.739$ vs $360.517$ (0.89 % low); $N=1000$: $5912.128$ vs $5907.755$ (0.07 %). Adding $\tfrac12\ln2\pi N$ leaves errors of $0.0083$, $0.00083$, $0.000083$ (so $N!$ itself is off by $1/12N$: 0.83 %, 0.083 %, 0.0083 %).

*Used for:* the entropy of mixing, $\binom Nn\simeq e^{Ns(x)}$, the Sackur–Tetrode entropy, and the rate function of a coin.

Used in: [[SM01 Probability Large Numbers and Information]], [[SM02 Phase Space Liouville and the Microcanonical Ensemble]]. Related: [[Saddle Point Method]] · [[Multinomial Coefficient]] · [[Large Deviation Principle]] · [[Sackur-Tetrode Equation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
