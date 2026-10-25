---
id: ph2113/2026-08-18-wavefunction-to-uncertainty
aliases: [From the wavefunction to the uncertainty principle, PH2113 wavefunction lecture]
tags: [ph2113, lecture, wavefunction, uncertainty]
trust_tier: agent_written
---

# From the wavefunction to the uncertainty principle (2026-08-18)

## Covered
Source: Classroom, PH2113_Wavefunction_to_Uncertainty. Page one text was in the batch; the rest was read in full.

**1. The double slit forces a probabilistic reading.** Electrons arrive one at a time as single flashes; accumulated flashes form an interference pattern, with positions where electrons never arrive even though each slit alone would deliver them. A definite path through one slit cannot do this. Resolution: predict the probability of arrival, obtained from a wave amplitude so that amplitudes can cancel.

**2. Born rule.** The state is a wavefunction $\psi(x,t)$; probability of finding the particle in $[x,x+dx]$ is
$$P(x,t)\,dx=|\psi(x,t)|^2dx,\qquad \int_{-\infty}^{\infty}|\psi|^2dx=1.$$
$\psi$ adds when two paths are available, not the probability; where $\psi_1+\psi_2=0$ the probability vanishes (dark fringes).

**3. Candidate $\psi=A\cos kx$.** $k=2\pi/\lambda$, $p=h/\lambda=\hbar k$; a single $k$ means a single momentum. $A$ is fixed by normalisation (only $|\psi|^2$ is measurable). $|\psi|^2=A^2\cos^2kx=\tfrac{A^2}2[1+\cos2kx]$ oscillates forever: not localised, $\Delta x=\infty$, and $\int A^2\cos^2kx\,dx$ diverges so $A$ cannot be fixed. Since $\cos kx=\tfrac12(e^{ikx}+e^{-ikx})$ it is a standing wave, an equal mixture of $+\hbar k$ and $-\hbar k$.

**4. Complex $\psi$.** A particle moving one way with momentum $\hbar k$ needs the complex travelling wave $e^{i(kx-\omega t)}$. Measurable: $P=|\psi|^2=\psi^*\psi$. The phase does not show in $P$ for a single wave but produces interference when two waves are added.

**5. Free particle.** $\psi=Ae^{i(kx-\omega t)}$ has $P=|A|^2$, constant in $x$ and $t$: $\Delta x=\infty$ (not normalisable) and $\Delta p=0$. Definite momentum costs all position knowledge.

**6. Localising by a single slit.** Slit width $a$: $\Delta x\approx a$; first minimum at $\sin\theta=\lambda/a$; transverse momentum $\Delta p_x\approx p\sin\theta=(h/\lambda)(\lambda/a)=h/a$, so $\Delta x\,\Delta p_x\approx h$. Narrowing the slit widens the pattern.

**7. Superposing waves.** $e^{ik_1x}+e^{ik_2x}=2\cos[(k_1-k_2)x/2]\,e^{i(k_1+k_2)x/2}$: carrier $e^{i\bar kx}$ times envelope $2\cos(\Delta kx/2)$, with exact zeros at $x_n=(2n+1)\pi/\Delta k$, spacing $2\pi/\Delta k$. To localise a particle, superpose many $k$ so they cancel except in one small region.

**8. Delta function.** Equal weights over $-K\le k\le K$: $\psi(x)=\frac1{2\pi}\int_{-K}^{K}e^{ikx}dk=\frac{\sin Kx}{\pi x}$, peak height $K/\pi$, first zeros $\pm\pi/K$, so $\Delta x\,\Delta k\approx\pi$ independent of $K$. $K\to\infty$: $\frac1{2\pi}\int e^{ikx}dk=\delta(x)$, with $\Delta x=0$, $\Delta p=\infty$, the opposite extreme to the plane wave. Both are unphysical.

**9. Gaussian packet.**
$$\psi(x)=(2\pi\sigma^2)^{-1/4}e^{-x^2/4\sigma^2},\quad |\psi|^2=(2\pi\sigma^2)^{-1/2}e^{-x^2/2\sigma^2},\quad \Delta x=\sigma.$$
$\varphi(k)=\frac1{\sqrt{2\pi}}\int\psi e^{-ikx}dx=(2\sigma^2/\pi)^{1/4}e^{-\sigma^2k^2}$, $|\varphi|^2\propto e^{-2\sigma^2k^2}$ with variance $1/4\sigma^2$, so $\Delta k=1/2\sigma$, $\Delta p=\hbar/2\sigma$ and
$$\Delta x\,\Delta p=\hbar/2.$$
The Gaussian saturates the bound; the Heisenberg principle is $\Delta x\,\Delta p\ge\hbar/2$. It is not about clumsy measurement: a state with both small does not exist. Consistent with plane wave ($\infty\cdot0$), delta ($0\cdot\infty$), Gaussian.

**10. Hydrogen estimate.** Confinement to size $r$ gives $\Delta p\approx\hbar/r$ and
$$E(r)=\frac{\hbar^2}{2m_er^2}-\frac{e^2}{4\pi\varepsilon_0r}.$$
$dE/dr=0\Rightarrow r_{\min}=\frac{4\pi\varepsilon_0\hbar^2}{m_ee^2}=a_0=5.292\times10^{-11}$ m, $E_{\min}=-\frac{\hbar^2}{2m_ea_0^2}=-\frac{m_ee^4}{2(4\pi\varepsilon_0)^2\hbar^2}=-2.180\times10^{-18}\,\text{J}=-13.61$ eV (measured 13.606 eV, 0.529 Å). Squeezing $r$ raises kinetic energy as $1/r^2$, faster than the potential falls as $1/r$, so the atom is stable. Caution from the note: with the strict bound $\Delta p\ge\hbar/2r$ one gets $r_{\min}=a_0/4$ and $E=-54.4$ eV; trust the scaling, not the prefactor.

## From the post
"Todays lecture note attached. Also Thursday we'll have regular lecture at NLH."

## Files
- [PH2113_Wavefunction_to_Uncertainty (1).pdf](https://drive.google.com/file/d/1xePvpLPCOTNh-j-7qQD9Skj2Y8kokv7u/view?usp=drive_web)

## Related
- [[ph2113/2026-08-11-problem-set-1]]: Problems 6-8 on the plane wave and Born rule
- [[ph2113/2026-08-31-states-operators-measurements-notes]]: operator and commutator form of the uncertainty relation
- [[ph2113/2026-09-10-tutorial-solutions-states-interference-uncertainty]]: Gaussian $\Delta x\Delta p$ and uncertainty estimates
- [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]]: Fourier/Gaussian primer
