---
id: mt3184-differential-geometry-and-lie-groups/2026-11-16-midsem-exam
aliases: [MT3184 Midsem exam and solutions]
tags: [mt3184, exam, midsem]
trust_tier: agent_written
---
# Midsem Exam (2026-11-16)

## Covered
The exam paper (IISER Pune, Mid-Sem 2026 August Semester, MT3184, instructor Tejas Kalelkar, dated 24-09-2026, 2 hrs, 40 marks) and the instructor's handwritten solutions. Conventions: all manifolds are smooth, connected, without boundary; a Lie algebra $\mathfrak g$ is abelian if $[X,Y]=0$ for all $X,Y$.

Questions, with what each practises and the solution's approach (the solutions PDF is handwritten and its text extraction is badly garbled, so only the visible outline is given; check the PDF for details):

1. (4 pts) Define (a) a tangent vector of a manifold, (b) a partition of unity subordinate to a cover. Solution: (a) a tangent vector at $p$ is a linear map $v:C^\infty(M)\to\mathbb R$ satisfying the Leibniz rule $v(fg)=f(p)v(g)+g(p)v(f)$; (b) for a cover $\{U_\alpha\}$, smooth maps $\psi_\alpha:M\to[0,1]$ with $\operatorname{supp}\psi_\alpha\subset U_\alpha$, the supports locally finite, and $\sum_\alpha\psi_\alpha\equiv1$.
2. (7 pts) On $S^2$ with $f(x,y,z)=z$: define the stereographic atlas $\mathcal A_S$, give an atlas $\mathcal A_{\mathbb R}$ of $\mathbb R$, and compute the derivative of $f$ at $(0,1,0)$ in these charts. The solution uses the two stereographic charts with $\mathrm{id}_{\mathbb R}$ on $\mathbb R$; the result is a $1\times2$ Jacobian matrix. My own check, assuming projection from the north pole with $f=\frac{|u|^2-1}{|u|^2+1}$ and $(0,1,0)\leftrightarrow u=(0,1)$: $\partial f/\partial u_i=4u_i/(|u|^2+1)^2$ gives $(0\ \ 1)$. The solution's exact chart convention was not legible, so the signs may differ.
3. (7 pts) An immersed submanifold $S$ of $M$ that is compact is embedded. Two solutions are given. (i) By contradiction: suppose $p\in S$ has no slice-chart neighbourhood; by the constant rank theorem there are charts $(U,\varphi)$ at $p$ in $S$ and $(V,\psi)$ at $\iota(p)$ in $M$ where $\iota$ is $x\mapsto(x,0)$; failure of slice charts gives points $p_n\in S$ with $\iota(p_n)\to\iota(p)$ but $p_n\notin U$; compactness gives a subsequence $p_{n_j}\to q\in S$, continuity gives $\iota(p_{n_j})\to\iota(q)$, Hausdorffness of $M$ gives $\iota(q)=\iota(p)$, injectivity gives $q=p$, so $p_{n_j}\in U$ eventually: contradiction. (ii) The inclusion $\iota:S\to M$ is an injective continuous map from a compact space to a Hausdorff space, so closed (closed subset of compact is compact, its continuous image is compact, hence closed in $M$), hence a homeomorphism onto its image with the subspace topology, i.e. a topological embedding. An immersion that is a topological embedding is an embedding, and constant-rank charts then give slice charts.
4. (7 pts) $F:M\to N$ smooth and equivariant for a transitive smooth $G$-action on $M$ and any smooth $G$-action on $N$ ⇒ $F$ has constant rank. Solution: with actions $\theta$ on $M$, $\psi$ on $N$, equivariance $F\circ\theta_g=\psi_g\circ F$; differentiate at $x$: $dF_{g x}\circ d(\theta_g)_x=d(\psi_g)_{F(x)}\circ dF_x$; $\theta_g,\psi_g$ are diffeomorphisms so $dF_{gx}$ and $dF_x$ have the same rank; by transitivity every point is $g x$.
5. (7 pts) $G,H$ connected Lie groups, homomorphisms $F_1,F_2:G\to H$ equal on an open set $U$ ⇒ $F_1=F_2$. Solution: take $g\in U$; $V=g^{-1}U$ is a neighbourhood of $e$; for $x\in V$, $gx\in U$, so $F_1(g)F_1(x)=F_2(g)F_2(x)$ and $F_1(g)=F_2(g)$ give $F_1=F_2$ on $V$; a neighbourhood of $e$ generates the connected group $G$ (the subgroup $\langle V\rangle$ is open, hence closed, hence all of $G$); homomorphisms agreeing on generators agree everywhere.
6. (8 pts) Non-abelian 2-dimensional Lie algebra $\mathfrak g$: (a) for a basis $(V_1,V_2)$ and $X=a_1V_1+a_2V_2$, $Y=b_1V_1+b_2V_2$, bilinearity and antisymmetry give $[X,Y]=(a_1b_2-a_2b_1)[V_1,V_2]$; (b) there is a basis $(W_1,W_2)$ with $[W_1,W_2]=W_2$ (the solution picks a nonzero bracket $W_2$ spanning the image and rescales; handwriting garbled); (c) any other non-abelian 2-dimensional Lie algebra $\mathfrak h$ has such a basis too, and the linear map sending basis to basis is a Lie algebra isomorphism.

Where to practise: Q2 ← [[mt3184-differential-geometry-and-lie-groups/2026-08-20-hw3]]; Q3 ← [[mt3184-differential-geometry-and-lie-groups/2026-09-03-august-31-september-4]]; Q4 ← equivariant rank theorem ([[mt3184-differential-geometry-and-lie-groups/2026-08-27-august-24-28]]); Q5 ← [[mt3184-differential-geometry-and-lie-groups/2026-11-06-hw10]] Q1; Q6 ← [[mt3184-differential-geometry-and-lie-groups/2026-10-10-hw7]] (low-dimensional Lie algebras).

## From the post
Mid-semester exam and their solutions.

## Files
- [Midsem.pdf](https://drive.google.com/file/d/1H5AcnJrcPS3qDdQuLxD-Nsvik2jRmF4r/view?usp=drive_web): the paper, read in full.
- [DG Midsem Solutions.pdf](https://drive.google.com/file/d/15gg6c0wKm2lgJgoGCfC0-x7TivMpyR4K/view?usp=drive_web): handwritten solutions; the text layer is heavily garbled (especially Q2 and Q6), so only the legible parts are summarised.

## Related
- [[mt3184-differential-geometry-and-lie-groups/2026-08-07-hw1]]: atlases and smooth structures (Q1, Q2)
- [[mt3184-differential-geometry-and-lie-groups/2026-08-20-hw3]]: projection/stereographic-type charts on $S^2$ (Q2)
- [[mt3184-differential-geometry-and-lie-groups/2026-09-03-august-31-september-4]]: immersed vs embedded submanifolds (Q3)
- [[mt3184-differential-geometry-and-lie-groups/2026-11-06-hw10]]: homomorphisms agreeing on a neighbourhood of $e$ (Q5)
- [[mt3184-differential-geometry-and-lie-groups/2026-10-10-hw7]]: low-dimensional Lie algebras (Q6)

<!-- kurooto:material5ea37376 -->
## Concepts in Midsem
[[zettel/abelian-lie-algebra]], [[zettel/tangent-vector-of-a-manifold]], [[zettel/partition-of-unity-subordinate-to-a-cover]], [[zettel/compact-immersed-submanifold-embedding-theorem]], [[zettel/equivariant-map-constant-rank-theorem]], [[zettel/identity-of-connected-lie-group-homomorphisms]], [[zettel/classification-of-two-dimensional-non-abelian-lie-algebras]]
<!-- /kurooto:material5ea37376 -->
