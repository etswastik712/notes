---
title: Orthogonal Polynomials
aliases: ["Hermite Legendre Laguerre", "Gram-Schmidt on monomials", "weight function"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Orthogonal Polynomials

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond.**

> [!intuition] In one picture
> Fix a weight $w(x)$ and run Gram–Schmidt on $1,x,x^2,\dots$: out come polynomials orthogonal for that weight.

> [!key] Definition
> $\displaystyle\int p_m(x)p_n(x)\,w(x)\,\mathrm dx=h_n\delta_{mn}$. Hermite: $w=e^{-\xi^2}$ on $\mathbb R$, $h_n=\sqrt\pi2^nn!$; Legendre: $w=1$ on $[-1,1]$; Laguerre: $w=e^{-x}$ on $[0,\infty)$.

## Gram–Schmidt check
With $w=e^{-\xi^2}$: $p_0=1$, $p_1=\xi$, $p_2=\xi^2-\frac{\langle\xi^2,1\rangle}{\langle1,1\rangle}=\xi^2-\tfrac12=\tfrac14H_2$ ✓. All satisfy a **three-term recurrence** (for Hermite $H_{n+1}=2\xi H_n-2nH_{n-1}$) and a second-order ODE (Sturm–Liouville), and their zeros interlace. Legendre polynomials return in the central-force problems (angular part of hydrogen) and Laguerre in the radial part; neither is in the folder.

> [!pitfall] Orthogonal is relative to the weight
> The same polynomial set is not orthogonal under $w=1$.

Used in: [[QM06 The Oscillator Toolbox]] §4. Related: [[Hermite Polynomials]] · [[Gram-Schmidt Orthogonalisation]] · [[Orthonormality of Eigenfunctions]] · [[Probabilists' Hermite Polynomials]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
