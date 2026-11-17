---
id: ph2113/2026-11-16-hydrogen-atom-3d-notes
aliases: [Hydrogen atom, Schrödinger equation in three dimensions]
tags: [ph2113, lecture-notes]
trust_tier: agent_written
---

# Schrödinger equation in three dimensions: the hydrogen atom

## Covered
(Classroom: Hydrogen_atom.pdf, posted 2026-11-16.)

**Natural scales by dimensional analysis.** $V(r)=-\dfrac{e^2}{4\pi\epsilon_0r}$ with parameters $m_e$, $e$, $4\pi\epsilon_0$, $\hbar$. The combination $\dfrac{m}{\hbar^2}\Big(\dfrac{e^2}{4\pi\epsilon_0}\Big)^2$ has units of energy and equals $2\times13.6$ eV (twice the ionisation energy); $\dfrac{\hbar^2}{m}\dfrac{4\pi\epsilon_0}{e^2}$ is a length equal to the Bohr radius $0.529\times10^{-10}$ m.

**Spherical polar coordinates.** $r=\sqrt{x^2+y^2+z^2}$, $\theta=\cos^{-1}(z/r)$, $\varphi=\tan^{-1}(y/x)$; $x=r\sin\theta\cos\varphi$, $y=r\sin\theta\sin\varphi$, $z=r\cos\theta$. For a central potential, $-\frac{\hbar^2}{2m}\nabla^2\psi+V(r)\psi=E\psi$ with
$$\nabla^2=\frac1{r^2}\partial_r\big(r^2\partial_r\big)+\frac1{r^2\sin\theta}\partial_\theta\big(\sin\theta\,\partial_\theta\big)+\frac1{r^2\sin^2\theta}\partial_\varphi^2 .$$

**Angular momentum in 3-d.** Two operators commute with $\hat H$: $\hat L^2$ and $\hat L_z$,
$$\hat L^2=-\hbar^2\Big[\frac1{\sin\theta}\partial_\theta(\sin\theta\,\partial_\theta)+\frac1{\sin^2\theta}\partial_\varphi^2\Big],\qquad \hat L_z=-i\hbar\,\partial_\varphi .$$
- $\hat L_z$ eigenfunctions: $\Phi(\varphi)=e^{im\varphi}$, $m$ an integer, eigenvalue $\hbar m$.
- Then $\hat L^2\Theta=C\Theta$ reduces to a $\theta$-equation with $m^2/\sin^2\theta$; its solutions are the associated Legendre functions $P_l^m(\cos\theta)$ when $C=\hbar^2l(l+1)$, $l$ an integer, $m=-l,\dots,l$. So $\hat L^2$ has eigenvalues $\hbar^2l(l+1)$.
- First few: $P_0^0=1$, $P_1^0=x$, $P_1^1=-\sqrt{1-x^2}$, $P_2^0=\tfrac12(3x^2-1)$, $P_2^1=-3x\sqrt{1-x^2}$, $P_2^2=3(1-x^2)$ (with $x=\cos\theta$).
- Simultaneous eigenstates of $\hat L^2$ and $\hat L_z$: spherical harmonics $Y_{l,m}\propto P_l^m(\cos\theta)e^{im\varphi}$; orthonormal and complete on the sphere (normalisation not worked out).

**Radial equation.** Using $\hat L^2Y_{l,m}=\hbar^2l(l+1)Y_{l,m}$ in $\hat H=-\frac{\hbar^2}{2m}\frac1{r^2}\partial_r(r^2\partial_r)+\frac{\hat L^2}{2mr^2}-\frac{e^2}{4\pi\epsilon_0r}$,
$$\Big[-\frac{\hbar^2}{2m}\Big(\frac{d^2}{dr^2}+\frac2r\frac d{dr}\Big)+\frac{\hbar^2l(l+1)}{2mr^2}-\frac{e^2}{4\pi\epsilon_0r}-E\Big]R(r)=0 .$$
The algebra of the solution is left to Griffiths; the main features are:
- Normalisable solutions exist only for $E_n=-\dfrac{me^4}{2(4\pi\epsilon_0)^2\hbar^2}\dfrac1{n^2}$, $n=1,2,3,\dots$ (negative: bound states; levels crowd together as $n$ grows).
- $E$ does not depend explicitly on $l$ or $m$. For given $n$, $l=0,\dots,n-1$, and each $l$ has $m=-l,\dots,l$, so the degeneracy is $n^2$ (spin not yet included).
- $\psi_{n,l,m}=N_{n,l}\,e^{-r/na}\Big(\dfrac{2r}{na}\Big)^lL^{2l+1}_{n-l-1}(2r/na)\,Y_l^m(\theta,\varphi)$, with $a$ the Bohr radius and $L$ an associated Laguerre polynomial; the exponential makes it normalisable.
- First radial functions as printed: $R_{1,0}=2a^{-3/2}e^{-r/a}$; $R_{2,0}=\dfrac1{\sqrt2}a^{-3/2}\big(2-\tfrac ra\big)e^{-r/2a}$; $R_{2,1}=\dfrac1{\sqrt{24}}a^{-3/2}\dfrac ra\,e^{-r/2a}$. The sheet asks what pattern appears as $n$ rises at fixed $l$ and as $l$ rises at fixed $n$.

**Probability density.** $|\psi|^2$ of any eigenstate is independent of $\varphi$. Volume element $dV=r^2\sin\theta\,dr\,d\theta\,d\varphi$; the shell probability $P(r)=\int_0^{2\pi}d\varphi\int_0^\pi\sin\theta\,d\theta\,|\psi|^2r^2$. For the spherically symmetric 1s state $P(r)\,dr=4\pi r^2|R_{1,0}|^2dr$: $R_{1,0}$ peaks at $r=0$ but $P(r)$ peaks at a finite $r$ because of the $r^2$ factor. The sheet asks: at which $r$ does it peak? (not answered in the sheet; for $P\propto r^2e^{-2r/a}$ setting $dP/dr=0$ gives $r=a$, derived here, not stated in the sheet.)

## From the post
Notes and python notebook for this week and last.

## Files
- [Hydrogen_atom.pdf](https://drive.google.com/file/d/1AAknDP-m4PAEKBy6g8f25xqebbvbTRJG/view?usp=drive_web) (read in full; figures not extracted)

## Doubts
- The printed $R_{2,0}$ has prefactor $1/\sqrt2$ together with $(2-r/a)$. With that factor $\int_0^\infty R_{2,0}^2r^2dr=4$, not 1; the normalised function is $\frac1{\sqrt2}a^{-3/2}(1-\tfrac r{2a})e^{-r/2a}$, equivalently $\frac1{2\sqrt2}a^{-3/2}(2-\tfrac ra)e^{-r/2a}$ (checked by direct integration). Possibly a typo in the sheet or in the text extraction; check the PDF.

## Related
- [[ph2113/2026-11-16-angular-momentum-2d-handwritten-notes]]: the 2-d version of the same separation ($e^{il\theta}$, radial equation)
- [[ph2113/2026-11-16-tutorial-vii-polar-schrodinger-2d-oscillator]]: Problem 3 derives $P(r)=4\pi r^2|\psi|^2$ used here
- [[ph2113/2026-08-18-wavefunction-to-uncertainty]]: the hydrogen-size estimate from the uncertainty principle
- [[06-quantum-mechanics/concepts/angular-momentum-algebra]]: their own concept note on angular momentum
- [[06-quantum-mechanics/concepts/hydrogen-atom-stability]]: their own concept note on hydrogen stability
