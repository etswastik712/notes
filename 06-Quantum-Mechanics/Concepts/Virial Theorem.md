---
title: Virial Theorem
aliases: ["virial", "2<T> = <x V prime>"]
subject: qm
type: concept
scope: [extra-book, extra-beyond]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, extra/beyond, src/book, src/own-notes, status/draft]
---
# Virial Theorem

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book** (a standard exercise in Griffiths). · 🔵 **extra · beyond:** the derivation from $\mathrm d\langle xp\rangle/\mathrm dt=0$ and the numerical checks.

> [!intuition] In one picture
> In a stationary state, kinetic and potential energy are locked together by the shape of the well.

> [!key] Definition
> $2\langle T\rangle=\Big\langle x\dfrac{\mathrm dV}{\mathrm dx}\Big\rangle$; for $V=c\,x^s$: $\ 2\langle T\rangle=s\langle V\rangle$.

## Derivation
$[\hat H,\hat x\hat p]=-i\hbar\hat p^2/m+i\hbar\hat xV'$, so $\frac{\mathrm d}{\mathrm dt}\langle\hat x\hat p\rangle=2\langle T\rangle-\langle xV'\rangle$ (Ehrenfest); in a stationary state it is $0$.

## Cases (finite-difference ground states, $\hbar=m=1$)
| $V$ | $s$ | $E_0$ | $2\langle T\rangle/\langle V\rangle$ |
|---|---|---|---|
| $x^2/2$ | 2 | 0.50000 | 2.0000 |
| $x^4$ | 4 | 0.66799 | 4.0000 |
| $\lvert x\rvert$ | 1 | 0.80862 | 1.0000 |

Oscillator: $\langle T\rangle=\langle V\rangle=\tfrac12E_n$. Coulomb ($s=-1$, in 3-D): $\langle T\rangle=-E$, $\langle V\rangle=2E$, i.e. $13.6$ and $-27.2$ eV for hydrogen.

> [!pitfall] Needs a stationary (or time-averaged) state
> For a superposition $\langle xp\rangle$ oscillates and the relation holds only on the time average.

Used in: [[QM06 The Oscillator Toolbox]] §6.3. Related: [[Ehrenfest Theorem]] · [[Harmonic Oscillator]] · [[Stationary State]] · [[Hydrogen Atom Stability]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
