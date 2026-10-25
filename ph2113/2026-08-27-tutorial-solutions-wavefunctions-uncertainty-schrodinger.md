---
id: ph2113/2026-08-27-tutorial-solutions-wavefunctions-uncertainty-schrodinger
aliases: [PH2113 tutorial solutions]
tags: [ph2113, tutorial, solutions]
trust_tier: agent_written
---

# PH2113 Tutorial: short solution guide (wavefunctions, uncertainty, Schrödinger equation)

## Covered
Five tutorial problems with short solutions (Classroom: PH2113_Tutorial_Solutions_Wavefunctions_Uncertainty_Schrodinger.pdf).

1. **Uncertainty and localisation.** From $\Delta x\,\Delta p \ge \hbar/2$: $\Delta p_{\min}=\hbar/(2\Delta x)$. For $\Delta x = 10^{-10}$ m this is $\simeq 5.3\times10^{-25}$ kg m/s ($\hbar = 1.055\times10^{-34}$ J s, $\Delta x$ taken as $2\times10^{-10}$ in the denominator, i.e. $2\Delta x = 2\times 10^{-10}$ m). With $\Delta p \simeq m_e\Delta v$: $\Delta v \simeq 5.8\times10^5$ m/s $\simeq 1.9\times10^{-3}c$, so the estimate is non-relativistic. Setting the momentum scale to $m_e c$ gives $\Delta x \sim \hbar/(m_e c)\simeq 3.9\times10^{-13}$ m (the exact lower-bound equality gives an extra factor $1/2$): the scale where relativistic effects can no longer be ignored.
2. **Acceptable wavefunctions.**
   - $\psi_1 = Ae^{-|x|/a}$: $1 = 2|A|^2\int_0^\infty e^{-2x/a}dx = |A|^2 a$, so $A = 1/\sqrt a$ (up to a phase). Normalisable.
   - $\psi_2$: $|\psi_2|^2\sim 1/|x|$ at large $|x|$, and $\int dx/x$ diverges. Not normalisable.
   - $\psi_3 = Ae^{x^2/a^2}$ grows exponentially. Not normalisable.
   - $\psi_4$: normalisable ($1=|A|^2\int_0^\infty e^{-2x/a}dx = |A|^2 a/2$, so $A=\sqrt{2/a}$) but discontinuous at $x=0$ (left limit 0, right value $A$), so it cannot solve the Schrödinger equation there for an ordinary finite nonsingular potential.
3. **Periodic boundary condition, ring.** Normalise $\psi = Ae^{ikx}$ on $0\le x<L$: $|A|^2L = 1$, $A=1/\sqrt L$. Periodicity: $e^{ikL}=1\Rightarrow k_n = 2\pi n/L$, so $E_n = \hbar^2k_n^2/2m = 2\pi^2\hbar^2n^2/(mL^2)$. Spacing $\Delta k = 2\pi/L\to0$ as $L\to\infty$: discrete spectrum becomes a continuum. For a ring $L=2\pi R$: $E_n=\hbar^2n^2/(2mR^2)$. States $n$ and $-n$ move in opposite directions but have the same energy since $E_n\propto n^2$.
4. **Probability conservation.** Take the TDSE $i\hbar\Psi_t = -\frac{\hbar^2}{2m}\Psi_{xx}+V\Psi$ and its conjugate; multiply the first by $\Psi^*$, the second by $\Psi$ and combine. For real $V$ the $V$ terms cancel:
   $$\frac{\partial|\Psi|^2}{\partial t} = -\frac{\partial}{\partial x}\left[\frac{\hbar}{2mi}(\Psi^*\Psi' - \Psi\Psi'^*)\right],$$
   i.e. $\partial_t\rho+\partial_x j=0$. Integrating over all space, $\frac{d}{dt}\int|\Psi|^2dx = -[j]_{-\infty}^{\infty}=0$ when the boundary current vanishes, so total probability is conserved.
5. **Global vs relative phase.** If $\Psi'=e^{i\alpha}\Psi$ then $|\Psi'|^2=|\Psi|^2$: an overall phase changes no probability. For $\psi = e^{ikx}+e^{i\varphi}e^{-ikx}$: $|\psi|^2 = 2+2\cos(2kx-\varphi)$; changing the relative phase $\varphi$ shifts the interference pattern, so relative phase can be observable.

**Further thought (brief guide).**
- $e^{\pm ikx}$ are momentum states with $p=\pm\hbar k$; $\cos kx=(e^{ikx}+e^{-ikx})/2$, $\sin kx=(e^{ikx}-e^{-ikx})/2i$. Exponentials suit direction of motion; sine/cosine often suit boundaries and symmetry.
- $e^{ikx}$ and $e^{-ikx}$ are different states: a momentum measurement distinguishes $+\hbar k$ from $-\hbar k$.
- For finite $L$, $|\psi_L|^2=1/L$ and total probability is 1; as $L$ grows the probability spreads over a larger region, and the pointwise limit $\psi_L\to0$ does not mean the particle disappears.
- Quantisation comes from the Schrödinger equation together with physical boundary conditions: the same free-particle equation has continuous energies on the line and discrete energies under periodic boundary conditions.

## From the post
Solution set.

## Files
- [PH2113_Tutorial_Solutions_Wavefunctions_Uncertainty_Schrodinger.pdf](https://drive.google.com/file/d/1VGOYkrQ0TXmGg0YCLMu6ZeXkO-O118XA/view?usp=drive_web)

Posted: [Classroom](https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODc2MTAyMDU2NTkw)

## Related
- [[06-quantum-mechanics/concepts/particle-on-a-ring]]: problem 3 is the ring quantisation
- [[06-quantum-mechanics/concepts/probability-current]]: problem 4, continuity equation
- [[06-quantum-mechanics/concepts/heisenberg-uncertainty-principle]]: problem 1
- [[06-quantum-mechanics/concepts/normalisation-of-a-wavefunction]]: problem 2
- [[06-quantum-mechanics/concepts/boundary-conditions-and-quantisation]]: why periodicity quantises $k$
