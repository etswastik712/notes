---
title: Negative Temperature
aliases: ["negative absolute temperature", "population inversion temperature"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Negative Temperature

> [!info] Source
> Kardar §4.3 (p.102); [[SM02 Phase Space Liouville and the Microcanonical Ensemble]] §5.

> [!intuition] In one picture
> If a system's states run out (bounded energy), adding energy *reduces* its entropy: $\partial S/\partial E<0$, so $T<0$ — and it is hotter than any positive $T$.

> [!key] Key facts
> Two-level system: $x=n/N=1/(e^{\varepsilon/k_BT}+1)$; $S=Nk[-x\ln x-(1-x)\ln(1-x)]$ peaks at $x=\tfrac12$ ($T=\pm\infty$); for $x>\tfrac12$, $T<0$. Order from cold to hot: $T=0^+\to+\infty\to-\infty\to0^-$ (use $\beta=1/k_BT$ from $+\infty$ to $-\infty$). Heat flows from negative-$T$ to positive-$T$ systems.

> [!example] Numbers (recomputed)
> $x=0.25$: $s=0.5623$, $k_BT/\varepsilon=0.910$. $x=0.90$ (inverted): $k_BT/\varepsilon=-0.455$. Requires an upper-bounded spectrum and isolation from the lattice (nuclear spins in LiF, Purcell and Pound 1951; lasers).

Used in: [[SM02 Phase Space Liouville and the Microcanonical Ensemble]]. Related: [[Schottky Anomaly]] · [[Thermodynamic Temperature]] · [[Microcanonical Ensemble]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
