---
title: Fourier Invariance of Hermite Functions
aliases: ["Hermite functions Fourier transform", "oscillator in momentum space", "momentum-space oscillator wavefunction"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Fourier Invariance of Hermite Functions

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught (the $n=0$ case):** Fourier transform of a Gaussian is a Gaussian ([[PH2113_wavefunctions_potentials_schrodinger_Tutorial.pdf#page=3|Tutorial Note P5–P6]]). · 🔵 **extra · beyond:** all $n$.

> [!intuition] In one picture
> Position and momentum play the same role in $\hat H$, so the oscillator looks the same in both pictures, up to a phase.

> [!key] Definition
> $\tilde\psi_n(p)=(-i)^n(m\hbar\omega)^{-1/4}u_n\big(p/\sqrt{m\hbar\omega}\big)$ where $\psi_n(x)=(m\omega/\hbar)^{1/4}u_n(\xi)$: the Fourier transform has eigenvalues $(-i)^n\in\{1,-i,-1,i\}$ on the Hermite functions.

## Proof by ladders
In momentum space $\hat x=i\hbar\,\mathrm d/\mathrm dp$: $\hat a=\frac i{\sqrt2}(\eta+\partial_\eta)$ and $\hat a^\dagger=\frac{-i}{\sqrt2}(\eta-\partial_\eta)$, the position-space forms times $i$ and $-i$. The ground state ($\hat a\tilde\psi_0=0$) is $e^{-\eta^2/2}$; each $\hat a^\dagger$ contributes a factor $-i$.

## Numerical check
For $n=0,\dots,4$ at $p=0.4,1.3$ the ratio $\tilde\psi_n/\psi_n$ equals $1,-i,-1,i,1$ to five digits (Figure QM6.2 C: $\mathrm{Im}\,\tilde\psi_3$ lies on $\psi_3$).

## Meaning
The Fourier transform $\mathcal F$ commutes with $\hat H$; $\mathcal F^2=$ parity, $\mathcal F^4=\hat1$. Time evolution for a quarter period is $e^{-i\hat H T/4\hbar}$ with eigenvalue $e^{-i\pi/4}(-i)^n$: **a quarter period of oscillator time is a Fourier transform** (up to a global phase), the rotation of phase space by $90^\circ$ ($x\to p$) ([[Phase Space Picture of the Oscillator]], [[Time Evolution Operator]]).
Consequences: $\langle p^2\rangle_n=m\hbar\omega\langle\xi^2\rangle_n=(n+\tfrac12)m\hbar\omega$.

> [!pitfall] Phases depend on the transform convention
> With $e^{+ipx/\hbar}$ in the transform the eigenvalues become $i^n$; the physics (same shape) does not change.

Used in: [[QM06 The Oscillator Toolbox]] §5. Related: [[Fourier Transform and Wave Packets]] · [[Hermite Polynomials]] · [[Parity Operator]] · [[Gaussian Wave Packet]] · [[Parseval-Plancherel Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
