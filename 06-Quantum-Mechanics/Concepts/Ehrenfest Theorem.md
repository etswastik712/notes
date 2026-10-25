---
title: Ehrenfest Theorem
aliases: ["Ehrenfest", "expectation values obey classical equations"]
subject: qm
type: concept
scope: [extra-book, extra-beyond]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, extra/beyond, src/book, src/own-notes, status/draft]
---
# Ehrenfest Theorem

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Griffiths §1.5 (page not checked). · 🔵 **extra · beyond:** the commutator form and the oscillator application.

> [!intuition] In one picture
> Averages of quantum observables follow the classical equations of motion, but only exactly when the force is linear.

> [!key] Definition
> $\dfrac{\mathrm d}{\mathrm dt}\langle\hat A\rangle=\dfrac i\hbar\langle[\hat H,\hat A]\rangle+\Big\langle\dfrac{\partial\hat A}{\partial t}\Big\rangle$; hence $\dfrac{\mathrm d\langle x\rangle}{\mathrm dt}=\dfrac{\langle p\rangle}m$ and $\dfrac{\mathrm d\langle p\rangle}{\mathrm dt}=-\langle V\prime(x)\rangle$.

## Consequences
- **Stationary states:** $\langle n|[\hat H,\hat A]|n\rangle=0$, so no expectation value changes.
- **Oscillator:** $V'=m\omega^2x$ is linear, so $\langle V'\rangle=m\omega^2\langle x\rangle$ and $\langle x\rangle(t)=\langle x\rangle_0\cos\omega t+\dfrac{\langle p\rangle_0}{m\omega}\sin\omega t$ for **every** state. Checked for $(\psi_0+\psi_1)/\sqrt2$: $\langle x\rangle=\sqrt{\hbar/2m\omega}\cos\omega t$, $\langle p\rangle=-\sqrt{m\hbar\omega/2}\sin\omega t$.
- **Anharmonic $V$:** $\langle V'(x)\rangle\ne V'(\langle x\rangle)$, so the centre does not follow the classical orbit and a packet spreads.

> [!pitfall] It is not "quantum mechanics is classical"
> Only the *averages* of linear-force problems are classical; widths, interference and the spectrum are not.

Used in: [[QM06 The Oscillator Toolbox]] §6.1. Related: [[Heisenberg Picture]] · [[Commutator]] · [[Expectation Value]] · [[Stationary State]] · [[Correspondence Principle]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
