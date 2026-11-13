---
title: Conditional Density Function
aliases: ["conditional pdf", "f_{Y|X}", "Bayes rule for densities", "conditional density"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft, quiz/probability, quiz/pr-hw6]
---
# Conditional Density Function

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Week4_notes.pdf#page=2|Week 4 notes]], p. 3: $f_{Y|X}=f_{X,Y}/f_X$, Bayes' rule for densities, the uniform-disc example.
> 🔵 **extra · beyond:** the chord interpretation and the numerical Bayes check (mine).

> [!intuition] In one picture
> Take the joint density, cut it along the line $X=x$, and **rescale the slice so that its area is 1**: the denominator $f_X(x)$ is exactly the area of the slice.

> [!key] Definition
> $f_{Y\mid X}(y\mid x)=\dfrac{f_{X,Y}(x,y)}{f_X(x)}$ where $f_X(x)>0$; $\int f_{Y\mid X}(y\mid x)\,\mathrm dy=1$. **Bayes:** $f_{Y\mid X}(y\mid x)=\dfrac{f_{X\mid Y}(x\mid y)\,f_Y(y)}{f_X(x)}$. Independence $\iff f_{Y\mid X}(y\mid x)=f_Y(y)$ for all $x$.

Uniform on the disc of radius $R$: $f_{X_1}(x)=\frac{2\sqrt{R^2-x^2}}{\pi R^2}$ and $X_2\mid X_1=x$ is uniform on the chord $|y|\le\sqrt{R^2-x^2}$, density $\frac1{2\sqrt{R^2-x^2}}$ ($R=2$, $x=1$: $0.2887$). The chord length depends on $x$, so $X_1,X_2$ are dependent although uncorrelated.

Used in: [[PR09 Change of Variables the Multivariate Normal and Products of Uniforms]], [[PR07 Sums of Independent Variables Covariance and Correlation]]. Related: [[Joint Density Function]] · [[Marginal Distribution]] · [[Conditional Probability]] · [[Bayes' Theorem]] · [[Independence of Random Variables]] · [[Probability Density Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
