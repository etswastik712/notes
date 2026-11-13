---
title: Box-Muller Transform
aliases: ["Box–Muller", "generating normal random variables", "polar method for normals", "Rayleigh from uniforms"]
subject: probability
type: concept
scope: [extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, extra/beyond, src/lecture-notes, src/own-notes, status/draft, quiz/probability, quiz/pr-hw6]
---
# Box-Muller Transform

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** the polar-coordinate use of the change-of-variables formula (mine; Box and Muller 1958 is the source of the name).

> [!intuition] In one picture
> Two independent normals form a point in the plane whose **direction is uniform** and whose **distance has the Rayleigh law**; run it backwards and two uniforms make two normals.

> [!key] Definition
> For independent $U_1,U_2\sim U(0,1)$: $R=\sqrt{-2\ln U_1}$ (so $P(R>r)=e^{-r^2/2}$) and $\Theta=2\pi U_2$; then $X=R\cos\Theta$, $Y=R\sin\Theta$ are **independent $N(0,1)$**. Reason: polar coordinates have Jacobian $r$, so $\frac1{2\pi}e^{-(x^2+y^2)/2}\,\mathrm dx\,\mathrm dy=(re^{-r^2/2}\,\mathrm dr)\,\frac{\mathrm d\theta}{2\pi}$.

Checked on $2\cdot10^6$ draws: means $-0.0005,0.0003$, variances $0.9998,0.9990$, correlation $0.0005$; $P(R<1)=1-e^{-1/2}=0.3935$ (simulation $0.3933$). The integral $\iint e^{-(x^2+y^2)/2}=2\pi$ is the same computation: $\int e^{-x^2/2}\mathrm dx=\sqrt{2\pi}$.

Used in: [[PR09 Change of Variables the Multivariate Normal and Products of Uniforms]]. Related: [[Change of Variables for Densities]] · [[Rayleigh Distribution]] · [[Standard Normal Distribution]] · [[Probability Integral Transform]] · [[Uniform Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
