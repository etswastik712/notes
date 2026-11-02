---
title: Homomorphism Theorem for Lie Groups
aliases: ["Theorem 20.19", "Corollary 20.20", "integrating Lie algebra homomorphisms", "Homomorphism Theorem"]
subject: diff-geometry
type: concept
scope: [taught, extra-book]
by: [lecture-notes, book]
status: draft
tags: [subject/diff-geometry, type/concept, taught, extra/book, src/lecture-notes, src/book, status/draft]
---
# Homomorphism Theorem for Lie Groups

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** slide DG18 via [[mt3184-differential-geometry-and-lie-groups/2026-09-15-september-14-18|Sep 14–18 note]].
> 🟡 **extra · book:** [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=548|Lee Thm 20.19, p. 530]], [[John M. Lee - Introduction to Smooth Manifolds.pdf#page=549|Lee Cor. 20.20, p. 531]].

> [!intuition] In one picture
> On a simply connected group every Lie algebra homomorphism integrates to a unique group homomorphism.

> [!key] Definition
> $G$ simply connected, $\varphi:\mathfrak g\to\mathfrak h$ a Lie algebra homomorphism $\Rightarrow$ $\exists!\ \Phi:G\to H$ with $\Phi_*=\varphi$. Proof via the graph $\{(X,\varphi X)\}$, a subalgebra of $\mathfrak g\oplus\mathfrak h$: the corresponding subgroup $K\le G\times H$ projects by a covering $K\to G$ which is a diffeomorphism since $G$ is simply connected; $\Phi=\pi_2\pi_1^{-1}$. Uniqueness: $\Phi(\exp X)=\exp\Phi_*X$. Corollary: simply connected groups with isomorphic algebras are isomorphic.

$\mathrm{Ad}:SU(2)\to SO(3)$ integrates $\tau_k\mapsto E_k$ (kernel $\{\pm I\}$); the graph of $\tau_k\mapsto E_k$ is a subalgebra (error $2\times10^{-16}$). Fails without simple connectivity: $\mathrm{id}:\mathfrak{so}(3)\to\mathfrak{su}(2)$ does not integrate to $SO(3)\to SU(2)$.

Used in: [[DM15 Closed Subgroups and the Lie Correspondence]]. Related: [[Lie Correspondence]] · [[Induced Lie Algebra Homomorphism]] · [[Universal Covering Group]] · [[Smooth Covering Map]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
