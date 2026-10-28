---
title: Transfer Function
aliases: ["transfer function", "frequency response"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Transfer Function

> [!intuition] In one picture
> $H(s)=Y(s)/U(s)$: the factor by which a linear time-invariant system multiplies the input $e^{st}$.

> [!key] Key facts
> $H(s)=\mathcal L\{h\}$ with $h$ the impulse response; $\lvert H(i\omega)\rvert$ is the frequency response. First-order relaxation $H=1/(1+\tau s)$ gives the low-pass filter of [[LS01 Landscapes as Physical Systems]].

## In this vault
Oscillator resonance, filters, climate response.

> [!pitfall] Watch out
> Defined for zero initial state.

Used in: [[Fourier and Laplace Transforms]]. Related: [[Poles and Stability]] · [[Convolution Theorem]] · [[Laplace Transform]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
