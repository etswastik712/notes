---
id: ph2113/2026-10-06-particle-in-a-box-notes
aliases: [PH2113 particle in a box notes]
tags: [ph2113, particle-in-a-box]
trust_tier: agent_written
---

# Particle in a box (lecture notes)

## Covered
The file is a handwritten scan whose text extraction is partly garbled; only what is legible is summarised.

- **Setup.** Potential $V(x)=0$ for $0<x<a$, $V=\infty$ elsewhere.
- **Classical solution.** A particle of fixed mass $m$ and momentum $p$ bounces around the box with speed $|p|/m$; higher energy means more bounces per unit time; any value of $p$ is allowed, so there is no quantisation of energy. Posed question: what is the classical probability density of finding the particle at some $x$?
- **Quantum solution.** For a well-behaved wavefunction, $\psi=0$ at all points outside $0\le x\le a$. Inside, $V=0$ and the TISE reads $-\frac{\hbar^2}{2m}\psi''=E\psi$, i.e. $\psi''=-k^2\psi$ with $k^2=2mE/\hbar^2$. Most general solution: $\psi(x)=A\sin kx+B\cos kx$. No quantisation yet.
- **Boundary conditions.** $\psi$ must be continuous at the walls: $\psi(0)=0$ and $\psi(a)=0$. At $x=0$: $B=0$, so $\psi=A\sin kx$. At $x=a$: $A\sin ka=0\Rightarrow ka=n\pi$, $n=1,2,3,\dots$ Only these values give physical solutions; the values are discrete, so the system is quantised.
- **Eigenfunctions and energies.** $\psi_n(x)=A_n\sin(n\pi x/a)$, $E_n=\frac{n^2\pi^2\hbar^2}{2ma^2}$; $E_1$ is the smallest unit of energy. Posed question: what happens when $a\to0$ and $a\to\infty$?
- **Normalisation.** $\int\psi_n^*\psi_n\,dx=1$ fixes $A_n$ (worked as $|A_n|^2\int_0^a\sin^2(n\pi x/a)\,dx=1$).
- **Time evolution of eigenstates.** $\Psi_n(x,t)=A_n\sin(n\pi x/a)\,e^{-iE_nt/\hbar}$, with $E_n=n^2\pi^2\hbar^2/2ma^2$; visualised for several $n$.
- **Orthogonality.** $\int\psi_m^*(x)\psi_n(x)\,dx=\delta_{mn}$ (Kronecker delta: 1 if $m=n$, 0 otherwise).
- **Observables / expectation values.** $\langle x\rangle$ for the $n$-th state follows from symmetry of the box about $a/2$; $\langle x^2\rangle$ is worked by substitution $y=n\pi x/a$ with $\sin^2y=\tfrac12(1-\cos2y)$ and integration by parts; $\langle p\rangle$ and $\langle p^2\rangle$ are started with $\hat p=-i\hbar\,d/dx$ (scan legible only in part). These are the quantities Tutorial I asks you to finish.

## From the post
Notes for the particle-in-a-box system.

## Files
- [Particle_in_a_box.pdf](https://drive.google.com/file/d/1fYAS-eOsb6G_TB27BbJRtfj4SAX04iXn/view?usp=drive_web): handwritten; extraction garbled, final expectation-value results not legible.

## Related
- [[06-quantum-mechanics/qm04-the-particle-in-a-box]]: your own notes on the same system
- [[06-quantum-mechanics/concepts/particle-in-a-box]]: your concept note
- [[ph2113/2026-10-06-tutorial-i-particle-in-a-box]]: the problem set built on this
- [[ph2113/2026-08-31-states-operators-measurements-notes]]: expectation values and time evolution in general
