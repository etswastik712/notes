---
title: Multivariate Normal Distribution
aliases: ["multivariate Gaussian", "N(mu, Sigma)", "jointly normal", "non-degenerate multivariate normal", "orthogonal diagonalisation of the covariance matrix"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft, quiz/probability, quiz/pr-hw6]
---
# Multivariate Normal Distribution

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[hw6_edited.pdf#page=1|HW6]], Q1: the pdf, $Y=OX$ with $O\Sigma O^{\mathsf T}$ diagonal $\Rightarrow$ independent normals.
> 🔵 **extra · beyond:** the three-step proof, the geometry and the numerical checks (mine).

> [!intuition] In one picture
> A bell-shaped cloud whose level sets are ellipses. Rotate to the ellipse's axes and the cloud becomes a product of one-dimensional bells: **independent** coordinates whose variances are the eigenvalues of $\Sigma$.

> [!key] Definition
> $X\sim N(\mu,\Sigma)$ with $\Sigma\succ0$: $f_X(x)=\dfrac{\exp(-\frac12(x-\mu)^{\mathsf T}\Sigma^{-1}(x-\mu))}{(2\pi)^{n/2}\sqrt{\det\Sigma}}$. If $O^{-1}=O^{\mathsf T}$ and $O\Sigma O^{\mathsf T}=\operatorname{diag}(\lambda_i)$ then $Y=OX$ has independent coordinates $Y_i\sim N((O\mu)_i,\lambda_i)$.

Proof: $|\det O|=1$; the exponent becomes $\sum(y_i-\mu_i')^2/\lambda_i$; $\det\Sigma=\prod\lambda_i$. $\Sigma=\begin{pmatrix}2&1\\1&2\end{pmatrix}$: $\lambda=3,1$, $Y_1=\frac{X_1+X_2}{\sqrt2}$, $Y_2=\frac{X_1-X_2}{\sqrt2}$. Only the trace is preserved ($\operatorname{Var}X_i=2,2$ against $\operatorname{Var}Y_i=3,1$). For *jointly* normal variables uncorrelated $\Rightarrow$ independent.

Used in: [[PR09 Change of Variables the Multivariate Normal and Products of Uniforms]], [[PR07 Sums of Independent Variables Covariance and Correlation]], [[QM03 States Operators and Measurement]]. Related: [[Covariance Matrix]] · [[Normal Distribution]] · [[Standard Normal Distribution]] · [[Change of Variables for Densities]] · [[Independence of Random Variables]] · [[Covariance and Correlation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
