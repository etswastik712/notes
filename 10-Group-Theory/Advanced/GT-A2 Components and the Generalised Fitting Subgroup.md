---
title: GT-A2 Components and the Generalised Fitting Subgroup
aliases: [GT-A2, components, quasisimple, generalised Fitting subgroup, F*(G), layer E(G)]
subject: group-theory
type: chapter
part: Advanced
by: [book, own-notes]
status: draft
prereq: ["[[GT07 p-Groups and Nilpotent Groups]]", "[[GT04 Commutators Simple Groups and Composition Series]]"]
tags: [subject/group-theory, type/chapter, src/book, src/own-notes, status/draft]
---
# GT-A2 · Components and the Generalised Fitting Subgroup (advanced)

◀ [[Advanced Group Theory]] · [[GT07 p-Groups and Nilpotent Groups]] · [[Group Theory - Course Map|Course Map]]

> [!info] Source and approach
> Corresponds to K–S §6.5 ([[Kurzweil-Stellmacher_Theory of finite groups.pdf#page=154|PDF p.154]]); PDF page = printed page + 13. **Guide chapter**: the section text was not read. The proof that $C_G(F(G))\le F(G)$ for **solvable** $G$ is written out in full; the general statement for $F^*(G)$ is quoted.

> [!tip] Start here
> - **The picture.** In a solvable group the largest nilpotent normal subgroup $F(G)$ "controls" the group: nothing outside $F(G)$ commutes with all of it. For a general finite group this is no longer true (e.g. $G=A_5$ has $F(G)=1$), and one has to add the **non-Abelian simple-like pieces**, the *components*. The result is the **generalised Fitting subgroup** $F^*(G)$, which again controls the group: $C_G(F^*(G))\le F^*(G)$.
> - **What you need.** Nilpotent groups and the Fitting subgroup ([[GT07 p-Groups and Nilpotent Groups]]), simple groups ([[GT04 Commutators Simple Groups and Composition Series]]).

> [!key] Definitions
> A group $L$ is **quasisimple** if $L=L'$ (perfect) and $L/Z(L)$ is simple. A **component** of $G$ is a subnormal quasisimple subgroup. The **layer** $E(G)$ is the product of all components; the **generalised Fitting subgroup** is $F^*(G)=F(G)\,E(G)$. *Examples:* $A_5$ is simple, hence quasisimple; $SL_2(5)$ (order 120, perfect, $/Z\cong A_5$; recalled) is quasisimple but not simple.

> [!derivation] Theorem 1 (Fitting, solvable case). If $G$ is solvable then $C_G(F(G))\le F(G)$.
> *What the proof is doing:* if something outside $F=F(G)$ centralised $F$, take a minimal normal subgroup of the quotient inside the centraliser; it would be nilpotent, normal and bigger than allowed.
> *Proof.* Let $F=F(G)$, $C=C_G(F)\trianglelefteq G$. Then $C\cap F=Z(F)$ (elements of $F$ commuting with all of $F$). Suppose $C\not\le F$, i.e. $C\ne Z(F)$. Then $C/Z(F)$ is a non-trivial solvable normal subgroup of $G/Z(F)$ (here $Z(F)\trianglelefteq G$ as characteristic in $F$). Choose a minimal normal subgroup $M/Z(F)$ of $G/Z(F)$ inside it; it is an elementary Abelian $p$-group (GT04, Theorem 3.1). The subgroup $M\le C$ centralises $Z(F)\le F$, so $Z(F)\le Z(M)$, and $M/Z(M)$ is a quotient of the $p$-group $M/Z(F)$, hence nilpotent; a group with $M/Z(M)$ nilpotent is nilpotent, so **$M$ is a nilpotent normal subgroup of $G$**, thus $M\le F$. But $M\le C$, so $M\le C\cap F=Z(F)$, i.e. $M/Z(F)=1$, a contradiction. Hence $C\le F$. ∎

> [!key] Theorem 2 (stated, K–S §6.5). For every finite group $G$: $C_G(F^*(G))\le F^*(G)$ (indeed $C_G(F^*)=Z(F^*)$). This is the structural backbone of the classification of finite simple groups.

> [!example] Computed
> | $G$ | $F(G)$ | $E(G)$ | $F^*(G)$ | $C_G(F^*)$ |
> |---|---|---|---|---|
> | $S_4$ | $V_4$ | $1$ | $V_4$ | $V_4$ (order 4) |
> | $S_3$ | $A_3$ | $1$ | $A_3$ | $A_3$ |
> | $A_5$ | $1$ | $A_5$ | $A_5$ | $1$ |
> | $S_5$ | $1$ | $A_5$ | $A_5$ | $1$ (computed: $|C_{S_5}(A_5)|=1$) |
> In the solvable cases $F^*=F$; in $A_5$ and $S_5$ the Fitting subgroup is trivial and the control comes entirely from the component $A_5$.

> [!connection] In other subjects
> The statement "something is controlled by its simplest normal pieces" is the group-theoretic analogue of **the nilradical and Levi decomposition of Lie algebras** (relevant to the Lie-group notes of MT3184 referenced from [[GT10 Symmetry Representations and Characters]] §6) and of building a molecule's symmetry from its rotation subgroup and reflections. **Concept notes:** [[Generalised Fitting Subgroup]] · [[Quasisimple Group]] · [[Fitting Subgroup]]

## Provenance
> [!provenance]- Source map
> | Topic | Source | Origin |
> |---|---|---|
> | components, layer, generalised Fitting subgroup | K–S §6.5 (PDF p.154; TOC title only) | book (by title) |
> | proof of $C_G(F)\le F$ for solvable $G$, table of examples | my write-up; computed (`scripts/gt_numbers2.py`: $C_{S_4}(V_4)$, $C_{S_5}(A_5)$) | mine |
> | $C_G(F^*)\le F^*$ in general, order and quasisimplicity of $SL_2(5)$ | recalled | not checked (`[verify]`) |
