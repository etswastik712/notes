---
id: ph2113/2026-08-06-lecture-3-compton-scattering
aliases: [PH2113 Lecture 3, Compton derivation, Thomson scattering]
tags: [ph2113, lecture, compton, thomson]
trust_tier: agent_written
---

# Lecture 3: Compton scattering, photon recoil and the classical limit (2026-08-06)

## Covered
Source: Classroom, PH2113_Lecture3 (the derivation is in Appendices A-D). The first 12,272 of 27,971 characters were seen in the batch and the rest was read in full; the final lines of Appendix D (recoil angle) were cut off.

**Scattering and measurement.** A beam is sent at a target and detectors record direction, energy, momentum. Compton: X-rays of wavelength $\lambda$, scattered radiation detected at angle $\theta$ from the beam. Free-and-at-rest approximation holds when the photon energy far exceeds the binding energy of an outer electron. Measured: a component with $\lambda'>\lambda$; shift depends on $\theta$ (zero forward, increasing with angle); electron recoils; for approximately free electrons the shifted component follows the same angular law for different target materials.

**Shift law.**
$$\Delta\lambda=\lambda'-\lambda=\frac h{m_ec}(1-\cos\theta)=\lambda_C(1-\cos\theta),\quad \lambda_C=\frac{6.62607015\times10^{-34}}{(9.109\times10^{-31})(2.99792458\times10^{8})}\,\text{m}=2.426\ \text{pm}.$$
At $90^\circ$, $\Delta\lambda=\lambda_C=2.426$ pm; at $180^\circ$, $\Delta\lambda=2\lambda_C=4.853$ pm (the maximum). Table: 45°: 0.711 pm; 135°: 4.142 pm.

**Particle picture.** $E_\gamma=hc/\lambda$, $p_\gamma=E_\gamma/c=h/\lambda$; conservation
$$E_\gamma+m_ec^2=E'_\gamma+E_e,\qquad \mathbf p_\gamma=\mathbf p'_\gamma+\mathbf p_e.$$
$\lambda'>\lambda$ means $E'_\gamma<E_\gamma$, $p'_\gamma<p_\gamma$; the missing energy and momentum appear as electron kinetic energy $K_e=E_\gamma-E'_\gamma$ and recoil momentum. Angular trend: $\mathbf p_e=\mathbf p_\gamma-\mathbf p'_\gamma$ is larger when the photon is turned through a larger angle.

Observation to interpretation: $\lambda'>\lambda$, photon loses energy and momentum, electron gains them; shift depends on $\theta$, momentum change depends on the angle between in/out photon momenta; the scale $h/(m_ec)$ is set by $h$ and electron mass, not intensity or material. "Particle-like" means energy and momentum are exchanged as if one photon collides with one electron; light remains a wave elsewhere (diffraction, interference).

**Thomson model.** $\mathbf E(t)=E_0\cos\omega t\,\hat x$, force $-e\mathbf E$, so $\mathbf a(t)=-(eE_0/m_e)\cos\omega t\,\hat x$: the electron is driven at the wave's own frequency. Far-field radiation $\mathbf E_{\rm rad}\propto\hat n\times(\hat n\times\mathbf a(t_r))/R$; the time dependence is inherited from $\mathbf a(t)$, so
$$\omega'=\omega,\ \nu'=\nu,\ \lambda'=\lambda.$$
Unpolarised angular distribution
$$\frac{d\sigma}{d\Omega}=\frac{r_e^2}2(1+\cos^2\theta),\qquad r_e=\frac{e^2}{4\pi\varepsilon_0m_ec^2}\simeq2.82\times10^{-15}\ \text{m}.$$
Assumptions: electron speed $\ll c$; $h\nu\ll m_ec^2=511$ keV; negligible recoil; field not strong enough for relativistic or nonlinear motion; electron approximately free. Limitation: leading order predicts no wavelength shift; the shifted component has lower frequency, a universal angular dependence, and its missing energy/momentum go to one recoiling electron, none of which Thomson gives. Thomson is the limit $h\nu/m_ec^2\ll1$, not false. The tiny shift for visible light comes from the Compton formula, not from Thomson.

**Why invisible in everyday life.** $\Delta\lambda$ is the same for all $\lambda$; what matters is $\Delta\lambda/\lambda$.

| Radiation | $\lambda$ | Shift | $\Delta\lambda/\lambda$ |
|---|---|---|---|
| Visible | 500 nm | 2.426 pm (90°) | $4.85\times10^{-6}$ |
| Visible | 500 nm | 4.853 pm (180°) | $9.71\times10^{-6}$ |
| X-ray | 71 pm | 2.426 pm (90°) | $3.42\times10^{-2}$ |

A 500 nm photon has $E_\gamma\simeq2.48$ eV; in backscattering $K_e\simeq2.4\times10^{-5}$ eV. Classical and non-relativistic descriptions are approximations that emerge when quantum and relativistic corrections (of order $E_\gamma/m_ec^2$) are too small to observe.

**Appendix A (relativity).** $\gamma=1/\sqrt{1-v^2/c^2}$, $\mathbf p=\gamma m\mathbf v$, $E=\gamma mc^2$, $K=(\gamma-1)mc^2$, $E^2=p^2c^2+m^2c^4$; photon ($m=0$): $E_\gamma=p_\gamma c$, hence $p_\gamma=h/\lambda$.

**Appendix B (geometry).** Incident photon along $+x$, $p=E/c$; scattered photon at angle $\theta$ above the axis, electron at $\phi$ below it. Components: $p=p'\cos\theta+p_e\cos\phi$ and $0=p'\sin\theta-p_e\sin\phi$. Squaring and adding eliminates $\phi$:
$$p_e^2=p^2+p'^2-2pp'\cos\theta\ \Rightarrow\ p_e^2c^2=E^2+E'^2-2EE'\cos\theta,$$
and $E_e=m_ec^2+E-E'$, $K_e=E-E'$.

**Appendix C (derivation).** Insert into $E_e^2=p_e^2c^2+m_e^2c^4$:
$$(m_ec^2+E-E')^2=m_e^2c^4+E^2+E'^2-2EE'\cos\theta.$$
Expand and cancel the common terms using $(E-E')^2=E^2+E'^2-2EE'$:
$$2m_ec^2(E-E')=2EE'(1-\cos\theta)\ \Rightarrow\ m_ec^2\Big(\frac1{E'}-\frac1E\Big)=1-\cos\theta.$$
With $E=hc/\lambda$, $E'=hc/\lambda'$: $\lambda'-\lambda=\frac h{m_ec}(1-\cos\theta)$.

**Appendix D.** $E'=\dfrac{E}{1+\frac{E}{m_ec^2}(1-\cos\theta)}$; $K_e=E-E'=hc(1/\lambda-1/\lambda')$; $p_e=\sqrt{p^2+p'^2-2pp'\cos\theta}$.

## From the post
"Please find attached todays lecture note."

## Files
- [PH2113_Lecture3_Compton_Scattering_Particle_Picture-.pdf](https://drive.google.com/file/d/17jtM630-0Z9gxoTJH117h_-GIAo49YjZ/view?usp=drive_web)

## Related
- [[ph2113/2026-08-04-lectures-1-2-double-slit-and-compton]]: Lecture 2 introduces the same experiment with the observations first
- [[ph2113/2026-08-11-problem-set-1]]: Problem 3 applies the shift law
- [[ph2113/2026-09-03-quiz-ideal-solutions]]: quiz Compton question
- [[ph2113/2026-09-02-mock-quiz-and-solutions]]: mock quiz Compton question
