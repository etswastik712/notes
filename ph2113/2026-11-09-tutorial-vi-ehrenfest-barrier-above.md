---
id: ph2113/2026-11-09-tutorial-vi-ehrenfest-barrier-above
aliases: [Tutorial VI, PH2113 Tutorial 6]
tags: [ph2113, tutorial, ehrenfest, barrier]
trust_tier: agent_written
---

# Tutorial VI: second Ehrenfest equation and the barrier for $E>V_0$

## Covered
Two problems (Classroom: Tutorial6.pdf). The sheet is the problem statement only; the derivations below are worked out from it, not taken from a solution set.

**Problem 1: second Ehrenfest equation.** Show
$$\frac{d}{dt}\langle p\rangle=\frac{d}{dt}\int_{-\infty}^{\infty}\psi^*\Big(-i\hbar\frac{\partial}{\partial x}\Big)\psi\,dx=-\Big\langle\frac{dV}{dx}\Big\rangle,$$
and for $V=kx^2/2$ recover the classical equation $m\,\frac{d^2\langle x\rangle}{dt^2}=-k\langle x\rangle$.

Derivation (worked out here, for the TDSE $i\hbar\partial_t\psi=-\frac{\hbar^2}{2m}\psi''+V\psi$ with real $V(x)$):
- $\partial_t\psi=\frac{i\hbar}{2m}\psi''-\frac{i}{\hbar}V\psi$ and, taking the complex conjugate, $\partial_t\psi^*=-\frac{i\hbar}{2m}\psi^{*\prime\prime}+\frac{i}{\hbar}V\psi^*$.
- $\frac{d\langle p\rangle}{dt}=-i\hbar\int\big(\partial_t\psi^*\,\psi'+\psi^*\,\partial_t\psi'\big)dx$.
- The kinetic parts give $-\frac{\hbar^2}{2m}\int\big(\psi^{*\prime\prime}\psi'-\psi^*\psi'''\big)dx$. Since $\psi^{*\prime\prime}\psi'-\psi^*\psi'''=\frac{d}{dx}\big(\psi^{*\prime}\psi'-\psi^*\psi''\big)$, this is a boundary term $\big[\psi^{*\prime}\psi'-\psi^*\psi''\big]_{-\infty}^{\infty}$, which vanishes for a normalisable $\psi$ whose derivatives also vanish at infinity.
- The potential parts give $\int\big(V\psi^*\psi'-\psi^*(V\psi)'\big)dx=\int\big(V\psi^*\psi'-\psi^*V'\psi-\psi^*V\psi'\big)dx=-\int V'|\psi|^2dx=-\langle V'\rangle$.
- Hence $\frac{d\langle p\rangle}{dt}=-\langle dV/dx\rangle$ (the quantum analogue of $\dot p=-V'$; note $\langle V'(x)\rangle\ne V'(\langle x\rangle)$ in general).

Harmonic case: $V'=kx$, so $\frac{d\langle p\rangle}{dt}=-k\langle x\rangle$. With the first Ehrenfest equation $\frac{d\langle x\rangle}{dt}=\langle p\rangle/m$ (standard result, not stated on this sheet; derive it the same way from the TDSE), $m\frac{d^2\langle x\rangle}{dt^2}=-k\langle x\rangle$: exactly Newton's law for the mean, because $V'$ is linear in $x$ so $\langle V'\rangle=V'(\langle x\rangle)$.

**Problem 2: barrier $V=V_0$ for $-a<x<a$, 0 elsewhere, with $E>V_0$.** Particle incident from the left, with
$$\psi_I=Ae^{ik_0x}+Be^{-ik_0x}\ (x<-a),\quad \psi_{II}=Ce^{ikx}+De^{-ikx}\ (-a<x<a),\quad \psi_{III}=Fe^{ik_0x}\ (x>a),$$
$k_0=\sqrt{2mE}/\hbar$, $k=\sqrt{2m(E-V_0)}/\hbar$.

(a) Continuity of $\psi$ and $\psi'$ (finite jump in $V$) at $x=\pm a$ gives four conditions:
- $x=-a$: $Ae^{-ik_0a}+Be^{ik_0a}=Ce^{-ika}+De^{ika}$
- $x=-a$: $k_0\big(Ae^{-ik_0a}-Be^{ik_0a}\big)=k\big(Ce^{-ika}-De^{ika}\big)$
- $x=a$: $Ce^{ika}+De^{-ika}=Fe^{ik_0a}$
- $x=a$: $k\big(Ce^{ika}-De^{-ika}\big)=k_0Fe^{ik_0a}$

Solving the last two for $C,D$ (checked by substitution): $C=\tfrac12\big(1+\tfrac{k_0}{k}\big)Fe^{i(k_0-k)a}$, $D=\tfrac12\big(1-\tfrac{k_0}{k}\big)Fe^{i(k_0+k)a}$. Putting these in the first two gives $A$ and $B$ in terms of $F$, then $T=|F|^2/|A|^2$ (the same algebra as Problem 3 of [[ph2113/2026-11-02-tutorial-v-finite-well-double-well-transmission]], with the sign of $V_0$ reversed).

(b) Since $E>V_0$: $k^2=k_0^2-2mV_0/\hbar^2<k_0^2$, so $k<k_0$ and the wavelength inside, $2\pi/k$, is longer than outside, $2\pi/k_0$ (the particle is slower, kinetic energy $E-V_0$). Sketch of $\mathrm{Re}\,\psi$: in I a cosine of wavenumber $k_0$ whose envelope varies between $|A|-|B|$ and $|A|+|B|$ (incident plus reflected); in II a cosine of smaller wavenumber $k$, stretched; in III a pure cosine $|F|\cos(k_0x+\arg F)$ of constant amplitude and wavenumber $k_0$, joined to II with continuous value and slope. As $E\to V_0^+$: $k\to0$, the wavelength inside $\to\infty$ and $\psi_{II}$ flattens (nearly straight line inside). As $E\gg V_0$: $k/k_0\to1$, both wavelengths coincide, the barrier is a small perturbation, $T\to1$ and $B\to0$.

## From the post
Tutorials for this week.

## Files
- [Tutorial6.pdf](https://drive.google.com/file/d/1Decm-qgVSF9thoenbpJkfuV0YnH8-OBE/view?usp=drive_web): read in full (text only; no figures on it). Post: https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODk4MzUzNDUxNzk5

## Related
- [[ph2113/2026-11-02-tutorial-v-finite-well-double-well-transmission]]: derivation of $F/A$ and $T$ for $E>V_0$ over a well; same matching algebra
- [[ph2113/2026-11-04-barrier-notes]]: the same barrier for $E<V_0$ (exponentials, tunnelling); the $E>V_0$ case is $\kappa\to ik$
- [[ph2113/2026-10-27-finite-well-notes]]: scattering over a well, transmission resonances
- [[ph2113/2026-10-19-tutorial-iii-harmonic-oscillator-expectation-values]]: expectation values for the oscillator, where Ehrenfest applies
- [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]]: why $\psi,\psi'$ are continuous at a finite jump in $V$
- [[ph2113/2026-08-31-states-operators-measurements-notes]]: expectation values and time evolution
