---
title: Cauchy Distribution
aliases: ["Lorentzian distribution", "Cauchy-Lorentz", "Breit-Wigner line shape"]
subject: probability
type: concept
scope: [extra-beyond]
by: [book]
status: draft
tags: [subject/probability, type/concept, extra/beyond, src/book, status/draft]
---
# Cauchy Distribution

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** Kardar §2.5 (pp.46–47) as the standard counter-example to the central limit theorem; used in [[SM01 Probability Large Numbers and Information]] §4.3. The Cauchy law appears among the problems of the probability course only as a distribution *without* a mean.

> [!intuition] In one picture
> A bell with such fat tails that its mean and variance do not exist: averaging does not tame it. It is the distribution of $\tan\theta$ for $\theta$ uniform, the shape of a spectral line (Lorentzian), and the ratio of two independent standard normals.

> [!key] Definition
> $p(x)=\dfrac{a/\pi}{(x-x_0)^2+a^2}$; characteristic function $e^{ix_0k-a|k|}$ (non-analytic at $k=0$, so no moments). The **mean of $N$ independent Cauchy variables is Cauchy with the same $a$** for every $N$ (stable law with $\alpha=1$). $P(|x-x_0|>ta)=1-\tfrac2\pi\arctan t$ ($0.0635$ for $t=10$).

> [!example] Simulation (recomputed)
> The middle-50 % half-width of the sample mean stays $\approx1$ for $N=1\ldots10^4$ (Gaussian: $0.6745/\sqrt N$). Lévy stable laws $\alpha<2$ ($|x|^{-1-\alpha}$ tails) generalise it; $\alpha=3/2$ is the Holtsmark distribution of gravitational forces.

Used in: [[SM01 Probability Large Numbers and Information]]. Related: [[Central Limit Theorem]] · [[Characteristic Function]] · [[Moment Generating Function]] (the Cauchy has none) · [[Normal Distribution]] · [[Cumulant]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
