---
title: Delta Function Potential
aliases: ["delta-function well", "delta potential", "Dirac delta well"]
subject: qm
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/qm, type/concept, extra/book, src/book, status/draft]
---
# Delta Function Potential

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book**: the delta-function well is Griffiths §2.5 and the $V_0\to\infty$, $a\to0$ limit of the finite well (Sakurai §2.5).

> [!intuition] In one picture
> An infinitely deep, infinitesimally thin attractive well: it supports exactly **one** bound state, whose size is set by $\hbar^2/m\alpha$.

> [!key] The bound state
> For $V(x)=-\alpha\delta(x)$ ($\alpha>0$), the unique bound state has
> $$E=-\frac{m\alpha^2}{2\hbar^2},\qquad\psi(x)=\sqrt{\frac{m\alpha}{\hbar^2}}\,e^{-m\alpha|x|/\hbar^2}.$$
> The wavefunction is continuous at $x=0$ but $\psi'$ has a jump: $\psi'(0^+)-\psi'(0^-)=-2m\alpha\psi(0)/\hbar^2$.

## Derivation
Outside $x=0$: $\psi=Be^{-\kappa|x|}$ with $\kappa=\sqrt{-2mE}/\hbar$. Integrate the TISE over $(-\varepsilon,\varepsilon)$ and take $\varepsilon\to0$: the kinetic term gives $\psi'(0^+)-\psi'(0^-)$; the potential term gives $-2m\alpha\psi(0)/\hbar^2$. So $-2\kappa=-2m\alpha/\hbar^2$, fixing $\kappa=m\alpha/\hbar^2$ and $E=-m\alpha^2/2\hbar^2$.

> [!pitfall] Only one bound state
> The odd wavefunction $\sim\operatorname{sgn}(x)e^{-\kappa|x|}$ is discontinuous at $x=0$ and fails the jump condition: the delta potential in 1-D has **exactly one** bound state.

> [!connection] Limit of the finite well
> The delta potential is the limit of the finite square well (width $2a$, depth $V_0$) as $V_0\to\infty$, $a\to0$, $2V_0a=\alpha$ fixed. See [[QM07 The Finite Square Well]] §7 (the limit) and [[QM08 Quantum Tunnelling]] §4 (the same delta as a *barrier*: its transmission has a pole at the bound state).

Used in: [[QM07 The Finite Square Well]] §7–§8, [[QM08 Quantum Tunnelling]] §4, §8. Related: [[Dirac Delta Function]] · [[QM07 The Finite Square Well]] · [[Boundary Conditions and Quantisation]] · [[Admissible Wavefunction]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
