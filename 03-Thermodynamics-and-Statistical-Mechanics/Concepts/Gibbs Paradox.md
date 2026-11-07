---
title: Gibbs Paradox
aliases: ["Gibbs paradox", "entropy of mixing", "indistinguishability factor N!"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Gibbs Paradox

> [!info] Source
> Kardar §4.5 (p.107); Pathria §1.5–1.6; [[SM02 Phase Space Liouville and the Microcanonical Ensemble]] §7.

> [!intuition] In one picture
> Mixing two samples of the *same* gas should create no entropy, but a naive count says it does: the fix is that identical particles are indistinguishable.

> [!key] Key facts
> Without $1/N!$: $S(2V,2N)-2S(V,N)=2Nk_B\ln2\ne0$. With $\mathrm d\Gamma\to\mathrm d\Gamma/N!$ the entropy depends on $V/N$ and is extensive. Different gases: $\Delta S_{\rm mix}=-Nk_B\sum x_i\ln x_i$; identical gases: $0$.

> [!example] Numbers (recomputed)
> 1 mol He + 1 mol Ar: $2R\ln2=11.53$ J K$^{-1}$; air ($0.21$ O$_2$, $0.79$ N$_2$): $4.27$ J mol$^{-1}$K$^{-1}$ per mole; $x_i=\tfrac12$ gives $R\ln2=5.76$.

*Subtlety (Jaynes):* the mixing entropy is a step function of "different or not"; it depends on whether you can *measure* the difference. Quantum mechanics derives $1/N!$ from symmetrisation (SM08).

Used in: [[SM02 Phase Space Liouville and the Microcanonical Ensemble]]. Related: [[Sackur-Tetrode Equation]] · [[Statistical Entropy]] · [[Shannon Entropy]] · [[Chemical Potential]].

## Continued in Part II (added 2026-11-02)
- The quantum resolution: $1/N!$ is the identity term of the sum over $N!$ permutations in $Z_N$, and exchange terms give the first quantum correction ([[SM08 Quantum Ensembles and Identical Particles]] §5.1).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Brine Rejection]] (Climate): mixing and unmixing of salt and water: salinity and density bookkeeping by entropy and mass balance (recalled link).
