---
title: Von Neumann Measurement Model
aliases: [measurement as entanglement, pointer model of the SG measurement]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Von Neumann Measurement Model

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **Extra · beyond:** [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §8 (after Griffiths §4.4, the beam-frame argument by Ballentine, [[Griffiths - Introduction to quantum mechanics.pdf#page=178|p.163]]).

> [!intuition] In one picture
> A good measurement is a unitary interaction that entangles the system (spin) with a pointer (position); ignoring the pointer leaves the spin in a mixture.

> [!key] Definition and key results
> $U=e^{ikz\sigma_z}$, $k=\mu B'\tau/\hbar$ shifts $p_z$ by $\pm\Delta p=\pm F\tau$: $(a|{+}\rangle+b|{-}\rangle)\varphi\to a|{+}\rangle\varphi e^{ikz}+b|{-}\rangle\varphi e^{-ikz}$. Reduced spin state: off-diagonals $\times\mathcal O=e^{-2k^2\sigma_z^2}=e^{-\Delta p^2/2\sigma_p^2}$.

Silver: $\Delta p=5.9\times10^{-25}$ kg m/s, $\sigma_p=2.6\times10^{-30}$ (for $\sigma_z=20\ \mu$m), $\Delta p/\sigma_p=2.2\times10^5$: $\mathcal O=e^{-2.5\times10^{10}}$. Reversing the gradient restores $\mathcal O=1$ (Humpty-Dumpty). Free electrons: Lorentz/spin force $\sim4\pi w/\lambda\sim10^5$ (Bohr–Mott).

> [!pitfall] Pitfall
> Decoherence of $\rho_{\rm spin}$ is not collapse: the superposition lives on in the correlation until a macroscopic plate fixes the outcome.

Used in: [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §8. Related: [[Measurement Postulate]] · [[Stern-Gerlach Experiment]] · [[Density Matrix]] · [[Heisenberg Uncertainty Principle]] · [[Dirac Algebra]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
