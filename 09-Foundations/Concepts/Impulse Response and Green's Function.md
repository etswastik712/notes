---
title: Impulse Response and Green's Function
aliases: ["impulse response", "Green's function", "Duhamel"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Impulse Response and Green's Function

> [!intuition] In one picture
> The response to a unit spike; any response is a superposition of shifted impulse responses.

> [!key] Key facts
> $y=h*u$; $\mathcal L\{\delta\}=1$ so $H=\mathcal L\{h\}$. Diffusion kernel $G=e^{-x^2/4Dt}/\sqrt{4\pi Dt}$ is the Green's function of the heat equation. Causality: $h(t)=0$ for $t<0$.

## In this vault
Point source $\to$ distributed source in PDEs; hillslope and heat problems.

> [!pitfall] Watch out
> Boundary conditions modify the Green's function (method of images).

Used in: [[Fourier and Laplace Transforms]]. Related: [[Convolution]] · [[Transfer Function]] · [[Dirac Delta Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Diffusion Equation]] (Thermodynamics): the Gaussian heat kernel is the Green's function of $\partial_t-D\partial_x^2$: any initial profile spreads as its convolution with it.
