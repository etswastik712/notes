---
title: Diffusion Equation
aliases: [heat equation, diffusion, Fokker-Planck equation]
subject: thermo
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/thermo, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Diffusion Equation

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **Extra · beyond** ([[THX1 Diffusion Random Walks and the Heat Equation]] §2–§3; the Landscapes version is [[LS12 Hillslope Transport and the Diffusion Equation]]).

> [!intuition] In one picture
> Conservation plus a flux down the gradient: the lumps flatten, the short wavelengths first.

> [!key] Definition and key results
> $\partial_tu=D\nabla^2u$. Kernel $e^{-x^2/4Dt}/\sqrt{4\pi Dt}$, front width $\propto\sqrt{Dt}$, sinusoid decays at $Dk^2$, step gives $\operatorname{erfc}(x/2\sqrt{Dt})$, periodic forcing penetrates $\delta=\sqrt{2\kappa/\omega}$. Diffusion times $L^2/2D$.

> [!pitfall] Pitfall
> $D$ is not a velocity: it has units length²/time, so the front moves ever more slowly.

Used in: [[THX1 Diffusion Random Walks and the Heat Equation]], [[LS12 Hillslope Transport and the Diffusion Equation]], [[LS22 Floods Planform and River Profiles]]. Related: [[Fick's and Fourier's Laws]] · [[Random Walk]] · [[Péclet Number]] · [[Brownian Motion and the Einstein Relation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Impulse Response and Green's Function]] and [[Fourier Transform]] (Foundations): the kernel is the Green's function; $e^{-Dk^2t}$ in Fourier space
- [[Free Particle]] (Quantum Mechanics): the same equation with imaginary $D=i\hbar/2m$
- [[Closure Temperature]] (Landscapes): diffusion of helium out of a grain sets the clock
- [[Normal Distribution]] (Probability): the normal density with variance $2Dt$ is the fundamental solution of the diffusion equation.
