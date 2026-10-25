---
id: ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger
aliases: [PH2113 tutorial: Wave Functions, Potentials and the Schrödinger Equation]
tags: [ph2113, problem-set, agent_written]
trust_tier: agent_written
---

# Tutorial: Wave Functions, Potentials and the Schrödinger Equation (2026-09-13)

## Covered
Problem-oriented tutorial note with a short Fourier/Gaussian primer; core questions are Problems 1-6 (no new material, "bringing together some important aspects"). (Classroom: PH2113_wavefunctions_potentials_schrodinger_Tutorial.pdf)

**1. What a wave function must satisfy.**
- Ordinary normalisable state on the line: $\int|\psi|^2dx<\infty$ (=1 after normalisation); satisfies the problem's boundary conditions; single-valued.
- For $\hat H=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V$, enough smoothness for $\hat H\psi$ to make sense. For a finite, nonsingular $V$, energy eigenfunctions are continuous with continuous first derivative. Exceptions: an infinite wall changes the boundary condition; a $\delta$-potential allows a jump in $\psi'$.
- Square-integrability is the fundamental probability requirement; extra smoothness depends on $\hat H$. A square-integrable function can still have infinite or ill-defined kinetic energy. Normalisability, boundary conditions and the domain of $\hat H$ are separate issues.

**Problem 1 (wave-function detective), $a>0$:** decide if each can be an ordinary physical state: (a) $Ae^{-x^2/a^2}$; (b) $A/(1+x^2)^{1/4}$; (c) $Ae^{-x^2/a^2}e^{ix^3/a^3}$; (d) $A$ for $|x|<a$, 0 otherwise; (e) $Ae^{-|x|/a}$ (is the cusp at 0 automatically forbidden?); (f) $Ae^{ikx}$ on the whole line; (g) ring, $\psi(\phi)=Ae^{i\phi/2}$ with $\phi\equiv\phi+2\pi$. Practises: normalisability, continuity, periodic boundary conditions.

**2. Allowed potentials.**
- $V$ is normally real so $\hat H$ can be Hermitian/self-adjoint on a suitable domain; finite jumps are fine; $\delta(x)$ and infinite walls are useful idealisations with special matching/boundary conditions; a singular potential is not automatically forbidden, what matters is whether a consistent self-adjoint $\hat H$ exists. A complex potential models absorption/loss and is not the usual closed-system Hamiltonian.
- **Problem 2:** classify (i) $V_0\Theta(x)$, (ii) $\frac12m\omega^2x^2$, (iii) $\lambda\delta(x)$, (iv) $i\Gamma$ with $\Gamma\in\mathbb R$, (v) $-g/x^2$, (vi) $V=\infty$ outside $0<x<L$ as: ordinary and standard / idealised but standard / requiring extra care / not a standard closed-system potential. Then integrate $-\frac{\hbar^2}{2m}\psi''+V\psi=E\psi$ over $(x_0-\epsilon,x_0+\epsilon)$: (a) with only a finite jump in $V$, $\psi'$ is continuous; (b) for $V=\lambda\delta(x-x_0)$, $\psi'(x_0^+)-\psi'(x_0^-)=\frac{2m\lambda}{\hbar^2}\psi(x_0)$; (c) hence the cusp in 1(e) is not automatically unphysical.

**3. Structural facts about $i\hbar\,\partial_t\psi=\hat H\psi$.** It is linear (superpositions are solutions); if $\hat H$ is self-adjoint, evolution preserves total probability; an energy eigenstate changes only by a phase, so its probability density is time-independent.
- **Problem 3:** for $\hat H\phi_n=E_n\phi_n$, (a) show $\psi_n=\phi_ne^{-iE_nt/\hbar}$ solves the TDSE; (b) $|\psi_n|^2$ is time-independent; (c) for $\psi=c_1\phi_1e^{-iE_1t/\hbar}+c_2\phi_2e^{-iE_2t/\hbar}$ identify the time-dependent interference term in $|\psi|^2$ and its angular frequency.
- **Problem 4:** if $V'=V+V_0$, show $\psi'=e^{-iV_0t/\hbar}\psi$ solves the new equation; what happens to $|\psi|^2$, position probabilities and expectation values (the zero of potential energy does not matter).

**4. Fourier transform.** Convention: $\tilde\psi(k)=\frac1{\sqrt{2\pi}}\int e^{-ikx}\psi(x)dx$, $\psi(x)=\frac1{\sqrt{2\pi}}\int e^{ikx}\tilde\psi(k)dk$. A plane wave $e^{ikx}$ has $p=\hbar k$, so $\tilde\psi(k)$ says which momenta are present; a sharply localised packet needs many $k$ (origin of the uncertainty relation).
- **Problem 5:** ring of circumference $L$, $u_n=e^{i2\pi nx/L}/\sqrt L$, $\psi=\sum c_nu_n$, $c_m=\int_0^Lu_m^*\psi\,dx$. For $\psi=u_3$ find $c_m$ and what it says about momentum content.

**5. Gaussians.** Smooth, localised, easy to normalise, Fourier transform is again a Gaussian. Normalised form $\psi=(2\pi\sigma_x^2)^{-1/4}\exp(-x^2/4\sigma_x^2)$ with $\Delta x=\sigma_x$.
- **Problem 6:** using $\int e^{-ax^2+bx}dx=\sqrt{\pi/a}\,e^{b^2/4a}$ ($\mathrm{Re}\,a>0$), show $\tilde\psi(k)=(2\sigma_x^2/\pi)^{1/4}e^{-\sigma_x^2k^2}$; explain without another integral why narrower in $x$ means broader in $k$; with $p=\hbar k$, $\Delta p=\hbar/2\sigma_x$ and $\Delta x\Delta p=\hbar/2$; why the Gaussian is an important wave packet.

Take-away (from the sheet): a wave function is judged by normalisability, boundary conditions and the Hamiltonian, not appearance; potentials may be discontinuous or even singular if the Hamiltonian is defined consistently; Fourier analysis links spatial shape to momentum content.

## From the post
Find attached discussion/ Problem set for Tuesday Tutorial. No new material, just bringing together some important aspects. : Please note Tuesday tutorial will be in NLH only. Tutors will help you to solve problems. Please bring Pen paper.   Thursday will be in usual locations.

## Files
- [PH2113_wavefunctions_potentials_schrodinger_Tutorial.pdf](https://drive.google.com/file/d/1_SFgWn4KDCtiEwKUdZQQkzCZW__Ynrnw/view?usp=drive_web) (read in full; no solutions in it)
- Classroom post: https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODg0NzY5MzEwMjIy

## Related
- [[ph2113/2026-08-27-tutorial-solutions-wavefunctions-uncertainty-schrodinger]]: earlier tutorial on acceptable wavefunctions, ring and phase
- [[ph2113/2026-08-31-states-operators-measurements-notes]]: stationary states and time evolution (Problems 3-4)
- [[06-quantum-mechanics/concepts/fourier-transform-and-wave-packets]]: Problems 5-6
- [[06-quantum-mechanics/concepts/gaussian-wave-packet]]: Problem 6
- [[09-foundations/concepts/gaussian-integral]]: the integral formula used in Problem 6
