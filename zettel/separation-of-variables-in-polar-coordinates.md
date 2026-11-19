---
id: zettel/separation-of-variables-in-polar-coordinates
aliases: ["Separation of Variables in Polar Coordinates", "polar separation of variables"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Separation of Variables in Polar Coordinates

The factorization of the two-dimensional spatial wavefunction into an independent radial component and an angular component.

$$\psi(r, \theta) = R(r)\Theta(\theta)$$

$$-\frac{\hbar^2}{2m} \left( \frac{1}{R}\frac{d^2 R}{dr^2} + \frac{1}{rR}\frac{dR}{dr} \right) - \frac{\hbar^2}{2mr^2 \Theta}\frac{d^2 \Theta}{d\theta^2} = E$$

## Links

---
Source: Angular_momentum, pp. 1–3

<!-- kurooto:seen -->
- needs:: [[zettel/two-dimensional-schrodinger-equation-in-polar-coordinates]] — The separation of variables in polar coordinates starts from the 2D Schrödinger equation written in (r, θ), which the candidate note derives via the chain rule before the factorization ψ = R(r)Θ(θ) can be applied
- example-of:: [[zettel/two-dimensional-harmonic-oscillator-in-polar-coordinates]] — The separation method is applied to the circularly symmetric oscillator potential V(r) = (1/2)mω²r², yielding Θ(θ) = e^{ilθ} and a radial equation for R(r), which is a concrete instance of the separation
- example-of:: [[zettel/circular-infinite-well-energy-eigenvalues-and-eigenstates]] — The circular infinite well's stationary states are obtained by separating ψ = R(r)Θ(θ) and solving the radial equation with Bessel functions, so this note shows the separation carried through to quantised eigenvalues
- used-in:: [[zettel/associated-legendre-polynomials]] — Separating the angular part of the 3D problem produces the polar-angle equation whose bounded solutions are the associated Legendre polynomials, the same separation logic applied one dimension up
- generalises:: [[zettel/hydrogen-atom-radial-equation]] — The hydrogen radial equation arises from the same radial/angular factorization of the Schrödinger equation, extended to three dimensions with a Coulomb potential and centrifugal term
## Seen in
- [[ph2113/2026-11-16-tutorial-vii-polar-schrodinger-2d-oscillator|Angular_momentum]] pp. 1–3
<!-- /kurooto:seen -->
