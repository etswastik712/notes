---
title: Planck Mean Energy
aliases: ["Planck factor", "Bose–Einstein occupation"]
subject: thermo
type: concept
scope: [extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, extra/beyond, src/lecture-notes, status/draft]
---
# Planck Mean Energy

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** derived here: the bridge from the oscillator to Planck's law.

> [!intuition] In one picture
> A radiation mode is an oscillator; thermal averaging gives it less than $k_BT$ once the quantum is larger than the thermal energy.

> [!key] Definition
> $\bar\varepsilon(\omega)=\hbar\omega/(e^{\hbar\omega/k_BT}-1)$, mean occupation $\langle n\rangle=1/(e^x-1)$, $x=\hbar\omega/k_BT$. $x\to0$: $k_BT$; $x\gg1$: $\hbar\omega e^{-x}$.

## Numbers
15 µm mode at 288 K: $x=3.33$, $\langle n\rangle=0.037$, $\bar\varepsilon=0.123k_BT$. With $u(\omega)=(\hbar\omega^3/\pi^2c^3)/(e^x-1)$ (mode density stated): $a=\pi^2k_B^4/15\hbar^3c^3=7.566\times10^{-16}$ J m$^{-3}$K$^{-4}$; $\sigma=ac/4=5.670\times10^{-8}$; 288 K: $390$ W m$^{-2}$.

> [!pitfall] Zero-point energy dropped
> The $\tfrac12\hbar\omega$ per mode is infinite when summed and is not part of the radiation field one measures.

Used in: [[TH06 From Kinetic Theory to Statistical Mechanics]]. Related: [[Planck Law]] · [[Stefan-Boltzmann Law]] · [[Wien Displacement Law]] · [[Partition Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
