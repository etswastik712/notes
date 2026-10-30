"""Concept notes for DM05 (Immersions, Embeddings, Submersions and Coverings).  .venv/bin/python -W ignore scripts/spec_dm05.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "DM05 Immersions, Embeddings, Submersions and Coverings"
MT = "mt3184-differential-geometry-and-lie-groups"
T, EB = "taught", "extra-book"
BY = ["lecture-notes", "book"]

ITEMS = [
    dict(title="Immersion and Submersion", aliases=["immersion", "submersion", "smooth submersion", "smooth immersion"], scope=[T], by=BY,
         syl={T: f"slides DG11–DG12 via [[{MT}/2026-09-03-august-31-september-4|Aug 31–Sep 4 note]]; [[{MT}/2026-09-04-hw5|HW5]] Q1."},
         intuition="An immersion never squashes a direction (velocity never vanishes); a submersion reaches every direction in the target.",
         key="$F:M\\to N$ is an **immersion** if every $dF_p$ is injective, a **submersion** if every $dF_p$ is surjective. By the Rank Theorem an immersion is locally an inclusion $(x)\\mapsto(x,0)$ and a submersion locally a projection $(x,y)\\mapsto x$ ([[Rank Theorem]]). Submersions are open maps with local sections.",
         body="Immersion: $\\dim M\\le\\dim N$; submersion: $\\dim M\\ge\\dim N$. Examples: $\\det:GL(n,\\mathbb R)\\to\\mathbb R^\\times$ (submersion), the cusp $t\\mapsto(t^2,t^3)$ (not an immersion). Immersions need not be embeddings ([[Smooth Embedding]]).",
         used=[CH, "DM04 The Tangent Bundle and the Rank Theorem"], related=["Smooth Embedding", "Local Section Theorem", "Rank Theorem"]),
    dict(title="Smooth Embedding", aliases=["embedding", "embedded image", "injective immersion"], scope=[T, EB], by=BY,
         syl={T: f"DG12: the figure-eight and the dense line are injective immersions that are not embeddings; HW5 Q1.", EB: f"[[{LEE}#page=103|Lee Examples 4.17–4.20, p. 85]]; [[{LEE}#page=105|Prop. 4.22, p. 87]]."},
         intuition="An immersion that is also a faithful copy topologically: the image looks, with its inherited topology, exactly like the domain.",
         key="A smooth immersion that is a homeomorphism onto its image (subspace topology). An **injective immersion** is an embedding if $F$ is open/closed, **proper**, $M$ is compact, or $\\dim M=\\dim N$ (HW5 Q1). Immersions are locally embeddings (Lee Thm 4.25).",
         body="Not embeddings: figure-eight $\\beta(t)=(\\sin2t,\\sin t)$, dense line $t\\mapsto(e^{it},e^{i\\sqrt2t})$ on $T^2$ ([[Dense Line on the Torus]]). $t\\mapsto(t^3,0)$ is a topological but not smooth embedding. Images of embeddings are embedded submanifolds ([[DM06 Submanifolds]]).",
         used=[CH], related=["Immersion and Submersion", "Proper Map", "Homeomorphism and Embedding"]),
    dict(title="Proper Map", aliases=["proper continuous map", "proper"], scope=[T, EB], by=BY,
         syl={T: f"[[{MT}/2026-09-04-hw5|HW5]] Q1(b).", EB: f"[[{LEE}#page=629|Lee Thm A.57, p. 611]]."},
         intuition="Preimages of compact sets are compact: nothing can escape to infinity in the domain while staying bounded in the target.",
         key="$F:X\\to Y$ is **proper** if $F^{-1}(K)$ is compact for each compact $K$. A proper continuous map into a locally compact Hausdorff space is **closed**; hence a proper injective immersion is an embedding. Every continuous map from a compact space is proper.",
         body="The dense line on the torus is not proper (the image is bounded but the domain is not compact). The closed map lemma is the compact case ([[Closed Map Lemma]]).",
         used=[CH], related=["Smooth Embedding", "Closed Map Lemma", "Locally Compact Space"]),
    dict(title="Local Section Theorem", aliases=["local sections", "Theorem 4.26", "section of a submersion"], scope=[EB], by=["book"],
         syl={EB: f"[[{LEE}#page=106|Lee Thm 4.26, p. 88]]."},
         intuition="Through every point of the domain of a submersion there is a smooth way of choosing, over a neighbourhood of the image, a point in each fibre.",
         key="$\\pi:M\\to N$ is a submersion iff every point of $M$ lies in the image of a smooth local section $\\sigma:V\\to M$ ($\\pi\\sigma=\\mathrm{id}_V$). Consequences: submersions are open; the characteristic property.",
         body="Proof: rank theorem gives $\\sigma(x)=(x,0)$; converse by $d\\pi\\circ d\\sigma=\\mathrm{id}$. For $\\pi(x,y)=x+y^2$: $\\sigma(s)=(s-y_0^2,y_0)$.",
         used=[CH], related=["Immersion and Submersion", "Characteristic Property of Surjective Submersions"]),
    dict(title="Characteristic Property of Surjective Submersions", aliases=["passing smoothly to the quotient", "smooth quotient property", "Theorem 4.29"], scope=[EB], by=["book"],
         syl={EB: f"[[{LEE}#page=108|Lee Thms 4.29–4.31, p. 90]]."},
         intuition="A map out of the base of a surjective submersion is smooth exactly when its pull-back to the total space is: smoothness descends.",
         key="For a surjective submersion $\\pi:M\\to N$: $F:N\\to P$ is smooth iff $F\\circ\\pi$ is smooth; a smooth $G:M\\to P$ constant on fibres factors uniquely through a smooth $\\widehat G:N\\to P$.",
         body="Used to show maps induced on quotients ($G/H$, $\\mathbb{RP}^n$) are smooth ([[DM09 Group Actions and Semidirect Products]]). Proof via local sections.",
         used=[CH], related=["Local Section Theorem", "Quotient Topology"]),
    dict(title="Smooth Covering Map", aliases=["smooth covering", "covering manifold", "universal covering manifold"], scope=[EB], by=["book"],
         syl={EB: f"[[{LEE}#page=109|Lee Prop. 4.33, p. 91]], [[{LEE}#page=110|Prop. 4.40, p. 92]], [[{LEE}#page=112|Cor. 4.43, p. 94]]."},
         intuition="A covering in which the floors are not just homeomorphic but diffeomorphic to the base.",
         key="A smooth surjection $\\pi:E\\to M$ of connected manifolds with evenly covered neighbourhoods whose sheets map **diffeomorphically**. Equivalent: a topological covering that is a local diffeomorphism. Smooth coverings are local diffeomorphisms, submersions, open, quotient maps; every connected manifold has a universal covering manifold; lifts of smooth maps are smooth.",
         body="$\\mathbb R\\to S^1$, $z\\mapsto z^k$ ($k$ sheets), $S^n\\to\\mathbb{RP}^n$, $\\exp:\\mathbb C\\to\\mathbb C^\\times$, $SU(2)\\to SO(3)$ (a covering homomorphism, [[DM08 Lie Groups]]). Topological version: [[Covering Space]].",
         used=[CH], related=["Covering Space", "Universal Cover", "Immersion and Submersion"]),
    dict(title="Dense Line on the Torus", aliases=["irrational winding", "dense curve on the torus", "Lie subgroup that is not closed"], scope=[T], by=BY,
         syl={T: f"slide DG12 (injective immersion with non-embedded image); [[{MT}/2026-09-03-august-31-september-4|Aug 31–Sep 4 note]]; HW9 Q6 (closure of a Lie subgroup)."},
         intuition="Wind a line around a doughnut with an irrational slope: it never closes up, never repeats, and comes arbitrarily close to every point.",
         key="$F(t)=(e^{it},e^{i\\alpha t})$, $\\alpha$ irrational: an injective immersion $\\mathbb R\\to T^2$ with dense image, hence not an embedding. By Dirichlet, $F(2\\pi q)\\to F(0)$ along integers $q\\to\\infty$.",
         body="$\\alpha=\\sqrt2$: smallest distance to $F(0)$ for $t\\le10,10^2,10^3,10^4$ is $1.50,0.107,0.0183,0.00153$; at $t=2\\pi\\cdot985$ it is $2.3\\times10^{-3}$. It is a one-parameter subgroup of $T^2$ whose image is a **non-closed Lie subgroup** ([[DM15 Closed Subgroups and the Lie Correspondence]]).",
         used=[CH], related=["Smooth Embedding", "Immersion and Submersion"]),
]

if __name__ == "__main__":
    write("14-Differential-Geometry", "diff-geometry", ITEMS)
