"""Concept notes for DM02 (Smooth Maps and Partitions of Unity).  .venv/bin/python -W ignore scripts/spec_dm02.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "DM02 Smooth Maps and Partitions of Unity"
MT = "mt3184-differential-geometry-and-lie-groups"
T, EB = "taught", "extra-book"
BY = ["lecture-notes", "book"]

ITEMS = [
    dict(title="Smooth Function", aliases=["smooth real-valued function", "C^infty(M)", "smooth function on a manifold"], scope=[T], by=BY,
         syl={T: f"[[{MT}/2026-08-07-august-3-7|week 1]] (smooth maps); HW2 Q1."},
         intuition="A function whose coordinate expression is smooth in every chart: calculus-friendly, independent of the coordinates chosen.",
         key="$f:M\\to\\mathbb R$ is smooth if $f\\circ\\varphi^{-1}$ is smooth for every smooth chart $(U,\\varphi)$. $C^\\infty(M)$ is a ring, and an $\\mathbb R$-algebra; vector fields act on it as derivations ([[DM10 Vector Fields and Lie Brackets]]).",
         body="Coordinate functions $x^i:U\\to\\mathbb R$ of a chart are smooth on $U$. Bump functions and partitions of unity are smooth functions with controlled supports.",
         used=[CH], related=["Smooth Map", "Bump Function", "Partition of Unity"]),
    dict(title="Smooth Map", aliases=["smooth mapping", "smooth maps between manifolds"], scope=[T], by=BY,
         syl={T: f"[[{MT}/2026-08-07-hw1|HW1]] Q3; [[{MT}/2026-08-14-hw2|HW2]] Q4."},
         intuition="A map that is smooth when written in coordinates on both sides.",
         key="$F:M\\to N$ is smooth if each $p$ has smooth charts $(U,\\varphi)\\ni p$, $(V,\\psi)\\ni F(p)$ with $F(U)\\subseteq V$ and $\\psi\\circ F\\circ\\varphi^{-1}$ smooth. For continuous $F$ this need be checked in **one** chart pair at each point (HW1 Q3).",
         body="Smooth $\\Rightarrow$ continuous; compositions, projections, inclusions of open sets, charts, product maps are smooth. Antipodal map of $S^2$: $u\\mapsto-u$ in stereographic charts. Matrix multiplication and inversion on $GL(n,\\mathbb R)$ are smooth ([[DM08 Lie Groups]]). The derivative of a smooth map: [[Differential of a Smooth Map]].",
         used=[CH], related=["Coordinate Representation of a Map", "Diffeomorphism", "Smooth Function"]),
    dict(title="Diffeomorphism", aliases=["diffeomorphic", "smooth isomorphism"], scope=[T], by=BY,
         syl={T: f"[[{MT}/2026-08-27-august-24-28|Aug 24–28 note]] (Prop 8.19: diffeomorphism and $F$-related fields); Thm 4.14 (global rank theorem)."},
         intuition="A change of coordinates between manifolds: smooth, invertible, with smooth inverse.",
         key="A smooth bijection $F:M\\to N$ with smooth inverse. Equivalent (inverse function theorem): a smooth bijection with invertible $dF_p$ for all $p$; a bijective constant-rank smooth map is a diffeomorphism (Global Rank Theorem, [[DM04 The Tangent Bundle and the Rank Theorem]]).",
         body="$x\\mapsto x^3$ is a smooth bijection of $\\mathbb R$ that is not a diffeomorphism. Lie group isomorphisms are diffeomorphisms ([[DM08 Lie Groups]]); left translations $L_g$ are diffeomorphisms.",
         used=[CH], related=["Smooth Map", "Local Diffeomorphism", "Inverse Function Theorem"]),
    dict(title="Coordinate Representation of a Map", aliases=["local expression", "coordinate expression", "representation in charts"], scope=[T], by=BY,
         syl={T: f"[[{MT}/2026-08-14-hw2|HW2]] Q4, [[{MT}/2026-08-20-hw3|HW3]] Q1; Test 1 Q2–Q4."},
         intuition="Write the map in the coordinates you choose on each side; all calculus (Jacobians, differentials) is done there.",
         key="For $F:M\\to N$ and charts $(U,\\varphi)$, $(V,\\psi)$ with $F(U)\\subseteq V$: $\\widehat F=\\psi\\circ F\\circ\\varphi^{-1}:\\varphi(U)\\to\\psi(V)$. The differential $dF_p$ has the Jacobian $D\\widehat F(\\varphi(p))$ as matrix in the coordinate bases ([[DM03 Tangent Vectors and the Differential]]).",
         body="Choose charts that make $\\widehat F$ simple: e.g. antipodal map of $S^2$ in $\\psi_2$ (at $N$) and $\\psi_1$ (at $S$) is $u\\mapsto-u$.",
         used=[CH], related=["Smooth Map", "Transition Map"]),
    dict(title="Bump Function", aliases=["cutoff function", "cut-off function", "flat function", "smooth step"], scope=[T, EB], by=BY,
         syl={T: f"HW2 Q1, Test 1 Q1 (locality of tangent vectors), HW4 Q2 (extension of a vector).", EB: f"[[{LEE}#page=59|Lee Lemmas 2.20–2.22 (pp. 41–42)]], [[{LEE}#page=62|Prop. 2.25 (p. 44)]]; Tu §13."},
         intuition="A smooth function that is $1$ on a chosen set and $0$ outside a slightly larger one: a smooth switch.",
         key="$f(t)=e^{-1/t}$ ($t>0$), $0$ otherwise, is smooth and flat at $0$; $h(t)=f(t)/(f(t)+f(1-t))$ is a smooth step ($0$ for $t\\le0$, $1$ for $t\\ge1$); $b(x)=h(2-|x|)$ is $1$ on $\\overline B_1$ and supported in $\\overline B_2$. On a manifold: for closed $A\\subseteq U$ open there is smooth $\\psi$ with $\\psi=1$ on $A$, $\\operatorname{supp}\\psi\\subseteq U$.",
         body="Numbers: $f(t)/t^{20}=3.7\\times10^{-4}$ at $t=0.01$; $h(0.25)=0.0650$, $h(0.75)=0.9350$. Proves locality of derivations and lets one extend vectors to vector fields.",
         used=[CH], related=["Partition of Unity", "Smooth Extension Lemma", "Smooth Urysohn Lemma"]),
    dict(title="Partition of Unity", aliases=["subordinate partition of unity", "partitions of unity"], scope=[T, EB], by=BY,
         syl={T: f"[[{MT}/2026-08-07-august-3-7|week 1 post]]: partitions of unity discussed (proof not confirmed).", EB: f"[[{LEE}#page=61|Lee Thm 2.23, p. 43]]."},
         intuition="Smooth weights $\\psi_\\alpha\\ge0$, each living in one patch, that sum to $1$ everywhere: a way to blend local constructions into a global one.",
         key="A family $\\{\\psi_\\alpha\\}$ of smooth $[0,1]$-valued functions with locally finite supports and $\\sum\\psi_\\alpha=1$; subordinate to $\\{U_\\alpha\\}$ if $\\operatorname{supp}\\psi_\\alpha\\subseteq U_\\alpha$. Exists for every open cover of a smooth manifold (compact exhaustion + bumps, [[Compact Exhaustion]]).",
         body="Example on $\\mathbb R$ subordinate to $\\{(-\\infty,1),(0,\\infty)\\}$: $\\psi_2=h(3x-1)$, $\\psi_1=1-\\psi_2$. Supports are closures: check them, not zero sets. Used for extension, smooth Urysohn, Riemannian metrics, integration.",
         used=[CH], related=["Bump Function", "Locally Finite Family", "Paracompact Space"]),
    dict(title="Smooth Extension Lemma", aliases=["extension lemma", "extending smooth functions"], scope=[EB], by=["book"],
         syl={EB: f"[[{LEE}#page=63|Lee Lemma 2.26, p. 45]]."},
         intuition="A function that is smooth near a closed set can be extended to a smooth function on the whole manifold, because a partition of unity glues the local extensions.",
         key="If $A\\subseteq M$ is closed and $f:A\\to\\mathbb R^k$ is locally the restriction of smooth functions, then for every open $U\\supseteq A$ there is a smooth $\\tilde f$ on $M$, $\\tilde f|_A=f$, $\\operatorname{supp}\\tilde f\\subseteq U$.",
         body="Simplest case: $f$ smooth on an open $W\\supseteq A$: $\\tilde f=\\psi f$ with a bump $\\psi$. Used to extend vectors and functions from submanifolds ([[DM06 Submanifolds]]).",
         used=[CH], related=["Partition of Unity", "Bump Function"]),
    dict(title="Smooth Urysohn Lemma", aliases=["smooth Urysohn", "smooth separation of closed sets"], scope=[EB], by=["book"],
         syl={EB: f"[[{LEE}#page=65|Lee Thm 2.29, p. 47]] (every closed set is a zero set of a smooth function); a consequence of [[Partition of Unity]]."},
         intuition="Smooth functions are rich enough to separate any two disjoint closed sets, like the topological Urysohn lemma but with $C^\\infty$.",
         key="For disjoint closed $A,B\\subseteq M$ there is smooth $f:M\\to[0,1]$ with $f|_A=0$, $f|_B=1$ (from a partition of unity subordinate to $\\{M\\setminus B,M\\setminus A\\}$).",
         body="Smooth analogue of [[Separation Axioms]]; on $\\mathbb R$, $f=h$ separates $\\{x\\le0\\}$ from $\\{x\\ge1\\}$.",
         used=[CH], related=["Partition of Unity", "Bump Function", "Separation Axioms"]),
]

if __name__ == "__main__":
    write("14-Differential-Geometry", "diff-geometry", ITEMS)
