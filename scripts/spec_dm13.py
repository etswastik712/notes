"""Concept notes for DM13 (Lie Derivatives and Commuting Vector Fields).  .venv/bin/python -W ignore scripts/spec_dm13.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "DM13 Lie Derivatives and Commuting Vector Fields"
MT = "mt3184-differential-geometry-and-lie-groups"
T, EB = "taught", "extra-book"
BY = ["lecture-notes", "book"]

ITEMS = [
    dict(title="Lie Derivative of a Vector Field", aliases=["Lie derivative", "L_V W", "Theorem 9.38", "derivative along a flow"], scope=[T, EB], by=BY,
         syl={T: f"slides DG24–DG25 via [[{MT}/2026-10-16-october-12-16|Oct 12–16]] and [[{MT}/2026-10-24-october-19-24|Oct 19–24]] notes; HW8 Q5–Q6.", EB: f"[[{LEE}#page=246|Lee Lemma 9.36, p. 228]], [[{LEE}#page=247|Lee Thm 9.38, p. 229]]."},
         intuition="How $W$ changes as seen by an observer carried along by the flow of $V$: pull $W$ back to $p$ with the flow and differentiate.",
         key="$(\\mathcal L_VW)_p=\\frac d{dt}|_0\\,d(\\theta_{-t})_{\\theta_t(p)}W_{\\theta_t(p)}$ ($\\theta$ the flow of $V$). Exists and is smooth (Lemma 9.36). **Theorem 9.38: $\\mathcal L_VW=[V,W]$** (flow-box proof by cases). Properties: $\\mathcal L_VW=-\\mathcal L_WV$; $\\mathcal L_{[V,W]}=[\\mathcal L_V,\\mathcal L_W]$; $\\mathcal L_V(gW)=(Vg)W+g\\mathcal L_VW$; $F_*\\mathcal L_VX=\\mathcal L_{F_*V}F_*X$.",
         body="Constant $V=v$ on $\\mathbb R^n$: $\\mathcal L_VW=D_vW$ (HW8 Q5). Shear $y\\partial_x+\\partial_y$ and $x\\partial_y$: $[V,W]=(-x,y)$ checked from the definition. Depends on $V$ near $p$, not just along an integral curve (HW8 Q6). Quantum analogue: Heisenberg equation $\\dot A=\\tfrac i\\hbar[H,A]$.",
         used=[CH, "DM14 One-Parameter Subgroups and the Exponential Map"], related=["Lie Bracket of Vector Fields", "Flow of a Vector Field", "Invariant Vector Field", "Commuting Vector Fields"]),
    dict(title="Invariant Vector Field", aliases=["invariant under a flow", "flow-invariant vector field", "Theorem 9.42"], scope=[EB], by=BY,
         syl={EB: f"[[{LEE}#page=249|Lee Prop. 9.41, Thm 9.42, p. 231]]."},
         intuition="A field that the flow carries onto itself: moving the field along the flow changes nothing.",
         key="$W$ is invariant under the flow $\\theta$ of $V$ if $d(\\theta_t)_pW_p=W_{\\theta_t(p)}$. **Thm 9.42:** $[V,W]=0\\iff W$ is $\\theta^V$-invariant $\\iff V$ is $\\theta^W$-invariant. Cor 9.43: every field is invariant under its own flow. Proof via $X(t)=d(\\theta_{-t})W_{\\theta_tp}$ and $X'(t_0)=d(\\theta_{-t_0})(\\mathcal L_VW)_{\\theta_{t_0}p}$ (Prop 9.41).",
         body="Left-invariant fields on a Lie group are invariant under all left translations ([[Left-Invariant Vector Field]]); a field is invariant under its own flow ($[V,V]=0$). The shear field is not invariant under translation along $x$-flows of non-parallel fields.",
         used=[CH], related=["Lie Derivative of a Vector Field", "Commuting Vector Fields", "Flow of a Vector Field"]),
    dict(title="Commuting Vector Fields", aliases=["commuting flows", "[V,W]=0", "Theorem 9.44"], scope=[EB], by=BY,
         syl={EB: f"[[{LEE}#page=251|Lee Thm 9.44, p. 233]]."},
         intuition="Two vector fields commute when it does not matter in which order you flow along them.",
         key="$[V,W]=0$ iff $VWf=WVf$ for all $f$ iff **the flows commute**: $\\theta_t\\psi_s=\\psi_s\\theta_t$ (Thm 9.44; for non-complete fields wherever both sides are defined). In general $\\theta_t\\psi_s-\\psi_s\\theta_t\\approx-st[V,W]$; for $V=\\partial_x$, $W=x\\partial_y$ it is exactly $-st\\,\\partial_y$.",
         body="$E=x\\partial_x+y\\partial_y$ and $R=-y\\partial_x+x\\partial_y$ commute (dilations and rotations commute); $\\partial_x$ and $x\\partial_y$ do not. HW9 Q4: $[X,Y]=0\\iff\\exp tX\\exp sY=\\exp sY\\exp tX$ ([[DM14 One-Parameter Subgroups and the Exponential Map]]). Simultaneous straightening: [[Commuting Frame]].",
         used=[CH, "DM14 One-Parameter Subgroups and the Exponential Map"], related=["Lie Bracket of Vector Fields", "Invariant Vector Field", "Flow of a Vector Field", "Commuting Frame"]),
    dict(title="Commuting Frame", aliases=["holonomic frame", "coordinate frame criterion", "canonical form for commuting vector fields", "Theorem 9.46"], scope=[EB], by=BY,
         syl={EB: f"[[{LEE}#page=252|Lee Ex. 9.45, Thm 9.46, p. 234]]."},
         intuition="A frame that is secretly the coordinate frame of some chart: its brackets vanish.",
         key="$(E_i)$ with $[E_i,E_j]=0$. **Thm 9.46:** independent commuting $V_1,\\dots,V_k$ are $\\partial/\\partial s^1,\\dots,\\partial/\\partial s^k$ in some chart centred at each point (flowout along all flows at once). Hence **a frame is a coordinate frame iff it commutes.**",
         body="$(E,R)=(r\\partial_r,\\partial_\\theta)$ commute: log-polar coordinates $(\\log r,\\theta)$. The orthonormal polar frame $(\\partial_r,\\tfrac1r\\partial_\\theta)$ has $[\\cdot,\\cdot]=-\\tfrac1{r^2}\\partial_\\theta\\ne0$, so is not a coordinate frame. Obstruction for distributions: Frobenius ([[DM15 Closed Subgroups and the Lie Correspondence]]).",
         used=[CH], related=["Commuting Vector Fields", "Local Frame", "Flowout Theorem", "Regular and Singular Points"]),
]

if __name__ == "__main__":
    write("14-Differential-Geometry", "diff-geometry", ITEMS)
