---
title: Saddle Point Method
aliases: ["Laplace method", "steepest descent", "method of the largest term"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Saddle Point Method

> [!info] Source
> Kardar §2.6 (pp.47–49); [[SM01 Probability Large Numbers and Information]] §5.1–5.2.

> [!intuition] In one picture
> An integral or sum of $e^{N\varphi}$ is the area under a hump that gets narrower ($\sim N^{-1/2}$) and taller ($\sim e^N$) with $N$: the area is height times width.

> [!key] Key facts
> $\int\mathrm dx\,e^{N\varphi(x)}\simeq e^{N\varphi(x^*)}\sqrt{2\pi/N|\varphi''(x^*)|}$ at the maximum $\varphi'(x^*)=0$. For a sum of positive terms with a power-law number of terms, $\tfrac1N\ln\sum\to\varphi_{\max}$.

> [!example] Beta integral (recomputed)
> $\int_0^1x^N(1-x)^N\mathrm dx\simeq4^{-N}\sqrt{\pi/4N}$ against the exact $(N!)^2/(2N+1)!$: $2.67\times10^{-7}$ vs $2.58\times10^{-7}$ at $N=10$ (3.7 % high; the error is $O(1/N)$).

In statistical mechanics: [[Equivalence of Ensembles]] ($Z=\int\Omega e^{-\beta E}\mathrm dE$), Stirling, the rate function ($I=\sup_t[ts-K(t)]$).

Used in: [[SM01 Probability Large Numbers and Information]], [[SM03 The Canonical Ensemble]]. Related: [[Stirling's Approximation]] · [[Large Deviation Principle]] · [[Gaussian Integral]] · [[Equivalence of Ensembles]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
