---
title: Gibbs Canonical Ensemble
aliases: ["T-P ensemble", "isothermal-isobaric ensemble", "constant-pressure ensemble"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Gibbs Canonical Ensemble

> [!info] Source
> Kardar §4.8 (p.115); Pathria §4.6; [[SM03 The Canonical Ensemble]] §7.

> [!intuition] In one picture
> A canonical system whose volume is also allowed to fluctuate against a bath at constant $P$.

> [!key] Key facts
> $\mathcal Z_G(T,P,N)=\frac1{V_0}\int\mathrm dV\,e^{-\beta PV}Z(T,V,N)$, $G=-k_BT\ln\mathcal Z_G$, $\langle V\rangle=-\partial\ln\mathcal Z_G/\partial(\beta P)$, $\mathrm{Var}V=k_BTV\kappa_T$.

> [!example] Ideal gas (exact)
> $\mathcal Z_G\propto(k_BT/P)^{N+1}$: $\langle V\rangle=(N+1)k_BT/P$, relative fluctuation $1/\sqrt{N+1}$ (3.2 % for $N=1000$).

Used in: [[SM03 The Canonical Ensemble]]. Related: [[Gibbs Free Energy]] · [[Canonical Ensemble]] · [[Gibbs-Duhem Relation]] · [[Legendre Transform]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
