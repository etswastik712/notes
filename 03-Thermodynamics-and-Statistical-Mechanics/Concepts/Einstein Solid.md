---
title: Einstein Solid
aliases: ["Einstein model", "two-state counting model", "stars and bars"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Einstein Solid

> [!info] Source
> Schroeder Ch. 2 (recalled); Einstein 1907; [[SM02 Phase Space Liouville and the Microcanonical Ensemble]] §8.

> [!intuition] In one picture
> $N$ identical oscillators sharing $q$ indivisible quanta: a model small enough to count by hand and big enough to show why energy flows to equalise temperature.

> [!key] Key facts
> $\Omega(N,q)=\binom{q+N-1}q$; $1/T=\partial_qS/\varepsilon=\frac{k_B}\varepsilon\ln\frac{q+N}q$. Two solids: most probable split $q_A=qN_A/(N_A+N_B)$, Gaussian width $\sigma^{-2}=\frac{N_A}{q_A(q_A+N_A)}+\frac{N_B}{q_B(q_B+N_B)}$; for equal solids with $q=2N$: $\sigma/q_A=1/\sqrt N$.

> [!example] $N_A=300$, $N_B=200$, $q=100$ (recomputed)
> Peak $q_A=60$, $\sigma=5.36$, $P(\text{peak})=0.0741$, $P(q_A=0)=3\times10^{-35}$, $\log_{10}\Omega_{\rm tot}=115.97$; at the peak $k_BT/\hbar\omega=0.558$ for both. By hand: $N_A=N_B=3$, $q=6$: products $28,63,90,100,90,63,28$ sum to $462=\binom{11}6$.

Used in: [[SM02 Phase Space Liouville and the Microcanonical Ensemble]]. Related: [[Microcanonical Ensemble]] · [[Multinomial Coefficient]] · [[QM05 The Harmonic Oscillator]] · [[Heat Capacity]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
