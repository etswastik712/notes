---
title: Bloch Theorem
aliases: ["Bloch states", "crystal momentum"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Bloch Theorem

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **Extra · beyond:** [[QM08 Quantum Tunnelling]] §8.

> [!intuition] In one picture
> In a periodic potential every eigenstate is a plane wave modulated by a function with the same period as the lattice.

> [!key] Definition and key results
> $\psi_q(x+a)=e^{iqa}\psi_q(x)$, $\psi_q=e^{iqx}u_q(x)$, $u_q(x+a)=u_q(x)$. The translation operator $T_a=e^{-i\hat pa/\hbar}$ commutes with $H$, so $e^{-iqa}$ labels the state; $q$ is defined modulo $2\pi/a$.

Consequence: energies form bands $E_n(q)$ separated by gaps.

Used in: [[QM08 Quantum Tunnelling]] §8, [[Dirac Algebra]] §7. Related: [[Kronig-Penney Model]] · [[Unitary Operator]].

> [!connection] Group theory used here
> The translation group $\mathbb Z$ is Abelian, so its irreducible representations are one-dimensional characters $e^{iqa}$: [[GT03 Cyclic and Abelian Groups and Direct Products]] §6, [[Fourier and Laplace Transforms]] §5.5; see [[Where Groups Appear in the Vault]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
