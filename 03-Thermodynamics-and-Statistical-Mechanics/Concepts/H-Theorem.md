---
title: H-Theorem
aliases: ["Boltzmann H theorem", "H function", "Boltzmann entropy"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# H-Theorem

> [!info] Source
> Kardar §3.5 (pp. 71–75); Huang §4.1 (p. 73); [[SM04 Kinetic Theory and the Boltzmann Equation]] §6.

> [!intuition] In one picture
> A functional of the one-particle distribution that never increases under collisions and stops changing only at the Maxwell distribution: the arrow of time of a dilute gas.

> [!key] Key facts
> $H=\int f\ln f\,\mathrm d^3q\,\mathrm d^3p$, $\dot H=-\tfrac14\int w\,(f_1'f_2'-f_1f_2)\ln\frac{f_1'f_2'}{f_1f_2}\le0$ (since $(x-y)\ln(x/y)\ge0$). $\dot H=0\iff\ln f$ collision invariant $\iff$ Maxwell–Boltzmann. $S_B=-k_B\int f(\ln h^3f-1)$ increases; at equilibrium it is the **Sackur–Tetrode** entropy $Nk_B[-\ln n\lambda^3+\tfrac52]$.

> [!example] A solvable demonstration (recomputed)
> Kac collision model, $N=10^5$: $H$ falls from $-1.26$ to $-1.4195$ ($-\tfrac12\ln2\pi e=-1.4189$) monotonically; excess kurtosis $=-1.2e^{-t/4}$. For any $f$ with the same $n,\mathbf u,T$: $H[f]-H_{\rm MB}=D(f\|f_{\rm MB})\ge0$ ([[Relative Entropy]]).

Used in: [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[Boltzmann Equation]] · [[Molecular Chaos]] · [[Statistical Entropy]] · [[Relative Entropy]] · [[Irreversibility]] · [[Loschmidt and Zermelo Paradoxes]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
