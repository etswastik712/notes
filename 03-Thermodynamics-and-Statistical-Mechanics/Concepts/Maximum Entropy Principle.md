---
title: Maximum Entropy Principle
aliases: ["MaxEnt", "Jaynes principle", "principle of least bias"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Maximum Entropy Principle

> [!info] Source
> Kardar §2.7 (p. 51); Jaynes (1957), recalled; [[SM01 Probability Large Numbers and Information]] §7.7 and [[SM03 The Canonical Ensemble]] §1.1.

> [!intuition] In one picture
> Of all distributions consistent with what you know, take the one that assumes nothing else: the one with the largest entropy.

> [!key] Key facts
> Maximise $S=-\sum p\ln p$ subject to $\sum p=1$, $\sum pf_a=F_a$: unique solution $p_i=e^{-\lambda\cdot f(i)}/Z$, $F_a=-\partial_{\lambda_a}\ln Z$, $S_{\max}=\ln Z+\lambda\cdot F$ (a Legendre transform). With $f=E$ it is the Boltzmann distribution, $\lambda=\beta$.

> [!example] Jaynes' die (recomputed)
> Mean 4.5: $\lambda=-0.3710$, $p=(0.054,0.079,0.114,0.165,0.240,0.348)$, $S=1.6136<\ln6=1.7918$.
> [!pitfall] Constraints are the physics
> The method assigns probabilities; that only the conserved quantities need be constrained is a statement about dynamics (mixing).

Used in: [[SM01 Probability Large Numbers and Information]], [[SM03 The Canonical Ensemble]]. Related: [[Shannon Entropy]] · [[Relative Entropy]] · [[Boltzmann Distribution]] · [[Legendre Transform]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
