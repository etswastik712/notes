---
title: Barometric Formula
aliases: ["isothermal atmosphere", "exponential atmosphere", "Boltzmann atmosphere"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Barometric Formula

> [!info] Source
> Boltzmann factor for $U=mgz$ ([[SM03 The Canonical Ensemble]] §4.2); the hydrostatic route is [[CL06 Hydrostatic Balance and Vertical Structure]].

> [!intuition] In one picture
> Each molecule climbs against gravity at an energy cost $mgz$; the density falls by the Boltzmann factor.

> [!key] Key facts
> $n(z)=n_0e^{-z/H}$, $H=k_BT/mg=RT/Mg$. Air: $H=8.43$ km at 288 K, $7.46$ km at 255 K; half pressure at $H\ln2=5.85$ km. Each species has its own $H$ (CO$_2$ 5.55, N$_2$ 8.72, He 61, H$_2$ 121 km at 288 K).

> [!example] Check against the real atmosphere (recomputed)
> $p(5.5\ \text{km})/p_0$: 0.521 (isothermal 288 K), 0.479 (255 K), 0.498 (standard atmosphere); at 10 km: 0.306, 0.262, 0.261; Everest (8849 m): 31.0 kPa (255 K isothermal) vs 31.4 kPa standard. Above $\sim100$ km turbulent mixing stops and scale heights separate.

Used in: [[SM03 The Canonical Ensemble]]. Related: [[Scale Height]] · [[Hydrostatic Balance]] · [[Boltzmann Distribution]] · [[Ideal Gas Law]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
