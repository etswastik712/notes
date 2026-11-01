---
title: Gibbs Entropy
aliases: ["fine-grained entropy", "ensemble entropy", "S = -k int rho ln rho"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Gibbs Entropy

> [!info] Source
> Gibbs (1902), Kardar §4.2; [[SM06 Entropy Information and the Arrow of Time]] §1.

> [!intuition] In one picture
> The entropy of *our probability distribution* over microstates, not of the microstate itself.

> [!key] Key facts
> $S_G=-k_B\int\rho\ln\rho\,\mathrm d\Gamma$; constant under Hamiltonian flow (Liouville); $=k_B\ln\Omega$ microcanonical; $=k_B\ln Z+\langle E\rangle/T$ canonical; $S_G\le S_{\rm cg}$ with $S_{\rm cg}-S_G=kD(\rho\|\bar\rho)$.

> [!pitfall] Gibbs entropy does not increase
> Only the coarse-grained entropy does (cat map: slope $\lambda=0.962$ per step); see [[Arnold Cat Map]].

Used in: [[SM06 Entropy Information and the Arrow of Time]]. Related: [[Boltzmann Entropy]] · [[Shannon Entropy]] · [[Liouville's Theorem]] · [[Von Neumann Entropy]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
