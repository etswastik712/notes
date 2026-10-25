---
id: ph2113/2026-09-07-matrices-expectation-uncertainty
aliases: [PH2113 matrices expectation uncertainty]
tags: [ph2113, lecture]
trust_tier: agent_written
---

# States, operators, bases, expectation values and uncertainty: from 2×2 matrices to wavefunctions

## Covered
(Classroom: PH2113_matrices_expectation_uncertainty.pdf; the teacher says it is very similar to [[ph2113/2026-08-31-states-operators-measurements-notes]] with a few more illustrative points.)

**Two-level system.** State $|\psi\rangle=(a,b)^T$, $|a|^2+|b|^2=1$. Observables are Hermitian matrices, e.g. $X=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix}$, $Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$. Eigenstates ($\pm1$): $|\pm z\rangle=(1,0)^T,(0,1)^T$; $|\pm x\rangle=\frac1{\sqrt2}(1,\pm1)^T$; $|\pm y\rangle=\frac1{\sqrt2}(1,\pm i)^T$. Eigenstate means definite value: $\hat A|a\rangle=a|a\rangle$ gives $a$ with certainty.

**Bases.** $|{+z}\rangle=\frac1{\sqrt2}(|{+x}\rangle+|{-x}\rangle)=\frac1{\sqrt2}(|{+y}\rangle+|{-y}\rangle)$: an eigenstate of $Z$ is a superposition of $X$ and $Y$ eigenstates. For $|\psi\rangle=c_1|a_1\rangle+c_2|a_2\rangle$, $P(a_i)=|c_i|^2$. Example: $\frac{\sqrt3}2|{+z}\rangle+\frac12|{-z}\rangle$ gives $Z=+1$ with prob. $3/4$, $-1$ with prob. $1/4$.
- *Basis change example:* $|{+x}\rangle=\frac{1-i}2|{+y}\rangle+\frac{1+i}2|{-y}\rangle$; $X|{+y}\rangle=i|{-y}\rangle$, $X|{-y}\rangle=-i|{+y}\rangle$; acting on the superposition returns $|{+x}\rangle$ with eigenvalue $+1$. In the $Y$ basis $X$ is represented by $\begin{pmatrix}0&-i\\i&0\end{pmatrix}$. Basis changes the coordinates, not the physics; eigenvalue equations hold in every basis.

**Expectation.** $\langle A\rangle=\langle\psi|A|\psi\rangle=|c_1|^2a_1+|c_2|^2a_2$, an average not necessarily an allowed outcome. $|{+x}\rangle$: $\langle X\rangle=1$, $\Delta X=0$. $|{+z}\rangle$ as $(|{+x}\rangle+|{-x}\rangle)/\sqrt2$: $\langle X\rangle=0$, though each measurement gives $\pm1$. $\frac{\sqrt3}2|{+z}\rangle+\frac12|{-z}\rangle$: $\langle Z\rangle=\frac12$.

**Wave mechanics dictionary.** State vector ↔ $\psi(x)$; Hermitian matrix ↔ operator $\hat x,\hat p,\hat H$; $A|a_n\rangle=a_n|a_n\rangle$ ↔ $\hat A\phi_n=a_n\phi_n$; $|\psi\rangle=\sum c_n|a_n\rangle$ ↔ $\psi=\sum c_n\phi_n$; probability $|c_n|^2$; expectation $\langle\psi|A|\psi\rangle$ ↔ $\int\psi^*\hat A\psi\,dx$. Continuous spectrum: $\psi(x)=\int dp\,c(p)\phi_p(x)$, $|c(p)|^2dp$ = probability of momentum in $[p,p+dp]$.

**Position representation.** $\langle A\rangle=\int dx\,\psi^*\hat A\psi$. Box $\psi_n=\sqrt{2/L}\sin(n\pi x/L)$: $\langle x\rangle=L/2$ (worked integral). Ring $e^{ik_nx}/\sqrt L$: $\langle p\rangle=\hbar k_n$, $\langle H\rangle=\hbar^2k_n^2/2m$. $\cos kx$: $\langle p\rangle=0$. Gaussian packet at $x_0$, mean wavenumber $k_0$: $\langle x\rangle=x_0$, $\langle p\rangle=\hbar k_0$. Energy eigenstate: $\langle H\rangle=E_n$.

**Uncertainty.** $\Delta A=\sqrt{\langle A^2\rangle-\langle A\rangle^2}$; eigenstate $\Rightarrow\Delta A=0$. $X$ in $|{+z}\rangle$: $\Delta X=1$. $Z$ in $\frac{\sqrt3}2|{+z}\rangle+\frac12|{-z}\rangle$: $\Delta Z=\sqrt3/2$. $\cos kx$: $\Delta p=\hbar|k|$ but $\Delta E=0$. Box ground state $\Delta x\Delta p\simeq0.568\hbar>\hbar/2$; minimum-uncertainty Gaussian $\Delta x\Delta p=\hbar/2$.

**Commutators.** $[A,B]=AB-BA$; $\Delta A\Delta B\ge\frac12|\langle[A,B]\rangle|$. $[X,Y]=2iZ$, $[Y,Z]=2iX$, $[Z,X]=2iY$. In $|{+z}\rangle$: $\langle Z\rangle=1$, $\Delta X=\Delta Y=1$, so $\Delta X\Delta Y=1=\frac12|\langle[X,Y]\rangle|$: the bound is saturated. Commuting: $A=Z$, $B=Z^2=I$. Free particle/ring: $[\hat H,\hat p]=0$. $[\hat x,\hat p]=i\hbar$ because the derivative in $\hat p$ also acts on the factor $x$: $(\hat x\hat p-\hat p\hat x)\psi=i\hbar\psi$.

**Comparison table.** $|{+x}\rangle$: $X=+1$ definite, $Y,Z$ not. $|{+z}\rangle$: $Z=+1$, $X,Y$ not. $e^{ikx}$ on ring: $p=\hbar k$ and $E=\hbar^2k^2/2m$ definite, position completely spread. $\cos kx$: energy definite, momentum $\pm\hbar k$. Box eigenstate: energy definite, momentum not. Localised Gaussian: neither $x$ nor $p$ exact.

## From the post
For today and tomorrow's lecture (very similar to last lecture note I shared earlier, just few illustrative points and examples included).

## Files
- [PH2113_matrices_expectation_uncertainty.pdf](https://drive.google.com/file/d/1BnwRAb6F7e7Rzjk367vwy6FuBnMzcX0r/view?usp=drive_web)

Posted: [Classroom](https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODcyODAwNzEyMjcx)

## Related
- [[ph2113/2026-08-31-states-operators-measurements-notes]]: the earlier lecture note this repeats and extends
- [[06-quantum-mechanics/qm03-states-operators-and-measurement]]: their own notes on this topic
- [[06-quantum-mechanics/concepts/hermitian-operator]]: observables as Hermitian matrices
- [[06-quantum-mechanics/concepts/commutator]]: commutators and the uncertainty bound
- [[06-quantum-mechanics/concepts/canonical-commutation-relation]]: $[\hat x,\hat p]=i\hbar$
