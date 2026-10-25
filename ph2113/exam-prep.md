---
id: ph2113/exam-prep
aliases: ["Exam prep: PH2113"]
tags: [exam-prep, ph2113]
trust_tier: agent_written
---

# Exam prep: PH2113

<!-- kurooto:exam-prep (kept current by Kurooto from your courses; write your own notes outside these markers) -->
## Next assessment
Midsem: date not announced in the posts seen so far. Rules (Classroom, 2026-09-22): calculator allowed, formula sheet NOT allowed; covers the entire course material before midsem; Fourier series/transform need not be learnt separately. The earlier quiz (2026-09-03, 15 marks) is past.

## Covered so far
- [[ph2113/2026-08-27-tutorial-solutions-wavefunctions-uncertainty-schrodinger]]: uncertainty estimates, acceptable wavefunctions, ring quantisation, probability conservation, global vs relative phase
- [[ph2113/2026-08-31-states-operators-measurements-notes]]: states, superposition, operators, eigenstates, commutators, measurement probabilities, expectation, uncertainty, time evolution
- [[ph2113/2026-09-02-mock-quiz-and-solutions]]: mock quiz (photoelectric, Compton, acceptable wavefunctions, time evolution, parity/matrix eigenstates)
- [[ph2113/2026-09-03-quiz-ideal-solutions]]: quiz solutions (photoelectric, Compton, phase, ring, momentum eigenstates)
- [[ph2113/2026-09-07-matrices-expectation-uncertainty]]: 2×2 matrix version of the same machinery, basis change, commutator examples
- [[ph2113/2026-09-08-tutorial-states-interference-uncertainty]]: problem set: superposition, double slit, pencil and Gaussian uncertainty, vanishing commutator, two-state matrices
- [[ph2113/2026-09-10-tutorial-solutions-states-interference-uncertainty]]: worked solutions to the above
- [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]]: problem set: acceptable wavefunctions, allowed potentials and matching conditions, stationary states, Fourier/Gaussian primer

## Must know
- Acceptable wavefunction on the whole line with a finite nonsingular potential: finite, single-valued, continuous, normalisable ($\int|\psi|^2dx=1$).
- Overall phase changes no probability; relative phase can (e.g. $|\psi|^2=2+2\cos(2kx-\varphi)$).
- Ring: $\psi(x+L)=\psi(x)$, $\psi_n=e^{ik_nx}/\sqrt L$, $k_n=2\pi n/L$, $E_n=2\pi^2\hbar^2n^2/(mL^2)$; $E_n=E_{-n}$ (degenerate), $p_{-n}=-p_n$.
- $\hat x=x$, $\hat p=-i\hbar\,d/dx$, $\hat H=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V$; operators are linear.
- Eigenstate: $\hat A\psi=a\psi$; a measurement of $A$ gives $a$ with certainty; $\Delta A=0$.
- Born rule: $\Psi=\sum c_a\phi_a\Rightarrow P(A=a)=|c_a|^2$, $\sum|c_a|^2=1$.
- $\langle A\rangle=\sum|c_a|^2a=\int\Psi^*\hat A\Psi\,dx$ (an average; need not be a possible outcome).
- $\Delta A=\sqrt{\langle A^2\rangle-\langle A\rangle^2}$; for $a\psi_n+b\psi_{-n}$, $\Delta p=2|a||b||p_n|$.
- $[\hat A,\hat B]=\hat A\hat B-\hat B\hat A$; $[\hat x,\hat p]=i\hbar$; $\Delta A\Delta B\ge\frac12|\langle[\hat A,\hat B]\rangle|$, so $\Delta x\Delta p\ge\hbar/2$.
- $[\hat A,\hat B]=0$ means compatible (common eigenstates), not that both uncertainties vanish in every state. Example: $[\hat H,\hat p]=0$ for a free particle on a ring, yet $\sqrt{2/L}\cos kx$ has $\Delta H=0$ and $\Delta p=\hbar k\neq0$, because of the degeneracy $E(+k)=E(-k)$ (Classroom: tutorial solutions, Q4).
- $\langle p\rangle=0$ is not "momentum definitely zero": for $(\psi_++\psi_-)/\sqrt2$, $p=\pm\hbar k$ with probability $\tfrac12$ each, $\Delta p=\hbar k$.
- Two-path superposition: $|\psi_1+\psi_2|^2=2A^2[1+\cos(\varphi_2-\varphi_1)]=4A^2\cos^2\frac{\varphi_2-\varphi_1}{2}$; fringes at $y_n=n\lambda D/d$, spacing $\lambda D/d$; a constant relative phase $\alpha$ shifts the pattern, not its spacing; with no coherent superposition (probabilities added) the interference term vanishes.
- Gaussian packet $\psi=(2\pi\sigma^2)^{-1/4}\exp[-(x-x_0)^2/4\sigma^2+ik_0x]$: $\langle x\rangle=x_0$, $\Delta x=\sigma$, $\langle p\rangle=\hbar k_0$, $\Delta p=\hbar/2\sigma$, so $\Delta x\Delta p=\hbar/2$: a minimum-uncertainty state. Its Fourier transform is again Gaussian, $\tilde\psi(k)=(2\sigma^2/\pi)^{1/4}e^{-\sigma^2k^2}$.
- Narrow in $x$ means broad in $k$; $p=\hbar k$ (Classroom: wavefunctions/potentials tutorial, Problems 5-6).
- Matching conditions: finite jump in $V$ gives continuous $\psi'$; for $V=\lambda\delta(x-x_0)$, $\psi'(x_0^+)-\psi'(x_0^-)=\frac{2m\lambda}{\hbar^2}\psi(x_0)$, so a cusp is not automatically unphysical. $V$ is normally real; a complex potential models loss, not a closed system.
- Adding a constant $V_0$ to $V$ multiplies $\psi$ by $e^{-iV_0t/\hbar}$ and changes no probabilities.
- Stationary state: $\Psi_n=\psi_ne^{-iE_nt/\hbar}$, $|\Psi_n|^2$ time-independent. General: $\Psi=\sum c_ne^{-iE_nt/\hbar}\psi_n$; $|c_n|$, $\langle E\rangle$, $\Delta E$ are constant; relative phases change, so $|\Psi|^2$ and observables with off-diagonal elements can change, e.g. $\langle X\rangle=\cos[(E_2-E_1)t/\hbar]$.
- Continuity: $\partial_t\rho+\partial_xj=0$, $j=\frac{\hbar}{2mi}(\Psi^*\Psi'-\Psi\Psi'^*)$; total probability is conserved when the boundary current vanishes.
- Photoelectric effect: threshold frequency; intensity changes photon number, not energy per photon ($E=h\nu$). Compton: the recoiling electron takes energy and momentum, so the photon's wavelength increases; the change is largest for backscattering and smaller for heavier targets.
- Time is a parameter, not an operator: a $\hat T$ with $[\hat T,\hat H]=i\hbar$ would need a spectrum unbounded below.
- Two-state matrices: $X|{\pm y}\rangle=\pm i|{\mp y}\rangle$; $[X,Y]=2iZ$; for $|{+z}\rangle$, $\Delta X\Delta Y=1=\frac12|\langle[X,Y]\rangle|$.

## Typical questions
- Explain-in-words photoelectric and Compton questions (mock quiz Q1-Q2, quiz Q1-Q2): [[ph2113/2026-09-02-mock-quiz-and-solutions]], [[ph2113/2026-09-03-quiz-ideal-solutions]].
- Is a given $\psi$ physically acceptable (normalisable, continuous)? Tutorial Q2, mock Q3: [[ph2113/2026-08-27-tutorial-solutions-wavefunctions-uncertainty-schrodinger]]; more cases (a)-(g) in [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]] Problem 1.
- Ring: periodic boundary condition, quantisation, degeneracy of $\pm n$ (tutorial Q3, quiz Q4; Problem 5 of the 09-13 tutorial).
- Does $|\Psi|^2$ change with time for a superposition? (mock Q4, lecture note section 9; 09-13 tutorial Problem 3; E3 of [[ph2113/2026-09-10-tutorial-solutions-states-interference-uncertainty]]).
- Is a state an eigenstate of an operator (parity, momentum, matrix $\hat A$), and what happens to a superposition (mock Q5, quiz Q5, [[ph2113/2026-09-07-matrices-expectation-uncertainty]]).
- Compute probabilities, $\langle A\rangle$, $\Delta A$ for a given superposition (lecture notes sections 6-8; 2×2 examples in the 09-07 note and E1-E2 of the 09-10 solutions).
- Same $|\psi|^2$ but different state (quiz Q3).
- Double-slit intensity and fringe spacing, coherent vs incoherent: [[ph2113/2026-09-10-tutorial-solutions-states-interference-uncertainty]] Q2.
- Estimate with the uncertainty principle (pencil: $\omega$, $\Delta x_{\min}$, growth time): same note, Q3(A). Gaussian $\Delta x,\Delta p$ by direct integration: Q3(B).
- Vanishing commutator but nonzero $\Delta p$ (degeneracy): same note, Q4.
- Matching conditions at a step or $\delta$ potential; classify potentials: [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]] Problem 2.
- Fourier transform of a Gaussian and why narrow-in-$x$ means broad-in-$k$: same note, Problem 6.

## Gaps
- Midsem date, time and room are not in the posts seen; confirm. The 2026-09-22 post says no formula sheet, so the formulas under Must know need to be memorised.
- Question text of the 2026-09-03 quiz is not in the files, only its solutions.
- Topics before these notes (photoelectric effect, Compton scattering, the Schrödinger equation itself) have no course-material note yet, only the user's own notes in [[06-quantum-mechanics/quantum-mechanics-course-map]]. Classroom also holds Lecture 7 and Lecture 8 PDFs (uncertainty, Compton scale, Schrödinger equation) that are not yet filed as notes.
- The 2026-09-13 tutorial has no posted solutions; Problems 1-6 there are unworked in the notes.
- The 2026-09-15 post says to solve the remaining tutorial problems not done in class; which ones is not stated.
<!-- /kurooto:exam-prep -->
