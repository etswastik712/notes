---
title: Moment Generating Function
aliases: ["MGF", "mgf"]
subject: probability
type: concept
scope: [extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, extra/book, src/lecture-notes, status/draft]
---
# Moment Generating Function

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** AI notes `probability_moments_and_mgf_notes.pdf` §2 (including the course policy: derive any named MGF from first principles before using it).

> [!intuition] In one picture
> A function whose Taylor coefficients are the moments, and which multiplies when independent variables are added.

> [!key] Definition
> $M_X(t)=E[e^{tX}]$ (finite near 0). $E[X^k]=M_X^{(k)}(0)$; $M_{aX+b}(t)=e^{bt}M_X(at)$; $M_{\sum X_i}=\prod M_{X_i}$ for independent $X_i$; equal MGFs near 0 imply equal laws.

## First-principles table (derive before use)
Bernoulli $q+pe^t$; Binomial $(q+pe^t)^n$; Poisson $e^{\lambda(e^t-1)}$; Geometric $\frac{pe^t}{1-qe^t}$ ($t<-\ln q$); Exponential $\frac\lambda{\lambda-t}$ ($t<\lambda$); Uniform $\frac{e^{tb}-e^{ta}}{t(b-a)}$; Normal $e^{\mu t+\sigma^2t^2/2}$ (complete the square).

> [!example] Independent normals
> $M_{X+Y}=e^{(\mu_1+\mu_2)t+\frac12(\sigma_1^2+\sigma_2^2)t^2}$, so $X+Y\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$.

The Cauchy has no MGF.

Used in: [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Moments of a Random Variable]] · [[Central Limit Theorem]] · [[Poisson Limit Theorem]] · [[Normal Distribution]].

## Added with QM06 (oscillator toolbox)
**Hermite link:** $e^{xt-t^2/2}=e^{xt}/M_Z(t)$ with $M_Z(t)=e^{t^2/2}$ is the generating function of the probabilists' Hermite polynomials; $E[Z^{2k}]=(2k-1)!!$ is also $\langle x^{2k}\rangle_0$ in the oscillator ground state ([[Probabilists' Hermite Polynomials]]).

## Added with the Week 2 and Week 3 lectures
**Taught (Week 3):** $M_X(t)=E[e^{tX}]$ on $-\delta<t<\delta$; the **exponential generating function** of the moments ([[Exponential Generating Function]]), so $E[X^n]=n!\,[t^n]M_X$; $M_{aX+b}(t)=e^{tb}M_X(at)$ (so $N(\mu,\sigma^2)$: $e^{\mu t+\sigma^2t^2/2}$); first-principles MGFs of uniform ($\frac{e^{tb}-e^{ta}}{t(b-a)}$), exponential ($\frac\lambda{\lambda-t}$), $N(0,1)$ ($e^{t^2/2}$), Bernoulli ($q+pe^t$), binomial ($(q+pe^t)^n$), geometric in the **failures** convention ($\frac p{1-qe^t}$; trials: $\frac{pe^t}{1-qe^t}$), two dice ($(\frac16\sum e^{kt})^2$), folded normal ($2e^{t^2/2}\Phi(t)$). **Two slips on the handwritten pages** (uniform Taylor denominator $m\to m+1$; the sign in the $N(\mu,\sigma^2)$ exponent) are corrected in [[PR06 Moments Generating Functions and Limit Theorems]] §3.1.

> [!connection] See also
> The MGF is a (two-sided) Laplace transform and its companion the characteristic function a Fourier transform: [[Fourier and Laplace Transforms]] §7.1, §9.

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Partition Function]] (Thermodynamics): $Z(\beta)=\sum_i e^{-\beta E_i}$ is the moment generating function of the energy at $t=-\beta$ (up to normalisation); $\langle E\rangle=-\partial_\beta\ln Z$ and $\mathrm{Var}\,E=\partial_\beta^2\ln Z$ are the first two cumulants.
- [[Hermite Generating Function and Recurrences]] (Quantum Mechanics): the generating function $e^{xt-t^2/2}=\sum He_n(x)t^n/n!$ is the exponential kernel $e^{tx}$ divided by the moment generating function of the standard normal, $E[e^{tZ}]=e^{t^2/2}$.

## Continued in Part II (added 2026-10-30)
- $\ln M$ is the cumulant generating function; $\ln Z(\beta)$ is the same object for the energy, so $\kappa_n(E)=(-1)^n\partial_\beta^n\ln Z$: [[Cumulant]], [[SM03 The Canonical Ensemble]] §2.1.
