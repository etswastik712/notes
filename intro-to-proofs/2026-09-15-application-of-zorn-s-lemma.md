---
id: intro-to-proofs/2026-09-15-application-of-zorn-s-lemma
aliases: [Zorn's lemma, Existence of a basis]
tags: [intro-to-proofs, posets, zorn, linear-algebra]
trust_tier: agent_written
---
# Application of Zorn's lemma

## Covered
Source: Zorn's_lemma.pdf (Classroom: Application of Zorn's lemma).

**Definitions.** A *chain* in a poset $(P,\le)$ is a subset $C$ whose elements are pairwise comparable. $u\in P$ is an *upper bound* of $C$ if $x\le u$ for all $x\in C$. $m\in P$ is *maximal* if $m\le x\Rightarrow x=m$ for all $x\in P$ (nothing in $P$ is strictly larger).

**Zorn's Lemma.** Let $(P,\le)$ be a nonempty poset in which every chain has an upper bound in $P$. Then $P$ has a maximal element.

**Theorem.** Every vector space $V$ over a field $F$ has a basis. A basis is a subset $B$ that is linearly independent (whenever $a_1v_1+\dots+a_nv_n=0$ with $v_i\in B$, all $a_i=0$) and has $\mathrm{span}(B)=V$, where $\mathrm{span}(S)=\bigcap\{W\le V: S\subseteq W\}$.

**Case $V=\{0\}$.** $\varnothing$ is a basis: it is vacuously linearly independent; $\mathrm{span}(\varnothing)=\bigcap_{W\le V}W$, every subspace contains $0$ so $0$ is in the intersection, and $\{0\}$ is itself a subspace so the intersection is inside $\{0\}$; hence $\mathrm{span}(\varnothing)=\{0\}=V$.

**Case $V\ne\{0\}$.** Let $\mathcal P=\{S\subseteq V: S\text{ linearly independent}\}$, ordered by inclusion.
1. $\mathcal P\ne\varnothing$ since $\varnothing\in\mathcal P$.
2. Every chain $\mathcal C\subseteq\mathcal P$ has an upper bound: let $U=\bigcup_{S\in\mathcal C}S$. If $a_1v_1+\dots+a_nv_n=0$ with $v_i\in U$, pick $S_i\in\mathcal C$ with $v_i\in S_i$. Finitely many comparable sets have a largest one $S_j$, so all $v_i\in S_j$, which is independent, hence all $a_i=0$. So $U\in\mathcal P$ and $S\subseteq U$ for all $S\in\mathcal C$.
3. By Zorn there is a maximal $B\in\mathcal P$; it is linearly independent. Claim $\mathrm{span}(B)=V$. If not, pick $v\notin\mathrm{span}(B)$. If $a_1b_1+\dots+a_nb_n+\lambda v=0$ with $b_i\in B$: $\lambda\ne0$ would give $v=-\lambda^{-1}(a_1b_1+\dots+a_nb_n)\in\mathrm{span}(B)$, contradiction; so $\lambda=0$, and independence of $B$ gives all $a_i=0$. Thus $B\cup\{v\}\in\mathcal P$ and $B\subsetneq B\cup\{v\}$, contradicting maximality. So $B$ is a basis.

Proof pattern: define the poset of the right objects (here independent sets), check non-emptiness, show a union of a chain stays in the poset, take the maximal element, show it has the wanted property by contradiction.

## From the post
(no text)

## Files
- [Zorn's_lemma.pdf](https://drive.google.com/file/d/1XCuUI5y5WUkckvaB9Pw5RtFU2WNPMEsX/view?usp=drive_web) (saved as intro-to-proofs/2026-10-25-zorn-s-lemma-1XCuUI.pdf)

## Related
- [[11-Proofs-Analysis-Topology/Concepts/Zorn's Lemma]]: their concept note
- [[11-Proofs-Analysis-Topology/Concepts/Basis of a Vector Space]]: basis definition
- [[11-Proofs-Analysis-Topology/Concepts/Partially Ordered Set]]: posets, chains
- [[11-Proofs-Analysis-Topology/PA03 Relations Equivalence and Order]]: their chapter with this proof (section 4)
