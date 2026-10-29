---
id: ph2113/2026-08-31-states-operators-measurements-notes
aliases: [PH2113 states operators measurements lecture note]
tags: [ph2113, lecture]
trust_tier: agent_written
---

# Quantum states, operators, measurements, uncertainty and time evolution

## Covered
Lecture note built on the particle on a ring (Classroom: PH2113_states_operators_notes.pdf).

**Ring.** $\psi(x+L)=\psi(x)$; $\psi_n=\frac1{\sqrt L}e^{ik_nx}$, $k_n=2\pi n/L$, $n\in\mathbb Z$; $p_n=\hbar k_n=2\pi\hbar n/L$; $E_n=p_n^2/2m=2\pi^2\hbar^2n^2/(mL^2)$.
- *Numbers:* electron on $L\approx0.83$ nm (benzene-sized): $E_n\approx2.18\,n^2$ eV, discrete and eV-scale. For $L=1$ cm: $E_1\approx1.5\times10^{-14}$ eV, about $10^{13}$ times below $k_BT\approx0.025$ eV, so the spectrum looks continuous. $E_n\propto1/L^2$: growing $L$ shrinks the spacing, not the discreteness (correspondence principle).

**States and superposition.** A state is $\psi(x)$ (or $|\psi\rangle$), $\int|\psi|^2dx=1$. If $\psi_1,\psi_2$ are allowed, $\Psi=c_1\psi_1+c_2\psi_2$ is allowed (same boundary conditions, normalised). Orthonormality $\int_0^L\psi_m^*\psi_n\,dx=\delta_{mn}$, so $\sum|c_n|^2=1$. Examples: $(\psi_n+\psi_{-n})/\sqrt2=\sqrt{2/L}\cos k_nx$; $(\psi_n-\psi_{-n})/(i\sqrt2)=\sqrt{2/L}\sin k_nx$ (both contain $\pm p_n$).
- *Phases:* $\psi'=e^{i\alpha}\psi$ gives the same $|\psi'|^2$ (same physical state). Relative phase matters: $\Psi_\varphi=(\psi_n+e^{i\varphi}\psi_{-n})/\sqrt2$ has $|\Psi_\varphi|^2=\frac1L[1+\cos(2k_nx-\varphi)]$.

**Operators.** $\hat x=x$, $\hat p=-i\hbar\,d/dx$, $\hat H=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V$ ($V=0$: $\hat H=\hat p^2/2m$). Operators are linear. Examples: $\hat pe^{ikx}=\hbar k\,e^{ikx}$; $\hat p\cos kx=i\hbar k\sin kx$ (not proportional); $\hat H\cos kx=\frac{\hbar^2k^2}{2m}\cos kx$ (proportional); parity $\hat P\psi(x)=\psi(-x)$: $\hat P\cos kx=+\cos kx$, $\hat P\sin kx=-\sin kx$.

**Eigenstates.** $\hat A\psi=a\psi$: $\psi$ is an eigenstate with eigenvalue $a$; measuring $A$ gives $a$ with certainty. Ask "eigenstate of which operator?".
- $\psi_n$ is an eigenstate of both $\hat p$ and $\hat H$. $E_n=E_{-n}$ but $p_{-n}=-p_n$: degeneracy.
- $\cos k_nx$: definite energy, not definite momentum. $(\psi_0+\psi_1)/\sqrt2$: not an energy eigenstate ($\hat H\Psi=(E_0\psi_0+E_1\psi_1)/\sqrt2$).
- Box: $\phi_n=\sqrt{2/L}\sin(n\pi x/L)$, $E_n=n^2\pi^2\hbar^2/(2mL^2)$: definite energy, $\hat p\phi_n\propto\cos(n\pi x/L)$, not definite momentum.

**Commutators.** $[\hat A,\hat B]=\hat A\hat B-\hat B\hat A$. $[\hat x,\hat p]\psi=i\hbar\psi$, so $[\hat x,\hat p]=i\hbar$ (derivation: $\hat p\hat x\psi=-i\hbar\psi-i\hbar x\psi'$).
- $[\hat A,\hat B]=0$: compatible, common set of eigenstates. $[\hat A,\hat B]\ne0$: incompatible, no state (barring accidents) has both sharp.
- $[\hat H,\hat p]=0$ for the free particle/ring. $[\hat H,\hat x]\ne0$ when $\hat H$ depends on momentum.
- Generalised uncertainty: $\Delta A\,\Delta B\ge\frac12|\langle[\hat A,\hat B]\rangle|$.
- Measurement order matters for non-commuting observables. Classical numbers always commute, which is why observables must be operators.

**Measurement probabilities.** $\hat A\phi_a=a\phi_a$, $\Psi=\sum c_a\phi_a$, $\sum|c_a|^2=1$: $P(A=a)=|c_a|^2$. Examples: $(\psi_0+\psi_1)/\sqrt2$ gives $E_0$ or $E_1$ each with probability $\tfrac12$; $\sqrt{3/4}\,\psi_n+\tfrac12\psi_{-n}$ gives $+p_n$ with prob. $3/4$, $-p_n$ with prob. $1/4$.

**Expectation values.** $\langle A\rangle=\sum|c_a|^2a=\int\Psi^*\hat A\Psi\,dx$; $\langle x\rangle=\int\Psi^*x\Psi$, $\langle p\rangle=\int\Psi^*(-i\hbar\partial_x)\Psi$, $\langle E\rangle=\int\Psi^*\hat H\Psi$. It is an ensemble average and need not be an allowed single result (outcomes 0 and 10 eV with probability $\tfrac12$ each: $\langle E\rangle=5$ eV). For $\Psi=a\psi_n+b\psi_{-n}$: $\langle p\rangle=(|a|^2-|b|^2)p_n$. For $(\psi_r+\psi_s)/\sqrt2$: $\langle E\rangle=(E_r+E_s)/2$.

**Uncertainty.** $(\Delta A)^2=\langle(A-\langle A\rangle)^2\rangle=\langle A^2\rangle-\langle A\rangle^2$. Eigenstate $\Leftrightarrow\Delta A=0$. Ring: $\Delta p=0$ for $\psi_n$; for $(\psi_n+\psi_{-n})/\sqrt2$, $\Delta p=|p_n|$ but $\Delta E=0$; for $a\psi_n+b\psi_{-n}$, $\Delta p=2|a||b||p_n|$ (zero for one component, maximal for equal weights). Two equally likely values $a_1,a_2$: $\Delta A=|a_2-a_1|/2$.
- *Box:* $\langle x\rangle=L/2$, $\langle x^2\rangle=L^2(\frac13-\frac1{2n^2\pi^2})$, $\Delta x=L\sqrt{\frac1{12}-\frac1{2n^2\pi^2}}$, $\langle p\rangle=0$, $\Delta p=n\pi\hbar/L$, $\Delta x\Delta p=\hbar\sqrt{n^2\pi^2/12-1/2}>\hbar/2$; ground state $\Delta x\simeq0.181L$, $\Delta x\Delta p\simeq0.568\hbar$. Electron in $L=1$ nm: $E_1\approx0.376$ eV, $\Delta x\Delta p\approx6.0\times10^{-35}$ J s vs $\hbar/2=5.3\times10^{-35}$.

**Time evolution.** $i\hbar\,\partial_t\Psi=\hat H\Psi$. Energy eigenstate: $\Psi_n=\psi_ne^{-iE_nt/\hbar}$, $|\Psi_n|^2$ time-independent (stationary; not zero momentum, e.g. ring $\psi_n$ has uniform density but definite $p_n$). General: $\Psi(x,t)=\sum c_ne^{-iE_nt/\hbar}\psi_n$; $|c_n|$ fixed so energy statistics ($\langle E\rangle,\Delta E$) are constant; relative phases evolve.
- $(\psi_0+\psi_1)/\sqrt2$: $|\Psi|^2=\frac1L[1+\cos(kx-\omega t)]$, $\omega=E_1/\hbar$: pattern moves round the ring.
- $(\psi_n+\psi_{-n})/\sqrt2$: same phase for both ($E_n=E_{-n}$), so $|\Psi|^2=\frac2L\cos^2k_nx$ is stationary though not a momentum eigenstate.
- *Time is not an operator:* a $\hat T$ with $[\hat T,\hat H]=i\hbar$ would need an energy spectrum unbounded below; systems have a ground state. Ring momentum is discrete yet unbounded, since $x$ is periodic; time has no such periodicity.

**Diagnostic table** ($\Delta E$, $\Delta p$): $\psi_n$: yes/yes, 0, 0. $(\psi_n+\psi_{-n})/\sqrt2$: definite $E$, not $p$; $0$, $|p_n|$. $(\psi_0+\psi_1)/\sqrt2$: neither; $E_1/2$, $|p_1|/2$. Box $\sin$: definite $E$, not $p$; $0$, $n\pi\hbar/L$.

**Why operators.** A state alone does not answer "what do I get if I measure $A$?". The operator's eigenvalues are the possible outcomes, its eigenstates the states with a definite value, expansion coefficients give the Born-rule probabilities $|c_n|^2$, and the state collapses onto the eigenstate afterwards. Non-commutation encodes that incompatible quantities cannot both be sharp.

## From the post
Lecture note for today, tomorrow.

## Files
- [PH2113_states_operators_notes.pdf](https://drive.google.com/file/d/1vVCbbGYBGyblziDjyDiCIX3ipY9gj6xx/view?usp=drive_web)

Posted: [Classroom](https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODcyNDg0MDYxOTE1)

## Related
- [[06-quantum-mechanics/qm03-states-operators-and-measurement]]: their own notes on this topic
- [[06-quantum-mechanics/qm02-the-schrodinger-equation-and-stationary-states]]: stationary states and time evolution
- [[06-quantum-mechanics/qm04-the-particle-in-a-box]]: box states used in the uncertainty example
- [[06-quantum-mechanics/concepts/particle-on-a-ring]]: running example
- [[06-quantum-mechanics/concepts/commutator]]: compatibility and the uncertainty bound
- [[06-quantum-mechanics/concepts/canonical-commutation-relation]]: $[\hat x,\hat p]=i\hbar$
- [[06-quantum-mechanics/concepts/uncertainty-of-an-observable]]: definition of $\Delta A$
- [[06-quantum-mechanics/concepts/time-is-not-an-operator]]: section 9.3
- [[06-quantum-mechanics/concepts/parity-operator]]: parity example

<!-- kurooto:material8d55b07e -->
## Concepts in PH2113_states_operators_notes
[[zettel/schrodinger-equation-linearity-and-superposition]], [[zettel/linear-operator]], [[zettel/born-rule-and-expansion-postulate]], [[zettel/quantum-expectation-value]], [[zettel/macroscopic-correspondence-on-a-ring]], [[zettel/dynamical-probability-density-from-non-degenerate-superposition]]
<!-- /kurooto:material8d55b07e -->
