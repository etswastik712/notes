---
title: Spinor
aliases: [two-component spinor, Pauli spinor]
subject: qm
type: concept
scope: [extra-book]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, src/book, src/own-notes, status/draft]
---
# Spinor

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book:** Sakurai §3.2.4 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf#page=179|PDF p.179]]); Griffiths §4.4.1 ([[Griffiths - Introduction to quantum mechanics.pdf#page=169|p.169 ff.]]).

> [!intuition] In one picture
> The column of two complex amplitudes that describes a spin-½: a vector that changes sign under a $2\pi$ rotation.

> [!key] Definition and key results
> $\chi=\binom{c_+}{c_-}$, $|c_+|^2+|c_-|^2=1$, $c_\pm=\langle\pm z|\chi\rangle$. A rotation by $\theta$ about $\mathbf n$ acts as $U=e^{-i\theta\,\mathbf n\cdot\boldsymbol\sigma/2}$; $U(2\pi)=-\mathbf1$, $U(4\pi)=\mathbf1$ ([[Spin Rotation Operator]]).

The class of $\chi$ up to a global phase is a point on the [[Bloch Sphere]]. Pauli's two-component theory (1926) is the non-relativistic limit of Dirac's four-component spinor. The neutron-interferometer experiment shows the sign of $U(2\pi)$ directly.

> [!pitfall] Pitfall
> A spinor is not a 3-vector: it needs the *half* angle, so a $2\pi$ turn flips its sign even though every observable returns.

Used in: [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §4, §7.2–§7.3. Related: [[Spin]] · [[Bloch Sphere]] · [[Pauli Matrices]] · [[Unitary Operator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Exponential Map]] (Differential Geometry): $\exp\big(-\tfrac i2\theta\,\hat n\!\cdot\!\sigma\big)\in SU(2)$ rotates spinors by $\theta$ about $\hat n$, and $\theta=2\pi$ gives $-I$: $SU(2)\to SO(3)$ is $2:1$.
