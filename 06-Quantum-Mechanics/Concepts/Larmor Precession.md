---
title: Larmor Precession
aliases: [spin precession, Larmor frequency]
subject: qm
type: concept
scope: [extra-book]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, src/book, src/own-notes, status/draft]
---
# Larmor Precession

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book:** Griffiths §4.4.2 ([[Griffiths - Introduction to quantum mechanics.pdf#page=176|p.161]]); Sakurai §2.1.5 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf#page=89|PDF p.89]]), §3.2.2.

> [!intuition] In one picture
> A magnetic moment in a field behaves like a spinning top in gravity: its axis circles the field at a fixed rate.

> [!key] Definition and key results
> $H=-\gamma\mathbf B\cdot\mathbf S\Rightarrow\dfrac{\mathrm d\mathbf S}{\mathrm dt}=\gamma\,\mathbf S\times\mathbf B$; $\boldsymbol\omega_L=-\gamma\mathbf B$, $\omega_L=|\gamma|B$. Electron $\gamma/2\pi=28.025$ GHz/T, proton $42.577$ MHz/T, neutron $29.165$ MHz/T. The ket is $e^{-i\omega t/2}c_+|{+}\rangle+e^{+i\omega t/2}c_-|{-}\rangle$ (period $4\pi/\omega$ for the ket, $2\pi/\omega$ for $\langle\mathbf S\rangle$).

Quantum result equals the classical torque law ([[Ehrenfest Theorem]]). Larmor's theorem: in a frame rotating at $\omega_L$ a uniform weak field disappears, the Lorentz–Coriolis analogy of [[Rotating Reference Frames]]. In an SG magnet the transverse force averages away over $1.8\times10^5$ turns.

> [!pitfall] Pitfall
> $\omega_L$ is the frequency of $\langle\mathbf S\rangle$, not of the ket; the level splitting $\hbar\omega_L$ equals $2\mu B$ for spin-½.

Used in: [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §2, §7.1. Related: [[Spin Rotation Operator]] · [[Rabi Oscillation]] · [[Heisenberg Picture]] · [[Zeeman Effect]] · [[Magnetic Resonance]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
