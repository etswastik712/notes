---
id: ph2113/2026-11-16-tutorial-vii-polar-schrodinger-2d-oscillator
aliases: [Tutorial VII]
tags: [ph2113, tutorial]
trust_tier: agent_written
---

# Tutorial VII: Schrödinger equation in polar coordinates, 2-d oscillator, radial probability density

## Covered
Three problems (Classroom: tutorial7.pdf, posted 2026-11-16).

**Polar coordinates.** $r=\sqrt{x^2+y^2}$, $\theta=\tan^{-1}(y/x)$; conversely $x=r\cos\theta$, $y=r\sin\theta$.

**Problem 1: Schrödinger equation in 2-d polar coordinates.** Show that
$$-\frac{\hbar^2}{2m}\left[\frac{\partial^2\psi}{\partial r^2}+\frac1r\frac{\partial\psi}{\partial r}+\frac1{r^2}\frac{\partial^2\psi}{\partial\theta^2}\right]+V(r,\theta)\psi=E\psi .$$
Method given: chain rule, e.g. $\partial_x\psi=\partial_r\psi\,\partial_xr+\partial_\theta\psi\,\partial_x\theta$, and the same for the second derivatives, using the four coordinate relations above.

**Problem 2: 2-d simple harmonic oscillator.** $V(x,y)=\tfrac12m\omega^2(x^2+y^2)=\tfrac12m\omega^2r^2$, so it has circular symmetry. The angular part is an eigenfunction of the angular momentum operator, $\Theta(\theta)=e^{il\theta}$ with $l$ an integer. Show that the radial equation is
$$\frac{d^2R}{dr^2}+\frac1r\frac{dR}{dr}+\left[\frac{2m}{\hbar^2}\Big(E-\tfrac12m\omega^2r^2\Big)-\frac{l^2}{r^2}\right]R=0 .$$
(The bracket is written from the dimensionally consistent form; the sheet's extracted text puts $l^2/r^2$ inside the $2m/\hbar^2$ bracket, which would not be dimensionally consistent, so check the PDF.) The solutions are Laguerre polynomials; solving is not required (look them up in Mathematica or similar). Footnote: the 2-d oscillator can also be solved with the 1-d ladder operators by introducing two sets, $\hat a_\pm^x$ and $\hat a_\pm^y$.

**Problem 3: radial probability density.** $|\psi(r,\theta)|^2$ is the probability density; the radial density is the probability of finding the particle in a thin shell of radius $r$ and thickness $dr$. Show
- 2-d: $P(r)=\int_0^{2\pi}|\psi(r,\theta)|^2\,r\,d\theta$,
- 3-d: $P(r)=\int_0^\pi\!\int_0^{2\pi}|\psi(r,\theta,\varphi)|^2\,r^2\sin\theta\,d\theta\,d\varphi$,
- if $\psi$ is independent of the angles: $P(r)=2\pi r|\psi(r)|^2$ (2-d) and $P(r)=4\pi r^2|\psi(r)|^2$ (3-d).

What each practises: Problem 1, chain rule and second derivatives in a coordinate change; Problem 2, separation of variables with a circularly symmetric potential and the role of $e^{il\theta}$; Problem 3, the area/volume element ($r\,dr\,d\theta$, $r^2\sin\theta\,dr\,d\theta\,d\varphi$) behind the radial density. No solutions posted.

## From the post
Tutorial for this week.

## Files
- [tutorial7.pdf](https://drive.google.com/file/d/1Gy3ewB3wDgssdn_jLcq_KpwouR-d2BV-/view?usp=drive_web) (read in full; saved as ph2113/2026-11-17-tutorial7-1Gy3ew.pdf)

## Related
- [[ph2113/2026-11-16-angular-momentum-2d-handwritten-notes]]: the lecture derivation of the same polar-coordinate equation and $e^{il\theta}$
- [[ph2113/2026-11-16-circular-well-2d-and-density-notebook]]: the same radial equation solved for the circular well (Bessel functions)
- [[ph2113/2026-11-16-hydrogen-atom-3d-notes]]: the 3-d radial probability density $4\pi r^2|\psi|^2$ for the 1s state
- [[ph2113/2026-10-19-harmonic-oscillator-ladder-operator-notes]]: the 1-d oscillator and ladder operators that the footnote extends to 2-d
- [[ph2113/2026-10-19-tutorial-iii-harmonic-oscillator-expectation-values]]: earlier oscillator tutorial

<!-- kurooto:materiale4639def -->
## Concepts in tutorial7
[[zettel/two-dimensional-schrodinger-equation-in-polar-coordinates]], [[zettel/two-dimensional-harmonic-oscillator-in-polar-coordinates]], [[zettel/radial-probability-density]]
<!-- /kurooto:materiale4639def -->

<!-- kurooto:material553a7731 -->
## Concepts in Angular_momentum
[[zettel/circular-infinite-well-potential-in-two-dimensions]], [[zettel/separation-of-variables-in-polar-coordinates]], [[zettel/circular-infinite-well-energy-eigenvalues-and-eigenstates]]
<!-- /kurooto:material553a7731 -->
