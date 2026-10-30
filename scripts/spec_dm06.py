"""Concept notes for DM06 (Submanifolds).  .venv/bin/python -W ignore scripts/spec_dm06.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "DM06 Submanifolds"
MT = "mt3184-differential-geometry-and-lie-groups"
T, EB = "taught", "extra-book"
BY = ["lecture-notes", "book"]

ITEMS = [
    dict(title="Embedded Submanifold", aliases=["submanifold", "regular submanifold", "embedded submanifold"], scope=[T, EB], by=BY,
         syl={T: f"slide DG8 (submanifolds and tangent spaces) via [[{MT}/2026-08-20-august-17-21|Aug 17–21 note]]; HW5 Q1.", EB: f"[[{LEE}#page=117|Lee Props. 5.1–5.7, pp. 99–101]]."},
         intuition="A subset that is a manifold in its own right with the inherited topology, sitting inside the big manifold like a flat coordinate plane in suitable coordinates.",
         key="$S\\subseteq M$ with the subspace topology and a smooth structure making $\\iota:S\\hookrightarrow M$ a smooth embedding. Equivalent: slice charts around every point ([[Slice Chart]]). Examples: open subsets, graphs, slices $M\\times\\{q\\}$, regular level sets, images of embeddings, spheres, $O(n)$, $SL(n)$.",
         body="Maps into $S$ that are smooth into $M$ are smooth into $S$ (Cor. 5.30); the smooth structure of $S$ is unique (Thm 5.31). Non-examples: figure-eight, cross. Looser notion: [[Immersed Submanifold]].",
         used=[CH], related=["Slice Chart", "Regular Level Set Theorem", "Immersed Submanifold", "Smooth Embedding"]),
    dict(title="Slice Chart", aliases=["slice", "local slice criterion", "k-slice"], scope=[T, EB], by=BY,
         syl={T: f"slide DG8 (proof of injectivity of $di_p$ uses a slice chart).", EB: f"[[{LEE}#page=119|Lee Thm 5.8 (Local Slice Criterion), p. 101]]."},
         intuition="Coordinates on $M$ in which the submanifold becomes a flat coordinate plane.",
         key="A chart $(U,\\varphi)$ of $M^n$ with $\\varphi(S\\cap U)=\\{x^{k+1}=\\dots=x^n=0\\}$. $S$ is an embedded $k$-submanifold iff such a chart exists around each point of $S$ (proof: rank theorem + subspace topology).",
         body="Circle near $(0,1)$: $\\varphi(x,y)=(x,y-\\sqrt{1-x^2})$. Graph of $f$: $(x,y)\\mapsto(x,y-f(x))$. Sphere near $N$: $(x,y,z-\\sqrt{1-x^2-y^2})$. In a slice chart $T_pS=\\operatorname{span}\\{\\partial_1,\\dots,\\partial_k\\}$.",
         used=[CH], related=["Embedded Submanifold", "Rank Theorem", "Tangent Space of a Submanifold"]),
    dict(title="Regular Value", aliases=["critical value", "critical point", "regular point"], scope=[T], by=BY,
         syl={T: f"[[{MT}/2026-08-27-hw4|HW4]] Q1."},
         intuition="A value that the map approaches 'transversally': at every preimage the differential is onto.",
         key="$q\\in N$ is a **regular value** of $F:M\\to N$ if $dF_p$ is surjective for every $p\\in F^{-1}(q)$; otherwise $q$ is a **critical value** and points with $dF_p$ not onto are **critical points**.",
         body="$F=x^2-y^2$: every $c\\neq0$ is regular, $0$ is critical (level set a cross). Sard's theorem: critical values have measure zero ([[DM07 Sard Whitney and Transversality]]). Regular values of $\\det$: all of $\\mathbb R^\\times$.",
         used=[CH], related=["Regular Level Set Theorem", "Immersion and Submersion"]),
    dict(title="Regular Level Set Theorem", aliases=["regular value theorem", "implicit function theorem for manifolds", "submersion level set theorem"], scope=[T, EB], by=BY,
         syl={T: f"[[{MT}/2026-08-27-hw4|HW4]] Q1.", EB: f"[[{LEE}#page=124|Lee Cors. 5.13–5.14, pp. 105–106]]."},
         intuition="Solutions of a system of equations whose derivative has full rank form a manifold of the expected dimension: the manifold version of the implicit function theorem.",
         key="$q$ regular value of $F:M^m\\to N^n$ $\\Rightarrow$ $S=F^{-1}(q)$ is an embedded submanifold of dimension $m-n$ with $T_pS=\\ker dF_p$. Proof: surjectivity of $dF$ is an open condition $\\Rightarrow$ $F$ is a submersion near $S$ $\\Rightarrow$ rank theorem gives slice charts.",
         body="$S^n=|x|^{-2}(1)$; $SL(n,\\mathbb R)=\\det^{-1}(1)$ (dim $n^2-1$); $O(n)=\\Phi^{-1}(I)$, $\\Phi=AA^T$ (dim $n(n-1)/2$). Euclidean version: [[Implicit Function Theorem]].",
         used=[CH], related=["Regular Value", "Embedded Submanifold", "Implicit Function Theorem", "Orthogonal Group"]),
    dict(title="Tangent Space of a Submanifold", aliases=["T_pS", "tangent space of a level set", "Proposition 5.37"], scope=[T], by=BY,
         syl={T: f"slides DG8, DG10 (Prop 5.37, converse set as homework) via [[{MT}/2026-08-27-august-24-28|Aug 24–28 note]]; [[{LEE}#page=134|Lee Prop. 5.37, p. 116]]."},
         intuition="The directions you can move without leaving the submanifold, seen inside the ambient tangent space.",
         key="$T_pS\\subseteq T_pM$ equals the image of $d\\iota_p$, equals $\\ker dF_p$ for a regular level set, and equals $\\{v\\in T_pM:vf=0\\ \\text{whenever}\\ f|_S\\equiv0\\}$ (Prop. 5.37).",
         body="$T_pS^n=p^\\perp$ (checked: $dF_p\\alpha'(\\tfrac14)=0$); $T_IO(n)=\\{B+B^T=0\\}$; $T_ISL(n)=\\ker\\operatorname{tr}$. A vector field is tangent to $S$ iff $Xf|_S=0$ for all $f|_S=0$ ([[DM10 Vector Fields and Lie Brackets]]).",
         used=[CH], related=["Embedded Submanifold", "Regular Level Set Theorem", "Tangent Space"]),
    dict(title="Immersed Submanifold", aliases=["immersed", "weakly embedded"], scope=[T, EB], by=BY,
         syl={T: f"slide DG12 (Prop 5.18) via [[{MT}/2026-09-03-august-31-september-4|Aug 31–Sep 4 note]].", EB: f"[[{LEE}#page=127|Lee Prop. 5.18, p. 109]]; Props. 5.21–5.23, Thm 5.29."},
         intuition="A subset that is a manifold in a topology of its own, finer than the inherited one, so that the inclusion is still an immersion.",
         key="$S\\subseteq M$ with a topology and smooth structure making $S\\hookrightarrow M$ an immersion. The image of an injective immersion is one (Prop. 5.18). Immersed submanifolds are locally embedded; embedded iff the topology is the subspace topology.",
         body="Figure-eight, dense line on $T^2$. Maps into $S$ that are smooth into $M$ need not be continuous into $S$ (Thm 5.29 requires continuity). Lie subgroups are immersed submanifolds ([[DM08 Lie Groups]]).",
         used=[CH], related=["Embedded Submanifold", "Dense Line on the Torus", "Smooth Embedding"]),
    dict(title="Orthogonal Group", aliases=["O(n)", "SO(n)", "orthogonal matrices"], scope=[T], by=BY,
         syl={T: f"[[{MT}/2026-10-10-october-5-9|Oct 5–9 note]] (DG19–DG20: $O(n)$ embedded, $SO(n)$ its identity component, $\\mathrm{{Lie}}(O(n))$ skew); HW6 Q1–Q3, HW7 Q3."},
         intuition="Rotations and reflections of $\\mathbb R^n$: the linear maps preserving lengths.",
         key="$O(n)=\\{A:AA^T=I\\}=\\Phi^{-1}(I)$, $\\Phi(A)=AA^T$. $d\\Phi_A(B)=BA^T+AB^T$ is onto $\\operatorname{Sym}(n)$ for every invertible $A$, so $O(n)$ is an embedded submanifold of dimension $n(n-1)/2$ ($1,3,6,10$ for $n=2,\\dots,5$, checked), compact, with $T_IO(n)=\\{B+B^T=0\\}$ (skew matrices). $SO(n)=O(n)_0$.",
         body="$\\det:O(n)\\to\\{\\pm1\\}$ shows $SO(n)$ is open and closed in $O(n)$. $O(n)\\cong SO(n)\\rtimes O(1)$ (HW6 Q3b). A Lie group ([[DM08 Lie Groups]]); $\\mathrm{Lie}(SO(3))\\cong(\\mathbb R^3,\\times)$ ([[DM11 The Lie Algebra of a Lie Group]]).",
         used=[CH], related=["Special Linear Group", "Regular Level Set Theorem", "Lie Group"]),
    dict(title="Special Linear Group", aliases=["SL(n)", "SL(n,R)", "unimodular group"], scope=[T], by=BY,
         syl={T: f"[[{MT}/2026-09-03-august-31-september-4|Aug 31–Sep 4 note]] (Prop 7.16: $SL(n)=\\ker\\det$ is an embedded Lie subgroup of dimension $n^2-1$); HW5 Q3, HW6 Q7."},
         intuition="Matrices that preserve volume and orientation: determinant $1$.",
         key="$SL(n,\\mathbb R)=\\det^{-1}(1)$; $d(\\det)_X(B)=\\det X\\operatorname{tr}(X^{-1}B)$ is onto $\\mathbb R$ at every $X\\in GL(n)$, so $SL(n,\\mathbb R)$ is an embedded submanifold of dimension $n^2-1$, with $T_ISL(n)=\\ker\\operatorname{tr}$ ($\\mathfrak{sl}(n)$, closed under the commutator).",
         body="$GL(n,\\mathbb C)\\cong SL(n,\\mathbb C)\\rtimes\\mathbb C^\\times$ (HW6 Q3c). Kernel of the homomorphism $\\det$ ([[DM08 Lie Groups]]).",
         used=[CH], related=["Orthogonal Group", "Regular Level Set Theorem", "Lie Group"]),
]

if __name__ == "__main__":
    write("14-Differential-Geometry", "diff-geometry", ITEMS)
