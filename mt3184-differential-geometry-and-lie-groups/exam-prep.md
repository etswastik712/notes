---
id: mt3184-differential-geometry-and-lie-groups/exam-prep
aliases: ["Exam prep: MT3184: Differential Geometry and Lie Groups"]
tags: [exam-prep, mt3184-differential-geometry-and-lie-groups]
trust_tier: agent_written
---

# Exam prep: MT3184: Differential Geometry and Lie Groups

<!-- kurooto:exam-prep (kept current by Kurooto from your courses; write your own notes outside these markers) -->
## Next assessment
Second class test: in the week of 2026-10-26 according to the syllabus outline (exact day, time and syllabus not announced; it should cover the exponential map material, since the same week is listed for one-parameter subgroups and the exponential map, a tutorial and the class test). Then the end-sem, 2026-11-23 to 2026-12-02 (cumulative; exact paper dates not announced). Grading: 2 class tests 20%, mid-term 40%, final 40%. Earlier: Test 1 ([[mt3184-differential-geometry-and-lie-groups/2026-09-03-test-i]], first announced on 2026-08-20 for 2026-08-31 on HW1-HW3 and DG 1-8) and the midterm (2026-09-24 15:00, month inferred).

## Covered so far
- [[mt3184-differential-geometry-and-lie-groups/2026-08-07-august-3-7]]: smooth manifolds, smooth maps, partitions of unity (slides not readable)
- [[mt3184-differential-geometry-and-lie-groups/2026-08-14-august-10-14]]: tangent spaces, differentials, change of coordinates (slides not readable)
- [[mt3184-differential-geometry-and-lie-groups/2026-08-20-august-17-21]]: submanifolds and their tangent spaces, Chart Lemma, tangent bundle, vector fields
- [[mt3184-differential-geometry-and-lie-groups/2026-08-20-hw3]]: HW3, tangent vectors of curves in projection charts, the tangent bundle via the Chart Lemma, a vector field on $S^2$ with one zero
- [[mt3184-differential-geometry-and-lie-groups/2026-08-27-august-24-28]]: vector fields, derivations, Lie groups and homomorphisms, rank theorems
- [[mt3184-differential-geometry-and-lie-groups/2026-09-03-august-31-september-4]]: immersed submanifolds, Lie subgroups, kernels, identity component
- [[mt3184-differential-geometry-and-lie-groups/2026-09-10-september-7-12]]: Closed Subgroup Theorem, group actions, orbits and stabilizers, semidirect products, Lie algebras
- [[mt3184-differential-geometry-and-lie-groups/2026-09-15-september-14-18]]: Lie correspondence, induced homomorphisms, Homomorphism Theorem
- [[mt3184-differential-geometry-and-lie-groups/2026-10-10-october-5-9]]: Lie subgroups revisited, $\mathrm{Lie}(G)$, $\mathfrak{gl}(n)$, $\mathrm{Lie}(SO(n))$, representations and Ado, integral curves, flows
- [[mt3184-differential-geometry-and-lie-groups/2026-10-16-october-12-16]]: naturality, complete fields, Flowout Theorem, regular/singular points, straightening, Lie derivatives
- [[mt3184-differential-geometry-and-lie-groups/2026-10-24-october-19-24]]: end of the Lie derivative, one-parameter subgroups, matrix exponential, the exponential map and its properties

## Must know
- Smooth structure: two smooth atlases induce the same smooth structure iff their union is a smooth atlas; every smooth atlas lies in a unique maximal one ([[mt3184-differential-geometry-and-lie-groups/2026-08-07-hw1]] Q1).
- Smoothness of a continuous map $F$ at $p$ can be checked in one pair of charts: $\psi\circ F\circ\varphi^{-1}$ smooth ([[mt3184-differential-geometry-and-lie-groups/2026-08-07-hw1]] Q3).
- Tangent vectors are local: if $f=g$ near $p$ then $v(f)=v(g)$; $T_{(p,q)}(M\times N)\cong T_pM\oplus T_qN$ via $(d\pi_1,d\pi_2)$ ([[mt3184-differential-geometry-and-lie-groups/2026-08-14-hw2]] Q1, Q2).
- Smooth Manifold Chart Lemma (Lemma 1.35): bijective charts onto open sets, open overlaps, smooth transitions, countably many charts covering, and separation of points give a unique smooth structure making them charts. $TM$ is then a $2n$-dimensional manifold with $\pi$ smooth (Prop 3.18); the chart on $\pi^{-1}(U)$ is $\tilde\varphi:\sum v^i\partial_i|_p\mapsto(\varphi(p),v^1,\dots,v^n)$ and the overlap maps are $(x,v)\mapsto(\varphi_\beta\circ\varphi_\alpha^{-1}(x),\,D(\varphi_\beta\circ\varphi_\alpha^{-1})_xv)$ ([[mt3184-differential-geometry-and-lie-groups/2026-08-20-august-17-21]]; proving this is [[mt3184-differential-geometry-and-lie-groups/2026-08-20-hw3]] Q2).
- Vector field: smooth $X: M\to TM$ with $\pi\circ X=\mathrm{id}$; smooth iff its component functions in every chart are smooth, iff $Xf\in C^\infty$ for all smooth $f$ (Prop 8.14). (Classroom: DG9)
- Derivations of $C^\infty(M)$ correspond to vector fields. (Classroom: DG10)
- $F$-related fields: $dF_p(X_p)=Y_{F(p)}$; a diffeomorphism $F$ gives a unique $F$-related $Y$ for each $X$ (Prop 8.19).
- Rank Theorem: constant rank $r$ ⇒ charts with $\psi\circ F\circ\varphi^{-1}(x)=(x^1,\dots,x^r,0,\dots,0)$. Global Rank Theorem: surjective ⇒ submersion; injective ⇒ immersion; bijective ⇒ diffeomorphism. (Classroom: DG11)
- A Lie group is a manifold that is a group with smooth multiplication and inversion; every Lie group homomorphism has constant rank (Thm 7.5).
- Immersed submanifold: a subset with its own topology and smooth structure such that the inclusion is an immersion; an injective immersion has an immersed image (Prop 5.18).
- Lie subgroup: a subgroup that is an immersed submanifold and a Lie group. $\ker F$ of a Lie group homomorphism is an embedded Lie subgroup of dimension $\dim G-\mathrm{rank}\,dF$ (Prop 7.16).
- The identity component $G_0$ is a normal, open, connected subgroup, the only such; the components are its cosets (Prop 7.15).
- Closed Subgroup Theorem: a subgroup $H\le G$ is closed iff it is an embedded Lie subgroup (Thm 20.12).
- Equivariant Rank Theorem: transitive $G$ on $M$, $F: M\to N$ equivariant ⇒ constant rank (Thm 7.25). Stabilizers are embedded Lie subgroups; orbits are immersed submanifolds.
- Lie algebra: a real vector space with a bilinear, antisymmetric bracket satisfying the Jacobi identity. $\mathrm{Lie}(G)$ is the Lie algebra of left-invariant vector fields; evaluation $\varepsilon:\mathrm{Lie}(G)\to T_eG$ is a vector space isomorphism (Thm 8.37). A Lie group homomorphism $F$ induces a Lie algebra homomorphism $F_*$ (Thm 8.44).
- Homomorphism Theorem: if $G$ is simply connected and $\varphi:\mathrm{Lie}(G)\to\mathrm{Lie}(H)$ is a Lie algebra homomorphism, there is a unique Lie group homomorphism $F:G\to H$ with $F_*=\varphi$. Lie's Third Theorem: every finite-dimensional real Lie algebra is $\mathrm{Lie}(G)$ for a simply connected $G$. (Classroom: DG18, DG20)
- $\mathrm{Lie}(GL(n,\mathbb R))\cong\mathfrak{gl}(n,\mathbb R)$ with $[A,B]=AB-BA$; $\mathrm{Lie}(SO(n))=\{A: A+A^T=0\}$ (DG20).
- Every Lie group is parallelizable (left-invariant global frame). Ado's Theorem: every finite-dimensional real Lie algebra has a faithful representation, hence embeds in some $\mathfrak{gl}(n,\mathbb R)$.
- Integral curve of $V$ at $p$: $\gamma'(t)=V_{\gamma(t)}$, $\gamma(0)=p$. Fundamental Theorem on Flows (Thm 9.12): $V$ has a unique maximal flow $\theta:D\to M$; $\theta^{(p)}$ is the maximal integral curve at $p$; $\theta_t:M_t\to M_{-t}$ is a diffeomorphism with inverse $\theta_{-t}$. (DG21, DG22)
- Naturality: if $X$ and $Y$ are $F$-related, $F$ maps integral curves of $X$ to integral curves of $Y$ (Prop 9.6) and $F\circ\theta_t=\eta_t\circ F$ (Prop 9.13).
- Uniform Time Lemma (9.15): a uniform $\varepsilon$ with $(-\varepsilon,\varepsilon)\subset D^{(p)}$ for all $p$ ⇒ $V$ complete. Compactly supported fields and left-invariant fields on Lie groups are complete (9.16, 9.18).
- Flowout Theorem (9.20): $V$ nowhere tangent to the embedded submanifold $S$ ⇒ $\Phi=\theta|_{D\cap(\mathbb R\times S)}$ is an immersion, injective near $\{0\}\times S$; in codimension 1 a diffeomorphism onto an open set.
- Singular point $V_p=0$ ⇒ $\theta^{(p)}$ constant; regular point ⇒ $\theta^{(p)}$ immersion (Prop 9.21); near a regular point there is a chart with $V=\partial/\partial s^1$ (Thm 9.22).
- Lie derivative via the flow; $\mathcal L_VW=[V,W]$ (Thm 9.38; exact statement was cut off in the OCR, check the PDF).
- One-parameter subgroup: a Lie group homomorphism $\gamma:\mathbb R\to G$. Thm 20.1: the one-parameter subgroups of $G$ are exactly the maximal integral curves, starting at $e$, of left-invariant vector fields. (Classroom: DG25)
- Prop 20.2: for $A\in\mathfrak{gl}(n,\mathbb R)$ the series $\sum A^k/k!$ converges (uniformly on bounded sets) to $e^A\in GL(n,\mathbb R)$, and $t\mapsto e^{tA}$ is the one-parameter subgroup generated by $A$. (DG26)
- Prop 20.3: for a Lie subgroup $H\le G$, the one-parameter subgroups of $H$ are those of $G$ with initial velocity in $T_eH$; so every homomorphism $\mathbb R\to SO(n)$ is $t\mapsto e^{tA}$ with $A$ skew-symmetric. (DG26)
- Exponential map: $\exp:\mathfrak g\to G$, $\exp X=\gamma_X(1)$; $\exp(sX)$ is the one-parameter subgroup generated by $X$ (Prop 20.5); $\exp$ is smooth, $\exp((s+t)X)=\exp(sX)\exp(tX)$, $\exp(-X)=(\exp X)^{-1}$, $(\exp X)^n=\exp(nX)$; for $GL(n,\mathbb R)$, $\exp A=e^A$; $d\exp_0=\mathrm{id}$, so $\exp$ is a local diffeomorphism at $0$. (DG26)

## Typical questions
- Atlas questions: maximal atlases, same smooth structure iff union is an atlas, transition maps of the graph and stereographic atlases of $S^2$, distinct smooth structures on a ball ([[mt3184-differential-geometry-and-lie-groups/2026-08-07-hw1]]).
- Tangent vector computations: locality, product manifolds, $Xf$ and change of basis between stereographic charts, local form and derivative of the antipodal map, curves realising a tangent vector ([[mt3184-differential-geometry-and-lie-groups/2026-08-14-hw2]]).
- Velocity of an explicit curve on $S^2$ in a projection chart, differential of a rotation of $S^2$ in local coordinates, change of basis between projection charts ([[mt3184-differential-geometry-and-lie-groups/2026-08-20-hw3]] Q1).
- Prove $TM$ is a manifold and $\pi$ smooth with the Chart Lemma ([[mt3184-differential-geometry-and-lie-groups/2026-08-20-hw3]] Q2).
- Build a vector field on $S^2$ with exactly one zero: push a constant field on $\mathbb R^2$ through the inverse stereographic chart, write it in the other chart, check smooth extension of its components ([[mt3184-differential-geometry-and-lie-groups/2026-08-20-hw3]] Q3).
- Level sets of regular values are submanifolds with $T_pS=\ker dF_p$ (HW4 Q1).
- $F$-related fields under an explicit diffeomorphism (HW4 Q3).
- Differentials of the group operations, $dm_{(e,e)}(X,Y)=X+Y$ and $di_e=-1$ (HW4 Q6).
- Immersed vs embedded submanifold criteria: proper, compact, equal dimension (HW5 Q1).
- Derivative of $\det$ and the trace (HW5 Q3, HW6 Q7).
- Stabilizers and $U(n)$ as embedded Lie subgroups; semidirect product decompositions (HW6 Q1-Q3).
- Lie brackets of explicit vector fields; abelian Lie group ⇒ abelian Lie algebra (HW6 Q5, Q6).
- Classify low-dimensional Lie algebras; compute $\mathrm{Lie}(SO(n))$, $\mathrm{Lie}(SO(3))\cong(\mathbb R^3,\times)$; kernel of $F_*$ ([[mt3184-differential-geometry-and-lie-groups/2026-10-10-hw7]] Q1-Q3).
- Maximal integral curve is constant, injective or periodic; compute an explicit flow such as that of $y\partial_x+\partial_y$; fixed-point-free map homotopic to the identity ([[mt3184-differential-geometry-and-lie-groups/2026-10-10-hw7]] Q4-Q6).
- Reparametrised integral curves, completeness of compactly supported fields, escape from compact sets, Flowout embedding, $D_vW=\mathcal L_VW$, non-dependence of $\mathcal L_VW$ on $V$ along a curve only ([[mt3184-differential-geometry-and-lie-groups/2026-10-16-hw8]] Q1-Q6).
- Tangent-vector and chart computations (Test 1: [[mt3184-differential-geometry-and-lie-groups/2026-09-03-test-i]]).
- Prove that the one-parameter subgroups are the integral curves of left-invariant fields; prove $e^A\in GL(n,\mathbb R)$ and that $e^{tA}$ is a one-parameter subgroup; compute $\exp$ for $GL(n)$, $SO(n)$ ([[mt3184-differential-geometry-and-lie-groups/2026-10-24-october-19-24]]; no homework on this yet).

## Gaps
- Slides DG1-DG7 are scans with no readable text, so weeks 1-3 are only summarised from the posts and homework (definitions of manifolds, tangent spaces and partitions of unity are not noted in detail). DG8 is badly garbled OCR.
- DG16 (rest), the end of DG20 (explicit Lie algebra example), the end of DG24 (Lie derivative and $[V,W]$), parts of DG23 and the first page and last slide of DG25/DG26 (properties of $\mathcal L_V$; $\exp$ and homomorphisms) were only partly legible; the rest of DG16 is not yet noted.
- Handwritten slides are OCR-garbled in places; check definitions and statements against the PDFs before relying on them (notably Thm 20.19, the Flowout hypotheses, Prop 9.13, Thm 9.38 and the smoothness proof of $\exp$).
- HW3 is filed as a problem list only; no solutions are in the materials, and the stereographic-chart formulas for Q3 are not worked out anywhere in the notes.
- The date and syllabus of the second class test are not announced; the midterm's marks/solutions are not known; Test 1 solutions beyond Q1 were unreadable. The 2026-08-31 date announced for Test 1 differs from the 2026-09-03 date in the notes.
- The syllabus lists differential forms, Stokes' Theorem, infinitesimal generators of group actions and the Closed Subgroup Theorem for later weeks; the Closed Subgroup Theorem is noted but differential forms and Stokes appear in no filed lecture note yet.
- The 24 October replacement class (exponential map) is filed; no homework on the exponential map yet.
- No textbook notes (Lee, Boothby) were found in the books folder, so nothing here cites a book page.
<!-- /kurooto:exam-prep -->
