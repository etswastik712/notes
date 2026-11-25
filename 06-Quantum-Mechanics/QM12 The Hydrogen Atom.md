---
title: QM12 The Hydrogen Atom
aliases: [QM12, hydrogen atom, Schrodinger equation in three dimensions, spherical harmonics, associated Legendre polynomials, hydrogen spectrum, radial wavefunctions, Bohr radius, L^2 and L_z]
subject: qm
type: chapter
chapter: 12
part: III
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
prereq: ["[[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]]", "[[QM01 From Waves to Probabilities]]"]
tags: [subject/qm, type/chapter, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# QM12 · The Hydrogen Atom

◀ [[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]] · [[Quantum Mechanics - Course Map|Course Map]] · next: [[QM13 The Probability Current and Ehrenfest Theorem]] · related: [[QM09 The Stern-Gerlach Experiment and Spin]] (angular momentum algebra, spin)

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map
> 🟢 **Taught:** the typed note [[Hydrogen_atom.pdf|Schrödinger equation in three dimensions: hydrogen atom]] (8 pp., 17 Nov; posted on Classroom 16 Nov 2026): natural scales by dimensional analysis (§1), spherical coordinates and the Laplacian (§2), $\hat L^2$, $\hat L_z$, $e^{im\varphi}$, associated Legendre polynomials, spherical harmonics (§3), the radial equation (§4), the spectrum and degeneracy (§5), radial wavefunctions and the radial probability density (§6). "You can follow the algebra in Griffiths to understand how the solution to this equation is obtained. Here we will simply discuss the main features."
> 🔵 **Extra · beyond (mine):** numbers (27.21 eV, 0.529 Å, spectral lines, reduced mass), normalisation checks that catch a slip in the notes' $R_{2,0}$, the peak of the 1s radial density (the notes' closing question, answered), $\langle r\rangle$, a finite-difference solution of the radial equation that recovers $-1/n^2$, the interactive tool. Numbers: `scripts/qm11_12_numbers.py`; figure: `scripts/fig_qm12.py`.

> [!key] After this chapter you can
> - build the hydrogen **energy scale** $m e^4/\hbar^2(4\pi\epsilon_0)^2=27.2$ eV and **length scale** $a=0.529$ Å from dimensional analysis,
> - write $\nabla^2$, $\hat L^2$ and $\hat L_z$ in spherical coordinates and show $[\hat H,\hat L^2]=[\hat H,\hat L_z]=0$ for a central potential,
> - derive $\Phi=e^{im\varphi}$, state that $\hat L^2$ has eigenvalues $\hbar^2l(l+1)$ with $Y_{lm}\propto P_l^m(\cos\theta)e^{im\varphi}$, $m=-l,\dots,l$,
> - write the **radial equation** with $\hbar^2l(l+1)/2mr^2$, state $E_n=-13.6\,\text{eV}/n^2$, $l=0,\dots,n-1$, degeneracy $n^2$,
> - normalise $R_{10},R_{20},R_{21}$ and find where the 1s **radial probability density** peaks ($r=a$).

> [!intuition] One sentence
> The Coulomb pull and the confinement cost set one natural size (the Bohr radius) and energy (13.6 eV); spherical symmetry splits the problem into angles, solved once and for all by the spherical harmonics, and a radial equation whose bound states, by a special property of $1/r$, depend only on $n$.

![[fig_qm12_hydrogen.png]]
*Figure QM12.1. A: the hydrogen levels $E_n=-13.6$ eV$/n^2$, drawn once per $l=0,\dots,n-1$ (all at the same energy: the $l$-degeneracy special to $1/r$); with $2l+1$ values of $m$ each, $n^2$ states. B: radial functions $R_{10},R_{20},R_{21},R_{30}$ (units $a^{-3/2}$): $R_{n0}$ is non-zero at the origin and has $n-1$ nodes; $R_{21}$ starts as $r$. C: radial probability densities $P(r)=r^2R^2$: the 1s peak sits at $r=a$, the 2p at $4a$; s-states have small inner bumps. `scripts/fig_qm12.py`.*

## 1. The natural scales
<span class="scope-taught">taught</span> *[[Hydrogen_atom.pdf#page=1|notes p.1]]*

$V(r)=-\dfrac{e^2}{4\pi\epsilon_0r}$. The parameters are $m_e$, $e^2/4\pi\epsilon_0$ (keep the $4\pi$: $\epsilon_0$ always appears with it here) and $\hbar$. The unique combinations with dimensions of energy and length:
$$\varepsilon=\frac{m_e}{\hbar^2}\Big(\frac{e^2}{4\pi\epsilon_0}\Big)^2=27.211\ \text{eV}=2\times13.606\ \text{eV},\qquad a=\frac{\hbar^2\,4\pi\epsilon_0}{m_ee^2}=0.52918\ \text{Å}.$$
The energy scale is **exactly twice the ionisation energy** of hydrogen; the length is the **Bohr radius**. (The same two numbers came out of the uncertainty-principle estimate in [[QM01 From Waves to Probabilities]] §6.)

> [!example]- 🔵 How to find the combination (extra · beyond)
> Write $\varepsilon=m^\alpha(e^2/4\pi\epsilon_0)^\beta\hbar^\gamma$ with $[e^2/4\pi\epsilon_0]=\text{J m}$, $[\hbar]=\text{J s}$, $[m]=\text{kg}=\text{J s}^2\text{m}^{-2}$. Matching J, m, s: $\alpha+\beta+\gamma=1$, $-2\alpha+\beta=0$, $2\alpha+\gamma=0$ → $\alpha=1,\beta=2,\gamma=-2$. For a length: $\alpha=-1,\beta=-1,\gamma=2$.

## 2. Spherical coordinates and the Laplacian
<span class="scope-taught">taught</span> *[[Hydrogen_atom.pdf#page=2|notes pp.1–3]]*

$r=\sqrt{x^2+y^2+z^2}$, $\theta=\cos^{-1}(z/r)$ (polar angle), $\varphi=\tan^{-1}(y/x)$ (azimuth); $x=r\sin\theta\cos\varphi$, $y=r\sin\theta\sin\varphi$, $z=r\cos\theta$. For a **central potential** $V(r)$ the TISE is $-\frac{\hbar^2}{2m}\nabla^2\psi+V(r)\psi=E\psi$ with
$$\nabla^2=\frac1{r^2}\frac{\partial}{\partial r}\Big(r^2\frac{\partial}{\partial r}\Big)+\frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\Big(\sin\theta\frac{\partial}{\partial\theta}\Big)+\frac{1}{r^2\sin^2\theta}\frac{\partial^2}{\partial\varphi^2}.$$
(The 3D analogue of [[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]] §2; the same Laplacian appears in electrostatics, [[ED01 Electrostatics - Review]].)

## 3. Angular momentum in 3D: $\hat L^2$, $\hat L_z$ and the spherical harmonics
<span class="scope-taught">taught</span> *[[Hydrogen_atom.pdf#page=2|notes pp.2–4]]*

Angular momentum is now a vector: its magnitude plus one component (conventionally $L_z$) specify it. Both
$$\hat L^2=-\hbar^2\Big[\frac1{\sin\theta}\frac{\partial}{\partial\theta}\Big(\sin\theta\frac{\partial}{\partial\theta}\Big)+\frac1{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2}\Big],\qquad \hat L_z=-i\hbar\frac{\partial}{\partial\varphi}$$
commute with $\hat H$ (and with each other; the three components do not commute among themselves: [[Angular Momentum Algebra]]). Comparing with §2, the angular part of $\nabla^2$ **is** $-\hat L^2/\hbar^2r^2$.

1. **$\varphi$**: eigenfunctions of $\hat L_z$ are $\Phi(\varphi)=e^{im\varphi}$, $m$ an integer (single-valued, as in 2D), eigenvalue $\hbar m$.
2. **$\theta$**: putting $\Phi$ into $\hat L^2\Theta\Phi=C\,\Theta\Phi$,
$$-\hbar^2\Big[\frac1{\sin\theta}\frac{d}{d\theta}\Big(\sin\theta\frac{d\Theta}{d\theta}\Big)-\frac{m^2}{\sin^2\theta}\Theta\Big]=C\,\Theta .$$
Well-behaved solutions on the whole sphere exist only for $C=\hbar^2l(l+1)$, $l=0,1,2,\dots$, with $|m|\le l$: the **associated Legendre polynomials** $P_l^m(\cos\theta)$. So **$\hat L^2$ has eigenvalues $\hbar^2l(l+1)$** and $\hat L_z$ has $\hbar m$, $m=-l,\dots,l$.

| $P_l^m(x)$, $x=\cos\theta$ | |
|---|---|
| $P_0^0=1$ | $P_1^0=x$, $P_1^1=-\sqrt{1-x^2}$ |
| $P_2^0=\tfrac12(3x^2-1)$ | $P_2^1=-3x\sqrt{1-x^2}$, $P_2^2=3(1-x^2)$ |

(The notes' table, with the Condon–Shortley sign; checked against `scipy.special.lpmv` at $x=0.3$.) The simultaneous eigenfunctions are the **spherical harmonics**
$$Y_{l,m}(\theta,\varphi)\propto P_l^m(\cos\theta)\,e^{im\varphi},$$
orthonormal (normalisation not worked out in the notes) and complete on the sphere.

> [!pitfall] $\sqrt{l(l+1)}\,\hbar$, not $l\hbar$
> The magnitude of $\vec L$ is $\hbar\sqrt{l(l+1)}$, larger than the largest $L_z=\hbar l$: the vector can never point exactly along $z$, because $L_x$ and $L_y$ cannot both vanish when $L_z$ is sharp ([[Angular Momentum Algebra]]). In 2D (QM11) there was only one component and the eigenvalue was simply $\hbar l$.

## 4. The radial equation
<span class="scope-taught">taught</span> *[[Hydrogen_atom.pdf#page=4|notes p.4]]*

Write $\hat H=-\dfrac{\hbar^2}{2m}\dfrac1{r^2}\dfrac{\partial}{\partial r}\Big(r^2\dfrac{\partial}{\partial r}\Big)+\dfrac{\hat L^2}{2mr^2}-\dfrac{e^2}{4\pi\epsilon_0r}$ and use $\hat L^2Y_{lm}=\hbar^2l(l+1)Y_{lm}$ with $\psi=R(r)Y_{lm}$:
$$\boxed{\Big[-\frac{\hbar^2}{2m}\Big(\frac{d^2}{dr^2}+\frac2r\frac{d}{dr}\Big)+\frac{\hbar^2l(l+1)}{2mr^2}-\frac{e^2}{4\pi\epsilon_0r}-E\Big]R(r)=0} .$$
Compared with 2D (QM11 §4), $\frac1r\to\frac2r$ and $l^2\to l(l+1)$. The **effective potential** $\frac{\hbar^2l(l+1)}{2mr^2}-\frac{e^2}{4\pi\epsilon_0r}$ has a centrifugal wall for $l\ge1$; with $u=rR$ the equation becomes a 1D Schrödinger equation for $u$ in that potential (the substitution Griffiths uses).

## 5. The spectrum
<span class="scope-taught">taught</span> *[[Hydrogen_atom.pdf#page=5|notes p.5]]*

Normalisable solutions exist only for
$$\boxed{E_n=-\frac{m e^4}{2(4\pi\epsilon_0)^2\hbar^2}\frac1{n^2}=-\frac{13.6\ \text{eV}}{n^2}},\qquad n=1,2,3,\dots$$
*Why only these energies* (the step the notes skip; Griffiths §4.2 does it in full). The mechanism is the oscillator's ([[QM06 The Oscillator Toolbox]] §4.1). For a bound state $E<0$, so far out the solution behaves as $e^{\pm\kappa r}$ with $\kappa=\sqrt{-2mE}/\hbar$. Normalisability keeps $e^{-\kappa r}$, and we write $u=rR=r^{l+1}e^{-\kappa r}\times(\text{power series})$. The recursion for the series coefficients makes it grow like $e^{2\kappa r}$, which would undo the decay, unless the series **stops**. It stops at degree $n_r$ only if $\kappa=1/(na)$ with $n=n_r+l+1$ a positive integer. Then $E=-\hbar^2\kappa^2/2m=-\hbar^2/(2ma^2n^2)$, which is the formula above. Energy quantisation is again "the equation plus the demand of a normalisable solution". The count $n=n_r+l+1$ is also why the radial node number is $n-l-1$.

- **Negative**: bound states.
- **No $l$ or $m$ in $E_n$**: for given $n$, $l=0,1,\dots,n-1$, and each $l$ has $2l+1$ values of $m$: degeneracy $\sum_{l=0}^{n-1}(2l+1)=\boxed{n^2}$ (spin not yet included; with it $2n^2$).
- The levels crowd together toward $E=0$ as $n\to\infty$ (Fig. QM12.1A; the notes' Figure 3).

> [!example] 🔵 Numbers (extra · beyond)
> $E_1=-13.606$, $E_2=-3.401$, $E_3=-1.512$, $E_4=-0.850$ eV. Lines: **Lyman α** ($2\to1$) 10.20 eV, 121.5 nm (UV); **Balmer α** ($3\to2$) 1.890 eV, **656.1 nm** (the red H-α line); Balmer β ($4\to2$) 2.551 eV, 486.0 nm. Using the electron–proton **reduced mass** instead of $m_e$ multiplies all energies by 0.999456: $E_1=-13.598$ eV. A finite-difference solution of §4's equation (units $\hbar=m_e=e^2/4\pi\epsilon_0=1$) gives $E=-0.49998,-0.12500,-0.05556$ Hartree for $l=0$, i.e. $n=1.000,2.000,3.000$, and the $l=1$ and $l=2$ ladders start at $n=2$ and $n=3$: the $l$-degeneracy found numerically.

> [!intuition] Why the $l$-degeneracy is special
> In a generic central potential (the 2D circular well of QM11, or a screened Coulomb potential in a many-electron atom) levels with the same number of nodes but different $l$ have **different** energies: the centrifugal wall pushes higher-$l$ states up. For the pure $1/r$ potential the extra symmetry of the Kepler problem (the conserved Runge–Lenz vector; *named from general knowledge, not in the notes*) makes $E$ depend on $n=n_r+l+1$ alone. This is why chemistry's $2s$ and $2p$ split only in multi-electron atoms.

## 6. Wavefunctions and the radial probability density
<span class="scope-taught">taught</span> *[[Hydrogen_atom.pdf#page=5|notes pp.5–8]]*

For allowed energies, with $a$ the Bohr radius:
$$\psi_{n,l,m}=N_{n,l}\,e^{-r/na}\Big(\frac{2r}{na}\Big)^lL^{2l+1}_{n-l-1}\Big(\frac{2r}{na}\Big)\,Y_{lm}(\theta,\varphi),$$
with $L^{p}_{q}$ the **associated Laguerre polynomials**; the exponential makes $\psi$ normalisable. The first radial functions:
$$R_{1,0}=2\,a^{-3/2}e^{-r/a},\qquad R_{2,0}=\frac1{\sqrt2}a^{-3/2}\Big(1-\frac r{2a}\Big)e^{-r/2a},\qquad R_{2,1}=\frac1{\sqrt{24}}a^{-3/2}\frac ra\,e^{-r/2a}.$$

> [!warning] [!verify] A factor of 2 in the notes' $R_{2,0}$ (Eq. 29)
> The notes print $R_{2,0}=\frac1{\sqrt2}\big(\frac1a\big)^{3/2}\big(2-\frac ra\big)e^{-r/2a}$ (checked on the page image). With $(2-r/a)$ this has $\int R^2r^2dr=4$, not 1; the normalised form is $\frac1{\sqrt2}a^{-3/2}(1-\frac r{2a})e^{-r/2a}=\frac{1}{2\sqrt2}a^{-3/2}(2-\frac ra)e^{-r/2a}$ (Griffiths' form). The notes' **plot** (Fig. 4) starts $R_{2,0}$ at $\approx0.7=1/\sqrt2$, i.e. it uses the correct normalisation: the slip is in the typed equation only. $R_{1,0}$ and $R_{2,1}$ as printed integrate to 1.

The probability density $|\psi_{nlm}|^2$ does not depend on $\varphi$ (since $|e^{im\varphi}|=1$). In a volume element $dV=r^2\sin\theta\,dr\,d\theta\,d\varphi$ the probability is $|\psi|^2r^2\sin\theta\,dr\,d\theta\,d\varphi$, and the shell probability (QM11 §7) is
$$P(r)=\int_0^{2\pi}\!\!d\varphi\int_0^\pi\!\sin\theta\,d\theta\,|\psi|^2r^2=r^2|R_{nl}(r)|^2\quad(\text{for normalised }Y_{lm}).$$

> [!example] The notes' question: where does the 1s radial density peak?
> $|R_{1,0}|^2$ is largest at $r=0$, but $P(r)=4\pi r^2|\psi_{100}|^2=r^2R_{10}^2=\frac{4}{a^3}r^2e^{-2r/a}$ vanishes at the nucleus. $\frac{dP}{dr}\propto\big(2r-\frac{2r^2}{a}\big)e^{-2r/a}=0$ gives $\boxed{r=a}$: **the most probable distance is the Bohr radius** (numerically 1.0000 a). The mean is larger, $\langle r\rangle=\tfrac32a$, because the tail is long. For 2p: peak $4a$, $\langle r\rangle=5a$; for 2s: outer peak $5.24a$, $\langle r\rangle=6a$, a node at $r=2a$.

Fig. 6 of the notes shows the familiar orbital density pictures (from Wikipedia). Patterns in Fig. 4 (the notes ask): at fixed $l$, increasing $n$ adds radial nodes ($n-l-1$) and spreads the function out ($\propto n^2a$); at fixed $n$, increasing $l$ removes nodes and pushes the function away from the origin ($\propto r^l$).

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Hydrogen radial wavefunctions and radial probability
> The hydrogen radial functions R_{nl}(r) ∝ e^{−r/na}(2r/na)^l L^{2l+1}_{n−l−1}(2r/na), normalised numerically so that ∫R² r² dr = 1, and the radial probability density P(r) = r² R² (the probability per unit radius of finding the electron in a thin shell).
>
> ![[qm_hydrogen_radial.png|720]]
>
> **Try:** n = 1, l = 0: R is largest at r = 0 but P(r) peaks at r = a (the notes' question) and ⟨r⟩ = 1.5 a. n = 2, l = 1: P peaks at 4 a. Compare n = 3 with l = 0, 1, 2: the same energy (−1.51 eV) but 2, 1, 0 radial nodes.
>
> [▶ Open the tool in your browser](../Assets/interactive/qm_hydrogen_radial.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/qm_hydrogen_radial.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How QM12 connects
> **Builds on:** [[QM11 Two-Dimensional Problems Angular Momentum and the Circular Well]] (separation, centrifugal term, radial density), [[QM01 From Waves to Probabilities]] §6 (the uncertainty estimate of $a$ and 13.6 eV), [[QM09 The Stern-Gerlach Experiment and Spin]] (angular-momentum algebra, spin and the $2n^2$).
> **Concepts:** [[Spherical Harmonics]] · [[Associated Legendre Polynomials]] · [[Hydrogen Atom Spectrum]] · [[Bohr Radius and Atomic Units]] · [[Radial Probability Density]] · [[Centrifugal Barrier]] · [[Laplacian in Polar and Spherical Coordinates]] · [[Angular Momentum Algebra]] · [[Hydrogen Atom Stability]] · [[Hydrogen 21 cm Line]]
> **Other subjects:** [[ED01 Electrostatics - Review]] (Legendre expansions of potentials) · [[Inorganic Chemistry - Course Map]] (s, p, d orbitals, the shapes behind VSEPR, MO and crystal-field theory) · [[Partition Function of the Hydrogen Atom]] (statistical mechanics of the $n^2$ levels) · [[CL07 Optical Properties of the Atmosphere]] (line spectra)

## Summary
> [!summary] Cheat-sheet
> - Scales: $\frac{m}{\hbar^2}(\frac{e^2}{4\pi\epsilon_0})^2=27.21$ eV $=2\times13.6$ eV; $a=\frac{4\pi\epsilon_0\hbar^2}{me^2}=0.529$ Å.
> - $\hat L^2=-\hbar^2[\frac1{\sin\theta}\partial_\theta\sin\theta\partial_\theta+\frac1{\sin^2\theta}\partial_\varphi^2]$, $\hat L_z=-i\hbar\partial_\varphi$; eigenvalues $\hbar^2l(l+1)$, $\hbar m$, $|m|\le l$; $Y_{lm}\propto P_l^m(\cos\theta)e^{im\varphi}$.
> - Radial: $-\frac{\hbar^2}{2m}(R''+\frac2rR')+[\frac{\hbar^2l(l+1)}{2mr^2}-\frac{e^2}{4\pi\epsilon_0r}]R=ER$.
> - $E_n=-13.6/n^2$ eV; $l=0..n-1$; degeneracy $n^2$ ($2n^2$ with spin). Lyman α 121.5 nm, H-α 656 nm.
> - $R_{10}=2a^{-3/2}e^{-r/a}$; $R_{20}=\frac1{\sqrt2}a^{-3/2}(1-\frac r{2a})e^{-r/2a}$ (notes' Eq. 29 off by 2); $R_{21}=\frac1{\sqrt{24}}a^{-3/2}\frac rae^{-r/2a}$.
> - $P(r)=r^2R^2$; 1s peaks at $r=a$, $\langle r\rangle=1.5a$.

## Practice
1. Show that $m e^4/\hbar^2(4\pi\epsilon_0)^2$ has units of energy and evaluate it in eV.
2. Show that the angular part of $\nabla^2$ equals $-\hat L^2/\hbar^2r^2$, and hence that $[\hat H,\hat L^2]=0$ for any $V(r)$.
3. Check that $Y\propto P_1^0(\cos\theta)=\cos\theta$ satisfies $\hat L^2Y=2\hbar^2Y$.
4. How many states (with spin) have $n=3$? List the $(l,m)$ values.
5. Find the wavelength of the $n=4\to n=2$ line and say which colour it is.
6. Normalise $R(r)=Ae^{-r/a}$ with $\int|R|^2r^2dr=1$.
7. Show that $P(r)$ for 2p peaks at $r=4a$.
8. For the 1s state, find the probability that the electron is farther than $2a$ from the nucleus.
9. What is $\langle V\rangle$ for 1s? Use $\langle1/r\rangle=1/a$ and compare with $E_1$ (virial theorem: $\langle T\rangle=-E$).
10. Why do 2s and 2p have the same energy in hydrogen but not in lithium?

> [!example]- Solutions
> 1. $[e^2/4\pi\epsilon_0]^2=\text{J}^2\text{m}^2$, $[m/\hbar^2]=\text{kg}/\text{J}^2\text{s}^2$: product $\text{kg m}^2/\text{s}^2=\text{J}$. 27.21 eV.
> 2. Compare the $\theta,\varphi$ terms of $\nabla^2$ with $\hat L^2$; $\hat L^2$ acts only on angles, $V(r)$ and the radial operator only on $r$.
> 3. $\frac1{\sin\theta}\frac{d}{d\theta}(\sin\theta\cdot(-\sin\theta))=\frac{-2\sin\theta\cos\theta}{\sin\theta}=-2\cos\theta$ → $\hat L^2Y=2\hbar^2Y$, $l=1$.
> 4. $2n^2=18$: $l=0$ ($m=0$), $l=1$ ($m=-1,0,1$), $l=2$ ($m=-2..2$): 9 orbitals × 2 spins.
> 5. 486.0 nm (Balmer β), blue-green.
> 6. $A^2\int_0^\infty e^{-2r/a}r^2dr=A^2\cdot2(a/2)^3=A^2a^3/4=1$ → $A=2a^{-3/2}$ (= $R_{10}$).
> 7. $P\propto r^4e^{-r/a}$; $\frac{d}{dr}=0$: $4r^3-r^4/a=0$ → $r=4a$.
> 8. $\int_{2a}^\infty\frac{4}{a^3}r^2e^{-2r/a}dr=e^{-4}(1+4+8)=13e^{-4}=0.238$.
> 9. $\langle V\rangle=-\frac{e^2}{4\pi\epsilon_0}\langle1/r\rangle=-27.2$ eV $=2E_1$; $\langle T\rangle=+13.6$ eV.
> 10. §5 intuition: the pure $1/r$ potential's extra symmetry; in lithium, inner electrons screen the nucleus and the 2s electron penetrates closer, so it is more tightly bound than 2p.

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (6): the other tool's concept notes from the lectures, unreviewed
> [[zettel/associated-legendre-polynomials|Associated Legendre Polynomials]] · [[zettel/hydrogen-atom-radial-equation|Hydrogen Atom Radial Equation]] · [[zettel/hydrogen-atom-radial-wavefunctions|Hydrogen Atom Radial Wavefunctions]] · [[zettel/hydrogen-ground-state-scale-from-uncertainty|Hydrogen Ground-State Scale from Uncertainty]] · [[zettel/hydrogen-spectrum-and-degeneracy|Hydrogen Spectrum and Degeneracy]] · [[zettel/spherical-harmonics|Spherical Harmonics]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | dimensional analysis, scales | [[Hydrogen_atom.pdf#page=1\|notes p.1]] | taught |
> | spherical coordinates, Laplacian | [[Hydrogen_atom.pdf#page=2\|pp.1–3]] | taught |
> | $\hat L^2$, $\hat L_z$, $e^{im\varphi}$, Legendre, $P_l^m$ table, $Y_{lm}$ | [[Hydrogen_atom.pdf#page=3\|pp.3–4]] | taught |
> | radial equation | [[Hydrogen_atom.pdf#page=4\|p.4]] | taught |
> | $E_n$, degeneracy, Laguerre form, $R_{10},R_{20},R_{21}$, $P(r)$, the 1s question | [[Hydrogen_atom.pdf#page=5\|pp.5–8]] (text layer; p.6 equations checked on the page image) | taught |
> | numbers, lines, reduced mass, normalisation checks, FD solution, peak and $\langle r\rangle$, Practice | `scripts/qm11_12_numbers.py`, `scripts/fig_qm12.py` | extra/beyond |
>
> **Notes.** (1) [!verify] Eq. 29's $R_{2,0}$ prefactor (see §6). (2) The notes are dated 17 November 2025 (last year's date). (3) The notes defer the radial solution to Griffiths; Griffiths was not read for this chapter (the vault's copies are under `physics/quantum-mechanics/books/`). (4) The shared drive holds CH1213's *H-atom Part 1/2* lectures (centre-of-mass reduction, radial equation): listed in [[physics/quantum-mechanics/shared-drive-sources|shared-drive sources]], not read here. (5) The Runge–Lenz remark and the lithium screening argument are general knowledge, labelled.
