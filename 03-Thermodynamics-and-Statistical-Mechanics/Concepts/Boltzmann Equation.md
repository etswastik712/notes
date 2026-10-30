---
title: Boltzmann Equation
aliases: ["Boltzmann transport equation", "collision integral"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Boltzmann Equation

> [!info] Source
> Kardar §3.4 (p. 71, eq. 3.41); Huang §3.3 (p. 60); Reif Ch. 14; [[SM04 Kinetic Theory and the Boltzmann Equation]] §4.

> [!intuition] In one picture
> Free flight on the left; on the right, molecules knocked out of a momentum cell by collisions and molecules knocked into it by the reverse collisions.

> [!key] Key facts
> $\big[\partial_t+\tfrac{\mathbf p}m\cdot\nabla_{\mathbf q}-\nabla U\cdot\nabla_{\mathbf p}\big]f=\int\mathrm d^3p_2\,\mathrm d\Omega\,\frac{\mathrm d\sigma}{\mathrm d\Omega}|\mathbf v_1-\mathbf v_2|\,[f(\mathbf p_1')f(\mathbf p_2')-f(\mathbf p_1)f(\mathbf p_2)]$. Valid for dilute gases ($nd^3\ll1$), short-range forces, slowly varying fields, and **molecular chaos** for incoming pairs.

> [!example] Consequences
> Collision invariants $1,\mathbf p,p^2$ give the conservation laws; $H=\int f\ln f$ never increases ([[H-Theorem]]); equilibrium is Maxwell; first-order solutions give $\eta,\kappa$; zeroth order gives Euler ([[Euler Equations]]). For Coulomb gases drop the collision term (Vlasov); for fermions/bosons multiply by $(1\pm f)$.

Used in: [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[Molecular Chaos]] · [[Collision Invariants]] · [[H-Theorem]] · [[Scattering Cross Section]] · [[Relaxation Time Approximation]] · [[Kinetic Theory of Gases]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
