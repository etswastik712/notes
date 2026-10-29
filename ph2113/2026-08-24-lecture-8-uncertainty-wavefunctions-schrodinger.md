---
id: ph2113/2026-08-24-lecture-8-uncertainty-wavefunctions-schrodinger
aliases: [PH2113 Lecture 8, Uncertainty, physical wavefunctions and the Schrödinger equation]
tags: [ph2113, lecture, uncertainty, wavefunction, schrodinger]
trust_tier: agent_written
---

# Lecture 8: Uncertainty, physical wavefunctions, and the Schrödinger equation (2026-08-24)

## Covered
Source: Classroom, PH2113_Lecture8_Uncertainty_Wavefunctions_Schrodinger (1).pdf (read in full).

**1. Meaning of $\Delta x\Delta p\ge\hbar/2$.** $\Delta x,\Delta p$ are standard deviations of position and momentum outcomes over identically prepared systems. It is not about instrument imperfection: the state itself cannot have both distributions arbitrarily narrow. A plane wave $Ae^{ikx}$ has one $k$, $p=\hbar k$, but is not localised; a localised packet $\psi=\int A(k)e^{ikx}dk$ needs a range of $k$: small $\Delta x\Rightarrow$ large $\Delta k$, $\Delta p=\hbar\Delta k$.

**2. Validity limit: the Compton scale.** $\Delta p\sim\hbar/\Delta x$; when $\Delta x\sim\hbar/(mc)$, $\Delta p\sim mc$ and relativistic effects matter. $\hbar/(mc)$ is the *reduced* Compton wavelength; $\lambda_C=h/(mc)=2\pi\hbar/(mc)$. For the electron $\hbar/(mc)\approx3.9\times10^{-13}$ m. It marks where the non-relativistic one-particle description stops being trustworthy, not a minimum size: electron scattering probes down to about $10^{-18}$ m with no internal structure.
- *Dimensional analysis:* $\ell=\hbar^ac^bm^d$ with $[\hbar]=\text{kg m}^2\text{s}^{-1}$, $[c]=\text{m s}^{-1}$, $[m]=\text{kg}$. Powers: kg: $a+d=0$; m: $2a+b=1$; s: $-a-b=0$. Unique solution $a=1,b=-1,d=-1$, so $\ell\propto\hbar/(mc)$. It fixes the scaling only, not the numerical prefactor nor the physical relevance.

**3. Which functions can be states.** Born: $dP=|\psi|^2dx$; ordinary localised state has $\int|\psi|^2dx<\infty$, normalised to 1. Elementary requirements: single-valued; $|\psi|^2$ integrable; obeys the problem's boundary conditions; for regular finite potentials, $\psi$ continuous (and normally $\psi'$ continuous). Distinguish (i) admissible as a state from (ii) solving the Schrödinger equation for a given $V$; a normalisable function can fail to be an eigenfunction of $\hat H$.

**4. Examples (admissible?).**
1. $Ae^{-ax^2}$: normalisable, allowed.
2. $Ae^{-a|x|}$: normalisable, allowed as a state; the cusp at 0 means it is not a stationary solution for a regular finite potential there, but can occur for a $\delta$-potential.
3. $Ae^{ax^2}$: $\int|\psi|^2=\infty$, not allowed on $(-\infty,\infty)$.
4. $A/\sqrt{1+|x|}$: $\to0$ but $|\psi|^2\sim1/|x|$, integral diverges: not normalisable. $\psi\to0$ is not sufficient.
5. $A/(1+|x|)$: $|\psi|^2\sim1/x^2$, converges: allowed.
6. $A/x$ on a region containing $0$: $|\psi|^2\sim1/x^2$ diverges at the origin: not allowed.
7. Constant $A$: not normalisable on the line; on $0\le x\le L$, $|A|^2L=1$, $A=1/\sqrt L$. Acceptability depends on domain and boundary conditions.

**5. The plane wave** $Ae^{ikx}$ has $|\psi|^2=|A|^2$, not normalisable on the line: an idealised state of exact momentum, handled as a generalised state; wave packets are the physical ones.

**6-7. Dynamics: the TDSE is a postulate.**
$$i\hbar\frac{\partial\psi}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}+V(x,t)\psi.$$
Not derived from classical mechanics; justified by agreement with experiment.

**8. Consistency check with a plane wave** (constant $V$), $\psi=Ae^{i(kx-\omega t)}$, using $E=\hbar\omega$, $p=\hbar k$: $i\hbar\partial_t\psi=E\psi$, $-i\hbar\partial_x\psi=p\psi$, $-\frac{\hbar^2}{2m}\partial_x^2\psi=\frac{p^2}{2m}\psi$, hence $E=p^2/2m+V$. A check, not a derivation.

**9. Why derivatives.** $\partial_t$ extracts $\omega$, so $E\leftrightarrow i\hbar\partial_t$; $\partial_x$ extracts $k$, so $p\leftrightarrow-i\hbar\partial_x$ (to be called operators later).

**10. Free particle.** $V=0$: $\hbar\omega=\hbar^2k^2/2m$, i.e. $E=p^2/2m$.

**11. TISE.** For $V=V(x)$, $\psi=\varphi(x)T(t)$ gives $i\hbar\frac1T\frac{dT}{dt}=-\frac{\hbar^2}{2m}\frac1\varphi\varphi''+V(x)=E$, so $T=e^{-iEt/\hbar}$ and
$$-\frac{\hbar^2}{2m}\varphi''+V\varphi=E\varphi,\qquad \psi=\varphi(x)e^{-iEt/\hbar},\ |\psi|^2=|\varphi|^2.$$
Stationary states.

**12. Is energy automatically discrete? No.** Free particle: any real $k$, $E=\hbar^2k^2/2m$ continuous. Discreteness comes from boundary conditions allowing only selected wavelengths, hence momenta $p=h/\lambda$ and energies $p^2/2m$.

**Summary of the note:** uncertainty is an intrinsic spread; localisation to $\hbar/mc$ ends the non-relativistic regime (fixed uniquely by dimensional analysis, a validity threshold, not a size); states must be normalisable (domain and boundary conditions matter); the TDSE is a postulate; plane-wave check gives $E=p^2/2m+V$; stationary states obey the TISE. Next: why boundary conditions give discrete energies.

## From the post
"Todays lecture note attached. Tutorials: Thursday this week and Tuesday next week (will confirm later). We'll have Quiz next week Thursday."

## Files
- [PH2113_Lecture8_Uncertainty_Wavefunctions_Schrodinger (1).pdf](https://drive.google.com/file/d/1HOiv-dXu74qPdtV8_WVI_U1i0J8GU8Mx/view?usp=drive_web)
- Classroom post: https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODU2MDg4Mjg1OTgz

## Related
- [[ph2113/2026-08-20-lecture-6-7-fourier-synthesis-to-schrodinger]]: previous lecture; same TDSE/operator motivation
- [[ph2113/2026-08-25-lecture-9-free-particle-ring-general-properties]]: next lecture; boundary conditions and discrete spectra
- [[ph2113/2026-08-27-tutorial-solutions-wavefunctions-uncertainty-schrodinger]]: problems 1-2 practise the Compton-scale estimate and acceptable wavefunctions
- [[ph2113/2026-08-06-lecture-3-compton-scattering]]: where $\lambda_C=h/m_ec$ was introduced

<!-- kurooto:materialcba26064 -->
## Concepts in PH2113_Lecture8_Uncertainty_Wavefunctions_Schrodinger (1)
[[zettel/position-momentum-uncertainty-relation-from-fourier-transform]], [[zettel/reduced-compton-wavelength-validity-threshold]], [[zettel/delocalized-plane-wave-idealization]], [[zettel/time-independent-schrodinger-equation]], [[zettel/differential-coordinate-representations-of-energy-and-momentum]], [[zettel/free-particle-dispersion-relation-in-schrodinger-theory]], [[zettel/particle-in-a-box-time-evolution]], [[zettel/boundary-induced-energy-quantization]]
<!-- /kurooto:materialcba26064 -->
