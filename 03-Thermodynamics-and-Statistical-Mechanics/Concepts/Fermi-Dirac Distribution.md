---
title: Fermi-Dirac Distribution
aliases: ["Fermi function", "FD statistics", "fermion occupation"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Fermi-Dirac Distribution

> [!info] Source
> Kardar §7.3; Pathria Ch. 5, 8; derived for one mode in [[SM05 The Grand Canonical Ensemble and Chemical Equilibrium]] §5; full theory SM08, SM12 (planned).

> [!intuition] In one picture
> A state holds zero or one fermion; the grand ensemble of that two-outcome system gives a smooth step at the chemical potential.

> [!key] Key facts
> $\langle n\rangle=1/(e^{(\varepsilon-\mu)/k_BT}+1)$, from $\mathcal Z_{\rm mode}=1+e^{-x}$; variance $\langle n\rangle(1-\langle n\rangle)$; $=\tfrac12$ at $\varepsilon=\mu$; $\to e^{-x}$ for $x\gg1$; at $T=0$ a step at the Fermi energy $\mu(0)=E_F$.

> [!example] Values (recomputed)
> $x=0.5,1,2,5$: $0.378,\ 0.269,\ 0.119,\ 0.00669$ (Boltzmann: $0.607,\ 0.368,\ 0.135,\ 0.00674$).

Used in: [[SM05 The Grand Canonical Ensemble and Chemical Equilibrium]]. Related: [[Bose-Einstein Distribution]] · [[Grand Canonical Ensemble]] · [[Langmuir Isotherm]] · [[Maxwell-Boltzmann Distribution]].

## Continued in Part II (added 2026-11-02)
- As the equilibrium of the Pauli-blocked collision integral (Uehling–Uhlenbeck) and from the grand canonical ensemble of identical fermions: [[SM08 Quantum Ensembles and Identical Particles]] §5.2 and §6 ([[Ideal Quantum Gas]], [[Quantum Boltzmann Equation]]).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Logistic Distribution]] (Probability): the Fermi function $1/(e^{x}+1)$ is the logistic function $\sigma(-x)$, the CDF of the logistic distribution: the same sigmoid describes the occupation of a fermion level, the polarisation $\tfrac12(1+\tanh)$ of a spin-1/2 paramagnet and a logistic response curve.
- [[Logistic Growth]] (Eco-Evo): the solution of logistic growth, $N(t)=K/(1+e^{-r(t-t_0)})$, is a Fermi function of time: carrying capacity plays the role of the single available state and $r$ of the inverse temperature.
