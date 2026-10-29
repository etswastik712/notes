---
title: Rabi Oscillation
aliases: [Rabi flopping, Rabi formula, Rabi frequency]
subject: qm
type: concept
scope: [extra-book, extra-beyond]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, extra/beyond, src/book, src/own-notes, status/draft]
---
# Rabi Oscillation

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book:** Sakurai §5.5.3–5.5.4 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf#page=345|PDF p.345 ff.]]). 🔵 **Extra · beyond:** the rotating-frame derivation, numbers ([[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §7.4).

> [!intuition] In one picture
> Drive a two-level system near its transition and the population sloshes between the levels; on resonance it flips completely.

> [!key] Definition and key results
> $H'=\frac\hbar2(\Delta\sigma_z+\Omega\sigma_x)\Rightarrow P_{\rm flip}=\dfrac{\Omega^2}{\Omega^2+\Delta^2}\sin^2\!\big(\tfrac12\sqrt{\Omega^2+\Delta^2}\,t\big)$. Resonance width $2\Omega$; $\pi$-pulse $\Omega t=\pi$, $\pi/2$-pulse tips into the plane. Holds for **every** two-level system ([[Flavour Oscillation]], [[Two-Level System]]).

Electron spin, $B_1=1$ mT: $\Omega/2\pi=28.0$ MHz, $\pi$-pulse $17.8$ ns; at $\Delta=\Omega/2$ the peak is $0.80$ at $16.0$ ns. Proton, $B_1=10\ \mu$T: $425.8$ Hz, $\pi$-pulse $1.17$ ms. A direct integration of the full rotating-field $H(t)$ confirms $P=1.000000$ at $t=\pi/\Omega$.

> [!pitfall] Pitfall
> Weaker drive means a *narrower* resonance. The rotating-wave approximation drops a term that shifts the resonance by $\sim\Omega^2/4\omega_0$.

Used in: [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §7.4, §12. Related: [[Magnetic Resonance]] · [[Larmor Precession]] · [[Two-Level System]] · [[Time Evolution Operator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
