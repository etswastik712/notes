---
title: Equivalence of Ensembles
aliases: ["ensemble equivalence", "thermodynamic limit equivalence"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Equivalence of Ensembles

> [!info] Source
> Kardar §4.6; Pathria §3.6; [[SM03 The Canonical Ensemble]] §3.

> [!intuition] In one picture
> A system in a bath has an energy so sharp ($1/\sqrt N$) that you cannot tell whether it was isolated or not.

> [!key] Key facts
> $Z=\int\mathrm dE\,\Omega e^{-\beta E}$: saddle at $\partial_ES=1/T$ gives $\ln Z=S(E^*)/k-\beta E^*+O(\ln N)$, so $F$ is the Legendre transform of $E-TS$; width $\delta E=\sqrt{k_BT^2C_V}$. **Fails** at first-order transitions (bimodal $E$; convex $S(E)$) and for long-range forces (microcanonical $C_V<0$).

> [!example] Ideal gas (exact)
> $\int E^{3N/2-1}e^{-\beta E}\mathrm dE=\Gamma(3N/2)\beta^{-3N/2}$; Stirling then reproduces $S/k-\beta E$ at $E^*=\tfrac32Nk_BT$ up to $O(\ln N)$.

Used in: [[SM03 The Canonical Ensemble]]. Related: [[Saddle Point Method]] · [[Legendre Transform]] · [[Microcanonical Ensemble]] · [[Canonical Ensemble]] · [[Thermodynamic Stability]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
