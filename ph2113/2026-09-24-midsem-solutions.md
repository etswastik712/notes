---
id: ph2113/2026-09-24-midsem-solutions
aliases: [PH2113 midsem solutions]
tags: [ph2113, midsem, solutions]
trust_tier: agent_written
---

# PH2113 Mid-Semester Examination: Solutions

## Covered
Six questions (the question text is not in the file, only the solutions; the questions are inferred from the answers).

**Q1. de Broglie waves, Davisson-Germer.**
- (a) $K=eV$, $p=\sqrt{2m_eK}$, so $\lambda=h/p=h/\sqrt{2m_eeV}$. At $V=54$ V: $p=3.97\times10^{-24}$ kg m/s, $\lambda=0.167$ nm (equivalently $\lambda\simeq150.4/\sqrt V$ Å, with $V$ in volts).
- (b) Bragg-type condition $\lambda=d\sin\theta=0.215\sin50^\circ=0.165$ nm; agrees with (a) to about 1%, the experimental confirmation of the de Broglie wavelength.
- (c) Non-relativistic $\lambda_{NR}=hc/\sqrt{2Kmc^2}$; ratio to the exact result $\lambda_{NR}/\lambda_{ex}=\sqrt{1+K/2mc^2}\simeq1+K/4mc^2$. A 1% correction needs $K=0.04\,m_ec^2\approx20$ keV, so $V\approx20$ kV.

**Q2. Free particle, phase velocity, probability current.**
- (a) Substituting $\psi\propto e^{i(kx-\omega t)}$ into the TDSE: $\omega=\hbar k^2/2m$, $v_{ph}=\omega/k=\hbar k/2m$, $v_{gr}=d\omega/dk=\hbar k/m$, so $v_{ph}=\tfrac12v_{gr}$. The group velocity equals the classical velocity $p/m$ and is the physical one; the phase velocity of a single unnormalisable plane wave has no measurable meaning.
- (b) For $\Psi=A(e^{ikx}+Be^{-ikx})e^{-i\omega t}$, $j=\frac{\hbar k}{m}|A|^2(1-|B|^2)$. With $B=e^{i\varphi}$, $|B|=1$, so $j=0$ everywhere; $|\Psi|^2=4|A|^2\cos^2(kx-\varphi/2)$. $\Psi$ is a real function of $x$ times constant phases, so $\Psi^*\partial_x\Psi$ is real and $j=0$.
- (c) A standing wave: right- and left-moving parts of equal amplitude each carry flux $\frac{\hbar k}{m}|A|^2$ and cancel. Probability is present at each $x$ but not transported, like a standing wave on a string storing energy without net power flow.

**Q3. Time evolution in the infinite square well** (state $\tfrac1{\sqrt2}(\phi_1+\phi_2)$, well of width $L$).
- (a) $\Psi=\tfrac1{\sqrt2}[\phi_1e^{-iE_1t/\hbar}+\phi_2e^{-iE_2t/\hbar}]$, $|\Psi|^2=\tfrac12[\phi_1^2+\phi_2^2+2\phi_1\phi_2\cos((E_2-E_1)t/\hbar)]$. Only $E_2-E_1=3\pi^2\hbar^2/2mL^2$ appears; period $T=2\pi\hbar/(E_2-E_1)=4mL^2/(3\pi\hbar)$.
- (b) $\langle E\rangle=\tfrac12(E_1+E_2)=5\pi^2\hbar^2/4mL^2$.
- (c) With $\varepsilon=\pi^2\hbar^2/2mL^2$: $\langle E^2\rangle=8.5\varepsilon^2$, $\langle E\rangle^2=6.25\varepsilon^2$, $\Delta E=1.5\varepsilon=3\pi^2\hbar^2/4mL^2$. Then $\Delta E\,T=\pi\hbar$: $m$ and $L$ cancel. This is the energy-time relation $\Delta E\,\Delta t\gtrsim\hbar/2$: a state with energy spread $\Delta E$ cannot evolve appreciably in a time shorter than about $\hbar/\Delta E$.
- (d) $\langle x\rangle(t)=\frac L2-\frac{16L}{9\pi^2}\cos(2\pi t/T)$; amplitude $16L/9\pi^2=0.180L$, so $\langle x\rangle$ oscillates between $0.32L$ and $0.68L$. Diagonal terms each contribute $\tfrac12\cdot\tfrac L2$; the two off-diagonal terms combine with coefficient 1.

**Q4. Three length scales of the electron.**
- (a) Confining to $\Delta x=1$ fm... in the solution $\Delta pc\ge\hbar c/2\Delta x=197\text{ MeV fm}/2\text{ fm}=98.5$ MeV, about $193\,m_ec^2$, far above the pair-production threshold $2m_ec^2=1.02$ MeV. Not trustworthy: the particle is ultra-relativistic, so $E=p^2/2m$ fails, and $e^+e^-$ pair creation means particle number is not conserved, so no single-particle wave equation applies; quantum field theory is required.
- (b) Reduced Compton wavelength $\bar\lambda_C=\hbar/mc=\hbar c/mc^2=197\text{ MeV fm}/0.511\text{ MeV}=386$ fm (use $\hbar c$ to avoid SI conversions).
- (c) Minimising $E(a)=\frac{\hbar^2}{2m_ea^2}-\frac{e^2}{4\pi\varepsilon_0a}$: $dE/da=0$ gives $a=a_0=4\pi\varepsilon_0\hbar^2/m_ee^2=0.053$ nm, and $E(a_0)=-\frac{e^2}{8\pi\varepsilon_0a_0}=-\tfrac12\alpha^2m_ec^2=-13.6$ eV. With $\alpha=e^2/4\pi\varepsilon_0\hbar c$: $a_0=\bar\lambda_C/\alpha$ (check: $386\text{ fm}\times137=5.29\times10^4$ fm). The three scales are in ratio $\alpha:1:1/\alpha$: classical radius 2.8 fm, Compton 386 fm, Bohr $5.3\times10^4$ fm.

**Q5. Observables as matrices** ($A$ with $\det(A-aI)=(1-a)^2-4$; $A^2=\begin{pmatrix}5&4\\4&5\end{pmatrix}$, i.e. $A=\begin{pmatrix}1&2\\2&1\end{pmatrix}$; state $v=\frac1{\sqrt5}(2,1)^T$).
- (a) Eigenvalues $a_1=3$, $a_2=-1$; $u_1=\tfrac1{\sqrt2}(1,1)^T$, $u_2=\tfrac1{\sqrt2}(1,-1)^T$. $P_1=|u_1^Tv|^2=9/10$, $P_2=1/10$, sum 1.
- (b) $\langle A\rangle=v^TAv=2.6$ (check $\tfrac9{10}\cdot3+\tfrac1{10}(-1)=2.6$); $\langle A^2\rangle=8.2$; $\Delta A=\sqrt{8.2-6.76}=\sqrt{1.44}=1.2$.
- (c) $AB=\begin{pmatrix}1&-2\\2&-1\end{pmatrix}$, $BA=\begin{pmatrix}1&2\\-2&-1\end{pmatrix}$, so $[A,B]=\begin{pmatrix}0&-4\\4&0\end{pmatrix}\neq0$: they do not commute.
- (d) $Bu_+=\tfrac1{\sqrt2}(1,-1)^T$ is not a multiple of $u_+=u_1$, so $u_+$ is not an eigenvector of $B$. Non-commuting matrices share no common eigenbasis; $A$ and $B$ cannot both have definite values in the same state.

**Q6. Normalisability, boundary conditions, non-Hermitian potentials.**
- (a) $\psi=A/\sqrt{1+|x|}$: $\int|A|^2/(1+|x|)\,dx=2|A|^2\ln(1+x)|_0^\infty\to\infty$; not normalisable (log divergence). $\psi\to0$ at infinity is necessary but not sufficient: $\psi$ must decay faster than $1/\sqrt{|x|}$.
- (b) $\psi=Ae^{i\varphi/2}$ on a ring: $\psi(\varphi+2\pi)=-\psi(\varphi)$, double-valued, not allowed. Single-valuedness forces $e^{2\pi im}=1$, $m\in\mathbb Z$, $L_z=m\hbar$; half-integer $m$ is excluded for orbital angular momentum.
- (c) With $V=i\Gamma$ (and its conjugate equation), multiply and subtract: $i\hbar\,\partial_t|\psi|^2=-\frac{\hbar^2}{2m}\partial_x(\psi^*\psi'-\psi\psi^{*\prime})+2i\Gamma|\psi|^2$. The first term is a total derivative and integrates to zero for normalisable $\psi$, leaving $dP/dt=(2\Gamma/\hbar)P$, $P(t)=P(0)e^{2\Gamma t/\hbar}$. For $\Gamma<0$: exponential loss (absorptive medium, or unstable particle), $\tau=\hbar/2|\Gamma|$ from $P(0)e^{-t/\tau}$. $\hat H$ is non-Hermitian, so the system is not closed and probability is not conserved.
- (d) Is a superposition of two solutions a solution? Yes: the Schrödinger equation is linear and homogeneous. Is it an energy eigenstate? No: $\hat H(a\psi_1+b\psi_2)=aE_1\psi_1+bE_2\psi_2$, not a multiple of $a\psi_1+b\psi_2$ unless $E_1=E_2$. Linearity guarantees correct evolution; being an eigenstate means a definite value of an observable. A valid state need not have definite energy (compare Q3).

## From the post
Find Solution set for Mid sem.

As suggested by one of you, we will first scale up the marks on the question paper, with the original 30 marks scaled to 60 marks. The evaluation will then be done on this 60-mark scale, and the marks will subsequently be scaled back down to 30. This will allow us to make finer distinctions while evaluating partial credit—for example, it is easier to assign 1 mark out of 60 than 0.5 marks out of 30.

## Files
- [ph2113_solutions.pdf](https://drive.google.com/file/d/1l5BUZ_WWeq1wDEm7D_p2c7CpTWtGRIPK/view?usp=drive_web) (read; question text not included in it). Note: in Q4(a) the text extraction lost the given $\Delta x$ value; I wrote it from the formula $\hbar c/2\Delta x=98.5$ MeV, which implies $\Delta x=1$ fm. Q5's matrices $A$, $B$ and $v$ were reconstructed from the worked answers.

## Related
- [[ph2113/2026-09-07-matrices-expectation-uncertainty]]: the 2×2 matrix machinery of Q5
- [[ph2113/2026-08-31-states-operators-measurements-notes]]: expectation, uncertainty and time evolution (Q3, Q5)
- [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]]: acceptable wavefunctions, complex potentials, continuity (Q6)
- [[ph2113/2026-08-27-tutorial-solutions-wavefunctions-uncertainty-schrodinger]]: uncertainty estimates and ring quantisation (Q4, Q6)
- [[06-quantum-mechanics/qm04-the-particle-in-a-box]]: your own notes on the infinite well (Q3)
