---
title: Phase Space Picture of the Oscillator
aliases: ["phase space", "x-p plane", "Bohr-Sommerfeld for the oscillator"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Phase Space Picture of the Oscillator

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond.**

> [!intuition] In one picture
> Plot position against momentum: a classical oscillator walks around a circle, a stationary quantum state is the whole ring.

> [!key] Definition
> In $\xi=x\sqrt{m\omega/\hbar}$, $\eta=p/\sqrt{m\hbar\omega}$: $H=\tfrac12\hbar\omega(\xi^2+\eta^2)$, a circle of radius $\sqrt{2E/\hbar\omega}$ traversed at angular speed $\omega$.

## Pictures
- **Classical:** $E$ fixes the radius; the point moves clockwise, $\langle x\rangle=A\cos\omega t$.
- **Fock state $|n\rangle$:** radius $\sqrt{2n+1}$, rotation-invariant ring, so $\langle x\rangle=\langle p\rangle=0$ forever.
- **Coherent state:** a fixed blob of area $\sim\hbar/2$ riding the circle (Fig. QM6.1 B).
- **Area rule:** the ellipse of energy $E$ in the $(x,p)$ plane encloses $2\pi E/\omega$; setting it equal to $(n+\tfrac12)h$ reproduces $E_n=(n+\tfrac12)\hbar\omega$ (a Bohr–Sommerfeld/WKB statement, exact for the oscillator).

## Dynamics as rotation
$\hat a(t)=\hat ae^{-i\omega t}$ is a rotation of the complex coordinate $\alpha=(\xi+i\eta)/\sqrt2$ by $-\omega t$. A quarter period swaps $x$ and $p$ (the Fourier transform, [[Fourier Invariance of Hermite Functions]]).

> [!pitfall] A point in phase space is not a quantum state
> $\Delta x\Delta p\ge\hbar/2$ forbids a sharp point; the smallest allowed blobs are the coherent states.

Used in: [[QM06 The Oscillator Toolbox]] §5. Related: [[Harmonic Oscillator]] · [[Coherent State]] · [[Heisenberg Picture]] · [[Correspondence Principle]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Continued in Part II (added 2026-10-30)
- The classical phase space and Liouville's theorem for the oscillator (one state per $\hbar\omega$ of area $h$): [[Phase Space]], [[SM02 Phase Space Liouville and the Microcanonical Ensemble]] (Problem 1).
