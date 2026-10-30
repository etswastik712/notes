---
title: Characteristic Function
aliases: ["characteristic function", "char. function"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Characteristic Function

> [!intuition] In one picture
> The Fourier transform of a probability density, $\varphi(t)=E[e^{itX}]$; always exists.

> [!key] Key facts
> $\varphi_{X+Y}=\varphi_X\varphi_Y$ for independent variables; moments from derivatives at 0; Gaussian: $e^{-\sigma^2t^2/2}$; Cauchy: $e^{-\lvert t\rvert}$. CLT: $[\varphi(t/\sqrt n)]^n\to e^{-t^2/2}$.

## In this vault
Companion of the MGF (a Laplace transform): [[Moment Generating Function]], [[Central Limit Theorem]], [[Normal Distribution]].

> [!pitfall] Watch out
> Cauchy does not satisfy the CLT (no variance, not smooth at 0).

Used in: [[Fourier and Laplace Transforms]]. Related: [[Convolution Theorem]] · [[Fourier Transform]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Continued in Part II (added 2026-10-30)
- Kardar's convention $\tilde p(k)=\langle e^{-ikx}\rangle$ and the cumulants via $\ln\tilde p$: [[SM01 Probability Large Numbers and Information]] §2 ([[Cumulant]]).
