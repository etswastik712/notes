---
title: Mutual Information
aliases: ["total correlation", "subadditivity of entropy"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Mutual Information

> [!info] Source
> [[SM01 Probability Large Numbers and Information]] §7.5; the chain rule and data-processing inequality are standard (Shannon 1948).

> [!intuition] In one picture
> How much two variables tell you about each other: the relative entropy of their joint law to the product of the marginals.

> [!key] Key facts
> $I(X;Y)=S(X)+S(Y)-S(X,Y)=D\big(p_{XY}\|p_Xp_Y\big)\ge0$; $S(X,Y)=S(X)+S(Y|X)$; data processing $I(X;g(Y))\le I(X;Y)$. For $N$ variables the gap $\sum S_i-S_{\rm joint}\ge0$ is the total correlation.

> [!example] Channel (recomputed)
> Binary symmetric channel, flip $0.1$: $I=0.531$ bit $=$ capacity. In kinetic theory the Boltzmann entropy exceeds the Gibbs entropy by exactly this kind of correlation term ([[H-Theorem]]).

Used in: [[SM01 Probability Large Numbers and Information]], [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[Relative Entropy]] · [[Shannon Entropy]] · [[Molecular Chaos]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
