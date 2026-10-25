---
title: Fourier Transform and Wave Packets
aliases: ["Fourier synthesis", "wave packet"]
subject: qm
type: concept
scope: [taught]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, src/lecture-notes, status/draft]
---
# Fourier Transform and Wave Packets

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_Lecture6-7.pdf#page=2|L7 §2–3]], [[PH2113_Lecture6-7.pdf#page=4|L7 §7 (interlude)]], [[PH2113_wavefunctions_potentials_schrodinger_Tutorial.pdf#page=3|Tutorial §4]].

> [!intuition] In one picture
> Any shape is a recipe of plane waves. Few ingredients means a spread-out result; many ingredients lets them cancel everywhere except in one small place.

> [!key] Definition
> $\tilde\psi(k)=\dfrac1{\sqrt{2\pi}}\int\psi(x)e^{-ikx}\mathrm dx$ (analysis) and $\psi(x)=\dfrac1{\sqrt{2\pi}}\int\tilde\psi(k)e^{ikx}\mathrm dk$ (synthesis). With $p=\hbar k$, $|\tilde\psi|^2\mathrm dk$ is the probability for the momentum. For any square-integrable pair, $\Delta x\,\Delta k\ge\tfrac12$.

## Examples
> [!example] A band of $k$
> $\frac1{2\pi}\int_{-K}^{K}e^{ikx}\mathrm dk=\sin Kx/\pi x$: peak $K/\pi$, first zeros at $\pm\pi/K$, so $\Delta x\,\Delta k\approx\pi$ for every $K$. $K\to\infty$ gives $\delta(x)$. Two plane waves give $2\cos(\Delta k\,x/2)\,e^{i\bar kx}$: a carrier times an envelope with zeros at $x=(2n+1)\pi/\Delta k$.

> [!example] A Gaussian is its own shape
> $e^{-x^2/2\sigma^2}\leftrightarrow\sigma e^{-\sigma^2k^2/2}$: narrow in $x$ $\Leftrightarrow$ broad in $k$ ([[Gaussian Integral]]).

> [!pitfall] A change of description, not new physics
> The transform becomes physics only when $|\tilde\psi|^2$ is read as a momentum probability. The width trade-off itself is true for sound pulses, radio signals and light ([[Waves - Course Map]]).

Used in: [[QM01 From Waves to Probabilities]], [[QM05 The Harmonic Oscillator]]. Related: [[Gaussian Wave Packet]] · [[Heisenberg Uncertainty Principle]] · [[Gaussian Integral]] · [[Plane Wave]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
