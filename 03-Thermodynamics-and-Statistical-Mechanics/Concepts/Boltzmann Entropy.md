---
title: Boltzmann Entropy
aliases: ["S = k ln W", "macrostate entropy", "Boltzmann formula"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft, quiz/th-tut3]
---
# Boltzmann Entropy

> [!info] Source
> Boltzmann (1877), Kardar §4.2, Blundell §14.5; [[SM06 Entropy Information and the Arrow of Time]] §1.

> [!intuition] In one picture
> How many microscopic ways the world can be while looking the way it looks at your resolution.

> [!key] Key facts
> $S_B(M)=k_B\ln|\Gamma_M|$ with $\Gamma_M$ the set of microstates compatible with macrostate $M$ (measure $\mathrm d\Gamma/N!h^{3N}$). Equilibrium macrostate $\approx$ the whole energy shell: $S_B=k_B\ln\Omega$. Coarse-grained: $S_{\rm cg}=\langle S_B\rangle+H[p_M]\ge S_G$.

> [!example] Two boxes, $N=100$ (recomputed)
> $S_B(n)/k_B=\ln\binom{100}n$: $66.78$ ($n=50$), $64.79$ ($60$), $58.64$ ($70$): deficits $0,\ -1.99,\ -8.14\,k_B$. All on one side: $1.6\times10^{-30}$.

Used in: [[SM06 Entropy Information and the Arrow of Time]], [[SM02 Phase Space Liouville and the Microcanonical Ensemble]]. Related: [[Gibbs Entropy]] · [[Statistical Entropy]] · [[Microcanonical Ensemble]] · [[Large Deviation Principle]].

## Continued in the vault (added 2026-11-04)
- Microstates, macrostates and multiplicity from first principles: [[TH09 Microstates Macrostates and Multiplicity]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
