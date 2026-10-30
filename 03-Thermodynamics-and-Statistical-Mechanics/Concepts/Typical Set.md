---
title: Typical Set
aliases: ["asymptotic equipartition property", "AEP", "source coding theorem"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Typical Set

> [!info] Source
> [[SM01 Probability Large Numbers and Information]] §7.6; Shannon (1948).

> [!intuition] In one picture
> Almost all the probability sits on about $e^{NS}$ sequences that all have nearly the same probability $e^{-NS}$.

> [!key] Key facts
> $T_\epsilon=\{x:|-\tfrac1N\ln p(x)-S|<\epsilon\}$; $P(T_\epsilon)\to1$, $|T_\epsilon|\le e^{N(S+\epsilon)}$. Source coding: $NS/\ln2$ bits suffice and are necessary. Statistical mechanics: the microcanonical shell and the canonical ensemble have the same logarithm.

> [!example] $p=0.1$, $N=1000$ (recomputed)
> $P(T)=0.982$, $\ln|T|=367.8\le375.1$, against $693.1$ for all sequences.

Used in: [[SM01 Probability Large Numbers and Information]]. Related: [[Shannon Entropy]] · [[Large Deviation Principle]] · [[Multinomial Coefficient]] · [[Microcanonical Ensemble]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
