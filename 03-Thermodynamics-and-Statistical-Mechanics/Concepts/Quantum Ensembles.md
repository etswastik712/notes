---
title: Quantum Ensembles
aliases: ["quantum canonical ensemble", "quantum microcanonical ensemble", "canonical density matrix"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Quantum Ensembles

> [!info] Source
> Kardar §6.5 (p. 172); Pathria §5.1–5.2 (pp. 115–121); Huang §8.2–8.3 (pp. 174–178); [[SM08 Quantum Ensembles and Identical Particles]] §2.

> [!intuition] In one picture
> The classical phase-space density is replaced by a density matrix: a function of $\hat H$ (and $\hat N$) for equilibrium, with every sum over states becoming a trace.

> [!key] Key facts
> microcanonical $\hat\rho=\hat\Pi_{E,\delta E}/\Omega$; canonical $\hat\rho=e^{-\beta\hat H}/Z$, $Z=\mathrm{Tr}\,e^{-\beta\hat H}$; grand canonical $\hat\rho=e^{-\beta(\hat H-\mu\hat N)}/\mathcal Z$ (trace over Fock space). Each maximises $-\mathrm{Tr}\hat\rho\ln\hat\rho$ under its constraints. Non-interacting identical particles: $Z_N=\frac1N\sum_{l=1}^N(\pm1)^{l-1}Z_1(l\beta)Z_{N-l}$ ($+$ bosons, $-$ fermions).

> [!example] Checked (recomputed)
> Levels $\varepsilon_k=k$ ($k=0..11$), $\beta=0.7$: $Z_2$ (bosons) $=2.63572791$, $Z_2$ (fermions) $=1.30841716$, $Z_3$ (bosons) $=3.00336285$, $Z_3$ (fermions) $=0.36734071$, identical by brute-force enumeration and by the recursion.

Used in: [[SM08 Quantum Ensembles and Identical Particles]]. Related: [[Density Matrix]] · [[Canonical Ensemble]] · [[Microcanonical Ensemble]] · [[Grand Canonical Ensemble]] · [[Von Neumann Entropy]] · [[Partition Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
