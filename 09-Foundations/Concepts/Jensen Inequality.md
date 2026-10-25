---
title: Jensen Inequality
subject: foundations
type: concept
scope: [taught, extra-beyond]
by: [argha]
status: draft
tags: [subject/foundations, type/concept, taught, extra/beyond, src/argha, status/draft]
---
# Jensen Inequality

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** $\langle T^4\rangle>\langle T\rangle^4$ (Argha L3 sl. 39) · 🔵 **extra:** proof, ecology and probability uses

> [!intuition] In one picture
> On a bowl-shaped (convex) curve the *average of the heights* sits above the *height at the average*. Two rooms at 250 K and 350 K radiate more than two rooms at 300 K.

> [!key] Statement
> For a **convex** function $\phi$ and a random variable $X$: $\phi\big(\mathbb E[X]\big)\le\mathbb E\big[\phi(X)\big]$ (reversed for concave).

*Proof.* A convex $\phi$ lies above its tangent at $\mu=\mathbb E[X]$: $\phi(x)\ge\phi(\mu)+\phi'(\mu)(x-\mu)$. Take the expectation; the linear term vanishes. ∎

**Climate.** Emission $\sigma T^4$ is convex, so $\langle T^4\rangle\ge\langle T\rangle^4$: a non-uniform planet radiates more than a uniform one of the same mean $T$, and treating the planet as uniform *over*-estimates the temperature needed for balance (Argha L3 slide 39, Mercury). Half at 250 K, half at 350 K: $\bar T=300$ K but $\langle T^4\rangle^{1/4}=311.8$ K. For small fluctuations $\langle T^4\rangle^{1/4}\approx\bar T\,(1+\tfrac32\,\mathrm{Var}(T)/\bar T^2)$.

**Ecology.** Growth rates are nonlinear in the environment: with a convex rate, a fluctuating environment raises mean growth; with a concave rate (typical near saturation) it lowers it.

**Probability.** The inequality underlies bounds such as $\mathbb E[X]^2\le\mathbb E[X^2]$ ($\mathrm{Var}\ge0$). See [[Probability - Course Map]].

Used in [[CL03 Radiation and Planetary Energy Balance]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
