---
id: ph2113/exam-prep
aliases: ["Exam prep: PH2113"]
tags: [exam-prep, ph2113]
trust_tier: agent_written
---

# Exam prep: PH2113

<!-- kurooto:exam-prep (kept current by Kurooto from your courses; write your own notes outside these markers) -->
## Next assessment
Quiz 2 on 2026-10-29 (Thursday), during the regular tutorial slot, in your allotted tutorial room; be on time; calculators allowed (Classroom, posted 2026-10-21). Start time, marks and syllabus are not stated; quiz 1 ran 10:00-11:00 for 15 marks. Likely material: oscillator ladder operators and Tutorials I-III, but this is not confirmed. The midsem is past (solutions 2026-09-24); its rule was no formula sheet, so memorise the formulas below.

## Covered so far
- [[ph2113/2026-08-27-tutorial-solutions-wavefunctions-uncertainty-schrodinger]]: uncertainty estimates, acceptable wavefunctions, ring quantisation, probability conservation, global vs relative phase
- [[ph2113/2026-08-31-states-operators-measurements-notes]]: states, superposition, operators, eigenstates, commutators, measurement probabilities, expectation, uncertainty, time evolution
- [[ph2113/2026-09-02-mock-quiz-and-solutions]]: mock quiz (photoelectric, Compton, acceptable wavefunctions, time evolution, parity/matrix eigenstates)
- [[ph2113/2026-09-03-quiz-ideal-solutions]]: quiz solutions (photoelectric, Compton, phase, ring, momentum eigenstates)
- [[ph2113/2026-09-07-matrices-expectation-uncertainty]]: 2×2 matrix version of the same machinery, basis change, commutator examples
- [[ph2113/2026-09-08-tutorial-states-interference-uncertainty]]: problem set: superposition, double slit, pencil and Gaussian uncertainty, vanishing commutator, two-state matrices
- [[ph2113/2026-09-10-tutorial-solutions-states-interference-uncertainty]]: worked solutions to the above
- [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]]: problem set: acceptable wavefunctions, allowed potentials and matching conditions, stationary states, Fourier/Gaussian primer
- [[ph2113/2026-09-24-midsem-solutions]]: midsem solutions: de Broglie/Davisson-Germer, free-particle current, two-state box evolution, electron length scales, matrix observables, normalisability and complex potentials
- [[ph2113/2026-10-06-particle-in-a-box-notes]]: infinite well: boundary conditions, $E_n$, orthogonality, time evolution, expectation values (handwritten, partly illegible)
- [[ph2113/2026-10-06-tutorial-i-particle-in-a-box]]: problem set: $\Delta x\Delta p$ in the box, energy superpositions, symmetric potentials, $E\ge V_{\min}$
- [[ph2113/2026-10-12-tutorial-ii-harmonic-oscillator-ladder-operators]]: problem set: ladder operators, $\psi_1,\psi_2$, ground-state uniqueness, Gaussian integrals and Fourier transform
- [[ph2113/2026-10-19-harmonic-oscillator-ladder-operator-notes]]: oscillator lecture notes: ladder property, ground state, $E_n=\hbar\omega(n+\frac12)$, $\hat a_\pm\psi_n$ normalisation, expectation values (handwritten, partly garbled)
- [[ph2113/2026-10-19-tutorial-iii-harmonic-oscillator-expectation-values]]: problem set: $\langle p^2\rangle$ via ladder operators, $\langle x\rangle$, $\langle x^2\rangle$ Gaussian integrals, orthogonality of eigenfunctions

## Must know
- Acceptable wavefunction on the whole line with a finite nonsingular potential: finite, single-valued, continuous, normalisable ($\int|\psi|^2dx=1$). $\psi\to0$ is necessary but not sufficient: $1/\sqrt{1+|x|}$ is not normalisable (log divergence) (midsem Q6a).
- Overall phase changes no probability; relative phase can (e.g. $|\psi|^2=2+2\cos(2kx-\varphi)$).
- Ring: $\psi(x+L)=\psi(x)$, $\psi_n=e^{ik_nx}/\sqrt L$, $k_n=2\pi n/L$, $E_n=2\pi^2\hbar^2n^2/(mL^2)$; $E_n=E_{-n}$ (degenerate), $p_{-n}=-p_n$. Single-valuedness (e.g. $e^{i\varphi/2}$ fails) forces integer $m$, $L_z=m\hbar$.
- $\hat x=x$, $\hat p=-i\hbar\,d/dx$, $\hat H=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V$; operators are linear.
- Eigenstate: $\hat A\psi=a\psi$; a measurement of $A$ gives $a$ with certainty; $\Delta A=0$.
- Born rule: $\Psi=\sum c_a\phi_a\Rightarrow P(A=a)=|c_a|^2$, $\sum|c_a|^2=1$.
- $\langle A\rangle=\sum|c_a|^2a=\int\Psi^*\hat A\Psi\,dx$ (an average; need not be a possible outcome).
- $\Delta A=\sqrt{\langle A^2\rangle-\langle A\rangle^2}$; for $a\psi_n+b\psi_{-n}$, $\Delta p=2|a||b||p_n|$.
- $[\hat A,\hat B]=\hat A\hat B-\hat B\hat A$; $[\hat x,\hat p]=i\hbar$; $\Delta A\Delta B\ge\frac12|\langle[\hat A,\hat B]\rangle|$, so $\Delta x\Delta p\ge\hbar/2$.
- $[\hat A,\hat B]=0$ means compatible (common eigenstates), not that both uncertainties vanish in every state (degeneracy example: $\sqrt{2/L}\cos kx$ on the ring). Conversely $[A,B]\neq0$: an eigenvector of $A$ is in general not one of $B$ (midsem Q5d).
- $\langle p\rangle=0$ is not "momentum definitely zero": for $(\psi_++\psi_-)/\sqrt2$, $p=\pm\hbar k$ with probability $\tfrac12$ each, $\Delta p=\hbar k$.
- Two-path superposition: $|\psi_1+\psi_2|^2=4A^2\cos^2\frac{\varphi_2-\varphi_1}{2}$; fringe spacing $\lambda D/d$; incoherent addition has no interference term.
- Gaussian packet: $\Delta x=\sigma$, $\Delta p=\hbar/2\sigma$, $\Delta x\Delta p=\hbar/2$; its Fourier transform is again Gaussian, $\tilde\psi(k)=(2\sigma^2/\pi)^{1/4}e^{-\sigma^2k^2}$; narrow in $x$ means broad in $k$.
- Matching conditions: finite jump in $V$ gives continuous $\psi'$; for $V=\lambda\delta(x-x_0)$, $\psi'(x_0^+)-\psi'(x_0^-)=\frac{2m\lambda}{\hbar^2}\psi(x_0)$.
- TDSE $i\hbar\partial_t\Psi=-\frac{\hbar^2}{2m}\partial_x^2\Psi+V\Psi$; for $V(x)$, separation gives $T(t)=e^{-iEt/\hbar}$ and the TISE $-\frac{\hbar^2}{2m}\psi''+V\psi=E\psi$; stationary state $\Psi=\psi e^{-iEt/\hbar}$ has time-independent $|\Psi|^2$ (Classroom: Lecture 9).
- Stationary vs general: $\Psi=\sum c_ne^{-iE_nt/\hbar}\psi_n$; $|c_n|$, $\langle E\rangle$, $\Delta E$ constant; $|\Psi|^2$ and off-diagonal observables oscillate at $(E_2-E_1)/\hbar$.
- Infinite well (width $a$, $0<x<a$): $\psi=A\sin kx+B\cos kx$, $\psi(0)=\psi(a)=0\Rightarrow B=0$, $ka=n\pi$, $\psi_n\propto\sin(n\pi x/a)$, $E_n=n^2\pi^2\hbar^2/2ma^2$, $n=1,2,\dots$; $\int\psi_m^*\psi_n=\delta_{mn}$.
- Two-state box superposition $(\phi_1+\phi_2)/\sqrt2$: $T=2\pi\hbar/(E_2-E_1)=4mL^2/3\pi\hbar$, $\langle E\rangle=5\pi^2\hbar^2/4mL^2$, $\Delta E=3\pi^2\hbar^2/4mL^2$, $\Delta E\,T=\pi\hbar$ (midsem Q3).
- Free particle: $\omega=\hbar k^2/2m$, $v_{ph}=\hbar k/2m=\tfrac12v_{gr}$, $v_{gr}=\hbar k/m$ (physical). Current $j=\frac{\hbar}{2mi}(\Psi^*\Psi'-\Psi\Psi'^*)$; standing wave $\Rightarrow j=0$.
- Continuity: $\partial_t\rho+\partial_xj=0$; a complex potential $V=i\Gamma$ gives $P(t)=P(0)e^{2\Gamma t/\hbar}$, lifetime $\tau=\hbar/2|\Gamma|$ for $\Gamma<0$; $\hat H$ non-Hermitian means probability is not conserved.
- Superposition of solutions is a solution (linearity) but not an eigenstate unless the energies are equal.
- de Broglie: $\lambda=h/p=h/\sqrt{2m_eeV}\approx150.4/\sqrt V$ Å; non-relativistic error $\approx K/4mc^2$ (1% at about 20 keV).
- Electron length scales: $r_e=2.8$ fm, $\bar\lambda_C=\hbar/mc=386$ fm, $a_0=\bar\lambda_C/\alpha=0.053$ nm (ratio $\alpha:1:1/\alpha$); $E=-\tfrac12\alpha^2m_ec^2=-13.6$ eV. Confinement to about 1 fm gives $\Delta pc\approx98.5$ MeV, above pair production, so QFT is needed.
- Oscillator ladder operators: $\hat a_\pm=\frac1{\sqrt{2\hbar m\omega}}(\mp i\hat p+m\omega\hat x)$, $[\hat a_-,\hat a_+]=1$, $\hat H=\hbar\omega(\hat a_+\hat a_-+\tfrac12)=\hbar\omega(\hat a_-\hat a_+-\tfrac12)$ (Classroom: Tutorial III, oscillator notes).
- $\hat x=\sqrt{\hbar/2m\omega}\,(\hat a_++\hat a_-)$, $\hat p=i\sqrt{\hbar m\omega/2}\,(\hat a_+-\hat a_-)$.
- Ladder property: $\hat H(\hat a_\pm\psi)=(E\pm\hbar\omega)(\hat a_\pm\psi)$; eigenvalues are spaced by $\hbar\omega$.
- Ground state: $\hat a_-\psi_0=0$, $\psi_0=(m\omega/\pi\hbar)^{1/4}e^{-m\omega x^2/2\hbar}$, $E_0=\hbar\omega/2$; $E_n=\hbar\omega(n+\tfrac12)$.
- $\hat a_+\psi_n=\sqrt{n+1}\,\psi_{n+1}$, $\hat a_-\psi_n=\sqrt n\,\psi_{n-1}$, $\psi_n=\frac1{\sqrt{n!}}(\hat a_+)^n\psi_0$; $\hat a_+\hat a_-\psi_n=n\psi_n$.
- Hermitian conjugates: $\int f^*(\hat a_\pm g)\,dx=\int(\hat a_\mp f)^*g\,dx$.
- Eigenfunctions of a Hermitian $\hat H$ with different eigenvalues are orthogonal: $(E_n-E_m)\int\psi_m^*\psi_n\,dx=0$ (Tutorial III Problem 3).
- Oscillator expectation values by ladder operators: $\langle x\rangle=\langle p\rangle=0$ in $\psi_n$; $\langle p^2\rangle=\hbar m\omega(n+\tfrac12)$ (derived from $\langle\hat a_+\hat a_-\rangle=n$, $\langle\hat a_-\hat a_+\rangle=n+1$; check against your own notes).
- Photoelectric effect: threshold frequency; intensity changes photon number, not energy per photon ($E=h\nu$). Compton: the photon's wavelength increases; the change is largest for backscattering.
- Time is a parameter, not an operator.
- Two-state matrices: $X|{\pm y}\rangle=\pm i|{\mp y}\rangle$; $[X,Y]=2iZ$.

## Typical questions
- Explain-in-words photoelectric and Compton: [[ph2113/2026-09-02-mock-quiz-and-solutions]], [[ph2113/2026-09-03-quiz-ideal-solutions]].
- Is a given $\psi$ acceptable (normalisable, single-valued)? [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]] Problem 1; midsem Q6a-b in [[ph2113/2026-09-24-midsem-solutions]].
- Ring: periodic condition, quantisation, degeneracy: tutorial Q3, quiz Q4, 09-13 Problem 5.
- Does $|\Psi|^2$ change with time? Two-state superposition in a box: midsem Q3, [[ph2113/2026-10-06-tutorial-i-particle-in-a-box]] problem 3, 09-13 Problem 3.
- Eigenstate test and measurement probabilities with matrices: midsem Q5, [[ph2113/2026-09-07-matrices-expectation-uncertainty]].
- Expectation, $\Delta A$ for a superposition: lecture notes sections 6-8; [[ph2113/2026-10-06-tutorial-i-particle-in-a-box]] problems 1-2.
- Double-slit intensity, fringe spacing: [[ph2113/2026-09-10-tutorial-solutions-states-interference-uncertainty]] Q2.
- Uncertainty-principle estimates; Gaussian $\Delta x\Delta p$: same note Q3; midsem Q4a.
- Vanishing commutator but nonzero $\Delta p$: same note Q4.
- Matching conditions, classify potentials: 09-13 Problem 2.
- Gaussian integrals and Fourier transform: 09-13 Problem 6; [[ph2113/2026-10-12-tutorial-ii-harmonic-oscillator-ladder-operators]] Problem 5; $\langle x^2\rangle$ in $\psi_0$ by integration by parts: [[ph2113/2026-10-19-tutorial-iii-harmonic-oscillator-expectation-values]] Problem 2.
- Free-particle dispersion, current and standing waves; complex-potential decay: midsem Q2, Q6c.
- de Broglie wavelength numerics; length scales of the electron: midsem Q1, Q4.
- Ladder-operator proofs and oscillator states: [[ph2113/2026-10-12-tutorial-ii-harmonic-oscillator-ladder-operators]] Problems 1-3; derivation in [[ph2113/2026-10-19-harmonic-oscillator-ladder-operator-notes]].
- $\langle p^2\rangle$ (and $\langle x^2\rangle$) in $\psi_n$ by ladder operators: [[ph2113/2026-10-19-tutorial-iii-harmonic-oscillator-expectation-values]] Problem 1.
- Prove orthogonality of eigenfunctions with different eigenvalues: same note Problem 3.
- Proofs: symmetric $V$ gives parity eigenfunctions; $E\ge V_{\min}$; unique nodeless ground state (Tutorial I Problems 4-5, Tutorial II Problem 4).

## Gaps
- Quiz 2 (2026-10-29): start time, marks and syllabus are not announced; confirm. Formula sheets were not allowed at the midsem, so formulas above need to be memorised.
- The midsem question paper itself is not filed, only its solutions (questions inferred); Q4a and Q5 inputs were reconstructed.
- Tutorials I, II and III and the 09-13 tutorial have no posted solutions; their problems are unworked in the notes (the $\langle p^2\rangle$ result above is derived, not posted).
- The particle-in-a-box and oscillator handwritten scans are partly illegible/garbled (box: normalisation constant, final $\langle x^2\rangle$, $\langle p^2\rangle$; oscillator: the $\langle p^2\rangle$ line, parts of the factorisation step).
- Not yet in course notes: classical probability distribution of the oscillator, explicit $\psi_1,\psi_2$ and Hermite polynomials, $\langle x^2\rangle$ and $\langle V\rangle$ in $\psi_n$, time evolution of oscillator superpositions. Photoelectric, Compton and the Schrödinger equation also lack course notes (see [[06-quantum-mechanics/quantum-mechanics-course-map]] for your own).
- The 09-15 post says to solve problems not covered in class; which ones is not stated.
<!-- /kurooto:exam-prep -->
