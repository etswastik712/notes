---
id: mt3184-differential-geometry-and-lie-groups/exam-prep
aliases: ["Exam prep: MT3184: Differential Geometry and Lie Groups"]
tags: [exam-prep, mt3184-differential-geometry-and-lie-groups]
trust_tier: agent_written
---

# Exam prep: MT3184: Differential Geometry and Lie Groups

<!-- kurooto:exam-prep (kept current by Kurooto from your courses; write your own notes outside these markers) -->
## Next assessment
No further assessment announced yet. Midterm exam was announced for the 24th at 3pm (2026-09-24, month inferred; it covered everything up to DG18, including all homework, class notes and theorems). Test 1 (on Homework 1-3) took place earlier: [[mt3184-differential-geometry-and-lie-groups/2026-09-03-test-i]].

## Covered so far
- [[mt3184-differential-geometry-and-lie-groups/2026-08-27-august-24-28]]: vector fields, derivations, Lie groups and homomorphisms, rank theorems
- [[mt3184-differential-geometry-and-lie-groups/2026-09-03-august-31-september-4]]: immersed submanifolds, Lie subgroups, kernels, identity component
- [[mt3184-differential-geometry-and-lie-groups/2026-09-10-september-7-12]]: Closed Subgroup Theorem, group actions, orbits and stabilizers, semidirect products, Lie algebras
- [[mt3184-differential-geometry-and-lie-groups/2026-09-15-september-14-18]]: Lie correspondence, induced homomorphisms, Homomorphism Theorem
- [[mt3184-differential-geometry-and-lie-groups/2026-10-10-october-5-9]]: Lie subgroups revisited, $\mathrm{Lie}(G)$, $\mathfrak{gl}(n)$, $\mathrm{Lie}(SO(n))$, representations and Ado, integral curves, flows
- [[mt3184-differential-geometry-and-lie-groups/2026-10-16-october-12-16]]: naturality, complete fields, Flowout Theorem, regular/singular points, straightening, Lie derivatives
- [[mt3184-differential-geometry-and-lie-groups/2026-10-24-october-19-24]]: end of the Lie derivative, one-parameter subgroups, matrix exponential, the exponential map and its properties

## Must know
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
- DG16 (rest), the end of DG20 (explicit Lie algebra example), the end of DG24 (Lie derivative and $[V,W]$), parts of DG23 and the first page and last slide of DG25/DG26 (properties of $\mathcal L_V$; $\exp$ and homomorphisms) were only partly legible; the rest of DG16 is not yet noted.
- Handwritten slides are OCR-garbled in places; check definitions and statements against the PDFs before relying on them (notably Thm 20.19, the Flowout hypotheses, Prop 9.13, Thm 9.38 and the smoothness proof of $\exp$).
- The midterm's month and its marks/solutions are not known; no syllabus or marking scheme given yet; Test 1 solutions beyond Q1 were unreadable.
- The 24 October replacement class (exponential map) is now filed; whether it replaces the cancelled 19 October class or is extra is not stated. No homework on the exponential map yet.
- No textbook notes found for this course in the books folder.
<!-- /kurooto:exam-prep -->
