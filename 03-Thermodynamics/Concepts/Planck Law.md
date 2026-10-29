---
title: Planck Law
subject: thermo
type: concept
scope: [taught, extra-beyond]
by: [argha]
status: draft
tags: [subject/thermo, type/concept, taught, extra/beyond, src/argha, status/draft]
---
# Planck Law

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the formula, limits, three-factor reading (Argha L3 sl. 32) · 🔵 **extra:** derivation sketch

> [!intuition] In one picture
> To emit a photon the body must pay $h\nu$ out of a thermal pocket of size ~$k_BT$. Expensive (short-wavelength) photons are rare, cheap (long-wavelength) photons are plentiful but few modes exist: the compromise is the peak.

> [!key] Statement
> Spectral radiance of a blackbody at temperature $T$:
> $$B_\lambda(T)=\frac{2hc^{2}}{\lambda^{5}}\frac{1}{e^{hc/\lambda k_BT}-1},\qquad B_\nu(T)=\frac{2h\nu^{3}}{c^{2}}\frac{1}{e^{h\nu/k_BT}-1}.$$
> Emitted flux into a hemisphere is $\pi B$.

**Reading it** (Argha, L3 slide 32): $\underbrace{\mathrm d\lambda/\lambda^4}_{\text{states}}\times\underbrace{(e^{x}-1)^{-1}}_{\text{Bose–Einstein occupation}}\times\underbrace{hc/\lambda}_{\text{energy per photon}}$, with $x=hc/\lambda k_BT$.

**Limits.** $x\gg1$ (short $\lambda$): $B\propto e^{-x}/\lambda^5$ (Wien). $x\ll1$ (long $\lambda$): $B\to2ck_BT/\lambda^4$ (Rayleigh–Jeans).

> [!extra-beyond]- Extra (beyond): derivation sketch
> Standing electromagnetic modes in a box have density $g(\nu)\,\mathrm d\nu=\dfrac{8\pi\nu^{2}}{c^{3}}\mathrm d\nu$ per volume (two polarisations). Each mode of frequency $\nu$ holds a Bose–Einstein average occupation $\bar n=1/(e^{h\nu/k_BT}-1)$ (photons have no conserved number, $\mu=0$) and energy $h\nu$ per quantum. The energy density is
> $$u_\nu=\frac{8\pi h\nu^{3}}{c^{3}}\frac{1}{e^{h\nu/k_BT}-1},$$
> and the radiance is $B_\nu=uc/4\pi$.

Consequences: [[Wien Displacement Law]], [[Stefan-Boltzmann Law]]. Applied in [[CL03 Radiation and Planetary Energy Balance]]. Statistical foundations: [[Thermodynamics - Course Map]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Atmospheric Window]] (Climate): the 8-12 $\mu$m window sits near the peak of the Planck curve of a $\sim$288 K surface (Wien: $\lambda_{max}\approx10\ \mu$m), so it is the channel through which surface emission escapes.
- [[Thermal Harmonic Oscillator]] (Quantum Mechanics): each mode of the radiation field is a quantum oscillator; thermal averaging over its levels gives the Planck mean energy $\hbar\omega/(e^{\beta\hbar\omega}-1)$ and hence the Planck law.
