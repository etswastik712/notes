---
title: GT-A3 Primitive Maximal Subgroups
aliases: [GT-A3, primitive maximal subgroups, core of a subgroup, maximal subgroups, affine groups, primitive solvable groups]
subject: group-theory
type: chapter
part: Advanced
by: [book, own-notes]
status: draft
prereq: ["[[GT06 Permutation Groups]]", "[[GT08 Solvable Groups and Complements]]"]
tags: [subject/group-theory, type/chapter, src/book, src/own-notes, status/draft]
---
# GT-A3 · Primitive Maximal Subgroups (advanced)

◀ [[Advanced Group Theory]] · [[GT06 Permutation Groups]] · [[Group Theory - Course Map|Course Map]]

> [!info] Source and approach
> Corresponds to K–S §6.6 ([[Kurzweil-Stellmacher_Theory of finite groups.pdf#page=158|PDF p.158]]); PDF page = printed page + 13. **Guide chapter**: the section text was not read. The reduction "maximal subgroup $\Rightarrow$ primitive action with kernel the core" is proved (it is Theorem 2.1 of GT06); the structure theorem for solvable primitive groups is stated.

> [!tip] Start here
> - **The picture.** Every maximal subgroup $M$ of a finite group $G$ gives a *primitive permutation action* of $G$ on the cosets $G/M$; its kernel is the **core** $M_G$. So *the study of maximal subgroups is the study of primitive groups*. For solvable groups the answer is clean: a solvable primitive group is an **affine group** $V\rtimes H$ with $V$ an elementary Abelian group acted on faithfully and irreducibly by $H$.
> - **What you need.** Blocks and primitivity ([[GT06 Permutation Groups]]), semidirect products ([[GT08 Solvable Groups and Complements]]).

> [!key] Definitions
> The **core** of $M\le G$ is $M_G=\bigcap_{g\in G}g^{-1}Mg$, the largest normal subgroup of $G$ contained in $M$. A maximal subgroup $M$ is **primitive** (in K–S's sense) if $M_G=1$; then $G$ acts faithfully on the cosets of $M$.

> [!derivation] Theorem 1. If $M$ is a maximal subgroup of $G$, then $G$ acts primitively on the cosets $G/M$ with kernel $M_G$; so $G/M_G$ is a primitive permutation group on $|G:M|$ points with point stabiliser $M/M_G$.
> *Proof.* The stabiliser of the coset $M$ is $M$, which is maximal; by GT06 Theorem 2.1 the (transitive) action is primitive. The kernel of any action on cosets is the intersection of the stabilisers $g^{-1}Mg$, i.e. the core. ∎

> [!example] The maximal subgroups of $S_4$ (computed)
> | maximal subgroup $M$ | order | core $M_G$ | induced primitive group $G/M_G$ | action on |
> |---|---|---|---|---|
> | $S_3$ (4 conjugates) | 6 | $1$ | $S_4$ itself | 4 points (natural action) |
> | $D_4$ (3 conjugates) | 8 | $V_4$ | $S_4/V_4\cong S_3$ | 3 points |
> | $A_4$ | 12 | $A_4$ | $S_4/A_4\cong C_2$ | 2 points |
> Only $S_3$ is a *primitive maximal subgroup* ($M_G=1$).

> [!key] Theorem 2 (primitive solvable groups, stated; Galois). Let $G$ be a **solvable primitive** permutation group on $\Omega$. Then $G$ has a **unique minimal normal subgroup** $V$; $V$ is an elementary Abelian $p$-group acting regularly ($|\Omega|=p^d$), and $G=V\rtimes G_\alpha$ with $G_\alpha$ acting **faithfully and irreducibly** on $V\cong\mathbb F_p^d$ by conjugation. Conversely every such semidirect product is primitive.
> *Examples (all consistent):* $S_3=C_3\rtimes C_2$ on 3 points; $A_4=V_4\rtimes C_3$ and $S_4=V_4\rtimes S_3$ on 4 points ($p^d=2^2$); $F_{20}=C_5\rtimes C_4$ and $D_5=C_5\rtimes C_2$ on 5 points; $AGL(d,p)=\mathbb F_p^d\rtimes GL_d(p)$ on $p^d$ points. The non-solvable primitive groups ($A_n$, $S_n$ on $n$ points, ...) are the subject of the O'Nan–Scott theorem (outside this vault).

> [!connection] In other subjects
> **Crystals:** a space group is $\mathbb Z^3\rtimes P$, an *affine* group of exactly this shape (translations normal, point group acting); the classification of finite primitive affine groups is the finite-field version of the classification of crystal systems. **Landscapes and GIS:** the affine maps of the plane acting on a DEM grid ([[LS04 Map Projections and Reference Surfaces]]). **Concept notes:** [[Core of a Subgroup]] · [[Primitive Action and Blocks]] · [[Affine Group]]

## Provenance
> [!provenance]- Source map
> | Topic | Source | Origin |
> |---|---|---|
> | primitive maximal subgroups | K–S §6.6 (PDF p.158; TOC title only) | book (by title) |
> | Theorem 1 (via GT06), maximal subgroups and cores of $S_4$ (computed), examples | my write-up; computed (`scripts/gt_numbers2.py`) | mine |
> | structure theorem for solvable primitive groups | recalled; not proved | not checked (`[verify]`) |
