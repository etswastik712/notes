---
title: Grand Canonical Ensemble
aliases: ["grand ensemble", "Gibbs factor", "grand partition function", "constant-mu ensemble"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Grand Canonical Ensemble

> [!info] Source
> Kardar §4.9 (pp. 118–120); Pathria Ch. 4; Huang §7.3; Schroeder §7.1; [[SM05 The Grand Canonical Ensemble and Chemical Equilibrium]] §1–§3.

> [!intuition] In one picture
> A region of a big gas or a surface in contact with a vapour: it borrows both energy and particles, paying $E-\mu N$.

> [!key] Key facts
> $p_i=e^{-\beta(E_i-\mu N_i)}/\mathcal Z$, $\mathcal Z=\sum_Nz^NZ_N$, $z=e^{\beta\mu}$; $\Phi=-k_BT\ln\mathcal Z=F-\mu N=-PV$; $\langle N\rangle=k_BT\partial_\mu\ln\mathcal Z$; $\mathrm{Var}N=k_BT\partial_\mu\langle N\rangle=N^2k_BT\kappa_T/V$. Ideal gas: $\mathcal Z=e^{zV/\lambda^3}$, $N$ Poisson.

> [!example] Numbers (recomputed)
> $\langle N\rangle=3$: $P(0)=0.050$, $\sigma/\langle N\rangle=0.58$. Water at 20 °C: $\mathrm{Var}N/\langle N\rangle=0.062$. Energy variance of the ideal gas: $\tfrac{15}4N(kT)^2$ (canonical $\tfrac32N(kT)^2$).

Used in: [[SM05 The Grand Canonical Ensemble and Chemical Equilibrium]]. Related: [[Grand Potential]] · [[Chemical Potential]] · [[Fugacity]] · [[Number Fluctuations]] · [[Canonical Ensemble]] · [[Equivalence of Ensembles]].

## Continued in Part II (added 2026-11-02)
- Quantum version: trace over Fock space; $\ln\mathcal Z=-\epsilon\sum\ln(1-\epsilon ze^{-\beta\varepsilon_k})$ and $PV=\tfrac23E$ for any statistics: [[SM08 Quantum Ensembles and Identical Particles]] §5.2 ([[Ideal Quantum Gas]]).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
