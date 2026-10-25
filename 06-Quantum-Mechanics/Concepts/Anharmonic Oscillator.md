---
title: Anharmonic Oscillator
aliases: ["x^4 perturbation", "anharmonic corrections", "Morse potential (qualitative)"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Anharmonic Oscillator

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond** (perturbation theory is not in the course; used here only to show what $\langle x^4\rangle$ is for).

> [!intuition] In one picture
> Real wells are not exact parabolas; the next term tilts the rungs unevenly and lets light excite overtones.

> [!key] Definition
> $\hat H=\hat H_{\rm osc}+\lambda\hat x^4$: $\ \Delta E_n^{(1)}=\lambda\langle n|\hat x^4|n\rangle=\lambda\big(\tfrac\hbar{2m\omega}\big)^2(6n^2+6n+3)$.

## Numbers ($\hbar=m=\omega=1$, $140\times140$ matrix)
$\lambda=0.001$: $E_0-\tfrac12=0.0007474$ vs $3\lambda/4=0.00075$; with the second-order term $-\tfrac{21}8\lambda^2$ (standard value, confirmed to $3\times10^{-8}$) $0.0007474$. $E_1-\tfrac32=0.0037296$ vs $15\lambda/4=0.00375$. $\lambda=0.002$: $0.0014897$ vs $0.0015$.

## Physics
A $+\lambda x^4$ **stiffens** the well (spacing grows with $n$); real bonds **soften** (a cubic or Morse term, spacing shrinks) and overtones lie slightly below integer multiples of the fundamental; $\hat x$ then mixes rungs, so $\Delta n=\pm2,\pm3$ appear ([[Selection Rules]]). The virial theorem still holds: $2\langle T\rangle=4\langle V\rangle$ for $V=x^4$ ([[Virial Theorem]]).

> [!pitfall] Perturbation theory is asymptotic
> The series in $\lambda$ does not converge (the $x^4$ coefficients grow factorially); it is useful only for small $\lambda$.

Used in: [[QM06 The Oscillator Toolbox]] §9. Related: [[Harmonic Oscillator]] · [[Oscillator Expectation Values]] · [[Selection Rules]] · [[Virial Theorem]] · [[Ehrenfest Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
