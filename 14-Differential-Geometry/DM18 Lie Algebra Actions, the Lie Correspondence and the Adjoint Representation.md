---
title: DM18 Lie Algebra Actions, the Lie Correspondence and the Adjoint Representation
aliases: [DM18, infinitesimal generator, Lie algebra action, fundamental theorem on Lie algebra actions, Lie correspondence, simply connected Lie groups, adjoint representation, Ad and ad, normal subgroups and ideals, HW11, MT3184 midsem]
subject: diff-geometry
type: chapter
chapter: 18
part: IV
scope: [taught, extra-beyond]
by: [lecture-notes]
status: draft
prereq: ["[[DM17 Foliations, Weakly Embedded Submanifolds and Lie Subgroups]]", "[[DM15 Closed Subgroups and the Lie Correspondence]]", "[[DM14 One-Parameter Subgroups and the Exponential Map]]"]
tags: [subject/diff-geometry, type/chapter, taught, extra/beyond, src/lecture-notes, status/draft]
---
# DM18 · Lie Algebra Actions, the Lie Correspondence and the Adjoint Representation

◀ [[DM17 Foliations, Weakly Embedded Submanifolds and Lie Subgroups]] · [[Differential Geometry - Course Map|Course Map]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map (MT3184, weeks of 9–13 and 16–20 Nov 2026)
> 🟢 **Taught** (class notes posted on Classroom, read as page images): [[DG31.pdf]]–[[DG33.pdf]] ("we revised the infinitesimal generator of a group action and studied the Lie correspondence between simply connected Lie groups and finite dimensional Lie algebras"), [[DG34.pdf]] ("we used the adjoint representation to show that a Lie subgroup is normal if and only if its Lie algebra is an ideal"), [[HW11.pdf|Homework 11]], and the mid-semester exam [[Midsem.pdf]] with [[DG Midsem Solutions .pdf|solutions]] (posted 16 Nov).
> **Exam scope** (Classroom, 16 and 18 Nov): the final (Thursday **26 Nov, 10 am–12 pm**) covers the material of **HW5–HW11**; the proof of **Theorem 20.16** (complete $\mathfrak g$-actions integrate to $G$-actions for simply connected $G$) "will not be included in the final exam". Test 2 returned Tue 24 Nov (11:30–12, office).
> 🔵 **Extra · beyond (mine):** the HW11 and midsem solution outlines; the cross-references. Theorem numbers are the notes' (= Lee, *Introduction to Smooth Manifolds* 2nd ed.).

> [!key] After this chapter you can
> - define the **infinitesimal generator** $\hat\theta:\mathrm{Lie}(G)\to\mathfrak X(M)$ of a right action and prove it is a Lie algebra homomorphism (Thm 20.15),
> - state the **Fundamental Theorem on Lie algebra actions** (Thm 20.16) and use it to prove the **Lie correspondence** (Thm 20.19, Cor 20.20; surjectivity via Ado),
> - define $C_g$, $\mathrm{Ad}$, $\mathrm{ad}$, prove $\mathrm{Ad}$ is a homomorphism and $\mathrm{Ad}_*=\mathrm{ad}$ (Prop 20.24, Thm 20.27),
> - prove **$H\trianglelefteq G\iff\mathrm{Lie}(H)$ is an ideal** (Thm 20.28, via Lemma 20.23), and that $G$ is abelian iff $\mathfrak g$ is,
> - show $\exp:\mathfrak{sl}(2,\mathbb R)\to SL(2,\mathbb R)$ is **not surjective**.

> [!intuition] One sentence
> Everything a connected Lie group does near the identity is recorded in its Lie algebra, and for simply connected groups that record is complete: Lie algebra maps integrate to group maps, Lie algebra actions to group actions, ideals to normal subgroups — the adjoint representation is the bridge that turns conjugation in $G$ into brackets in $\mathfrak g$.

## 1. Subalgebras give subgroups (recap of Thm 19.26)
<span class="scope-taught">taught</span> *[[DG31.pdf#page=1|DG31 p.1]]*

If $\mathfrak h\subseteq\mathfrak g=\mathrm{Lie}(G)$ is a Lie subalgebra, $D_g=d(L_g)_e(\mathfrak h)$ defines a **left-invariant involutive distribution**; Frobenius gives a left-invariant foliation, and its leaf through $e$ is the unique connected Lie subgroup $H$ with $\mathrm{Lie}(H)=\mathfrak h$. So **{connected Lie subgroups of $G$} ↔ {Lie subalgebras of $\mathfrak g$}**, $H\mapsto\mathrm{Lie}(H)$, is a bijection ([[DM17 Foliations, Weakly Embedded Submanifolds and Lie Subgroups]] §6). Recall too ([[DG34.pdf#page=4|DG34 p.4]]): for a Lie subgroup $H$, $\mathfrak h=\{X\in\mathfrak g:\exp tX\in H\ \forall t\}$.

## 2. Infinitesimal generators of actions
<span class="scope-taught">taught</span> *[[DG31.pdf#page=1|DG31 pp.1–4]]*

**Flows as $\mathbb R$-actions.** A complete vector field $V$ on $M$ has a global flow $\theta:\mathbb R\times M\to M$, $\theta(t,p)=\gamma_p(t)$ (the integral curve from $p$): an $\mathbb R$-action whose infinitesimal generator is $V$: $\partial_t|_{t=0}\theta(t,p)=V_p$. Conversely, with $G=\mathbb R$, $\mathfrak g=\mathbb R$ (trivial bracket), a Lie algebra homomorphism $\hat\theta:\mathbb R\to\mathfrak X(M)$ with $\hat\theta(1)=V$ has $\hat\theta(x)=xV$, all complete if $V$ is: so there is an $\mathbb R$-action with infinitesimal generator $V$. For $X\in\mathrm{Lie}(G)$ (left-invariant), the flow is $\theta(t,p)=p\cdot\exp(tX)$ ($L_p$ carries integral curves from $e$ to integral curves from $p$).

**Definition.** For a smooth **right** action $\theta:M\times G\to M$, $(p,g)\mapsto p\cdot g$, and $X\in\mathrm{Lie}(G)$, the flow $\varphi(t,p)=p\cdot\exp(tX)$ is a flow ($\varphi(0,p)=p$; $\varphi(s+t,p)=(p\exp sX)\exp tX$ because $\theta$ is an action). Its infinitesimal generator
$$\hat X_p=\frac{d}{dt}\Big|_{t=0}p\cdot\exp(tX),\qquad\hat\theta(X):=\hat X .$$

> [!key] Theorem 20.15 — $\hat\theta:\mathrm{Lie}(G)\to\mathfrak X(M)$ is a Lie algebra homomorphism
> With the orbit map $\theta^{(p)}(g)=p\cdot g$: $d(\theta^{(p)})_e(X_e)=\frac d{dt}|_0\,p\exp tX=\hat X_p$, and $X$ and $\hat X$ are **$\theta^{(p)}$-related**: $d(\theta^{(p)})_g(X_g)=d(\theta^{(p)}\circ L_g)_e(X_e)=d(\theta^{(p\cdot g)})_e(X_e)=\hat X_{p\cdot g}$ (since $\theta^{(p)}\circ L_g=\theta^{(p\cdot g)}$). **Linear:** $\hat\theta(aX+bY)_p=d(\theta^{(p)})_e(aX_e+bY_e)$. **Brackets:** related fields have related brackets, so $[\hat X,\hat Y]_p=d(\theta^{(p)})_e([X,Y]_e)=\widehat{[X,Y]}_p$ ([[DM10 Vector Fields and Lie Brackets]]). (HW11 Q1 asks for the relatedness; "this is worked out in the notes".)

Any Lie algebra homomorphism $\hat\theta:\mathfrak g\to\mathfrak X(M)$ is called a (right) **$\mathfrak g$-action**; it is **complete** if every $\hat\theta(X)$ is a complete vector field.

> [!key] Theorem 20.16 — Fundamental Theorem on Lie algebra actions ([[DG31.pdf#page=4|DG31 p.4]])
> $M$ smooth, $G$ **simply connected** with $\mathfrak g=\mathrm{Lie}(G)$, $\hat\theta:\mathfrak g\to\mathfrak X(M)$ a complete $\mathfrak g$-action. Then there is a **unique** smooth right $G$-action on $M$ whose infinitesimal generator is $\hat\theta$.
> *Its proof was given on 17 Nov and is **not examinable**.* ([[DG32.pdf#page=1|DG32 p.1]] draws the correspondence: right $G$-actions ⇄ complete right $\mathfrak g$-actions.)

## 3. Simply connected groups and covers
<span class="scope-taught">taught</span> *[[DG32.pdf#page=1|DG32 p.1]]*

$X$ is **simply connected** if connected and every loop $\alpha:S^1\to X$ is homotopic to a constant ($H:S^1\times I\to X$, $H(\cdot,0)=\alpha$, $H(\cdot,1)$ constant) ([[PA15 Covering Spaces and the Fundamental Group]]). Every connected Lie group $G$ has a **unique simply connected Lie group $\tilde G$** with a surjective Lie group homomorphism $p:\tilde G\to G$ that is a covering map (each $g$ has an open $U\ni g$ with $p^{-1}(U)=\bigsqcup V_\alpha$, $p|_{V_\alpha}$ a diffeomorphism). If $G$ is already simply connected, any such $p$ is a diffeomorphism.

## 4. The Lie correspondence
<span class="scope-taught">taught</span> *[[DG32.pdf#page=2|DG32 pp.2–4]], [[DG33.pdf#page=1|DG33 pp.1–2]]*

$$\delta:\{\text{simply connected Lie groups}\}/\!\cong\ \longrightarrow\ \{\text{finite-dimensional Lie algebras}\}/\!\cong,\qquad G\mapsto\mathrm{Lie}(G),$$
is a **bijection**. **Well defined**: $\mathrm{Lie}(G)\cong T_eG$ is finite-dimensional, and $G_1\cong G_2\Rightarrow\mathfrak g_1\cong\mathfrak g_2$ by functoriality ($(\beta\circ\alpha)_*=\beta_*\alpha_*$, $(\mathrm{id})_*=\mathrm{id}$). Simple connectivity is essential: $\mathrm{Lie}(\mathbb R)\cong\mathrm{Lie}(S^1)\cong\mathbb R$ but $\mathbb R\not\cong S^1$.

> [!key] Theorem 20.19 — homomorphisms integrate
> $G$ simply connected, $H$ any Lie group, $\varphi:\mathfrak g\to\mathfrak h$ a Lie algebra homomorphism. Then there is a **unique** Lie group homomorphism $\Phi:G\to H$ with $\Phi_*=\varphi$.
> *Proof (the lecture's, via 20.16).* Elements of $\mathfrak h$ are left-invariant, hence complete, so $\varphi:\mathfrak g\to\mathfrak h\subset\mathfrak X(H)$ is a complete $\mathfrak g$-action; $G$ simply connected gives a right action $\theta:H\times G\to H$, $(h,g)\mapsto h\cdot g$, with $\hat\theta=\varphi$. Define $\Phi(g)=e\cdot g$.
> **Homomorphism:** for $h\in H$, $X\in\mathfrak g$, $X$ and $\hat X=\varphi(X)$ are $\theta^{(h)}$-related, so $\theta^{(h)}$ maps integral curves of $X$ to those of $\hat X$: $h\cdot\exp tX$ is the integral curve of $\hat X$ from $h$. But $\hat X$ is left-invariant, so that curve is also $L_h(e\cdot\exp tX)$. With $h=\Phi(g)=e\cdot g$: $(e\cdot g)(e\cdot\exp tX)=(e\cdot g)\cdot\exp tX=e\cdot(g\exp tX)$, i.e. $\Phi(g)\Phi(\exp tX)=\Phi(g\exp tX)$. Since $\exp$ is a diffeomorphism near 0 and a neighbourhood of $e$ generates the connected $G$, every $g'=\exp X_1\cdots\exp X_n$ and induction gives $\Phi(g)\Phi(g')=\Phi(gg')$.
> **$\Phi_*=\varphi$:** $\varphi(X)_e=\hat X_e=\frac d{dt}|_0\,e\cdot\exp tX=\frac d{dt}|_0\Phi(\exp tX)=d\Phi_e(X_e)$. **Uniqueness** (HW): $\Phi(\exp X)=\exp(\Phi_*X)$ and $\exp$ of a neighbourhood generates $G$. (An alternative proof by the graph of $\varphi$ is in [[DM15 Closed Subgroups and the Lie Correspondence]] §2.)

- **Corollary 20.20 ($\delta$ injective):** if $G$, $H$ are simply connected and $\mathfrak g\cong\mathfrak h$ via $\varphi$, integrate $\varphi$ and $\varphi^{-1}$ to $\Phi$, $\Psi$; $(\Psi\circ\Phi)_*=\mathrm{id}_{\mathfrak g}=(I_G)_*$, so by uniqueness $\Psi\circ\Phi=I_G$, likewise $\Phi\circ\Psi=I_H$.
- **$\delta$ surjective** ([[DG33.pdf#page=2|DG33 p.2]]): by **Ado's theorem**, $\mathfrak g$ is isomorphic to a subalgebra $\mathfrak g_0\subseteq\mathfrak{gl}(n,\mathbb R)$; take the connected Lie subgroup $G_0\le GL(n,\mathbb R)$ with $\mathrm{Lie}(G_0)=\mathfrak g_0$ (§1) and its universal cover $p:G\to G_0$; $dp_e$ is an isomorphism ($p$ a local diffeomorphism), so $\mathrm{Lie}(G)\cong\mathfrak g_0\cong\mathfrak g$.
- **Thm 21.26:** if $K\le G$ is a **closed normal** subgroup, $G/K$ is a Lie group. **Thm 21.32:** if $G_0$ is the simply connected group with Lie algebra $\mathfrak g$, then a connected $G$ has $\mathrm{Lie}(G)\cong\mathfrak g$ **iff $G\cong G_0/\Gamma$ for a discrete normal subgroup $\Gamma$** (all connected groups with a given Lie algebra are quotients of one simply connected group).

## 5. Ideals, kernels and the adjoint representation
<span class="scope-taught">taught</span> *[[DG33.pdf#page=3|DG33 pp.3–4]], [[DG34.pdf#page=2|DG34 p.2]]*

**Ideals.** $\mathfrak h\subseteq\mathfrak g$ is an **ideal** if it is a subspace and $[X,Y]\in\mathfrak h$ for all $X\in\mathfrak g$, $Y\in\mathfrak h$. Kernels of Lie algebra homomorphisms are ideals ($\varphi[X,Y]=[\varphi X,0]=0$) — "just as normal subgroups are kernels of Lie group homomorphisms".

**The adjoint representations.**
1. $C_g:G\to G$, $C_g(h)=ghg^{-1}$: a Lie group homomorphism.
2. $\mathrm{Ad}(g)=(C_g)_*:\mathfrak g\to\mathfrak g$, a Lie algebra automorphism. **Prop 20.24:** $\mathrm{Ad}:G\to GL(\mathfrak g)$ is a **Lie group homomorphism** (the **adjoint representation of $G$**): $C_{g_1g_2}=C_{g_1}\circ C_{g_2}\Rightarrow\mathrm{Ad}(g_1g_2)=\mathrm{Ad}(g_1)\mathrm{Ad}(g_2)$, $\mathrm{Ad}(e)=\mathrm{Id}$; smoothness later.
3. $\mathrm{ad}:\mathfrak g\to\mathfrak{gl}(\mathfrak g)$, $\mathrm{ad}(X)Y=[X,Y]$, a Lie algebra homomorphism (the Jacobi identity; HW11 Q2): the **adjoint representation of $\mathfrak g$**.

> [!key] Theorem 20.27 — $\mathrm{Ad}_*=\mathrm{ad}$
> $(\mathrm{Ad}_*X)(Y)_e=\frac d{dt}|_0\big(\mathrm{Ad}(\exp tX)Y\big)_e$. Since $\mathrm{Ad}(g)=(C_g)_*=(R_{g^{-1}}\circ L_g)_*$ and $Y$ is left-invariant, $(\mathrm{Ad}(\exp tX)Y)_e=d(R_{\exp(-tX)})(Y_{\exp tX})$. The flow of $X$ is $\theta_t(g)=g\exp tX=R_{\exp tX}(g)$, so this is $d(\theta_{-t})(Y_{\theta_t(e)})$, whose $t$-derivative at 0 is the **Lie derivative** $(\mathcal L_XY)_e=[X,Y]_e$ ([[DM13 Lie Derivatives and Commuting Vector Fields]]). Hence $\mathrm{Ad}_*X=\mathrm{ad}X$.

Combined with naturality of $\exp$ for homomorphisms ([[DM14 One-Parameter Subgroups and the Exponential Map]]): $\exp(\mathrm{Ad}(g)Y)=C_g(\exp Y)$ and $\mathrm{Ad}(\exp X)=e^{\mathrm{ad}X}=\sum_k\frac1{k!}(\mathrm{ad}X)^k$.

## 6. Normal subgroups ⟺ ideals
<span class="scope-taught">taught</span> *[[DG34.pdf#page=1|DG34 pp.1–3]]*

> [!key] Lemma 20.23
> $G$ connected, $H\le G$ a connected Lie subgroup, $\mathfrak g,\mathfrak h$ their Lie algebras. $H$ is normal $\iff$ $(\ast)$ $\exp(X)\exp(Y)\exp(-X)\in H$ for all $X\in\mathfrak g$, $Y\in\mathfrak h$.
> *Proof.* ⇒: $\exp(-X)=\exp(X)^{-1}$ and normality. ⇐: choose $0\in V\subseteq\mathfrak g$ and $e\in U\subseteq G$ with $\exp:V\to U$ and $\exp:V\cap\mathfrak h\to U\cap H$ diffeomorphisms and $V=-V$. By $(\ast)$, $ghg^{-1}\in H$ for $g\in U$, $h\in U\cap H$. Any $h\in H$ is a product $h_1\cdots h_m$ of elements of $U\cap H$ ($H$ connected), so $ghg^{-1}=\prod(gh_ig^{-1})\in H$ for $g\in U$; any $g\in G$ is $g_1\cdots g_k$ with $g_i\in U$, and induction on $k$ finishes.

> [!key] Theorem 20.28
> $G$ connected, $H\le G$ a connected Lie subgroup: **$H$ is normal in $G$ ⟺ $\mathrm{Lie}(H)$ is an ideal in $\mathrm{Lie}(G)$.**
> *Proof.* From the commuting squares $\exp\circ\mathrm{Ad}(g)=C_g\circ\exp$ and $\mathrm{Ad}\circ\exp=e^{\mathrm{ad}}$: for $g=\exp X$, (1) $\exp(\mathrm{Ad}(\exp X)Y)=\exp X\exp Y\exp(-X)$ and (2) $\mathrm{Ad}(\exp X)Y=\sum\frac1{k!}(\mathrm{ad}X)^kY$.
> ⇐ $\mathfrak h$ an ideal: $(\mathrm{ad}X)Y\in\mathfrak h$, by induction $(\mathrm{ad}X)^kY\in\mathfrak h$, so $\mathrm{Ad}(\exp X)Y\in\mathfrak h$ ($\mathfrak h$ closed), and by (1) $\exp X\exp Y\exp(-X)\in\exp(\mathfrak h)\subseteq H$; Lemma 20.23 gives normality.
> ⇒ $H$ normal: $\exp(\mathrm{Ad}(\exp tX)sY)=\exp tX\exp sY\exp(-tX)\in H$ for all $s$; linearity of $\mathrm{Ad}(\exp tX)$ gives $\exp(s\,\mathrm{Ad}(\exp tX)Y)\in H$ for all $s$, so $\mathrm{Ad}(\exp tX)Y\in\mathfrak h$ (§1's characterisation), and differentiating at $t=0$ (as in Thm 20.27): $[X,Y]\in\mathfrak h$.

> [!example] Applications in DG34 pp.4–5
> **(a) Commuting exponentials:** $[X,Y]=0\iff\exp tX\exp sY=\exp sY\exp tX$ for all $s,t$. ⇒: $\mathrm{ad}(tX)(sY)=0$ so $\mathrm{Ad}(\exp tX)sY=sY$, then (1). ⇐: (1) gives $\exp(s\,\mathrm{Ad}(\exp tX)Y)=\exp(sY)$; $\frac d{ds}|_0$: $\mathrm{Ad}(\exp tX)Y=Y$; $\frac d{dt}|_0$: $[X,Y]=0$.
> **(b) $G$ (connected) is abelian ⟺ $\mathfrak g$ is abelian.** ⇒ by (a) (or: inversion $i$ is a homomorphism, so $i_*[X,Y]=[i_*X,i_*Y]$ gives $-[X,Y]=[X,Y]$). ⇐: $\mathrm{ad}=\mathrm{Ad}_*=0$, so $\mathrm{Ad}$ is the constant map $I$ (a homomorphism is determined by its differential), so $(C_g)_*=\mathrm{Id}$, so $C_g=\mathrm{Id}_G$, i.e. $gh=hg$.

> [!example] $\exp$ need not be onto (DG34 p.1, a question)
> (a) If $A=e^B$ with $B\in\mathfrak{sl}(n,\mathbb R)$ then $C=e^{B/2}\in SL(n,\mathbb R)$ with $C^2=A$ ($\mathfrak{sl}(n,\mathbb R)=\ker d(\det)_I=\{\mathrm{tr}=0\}$, and $B/2\in\mathfrak{sl}$). (b) $A=\mathrm{diag}(-\tfrac12,-2)\in SL(2,\mathbb R)$ has no real square root in $SL(2,\mathbb R)$: a real $C$ with $C^2=A$ would have eigenvalues $\pm i/\sqrt2$, $\pm\sqrt2 i$; a real $2\times2$ matrix has conjugate-pair eigenvalues, so they would be $\{i/\sqrt2,-i/\sqrt2\}$ (giving $C^2=-\tfrac12I\ne A$) or $\{\sqrt2i,-\sqrt2i\}$ (giving $-2I$) — no choice works; the notes argue via $\det C$. So $A\notin\exp(\mathfrak{sl}(2,\mathbb R))$, although $SL(2,\mathbb R)$ is connected.

## 7. Homework 11, outlined
<span class="scope-extra-beyond">extra · beyond</span> *[[HW11.pdf]] (questions); solutions mine*

> [!example]- HW11 Q1–Q6
> 1. **$X$ and $\hat\theta(X)$ are $\theta^{(p)}$-related**: §2 (Thm 20.15's first step).
> 2. **ad is a representation**: $\mathrm{ad}[X,Y]Z=[[X,Y],Z]=[X,[Y,Z]]-[Y,[X,Z]]=[\mathrm{ad}X,\mathrm{ad}Y]Z$ by Jacobi; linearity is bilinearity of the bracket.
> 3. **$\det e^A=e^{\mathrm{tr}A}$**: $f(t)=\det e^{tA}$ is a homomorphism $\mathbb R\to\mathbb R^\times_{>0}$, $f'(t)=f(t)\,d(\det)_I(A)=f(t)\,\mathrm{tr}A$, $f(0)=1$, so $f(t)=e^{t\,\mathrm{tr}A}$ (or triangularise over $\mathbb C$: eigenvalues $\lambda_i$ of $A$ give $e^{\lambda_i}$ for $e^A$).
> 4. **Right translation's generator is the inclusion**: for $\theta(g,h)=gh$, $\hat X_g=\frac d{dt}|_0\,g\exp tX=d(L_g)_e(X_e)=X_g$ ($X$ left-invariant): $\hat\theta(X)=X$.
> 5. **$\ker\mathrm{Ad}=Z(G)$** ($G$ connected): $g\in Z(G)\Rightarrow C_g=\mathrm{Id}\Rightarrow\mathrm{Ad}(g)=\mathrm{Id}$. Conversely $\mathrm{Ad}(g)=\mathrm{Id}\Rightarrow C_g(\exp X)=\exp(\mathrm{Ad}(g)X)=\exp X$ for all $X$; $\exp(\mathfrak g)$ generates $G$, so $C_g=\mathrm{Id}$.
> 6. **$\mathrm{Lie}(Z(G))=\mathfrak z(\mathfrak g)$**: $Z(G)=\ker\mathrm{Ad}$ is a closed (normal) subgroup, so (Closed Subgroup Theorem) a Lie subgroup with Lie algebra $\ker(\mathrm{Ad}_*)=\ker\mathrm{ad}=\{X:[X,Y]=0\ \forall Y\}=\mathfrak z(\mathfrak g)$ ([[DM15 Closed Subgroups and the Lie Correspondence]] §1).

## 8. The mid-semester exam (24 Sep 2026), outlined
<span class="scope-extra-beyond">extra · beyond</span> *[[Midsem.pdf]] (questions); the instructor's handwritten solutions: [[DG Midsem Solutions .pdf]] (not transcribed); outlines mine*

> [!example]- Q1–Q6 (40 marks)
> 1. (4) Definitions: a **tangent vector** at $p$ is a derivation $v:C^\infty(M)\to\mathbb R$ at $p$ ($v(fg)=f(p)vg+g(p)vf$) ([[DM03 Tangent Vectors and the Differential]]); a **partition of unity subordinate to $\{U_\alpha\}$** is a family of smooth $\psi_\alpha:M\to[0,1]$ with $\mathrm{supp}\,\psi_\alpha\subseteq U_\alpha$, locally finite supports, $\sum\psi_\alpha\equiv1$ ([[DM02 Smooth Maps and Partitions of Unity]]).
> 2. (7) Stereographic atlas $\mathcal A_S$ on $S^2$ (projections from $N$ and $S$); any atlas $\mathcal A_R$ on $\mathbb R$ (e.g. the identity). $f(x,y,z)=z$ at $(0,1,0)$: in the chart from $N$, $(u,v)=\frac{(x,y)}{1-z}$, $z=\frac{u^2+v^2-1}{u^2+v^2+1}$; the point is $(u,v)=(0,1)$ and $\hat f=z(u,v)$ has $\partial_u\hat f=0$, $\partial_v\hat f=\frac{4v}{(u^2+v^2+1)^2}=1$: Jacobian $(0\ \ 1)$. From $S$, $(u,v)=\frac{(x,y)}{1+z}$ and $z=\frac{1-u^2-v^2}{1+u^2+v^2}$: at $(0,1)$, $\partial_v\hat f=\frac{-4v}{(1+u^2+v^2)^2}=-1$, Jacobian $(0\ \ {-1})$ (the two charts' orientations differ). In $\mathcal A_R$ with the identity chart the target coordinate is $z$ itself.
> 3. (7) A **compact immersed** submanifold is embedded: an injective immersion from a compact space is a topological embedding (a continuous bijection from compact to Hausdorff is a homeomorphism onto its image) ([[DM05 Immersions, Embeddings, Submersions and Coverings]]).
> 4. (7) **Equivariant rank theorem**: $F\circ\theta_g=\theta'_g\circ F$ gives $dF_{g\cdot p}\circ d(\theta_g)_p=d(\theta'_g)_{F(p)}\circ dF_p$ with the $d\theta$'s isomorphisms, so $\mathrm{rank}\,dF$ is constant on orbits; transitivity makes it constant ([[DM09 Group Actions and Semidirect Products]]).
> 5. (7) Homomorphisms agreeing on an open set agree: $F_1(g)=F_2(g)$ on open $W$; then on $W^{-1}W$, a neighbourhood of $e$ ($F_i$ homomorphisms); a neighbourhood of $e$ generates the connected $G$ ([[DM08 Lie Groups]]).
> 6. (8) Non-abelian 2-dimensional $\mathfrak g$: (a) $[X,Y]=[aV_1+bV_2,cV_1+dV_2]=(ad-bc)[V_1,V_2]$. (b) $[V_1,V_2]=W_2\ne0$; extend to a basis $(W_1,W_2)$ and rescale $W_1$ so that $[W_1,W_2]=W_2$ (possible since $[W_1,W_2]=\lambda W_2$ with $\lambda\ne0$ by (a)). (c) Any two such algebras have bases with $[W_1,W_2]=W_2$; matching bases is an isomorphism (e.g. $\mathfrak{aff}(1)$, the Lie algebra of $\mathrm{Aff}(1)$: [[DM17 Foliations, Weakly Embedded Submanifolds and Lie Subgroups]]).

## Map of this chapter
> [!connection] How DM18 connects
> **Builds on:** [[DM15 Closed Subgroups and the Lie Correspondence]] (the correspondence by graphs), [[DM17 Foliations, Weakly Embedded Submanifolds and Lie Subgroups]] (subalgebras → subgroups), [[DM14 One-Parameter Subgroups and the Exponential Map]], [[DM13 Lie Derivatives and Commuting Vector Fields]], [[DM12 Integral Curves, Flows and Flowouts]], [[DM09 Group Actions and Semidirect Products]], [[PA15 Covering Spaces and the Fundamental Group]].
> **Other subjects:** [[Group Theory - Course Map]] (normal subgroups, centres, quotients) · [[QM09 The Stern-Gerlach Experiment and Spin]] ($SU(2)$, simply connected, covers $SO(3)$ — Thm 21.32's $G_0/\Gamma$ with $\Gamma=\{\pm1\}$) · [[QM12 The Hydrogen Atom]] (angular momentum: the adjoint action of rotations).

## Summary
> [!summary] Cheat-sheet
> - Right action $\theta$: $\hat X_p=\frac d{dt}|_0p\exp tX$; $X\sim_{\theta^{(p)}}\hat X$; $\hat\theta$ a Lie algebra hom (20.15). Complete $\mathfrak g$-action + $G$ simply connected ⇒ unique $G$-action (20.16; proof not examinable).
> - Lie correspondence: s.c. Lie groups ↔ f.d. Lie algebras (20.19 integrate homs, 20.20 injective, Ado surjective); connected $G$ with algebra $\mathfrak g$ = $\tilde G/\Gamma$, $\Gamma$ discrete normal (21.32); $G/K$ Lie for closed normal $K$ (21.26).
> - $C_g$, $\mathrm{Ad}(g)=(C_g)_*$, $\mathrm{Ad}:G\to GL(\mathfrak g)$ hom (20.24), $\mathrm{ad}X=[X,\cdot]$, $\mathrm{Ad}_*=\mathrm{ad}$ (20.27), $\mathrm{Ad}(\exp X)=e^{\mathrm{ad}X}$, $\exp(\mathrm{Ad}(g)Y)=g\exp Yg^{-1}$.
> - Normal ⟺ ideal (20.28 via 20.23); $[X,Y]=0\iff$ exponentials commute; $G$ abelian ⟺ $\mathfrak g$ abelian; $\ker\mathrm{Ad}=Z(G)$, $\mathrm{Lie}(Z(G))=\mathfrak z(\mathfrak g)$; $\exp$ not onto $SL(2,\mathbb R)$.

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (2): the other tool's concept notes from the lectures, unreviewed
> [[zettel/compact-immersed-submanifold-embedding-theorem|Compact Immersed Submanifold Embedding Theorem]] · [[zettel/identity-of-connected-lie-group-homomorphisms|Identity of Connected Lie Group Homomorphisms]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | Thm 19.26 recap, flows as $\mathbb R$-actions, infinitesimal generators, Thm 20.15, $\mathfrak g$-actions, Thm 20.16 | [[DG31.pdf]] pp.1–4 (handwritten, read as images) | taught |
> | simply connected, universal cover, Lie correspondence, Thm 20.19 proof, Cor 20.20 | [[DG32.pdf]] pp.1–4 | taught |
> | correspondence outline, surjectivity via Ado, Thms 21.26, 21.32, ideals, Thm 20.28 statement, Ad/ad | [[DG33.pdf]] pp.1–4 | taught |
> | ideals and normal subgroups, $\exp$ not onto, Lemma 20.23, Ad rep, Thm 20.28 proof, abelian criteria | [[DG34.pdf]] pp.1–5 | taught |
> | HW11 questions | [[HW11.pdf]] | taught (homework; solutions mine) |
> | midsem questions | [[Midsem.pdf]]; instructor's solutions [[DG Midsem Solutions .pdf]] linked, **not read** (handwritten; text layer unusable) | taught (exam; outlines mine) |
> | exam scope, Thm 20.16 proof excluded, dates | Classroom announcements 16 and 18 Nov 2026 (`math/differential-geometry/classroom-sources.json`) | taught |
>
> **Notes.** Kept lean on request (audited course). Lee's book (in `books/`) was **not** re-read for this chapter; theorem numbers follow the notes. The DM17 `[!verify]` items about illegible parts of DG28/DG30 can now be checked against the PDFs (`math/differential-geometry/lecture-notes-slides/DG27.pdf`–`DG30.pdf`); not done here.
