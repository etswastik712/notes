---
title: GT-A1 Radical Residue and Hall Subgroups
aliases: [GT-A1, radical, O_p(G), O_pi(G), Hall subgroups, Hall's theorem, pi-separable groups, residue]
subject: group-theory
type: chapter
part: Advanced
by: [book, own-notes]
status: draft
prereq: ["[[GT08 Solvable Groups and Complements]]"]
tags: [subject/group-theory, type/chapter, src/book, src/own-notes, status/draft]
---
# GT-A1 · Radical, Residue and Hall Subgroups (advanced)

◀ [[Advanced Group Theory]] · [[GT08 Solvable Groups and Complements]] · [[Group Theory - Course Map|Course Map]]

> [!info] Source and approach
> Corresponds to K–S §6.3 (radical and residue, [[Kurzweil-Stellmacher_Theory of finite groups.pdf#page=141|PDF p.141]]) and §6.4 ($\pi$-separable groups, PDF p.146); PDF page = printed page + 13. **Guide chapter**: the section text was not read; definitions and statements are the standard ones; the proofs given (radical = intersection of Sylow subgroups; existence of Hall subgroups in solvable groups) are written out in full.

> [!tip] Start here
> - **The picture.** For a set of primes $\pi$, a **Hall $\pi$-subgroup** is a subgroup whose order is exactly the $\pi$-part of $|G|$ (a Sylow subgroup is the case $\pi=\{p\}$). In *solvable* groups Hall subgroups always exist; in non-solvable groups they can fail, and this failure characterises solvability.
> - **What you need.** Sylow theorems ([[GT05 Actions Conjugation and Sylow Theorems]]), solvable groups and the Schur–Zassenhaus theorem for Abelian $N$ ([[GT08 Solvable Groups and Complements]]).

> [!key] After this chapter you can
> - define $O_\pi(G)$ (the **radical**) and $O^\pi(G)$ (the **residue**) and compute them in small examples,
> - prove that $O_p(G)$ is the intersection of all Sylow $p$-subgroups,
> - define a **Hall $\pi$-subgroup** and **$\pi$-separable** groups,
> - prove that a **solvable** group has Hall $\pi$-subgroups for every set $\pi$ of primes, and state Hall's converse.

## 1. Radical and residue
> [!key] Definitions
> Let $\pi$ be a set of primes and $\pi'$ its complement. A **$\pi$-group** has all prime divisors of its order in $\pi$. $O_\pi(G)$ is the **largest normal $\pi$-subgroup** of $G$ (the product of all normal $\pi$-subgroups; it is a $\pi$-group because a product of two normal $\pi$-subgroups $A,B$ has order $|A||B|/|A\cap B|$). $O^\pi(G)$ is the **smallest normal subgroup $N$ with $G/N$ a $\pi$-group**. For one prime: $O_p(G)$, $O_{p'}(G)$, $O^p(G)$.

> [!derivation] Proposition 1.1. $O_p(G)$ equals the intersection of all Sylow $p$-subgroups of $G$.
> *Proof.* A normal $p$-subgroup $N$ lies in some Sylow $p$-subgroup $P$ (Sylow (a)); since $N$ is normal it is contained in all conjugates of $P$, i.e. in every Sylow $p$-subgroup. Hence $O_p(G)\le\bigcap_PP$. Conversely $\bigcap_PP$ is a $p$-group, and normal because conjugation permutes the Sylow $p$-subgroups (they are all conjugate). So it lies in $O_p(G)$. ∎

> [!example] Computed
> $O_2(S_4)=V_4$ (the three Sylow 2-subgroups $D_4$ meet exactly in $V_4$); $O_3(S_4)=1$; $O_2(A_4)=V_4$; $O_3(A_4)=1$. The Fitting subgroup is $F(G)=\prod_pO_p(G)$ (the largest nilpotent normal subgroup, [[GT07 p-Groups and Nilpotent Groups]]): $F(S_4)=O_2\cdot O_3=V_4$.

## 2. Hall subgroups and $\pi$-separable groups
> [!key] Definitions
> A **Hall $\pi$-subgroup** $H\le G$ is a $\pi$-group with $|G:H|$ a $\pi'$-number (so $|H|=|G|_\pi$, the $\pi$-part). $G$ is **$\pi$-separable** if it has a normal series $1=G_0\le\cdots\le G_r=G$ whose factors are each a $\pi$-group or a $\pi'$-group. Solvable groups are $\pi$-separable for **every** $\pi$ (their composition factors have prime order); $A_5$ is not $\{2\}$-separable (its single composition factor is neither a 2-group nor of odd order).

> [!derivation] Theorem 2.1 (Hall). A **solvable** group $G$ has a Hall $\pi$-subgroup for every set of primes $\pi$ (all of which are conjugate: stated).
> *What the proof is doing:* induct using a minimal normal subgroup $M$ (an elementary Abelian $p$-group, [[GT04 Commutators Simple Groups and Composition Series]]): pull back a Hall subgroup of $G/M$; if $p\in\pi$ the pull-back is already Hall, if $p\notin\pi$ it has $M$ as a normal Sylow subgroup of coprime index, so Schur–Zassenhaus splits it and the complement is Hall.
> *Proof.* Induct on $|G|$. Let $M$ be a minimal normal subgroup: elementary Abelian $p$-group. By induction $G/M$ has a Hall $\pi$-subgroup $H/M$ (with $M\le H$). *Case $p\in\pi$:* $|H|=|M||H/M|$ is a $\pi$-number and $|G:H|=|G/M:H/M|$ is a $\pi'$-number: $H$ is a Hall $\pi$-subgroup of $G$. *Case $p\notin\pi$:* $|H|=|M|\cdot(\pi\text{-number})$ with $M$ an Abelian normal subgroup of order a power of $p\notin\pi$, coprime to $|H:M|$; by Schur–Zassenhaus for Abelian $M$ ([[GT08 Solvable Groups and Complements]], §3) $M$ has a complement $L$ in $H$, $|L|=|H/M|$ a $\pi$-number, and $|G:L|=|G:H||M|$ is a $\pi'$-number. So $L$ is a Hall $\pi$-subgroup. ∎

> [!derivation] Hall's converse (stated). If a finite group has a Hall $\pi$-subgroup for **every** set $\pi$ of primes, it is solvable. Equivalently, a non-solvable group lacks some Hall subgroup.
> **Check with $A_5$** ($60=4\cdot3\cdot5$; computed): $A_5$ has $5$ Hall $\{2,3\}$-subgroups (the five copies of $A_4$, order 12), but **no** Hall $\{2,5\}$-subgroup (order 20) and **no** Hall $\{3,5\}$-subgroup (order 15): its subgroup orders are $1,2,3,4,5,6,10,12,60$. This is consistent with $A_5$ being non-solvable. $S_4$, being solvable, has all of them: Sylow 2 ($D_4$), Sylow 3 ($C_3$), and $S_4$ itself for $\{2,3\}$; $A_4$ has Hall $\{2\}$ ($V_4$) and $\{3\}$.

> [!example] Practice (with answers)
> 1. **Find $O_2$ and $O_{2'}$ of $S_3$.** *Answer:* $O_2(S_3)=1$ (no normal 2-subgroup); $O_{2'}(S_3)=A_3$ (largest normal subgroup of odd order).
> 2. **Which Hall subgroups does $A_5$ have?** *Answer:* a Hall $\{2,3\}$-subgroup (order 12: the five copies of $A_4$), the Sylow subgroups (Hall $\{p\}$), and *no* Hall $\{2,5\}$- or $\{3,5\}$-subgroup (no subgroups of order 20 or 15): so $A_5$ is not solvable, by Hall's converse.
> 3. **Why is a Hall $\{p\}$-subgroup just a Sylow $p$-subgroup?** *Answer:* order $|G|_p$ means the full $p$-part.

## 3. Where Hall subgroups appear
> [!connection] In other subjects
> - Hall's theorem is the group-theoretic form of "a solvable group splits into coprime parts" used when decomposing the symmetry group of a crystal into rotational and translational parts ([[Bloch Theorem]]) and for point groups of molecules, all solvable except the icosahedral ([[GT08 Solvable Groups and Complements]], [[GT10 Symmetry Representations and Characters]]).
> - Coprime-order decomposition is the same mechanism as the Chinese remainder theorem ([[GT03 Cyclic and Abelian Groups and Direct Products]]).
> **Concept notes:** [[Hall Subgroup]] · [[Radical of a Group]] · [[Fitting Subgroup]]

## Provenance
> [!provenance]- Source map
> | Topic | Source | Origin |
> |---|---|---|
> | radical, residue, $\pi$-separable groups | K–S §6.3–6.4 (PDF pp.141–153; TOC titles only) | book (by title) |
> | Proposition 1.1, Hall's theorem for solvable groups (existence), A5 Hall subgroups, examples | my write-up; computed in `scripts/gt_numbers2.py` and a one-off check | mine |
> | conjugacy of Hall subgroups, Hall's converse, definition of $\pi$-separable | recalled | not checked (`[verify]`) |
> **Flag.** The conjugacy part of Hall's theorem and the converse are stated, not proved.
