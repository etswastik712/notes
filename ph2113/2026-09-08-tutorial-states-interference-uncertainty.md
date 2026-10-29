---
id: ph2113/2026-09-08-tutorial-states-interference-uncertainty
aliases: [PH2113 tutorial: States, Interference and Uncertainty]
tags: [ph2113, problem-set, agent_written]
trust_tier: agent_written
---

# Tutorial: States, Interference and Uncertainty (problem set, 2026-09-08)

## Covered
Problem set (worked solutions are in [[ph2113/2026-09-10-tutorial-solutions-states-interference-uncertainty]]). Given relations: $\langle A\rangle=\int\psi^*\hat A\psi\,dx$, $\Delta A=\sqrt{\langle A^2\rangle-\langle A\rangle^2}$, $\Delta A\,\Delta B\ge\tfrac12|\langle[\hat A,\hat B]\rangle|$, $\hat x=x$, $\hat p=-i\hbar\,d/dx$, $[\hat x,\hat p]=i\hbar$. (Classroom: PH2113_tutorial-pdf.pdf)

Problems and what each practises:
- Q1 State, eigenstate, superposition: free particle with $\psi_\pm=e^{\pm ikx}/\sqrt L$, $\Psi=(\psi_++\psi_-)/\sqrt2$. (a) possible momentum outcomes; (b) is $\Psi$ a momentum / energy eigenstate (for $H=p^2/2m$); (c) $\langle p\rangle$, $\Delta p$, and the difference between "average momentum zero" and "momentum definitely zero".
- Q2 Double slit from superposition: amplitudes $\psi_j=Ae^{i\varphi_j}$. (a) show $|\Psi|^2=2A^2[1+\cos(\varphi_2-\varphi_1)]=4A^2\cos^2\frac{\varphi_2-\varphi_1}{2}$ and identify the interference term; (b) with $\varphi_2-\varphi_1\simeq\frac{2\pi d}{\lambda}\frac yD$ find bright fringes and spacing; (c) intensity when the particle goes through slit 1 or slit 2 incoherently (half the runs each) and why interference vanishes; (d) effect of a constant relative phase $\alpha$ in $\Psi=\psi_1+e^{i\alpha}\psi_2$.
- Q3(A) Balanced pencil as inverted oscillator: $M=4m/3$, $\omega=\sqrt{3g/2\ell}$, $x(t)=x_0\cosh\omega t+\frac{p_0}{M\omega}\sinh\omega t$ (given, no derivation needed). (a) why $\Delta x=\Delta p=0$ is forbidden; (b) minimise the seed $s^2=(\Delta x)^2+(\Delta p/M\omega)^2$ using $\Delta x\Delta p\ge\hbar/2$, giving $\Delta x=\sqrt{\hbar/2M\omega}$, $\Delta p=\sqrt{\hbar M\omega/2}$, $s_{\min}=\sqrt{\hbar/M\omega}$; (c) numbers for $m=10$ g, $\ell=15$ cm, and the time for $x_{\rm rms}\sim\frac{s_{\min}}2e^{\omega t}$ to reach 1 mm; (d) whether the uncertainty principle acts as a force.
- Q3(B) Gaussian wave packet $\psi=(2\pi\sigma^2)^{-1/4}\exp[-(x-x_0)^2/4\sigma^2+ik_0x]$: (e) show $\langle x\rangle=x_0$, $\Delta x=\sigma$, $\langle p\rangle=\hbar k_0$, $\langle p^2\rangle=\hbar^2k_0^2+\hbar^2/4\sigma^2$, $\Delta p=\hbar/2\sigma$; (f) show $\Delta x\Delta p=\hbar/2$, obtain the bound from $[x,p]=i\hbar$ alone, and say what is special about the Gaussian.
- Q4 Vanishing commutator: free particle on a ring, $[H,p]=0$, $\Psi=\sqrt{2/L}\cos kx$. (a) definite energy, $\Delta H$; (b) $\langle p\rangle,\langle p^2\rangle,\Delta p$; (c) both sides of $\Delta H\Delta p\ge\frac12|\langle[H,p]\rangle|$; (d) why $[H,p]=0$, $\Delta H=0$, $\Delta p\ne0$ is no contradiction (role of the degeneracy $E(+k)=E(-k)$); (e) what $[A,B]=0$ does and does not mean for uncertainties.
- Extra practice, two-state matrices: $X=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix}$, $|{+x}\rangle=\frac1{\sqrt2}(1,1)^T$, $|{\pm y}\rangle=\frac1{\sqrt2}(1,\pm i)^T$.
  - E1: same state in two eigenbases, $|{+x}\rangle=\frac{1-i}2|{+y}\rangle+\frac{1+i}2|{-y}\rangle$; verify $X|{+x}\rangle=|{+x}\rangle$, show $X|{+y}\rangle=i|{-y}\rangle$, $X|{-y}\rangle=-i|{+y}\rangle$ and recombine; measure $Y$ in $|{+x}\rangle$ (probabilities, $\langle Y\rangle$, $\Delta Y$).
  - E2: uncertainty from $[X,Y]=2iZ$ for $|{+z}\rangle$ and $|{+x}\rangle$.
  - E3: time evolution of $\frac1{\sqrt2}(|1\rangle+|2\rangle)$, fixed energy probabilities vs changing relative phase, an observable sensitive to it.

## From the post
Problem set.

## Files
- [PH2113_tutorial-pdf.pdf](https://drive.google.com/file/d/1ElcXuvw6dPxpk238k3Qcq-uZhSOK4rtb/view?usp=drive_web) (read in full)
- Classroom post: https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODcyODMzNDExNDY0

## Related
- [[ph2113/2026-08-31-states-operators-measurements-notes]]: states, Born rule, expectation, uncertainty these problems use
- [[ph2113/2026-09-07-matrices-expectation-uncertainty]]: the 2×2 matrix machinery for E1-E3
- [[06-quantum-mechanics/concepts/generalised-uncertainty-principle]]: the $\Delta A\Delta B\ge\frac12|\langle[A,B]\rangle|$ relation
- [[06-quantum-mechanics/concepts/gaussian-wave-packet]]: Q3(B)
- [[06-quantum-mechanics/concepts/superposition-principle]]: Q1 and Q2

<!-- kurooto:material5bbd5fbd -->
## Concepts in PH2113_tutorial-pdf
[[zettel/energy-eigenstate-superposition-with-momentum-degeneracy]], [[zettel/dynamical-amplification-of-quantum-uncertainty]], [[zettel/simultaneous-eigenstates-and-commuting-observables]], [[zettel/schrodinger-equation-linearity-and-superposition]]
<!-- /kurooto:material5bbd5fbd -->
