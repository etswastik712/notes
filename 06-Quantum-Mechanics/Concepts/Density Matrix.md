---
title: Density Matrix
aliases: [density operator, statistical operator]
subject: qm
type: concept
scope: [extra-book, extra-beyond]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, extra/beyond, src/book, src/own-notes, status/draft]
---
# Density Matrix

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book:** Sakurai §3.4 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf#page=189|PDF p.189 ff.]]). 🔵 **Extra · beyond:** the thermal case and numbers ([[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §6).

> [!intuition] In one picture
> The tool that describes an ensemble in which different atoms may be in different states: the oven beam, a thermal sample, one half of an entangled pair.

> [!key] Definition and key results
> $\rho=\sum_iw_i|\psi_i\rangle\langle\psi_i|$; $\langle A\rangle=\mathrm{Tr}(\rho A)$; $P(a)=\mathrm{Tr}(\rho P_a)$; Hermitian, $\mathrm{Tr}\rho=1$, non-negative. Spin-½: $\rho=\frac12(\mathbf1+\mathbf r\cdot\boldsymbol\sigma)$; purity $\mathrm{Tr}\rho^2=\frac12(1+r^2)$; entropy $-\mathrm{Tr}\rho\ln\rho$. Oven beam $\rho=\frac12\mathbf1$, $S=\ln2$.

Thermal: $\rho=e^{-H/k_BT}/Z$, giving $P=\tanh(\mu B/k_BT)$ ([[Canonical Ensemble]], [[Partition Function]]). Reduced state of a singlet: $\frac12\mathbf1$. Example $\mathbf r=(0.3,0,0.4)$: purity $0.625$, entropy $0.811$ bit, $P(+z)=0.70$.

> [!pitfall] Pitfall
> Different preparations can give the same $\rho$: $\frac12(|{+z}\rangle\langle{+z}|+|{-z}\rangle\langle{-z}|)=\frac12(|{+x}\rangle\langle{+x}|+|{-x}\rangle\langle{-x}|)$.

Used in: [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §6, §8, §11. Related: [[Pure and Mixed States]] · [[Bloch Sphere]] · [[Entanglement]] · [[Statistical Entropy]] · [[Expectation Value]].

## Continued in Part II (added 2026-11-02)
- The thermal and many-body version: $\hat\rho=e^{-\beta\hat H}/Z$, grand canonical $\hat\rho$ on Fock space and the exact recursion for identical particles ([[Quantum Ensembles]], [[SM08 Quantum Ensembles and Identical Particles]] §2).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
