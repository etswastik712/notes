---
id: ph2113/2026-11-02-tutorial-v-finite-well-double-well-transmission
aliases: [Tutorial V PH2113]
tags: [ph2113, tutorial, finite-well, scattering]
trust_tier: agent_written
---

# Tutorial V: finite well, double well, transmission over a well

## Covered
Three-problem tutorial sheet (Classroom: Tutorial5.pdf). Notation on this sheet: well $-a<x<a$ with $V=0$ inside and $V=V_0$ outside; $k_0=\sqrt{2mE}/\hbar$ is the wave number *inside* the well and $k=\sqrt{2m(E-V_0)}/\hbar$ the wave number *outside* when $E>V_0$. (Tutorial IV used $k$ for the outside decay constant when $E<V_0$, so check which is meant.)

**Problem 1: bound states of the finite well.**
- Sketch the first three bound-state eigenfunctions of the well $V=0$ for $-a<x<a$, $V=V_0$ elsewhere.
- Find the minimum $V_0a^2$ for which these three bound states exist.
- Practises: even/odd parity of states, decaying tails outside, number of nodes, and the existence condition for bound states from the quantisation conditions in [[ph2113/2026-10-27-finite-well-notes]] ($\tan k_0a=\kappa/k_0$ even, $\cot k_0a=-\kappa/k_0$ odd, with $\kappa^2+k_0^2=2mV_0/\hbar^2$). Solution not posted. Derived from those conditions (not posted, check): the states are even, odd, even, and the third appears when $z_0=\sqrt{2mV_0a^2}/\hbar$ exceeds $\pi$, so $V_0a^2>\pi^2\hbar^2/2m$.

**Problem 2: double well.**
- Potential: two wells of width $w$ separated by a barrier of width $d$, with height $V_0$ (figure in the PDF).
- Sketch the ground state $\psi_0(x)$ for (a) $d\ll w$ and (b) $d\gg w$.
- Practises: how a thin or thick barrier changes the overlap of the two wells' tails, symmetric (nodeless) ground state; compare with Tutorial I Problem 4-5 results on parity and the nodeless ground state ([[ph2113/2026-10-06-tutorial-i-particle-in-a-box]]).

**Problem 3: scattering over the well, $E>V_0$.**
Wavefunctions as derived in class (Classroom: Tutorial5.pdf, eqs. 1-3):
$$\psi_I=Ae^{ikx}+Be^{-ikx}\ (x<-a),\quad \psi_{II}=Ce^{ik_0x}+De^{-ik_0x}\ (-a<x<a),\quad \psi_{III}=Fe^{ikx}\ (x>a).$$
Continuity of $\psi$ and $\psi'$ at $x=\pm a$ gives (eqs. 4-7):
- $Ae^{-ika}+Be^{ika}=Ce^{-ik_0a}+De^{ik_0a}$
- $ik(Ae^{-ika}-Be^{ika})=ik_0(Ce^{-ik_0a}-De^{ik_0a})$
- $Ce^{ik_0a}+De^{-ik_0a}=Fe^{ika}$
- $ik_0(Ce^{ik_0a}-De^{-ik_0a})=ikFe^{ika}$

Tasks:
1. Eliminate $B,C,D$ to get
$$\frac FA=\frac{4kk_0\,e^{-2ika}}{(k+k_0)^2e^{-2ik_0a}-(k-k_0)^2e^{2ik_0a}}.\quad(8)$$
2. Show that $T=|F/A|^2$ is
$$T=\frac{1}{1+\dfrac{V_0^2}{4E(E-V_0)}\sin^2\!\Big(\dfrac{2a}{\hbar}\sqrt{2mE}\Big)}.\quad(9)$$
3. Sketch $\psi$ in regions I and III for one finite $E>V_0$ with $T=1$ and another with $T<1$.

Practises: elimination from a linear system, $|F/A|^2$ algebra, $T=1$ when $\sin(2k_0a)=0$ (resonances, $2k_0a=n\pi$: width a whole number of half-wavelengths), and reflection ($T<1$) giving a standing-wave pattern in region I as $A$ and $B$ interfere. Consistency check (derived): $(k^2-k_0^2)^2/4k^2k_0^2=V_0^2/4E(E-V_0)$ because $k^2-k_0^2=-2mV_0/\hbar^2$ and $k^2k_0^2=4m^2E(E-V_0)/\hbar^4$, so (9) is the same formula as the one in [[ph2113/2026-10-27-finite-well-notes]]. Region III has only $e^{ikx}$ (pure transmitted wave), so $|\psi_{III}|^2$ is constant; region I has $|\psi_I|^2$ oscillating unless $B=0$.

## From the post
This week's tutorial questions.

## Files
- [Tutorial5.pdf](https://drive.google.com/file/d/1YaTOVRlMm9HFWrdzOUyOUNAXkJKaVkO0/view?usp=drive_web): text read in full; the double-well figure was not extracted (only its labels $V_0$, $w$, $d$), so the exact well/barrier layout is taken from the problem text. Post: https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODk3MDY5MTIxNDM2

## Related
- [[ph2113/2026-10-27-finite-well-notes]]: the bound-state conditions and scattering result this sheet builds on
- [[ph2113/2026-10-26-tutorial-iv-finite-well-practice]]: previous finite-well tutorial (even-state condition, $k/k_0$ shape)
- [[ph2113/2026-10-06-particle-in-a-box-notes]]: infinite-well limit and node counting
- [[ph2113/2026-10-06-tutorial-i-particle-in-a-box]]: parity of eigenfunctions and nodeless ground state
- [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]]: continuity of $\psi,\psi'$ at finite jumps in $V$
