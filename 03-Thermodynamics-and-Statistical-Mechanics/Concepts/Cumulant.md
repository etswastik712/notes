---
title: Cumulant
aliases: ["cumulants", "connected moments", "cumulant generating function"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Cumulant

> [!info] Source
> Kardar §2.2–2.5; written up in [[SM01 Probability Large Numbers and Information]] §2.

> [!intuition] In one picture
> Moments with the pieces that factorise subtracted off: what is left is the genuinely *joint* information, and it adds for independent variables.

> [!key] Key facts
> $K(t)=\ln\langle e^{tx}\rangle=\sum_n\kappa_nt^n/n!$. $\kappa_1=\mu$, $\kappa_2=\sigma^2$, $\kappa_3=\langle(x-\mu)^3\rangle$, $\kappa_4=\langle(x-\mu)^4\rangle-3\sigma^4$. For independent variables $\kappa_n(x+y)=\kappa_n(x)+\kappa_n(y)$; the Gaussian has only $\kappa_1,\kappa_2$; the Poisson has $\kappa_n=\lambda$ for all $n$.

> [!example] Energy cumulants from the partition function
> $\kappa_n(E)=(-1)^n\partial_\beta^n\ln Z$: $\kappa_2=k_BT^2C_V$, and for an ideal gas $\kappa_n=\tfrac{3N}2(n-1)!(k_BT)^n$ ([[SM03 The Canonical Ensemble]] §3.2). The central limit theorem is the statement that $\kappa_n$ of a sum of $N$ terms grows like $N$ while $\sigma^n$ grows like $N^{n/2}$.

> [!pitfall] Moments do not add
> Variances add for independent variables; fourth moments do not ($\langle x^4\rangle=\kappa_4+3\kappa_2^2$).

Used in: [[SM01 Probability Large Numbers and Information]], [[SM03 The Canonical Ensemble]]. Related: [[Moment Generating Function]] · [[Characteristic Function]] · [[Central Limit Theorem]] · [[Wick's Theorem]] · [[Partition Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
