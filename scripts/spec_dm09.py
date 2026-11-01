"""Concept notes for DM09 (Group Actions and Semidirect Products).  .venv/bin/python -W ignore scripts/spec_dm09.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "DM09 Group Actions and Semidirect Products"
MT = "mt3184-differential-geometry-and-lie-groups"
T, EB = "taught", "extra-book"
BY = ["lecture-notes", "book"]

ITEMS = [
    dict(title="Smooth Action", aliases=["smooth group action", "Lie group action", "left action", "transitive action", "free action"], scope=[T], by=BY,
         syl={T: f"slides DG14–DG15 via [[{MT}/2026-09-10-september-7-12|Sep 7–12 note]]."},
         intuition="A Lie group acting as a family of diffeomorphisms of a manifold, varying smoothly with the group element.",
         key="A smooth map $\\theta:G\\times M\\to M$, $(g,p)\\mapsto g\\cdot p$, with $g_1\\cdot(g_2\\cdot p)=(g_1g_2)\\cdot p$ and $e\\cdot p=p$. Each $\\theta_g$ is a diffeomorphism (inverse $\\theta_{g^{-1}}$). **Transitive:** one orbit. **Free:** all stabilisers trivial.",
         body="Examples: left translation, conjugation, $GL(n,\\mathbb R)$ on $\\mathbb R^n$ (transitive on $\\mathbb R^n\\setminus\\{0\\}$), $SO(3)$ on $S^2$, congruence $A\\cdot X=AXA^T$ on $M(n,\\mathbb R)$, the irrational flow of $\\mathbb R$ on $T^2$ (free, dense orbits). The finite-group version is [[Group Action]].",
         used=[CH, "DM12 Integral Curves, Flows and Flowouts"], related=["Orbit Map and Stabiliser", "Equivariant Map", "Homogeneous Space", "Lie Group"]),
    dict(title="Orbit Map and Stabiliser", aliases=["orbit map", "stabiliser", "stabilizer", "isotropy group", "orbit", "isotropy subgroup"], scope=[T], by=BY,
         syl={T: f"slides DG15–DG16 via [[{MT}/2026-09-10-september-7-12|Sep 7–12 note]]; HW6 Q1."},
         intuition="Push one point around with the whole group (the orbit map) and record which group elements leave it fixed (the stabiliser).",
         key="$\\theta^{(p)}(g)=g\\cdot p$ is smooth and equivariant for left translation, so has **constant rank** (Thm 7.25). Hence $G_p=(\\theta^{(p)})^{-1}(p)$ is a properly embedded Lie subgroup of dimension $\\dim G-\\operatorname{rank}d\\theta^{(p)}_e$ (HW6 Q1; [[" + LEE + "#page=184|Lee Prop. 7.26, p. 166]]); $G_{g\\cdot p}=gG_pg^{-1}$; free $\\Rightarrow$ orbit is an immersed submanifold.",
         body="$O(n)$ = stabiliser of $I$ under congruence ($\\dim n^2-n(n+1)/2$), $U(n)$ = stabiliser of $I$ under $AXA^*$ ($\\dim n^2$), $SO(2)$ = stabiliser of $e_3$ in $SO(3)$ acting on $S^2$. Finite case: [[Orbit-Stabiliser Theorem]]. An orbit is immersed, not necessarily embedded: the irrational flow on $T^2$.",
         used=[CH], related=["Smooth Action", "Equivariant Rank Theorem", "Orthogonal Group", "Unitary Group", "Homogeneous Space"]),
    dict(title="Equivariant Map", aliases=["equivariant", "G-equivariant map", "intertwining map"], scope=[T], by=BY,
         syl={T: f"slide DG15 via [[{MT}/2026-09-10-september-7-12|Sep 7–12 note]]."},
         intuition="A map that commutes with the group action: moving first and then mapping equals mapping first and then moving.",
         key="$F:M\\to N$ smooth with $F(g\\cdot p)=g\\cdot F(p)$, i.e. $F\\circ\\theta_g=\\varphi_g\\circ F$. Examples: a homomorphism $F:G\\to H$ (left multiplication on $G$, $g\\cdot h=F(g)h$ on $H$), every orbit map, the radial projection $\\mathbb R^n\\setminus\\{0\\}\\to S^{n-1}$ for $O(n)$.",
         body="With a transitive action on the source, an equivariant map has constant rank ([[Equivariant Rank Theorem]]). On Lie algebras the analogue is the induced map $F_*$ ([[DM11 The Lie Algebra of a Lie Group]]).",
         used=[CH], related=["Smooth Action", "Equivariant Rank Theorem", "Lie Group Homomorphism"]),
    dict(title="Equivariant Rank Theorem", aliases=["Theorem 7.25", "constant rank of equivariant maps"], scope=[T, EB], by=BY,
         syl={T: f"slide DG15 via [[{MT}/2026-09-10-september-7-12|Sep 7–12 note]].", EB: f"[[{LEE}#page=183|Lee Thm 7.25, p. 165]]."},
         intuition="If the group can carry any point to any other and the map respects the action, the map looks the same everywhere, so its rank is constant.",
         key="$F:M\\to N$ equivariant for a **transitive** action on $M$ and any action on $N$ $\\Rightarrow$ $F$ has constant rank. Surjective $\\Rightarrow$ submersion, injective $\\Rightarrow$ immersion, bijective $\\Rightarrow$ diffeomorphism. Proof: $d(\\varphi_g)\\circ dF_p=dF_{g\\cdot p}\\circ d(\\theta_g)_p$ with isomorphic vertical maps.",
         body="Special case $M=G$: Theorem 7.5 (homomorphisms). Applied to orbit maps: stabilisers are embedded Lie subgroups, and $O(n)$, $U(n)$ get their dimensions from one rank computation. Used in [[Homogeneous Space]] (transitive $\\Rightarrow$ surjective submersion).",
         used=[CH], related=["Equivariant Map", "Orbit Map and Stabiliser", "Lie Group Homomorphism", "Global Rank Theorem"]),
    dict(title="Semidirect Product of Lie Groups", aliases=["semidirect product", "N semidirect H", "internal semidirect product", "split exact sequence of Lie groups"], scope=[T, EB], by=BY,
         syl={T: f"slide DG16 and handout 'DG Semidirect products' via [[{MT}/2026-09-10-september-7-12|Sep 7–12 note]]; HW6 Q3.", EB: f"[[{LEE}#page=186|Lee Prop. 7.33, p. 168]], [[{LEE}#page=187|Lee Thm 7.35, p. 169]]."},
         intuition="Two groups glued with a twist: $H$ acts on $N$ by automorphisms and the product law remembers it.",
         key="$N\\rtimes_\\theta H$ is the manifold $N\\times H$ with $(n_1,h_1)(n_2,h_2)=(n_1\\theta_{h_1}(n_2),h_1h_2)$. $N=N\\times\\{e\\}$ is normal (kernel of the projection), $H=\\{e\\}\\times H$ a complement. **Criterion (HW6 Q3a):** $G\\cong N\\rtimes H$ iff $\\varphi:G\\to H$, $\\psi:H\\to G$ with $\\varphi\\psi=\\mathrm{id}$, $\\ker\\varphi\\cong N$. Internal form: Thm 7.35.",
         body="$O(n)=SO(n)\\rtimes O(1)$, $GL(n,\\mathbb C)=SL(n,\\mathbb C)\\rtimes\\mathbb C^\\times$, $E(n)=\\mathbb R^n\\rtimes O(n)$ ([[Euclidean Group]]), $\\mathrm{Aff}(1)=\\mathbb R\\rtimes\\mathbb R^\\times$. $SU(2)\\to SO(3)$ does **not** split ($S^3$ is connected, $\\{\\pm1\\}\\times SO(3)$ is not). Abstract version: [[Semidirect Product]], [[Complement of a Normal Subgroup]].",
         used=[CH], related=["Euclidean Group", "Lie Group", "Lie Group Homomorphism", "Special Linear Group", "Orthogonal Group"]),
    dict(title="Euclidean Group", aliases=["E(n)", "rigid motions", "SE(n)", "group of isometries of R^n"], scope=[EB], by=BY,
         syl={EB: f"[[{LEE}#page=186|Lee Ex. 7.32, p. 168]]."},
         intuition="All rigid motions of space: rotate/reflect, then translate.",
         key="$E(n)=\\mathbb R^n\\rtimes O(n)$ with $(b,A)(b',A')=(b+Ab',AA')$, acting on $\\mathbb R^n$ by $x\\mapsto b+Ax$; as matrices $\\begin{pmatrix}A&b\\\\0&1\\end{pmatrix}$, so $E(n)\\hookrightarrow GL(n+1,\\mathbb R)$. $\\dim E(n)=n+n(n-1)/2$; $\\mathbb R^n=E(n)/O(n)$. It preserves lines, distances and angles.",
         body="$E(2)$: matrix product agrees with the semidirect law to $10^{-16}$; not a direct product ($\\mathbb R^2\\times SO(2)$ is abelian). The Lie-algebra version in [[DM11 The Lie Algebra of a Lie Group]]. Related: [[Affine Group]].",
         used=[CH], related=["Semidirect Product of Lie Groups", "Orthogonal Group", "Homogeneous Space"]),
    dict(title="Homogeneous Space", aliases=["G/H", "coset space", "homogeneous manifold", "G-homogeneous space"], scope=[EB], by=BY,
         syl={EB: f"[[{LEE}#page=569|Lee Thm 21.17, p. 551]], [[{LEE}#page=570|Lee Thm 21.18, p. 552]]."},
         intuition="A space on which a group acts transitively, so that all points look alike; it is the group modulo the stabiliser of one point.",
         key="If $G$ acts transitively on $M$, $\\theta^{(p)}:G\\to M$ is a surjective submersion with fibres the cosets $gG_p$, and $G/G_p\\to M$ is a diffeomorphism (Lee Thm 21.18). For closed $H\\le G$, $G/H$ is a manifold of dimension $\\dim G-\\dim H$ (Thm 21.17).",
         body="$S^n=O(n+1)/O(n)$ ($n$), $S^{2n+1}=U(n+1)/U(n)$ ($2n+1$), $S^2=SU(2)/U(1)$ ($2$), $\\mathbb{RP}^n=O(n+1)/(O(n)\\times O(1))$ ($n$), $\\mathbb R^n=E(n)/O(n)$ ($n$). Full treatment in the quotient-manifold chapter of Lee (beyond MT3184).",
         used=[CH], related=["Orbit Map and Stabiliser", "Equivariant Rank Theorem", "Smooth Action", "Real Projective Space"]),
]

if __name__ == "__main__":
    write("14-Differential-Geometry", "diff-geometry", ITEMS)
