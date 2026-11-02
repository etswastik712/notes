"""Concept notes for DM15 (Closed Subgroups and the Lie Correspondence).  .venv/bin/python -W ignore scripts/spec_dm15.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "DM15 Closed Subgroups and the Lie Correspondence"
MT = "mt3184-differential-geometry-and-lie-groups"
T, EB = "taught", "extra-book"
BY = ["lecture-notes", "book"]

ITEMS = [
    dict(title="Closed Subgroup Theorem", aliases=["Cartan's theorem", "Theorem 20.12", "closed subgroups are embedded", "Corollary 20.13"], scope=[T, EB], by=BY,
         syl={T: f"slide DG14 via [[{MT}/2026-09-10-september-7-12|Sep 7–12 note]]; HW9 Q6.", EB: f"[[{LEE}#page=541|Lee Thm 20.12, p. 523]], [[{LEE}#page=543|Lee Cor. 20.13, p. 525]]."},
         intuition="Topology forces smoothness: a subgroup that is merely a closed set is automatically cut out by a linear subspace of $\\mathfrak g$ near $e$.",
         key="$H\\le G$: closed $\\iff$ embedded submanifold $\\iff$ embedded Lie subgroup. Proof of (closed $\\Rightarrow$ embedded): $\\mathfrak h=\\{X:\\exp tX\\in H\\ \\forall t\\}$ is a subspace by the **Trotter formula**; $\\exp(U\\cap\\mathfrak h)=\\exp U\\cap H$ for small $U$ (sequence argument with $\\Phi=\\exp X\\exp Y$); left translates give slice charts; $\\mathrm{Lie}(H)=\\mathfrak h$. (Embedded $\\Rightarrow$ closed: slice chart + $W^{-1}W\\subseteq V$.)",
         body="Closed: $SL(n)$, $O(n)$, $U(n)$, centres, $\\mathbb Z\\subset\\mathbb R$, the circle $\\{(2t,3t)\\}\\subset T^2$. Not closed: $\\mathbb Q\\subset\\mathbb R$, the dense line in $T^2$. HW9 Q6: the closure of any Lie subgroup is an embedded Lie subgroup, so a Lie subgroup is embedded or dense in an embedded one.",
         used=[CH, "DM08 Lie Groups"], related=["Lie Subgroup", "Trotter Product Formula", "Exponential Map", "Embedded Submanifold"]),
    dict(title="Lie Correspondence", aliases=["Theorem 20.21", "Lie's third theorem", "Lie's fundamental theorems", "simply connected Lie groups and Lie algebras"], scope=[T, EB], by=BY,
         syl={T: f"slides DG17–DG20 via [[{MT}/2026-09-15-september-14-18|Sep 14–18]] and [[{MT}/2026-10-10-october-5-9|Oct 5–9]] notes.", EB: f"[[{LEE}#page=549|Lee Thm 20.21, p. 531]], [[{LEE}#page=550|Lee Thm 20.22, p. 532]]."},
         intuition="Up to topology, groups and algebras are the same thing: the Lie algebra remembers the group exactly when the group is simply connected.",
         key="$G\\mapsto\\mathrm{Lie}(G)$ is a **bijection** between isomorphism classes of simply connected Lie groups and finite-dimensional real Lie algebras. Injective: [[Homomorphism Theorem for Lie Groups]]. Surjective (**Lie's third theorem**): Ado $\\Rightarrow\\mathfrak g\\subseteq\\mathfrak{gl}(n)$, Thm 19.26 gives a connected subgroup, take the universal cover. All connected groups with algebra $\\mathfrak g$: $\\tilde G/\\Gamma$, $\\Gamma$ discrete central (Thm 21.32).",
         body="$\\mathbb R^n$ and $T^n$ share an abelian algebra; $SU(2)=S^3$ and $SO(3)=SU(2)/\\{\\pm I\\}$ share $\\mathfrak{su}(2)\\cong\\mathfrak{so}(3)\\cong(\\mathbb R^3,\\times)$; $\\mathrm{Aff}(1)^+\\cong\\mathbb R^2$ has $\\mathfrak{aff}(1)$; Heisenberg group $\\cong\\mathbb R^3$. Local versions are Lie's fundamental theorems.",
         used=[CH], related=["Homomorphism Theorem for Lie Groups", "Universal Covering Group", "Lie Algebra of a Lie Group", "Lie Algebra Representation"]),
    dict(title="Homomorphism Theorem for Lie Groups", aliases=["Theorem 20.19", "Corollary 20.20", "integrating Lie algebra homomorphisms", "Homomorphism Theorem"], scope=[T, EB], by=BY,
         syl={T: f"slide DG18 via [[{MT}/2026-09-15-september-14-18|Sep 14–18 note]].", EB: f"[[{LEE}#page=548|Lee Thm 20.19, p. 530]], [[{LEE}#page=549|Lee Cor. 20.20, p. 531]]."},
         intuition="On a simply connected group every Lie algebra homomorphism integrates to a unique group homomorphism.",
         key="$G$ simply connected, $\\varphi:\\mathfrak g\\to\\mathfrak h$ a Lie algebra homomorphism $\\Rightarrow$ $\\exists!\\ \\Phi:G\\to H$ with $\\Phi_*=\\varphi$. Proof via the graph $\\{(X,\\varphi X)\\}$, a subalgebra of $\\mathfrak g\\oplus\\mathfrak h$: the corresponding subgroup $K\\le G\\times H$ projects by a covering $K\\to G$ which is a diffeomorphism since $G$ is simply connected; $\\Phi=\\pi_2\\pi_1^{-1}$. Uniqueness: $\\Phi(\\exp X)=\\exp\\Phi_*X$. Corollary: simply connected groups with isomorphic algebras are isomorphic.",
         body="$\\mathrm{Ad}:SU(2)\\to SO(3)$ integrates $\\tau_k\\mapsto E_k$ (kernel $\\{\\pm I\\}$); the graph of $\\tau_k\\mapsto E_k$ is a subalgebra (error $2\\times10^{-16}$). Fails without simple connectivity: $\\mathrm{id}:\\mathfrak{so}(3)\\to\\mathfrak{su}(2)$ does not integrate to $SO(3)\\to SU(2)$.",
         used=[CH], related=["Lie Correspondence", "Induced Lie Algebra Homomorphism", "Universal Covering Group", "Smooth Covering Map"]),
    dict(title="Frobenius Theorem", aliases=["involutive distribution", "integrable distribution", "integral manifold", "Theorem 19.12", "foliation", "flat chart"], scope=[EB], by=BY,
         syl={EB: f"[[{LEE}#page=515|Lee Thm 19.12, p. 497]], [[{LEE}#page=524|Lee Thms 19.25–19.26, p. 506]]."},
         intuition="A field of planes is tangent to a family of surfaces exactly when the bracket of two fields in the planes stays in the planes.",
         key="A rank-$k$ distribution $D\\subseteq TM$ is **involutive** if $[X,Y]\\in\\Gamma(D)$ for $X,Y\\in\\Gamma(D)$; **Frobenius:** involutive $\\iff$ integrable $\\iff$ locally $D=\\mathrm{span}\\{\\partial_1,\\dots,\\partial_k\\}$ in a flat chart. Necessity: Cor 8.32; sufficiency: involutive $\\Rightarrow$ locally spanned by independent commuting fields (Thm 9.46).",
         body="$\\mathrm{span}\\{\\partial_x,\\partial_y\\}$ is involutive (planes $z=$ const); $\\mathrm{span}\\{\\partial_x,\\partial_y+x\\partial_z\\}$ has $[X_1,X_2]=\\partial_z\\notin D$ (contact). Application: a Lie subalgebra $\\mathfrak h\\le\\mathfrak g$ gives a left-invariant involutive distribution whose leaf through $e$ is the connected Lie subgroup with algebra $\\mathfrak h$ (Thm 19.26).",
         used=[CH], related=["Commuting Frame", "Lie Bracket of Vector Fields", "Lie Subgroup", "Lie Correspondence"]),
    dict(title="Universal Covering Group", aliases=["universal cover of a Lie group", "simply connected cover", "G tilde"], scope=[EB], by=BY,
         syl={EB: f"[[{LEE}#page=575|Lee Thm 21.32, p. 557]]; covering theory in [[PA15 Covering Spaces and the Fundamental Group]]."},
         intuition="Unroll the group until it is simply connected; the multiplication lifts and the Lie algebra does not change.",
         key="Every connected Lie group $G$ has a simply connected cover $\\tilde G\\to G$, a Lie group homomorphism and covering map with discrete central kernel $\\Gamma\\cong\\pi_1(G)$, and $\\mathrm{Lie}(\\tilde G)=\\mathrm{Lie}(G)$. The connected groups with algebra $\\mathfrak g$ are exactly the quotients $\\tilde G/\\Gamma$ (Thm 21.32).",
         body="$\\mathbb R\\to S^1$ (kernel $\\mathbb Z$), $\\mathbb R^n\\to T^n$, $SU(2)\\to SO(3)$ (kernel $\\{\\pm I\\}$, $\\pi_1(SO(3))=\\mathbb Z/2$). The universal cover of $SL(2,\\mathbb R)$ has no faithful finite-dimensional representation: not every Lie group is a matrix group.",
         used=[CH, "DM08 Lie Groups"], related=["Smooth Covering Map", "Lie Correspondence", "Homomorphism Theorem for Lie Groups", "Lie Group"]),
]

if __name__ == "__main__":
    write("14-Differential-Geometry", "diff-geometry", ITEMS)
