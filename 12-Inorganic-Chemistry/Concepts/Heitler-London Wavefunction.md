---
title: Heitler-London Wavefunction
aliases: ["VB wavefunction of H2", "Heitler London", "covalent VB function"]
subject: chemistry
type: concept
scope: [taught, extra-beyond]
by: [slides, own-notes]
status: draft
tags: [subject/chemistry, type/concept, taught, extra/beyond, src/slides, src/own-notes, status/draft]
---
# Heitler-London Wavefunction

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[chem pre-ms .pdf#page=10|slide 10]]. · 🔵 **extra · beyond:** normalisation and overlap numbers.

> [!intuition] In one picture
> Two electrons, two nuclei, and no way to say which electron belongs to which: add both possibilities.

> [!key] Definition
> $\psi=N\,[\chi_A(1)\chi_B(2)+\chi_A(2)\chi_B(1)]$, $\ N=\dfrac1{\sqrt{2(1+S^2)}}$, $\ S=\langle\chi_A|\chi_B\rangle=e^{-R}\big(1+R+\tfrac{R^2}3\big)$ ($R$ in $a_0$, $1s$ orbitals).

## Numbers (checked by numerical integration)
$S=0.858,\ 0.753,\ 0.586,\ 0.189$ at $R=1,\ 1.4,\ 2,\ 4\,a_0$. At $r_e=0.74$ Å: $S=0.7534$, $N=0.5648$. Dissociation energy quoted on the slide: 4.5 eV $=434$ kJ/mol. Only **paired spins** (singlet, symmetric spatial function) bond; the triplet has the antisymmetric spatial function and repels.

> [!pitfall] The sum, not the product
> $\chi_A(1)\chi_B(2)$ alone treats the electrons as distinguishable; the exchange term $\chi_A(2)\chi_B(1)$ carries the bonding.

Used in: [[CH01 VSEPR and Valence Bond Theory]]. Related: [[Valence Bond Theory]] · [[QM01 From Waves to Probabilities]] · [[Normalisation of a Wavefunction]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
