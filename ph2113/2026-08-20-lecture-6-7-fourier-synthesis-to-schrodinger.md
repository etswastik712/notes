---
id: ph2113/2026-08-20-lecture-6-7-fourier-synthesis-to-schrodinger
aliases: [PH2113 Lectures 6-7, Wave-particle duality and the Schrödinger equation]
tags: [ph2113, lecture, uncertainty, schrodinger]
trust_tier: agent_written
---

# Lectures 6-7: Wave-particle duality and the Schrödinger equation (2026-08-20)

## Covered
Source: Classroom, PH2113_Lecture6-7.pdf (read in full; the PDF header says "Lecture 7: Uncertainty → the Schrödinger equation").

**1. Two idealised extremes.** Neither is an ordinary normalisable wavefunction.
- Plane wave $\psi=Ae^{i(kx-\omega t)}$: one $k$, so one $p=\hbar k$; $\Delta p=0$; $|\psi|^2$ constant on the whole line so $\Delta x$ is not finite.
- $\delta(x-x_0)$: all wavenumbers present, so $\Delta x\to0$, $\Delta p\to\infty$.
- To quantify the trade-off with two finite standard deviations one needs a normalisable state.

**2. Fourier synthesis (purely a wave statement).** Narrow band of $k$ gives a broad packet in $x$; wide band gives a narrow packet: narrow in $k\Leftrightarrow$ broad in $x$. True for sound, water waves, radio, light; not yet quantum mechanics.

**3. Classical wave bound, Gaussian.** $\psi(x)=(2\pi\sigma^2)^{-1/4}e^{-x^2/4\sigma^2}$, $\Delta x=\sigma$. With $\tilde\psi(k)=\frac1{\sqrt{2\pi}}\int\psi e^{-ikx}dx$:
$$\tilde\psi(k)=\left(\frac{2\sigma^2}{\pi}\right)^{1/4}e^{-\sigma^2k^2},\quad \Delta k=\frac1{2\sigma},\quad \Delta x\,\Delta k=\frac12.$$
For any square-integrable amplitude whose standard deviations exist, $\Delta x\,\Delta k\ge\tfrac12$; the Gaussian is the minimum-bandwidth shape. A theorem about Fourier pairs, not specifically quantum.

**4. Two classical pictures.** Classical particle: $x(t),p(t)$ simultaneously definite, $\Delta x\Delta p$ can be zero. Classical wave: $\Delta x\,\Delta k\gtrsim1$ (order of magnitude). Quantum matter is neither: detections are localised, yet it diffracts and interferes.

**5. Quantum matter.** The missing ingredient is interpreting Fourier coefficients as amplitudes: $|\tilde\psi(k)|^2dk$ is the probability that the wavenumber lies in $dk$. With $p=\hbar k$, $\Delta p=\hbar\Delta k$, so
$$\Delta x\,\Delta p=\hbar\,\Delta x\,\Delta k\ge\frac\hbar2.$$
Wave mathematics supplies the width trade-off; quantum mechanics gives it meaning via $p=\hbar k$ and the probabilistic reading. Tennis ball, 57 g localised to 1 mm: $\Delta v\gtrsim\hbar/(2m\Delta x)\approx9\times10^{-31}$ m/s, irrelevant; for an electron on an atomic length scale the velocity scale is enormous.

**6. Hydrogen scale.** Size $r$ needs $p\sim\hbar/r$ (an order-of-magnitude statement, not $\Delta p=\hbar/2r$):
$$E(r)\sim\frac{\hbar^2}{2m_er^2}-\frac{e^2}{4\pi\epsilon_0r}.$$
Minimising gives $r_{\min}=a_0=\frac{4\pi\epsilon_0\hbar^2}{m_ee^2}=5.292\times10^{-11}$ m and $E_{\min}\sim-2.180\times10^{-18}$ J $=-13.61$ eV. Kinetic term $\propto1/r^2$ beats Coulomb $\propto1/r$, so no collapse. The scaling and stability are robust; the exact energy and wavefunction come from the Schrödinger equation (the numerical agreement is unusually favourable for Coulomb).

**7. What a Fourier transform means.** Analysis: $\tilde\psi(k)=\frac1{\sqrt{2\pi}}\int\psi(x)e^{-ikx}dx$ ("which wavelengths are present?"); synthesis: $\psi(x)=\frac1{\sqrt{2\pi}}\int\tilde\psi(k)e^{ikx}dk$. A change of description, no new physics; with $p=\hbar k$ it is the momentum content.

**8. Why a new dynamical law.** Born's rule and Fourier analysis do not say how $\psi$ changes in time. Need: given $\psi(x,0)$ predict $\psi(x,t)$, including $V(x)$. The Schrödinger equation is a **postulate** of non-relativistic QM; $E=\hbar\omega$, $p=\hbar k$, $E=p^2/2m+V$ motivate its form but do not logically derive it; justification is experimental.

**9. Operators from a plane wave.** For $\psi=Ae^{i(kx-\omega t)}$: $-i\hbar\partial_x\psi=\hbar k\psi=p\psi$ and $i\hbar\partial_t\psi=\hbar\omega\psi=E\psi$, so
$$\hat p=-i\hbar\frac{\partial}{\partial x},\qquad \hat E=i\hbar\frac{\partial}{\partial t}.$$
Linear, so they act consistently on superpositions of plane waves.

**10. TDSE.** From $E=p^2/2m+V(x)$:
$$i\hbar\frac{\partial\psi}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}+V(x)\psi.$$
The factor $i$ gives phase rotation rather than diffusive decay and, for real $V$, unitary evolution and probability conservation.

**11. Stationary states / TISE.** $\psi(x,t)=\varphi(x)e^{-iEt/\hbar}$ gives $E\varphi=-\frac{\hbar^2}{2m}\varphi''+V\varphi$. Input $V(x)$; output allowed $E$ and shapes $\varphi$. $|\psi|^2=|\varphi|^2$ is time independent although $\psi$ is not.

**12. Free-particle check.** $V=0$, plane wave: $\hbar\omega=\hbar^2k^2/2m=p^2/2m$, so $\omega(k)=\hbar k^2/2m$.

**13. Probability conservation.** With $P=|\psi|^2$ and real $V$: $\partial_tP+\partial_xj=0$,
$$j=\frac\hbar{2mi}\left(\psi^*\frac{\partial\psi}{\partial x}-\psi\frac{\partial\psi^*}{\partial x}\right).$$
Then $\frac d{dt}\int|\psi|^2dx=-[j]_{-\infty}^{\infty}=0$ for a normalisable state with vanishing boundary current: consistent with Born's rule.

## From the post
"Todays lecture note."

## Files
- [PH2113_Lecture6-7.pdf](https://drive.google.com/file/d/1oGV_WL8DZCu4ubquKq3r1re4lWEVfKZo/view?usp=drive_web)
- Classroom post: https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODU1OTc1MDM4NTk5

## Related
- [[ph2113/2026-08-18-wavefunction-to-uncertainty]]: the preceding lecture; plane wave, $\delta$, Gaussian and the hydrogen estimate are developed there
- [[ph2113/2026-08-24-lecture-8-uncertainty-wavefunctions-schrodinger]]: next lecture; the same TDSE motivation plus acceptable wavefunctions
- [[ph2113/2026-08-27-tutorial-solutions-wavefunctions-uncertainty-schrodinger]]: probability conservation (problem 4) and uncertainty estimates
- [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]]: Fourier/Gaussian primer on the same transform pair
