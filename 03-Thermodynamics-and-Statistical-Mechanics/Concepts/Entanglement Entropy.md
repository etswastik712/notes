---
title: Entanglement Entropy
aliases: ["Page curve", "entropy of a subsystem of a pure state", "Schmidt decomposition"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Entanglement Entropy

> [!info] Source
> Page (1993), recalled; simulated in [[SM06 Entropy Information and the Arrow of Time]] §5.

> [!intuition] In one picture
> A whole that is perfectly known can have parts that are completely uncertain: the part's entropy is its ignorance of the rest.

> [!key] Key facts
> For pure $|\psi\rangle_{AB}=\sum\sqrt{\lambda_i}|a_i\rangle|b_i\rangle$: $S(\rho_A)=S(\rho_B)=-\sum\lambda_i\ln\lambda_i$. Singlet: $\ln2$. Page: random pure state, $d_A\le d_B$: $\langle S_A\rangle=\ln d_A-d_A/(2d_B)$.

> [!example] Simulation (recomputed)
> $N=12$ qubits, $m=6$: $3.659$ (formula $3.659$, max $4.159$); $m=3$: $2.0717$ vs $2.0716$.

Used in: [[SM06 Entropy Information and the Arrow of Time]]. Related: [[Von Neumann Entropy]] · [[Mutual Information]] · [[Canonical Ensemble]] · [[QM09 The Stern-Gerlach Experiment and Spin]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
