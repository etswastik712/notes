"""Concept notes for DM12 (Integral Curves, Flows and Flowouts).  .venv/bin/python -W ignore scripts/spec_dm12.py"""
from mkconcept import write

LEE = "John M. Lee - Introduction to Smooth Manifolds.pdf"
CH = "DM12 Integral Curves, Flows and Flowouts"
MT = "mt3184-differential-geometry-and-lie-groups"
T, EB = "taught", "extra-book"
BY = ["lecture-notes", "book"]

ITEMS = [
    dict(title="Integral Curve", aliases=["integral curves", "maximal integral curve", "trajectory", "orbit curve"], scope=[T, EB], by=BY,
         syl={T: f"slides DG21–DG22 via [[{MT}/2026-10-10-october-5-9|Oct 5–9]] and [[{MT}/2026-10-16-october-12-16|Oct 12–16]] notes; HW7 Q4–Q5, HW8 Q1.", EB: f"[[{LEE}#page=225|Lee Prop. 9.2, p. 207]], [[{LEE}#page=226|Lee Prop. 9.6, p. 208]]."},
         intuition="The path of a particle that always moves with the velocity the vector field prescribes at its current location.",
         key="$\\gamma:J\\to M$ with $\\gamma'(t)=V_{\\gamma(t)}$, an ODE $\\dot x^i=V^i(x)$ in a chart. Exists and is unique through each point (Prop 9.2). $\\gamma(at)$ is an integral curve of $aV$; $F\\circ\\gamma$ is an integral curve of $Y$ if $X\\sim_FY$ (Prop 9.6). A maximal integral curve is **constant, injective or periodic**.",
         body="$V=-y\\partial_x+x\\partial_y$: rotation, period $2\\pi$. $V=y\\partial_x+\\partial_y$: $(x_0+y_0t+t^2/2,\\,y_0+t)$. $x^2\\partial_x$: $x_0/(1-x_0t)$, escapes in finite time. Left-invariant field on $GL(n)$ through $X_0$: $X_0e^{tA}$ ([[DM14 One-Parameter Subgroups and the Exponential Map]]). Existence theory: [[PA14 ODE Existence Uniqueness and Smooth Dependence]].",
         used=[CH], related=["Flow of a Vector Field", "Complete Vector Field", "Vector Field", "Regular and Singular Points"]),
    dict(title="Flow of a Vector Field", aliases=["flow", "maximal flow", "Fundamental Theorem on Flows", "Theorem 9.12", "infinitesimal generator", "flow domain", "one-parameter group of diffeomorphisms"], scope=[T, EB], by=BY,
         syl={T: f"slides DG21–DG22 via [[{MT}/2026-10-10-october-5-9|Oct 5–9 note]].", EB: f"[[{LEE}#page=230|Lee Thm 9.12, p. 212]], [[{LEE}#page=233|Lee Prop. 9.13, p. 215]]."},
         intuition="Let every point move along its integral curve for time $t$: the result is a diffeomorphism $\\theta_t$, and $t\\mapsto\\theta_t$ is a homomorphism from $(\\mathbb R,+)$ into the diffeomorphism group.",
         key="Every $V$ has a unique smooth **maximal flow** $\\theta:\\mathcal D\\to M$ ($\\mathcal D$ open, $\\mathcal D^{(p)}$ intervals): $\\theta^{(p)}$ is the maximal integral curve from $p$; $\\mathcal D^{(\\theta(s,p))}=\\mathcal D^{(p)}-s$; $\\theta_t:M_t\\to M_{-t}$ diffeo with $\\theta_s\\theta_t=\\theta_{s+t}$. A global flow is a smooth $\\mathbb R$-action ([[Smooth Action]]); its generator is $V_p=\\partial_t\\theta|_{t=0}$. Naturality: $X\\sim_FY\\Rightarrow\\eta_t\\circ F=F\\circ\\theta_t$.",
         body="Flow of $y\\partial_x+\\partial_y$ maps the unit square to parallelograms of equal area. Irrational flow on $T^2$: flow of $\\partial_x+\\sqrt2\\partial_y$ (dense orbits). Smoothness of $\\theta$ is smooth dependence of ODE solutions. The derivative of $\\theta_t$ along itself defines $\\mathcal L_VW$ ([[DM13 Lie Derivatives and Commuting Vector Fields]]).",
         used=[CH, "DM13 Lie Derivatives and Commuting Vector Fields", "DM14 One-Parameter Subgroups and the Exponential Map"], related=["Integral Curve", "Complete Vector Field", "Smooth Action", "Vector Field"]),
    dict(title="Complete Vector Field", aliases=["complete", "Uniform Time Lemma", "global flow", "compactly supported vector field is complete", "Theorem 9.16"], scope=[T, EB], by=BY,
         syl={T: f"slides DG22–DG23 via [[{MT}/2026-10-16-october-12-16|Oct 12–16 note]]; HW8 Q2.", EB: f"[[{LEE}#page=234|Lee Lemma 9.15, Thm 9.16, Thm 9.18, p. 216]]."},
         intuition="A field whose particles never escape to infinity in finite time, so the flow exists for all time.",
         key="$\\mathcal D=\\mathbb R\\times M$. **Uniform Time Lemma:** if $(-\\varepsilon,\\varepsilon)\\subseteq\\mathcal D^{(p)}$ for all $p$ then $V$ is complete. Hence: compactly supported fields are complete (HW8 Q2); on a compact manifold every field is complete; **every left-invariant field on a Lie group is complete** (Thm 9.18).",
         body="Complete: $x\\partial_x$, translations, rotation field, $\\sin x\\,\\partial_x$, left-invariant $\\tilde A$ on $GL(n)$. Not complete: $x^2\\partial_x$ (blow-up at $1/x_0$), $\\partial_x$ on $\\mathbb R^2\\setminus\\{0\\}$ (hole). Detection of incompleteness: [[Escape Lemma]].",
         used=[CH, "DM14 One-Parameter Subgroups and the Exponential Map"], related=["Flow of a Vector Field", "Escape Lemma", "Left-Invariant Vector Field", "Integral Curve"]),
    dict(title="Escape Lemma", aliases=["Lemma 9.19", "escape to infinity in finite time"], scope=[T, EB], by=BY,
         syl={T: f"HW8 Q3 via [[{MT}/2026-10-16-hw8|HW8]].", EB: f"[[{LEE}#page=235|Lee Lemma 9.19, p. 217]]."},
         intuition="A maximal integral curve that stops at a finite time must have run out of every compact set: it cannot be caught in a bounded region.",
         key="If $\\gamma:J\\to M$ is a maximal integral curve with $b=\\sup J<\\infty$ then for every $t_0\\in J$ the set $\\gamma([t_0,b))$ is **not** contained in any compact subset of $M$. (Otherwise a uniform time $\\varepsilon$ on the compact set would extend $\\gamma$ past $b$.)",
         body="$x^2\\partial_x$ from $x_0=2$: $x\\to\\infty$ as $t\\to\\tfrac12$. The same idea gives Thm 9.16: bounded support $\\Rightarrow$ complete. Compare the ODE statement in [[PA14 ODE Existence Uniqueness and Smooth Dependence]].",
         used=[CH], related=["Complete Vector Field", "Integral Curve", "Flow of a Vector Field"]),
    dict(title="Regular and Singular Points", aliases=["singular point", "regular point", "equilibrium point", "canonical form near a regular point", "flow box", "Theorem 9.22", "straightening a vector field"], scope=[T, EB], by=BY,
         syl={T: f"slide DG24 via [[{MT}/2026-10-16-october-12-16|Oct 12–16 note]]; HW7 Q4, Q6.", EB: f"[[{LEE}#page=237|Lee Prop. 9.21, p. 219]], [[{LEE}#page=238|Lee Thm 9.22, p. 220]]."},
         intuition="Where the field vanishes nothing moves; where it does not, the flow lines are locally parallel straight lines.",
         key="$p$ singular if $V_p=0$: then $\\theta^{(p)}\\equiv p$ (equilibrium). $p$ regular: $\\theta^{(p)}$ is an immersion (Prop 9.21). **Canonical form (Thm 9.22):** near a regular point there are coordinates with $V=\\partial/\\partial s^1$ (and $S=\\{s^1=0\\}$ for any transverse hypersurface $S$). A maximal curve is constant, injective or periodic.",
         body="HW7 Q6: with $V$ nowhere zero on a compact $M$, $\\theta_t$ ($t>0$ small) is homotopic to the identity and fixed-point free, proved with a flow-box chart. Polar coordinates are the canonical form of $-y\\partial_x+x\\partial_y$. The first non-trivial local invariants appear for several fields ([[DM13 Lie Derivatives and Commuting Vector Fields]]).",
         used=[CH], related=["Flowout Theorem", "Integral Curve", "Vector Field", "Flow of a Vector Field"]),
    dict(title="Flowout Theorem", aliases=["flowout", "Theorem 9.20", "flow out of a submanifold"], scope=[T, EB], by=BY,
         syl={T: f"slides DG22–DG23 via [[{MT}/2026-10-16-october-12-16|Oct 12–16 note]]; HW8 Q4.", EB: f"[[{LEE}#page=235|Lee Thm 9.20, p. 217]]."},
         intuition="Push a submanifold along a transverse vector field: the swept-out set is a submanifold one dimension higher.",
         key="$S$ embedded, $V$ nowhere tangent to $S$, $\\Phi=\\theta|_{\\mathbb R\\times S}$. (a) $\\Phi$ is an immersion; (b) $\\partial_t\\sim_\\Phi V$; (c) injective on $|t|<\\delta(p)$ for a smooth $\\delta>0$ (partition of unity), so $\\Phi(\\mathcal O_\\delta)$ is an immersed $(\\dim S+1)$-submanifold containing $S$, tangent to $V$; (d) codimension $1$: a diffeomorphism onto an open set. For compact $S$ a uniform $\\varepsilon$ gives an embedding (HW8 Q4).",
         body="Polar coordinates: $S$ = positive $x$-axis, $W=-y\\partial_x+x\\partial_y$, $\\Phi(t,s)=(s\\cos t,s\\sin t)$ ($\\det=-s$). Helicoid: $S$ = half-axis in $\\mathbb R^3$, $V$ helical, $\\Phi(t,s)=(s\\cos t,s\\sin t,t)$ (immersion with $\\sigma_{\\min}(d\\Phi)=1$). Proves the canonical form near a regular point and underlies Frobenius ([[DM15 Closed Subgroups and the Lie Correspondence]]).",
         used=[CH, "DM15 Closed Subgroups and the Lie Correspondence"], related=["Regular and Singular Points", "Flow of a Vector Field", "Immersion and Submersion", "Embedded Submanifold"]),
]

if __name__ == "__main__":
    write("14-Differential-Geometry", "diff-geometry", ITEMS)
