"""Concept notes for DM08 (Lie Groups).  .venv/bin/python -W ignore scripts/spec_dm08.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "DM08 Lie Groups"
MT = "mt3184-differential-geometry-and-lie-groups"
T, EB = "taught", "extra-book"
BY = ["lecture-notes", "book"]

ITEMS = [
    dict(title="Lie Group", aliases=["Lie groups", "smooth group", "topological group"], scope=[T], by=BY,
         syl={T: f"slides DG10–DG11 via [[{MT}/2026-08-27-august-24-28|Aug 24–28 note]]; HW4 Q5–Q6, HW5 Q2."},
         intuition="A group of symmetries that can be varied continuously: a manifold in which multiplication and inversion are smooth maps.",
         key="A smooth manifold $G$ with a group structure such that $m(g,h)=gh$ and $i(g)=g^{-1}$ are smooth. (Smoothness of $m$ alone suffices: $F(g,h)=(g,gh)$ is a bijective local diffeomorphism.) $dm_{(e,e)}(X,Y)=X+Y$, $di_e=-\\mathrm{id}$.",
         body="$\\mathbb R^n$, $S^1$, $T^n$, $S^3=SU(2)$, $GL(n,\\mathbb R)$, $SL$, $O(n)$, $SO(n)$, $U(n)$; not $S^2$ (not parallelizable). Every Lie group is parallelizable (left-invariant frame, [[DM11 The Lie Algebra of a Lie Group]]). Homogeneous: $L_g$ moves any point to any other ([[Left Translation]]).",
         used=[CH, "DM09 Group Actions and Semidirect Products"], related=["Left Translation", "Lie Group Homomorphism", "Lie Subgroup", "General Linear Group"]),
    dict(title="Left Translation", aliases=["right translation", "conjugation", "L_g", "R_g", "c_g"], scope=[T], by=BY,
         syl={T: f"slide DG10; [[{MT}/2026-08-27-august-24-28|Aug 24–28 note]]."},
         intuition="Shift the whole group by multiplying by a fixed element: a diffeomorphism that carries the identity to any chosen point.",
         key="$L_g(h)=gh$, $R_g(h)=hg$, $c_g(h)=ghg^{-1}$ are diffeomorphisms of $G$ ($L_g^{-1}=L_{g^{-1}}$). Hence $d(L_g)_e:T_eG\\to T_gG$ is an isomorphism and the geometry near $g$ equals that near $e$.",
         body="A vector $v\\in T_eG$ defines the left-invariant field $X_g=d(L_g)_e(v)$ ([[DM11 The Lie Algebra of a Lie Group]]). For a homomorphism $F\\circ L_g=L_{F(g)}\\circ F$ ($\\Rightarrow$ constant rank).",
         used=[CH], related=["Lie Group", "Lie Group Homomorphism", "Diffeomorphism"]),
    dict(title="Lie Group Homomorphism", aliases=["Lie group isomorphism", "constant rank of homomorphisms", "Theorem 7.5"], scope=[T], by=BY,
         syl={T: f"slide DG11 (Thm 7.5, Cor 7.6); [[{LEE}#page=171|Lee Thm 7.5, p. 153]]."},
         intuition="A smooth, structure-preserving map between groups: it looks the same at every point, so its rank is constant.",
         key="A smooth group homomorphism $F:G\\to H$. **Thm 7.5:** constant rank ($F\\circ L_g=L_{F(g)}\\circ F$). Hence bijective $\\Rightarrow$ isomorphism; $\\ker F$ is an embedded Lie subgroup of dimension $\\dim G-\\operatorname{rank}dF$; an injective $F$ has image a Lie subgroup.",
         body="$\\det:GL(n)\\to\\mathbb R^\\times$ (rank 1, kernel $SL(n)$); $\\mathbb R\\to S^1$ (kernel $\\mathbb Z$); $\\exp:\\mathbb R\\cong\\mathbb R_{>0}$; $\\mathbb R\\to T^2$ (dense, rank 1); $SU(2)\\to SO(3)$ (rank 3, kernel $\\pm1$). The induced map on Lie algebras: [[DM11 The Lie Algebra of a Lie Group]].",
         used=[CH], related=["Global Rank Theorem", "Lie Subgroup", "Left Translation"]),
    dict(title="Lie Subgroup", aliases=["embedded Lie subgroup", "closed subgroup", "immersed subgroup"], scope=[T, EB], by=BY,
         syl={T: f"slides DG12–DG14 via [[{MT}/2026-09-03-august-31-september-4|Aug 31–Sep 4 note]].", EB: f"[[{LEE}#page=177|Lee Thm 7.21, p. 159]]."},
         intuition="A subgroup that is itself a Lie group, sitting in $G$ as an immersed (possibly dense) or embedded submanifold.",
         key="A subgroup $H\\le G$ with a topology and smooth structure making it a Lie group and an immersed submanifold. Kernels of homomorphisms and images of injective homomorphisms are Lie subgroups. A Lie subgroup is closed iff embedded; **Closed Subgroup Theorem:** closed subgroups are embedded Lie subgroups ([[DM15 Closed Subgroups and the Lie Correspondence]]).",
         body="The dense line on $T^2$ is a Lie subgroup that is not closed. $SL(n)$, $O(n)$, $U(n)$, $SO(n)$ are embedded. An open subgroup is closed.",
         used=[CH], related=["Immersed Submanifold", "Embedded Submanifold", "Identity Component"]),
    dict(title="Identity Component", aliases=["G_0", "connected component of the identity", "components of a Lie group"], scope=[T], by=BY,
         syl={T: f"slide DG13 (Prop 7.15) via [[{MT}/2026-09-03-august-31-september-4|Aug 31–Sep 4 note]]; [[{LEE}#page=175|Lee Prop. 7.15, p. 157]]."},
         intuition="The part of the group reachable from the identity by a continuous path; every other component is a translate of it.",
         key="$G_0$ is a **normal, open, connected subgroup**, the only connected open subgroup; the components of $G$ are the cosets $gG_0$. For $W$ a symmetric neighbourhood of $e$: $\\langle W\\rangle$ is open if $W$ is open, connected if $W$ is connected, $=G$ if $G$ is connected. Open subgroups are closed.",
         body="$GL(n,\\mathbb R)_0=\\{\\det>0\\}$ (49.9% of random $3\\times3$ matrices), $O(n)_0=SO(n)$ (two components, $\\det=\\pm1$), $\\mathbb R^\\times_0=(0,\\infty)$. $G/G_0$ is discrete.",
         used=[CH], related=["Lie Group", "Orthogonal Group", "General Linear Group"]),
    dict(title="General Linear Group", aliases=["GL(n)", "GL(n,R)", "GL(n,C)"], scope=[T], by=BY,
         syl={T: f"slides DG10–DG11 (examples); HW4–HW6."},
         intuition="All invertible linear maps of $\\mathbb R^n$ (or $\\mathbb C^n$): the largest matrix group, from which the classical groups are cut out.",
         key="$GL(n,\\mathbb R)=\\{\\det\\ne0\\}$, an open subset of $M(n,\\mathbb R)\\cong\\mathbb R^{n^2}$, so an $n^2$-manifold; multiplication is polynomial, inversion $\\operatorname{adj}A/\\det A$ is smooth. $\\dim_{\\mathbb R}GL(n,\\mathbb C)=2n^2$. Two components for $\\mathbb R$ ($\\det\\gtrless0$), connected for $\\mathbb C$. $T_IGL(n)=M(n,\\mathbb R)$ with $[A,B]=AB-BA$ ([[DM11 The Lie Algebra of a Lie Group]]).",
         body="Subgroups: $SL(n)=\\ker\\det$, $O(n)$, $SO(n)$, $U(n)$, $SU(n)$ ([[Special Linear Group]], [[Orthogonal Group]], [[Unitary Group]]). $GL(n,\\mathbb C)\\cong SL(n,\\mathbb C)\\rtimes\\mathbb C^\\times$ (HW6 Q3c).",
         used=[CH], related=["Special Linear Group", "Orthogonal Group", "Lie Group"]),
    dict(title="Unitary Group", aliases=["U(n)", "SU(n)", "SU(2)", "unitary matrices"], scope=[T], by=BY,
         syl={T: f"[[{MT}/2026-09-11-hw6|HW6]] Q2 ($U(n)$ is an embedded $n^2$-dimensional Lie subgroup of $GL(n,\\mathbb C)$)."},
         intuition="Complex rotations: matrices preserving the Hermitian inner product; the symmetry group of quantum states.",
         key="$U(n)=\\{A\\in GL(n,\\mathbb C):A^*A=I\\}$, the stabiliser of $I$ under $A\\cdot X=AXA^*$ (orbit map to Hermitian matrices, dimension $n^2$), an embedded Lie subgroup of dimension $n^2$; $T_IU(n)=\\{B+B^*=0\\}$. $SU(n)=\\ker(\\det:U(n)\\to U(1))$, $\\dim n^2-1$. $SU(2)\\cong S^3$ and $SU(2)\\to SO(3)$ is a 2-sheeted covering homomorphism.",
         body="Spin-½ and the Stern–Gerlach experiment: [[QM09 The Stern-Gerlach Experiment and Spin]]; fundamental group of $SO(3)$: [[PA15 Covering Spaces and the Fundamental Group]].",
         used=[CH], related=["Orthogonal Group", "General Linear Group", "Lie Group"]),
]

if __name__ == "__main__":
    write("14-Differential-Geometry", "diff-geometry", ITEMS)
