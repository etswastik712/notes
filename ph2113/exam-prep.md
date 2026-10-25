---
id: ph2113/exam-prep
aliases: ["Exam prep: PH2113"]
tags: [exam-prep, ph2113]
trust_tier: agent_written
---

# Exam prep: PH2113

<!-- kurooto:exam-prep (kept current by Kurooto from your courses; write your own notes outside these markers) -->
## Next assessment
Not announced yet. The only dated assessment so far was the quiz on 2026-09-03, 10:00-11:00 (15 marks, already past).

## Covered so far
- [[ph2113/2026-08-27-tutorial-solutions-wavefunctions-uncertainty-schrodinger]]: uncertainty estimates, acceptable wavefunctions, ring quantisation, probability conservation, global vs relative phase
- [[ph2113/2026-08-31-states-operators-measurements-notes]]: states, superposition, operators, eigenstates, commutators, measurement probabilities, expectation, uncertainty, time evolution
- [[ph2113/2026-09-02-mock-quiz-and-solutions]]: mock quiz (photoelectric, Compton, acceptable wavefunctions, time evolution, parity/matrix eigenstates)
- [[ph2113/2026-09-03-quiz-ideal-solutions]]: quiz solutions (photoelectric, Compton, phase, ring, momentum eigenstates)
- [[ph2113/2026-09-07-matrices-expectation-uncertainty]]: 2×2 matrix version of the same machinery, basis change, commutator examples

## Must know
- Acceptable wavefunction on the whole line with a finite nonsingular potential: finite, single-valued, continuous, normalisable ($\int|\psi|^2dx=1$).
- Overall phase changes no probability; relative phase can (e.g. $|\psi|^2=2+2\cos(2kx-\varphi)$).
- Ring: $\psi(x+L)=\psi(x)$, $\psi_n=e^{ik_nx}/\sqrt L$, $k_n=2\pi n/L$, $E_n=2\pi^2\hbar^2n^2/(mL^2)$; $E_n=E_{-n}$ (degenerate), $p_{-n}=-p_n$.
- $\hat x=x$, $\hat p=-i\hbar\,d/dx$, $\hat H=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V$; operators are linear.
- Eigenstate: $\hat A\psi=a\psi$; a measurement of $A$ gives $a$ with certainty; $\Delta A=0$.
- Born rule: $\Psi=\sum c_a\phi_a\Rightarrow P(A=a)=|c_a|^2$, $\sum|c_a|^2=1$.
- $\langle A\rangle=\sum|c_a|^2a=\int\Psi^*\hat A\Psi\,dx$ (an average; need not be a possible outcome).
- $\Delta A=\sqrt{\langle A^2\rangle-\langle A\rangle^2}$; for $a\psi_n+b\psi_{-n}$, $\Delta p=2|a||b||p_n|$.
- $[\hat A,\hat B]=\hat A\hat B-\hat B\hat A$; $[\hat x,\hat p]=i\hbar$ (derive on a test function); $\Delta A\Delta B\ge\frac12|\langle[\hat A,\hat B]\rangle|$, so $\Delta x\Delta p\ge\hbar/2$.
- $[\hat A,\hat B]=0$ means compatible (common eigenstates); $[\hat H,\hat p]=0$ for a free particle.
- Stationary state: $\Psi_n=\psi_ne^{-iE_nt/\hbar}$, $|\Psi_n|^2$ time-independent. General: $\Psi(x,t)=\sum c_ne^{-iE_nt/\hbar}\psi_n$; $|c_n|$, $\langle E\rangle$, $\Delta E$ are constant; relative phases change, so $|\Psi|^2$ can change.
- Continuity: $\partial_t\rho+\partial_xj=0$, $j=\frac{\hbar}{2mi}(\Psi^*\Psi'-\Psi\Psi'^*)$; total probability is conserved when the boundary current vanishes.
- Photoelectric effect: threshold frequency; intensity changes photon number, not energy per photon ($E=h\nu$). Compton: the recoiling electron takes energy and momentum, so the photon's wavelength increases; the change is largest for backscattering and smaller for heavier targets.
- Time is a parameter, not an operator: a $\hat T$ with $[\hat T,\hat H]=i\hbar$ would need a spectrum unbounded below.

## Typical questions
- Explain-in-words photoelectric and Compton questions (mock quiz Q1-Q2, quiz Q1-Q2): [[ph2113/2026-09-02-mock-quiz-and-solutions]], [[ph2113/2026-09-03-quiz-ideal-solutions]].
- Is a given $\psi$ physically acceptable (normalisable, continuous)? Tutorial Q2, mock Q3: [[ph2113/2026-08-27-tutorial-solutions-wavefunctions-uncertainty-schrodinger]].
- Ring: periodic boundary condition, quantisation, degeneracy of $\pm n$ (tutorial Q3, quiz Q4).
- Does $|\Psi|^2$ change with time for a superposition? (mock Q4, lecture note section 9).
- Is a state an eigenstate of an operator (parity, momentum, matrix $\hat A$), and what happens to a superposition (mock Q5, quiz Q5, [[ph2113/2026-09-07-matrices-expectation-uncertainty]]).
- Compute probabilities, $\langle A\rangle$, $\Delta A$ for a given superposition (lecture notes sections 6-8; 2×2 examples in the 09-07 note).
- Same $|\psi|^2$ but different state (quiz Q3).

## Gaps
- No assessment dates beyond the 2026-09-03 quiz are known; syllabus and exam schedule not announced.
- Question text of the 2026-09-03 quiz is not in the files, only its solutions.
- Topics before these notes (photoelectric effect, Compton scattering, the Schrödinger equation itself) have no course-material note yet, only the user's own notes in [[06-quantum-mechanics/quantum-mechanics-course-map]].
- No problem sheets or homework deadlines have been posted in this batch.
<!-- /kurooto:exam-prep -->
