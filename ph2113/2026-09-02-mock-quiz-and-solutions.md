---
id: ph2113/2026-09-02-mock-quiz-and-solutions
aliases: [PH2113 mock quiz]
tags: [ph2113, quiz, practice]
trust_tier: agent_written
---

# PH2113 Mock Quiz (50 min, 15 marks) and ideal solutions

## Covered
Practice paper with its solution set (Classroom: PH2113_Mock_Quiz_50min_15marks.pdf, PH2113_Mock_Quiz_Ideal_Solutions.pdf). Explanations are expected, not bare formulas.

**Q1 Photoelectric effect (2).** Metal X emits, Y does not, at the same frequency $\nu$. (a) $\nu\ge\nu_{0X}$ and $\nu<\nu_{0Y}$: the frequency lies above X's threshold and below Y's. (b) Raising intensity at fixed frequency sends more photons per unit time but does not raise the energy per photon; one photon still lacks the energy to free an electron from Y.

**Q2 Thomson vs Compton (3).** (a) A recoiling electron carries kinetic energy that must come from the photon, so the photon has less energy, hence longer wavelength. (b) The electron, initially at rest, is observed to recoil, so it gained momentum, which conservation says came from the photon: photons carry momentum. (c) For a very heavy charged particle the recoil, and the energy taken, is much smaller, so the wavelength change becomes less important.

**Q3 Acceptable wavefunctions (3).** Finite nonsingular potential on the whole line; wavefunction must be finite, single-valued, continuous, normalisable.
- $\psi_A=Ne^{-x^2/a^2}$: acceptable (finite, continuous, decays).
- $\psi_B=Ne^{+x^2/a^2}$: not acceptable, grows without bound, $\int|\psi_B|^2$ diverges.
- $\psi_C$ ($+Ne^{-x^2/a^2}$ for $x<0$, $-Ne^{-x^2/a^2}$ for $x\ge0$): not acceptable, finite jump from $+N$ to $-N$ at $x=0$.

**Q4 Time evolution of a superposition (4).** $\Psi(x,0)=\frac1{\sqrt2}(\phi_1+\phi_2)$, $E_1\ne E_2$.
- (a) $\Psi(x,t)=\frac1{\sqrt2}[\phi_1e^{-iE_1t/\hbar}+\phi_2e^{-iE_2t/\hbar}]$.
- (b) "Only phases, so $|\Psi|^2$ cannot change" is wrong in general. The relative phase $e^{-i(E_2-E_1)t/\hbar}$ changes in time, and $|\Psi|^2=\frac12\big(|\phi_1|^2+|\phi_2|^2+\phi_1^*\phi_2e^{-i(E_2-E_1)t/\hbar}+\phi_2^*\phi_1e^{+i(E_2-E_1)t/\hbar}\big)$; the interference terms vary with time.
- (c) Only $\phi_1$: $\Psi=\phi_1e^{-iE_1t/\hbar}$, $|\Psi|^2=|\phi_1|^2$, independent of time.

**Q5 Operators and eigenstates (3).**
- (a) $\hat P\psi(x)=\psi(-x)$: $\hat P\cos kx=\cos kx$ (eigenstate, eigenvalue $+1$); $\hat Pe^{ikx}=e^{-ikx}$, not proportional to $e^{ikx}$, so not a parity eigenstate; the operator gives the opposite travelling wave.
- (b) $\hat A=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $u_\pm=\frac1{\sqrt2}(1,\pm1)^T$, eigenvalues $\pm1$; $v=(1,0)^T=\frac1{\sqrt2}(u_++u_-)$. $\hat Av=(0,1)^T$, not proportional to $v$, so $v$ is not an eigenvector. $\hat Av=\frac1{\sqrt2}(u_+-u_-)$: the components have different eigenvalues so their relative coefficient changes; a superposition of eigenvectors with different eigenvalues need not return proportional to itself.

## From the post
Mock Question paper + solutions for your practice.

## Files
- [PH2113_Mock_Quiz_50min_15marks.pdf](https://drive.google.com/file/d/1eWw_YP-XxVa-Utws6yi92TVJ4oDSX9sa/view?usp=drive_web)
- [PH2113_Mock_Quiz_Ideal_Solutions.pdf](https://drive.google.com/file/d/12yI06VQKXWy8dF1aU0AI3z4zj4M8Q61I/view?usp=drive_web)

Posted: [Classroom](https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODc3MDM3ODY3NjM5)

## Related
- [[ph2113/2026-09-03-quiz-ideal-solutions]]: the actual quiz solutions, same style
- [[06-quantum-mechanics/concepts/compton-scattering]]: Q2
- [[06-quantum-mechanics/concepts/wave-particle-duality]]: photoelectric effect and photons
- [[06-quantum-mechanics/concepts/parity-operator]]: Q5(a)
- [[06-quantum-mechanics/qm03-states-operators-and-measurement]]: Q4 and Q5 background
