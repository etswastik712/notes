---
title: Probabilists' Hermite Polynomials
aliases: ["He_n", "Hermite polynomials (probabilists)", "Chebyshev-Hermite"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Probabilists' Hermite Polynomials

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** the cross-subject bridge between [[Hermite Polynomials]] and probability.

> [!intuition] In one picture
> The same polynomials, rescaled so that they are orthogonal under the standard normal density.

> [!key] Definition
> $\mathrm{He}_n(x)=2^{-n/2}H_n(x/\sqrt2)$; $\ \mathrm{He}_2=x^2-1$, $\mathrm{He}_3=x^3-3x$, $\mathrm{He}_4=x^4-6x^2+3$; generating function $e^{xt-t^2/2}$; $\ E[\mathrm{He}_m(Z)\mathrm{He}_n(Z)]=n!\,\delta_{mn}$ for $Z\sim N(0,1)$.

## Links
- **MGF:** $e^{xt-t^2/2}=e^{xt}/M_Z(t)$ with $M_Z(t)=e^{t^2/2}$ ([[Moment Generating Function]], [[PR06 Moments Generating Functions and Limit Theorems]]).
- **Gaussian moments:** $x^4=\mathrm{He}_4+6\mathrm{He}_2+3$, so $E[Z^4]=3$; in general $E[Z^{2k}]=(2k-1)!!$ ($1,1,3,15,105$, checked), the same numbers as $\langle x^{2k}\rangle_0/\sigma^{2k}$ in the oscillator ground state.
- **Edgeworth:** the leading correction to the CLT density is $\frac{\gamma_1}{6\sqrt n}\mathrm{He}_3(x)\varphi(x)$, to the cdf $-\frac{\gamma_1}{6\sqrt n}\mathrm{He}_2(x)\varphi(x)$, whose maximum $\gamma_1/(6\sqrt{2\pi n})$ is the number compared with the exact Gamma cdf in PR06.
- **Oscillator:** $\psi_n\propto\mathrm{He}_n(\sqrt2\,\xi)\,e^{-\xi^2/2}$.

> [!pitfall] Which weight?
> $\int H_mH_ne^{-\xi^2}\mathrm d\xi=\sqrt\pi2^nn!\delta_{mn}$ but $\int\mathrm{He}_m\mathrm{He}_ne^{-x^2/2}\mathrm dx=\sqrt{2\pi}\,n!\,\delta_{mn}$; quote the weight with the polynomial.

Used in: [[QM06 The Oscillator Toolbox]] §4.4. Related: [[Hermite Polynomials]] · [[Normal Distribution]] · [[Central Limit Theorem]] · [[Orthogonal Polynomials]] · [[Gaussian Integral]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
