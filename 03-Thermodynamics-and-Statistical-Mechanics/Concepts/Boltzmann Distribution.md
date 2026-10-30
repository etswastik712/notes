---
title: Boltzmann Distribution
aliases: ["Boltzmann factor", "Gibbs distribution", "canonical distribution"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Boltzmann Distribution

> [!info] Source
> Kardar §4.6 (p.110); Pathria §3.1–3.2; [[SM03 The Canonical Ensemble]] §1; earlier sketch in [[TH06 From Kinetic Theory to Statistical Mechanics]] §6.

> [!intuition] In one picture
> A state of energy $E$ is $e^{-E/k_BT}$ times as likely as one of zero energy, because the bath has that many fewer ways to arrange itself.

> [!key] Key facts
> $p_\mu=e^{-\beta E_\mu}/Z$, $Z=\sum_\mu e^{-\beta E_\mu}$. Derivation: $p\propto\Omega_R(E-E_\mu)=e^{S_R(E-E_\mu)/k}\simeq e^{S_R/k}e^{-E_\mu/kT}$. Levels with degeneracy $g$: $p(\text{level})=g\,e^{-\beta\epsilon}/Z$. It is also the maximum-entropy distribution at fixed $\langle E\rangle$.

> [!example] Two faces of one factor
> $\tfrac12mv^2$ gives the Maxwell speed law; $mgz$ gives the barometric law; $\mp\mu_BB$ gives the paramagnet's $\tanh$ ([[Barometric Formula]], [[Curie Law]]).

Used in: [[SM03 The Canonical Ensemble]]. Related: [[Canonical Ensemble]] · [[Partition Function]] · [[Maxwell-Boltzmann Distribution]] · [[Shannon Entropy]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
