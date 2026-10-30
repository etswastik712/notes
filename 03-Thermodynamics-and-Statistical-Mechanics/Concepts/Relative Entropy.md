---
title: Relative Entropy
aliases: ["Kullback-Leibler divergence", "KL divergence", "Gibbs inequality"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Relative Entropy

> [!info] Source
> [[SM01 Probability Large Numbers and Information]] §7.3 (a standard result; proof by [[Jensen Inequality]]); used in [[SM03 The Canonical Ensemble]] §2.2.

> [!intuition] In one picture
> How many extra nats per symbol you pay for coding with the wrong distribution $q$ when the truth is $p$.

> [!key] Key facts
> $D(p\|q)=\sum_ip_i\ln(p_i/q_i)\ge0$, with equality iff $p=q$ (Gibbs' inequality; proof: $-D\le\ln\sum q_i\le0$ by Jensen). Against the uniform distribution $D=\ln M-S[p]$. Not symmetric, not a metric.

> [!example] Thermodynamic meaning
> For the Boltzmann distribution $p$ and any trial $q$: $F[q]-F=k_BT\,D(q\|p)\ge0$. The free energy is *minimised* by the canonical distribution and the excess is the relative entropy (SM03 §2.2): the basis of variational approximations (mean-field theory).
>
> Loaded die $p=(\tfrac12,\tfrac14,\tfrac18,\tfrac18)$ against uniform: $D=0.25$ bit $=2-1.75$.

Used in: [[SM01 Probability Large Numbers and Information]], [[SM03 The Canonical Ensemble]]. Related: [[Shannon Entropy]] · [[Jensen Inequality]] · [[Helmholtz Free Energy]] · [[Canonical Ensemble]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
