---
title: Normal Distribution
aliases: ["Gaussian distribution", "normal", "N(mu,sigma^2)"]
subject: probability
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, taught, src/lecture-notes, status/draft]
---
# Normal Distribution

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[week1_mt2113.pdf#page=8|week 1 p.8]], [[week1_mt2113.pdf#page=9|p.9]].

> [!intuition] In one picture
> The bell curve: location $\mu$, spread $\sigma$; the law of sums of many small independent effects.

> [!key] Definition
> $X\sim N(\mu,\sigma^2)$ iff $\frac{X-\mu}\sigma\sim N(0,1)$, i.e. $X=\sigma Z+\mu$; $f(x)=\frac1{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}$; $E[X]=\mu$, $\mathrm{Var}[X]=\sigma^2$; MGF $e^{\mu t+\sigma^2t^2/2}$.

## Properties
$E[\sigma Z+\mu]=\mu$, $\mathrm{Var}[\sigma Z+\mu]=\sigma^2$. Inflection points at $\mu\pm\sigma$ (homework Q5): $f''\propto(z^2-1)\varphi(z)$. Within $\pm1,\pm2,\pm3\sigma$: $68.27\%$, $95.45\%$, $99.73\%$. Independent normals add: $N(\mu_1,\sigma_1^2)+N(\mu_2,\sigma_2^2)=N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$ (by MGFs).

> [!example] $N(10,4)$
> $P[8<X<12]=P[|Z|<1]=0.6827$; $P[X>14]=P[Z>2]=0.0228$; $P[|X-10|<3.92]=0.95$.

Used in: [[PR05 Continuous Random Variables]], [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Standard Normal Distribution]] · [[Central Limit Theorem]] · [[Moment Generating Function]].

## Added with QM06 (oscillator toolbox)
**Quantum link:** the oscillator ground-state density $|\psi_0|^2$ is a normal density with variance $\hbar/2m\omega$; higher $|\psi_n|^2$ are Hermite-weighted Gaussians ([[Oscillator Expectation Values]], [[Probabilists' Hermite Polynomials]]).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Diffusion Equation]] (Thermodynamics): the normal density with variance $2Dt$ is the fundamental solution of the diffusion equation.
- [[Wave Energy and Power]] (Waves): the surface elevation of a narrow-band sea is Gaussian, so wave heights are Rayleigh distributed ($H_{1/3}=2\sigma$) and the largest 10% of waves carry 33% of the energy.

## Continued in Part II (added 2026-10-30)
- The only distribution with two cumulants; Wick's theorem; the joint Gaussian of momenta: [[Wick's Theorem]], [[SM01 Probability Large Numbers and Information]] §2.3.
