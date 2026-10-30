---
title: Knudsen Number
aliases: ["Kn", "rarefaction", "free molecular flow"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Knudsen Number

> [!info] Source
> [[SM04 Kinetic Theory and the Boltzmann Equation]] §11.1; the expansion parameter of the continuum limit.

> [!intuition] In one picture
> How many mean free paths fit in the system: when it is $\ll1$ the gas is a fluid; when it is $\gg1$ the molecules fly like independent particles.

> [!key] Key facts
> $\mathrm{Kn}=\lambda/L$. Regimes (Schaaf–Chambré, quoted): $\lesssim0.01$ continuum (Navier–Stokes); $0.01$–$0.1$ slip (velocity slip and temperature jump $\sim\lambda$); $0.1$–$10$ transition (Boltzmann/DSMC); $>10$ free molecular. Von Kármán: $\mathrm{Kn}\sim\mathrm{Ma}/\mathrm{Re}$.

> [!example] Values (recomputed)
> Air, 1 atm ($\lambda=67$ nm): 1 µm pore $0.067$ (slip); 1 cm tube $6.7\times10^{-6}$. $\lambda=1$ cm at $0.68$ Pa (vacuum-flask regime). At 100 km $\lambda\approx0.14$ m: a 1 m satellite is in the transition regime.

Used in: [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[Mean Free Path]] · [[Navier-Stokes Equations]] · [[Boltzmann Equation]] · [[Péclet Number]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
