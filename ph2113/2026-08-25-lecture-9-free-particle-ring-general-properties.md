---
id: ph2113/2026-08-25-lecture-9-free-particle-ring-general-properties
aliases: [PH2113 Lecture 9, Continuous and discrete energy spectra]
tags: [ph2113, lecture, free-particle, ring, spectrum]
trust_tier: agent_written
---

# Lecture 9: Continuous and discrete energy spectra (2026-08-25)

## Covered
Source: Classroom, PH2113_Lecture9_FreeParticle_Ring_GeneralProperties.pdf (read in full). The post says the note has a few extra topics that will be covered in tutorial/class.

**1. TDSE to TISE.** For $V(x,t)=V(x)$ try $\Psi=\psi(x)T(t)$; dividing by $\psi T$:
$$i\hbar\frac1T\frac{dT}{dt}=-\frac{\hbar^2}{2m}\frac1\psi\frac{d^2\psi}{dx^2}+V(x)=E.$$
Then $T(t)=e^{-iEt/\hbar}$ and $-\frac{\hbar^2}{2m}\psi''+V\psi=E\psi$ (TISE). Definite-energy solution $\Psi=\psi(x)e^{-iEt/\hbar}$, $|\Psi|^2=|\psi|^2$ time independent: a stationary state.

**2. Free particle on a line.** $V=0$: $\psi''+k^2\psi=0$, $k^2=2mE/\hbar^2$, $\psi=Ae^{ikx}+Be^{-ikx}$. $e^{i(kx-\omega t)}$ moves to $+x$ (phase velocity $\omega/k$), $p=+\hbar k$; $e^{-i(kx+\omega t)}$ moves to $-x$, $p=-\hbar k$. Choosing $B=0$ is choosing a state, not a restriction. $E=\hbar^2k^2/2m=p^2/2m$. No boundary condition restricts $k$, so any $E\ge0$: **continuous spectrum**. Quantum mechanics does not automatically mean discrete energy. The plane wave is not normalisable; a localised particle is a wave packet of nearby $k$.

**3. Periodic boundary condition $x\equiv x+L$.** Same equation, but $\psi(x+L)=\psi(x)$: $e^{ikL}=1$,
$$k_n=\frac{2\pi n}{L},\ n=0,\pm1,\dots;\quad p_n=\frac{2\pi\hbar n}{L},\quad E_n=\frac{\hbar^2k_n^2}{2m}=\frac{2\pi^2\hbar^2}{mL^2}n^2.$$
The Schrödinger equation did not change; the condition on $\psi$ did.

**4. Higher dimensions.** $i\hbar\partial_t\Psi=-\frac{\hbar^2}{2m}\nabla^2\Psi+V(\mathbf r)\Psi$; free solution $Ae^{i(\mathbf k\cdot\mathbf r-\omega t)}$, $\mathbf p=\hbar\mathbf k$, $E=\hbar^2k^2/2m$.

**5. Particle on a ring (radius $R$).** Polar free TISE: $-\frac{\hbar^2}{2m}\left[\partial_r^2+\frac1r\partial_r+\frac1{r^2}\partial_\theta^2\right]\psi=E\psi$. With $r=R$ fixed: $-\frac{\hbar^2}{2mR^2}\psi''(\theta)=E\psi$. Define $\alpha^2=2mR^2E/\hbar^2$: $\psi''+\alpha^2\psi=0$, $\psi=Ae^{i\alpha\theta}+Be^{-i\alpha\theta}$ (opposite directions of travel). Single-valuedness $\psi(\theta+2\pi)=\psi(\theta)$ gives $e^{2\pi i\alpha}=1$, $\alpha=n\in\mathbb Z$:
$$\psi_n=Ae^{in\theta},\qquad E_n=\frac{\hbar^2n^2}{2mR^2}.$$
Since $E_n=E_{-n}$, opposite motions are degenerate. Schrödinger equation + boundary condition $\Rightarrow$ allowed energies.

**6. Comparison.**

| | Line | Ring |
|---|---|---|
| Coordinate | $x\in(-\infty,\infty)$ | $\theta\in[0,2\pi)$ |
| Solution | $e^{ikx}$ | $e^{in\theta}$ |
| Restriction | none | $\psi(\theta+2\pi)=\psi(\theta)$ |
| Label | $k$ continuous | $n$ integer |
| Energy | $\hbar^2k^2/2m$ | $\hbar^2n^2/2mR^2$ |
| Spectrum | continuous | discrete |

Central lesson: quantisation is not an extra rule; only some solutions satisfy the physical boundary conditions.

**7. Many solutions.** The equation plus $V$ gives a set of possible states (e.g. $\psi_1,\psi_2,\dots$ with $E_1,E_2,\dots$, sometimes also a continuous family), not one wavefunction; the preparation fixes which (e.g. the coefficients $A,B$).

**8. Linearity and superposition.** TDSE linear: $\Psi=c_1\Psi_1+c_2\Psi_2$ solves it (vector-space structure). Same energy: $c_1\psi_1+c_2\psi_2$ is a stationary state of energy $E$. Different energies: $\Psi=c_1\psi_1e^{-iE_1t/\hbar}+c_2\psi_2e^{-iE_2t/\hbar}$ solves the TDSE but has no single definite energy.

**9. Phase.** $\Psi'=e^{i\alpha}\Psi$ gives $|\Psi'|^2=|\Psi|^2$: the same physical state. Relative phase matters: $\psi_1+\psi_2$ and $\psi_1-\psi_2$ give different interference.

**10. Physically acceptable wavefunctions** (finite, nonsingular 1D potentials): (1) single-valued; (2) normalisable, $\int|\psi|^2dx=1$; (3) continuous; (4) continuous $\psi'$. Delta potentials and infinite walls need modified boundary-condition statements. "Allowed state?" differs from "stationary solution for this $V$?".

**11. Allowed potentials.** Real, time-independent, piecewise continuous (finite jumps fine, e.g. a step $0$ for $x<0$, $V_0$ for $x>0$); more singular ones postponed. For time-dependent $V(x,t)$ the TDSE holds but $\psi(x)e^{-iEt/\hbar}$ need not.

**12. General properties of energies.** (1) need not be discrete; (2) can become discrete (ring); (3) boundary conditions, single-valuedness, normalisability select the values; (4) real for ordinary closed systems (operator reason later); (5) different states can share an energy ($E_n=E_{-n}$); (6) a general state need not have definite energy. Logic: $V\to$ Schrödinger equation $\to$ candidate solutions; candidates + physical conditions $\to$ allowed states and energies.

**Next:** what happens when $V$ changes between regions, in particular $E<V$ in some region, leading to tunnelling.

## From the post
"Find attached todays lecture note for todays class. There are few extra topics in this note which will be covered in tutorial/class."

## Files
- [PH2113_Lecture9_FreeParticle_Ring_GeneralProperties.pdf](https://drive.google.com/file/d/1M0tJGGqYBWPOvZ_dWeg3ce1FFyzuSug9/view?usp=drive_web)
- Classroom post: https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODc1Nzk5MDgyNjg1

## Related
- [[ph2113/2026-08-24-lecture-8-uncertainty-wavefunctions-schrodinger]]: previous lecture; TISE and why energy is not automatically discrete
- [[ph2113/2026-08-27-tutorial-solutions-wavefunctions-uncertainty-schrodinger]]: problems 3 and 5 are the periodic/ring quantisation and phase material
- [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]]: allowed potentials, matching conditions and stationary-state problems
- [[ph2113/2026-10-06-particle-in-a-box-notes]]: another case where boundary conditions give a discrete spectrum

<!-- kurooto:materiald0a3dd1c -->
## Concepts in PH2113_Lecture9_FreeParticle_Ring_GeneralProperties
[[zettel/particle-in-a-box-time-evolution]], [[zettel/time-independent-schrodinger-equation]], [[zettel/free-particle-on-an-infinite-line]], [[zettel/free-particle-periodic-boundary-condition]], [[zettel/emergence-of-energy-quantization-from-boundary-conditions]], [[zettel/overall-phase-vs-relative-phase]], [[zettel/wave-function-physical-acceptability-conditions]], [[zettel/admissible-potentials-for-stationary-analysis]]
<!-- /kurooto:materiald0a3dd1c -->
