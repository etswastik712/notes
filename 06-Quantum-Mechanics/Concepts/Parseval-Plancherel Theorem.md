---
title: Parseval-Plancherel Theorem
aliases: ["Parseval identity", "Plancherel theorem", "norm is conserved by Fourier transform"]
subject: qm
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Parseval-Plancherel Theorem

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught (used):** $\sum|c_n|^2=1$ and the Fourier transform of a normalised Gaussian is normalised. · 🔵 **extra · beyond:** the statement.

> [!intuition] In one picture
> The total probability is the same whether you count it in position or in momentum.

> [!key] Definition
> $\displaystyle\int|\tilde\psi(p)|^2\mathrm dp=\int|\psi(x)|^2\mathrm dx$ for $\tilde\psi(p)=(2\pi\hbar)^{-1/2}\int\psi e^{-ipx/\hbar}\mathrm dx$; and $\sum_n|c_n|^2=\langle\psi|\psi\rangle$ for any orthonormal basis.

## Checks
Gaussian packet: $\psi=(2\pi\sigma_x^2)^{-1/4}e^{-x^2/4\sigma_x^2}$ transforms to $(2\sigma_x^2/\pi)^{1/4}e^{-\sigma_x^2k^2}$, both of unit norm. Hermite functions: $|\tilde\psi_n|=|\psi_n|$ (scaled).

> [!pitfall] The $2\pi$ lives in the transform
> With a non-symmetric convention ($\int\psi e^{-ikx}\mathrm dx$ with no prefactor) the norms differ by $2\pi$; use the unitary convention.

Used in: [[QM06 The Oscillator Toolbox]] §1, §5. Related: [[Fourier Transform and Wave Packets]] · [[Completeness Relation]] · [[Unitary Operator]] · [[Hilbert Space]].

> [!connection] See also
> See [[Fourier and Laplace Transforms]] §3.2 for the statement and §2.3 for the series version (Parseval).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
