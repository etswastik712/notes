---
title: No-Cloning Theorem
aliases: [no cloning, no-cloning]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# No-Cloning Theorem

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **Extra · beyond:** derived here ([[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §11.4); Wootters and Zurek (1982) recalled.

> [!intuition] In one picture
> You cannot copy an unknown quantum state: if you could, a Stern–Gerlach analysis of the copies would reveal all three spin components.

> [!key] Definition and key results
> If a unitary $U$ satisfied $U|\psi\rangle|0\rangle=|\psi\rangle|\psi\rangle$ for all $|\psi\rangle$, then $\langle\psi|\phi\rangle=\langle\psi|\phi\rangle^2$, forcing $\langle\psi|\phi\rangle\in\{0,1\}$.

$|{+z}\rangle$ and $|{+x}\rangle$ have overlap $1/\sqrt2$: contradiction. Orthogonal states *can* be copied (classical bits); non-orthogonal ones cannot. The basis of the security of [[BB84 Protocol]].

> [!pitfall] Pitfall
> This is about *unknown* states and one unitary for all of them; one can copy a *known* state, or teleport (destroying the original).

Used in: [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §11.4. Related: [[BB84 Protocol]] · [[Unitary Operator]] · [[Entanglement]] · [[Sequential Stern-Gerlach Experiments]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
