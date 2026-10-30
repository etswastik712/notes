---
title: One-Particle Distribution Function
aliases: ["f1", "single-particle density", "reduced distribution function"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# One-Particle Distribution Function

> [!info] Source
> Kardar §3.1, §3.3 (pp. 57, 62–63); written up in [[SM04 Kinetic Theory and the Boltzmann Equation]] §2.

> [!intuition] In one picture
> How many molecules sit in each cell of the six-dimensional $(\mathbf q,\mathbf p)$ space: a swarm described by its density, not by its members.

> [!key] Key facts
> $f_1(\mathbf p,\mathbf q,t)=\big\langle\sum_i\delta^3(\mathbf p-\mathbf p_i)\delta^3(\mathbf q-\mathbf q_i)\big\rangle$, $\int f_1=N$. Moments: $n=\int f$, $\mathbf u=\langle\mathbf v\rangle$, $\tfrac32k_BT=\langle\tfrac12mc^2\rangle$, $P_{\alpha\beta}=nm\langle c_\alpha c_\beta\rangle$, $\mathbf h=n\langle\tfrac12mc^2\mathbf c\rangle$. $f_s=\frac{N!}{(N-s)!}\int\rho\,\prod_{i>s}\mathrm dV_i$ is the $s$-particle density.

> [!example] Equilibrium
> $f_1=n(2\pi mk_BT)^{-3/2}e^{-m\mathbf c^2/2k_BT}$ ([[Maxwell-Boltzmann Distribution]]); then $P_{\alpha\beta}=nk_BT\delta_{\alpha\beta}$ and $\mathbf h=0$. Everything fluid-mechanical is a moment of $f_1$.

Used in: [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[BBGKY Hierarchy]] · [[Boltzmann Equation]] · [[Phase Space]] · [[Liouville's Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
