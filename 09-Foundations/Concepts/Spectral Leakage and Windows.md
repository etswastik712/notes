---
title: Spectral Leakage and Windows
aliases: ["spectral leakage", "window function", "Hann window"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Spectral Leakage and Windows

> [!intuition] In one picture
> A finite record is the signal times a window; its spectrum is the true one convolved with the window's transform.

> [!key] Key facts
> Rectangular window: highest side-lobe $-13.3$ dB; Hann $-31.5$ dB (wider main lobe). Smooth tapering trades resolution for dynamic range.

## In this vault
Same sharpness-versus-ringing trade-off as [[Gibbs Phenomenon]].

> [!pitfall] Watch out
> Leakage is not a real spectral line.

Used in: [[Fourier and Laplace Transforms]]. Related: [[Discrete Fourier Transform]] · [[Gibbs Phenomenon]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
