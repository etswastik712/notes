---
title: Classical Probability Density of the Oscillator
aliases: ["classical oscillator density", "arcsine density"]
subject: qm
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Classical Probability Density of the Oscillator

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the question "what is the classical probability, where is it peaked?" opens the [[Harmonic_oscillator.pdf#page=2|oscillator lecture (p.2)]]. · 🔵 **extra · beyond:** the answer, derived and checked here.

> [!intuition] In one picture
> A mass on a spring lingers where it moves slowly: near the turning points, almost never at the centre.

> [!key] Definition
> $P_{\rm cl}(x)=\dfrac{1}{\pi\sqrt{A^2-x^2}}$ for $|x|<A$, $A=\sqrt{2E/m\omega^2}$: the fraction of time spent in $[x,x+\mathrm dx]$.

## Derivation
For $x(t)=A\cos\omega t$ the speed is $|v|=\omega\sqrt{A^2-x^2}$. The time in $\mathrm dx$ is $\mathrm dt=\mathrm dx/|v|$, and each $x$ is passed twice per period $T=2\pi/\omega$, so $P_{\rm cl}\,\mathrm dx=2\,\mathrm dt/T$, giving the boxed result. It is normalised ($\int_{-A}^{A}=1$), diverges (integrably) at $\pm A$ and is smallest at $0$.

## Numbers (simulation of $2\times10^6$ random times)
$P(|x|<A/2)=\tfrac2\pi\arcsin\tfrac12=\tfrac13$ (simulated $0.3332$); $P(|x|>0.9A)=0.2871$ (simulated $0.2875$). Moments: variance $A^2/2$, $\langle x^4\rangle=3A^4/8$, so the kurtosis is $\tfrac32$; the quantum ratio $\langle x^4\rangle/\langle x^2\rangle^2=(6n^2+6n+3)/(2n+1)^2\to\tfrac32$ as $n\to\infty$ ($1.50004$ at $n=100$). In probability language this is the **arcsine law**, a Beta$(\tfrac12,\tfrac12)$ density.

## Quantum versus classical
The ground state is one hump **at the centre**, the opposite of $P_{\rm cl}$. For large $n$ the quantum density oscillates about $P_{\rm cl}$ (for $n=20$: $P(|x|<x_t/2)=0.344$ against $1/3$) and leaks past the turning points ([[Correspondence Principle]]).

> [!pitfall] A probability density that diverges is still fine
> $1/\sqrt{A^2-x^2}$ is infinite at $x=\pm A$ but integrable; densities need only integrate to 1.

Used in: [[QM05 The Harmonic Oscillator]] §1, [[QM06 The Oscillator Toolbox]] §3. Related: [[Harmonic Oscillator]] · [[Correspondence Principle]] · [[Oscillator Expectation Values]] · [[Probability Density Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
