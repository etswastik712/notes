"""Concept notes for DM04 (The Tangent Bundle and the Rank Theorem).  .venv/bin/python -W ignore scripts/spec_dm04.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "DM04 The Tangent Bundle and the Rank Theorem"
MT = "mt3184-differential-geometry-and-lie-groups"
T, EB = "taught", "extra-book"
BY = ["lecture-notes", "book"]

ITEMS = [
    dict(title="Tangent Bundle", aliases=["TM", "tangent bundle of a manifold", "natural chart on TM"], scope=[T], by=BY,
         syl={T: f"slide DG8 via [[{MT}/2026-08-20-august-17-21|Aug 17–21 note]]; [[{MT}/2026-08-20-hw3|HW3]] Q2; [[{LEE}#page=84|Lee Prop. 3.18, p. 66]]."},
         intuition="All tangent spaces glued into one space: a point of $TM$ is a position together with a velocity at that position (phase space of motion on $M$).",
         key="$TM=\\bigsqcup_{p}T_pM$ with $\\pi:TM\\to M$. It is a smooth $2n$-manifold with natural charts $\\tilde\\varphi(\\sum v^i\\partial_i|_p)=(\\varphi(p);v^1,\\dots,v^n)$ and transitions $(x;v)\\mapsto(\\tau(x);D\\tau(x)v)$ (Chart Lemma); $\\pi$ is smooth.",
         body="$TS^1\\cong S^1\\times\\mathbb R$ ($(w,v)\\mapsto(1/w,-v/w^2)$); $T\\mathbb R^n=\\mathbb R^{2n}$; $TS^2$ is not trivial (Hairy Ball). Vector fields are sections of $\\pi$ ([[DM10 Vector Fields and Lie Brackets]]). Built with the [[Smooth Manifold Chart Lemma]].",
         used=[CH], related=["Global Differential", "Local Frame", "Smooth Manifold Chart Lemma"]),
    dict(title="Global Differential", aliases=["dF: TM -> TN", "differential as a bundle map"], scope=[EB], by=["book"],
         syl={EB: f"[[{LEE}#page=86|Lee Prop. 3.21, Cor. 3.22, p. 68]]."},
         intuition="All the pointwise differentials $dF_p$ assembled into one smooth map of tangent bundles.",
         key="$dF:TM\\to TN$, $dF|_{T_pM}=dF_p$, is smooth: in natural charts $(x;v)\\mapsto(\\widehat F(x);D\\widehat F(x)v)$. $d(G\\circ F)=dG\\circ dF$ and $d(\\mathrm{id})=\\mathrm{id}$: $T$ is a functor.",
         body="Sends a curve $\\gamma$ to its velocity curve $\\gamma'$; diffeomorphisms to diffeomorphisms of bundles. Used for $F$-relatedness of vector fields ([[DM10 Vector Fields and Lie Brackets]]).",
         used=[CH], related=["Tangent Bundle", "Differential of a Smooth Map"]),
    dict(title="Local Frame", aliases=["global frame", "parallelizable", "frame field", "trivial tangent bundle"], scope=[T], by=BY,
         syl={T: f"slide DG9 (local frame, Lie groups have global frames); [[{MT}/2026-08-27-hw4|HW4]] Q4."},
         intuition="A smoothly varying choice of a basis of the tangent space at every point of a region.",
         key="A **local frame** on $U$ is $n$ vector fields $E_1,\\dots,E_n$ forming a basis of $T_pM$ at each $p\\in U$ (a coordinate frame $\\partial/\\partial x^i$ is one). A **global frame** exists iff $M$ is **parallelizable**, iff $TM\\cong M\\times\\mathbb R^n$ (HW4 Q4).",
         body="Parallelizable: $\\mathbb R^n$, $S^1$, $S^3$, $S^7$, every Lie group (left-invariant fields: [[DM11 The Lie Algebra of a Lie Group]]). Not: $S^2$ ([[Hairy Ball Theorem]]).",
         used=[CH], related=["Tangent Bundle", "Hairy Ball Theorem"]),
    dict(title="Rank of a Smooth Map", aliases=["constant rank", "rank of dF", "rank of the differential"], scope=[T], by=BY,
         syl={T: f"slide DG11–DG12 via [[{MT}/2026-08-27-august-24-28|Aug 24–28 note]]."},
         intuition="How many independent directions survive the map at a point: the rank of the Jacobian in any charts.",
         key="$\\operatorname{rank}F|_p=\\operatorname{rank}dF_p$. $F$ has **constant rank** $r$ if this equals $r$ at every point; **immersion** ($r=\\dim M$), **submersion** ($r=\\dim N$) are the extreme cases ([[Immersion and Submersion]]).",
         body="Rank can jump: $x^2$ (rank 0 at $0$), the height function $z$ on $S^2$ (rank 0 at the poles, $|\\nabla z|=4|w|/(|w|^2+1)^2$ in the stereographic chart). Lie group homomorphisms and equivariant maps have constant rank ([[DM08 Lie Groups]], [[DM09 Group Actions and Semidirect Products]]).",
         used=[CH], related=["Rank Theorem", "Global Rank Theorem", "Differential of a Smooth Map"]),
    dict(title="Rank Theorem", aliases=["constant rank theorem", "Theorem 4.12", "normal form of constant rank maps"], scope=[T], by=BY,
         syl={T: f"slide DG11; [[{LEE}#page=99|Lee Thm 4.12, p. 81]]."},
         intuition="A map of constant rank is, in suitable coordinates on source and target, the plain map that keeps $r$ coordinates and zeroes the rest.",
         key="$F:M^m\\to N^n$ smooth of constant rank $r$ $\\Rightarrow$ around each $p$ there are charts centred at $p$ and $F(p)$ with $\\psi\\circ F\\circ\\varphi^{-1}(x^1,\\dots,x^m)=(x^1,\\dots,x^r,0,\\dots,0)$. Submersion $\\Leftrightarrow$ locally a projection; immersion $\\Leftrightarrow$ locally an inclusion.",
         body="Proof: apply the Euclidean theorem ([[Constant Rank Theorem (Euclidean)]]) to the coordinate representation and compose the charts with the diffeomorphisms. Normal form checked for $F(u,v)=(u+v,(u+v)^2)$: $\\psi F\\varphi^{-1}=(s,0)$ to $9\\times10^{-16}$.",
         used=[CH], related=["Global Rank Theorem", "Rank of a Smooth Map", "Constant Rank Theorem (Euclidean)", "Inverse Function Theorem"]),
    dict(title="Global Rank Theorem", aliases=["Theorem 4.14", "constant rank global consequences"], scope=[T], by=BY,
         syl={T: f"slides DG11, DG12; [[{LEE}#page=101|Lee Thm 4.14, p. 83]]."},
         intuition="A constant-rank map that is onto must have full rank in the target; one that is one-to-one must have full rank in the source.",
         key="$F:M\\to N$ smooth of **constant rank**: (a) surjective $\\Rightarrow$ submersion; (b) injective $\\Rightarrow$ immersion; (c) bijective $\\Rightarrow$ diffeomorphism.",
         body="(a) uses the Rank Theorem + [[Baire Category Theorem]] ($N$ would be a countable union of nowhere dense sets). Consequence: a bijective Lie group homomorphism is an isomorphism ([[DM08 Lie Groups]]). Fails without constant rank: $x\\mapsto x^3$.",
         used=[CH], related=["Rank Theorem", "Baire Category Theorem", "Diffeomorphism"]),
    dict(title="Baire Category Theorem", aliases=["Baire", "nowhere dense", "Baire category"], scope=[T, EB], by=BY,
         syl={T: f"slide DG11 (nowhere dense sets, Baire).", EB: f"[[{LEE}#page=629|Lee Thm A.58, p. 611]]; Munkres §48."},
         intuition="A nonempty complete or locally compact space is 'too big' to be a countable union of thin (nowhere dense) closed sets.",
         key="In a locally compact Hausdorff space or a complete metric space, a countable union of closed sets with empty interior has empty interior. $A$ is **nowhere dense** if $\\operatorname{int}\\bar A=\\varnothing$ ($\\mathbb Q\\subset\\mathbb R$: not; Cantor set: yes; $\\mathbb R^k\\times\\{0\\}\\subset\\mathbb R^n$, $k<n$: yes).",
         body="Proof for complete metric spaces by nested closed balls. In DM04 it proves that a surjective constant-rank map has full rank. Also gives uncountability of $\\mathbb R$-like spaces.",
         used=[CH], related=["Global Rank Theorem", "Locally Compact Space", "Cantor's Theorem"]),
    dict(title="Hairy Ball Theorem", aliases=["hairy ball", "Poincare-Hopf for spheres", "nowhere-vanishing vector field on S^n"], scope=[T], by=BY,
         syl={T: f"slide DG8 (stated: $S^n$ has a nowhere-vanishing vector field iff $n$ is odd); [[{MT}/2026-08-20-hw3|HW3]] Q3."},
         intuition="You cannot comb a hairy ball flat: some point always has a cowlick (on even-dimensional spheres).",
         key="$S^n$ has a nowhere-vanishing smooth vector field iff $n$ is odd. $S^1$: the rotation field; $S^3$: left-invariant fields of $SU(2)$; $S^2$: none, but the HW3 Q3 field $\\widetilde Y=(\\tilde u_2^2-\\tilde u_1^2,-2\\tilde u_1\\tilde u_2)$ has exactly one zero.",
         body="Stated, not proved (needs degree theory / Poincaré–Hopf). $S^2$ is not parallelizable; Lie groups always are ([[DM11 The Lie Algebra of a Lie Group]]).",
         used=[CH], related=["Local Frame", "Tangent Bundle"]),
]

if __name__ == "__main__":
    write("14-Differential-Geometry", "diff-geometry", ITEMS)
