---
title: Speed of Sound
aliases: ["Laplace correction", "sound speed"]
subject: thermo
type: concept
scope: [extra-book, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, extra/book, extra/beyond, src/lecture-notes, status/draft]
---
# Speed of Sound

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Zemansky §5.7 ([[Heat and thermodynamics an intermediate textbook (Mark Waldo Zemansky Richard Dittman) (z-library.sk, 1lib.sk, z-lib.sk).pdf#page=141|PDF p.141]]). · 🔵 **extra · beyond:** numbers.

> [!intuition] In one picture
> Sound oscillations are too fast for heat to equalise, so the gas stiffens adiabatically.

> [!key] Definition
> $c=\sqrt{K_S/\rho}=\sqrt{\gamma P/\rho}=\sqrt{\gamma RT/M}$ with the adiabatic bulk modulus $K_S=\gamma P$ (Laplace); Newton's isothermal $\sqrt{RT/M}$ is a factor $\sqrt\gamma$ too small.

## Numbers
Air $331.3$ m s$^{-1}$ at 0 °C, $343.2$ at 20 °C ($\propto\sqrt T$, independent of $P$); helium at 20 °C $1007$ m s$^{-1}$; CO$_2$ $\approx268$ m s$^{-1}$. $c=1/\sqrt{\rho\kappa_S}$ with $\kappa_S=\kappa_T/\gamma$.

> [!pitfall] Which compressibility
> Very slow oscillations would be isothermal; audible sound is adiabatic.

Used in: [[TH03 The Ideal Gas and Adiabatic Processes]]. Related: [[Ratio of Specific Heats]] · [[Reversible Adiabatic Process]] · [[Ruchhardt Method]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Continued in Part II (added 2026-10-30)
- Derived from the linearised Euler equations of kinetic theory, $c=\sqrt{5k_BT/3m}$ for a monatomic gas ($\gamma=\tfrac53$), with viscous and thermal damping at first order: [[SM04 Kinetic Theory and the Boltzmann Equation]] §9, §11 ([[Hydrodynamic Modes]]).
