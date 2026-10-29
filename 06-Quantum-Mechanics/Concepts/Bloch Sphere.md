---
title: Bloch Sphere
aliases: [Poincaré sphere (for light), qubit sphere, Bloch vector]
subject: qm
type: concept
scope: [extra-book, extra-beyond]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, extra/beyond, src/book, src/own-notes, status/draft]
---
# Bloch Sphere

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book:** Sakurai §1.1.2–1.3 and §3.4; QM03 §6 states $X,Y,Z$ (taught). 🔵 **Extra · beyond:** the mixed-state ball and the check of the QM03 example ([[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §4, §6).

> [!intuition] In one picture
> Every pure state of a spin-½ is a point on a unit sphere; every mixed state a point inside; an SG magnet along $\mathbf n'$ reports $\pm1$ with chance $\frac12(1\pm\mathbf n\cdot\mathbf n')$.

> [!key] Definition and key results
> $|\psi\rangle=\cos\frac\theta2|{+}\rangle+e^{i\varphi}\sin\frac\theta2|{-}\rangle\leftrightarrow\mathbf n=(\sin\theta\cos\varphi,\sin\theta\sin\varphi,\cos\theta)=\langle\boldsymbol\sigma\rangle$. Mixed: $\rho=\frac12(\mathbf1+\mathbf r\cdot\boldsymbol\sigma)$, $|\mathbf r|\le1$. Orthogonal states are **antipodal**; unitary evolution is a rotation of $\mathbf r$.

$(\sqrt3/2,\ 1/2)$ is $\theta=60^\circ$: $\mathbf n=(0.866,0,0.5)$, giving $P(+z)=0.75$, $P(+x)=0.933$, $P(+y)=0.5$, the QM03 numbers. For light the same sphere is the Poincaré sphere with angles doubled ([[Photon Polarisation]]).

> [!pitfall] Pitfall
> Antipodal means orthogonal, not perpendicular: the amplitude between two states $\gamma$ apart is $\cos(\gamma/2)$.

Used in: [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §4, §6, §7. Related: [[Spinor]] · [[Density Matrix]] · [[Two-Level System]] · [[Pauli Matrices]] · [[Global and Relative Phase]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
