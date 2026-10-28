---
title: Convolution
aliases: ["convolution", "blurring", "smoothing"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Convolution

> [!intuition] In one picture
> Slide one function past another and integrate the overlap; equivalent to superposing shifted copies.

> [!key] Key facts
> $(f*g)(x)=\int f(y)g(x-y)\mathrm dy$. Commutative, associative. Averaging, blurring, filtering and 'response to a distributed input' are convolutions. Density of $X+Y$ for independent variables is $f_X*f_Y$.

## In this vault
Sum of two $U(0,1)$ is a triangle. Diffusion is convolution with a Gaussian kernel. Impulse response $\to$ output.

> [!pitfall] Watch out
> Cyclic (DFT) and linear convolution differ: zero-pad.

Used in: [[Fourier and Laplace Transforms]]. Related: [[Convolution Theorem]] · [[Impulse Response and Green's Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
