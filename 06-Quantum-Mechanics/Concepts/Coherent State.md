---
title: Coherent State
aliases: ["coherent states", "Glauber state", "a|alpha>=alpha|alpha>", "quasi-classical state"]
subject: qm
type: concept
scope: [extra-beyond]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/book, src/own-notes, status/draft]
---
# Coherent State

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond** (Glauber 1963; Sakurai and Napolitano Ch. 2 problems).

> [!intuition] In one picture
> A ground-state Gaussian pushed to a position and momentum and then left to oscillate: it keeps its shape and follows the classical orbit.

> [!key] Definition
> $\hat a|\alpha\rangle=\alpha|\alpha\rangle$ ($\alpha\in\mathbb C$): $\ |\alpha\rangle=e^{-|\alpha|^2/2}\displaystyle\sum_n\frac{\alpha^n}{\sqrt{n!}}|n\rangle$, $\ P(n)=e^{-|\alpha|^2}\frac{|\alpha|^{2n}}{n!}$ (Poisson).

## Properties (all checked with $90\times90$ matrices)
- $\langle x\rangle=\sqrt{2\hbar/m\omega}\,\mathrm{Re}\,\alpha$, $\langle p\rangle=\sqrt{2m\hbar\omega}\,\mathrm{Im}\,\alpha$; $\langle n\rangle=\mathrm{Var}\,n=|\alpha|^2$.
- $\Delta x=\sqrt{\hbar/2m\omega}$, $\Delta p=\sqrt{m\hbar\omega/2}$, so $\Delta x\Delta p=\hbar/2$ for every $\alpha$ ([[Minimum Uncertainty State]]).
- Time: $\alpha\to\alpha e^{-i\omega t}$: stays coherent, does not spread; $\langle x\rangle(0.7)=2.11794$ both ways for $\alpha=1.2+0.9i$.
- $|\alpha\rangle=\hat D(\alpha)|0\rangle$ ([[Displacement Operator]]); position space: the ground Gaussian shifted to $x_0=\langle x\rangle$ and boosted by $p_0=\langle p\rangle$.
- $|\langle\alpha|\beta\rangle|=e^{-|\alpha-\beta|^2/2}$ (not orthogonal; overcomplete, $\frac1\pi\int|\alpha\rangle\langle\alpha|\mathrm d^2\alpha=\hat1$, stated).

## Uses
Laser light; the quantum state of a classical oscillation; the state produced when the equilibrium shifts suddenly ($|\alpha|^2=F^2/2\hbar m\omega^3$ after a sudden force $F$).

> [!pitfall] Not an energy eigenstate, not orthogonal
> $|\alpha\rangle$ is a superposition of all $n$; $\hat a$ is not Hermitian, so its eigenvalues are complex and eigenstates need not be orthogonal. There is **no** normalisable eigenstate of $\hat a^\dagger$.

Used in: [[QM06 The Oscillator Toolbox]] §7. Related: [[Number Basis]] · [[Ladder Operators]] · [[Displacement Operator]] · [[Photon Statistics]] · [[Poisson Distribution]] · [[Normal Ordering]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
