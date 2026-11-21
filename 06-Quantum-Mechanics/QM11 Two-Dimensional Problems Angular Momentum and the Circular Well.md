---
title: QM11 Two-Dimensional Problems Angular Momentum and the Circular Well
aliases: [QM11, two-dimensional Schrodinger equation, 2D TISE, angular momentum in 2D, L_z, circular well, circular infinite well, Bessel well, Tutorial VII, 2D harmonic oscillator, radial probability density]
subject: qm
type: chapter
chapter: 11
part: III
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
prereq: ["[[QM04 The Particle in a Box]]", "[[QM05 The Harmonic Oscillator]]", "[[QM03 States Operators and Measurement]]"]
tags: [subject/qm, type/chapter, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# QM11 · Two-Dimensional Problems, Angular Momentum and the Circular Well

◀ [[QM10 The Finite Barrier and Tutorial V]] · [[Quantum Mechanics - Course Map|Course Map]] · next: [[QM12 The Hydrogen Atom]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map
> 🟢 **Taught** (all posted on Classroom on 16 Nov 2026, "notes and python notebook for this week and last"):
> - the handwritten lecture [[Angular_momentum.pdf#page=2|Angular_momentum.pdf]] (6 pp., p.1 blank): 2D commutators, the 2D TISE, the polar form, $\hat L=-i\hbar\,\partial_\phi$, $[\hat H,\hat L]=0$ for $V(r)$, $e^{il\phi}$ with integer $l$, the radial equation, the $\pm l$ degeneracy → §1–§4;
> - the typed note [[Angular_momentum (2).pdf|Schrödinger equation in two dimensions: an example]] (3 pp., 17 Nov): the **circular infinite well**, Bessel functions, $E=\hbar^2k_{n,l}^2/2m$ → §5;
> - the notebook `circular_well_density.ipynb` (normalisation, rings vs lobes, energy-level diagram; read, not run) → §5.3;
> - [[tutorial7.pdf|Tutorial VII]] (polar Laplacian, the 2D oscillator, radial probability density) → §6–§7, all solved.
>
> 🔵 **Extra · beyond (mine):** the 2D oscillator spectrum $E=\hbar\omega(2n_r+|l|+1)$ and its $N+1$ degeneracy (the tutorial says "you need not solve"), a symbolic check of the polar Laplacian, the normalisation and the $\cos l\theta$ superpositions, comparisons with the square box, the interactive tool. All numbers: `scripts/qm11_12_numbers.py`; figures: `scripts/fig_qm11.py`.
>
> **Notation.** The handwritten notes use $\phi$ for the polar angle; the typed note and Tutorial VII use $\theta$. Below, $\phi$ in §1–§4 and $\theta$ from §5 on, as in each source; they are the same angle.

> [!key] After this chapter you can
> - write the 2D TISE in Cartesian and **polar** coordinates and derive the polar Laplacian by the chain rule (Tutorial VII Q1),
> - show $\hat L_z=x\hat p_y-y\hat p_x=-i\hbar\,\partial_\phi$, that it commutes with $\hat H$ for a circular potential, and that **single-valuedness** forces $l\in\mathbb Z$,
> - separate $\psi=R(r)e^{il\phi}$ and write the **radial equation** with its centrifugal term $\hbar^2l^2/2mr^2$; explain the $\pm l$ degeneracy,
> - solve the **circular infinite well**: $R=J_l(kr)$, $k_{n,l}a=j_{l,n}$, $E_{n,l}=\hbar^2j_{l,n}^2/2ma^2$; list the first levels,
> - get the radial equation of the **2D oscillator** and its spectrum, and use the **radial probability density** $P(r)=\int|\psi|^2r\,d\theta$ (2D), $\int|\psi|^2r^2\sin\theta\,d\theta d\varphi$ (3D).

> [!intuition] One sentence
> When a potential depends only on distance, rotating the system changes nothing, so angular momentum is conserved and every state can be labelled by how many times its phase winds around the centre ($e^{il\phi}$, $l$ an integer); what is left is a one-dimensional radial problem with an extra centrifugal wall $\hbar^2l^2/2mr^2$.

![[fig_qm11_circular_well.png]]
*Figure QM11.1. A: Bessel functions $J_0$–$J_3$; the circular-well condition $J_l(ka)=0$ picks out their zeros (dots, first zeros labelled). B: the spectrum in units of $\hbar^2/2ma^2$; levels with $l\ne0$ are doubly degenerate ($\pm l$). C: the $L_z$ eigenstate $n=2,l=1$ has a rotationally symmetric density (a ring, because $|e^{i\theta}|^2=1$). D: the same energy in the standing-wave form $\cos\theta$ shows 2 lobes. E: $n=1,l=3$ as $\cos3\theta$: 6 lobes. `scripts/fig_qm11.py`.*

## 1. The Schrödinger equation in two dimensions
<span class="scope-taught">taught</span> *[[Angular_momentum.pdf#page=2|Angular_momentum.pdf p.2]]*

The canonical commutators generalise component by component ([[Canonical Commutation Relation]]):
$$[\hat x,\hat p_x]=i\hbar,\quad[\hat y,\hat p_y]=i\hbar,\qquad [\hat x,\hat p_y]=0,\quad[\hat x,\hat y]=0 .$$
The first is non-zero because $x\,\partial_xf$ and $\partial_x(xf)$ differ; $x$ and $\partial_y$ simply do not interact. The TISE in 2D is
$$\Big[-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial y^2}+V(x,y)\Big]\psi=E\psi
\quad\Longleftrightarrow\quad\Big[\frac{\hat p_x^2}{2m}+\frac{\hat p_y^2}{2m}+V\Big]\psi=E\psi .$$
Now suppose the potential has **circular symmetry**: $V(x,y)=V(\sqrt{x^2+y^2})=V(r)$.

## 2. Polar coordinates (Tutorial VII Q1)
<span class="scope-taught">taught</span> *[[Angular_momentum.pdf#page=3|pp.3–4]]; [[tutorial7.pdf|Tutorial VII]] Q1*

$r=\sqrt{x^2+y^2}$, $\phi=\tan^{-1}(y/x)$; $x=r\cos\phi$, $y=r\sin\phi$. The four derivatives the lecture boxes:
$$\frac{\partial r}{\partial x}=\cos\phi,\quad\frac{\partial r}{\partial y}=\sin\phi,\quad\frac{\partial\phi}{\partial x}=-\frac{\sin\phi}{r},\quad\frac{\partial\phi}{\partial y}=\frac{\cos\phi}{r}.$$

> [!example]- Derivation of the polar Laplacian (Tutorial VII Q1, written out)
> By the chain rule, $\partial_x=\cos\phi\,\partial_r-\frac{\sin\phi}{r}\partial_\phi$ and $\partial_y=\sin\phi\,\partial_r+\frac{\cos\phi}{r}\partial_\phi$. Apply $\partial_x$ twice (the lecture's p.3), keeping track of the derivatives that act on the coefficients $\cos\phi$, $\sin\phi/r$:
> $$\partial_x^2\psi=\cos^2\!\phi\,\psi_{rr}-\frac{2\sin\phi\cos\phi}{r}\psi_{r\phi}+\frac{\sin^2\!\phi}{r}\psi_r+\frac{2\sin\phi\cos\phi}{r^2}\psi_\phi+\frac{\sin^2\!\phi}{r^2}\psi_{\phi\phi}.$$
> Likewise
> $$\partial_y^2\psi=\sin^2\!\phi\,\psi_{rr}+\frac{2\sin\phi\cos\phi}{r}\psi_{r\phi}+\frac{\cos^2\!\phi}{r}\psi_r-\frac{2\sin\phi\cos\phi}{r^2}\psi_\phi+\frac{\cos^2\!\phi}{r^2}\psi_{\phi\phi}.$$
> Add: the mixed terms and the $\psi_\phi$ terms cancel and $\sin^2+\cos^2=1$:
> $$\boxed{\nabla^2\psi=\frac{\partial^2\psi}{\partial r^2}+\frac1r\frac{\partial\psi}{\partial r}+\frac1{r^2}\frac{\partial^2\psi}{\partial\phi^2}}\qquad\Rightarrow\qquad -\frac{\hbar^2}{2m}\Big(\psi_{rr}+\frac1r\psi_r+\frac1{r^2}\psi_{\phi\phi}\Big)+V(r,\phi)\psi=E\psi .$$
> Checked symbolically (sympy) on three test functions: zero difference from $\partial_x^2+\partial_y^2$. *(On the lecture's p.3 the last two terms are written with $\theta$ for $\phi$ — the same angle.)*

## 3. Angular momentum in two dimensions
<span class="scope-taught">taught</span> *[[Angular_momentum.pdf#page=4|pp.4–5]]*

Classically $L=\vec r\times\vec p=m\,\vec r\times\vec v$, whose only component in the plane problem is $L=xp_y-yp_x$. Quantum mechanically
$$\hat L=\hat x\hat p_y-\hat y\hat p_x=-i\hbar\Big(x\frac{\partial}{\partial y}-y\frac{\partial}{\partial x}\Big)=-i\hbar\frac{\partial}{\partial\phi}.$$
(The last step: $x\partial_y-y\partial_x=r\cos\phi(\sin\phi\,\partial_r+\tfrac{\cos\phi}{r}\partial_\phi)-r\sin\phi(\cos\phi\,\partial_r-\tfrac{\sin\phi}{r}\partial_\phi)=\partial_\phi$; also checked symbolically.)

Since $V$ depends only on $r$ and the only $\phi$ in $\hat H$ is $\partial_\phi^2$, which commutes with $\partial_\phi$:
$$[\hat H,\hat L]=0 .$$
**Commuting operators have simultaneous eigenfunctions** ([[Commutator]]): find the eigenfunctions of $\hat L$ and they can also be chosen as eigenfunctions of $\hat H$. Let $\hat L\psi_l=A\psi_l$:
$$-i\hbar\,\partial_\phi\psi_l=A\psi_l\ \Rightarrow\ \partial_\phi\psi_l=\frac{iA}{\hbar}\psi_l\equiv il\,\psi_l\ \Rightarrow\ \psi_l(r,\phi)=R(r)\,e^{il\phi}.$$
**Quantisation from geometry**: $\phi\to\phi+2\pi$ is the same point, so the wavefunction must be unchanged: $e^{2\pi il}=1$, hence
$$l=0,\pm1,\pm2,\dots,\qquad \Phi_l(\phi)=\frac{1}{\sqrt{2\pi}}e^{il\phi},\qquad \hat L\Phi_l=\hbar l\,\Phi_l .$$
This is the [[Particle on a Ring]] result again, now as the angular part of every circular problem.

## 4. The radial equation and the ±l degeneracy
<span class="scope-taught">taught</span> *[[Angular_momentum.pdf#page=6|p.6]]*

Substitute $\psi=R(r)\Phi(\phi)$: $\partial_\phi^2\Phi=-l^2\Phi$, so
$$\boxed{\Big[-\frac{\hbar^2}{2m}\Big(\frac{d^2}{dr^2}+\frac1r\frac{d}{dr}-\frac{l^2}{r^2}\Big)+V(r)\Big]R(r)=E\,R(r)} .$$
"Have to solve this equation to get the energy eigenvalues and overall eigenfunction." Two general facts follow without solving it:

- **Degeneracy**: $l$ enters only as $l^2$, so **$+l$ and $-l$ have the same energy, irrespective of the details** of $V(r)$ (the lecture's boxed remark): a particle circulating clockwise or anticlockwise. Every $l\ne0$ level is at least doubly degenerate ([[Degeneracy]]).
- **The centrifugal barrier** $\hbar^2l^2/2mr^2$ acts as an extra repulsive potential that keeps $l\ne0$ states away from the origin ($R\propto r^{|l|}$ near $r=0$); the classical analogue is $L^2/2mr^2$ in the effective potential of central-force motion ([[CM04 Central Forces and Effective One-Dimensional Motion]]).

## 5. The circular infinite well
<span class="scope-taught">taught</span> *[[Angular_momentum (2).pdf|the typed note]] (3 pp.); `circular_well_density.ipynb`*

$V=0$ for $r<a$, $\infty$ outside. Inside, with $E=\hbar^2k^2/2m$, the radial equation becomes **Bessel's equation**
$$R''+\frac1rR'+\Big(k^2-\frac{l^2}{r^2}\Big)R=0\quad\Longrightarrow\quad R(r)=A\,J_l(kr)+B\,Y_l(kr).$$
($J_l$, $Y_l$: Bessel functions of the first and second kind; "you will encounter them in Math Methods II, Optics, and other higher courses".) **Boundary conditions**: finite at $r=0$ kills $Y_l$ (it diverges), $B=0$; $\psi(a)=0$ needs $J_l(ka)=0$:
$$k_{n,l}=\frac{j_{l,n}}{a},\qquad \boxed{E_{n,l}=\frac{\hbar^2k_{n,l}^2}{2m}=\frac{\hbar^2}{2ma^2}\,j_{l,n}^2},\qquad \psi_{n,l}=N_{n,l}\,J_l(k_{n,l}r)\,e^{il\theta},$$
where $j_{l,n}$ is the $n$-th zero of $J_l$; $n-1$ is the number of radial nodes inside the well.

### 5.1 The spectrum
<span class="scope-extra-beyond">extra · beyond</span> *zeros from `scipy.special.jn_zeros`*

| order | $(n,l)$ | $j_{l,n}$ | $E/(\hbar^2/2ma^2)$ | degeneracy |
|---|---|---|---|---|
| 1 | (1,0) | 2.4048 | 5.783 | 1 |
| 2 | (1,1) | 3.8317 | 14.682 | 2 |
| 3 | (1,2) | 5.1356 | 26.375 | 2 |
| 4 | (2,0) | 5.5201 | 30.471 | 1 |
| 5 | (1,3) | 6.3802 | 40.706 | 2 |
| 6 | (2,1) | 7.0156 | 49.218 | 2 |
| 7 | (1,4) | 7.5883 | 57.583 | 2 |
| 8 | (2,2) | 8.4172 | 70.850 | 2 |
| 9 | (3,0) | 8.6537 | 74.887 | 1 |

Unlike the 1D box, the levels are **not** in simple ratios: $E_{1,1}/E_{1,0}=2.539$, $E_{2,0}/E_{1,0}=5.27$. A comparison: a square box of the same **area** ($\pi a^2$, side $\sqrt\pi a$) has ground energy $2\pi^2/\pi=6.283$ in the same units, slightly above the disc's 5.783 — for a given area the disc confines least (it has no corners).

### 5.2 Normalisation
<span class="scope-taught">taught</span> *the notebook*

With $\int_0^aJ_l^2(kr)\,r\,dr=\tfrac{a^2}{2}J_{l+1}^2(ka)$ when $J_l(ka)=0$, and the angular integral $2\pi$:
$$|N_{n,l}|^2=\frac{1}{\pi a^2\,J_{l+1}^2(j_{l,n})}.$$
(Checked by quadrature for $(1,0),(2,1),(1,3)$: 1.000000.) The ground state has $|\psi(0)|^2=1.181/a^2$.

### 5.3 Rings or lobes?
<span class="scope-taught">taught</span> *the notebook's "note on θ-dependence"*

For an $L_z$ eigenstate $|e^{il\theta}|^2=1$, so the probability density is **circularly symmetric**: **rings**, not lobes (Fig. QM11.1C). Because $+l$ and $-l$ are degenerate, the combinations $\sqrt2\cos l\theta$ and $\sqrt2\sin l\theta$ are equally good **energy** eigenstates (but not $L_z$ eigenstates); they show $2l$ angular lobes (Fig. D, E). Which form is "the" state depends on which other observable you also want sharp: $\hat L_z$ (rings), or a reflection symmetry (lobes). The typed note points to the Wolfram demonstration *Particle in an Infinite Circular Well* for live pictures; the interactive tool below does the same.

## 6. The 2D harmonic oscillator (Tutorial VII Q2)
<span class="scope-taught">taught</span> *[[tutorial7.pdf|Tutorial VII]] Q2* · <span class="scope-extra-beyond">extra · beyond</span> *the spectrum*

$V=\tfrac12m\omega^2(x^2+y^2)=\tfrac12m\omega^2r^2$ is circular, so $\Theta=e^{il\theta}$ with $l\in\mathbb Z$, and §4's radial equation with this $V$, divided by $-\hbar^2/2m$, is exactly the tutorial's Eq. (8):
$$\frac{d^2R}{dr^2}+\frac1r\frac{dR}{dr}+\Big[\frac{2m}{\hbar^2}\Big(E-\tfrac12m\omega^2r^2\Big)-\frac{l^2}{r^2}\Big]R=0 .$$
The solutions are (associated) Laguerre polynomials times a Gaussian; the tutorial does not ask for them.

> [!example]- 🔵 The spectrum, two ways (extra · beyond)
> **Cartesian.** $\hat H=\hat H_x+\hat H_y$, two independent 1D oscillators ([[QM05 The Harmonic Oscillator]]): $E=\hbar\omega(n_x+n_y+1)=\hbar\omega(N+1)$. The number of pairs with $n_x+n_y=N$ is **$N+1$**: the degeneracy grows linearly (1, 2, 3, 4, 5 counted). This is the tutorial's footnote, two sets of ladder operators $\hat a^x_\pm,\hat a^y_\pm$ ([[Isotropic Oscillator and Degeneracy]], [[Schwinger Oscillator Model]]).
> **Polar.** The radial equation gives $E=\hbar\omega(2n_r+|l|+1)$, $n_r=0,1,2,\dots$ radial nodes. For $N=2n_r+|l|$ the allowed $l$ are $N,N-2,\dots,-N$: again $N+1$ states. Numerically (flux-conservative finite differences, $\hbar=m=\omega=1$): $l=0$: 1.0000, 3.0000, 4.9999; $l=\pm1$: 2.0000, 4.0000, 5.9999; $l=\pm2$: 3.0000, 5.0000, 6.9999.
> **Why both counts agree:** $N=1$ has $l=\pm1$ (the circular combinations $x\pm iy$ of the Cartesian $(1,0)$ and $(0,1)$); $N=2$ has $l=0,\pm2$.

## 7. Radial probability density (Tutorial VII Q3)
<span class="scope-taught">taught</span> *[[tutorial7.pdf|Tutorial VII]] Q3; the same idea in [[QM12 The Hydrogen Atom]] §6*

$|\psi|^2$ is a density **per unit area** (2D) or **volume** (3D). The probability of finding the particle in a thin shell between $r$ and $r+dr$ adds up all area (volume) elements in that shell:
- **2D**: the element is $dA=r\,dr\,d\theta$, so $P(r)\,dr=dr\int_0^{2\pi}|\psi(r,\theta)|^2\,r\,d\theta$, i.e. $\boxed{P(r)=\int_0^{2\pi}|\psi|^2r\,d\theta}$.
- **3D**: $dV=r^2\sin\theta\,dr\,d\theta\,d\varphi$, so $\boxed{P(r)=\int_0^\pi\!\!\int_0^{2\pi}|\psi|^2r^2\sin\theta\,d\theta\,d\varphi}$.
- If $\psi$ depends only on $r$, the angular integrals give the circumference and surface area: $P(r)=2\pi r|\psi(r)|^2$ (2D), $P(r)=4\pi r^2|\psi(r)|^2$ (3D).

> [!example] The 2D oscillator ground state
> $\psi_0=\pi^{-1/2}e^{-r^2/2}$ (units $\hbar=m=\omega=1$): $|\psi_0|^2$ is largest at $r=0$, but $P(r)=2\pi r|\psi_0|^2=2re^{-r^2}$ vanishes there (no area at the centre), integrates to 1 and **peaks at $r=1/\sqrt2=0.7071$**. "Most likely position" ≠ "most likely distance". The 3D analogue for hydrogen's 1s state is the question at the end of the hydrogen notes ([[QM12 The Hydrogen Atom]] §6).

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Particle in a circular infinite well
> The 2D well V = 0 for r < a, ∞ outside.
>
> ![[qm_circular_well.png|720]]
>
> **Try:** n = 1, l = 0 is the ground state (j = 2.405, E = 5.783 ħ²/2ma²). Step to n = 2, l = 1 and toggle 'cos lθ': the same energy (49.22) shows a ring or two lobes. n = 1, l = 3 gives six lobes; n counts radial nodes + 1.
>
> [▶ Open the tool in your browser](../Assets/interactive/qm_circular_well.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/qm_circular_well.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How QM11 connects
> **Builds on:** [[QM04 The Particle in a Box]] (boundary conditions quantise), [[QM05 The Harmonic Oscillator]] (1D oscillator, ladders), [[QM02 The Schrodinger Equation and Stationary States]] (particle on a ring), [[QM03 States Operators and Measurement]] (commuting observables). **Next:** [[QM12 The Hydrogen Atom]].
> **Concepts:** [[Laplacian in Polar and Spherical Coordinates]] · [[Circular Infinite Well]] · [[Bessel Functions]] · [[Centrifugal Barrier]] · [[Radial Probability Density]] · [[Particle on a Ring]] · [[Isotropic Oscillator and Degeneracy]] · [[Degeneracy]] · [[Commutator]]
> **Other subjects:** [[CM04 Central Forces and Effective One-Dimensional Motion]] (classical $L^2/2mr^2$) · [[Waves - Course Map]] (vibrating membranes: the same Bessel modes) · [[Group Theory - Course Map]] (rotations SO(2), $e^{il\phi}$ as its irreducible representations)

## Summary
> [!summary] Cheat-sheet
> - 2D: $[\hat x,\hat p_x]=[\hat y,\hat p_y]=i\hbar$, cross commutators 0. $\nabla^2=\partial_r^2+\tfrac1r\partial_r+\tfrac1{r^2}\partial_\phi^2$.
> - $\hat L=x\hat p_y-y\hat p_x=-i\hbar\partial_\phi$; $V=V(r)\Rightarrow[\hat H,\hat L]=0$; $\Phi_l=e^{il\phi}/\sqrt{2\pi}$, $l\in\mathbb Z$ (single-valued), eigenvalue $\hbar l$.
> - Radial: $-\frac{\hbar^2}{2m}(R''+\frac1rR'-\frac{l^2}{r^2}R)+VR=ER$; $\pm l$ degenerate; centrifugal $\hbar^2l^2/2mr^2$.
> - Circular well: $R=J_l(kr)$, $J_l(ka)=0$, $E=\hbar^2j_{l,n}^2/2ma^2$: 5.783, 14.682 (×2), 26.375 (×2), 30.471 …; $|N|^2=1/\pi a^2J_{l+1}^2(j_{l,n})$; $e^{il\theta}$ rings, $\cos l\theta$ lobes.
> - 2D oscillator: $E=\hbar\omega(2n_r+|l|+1)=\hbar\omega(N+1)$, degeneracy $N+1$.
> - $P(r)=2\pi r|\psi|^2$ (2D), $4\pi r^2|\psi|^2$ (3D) for angle-independent $\psi$.

## Practice
1. Show $[\hat x,\hat p_x]=i\hbar$ and $[\hat x,\hat p_y]=0$ by acting on a test function $f(x,y)$.
2. Derive $\partial\phi/\partial x=-\sin\phi/r$ from $\phi=\tan^{-1}(y/x)$.
3. Verify the polar Laplacian on $\psi=x^2-y^2$ (it should give 0 both ways; what are its $r,\phi$ form and its $l$ content?).
4. Show directly that $[\hat L,\hat H]=0$ for $V=V(r)$ but not for $V=\tfrac12m\omega^2(x^2+4y^2)$.
5. A particle on a ring of radius $a$ ($r$ fixed): from §4, show $E_l=\hbar^2l^2/2ma^2$.
6. Circular well with $a=1$ nm, electron. Find $E_{1,0}$ and $E_{1,1}$ in eV and the wavelength of the photon emitted in $1,1\to1,0$.
7. How many states (counting $\pm l$) lie below $E=60\,\hbar^2/2ma^2$ in the circular well?
8. 2D oscillator: list all $(n_r,l)$ with $E=4\hbar\omega$ and check the degeneracy against $(n_x,n_y)$.
9. For $\psi=R(r)$ in 2D, show $\int_0^\infty P(r)dr=1$ is the same as $\int|\psi|^2dA=1$.
10. **Tutorial VII** — all three questions are solved in §2, §6, §7; redo them without looking.

> [!example]- Solutions
> 1. $[\hat x,\hat p_x]f=-i\hbar(x\partial_xf-\partial_x(xf))=i\hbar f$; $[\hat x,\hat p_y]f=-i\hbar(x\partial_yf-\partial_y(xf))=0$.
> 2. $\partial_x\tan^{-1}(y/x)=\frac{1}{1+y^2/x^2}\cdot(-y/x^2)=-y/(x^2+y^2)=-\sin\phi/r$.
> 3. $x^2-y^2=r^2\cos2\phi$: $\psi_{rr}+\psi_r/r+\psi_{\phi\phi}/r^2=2\cos2\phi+2\cos2\phi-4\cos2\phi=0$. Content $l=\pm2$ ($\cos2\phi=\tfrac12(e^{2i\phi}+e^{-2i\phi})$).
> 4. For $V(r)$ only $\partial_\phi^2$ carries $\phi$; $[\partial_\phi,V(r)]=0$. For the anisotropic case $V=\tfrac12m\omega^2r^2(\cos^2\phi+4\sin^2\phi)$ depends on $\phi$: $[\hat L,V]=-i\hbar\,\partial_\phi V\ne0$.
> 5. With $r=a$ fixed, $R$ is constant: only $\frac{\hbar^2l^2}{2ma^2}$ remains. ([[Particle on a Ring]].)
> 6. $\hbar^2/2m_ea^2=0.0381$ eV for $a=1$ nm: $E_{1,0}=0.2203$ eV, $E_{1,1}=0.5593$ eV; $\Delta E=0.339$ eV, $\lambda=hc/\Delta E=3.66$ μm.
> 7. Levels below 60: (1,0) 1, (1,1) 2, (1,2) 2, (2,0) 1, (1,3) 2, (2,1) 2, (1,4) 2 → **12 states**.
> 8. $N=3$: $(n_r,l)=(0,\pm3),(1,\pm1)$ → 4 states; Cartesian $(3,0),(2,1),(1,2),(0,3)$ → 4. ✓
> 9. $\int|\psi|^2dA=\int_0^\infty\!\int_0^{2\pi}|R|^2r\,d\theta\,dr=\int_0^\infty2\pi r|R|^2dr=\int P\,dr$.

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (9): the other tool's concept notes from the lectures, unreviewed
> [[zettel/angular-wavefunction-representations-in-circular-wells|Angular Wavefunction Representations in Circular Wells]] · [[zettel/circular-infinite-well-energy-eigenvalues-and-eigenstates|Circular Infinite Well Energy Eigenvalues and Eigenstates]] · [[zettel/circular-infinite-well-potential-in-two-dimensions|Circular Infinite Well Potential in Two Dimensions]] · [[zettel/circular-well-normalization-constant|Circular Well Normalization Constant]] · [[zettel/radial-probability-density|Radial Probability Density]] · [[zettel/separation-of-variables-in-polar-coordinates|Separation of Variables in Polar Coordinates]] · [[zettel/two-dimensional-harmonic-oscillator-in-polar-coordinates|Two-Dimensional Harmonic Oscillator in Polar Coordinates]] · [[zettel/two-dimensional-quantum-state|Two-Dimensional Quantum State]] · [[zettel/two-dimensional-schrodinger-equation-in-polar-coordinates|Two-Dimensional Schrödinger Equation in Polar Coordinates]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | 2D commutators, TISE, circular symmetry | [[Angular_momentum.pdf#page=2\|Angular_momentum.pdf p.2]] (handwritten, read as images; p.1 blank) | taught |
> | chain rule, polar Laplacian | [[Angular_momentum.pdf#page=3\|pp.3–4]]; [[tutorial7.pdf\|Tutorial VII]] Q1 | taught |
> | $\hat L$, $[\hat H,\hat L]=0$, $e^{il\phi}$, $l\in\mathbb Z$, radial equation, $\pm l$ degeneracy | [[Angular_momentum.pdf#page=4\|pp.4–6]] | taught |
> | circular well, Bessel, $E=\hbar^2k_{n,l}^2/2m$ | [[Angular_momentum (2).pdf]] (typed, 17 Nov) | taught |
> | normalisation, rings vs lobes, energy diagram | `circular_well_density.ipynb` (cells read as text; **not executed**: downloaded code) | taught |
> | 2D oscillator radial equation, radial probability density | [[tutorial7.pdf\|Tutorial VII]] Q2–Q3 | taught |
> | spectrum table, area comparison, 2D oscillator spectrum and degeneracy, symbolic checks, $P(r)$ peak | `scripts/qm11_12_numbers.py`, `scripts/fig_qm11.py` | extra/beyond |
>
> **Notes.** (1) The two PDFs posted on 16 Nov are both named `Angular_momentum.pdf` on Drive (different files); the second is stored as `Angular_momentum (2).pdf` by the Classroom sync. (2) Tutorial VII is dated 12 November **2025** on the sheet (last year's date left in the header); the typed notes are dated 17 November 2025 likewise. (3) The handwritten p.3 writes $\theta$ in two terms where $\phi$ is meant. (4) The shared drive has CH1213's *Particle on a sphere* and *Eigen functions for box and ring* lectures ([[physics/quantum-mechanics/shared-drive-sources|shared-drive sources]]): not read for this chapter.
