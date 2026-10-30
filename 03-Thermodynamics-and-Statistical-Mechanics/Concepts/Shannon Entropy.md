---
title: Shannon Entropy
aliases: ["information entropy", "entropy of a distribution", "Shannon information"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Shannon Entropy

> [!info] Source
> Kardar §2.7 (pp.50–52); [[SM01 Probability Large Numbers and Information]] §7.

> [!intuition] In one picture
> The average surprise of a random outcome, or $\tfrac1N\ln$(number of typical sequences) of a long message.

> [!key] Key facts
> $S[p]=-\sum_ip_i\ln p_i$ ($\log_2$ gives bits); $0\le S\le\ln M$, maximal for the uniform distribution; additive for independent variables; unchanged by relabelling; decreases under merging outcomes. Typical sequences number $e^{NS}$ (multinomial + Stirling).

> [!example] Numbers (recomputed)
> Fair coin 1 bit; fair die $\log_26=2.585$ bits; coin with $p=0.1$: $0.469$ bit, so $10^6$ flips need $4.69\times10^5$ bits; $N=1000$ flips: $\ln g\approx325$ nats against $1000\ln2=693$. When all $\Omega$ microstates are equally likely $S=\ln\Omega$ (Boltzmann); in general $-k_B\sum p\ln p$ is Gibbs's entropy ([[Statistical Entropy]]).

*Maximum entropy:* with $\langle F\rangle$ fixed, $p_i\propto e^{-\lambda F_i}$ — the Boltzmann factor.

Used in: [[SM01 Probability Large Numbers and Information]], [[SM03 The Canonical Ensemble]]. Related: [[Relative Entropy]] · [[Statistical Entropy]] · [[Entropy]] · [[Multinomial Coefficient]] · [[Boltzmann Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
