---
title: QM04 The Particle in a Box
aliases: [QM04, PH2113 box, Tutorial I]
subject: qm
type: chapter
chapter: 4
part: II
scope: [taught, extra-book, extra-beyond]
by: [lecture-notes]
status: draft
prereq: ["[[QM03 States Operators and Measurement]]"]
tags: [subject/qm, type/chapter, taught, extra/book, extra/beyond, src/lecture-notes, src/book, src/own-notes, status/draft]
---
# QM04 · The Particle in a Box

◀ [[QM03 States Operators and Measurement]] · [[Quantum Mechanics - Course Map|Course Map]] · [[QM05 The Harmonic Oscillator]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**: the handwritten lecture [[Particle_in_a_box.pdf|Particle in a box]] (10 pp.: setup and classical solution p.2, the quantum solution pp.3–4, energies and normalisation pp.5–6, time evolution and nodes p.7, orthogonality p.8, expectation values p.9), the box example of [[PH2113_states_operators_notes.pdf#page=9|States and Operators §8.2]] (p.9) and [[tutorial1.pdf|Tutorial I]] (6 Oct 2026).
> - §1 the box and its classical solution (p.2)
> - §2 the quantum solution: boundary conditions $\Rightarrow$ quantised energy (pp.3–5)
> - §3 normalisation, orthogonality, nodes and parity (pp.6–8)
> - §4 time evolution (p.7)
> - §5 expectation values and the uncertainty product (p.9; SO §8.2)
> - §6 Tutorial I: energy outcomes, a moving superposition, parity theorem, $E\ge V_{\min}$
>
> 🟡 **Extra · book**
> - the finite well, which relaxes the infinite wall (Griffiths §2.6); the correspondence limit of $|\psi_n|^2$ (Griffiths §2.2, [[Griffiths - Introduction to quantum mechanics.pdf#page=39|PDF p.39]])
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §5 the closed form $\Delta x\,\Delta p/\hbar=\sqrt{n^2\pi^2/12-1/2}$ for every $n$; §6 the oscillating $\langle x\rangle$ of the two-state superposition; a numerical finite-well check of $E>V_{\min}$ and parity; the macroscopic quantum number; all worked numbers (`scripts/qm_numbers.py`, `fig_qm04_*.py`)

> [!key] After this chapter you can
> - solve the TISE in the box and show that the **boundary conditions** $\psi(0)=\psi(a)=0$ quantise the energy, $E_n=n^2\pi^2\hbar^2/2ma^2$,
> - **normalise** $\psi_n=\sqrt{2/a}\sin(n\pi x/a)$, state orthonormality, count nodes and give the parity,
> - compute $\langle x\rangle$, $\langle x^2\rangle$, $\langle p\rangle$, $\langle p^2\rangle$ and show $\Delta x\,\Delta p>\hbar/2$ for **every** $n$,
> - evolve a **superposition** of box states, find the energy outcomes and probabilities, and describe how the density moves,
> - prove the Tutorial I theorems: symmetric $V\Rightarrow$ even/odd eigenfunctions, and $E\ge V_{\min}$,
> - explain the **zero-point (confinement) energy** and why the quantum density tends to the classical uniform one as $n\to\infty$.

> [!intuition] The one-sentence story
> A wave that must vanish at both walls fits only whole numbers of half wavelengths, so only certain wavelengths, momenta and energies survive: **the walls quantise the energy**, and a narrower box (smaller $a$) forces shorter wavelengths and higher energy ($E\propto1/a^2$). The lowest state cannot have zero energy because that would mean no wave at all.

## 1. The box and its classical solution
<span class="scope-taught">taught</span> *handwritten p.2 ([[Particle_in_a_box.pdf#page=2|p.2]])*

$$V(x)=\begin{cases}0,&0\le x\le a\\\infty,&\text{elsewhere.}\end{cases}$$
**Classically**, a particle of mass $m$ and fixed kinetic energy $p^2/2m$ bounces between the walls at speed $|p|/m$; higher energy means more bounces per unit time. **Any** value of $p$ is allowed: there is no quantisation of energy. The lecture's question, "what is the probability density of finding the particle at some $x$ with $0<x<a$?", has the classical answer **uniform**: because the speed is constant, the particle spends equal times in equal intervals, so $P_{\rm cl}(x)=1/a$.

## 2. The quantum solution
<span class="scope-taught">taught</span> *handwritten pp.3–5 ([[Particle_in_a_box.pdf#page=3|pp.3–5]])*

**Outside** the box ($x\le0$ or $x\ge a$), $V=\infty$ and the TISE can be satisfied by a well-behaved (finite, normalisable) wavefunction only if $\psi(x)=0$ there: the particle cannot be found beyond the walls.

**Inside** ($V=0$): $-\frac{\hbar^2}{2m}\psi''=E\psi$, i.e. $\psi''=-k^2\psi$ with $k=\sqrt{2mE}/\hbar$ (for $E>0$), so
$$\psi(x)=A\sin kx+B\cos kx ,$$
the most general solution, but **no quantisation yet**.

> [!key] The boundary conditions quantise
> $\psi$ must be continuous at the walls, so $\psi(0)=\psi(a)=0$.
> - $\psi(0)=B=0$, so $\psi=A\sin kx$.
> - $\psi(a)=A\sin ka=0\Rightarrow ka=n\pi$, so $k_n=\dfrac{n\pi}a$, $n=1,2,3,\dots$
> ($n=0$ gives $\psi\equiv0$, no particle; negative $n$ gives the same state up to a sign.) Hence
> $$\boxed{\ \psi_n(x)=A_n\sin\frac{n\pi x}a,\qquad E_n=\frac{\hbar^2k_n^2}{2m}=\frac{n^2\pi^2\hbar^2}{2ma^2}=n^2E_1,\quad E_1=\frac{\pi^2\hbar^2}{2ma^2}\ }$$

$E_1,E_2,E_3=E_1,\,4E_1,\,9E_1$: the levels spread as $n^2$ and the **lowest energy is not zero**. $E_1$ is the smallest unit of energy; the lecture asks what happens as $a\to\infty$ or $\hbar\to0$: $E_n\to0$ and the spacing $E_{n+1}-E_n=(2n+1)E_1\to0$, so the levels merge into a continuum (the free particle and the classical limit).

> [!pitfall] The discreteness is not an extra postulate
> The Schrödinger equation inside the box is the free-particle equation and has solutions for **every** $E>0$. Only those that vanish at both walls survive: **Schrödinger equation + boundary condition $\Rightarrow$ quantisation**, the same lesson as the ring in [[QM02 The Schrodinger Equation and Stationary States]].

## 3. Normalisation, orthogonality, nodes and parity
<span class="scope-taught">taught</span> *handwritten pp.5–8 ([[Particle_in_a_box.pdf#page=6|pp.6–8]])*

**Normalisation.** $\int_0^a|\psi_n|^2\mathrm dx=|A_n|^2\int_0^a\sin^2\frac{n\pi x}a\,\mathrm dx=|A_n|^2\,\frac a2=1$, using $\sin^2u=\tfrac12(1-\cos2u)$ and $\int_0^a\cos(2n\pi x/a)\mathrm dx=0$. So
$$\boxed{\ A_n=\sqrt{\frac2a},\qquad\psi_n(x)=\sqrt{\frac2a}\sin\frac{n\pi x}a\ }$$

**Orthonormality.** $\displaystyle\int_0^a\psi_m^*\psi_n\,\mathrm dx=\delta_{mn}$. For $m\ne n$ use $\sin A\sin B=\tfrac12[\cos(A-B)-\cos(A+B)]$: both cosines integrate to zero over $[0,a]$. Orthogonality of eigenfunctions with different eigenvalues is a general property of Hermitian operators ([[QM03 States Operators and Measurement]]); here it also lets us extract expansion coefficients $c_n=\int\psi_n^*\Psi\,\mathrm dx$.

**Nodes and parity.** $\psi_n$ has $n-1$ **nodes** (interior zeros): going up one level adds one node. About the **centre** $x=a/2$, $\psi_n$ is even for odd $n$ and odd for even $n$: parity $(-1)^{n+1}$ (the lecture draws "even" and "odd" families).

![[fig_qm04_box.png]]
*Figure QM4.1. A: the first four levels with $\psi_n$ drawn on each (scaled for visibility). B: $a|\psi_n|^2$ for $n=1,2,5$ against the classical uniform $1/a$ (dashed): the quantum density has zeros, but its local average tends to $1/a$ as $n$ grows. C: $\Delta x\,\Delta p/\hbar$ against $n$; the dashed line is the bound $1/2$.*

> [!example] Numbers: an electron in a nanometre box ($a=1$ nm)
> $E_1=\pi^2\hbar^2/2m_ea^2=6.02\times10^{-20}$ J $=0.376$ eV (a standard benchmark for confinement at the nanometre scale), $E_2=1.504$ eV, $E_3=3.384$ eV. The $1\to2$ gap is $3E_1=1.128$ eV, corresponding to a photon of wavelength $hc/\Delta E=1.10$ µm (near infrared). Halving the box quadruples every energy.

> [!example] Numbers: a marble (to see the classical limit)
> $m=1$ g in a box $a=10$ cm: $E_1=5.5\times10^{-63}$ J. At 1 cm s$^{-1}$ its kinetic energy is $5\times10^{-8}$ J, so $n=\sqrt{E/E_1}\approx3\times10^{27}$ and the fractional level spacing $\Delta E/E\approx2/n\approx7\times10^{-28}$. Quantisation is present but utterly unobservable: the **correspondence principle**.

## 4. Time evolution
<span class="scope-taught">taught</span> *handwritten p.7 ([[Particle_in_a_box.pdf#page=7|p.7]]); SO §9 ([[PH2113_states_operators_notes.pdf#page=10|p.10]])*

Each energy eigenstate evolves as
$$\Psi_n(x,t)=\psi_n(x)\,e^{-iE_nt/\hbar}=\sqrt{\frac2a}\sin\frac{n\pi x}a\;e^{-i\omega_nt},\qquad\omega_n=\frac{E_n}\hbar .$$
$|\Psi_n|^2=|\psi_n|^2$ is time-independent: a **stationary state**. The real part $\psi_n(x)\cos\omega_nt$ oscillates in amplitude (the lecture's dashed sketch shows the shape flipped sign at $t=\pi/\omega_n$) but the nodes do not move. A general state $\Psi=\sum_nc_n\psi_ne^{-iE_nt/\hbar}$ has constant probabilities $|c_n|^2$ for the energy outcomes ([[QM03 States Operators and Measurement]]); only the **relative phases** change.

## 5. Expectation values and the uncertainty product
<span class="scope-taught">taught</span> *handwritten p.9 ([[Particle_in_a_box.pdf#page=9|p.9]]); SO §8.2 ([[PH2113_states_operators_notes.pdf#page=9|p.9]])*

**Position.** $|\psi_n|^2$ is symmetric about $a/2$, so $\langle x\rangle=a/2$ for every $n$. Direct integration agrees (the lecture substitutes $y=n\pi x/a$, writes $\sin^2y=\tfrac12(1-\cos2y)$ and integrates $y\cos2y$ by parts):
$$\langle x\rangle=\frac2a\int_0^ax\sin^2\frac{n\pi x}a\,\mathrm dx=\frac a2 .$$
This is the **average over many measurements**; it does not say that every measurement finds the particle at $a/2$ (for $n=2$ the density is **zero** there).

**Position spread.**
$$\langle x^2\rangle=a^2\Big(\frac13-\frac1{2n^2\pi^2}\Big),\qquad(\Delta x)^2=\langle x^2\rangle-\frac{a^2}4=a^2\Big(\frac1{12}-\frac1{2n^2\pi^2}\Big).$$
(Recomputed symbolically; $n=1$: $\langle x^2\rangle=0.2827\,a^2$.) For large $n$, $\Delta x\to a/\sqrt{12}=0.2887a$, the value of a **uniform** distribution: again the classical limit.

**Momentum.** $\langle p\rangle=-i\hbar\int\psi_n\psi_n'\,\mathrm dx\propto\int\sin\cos\,\mathrm dx=0$ (a real standing wave is a superposition of $\pm p$ with equal weights). Since $\psi_n''=-k_n^2\psi_n$ inside,
$$\langle p^2\rangle=-\hbar^2\!\int\psi_n\psi_n''\,\mathrm dx=\hbar^2k_n^2=2mE_n,\qquad\Delta p=\frac{n\pi\hbar}a .$$

> [!key] The uncertainty product
> $$\Delta x\,\Delta p=\hbar\sqrt{\frac{n^2\pi^2}{12}-\frac12}\ \ >\ \frac\hbar2\quad\text{for every }n.$$
> $n=1$: $\Delta x=0.1808\,a$, $\Delta p=\pi\hbar/a$, $\Delta x\,\Delta p=0.568\,\hbar$ (just above $0.5\hbar$). $n=2$: $1.670\hbar$; $n=3$: $2.627\hbar$; the product grows roughly as $n$ because $\Delta p\propto n$ while $\Delta x$ saturates (Fig. QM4.1C). The box state is **not** a minimum-uncertainty state (only the Gaussian is).
> **Numerical check ($a=1$ nm, electron, $n=1$):** $\Delta x=1.81\times10^{-10}$ m, $\Delta p=3.31\times10^{-25}$ kg m s$^{-1}$, $\Delta x\,\Delta p=5.99\times10^{-35}$ J s, above $\hbar/2=5.27\times10^{-35}$ J s by the factor $0.568/0.5=1.14$.

> [!pitfall] Energy sharp, momentum not
> $\phi_n$ is an eigenstate of $\hat H$ but **not** of $\hat p$ ($\hat p\phi_n\propto\cos$): definite energy, uncertain momentum $\pm n\pi\hbar/a$ (average $0$). The commutator $[\hat H,\hat p]\ne0$ in the box because $V$ is not constant ([[QM03 States Operators and Measurement]]): the walls transfer momentum.

## 6. Tutorial I (6 October 2026)
<span class="scope-taught">taught</span> *[[tutorial1.pdf|Tutorial I]]; my solutions are checked against the AI worked solutions `quantum_notes.pdf`, which agree*

**Q1. $\langle x^2\rangle$ and $\Delta x\,\Delta p$ for the $n$-th state.** Done above: $\Delta x\,\Delta p=\hbar\sqrt{n^2\pi^2/12-1/2}$.

**Q2. Energy outcomes.** $\psi=\frac1{\sqrt3}(\psi_1+\psi_2+\psi_3)$. A measurement of $E$ gives $E_1$, $4E_1$ or $9E_1$, each with probability $\tfrac13$, and
$$\langle E\rangle=\tfrac13(1+4+9)E_1=\tfrac{14}3E_1=4.67E_1,\qquad\langle E^2\rangle=\tfrac13(1+16+81)E_1^2=32.67E_1^2,\ \ \Delta E=3.30E_1 .$$
(Fig. QM4.2C.) The average $4.67E_1$ is **not** one of the possible results.

**Q3. A superposition that sloshes.** $\psi(x,0)=\frac1{\sqrt2}(\psi_1+\psi_2)$. Then $\Psi(x,t)=\frac1{\sqrt2}\big(\psi_1e^{-iE_1t/\hbar}+\psi_2e^{-iE_2t/\hbar}\big)$ and, with $E_2=4E_1$ and real $\psi_n$,
$$|\Psi|^2=\tfrac12(\psi_1^2+\psi_2^2)+\psi_1\psi_2\cos\frac{3E_1t}\hbar,\qquad\langle x\rangle(t)=\frac a2-\frac{16a}{9\pi^2}\cos\frac{3E_1t}\hbar .$$
($\langle\psi_1|x|\psi_2\rangle=-16a/9\pi^2$; $16/9\pi^2=0.180$.) The requested times, with phase $\theta=3E_1t/\hbar$:

| $t$ | $\theta$ | cross term | picture | $\langle x\rangle$ |
|---|---|---|---|---|
| $0$ | $0$ | $+\psi_1\psi_2$ | piled on the **left** (peak near $0.3a$) | $0.320a$ |
| $\pi\hbar/2E_1$ | $3\pi/2$ | $0$ | symmetric two-hump | $0.500a$ |
| $\pi\hbar/E_1$ | $3\pi$ | $-\psi_1\psi_2$ | piled on the **right** (peak near $0.7a$) | $0.680a$ |
| $2\pi\hbar/E_1$ | $6\pi$ | $+\psi_1\psi_2$ | back to the **left**, the start | $0.320a$ |

![[fig_qm04_superposition.png]]
*Figure QM4.2. A: $a|\Psi|^2$ at the four times of Tutorial I. B: $\langle x\rangle(t)$ oscillates about the centre with amplitude $0.18a$ at the Bohr frequency $3E_1/\hbar$; dots mark the four times. C: the three energy outcomes of Q2 and their mean $14E_1/3$.*

The density oscillates with period $2\pi\hbar/3E_1$; the **full** wavefunction (including the global phase) repeats after $2\pi\hbar/E_1$, the common period of the two frequencies $E_1/\hbar$ and $4E_1/\hbar$. For the $a=1$ nm electron the density period is $2\pi\hbar/3E_1=3.7$ fs.

**Q4. If $V(x)$ is symmetric, eigenfunctions are even or odd.**

> [!derivation] Parity theorem
> Let $V(-x)=V(x)$ and $\hat H\psi=E\psi$. Replace $x\to-x$ in the TISE: $\mathrm d^2/\mathrm dx^2$ is unchanged and so is $V$, so $\psi(-x)$ solves the **same** equation with the same $E$ ($[\hat P,\hat H]=0$). Then $\psi_\pm=\psi(x)\pm\psi(-x)$ are solutions with definite parity. If the level is **non-degenerate**, $\psi(-x)=c\psi(x)$ and applying the reflection twice gives $c^2=1$, so $c=\pm1$: the eigenfunction is itself even or odd. If the level is degenerate (the free particle's $e^{\pm ikx}$) one can still **choose** parity eigenfunctions ($\cos,\sin$).
> For the box centred at $a/2$ the eigenfunctions alternate even, odd, even, … as in §3. (Griffiths Problem 2.1, [[Griffiths - Introduction to quantum mechanics.pdf#page=39|PDF p.39]].)

**Q5. Energy is bounded below by the minimum of the potential.**

> [!derivation] $E\ge V_{\min}$ by contradiction
> The TISE is real, so take $\psi$ real. Suppose $E<V_{\min}$. Then wherever $\psi\ne0$,
> $$\frac{\psi''}\psi=\frac{2m}{\hbar^2}\big(V-E\big)\ \ge\ \kappa_0^2=\frac{2m}{\hbar^2}(V_{\min}-E)>0 .$$
> Pick $x_0$ with $\psi(x_0)>0$. **If $\psi'(x_0)\ge0$:** while $\psi>0$, $\psi''\ge\kappa_0^2\psi>0$, so $\psi'$ increases strictly, $\psi$ keeps growing, and $\psi(x)\ge\psi(x_0)\cosh\kappa_0(x-x_0)$ for $x>x_0$: it diverges. **If $\psi'(x_0)<0$:** run the same argument toward $x\to-\infty$ (there $\psi$ increases as $x$ decreases). Either way $\psi$ blows up at one end and cannot be normalised. Hence **no** normalisable eigenstate has $E<V_{\min}$. $\square$
> A slightly more careful version of the argument excludes $E=V_{\min}$ too, so $E>V_{\min}$ for every normalisable state (Griffiths Problem 2.2, [[Griffiths - Introduction to quantum mechanics.pdf#page=39|PDF p.39]]): the **zero-point energy** (for the box, $V_{\min}=0$ but $E_1=\pi^2\hbar^2/2ma^2>0$).

> [!extra-beyond]- 🔵 Extra (beyond): a numerical check with a finite well
> In units $\hbar=m=1$ take $V=0$ for $|x|<1$ and $V=20$ outside (width 2). Solving the TISE numerically on a grid gives the lowest energies $0.917,\ 3.645,\ 8.088,\ 14.00$ against $1.234,\ 4.935,\ 11.10,\ 19.74$ for an infinite well of the same width. All are above $V_{\min}=0$ and **below** the infinite-well values (the wavefunction leaks into the walls, so the effective box is wider); the states alternate even, odd, even. Griffiths §2.6 treats the finite well analytically.

> [!connection] Same mathematics, different systems
> The box levels $E\propto n^2/a^2$ model a conjugated electron in a molecule or a semiconductor quantum dot; the same standing-wave idea gives the harmonics of a string ([[Waves - Course Map]]) and the modes of an atmospheric layer. The ring of [[QM02 The Schrodinger Equation and Stationary States]] differs only in the boundary condition (periodic, giving $n^2$ levels doubly degenerate).

## Map of this chapter
> [!connection] How QM04 connects
> **Builds on:** [[QM02 The Schrodinger Equation and Stationary States]] (TISE, boundary conditions) and [[QM03 States Operators and Measurement]] (expectation values, uncertainty, superposition).
> **Leads to:** [[QM05 The Harmonic Oscillator]] (a different potential, and the algebraic method).
> **Concepts:** [[Particle in a Box]] · [[Infinite Square Well]] · [[Energy Quantisation]] · [[Normalisation of a Wavefunction]] · [[Orthonormality of Eigenfunctions]] · [[Zero-Point Energy]] · [[Node of a Wavefunction]] · [[Parity Operator]] · [[Expectation Value]] · [[Uncertainty of an Observable]] · [[Correspondence Principle]] · [[Time Evolution of a Superposition]]
> **Other subjects:** [[Waves - Course Map]] (standing waves), [[Inorganic Chemistry - Course Map]] (particle-in-a-box for conjugated systems), [[Thermodynamics - Course Map]] (the density of states of a box is the start of statistical mechanics).

## Summary
> [!summary] Cheat-sheet
> - Box $0<x<a$: inside $\psi=A\sin kx+B\cos kx$; $\psi(0)=\psi(a)=0\Rightarrow B=0$, $k_n=n\pi/a$. $\psi_n=\sqrt{2/a}\sin(n\pi x/a)$, $E_n=n^2\pi^2\hbar^2/2ma^2=n^2E_1$, $n\ge1$; **$E_1>0$** (zero-point energy); $E\propto1/a^2$.
> - Orthonormal $\int\psi_m\psi_n=\delta_{mn}$; $n-1$ nodes; parity $(-1)^{n+1}$ about the centre; stationary: $\Psi_n=\psi_ne^{-iE_nt/\hbar}$.
> - $\langle x\rangle=a/2$, $\langle x^2\rangle=a^2(\tfrac13-\tfrac1{2n^2\pi^2})$, $\Delta x=a\sqrt{\tfrac1{12}-\tfrac1{2n^2\pi^2}}$; $\langle p\rangle=0$, $\langle p^2\rangle=2mE_n$, $\Delta p=n\pi\hbar/a$; $\Delta x\Delta p=\hbar\sqrt{n^2\pi^2/12-1/2}$ ($0.568\hbar$ for $n=1$).
> - $\frac1{\sqrt3}(\psi_1+\psi_2+\psi_3)$: $E_1,4E_1,9E_1$ each $\frac13$, $\langle E\rangle=\frac{14}3E_1$. $\frac1{\sqrt2}(\psi_1+\psi_2)$: $|\Psi|^2$ oscillates at $3E_1/\hbar$, $\langle x\rangle=\frac a2-\frac{16a}{9\pi^2}\cos\frac{3E_1t}\hbar$.
> - Symmetric $V\Rightarrow$ even/odd eigenfunctions ($[\hat P,\hat H]=0$); $E>V_{\min}$ (contradiction by growth of $\psi$). Large $n$: density $\to1/a$ (classical). Electron, 1 nm: $E_1=0.376$ eV.

## Practice
1. **Numbers.** An electron in a box of width 0.5 nm. Find $E_1,E_2$, the $1\to2$ photon wavelength, and $E_1$ if the box is doubled. Same for a proton in a 5 fm box (use $\hbar c=197.3$ MeV fm).
2. **Normalise and expand.** $\psi(x)=Ax(a-x)$ inside the box. Find $A$, the probability $|c_1|^2$ of the ground state, and $\langle E\rangle$ in units of $E_1$.
3. **Uncertainty.** Compute $\Delta x\,\Delta p/\hbar$ for $n=1,\ 4,\ 10$ and show it exceeds $1/2$ in each case.
4. **A different mixture.** $\Psi=\frac1{\sqrt5}(\psi_1+2\psi_2)$. Probabilities of $E_1,E_2$; $\langle E\rangle$; $\Delta E$.
5. **Time scales.** For $\frac1{\sqrt2}(\psi_1+\psi_3)$: find the density's oscillation frequency in terms of $E_1$ and the time-averaged $\langle x\rangle$. Why is $\langle x\rangle$ constant at $a/2$?
6. **Parity.** Use the parity theorem to show that $\langle\psi_m|x-\tfrac a2|\psi_n\rangle=0$ when $m-n$ is even. What does this say about $\psi_1,\psi_3$ superpositions?
7. **$E\ge V_{\min}$.** Use the theorem to bound the energy of a particle in $V(x)=\tfrac12m\omega^2x^2$, and of a particle in a box with $V=-V_0$ inside. What is the minimum possible energy in each case?
8. **Zero-point estimate.** Estimate $E_1$ from $\Delta p\sim\hbar/\Delta x$ with $\Delta x=a$. How does the answer compare with the exact $E_1$?
9. **Classical limit.** For $n=10$ compute $a|\psi_n|^2$ averaged over one wavelength. Compute $\Delta x/a$ for $n=1$ and $n\to\infty$.
10. **Why $n=0$ is excluded.** Explain with the TISE and boundary conditions why $n=0$ is not a state and why negative $n$ is not a new state.

> [!example]- Solutions
> 1. $E_1=\pi^2\hbar^2/2ma^2=0.376\text{ eV}\times4=1.504$ eV; $E_2=6.016$ eV; gap $3E_1=4.51$ eV, $\lambda=hc/\Delta E=275$ nm (UV). Doubling the box to 1 nm gives $E_1=0.376$ eV. Proton, $a=5$ fm: $E_1=\pi^2(\hbar c)^2/2m_pc^2a^2=\pi^2(197.3)^2/(2\times938.3\times25)=8.19$ MeV, the nuclear scale.
> 2. $\int_0^ax^2(a-x)^2\mathrm dx=a^5/30$, so $A=\sqrt{30/a^5}$. $c_n=\sqrt{2/a}\,A\int_0^a x(a-x)\sin\frac{n\pi x}a\mathrm dx=\dfrac{4\sqrt{60}}{n^3\pi^3}$ for odd $n$ (zero for even $n$), so $|c_1|^2=960/\pi^6=0.9986$. $\langle E\rangle=\int\psi(-\tfrac{\hbar^2}{2m}\psi'')\mathrm dx=\dfrac{\hbar^2}{m}\dfrac{30}{a^5}\dfrac{a^3}6=\dfrac{5\hbar^2}{ma^2}=1.013E_1$ (slightly above $E_1$ because of the small admixture of $n=3,5,\dots$).
> 3. $\sqrt{n^2\pi^2/12-1/2}$: $n=1$: $0.568$; $n=4$: $\sqrt{13.16-0.5}=3.56$; $n=10$: $\sqrt{82.2-0.5}=9.04$. All above $0.5$.
> 4. $P(E_1)=\tfrac15$, $P(E_2=4E_1)=\tfrac45$; $\langle E\rangle=\tfrac15E_1+\tfrac{16}5E_1=3.4E_1$; $\langle E^2\rangle=\tfrac15+\tfrac{4\cdot16}5=13.0E_1^2$, so $\Delta E=\sqrt{13-11.56}E_1=1.2E_1$.
> 5. Energies $E_1$ and $9E_1$; the cross term oscillates as $\cos(8E_1t/\hbar)$, frequency $8E_1/\hbar$ (period $2\pi\hbar/8E_1$). $\langle\psi_1|x|\psi_3\rangle=0$ (both have the same parity about the centre), so there is no oscillating term in $\langle x\rangle$ and it stays at $a/2$; the density still changes shape.
> 6. $x-a/2$ is odd about the centre; $\psi_m\psi_n$ is even when $m-n$ is even (same parity), so the integrand is odd and integrates to zero. Hence a superposition of states of the same parity, such as $\psi_1+\psi_3$, has $\langle x\rangle=a/2$ for all time.
> 7. Harmonic: $V_{\min}=0$, so $E>0$ (indeed $E_0=\tfrac12\hbar\omega$, [[QM05 The Harmonic Oscillator]]). Box with $V=-V_0$ inside: $E>-V_0$, and in fact $E_1=-V_0+\pi^2\hbar^2/2ma^2$.
> 8. $\Delta p\sim\hbar/a$ gives $E\sim\Delta p^2/2m=\hbar^2/2ma^2$; the exact $E_1=\pi^2\times\hbar^2/2ma^2$ is $\pi^2\approx9.9$ times larger (using the exact $\Delta p=\pi\hbar/a$ gives $E_1$ exactly, since $\langle p\rangle=0$ and $\langle p^2\rangle=2mE_1$). The scaling $E\propto1/a^2$ is right.
> 9. $|\psi_{10}|^2=\frac2a\sin^2$ averages $\frac1a$ over a wavelength: the classical value. $\Delta x/a=0.1808$ for $n=1$ and $1/\sqrt{12}=0.2887$ as $n\to\infty$ (uniform).
> 10. $n=0$ gives $k=0$ and $\psi=A\sin0=0$: no particle (and $E=0$ would make $\psi''=0$, a straight line that cannot vanish at both walls unless zero). $-n$ gives $\sin(-n\pi x/a)=-\sin(n\pi x/a)$: the same state up to a sign (a global phase).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | the box, classical solution | [[Particle_in_a_box.pdf#page=2\|handwritten p.2]] | taught |
> | solution, boundary conditions, quantisation | [[Particle_in_a_box.pdf#page=3\|handwritten pp.3–5]] | taught |
> | normalisation, orthogonality, nodes | [[Particle_in_a_box.pdf#page=6\|handwritten pp.6–8]] | taught |
> | time evolution; visualisation | [[Particle_in_a_box.pdf#page=7\|handwritten p.7]]; [[PH2113_states_operators_notes.pdf#page=10\|SO §9]] | taught |
> | $\langle x\rangle,\langle p\rangle$; $\Delta x\Delta p$ in a box | [[Particle_in_a_box.pdf#page=9\|handwritten p.9]]; [[PH2113_states_operators_notes.pdf#page=9\|SO §8.2]] | taught |
> | Tutorial I (five questions) | [[tutorial1.pdf\|Tutorial I]] | taught |
> | finite well; classical limit | Griffiths §2.2, §2.6 (not read in detail) | extra/book |
> | closed form of $\Delta x\Delta p$ for all $n$; numerical finite-well check; marble | computed here (`scripts/qm_numbers.py`) | extra/beyond |
>
> **Read and not read.** The handwritten pages were read as images (10 pp.; the text layer is noise). The AI notes `quantum_notes.pdf` solve Tutorial I and agree with every result above. The handwritten notes call the box width $a$ (the typed notes call it $L$); I use $a$ in this chapter and $L$ for the ring.
>
> **Notes.** The handwritten page 9 shows $\langle x\rangle=a/2$ and starts $\langle p\rangle$ ($=0$ by the integral of $\sin\cos$); the $\langle x^2\rangle$ calculation is in SO §8.2 and Tutorial I Q1.

**References.** Griffiths, D. J. *Introduction to Quantum Mechanics*, §2.2 (infinite square well), §2.6 (finite well) · Landau, L. D. and Lifshitz, E. M. *Quantum Mechanics* §21 · CODATA 2018.
