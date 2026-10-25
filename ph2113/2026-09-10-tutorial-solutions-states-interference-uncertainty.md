---
id: ph2113/2026-09-10-tutorial-solutions-states-interference-uncertainty
aliases: [PH2113 tutorial solutions: States, Interference and Uncertainty]
tags: [ph2113, solutions, agent_written]
trust_tier: agent_written
---

# Tutorial solutions: States, Interference and Uncertainty (2026-09-10)

## Covered
Solutions to the problem set [[ph2113/2026-09-08-tutorial-states-interference-uncertainty]]. (Classroom: PH2113_tutorial_solutions.pdf)

**Q1.** $\hat p\psi_\pm=\pm\hbar k\psi_\pm$.
- (a) $\psi_+$: $p=+\hbar k$ with certainty; $\psi_-$: $-\hbar k$ with certainty; $\Psi$: $\pm\hbar k$ with probability $\frac12$ each.
- (b) $\Psi$ is not a momentum eigenstate (two different eigenvalues), but both components have $E=p^2/2m=\hbar^2k^2/2m$, so $\Psi$ is an energy eigenstate.
- (c) $\langle p\rangle=0$, $\langle p^2\rangle=\hbar^2k^2$, $\Delta p=\hbar k$. $\langle p\rangle=0$ is only an average; every measurement gives $+\hbar k$ or $-\hbar k$.

**Q2.**
- (a) $|\Psi|^2=A^2(e^{i\varphi_1}+e^{i\varphi_2})(e^{-i\varphi_1}+e^{-i\varphi_2})=2A^2[1+\cos(\varphi_2-\varphi_1)]=4A^2\cos^2\frac{\varphi_2-\varphi_1}2$. Interference term: $2A^2\cos(\varphi_2-\varphi_1)$.
- (b) Bright when $\varphi_2-\varphi_1=2\pi n$; with $\varphi_2-\varphi_1\simeq\frac{2\pi d}\lambda\frac yD$: $y_n=n\lambda D/d$, spacing $\Delta y=\lambda D/d$.
- (c) Incoherent (probabilities add): $I=\frac12|\psi_1|^2+\frac12|\psi_2|^2=A^2$, no phase-dependent term; no coherent superposition with a definite relative phase.
- (d) $|\Psi|^2=2A^2[1+\cos(\varphi_2-\varphi_1+\alpha)]$: the fringe pattern shifts, spacing unchanged.

**Q3(A) pencil.**
- (a) $\Delta x\Delta p\ge\hbar/2$ forbids $\Delta x=\Delta p=0$.
- (b) Saturate the bound, $\Delta p=\hbar/2\Delta x$, so $s^2=(\Delta x)^2+\hbar^2/[4M^2\omega^2(\Delta x)^2]$; the minimum is where the two terms are equal: $\Delta x=\sqrt{\hbar/2M\omega}$, $\Delta p=\sqrt{\hbar M\omega/2}$, $s_{\min}=\sqrt{\hbar/M\omega}$.
- (c) $m=0.010$ kg, $\ell=0.15$ m: $M=1.33\times10^{-2}$ kg, $\omega=\sqrt{3(9.8)/2(0.15)}\simeq9.9\ \mathrm{s^{-1}}$, $\Delta x_{\min}\simeq2.0\times10^{-17}$ m, $s_{\min}\simeq2.8\times10^{-17}$ m. From $10^{-3}\simeq\frac{s_{\min}}2e^{\omega t}$: $t\simeq\frac1\omega\ln\frac{2\times10^{-3}}{s_{\min}}\simeq3.2$ s (the sheet's value; recomputing gives about 3.3 s). A microscopic spread is amplified to a visible one on an everyday timescale.
- (d) No new force: the initial position and momentum cannot both be sharp, and the unstable classical dynamics amplifies the unavoidable spread.

**Q3(B) Gaussian.** $|\psi|^2=\frac1{\sqrt{2\pi\sigma^2}}e^{-(x-x_0)^2/2\sigma^2}$, so $\langle x\rangle=x_0$, $\Delta x=\sigma$. With $\psi'=-\big(\frac{x-x_0}{2\sigma^2}+\ik_0\big)\psi$ (sheet: $d\psi/dx=[-(x-x_0)/2\sigma^2+ik_0]\psi$), $\langle p\rangle=\hbar k_0$, $\langle p^2\rangle=\hbar^2k_0^2+\hbar^2/4\sigma^2$, $\Delta p=\hbar/2\sigma$, so $\Delta x\Delta p=\hbar/2$. From $[\hat x,\hat p]=i\hbar$: $\Delta x\Delta p\ge\frac12|\langle[\hat x,\hat p]\rangle|=\hbar/2$. The Gaussian saturates the bound: it is a minimum-uncertainty state.

**Q4 ring, $\Psi=(\psi_{+k}+\psi_{-k})/\sqrt2$.**
- (a) Both components have $E=\hbar^2k^2/2m$, so $H\Psi=E\Psi$, $\Delta H=0$.
- (b) $\langle p\rangle=0$, $\langle p^2\rangle=\hbar^2k^2$, $\Delta p=\hbar k$.
- (c) $\Delta H\Delta p=0$ and $\frac12|\langle[H,p]\rangle|=0$: the relation reads $0\ge0$.
- (d) No contradiction: definite energy arises from the degeneracy $E(+k)=E(-k)$, while the state still contains two momentum values.
- (e) $[A,B]=0$ means the observables can have simultaneous eigenstates; it does not mean both uncertainties vanish in every state.

**E1.** (a) $X|{+x}\rangle=\frac1{\sqrt2}(1,1)^T=|{+x}\rangle$. (b) $X|{+y}\rangle=i|{-y}\rangle$, $X|{-y}\rangle=-i|{+y}\rangle$; acting on the $Y$-basis expansion, the terms recombine to $|{+x}\rangle$. (c) $|\frac{1\mp i}2|^2=\frac12$: $Y=\pm1$ with probability $\frac12$ each, $\langle Y\rangle=0$, $\Delta Y=1$.

**E2.** $|{+z}\rangle$: $X^2=Y^2=I$, $\langle X\rangle=\langle Y\rangle=0$, so $\Delta X=\Delta Y=1$, $\Delta X\Delta Y=1$. $\frac12|\langle[X,Y]\rangle|=\frac12|2i\langle Z\rangle|=1$: the bound is saturated. For $|{+x}\rangle$: $\Delta X=0$ but $\langle Z\rangle=0$, so the lower bound is 0 and the relation still holds.

**E3.** $|\psi(t)\rangle=\frac1{\sqrt2}(e^{-iE_1t/\hbar}|1\rangle+e^{-iE_2t/\hbar}|2\rangle)$. Energy probabilities stay $\frac12$ (phases have unit modulus); the relative phase $e^{-i(E_2-E_1)t/\hbar}$ matters for observables with off-diagonal elements, e.g. $X=|1\rangle\langle2|+|2\rangle\langle1|$ gives $\langle X\rangle=\cos\frac{(E_2-E_1)t}\hbar$.
Correction to Q3(B) above (a typo in my formula): the derivative is $\psi'(x)=\left[-\dfrac{x-x_0}{2\sigma^2}+ik_0\right]\psi(x)$, as in the sheet.

## From the post
Solution set for todays Tutorial.

## Files
- [PH2113_tutorial_solutions.pdf](https://drive.google.com/file/d/18tZJEyw-j-z7RcRNeryCSCGKL3TQtyPv/view?usp=drive_web) (read in full; the sheet's Q4(e) label is misplaced after its text)
- Classroom post: https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODcyODk2NDQyNDM0

## Related
- [[ph2113/2026-09-08-tutorial-states-interference-uncertainty]]: the problem statements
- [[ph2113/2026-09-07-matrices-expectation-uncertainty]]: matrix methods used in E1-E3
- [[ph2113/2026-08-31-states-operators-measurements-notes]]: measurement probabilities and time evolution
- [[06-quantum-mechanics/concepts/minimum-uncertainty-state]]: Gaussian saturation of the bound
- [[06-quantum-mechanics/concepts/heisenberg-uncertainty-principle]]: the pencil argument and $\Delta x\Delta p\ge\hbar/2$
