---
title: Microcanonical Ensemble
aliases: ["isolated system ensemble", "constant-E ensemble"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Microcanonical Ensemble

> [!info] Source
> Kardar §4.2 (p.98); Pathria §2.3; [[SM02 Phase Space Liouville and the Microcanonical Ensemble]] §4.

> [!intuition] In one picture
> An isolated box with fixed $E$, $V$, $N$: every microstate on the energy shell is equally likely, and the entropy is the log of their number.

> [!key] Key facts
> $\rho=\delta(E-\mathcal H)/\Omega$, $S=k_B\ln\Omega(E,V,N)$; $\tfrac1T=\partial_ES$, $\tfrac PT=\partial_VS$, $\tfrac\mu T=-\partial_NS$. Equilibrium between two systems maximises $\Omega_A\Omega_B$: equal $T$, $P/T$, $\mu/T$; the energy peak has width $\sigma^2=k_BT^2C_AC_B/(C_A+C_B)$. The shell width changes $S$ only by $O(\ln N)$.

> [!example] Exact examples
> Two-level: $S=Nk[-x\ln x-(1-x)\ln(1-x)]$ ([[Negative Temperature]]); ideal gas: $\ln\Sigma=S_{ST}/k-\ln(\pi\sqrt6N)$ ([[Sackur-Tetrode Equation]]); Einstein solids ([[Einstein Solid]]).

*Weakness:* no real system is isolated; [[Canonical Ensemble]] and [[Equivalence of Ensembles]] repair this.

Used in: [[SM02 Phase Space Liouville and the Microcanonical Ensemble]]. Related: [[Statistical Entropy]] · [[Density of States]] · [[Canonical Ensemble]] · [[Gibbs Paradox]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
