"""Concept notes for PA15 (Covering Spaces and the Fundamental Group).  .venv/bin/python -W ignore scripts/spec_pa15.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "PA15 Covering Spaces and the Fundamental Group"
EB = ["extra-book"]

ITEMS = [
    dict(title="Homotopy", aliases=["homotopic maps", "path homotopy", "homotopy equivalence", "null-homotopic", "contractible"], scope=EB,
         syl=f"[[{LEE}#page=631|Lee Props. A.62, Thm A.71, pp. 613–615]]; Hatcher §0.",
         intuition="A continuous deformation of one map into another, played as a movie parametrised by $t\\in[0,1]$.",
         key="$f_0\\simeq f_1$ if there is a continuous $H:X\\times[0,1]\\to Y$ with $H_0=f_0$, $H_1=f_1$. A **path homotopy** fixes the endpoints. A homotopy equivalence has a homotopy inverse; a space homotopy equivalent to a point is **contractible**.",
         body="Convex sets are contractible (straight-line homotopy). Homotopy equivalences induce isomorphisms on $\\pi_1$ ([[Fundamental Group]]) and, for smooth manifolds, on de Rham cohomology.",
         used=[CH], related=["Fundamental Group", "Winding Number"]),
    dict(title="Fundamental Group", aliases=["pi_1", "π1", "simply connected", "first homotopy group"], scope=EB,
         syl=f"[[{LEE}#page=632|Lee App. A, Props. A.64–A.69, p. 614]]; Hatcher §1.1.",
         intuition="The group of loops at a point that cannot be pulled tight, multiplied by going around one after the other.",
         key="$\\pi_1(X,x_0)$ = path-homotopy classes of loops at $x_0$, product = concatenation. $X$ is **simply connected** if path-connected with $\\pi_1=1$. A map $f$ induces $f_*:\\pi_1(X)\\to\\pi_1(Y)$, functorially.",
         body="$\\pi_1(\\mathbb R^n)=1$, $\\pi_1(S^1)=\\mathbb Z$, $\\pi_1(S^n)=1$ ($n\\ge2$), $\\pi_1(T^n)=\\mathbb Z^n$, $\\pi_1(\\mathbb{RP}^n)=\\mathbb Z/2$ ($n\\ge2$), $\\pi_1(SO(3))=\\mathbb Z/2$, $\\pi_1(SL(2,\\mathbb R))=\\mathbb Z$. Simply connected Lie groups are the domain of the Lie correspondence ([[DM15 Closed Subgroups and the Lie Correspondence]]).",
         used=[CH], related=["Homotopy", "Covering Space", "Universal Cover", "Winding Number"]),
    dict(title="Covering Space", aliases=["covering map", "evenly covered", "sheet", "covering"], scope=EB,
         syl=f"[[{LEE}#page=633|Lee App. A 'Covering Maps', p. 615]]; Hatcher §1.3.",
         intuition="Several identical floors stacked over each small region of the base, joined by ramps as you go around holes.",
         key="A continuous surjection $\\pi:E\\to X$ such that each point has an open neighbourhood $U$ with $\\pi^{-1}(U)=\\bigsqcup\\widetilde U_\\alpha$, each $\\widetilde U_\\alpha\\to U$ a homeomorphism. Covering maps are local homeomorphisms and open maps; fibres are discrete.",
         body="$\\mathbb R\\to S^1$ (fibre $\\mathbb Z$), $z\\mapsto z^k$ ($k$ sheets), $S^n\\to\\mathbb{RP}^n$ (2 sheets), $\\mathbb R^n\\to T^n$, $SU(2)\\to SO(3)$ (2 sheets). Not a covering: $(0,2)\\to S^1$ (local homeomorphism, surjective, but not evenly covered at $1$). Smooth version: [[DM05 Immersions, Embeddings, Submersions and Coverings]].",
         used=[CH, "DM05 Immersions, Embeddings, Submersions and Coverings"], related=["Path Lifting", "Universal Cover", "Deck Transformation"]),
    dict(title="Path Lifting", aliases=["homotopy lifting", "unique path lifting", "monodromy"], scope=EB,
         syl=f"[[{LEE}#page=634|Lee Prop. A.77, p. 616]]; Hatcher Props. 1.30, 1.33.",
         intuition="Walk in the base and the covering tells you, uniquely, where you are walking upstairs once you fix where you start.",
         key="For a covering $\\pi:E\\to X$, every path $\\gamma$ in $X$ with a chosen start $e_0$ over $\\gamma(0)$ has a unique lift $\\tilde\\gamma$ with $\\tilde\\gamma(0)=e_0$; homotopies lift likewise. Path-homotopic paths have lifts with the same endpoint; $\\pi_*$ is injective.",
         body="Proof: cut $[0,1]$ into pieces mapping into evenly covered sets (compactness), lift piece by piece, glue ([[Gluing Lemma]]); uniqueness: the coincidence set is open and closed. Winding number = end of the lift through $\\mathbb R\\to S^1$ ([[Winding Number]]).",
         used=[CH], related=["Covering Space", "Lifting Criterion", "Fundamental Group"]),
    dict(title="Lifting Criterion", aliases=["lifting criterion", "lifting theorem"], scope=EB,
         syl=f"[[{LEE}#page=634|Lee Prop. A.78, p. 616]]; Hatcher Prop. 1.33.",
         intuition="A map can be lifted through a covering exactly when its loops are the images of loops upstairs.",
         key="$f:(Y,y_0)\\to(X,x_0)$, $Y$ path-connected and locally path-connected, lifts through the covering $\\pi:(E,e_0)\\to(X,x_0)$ iff $f_*\\pi_1(Y)\\subseteq\\pi_*\\pi_1(E)$. If $Y$ is simply connected the lift always exists (and is unique).",
         body="Every map $S^2\\to S^1$ lifts to $\\mathbb R$, hence is null-homotopic. Used to show that homomorphisms and smooth maps from simply connected groups/manifolds lift through covering homomorphisms.",
         used=[CH], related=["Path Lifting", "Universal Cover", "Fundamental Group"]),
    dict(title="Universal Cover", aliases=["universal covering space", "simply connected cover"], scope=EB,
         syl=f"[[{LEE}#page=634|Lee Prop. A.80, p. 616]]; Hatcher §1.3.",
         intuition="The most unwrapped version of a space: all its loops cut open, so the cover is simply connected.",
         key="A covering $\\widetilde X\\to X$ with $\\widetilde X$ simply connected. It exists for connected, locally path-connected, semilocally simply connected $X$ (every manifold), is unique up to isomorphism, and $\\operatorname{Deck}(\\widetilde X\\to X)\\cong\\pi_1(X)$. The universal cover of a connected Lie group is a Lie group.",
         body="$\\mathbb R\\to S^1$, $\\mathbb R^n\\to T^n$, $S^n\\to\\mathbb{RP}^n$, $SU(2)\\to SO(3)$ (verified: 2-sheeted homomorphism, kernel $\\pm1$), $\\widetilde{SL}(2,\\mathbb R)\\to SL(2,\\mathbb R)$ (no faithful finite-dimensional representation).",
         used=[CH], related=["Covering Space", "Deck Transformation", "Fundamental Group"]),
    dict(title="Deck Transformation", aliases=["deck group", "covering transformation"], scope=EB,
         syl="Hatcher §1.3.",
         intuition="A symmetry of the covering space that shuffles the floors without changing what lies below.",
         key="A homeomorphism $\\varphi:E\\to E$ with $\\pi\\circ\\varphi=\\pi$. They form a group; for a universal covering it is isomorphic to $\\pi_1(X)$. A free properly discontinuous action of a discrete group $\\Gamma$ has $X\\to X/\\Gamma$ as covering with deck group $\\Gamma$.",
         body="$\\mathbb R\\to S^1$: translations by $\\mathbb Z$; $S^n\\to\\mathbb{RP}^n$: antipodal map, $\\mathbb Z/2$; $z\\mapsto z^k$: $\\mathbb Z/k$.",
         used=[CH], related=["Universal Cover", "Covering Space", "Fundamental Group"]),
    dict(title="Winding Number", aliases=["degree of a loop", "winding number around a point"], scope=EB,
         syl=f"[[{LEE}#page=632|Lee Prop. A.68, p. 614]]; Hatcher Thm 1.7.",
         intuition="How many times a loop goes around, counted with sign: the integer at which the lifted path ends.",
         key="For a loop $\\gamma$ in $S^1$ (or in $\\mathbb C\\setminus\\{0\\}$, via $\\gamma/|\\gamma|$), lift through $t\\mapsto e^{2\\pi it}$ starting at $0$; the endpoint $\\tilde\\gamma(1)\\in\\mathbb Z$ is the winding number. $\\pi_1(S^1)\\cong\\mathbb Z$ via this map; $z\\mapsto z^k$ multiplies it by $k$.",
         body="Computed values: $e^{2\\pi i3t}\\mapsto3$, $e^{-2\\pi i2t}\\mapsto-2$, a wobbly $3$-turn loop $\\mapsto3$, circles of radius $1$ centred at $0.99$ and $1.01$ $\\mapsto1$ and $0$ (jumps when $0$ crosses the curve). Homotopy invariant.",
         used=[CH], related=["Fundamental Group", "Path Lifting", "Homotopy"]),
]

if __name__ == "__main__":
    write("11-Proofs-Analysis-Topology", "analysis", ITEMS)
