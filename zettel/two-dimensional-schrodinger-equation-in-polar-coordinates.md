---
id: zettel/two-dimensional-schrodinger-equation-in-polar-coordinates
aliases: ["Two-Dimensional Schrödinger Equation in Polar Coordinates", "2D Schrödinger equation in polar coordinates", "polar Schrödinger equation"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Two-Dimensional Schrödinger Equation in Polar Coordinates

The stationary Schrödinger equation expressed in planar polar coordinates (r, θ) for a particle of mass m in an arbitrary potential V(r, θ). It rewrites the kinetic energy operator via the 2D Laplacian transformed through the chain rule.

$$-\frac{\hbar^2}{2m} \left( \frac{\partial^2 \psi}{\partial r^2} + \frac{1}{r}\frac{\partial\psi}{\partial r} + \frac{1}{r^2}\frac{\partial^2 \psi}{\partial \theta^2} \right) + V(r, \theta)\psi = E\psi$$

## Links
- generalises:: [[zettel/two-dimensional-harmonic-oscillator-in-polar-coordinates]] — The 2D polar Schrödinger equation specifies the governing PDE which is restricted to the isotropic harmonic oscillator potential V(r) = (1/2)mω^2 r^2

---
Source: tutorial7, pp. 1–2

<!-- kurooto:seen -->
- used-in:: [[zettel/separation-of-variables-in-polar-coordinates]] — The polar form of the Schrödinger equation is the starting point for the separation ψ = R(r)Θ(θ) described in that note
- example-of:: [[zettel/circular-infinite-well-potential-in-two-dimensions]] — The circular infinite well is a specific potential V(r, θ) that can be substituted into the polar Schrödinger equation, which the well note's eigenvalue analysis relies on
- generalises:: [[zettel/hydrogen-atom-radial-equation]] — The hydrogen radial equation is the 3D spherical analogue of the planar polar equation, sharing the same radial kinetic term and centrifugal contribution
- used-in:: [[zettel/radial-probability-density]] — Integrating |ψ(r, θ)|² over θ in polar coordinates, as the radial probability density note does, requires the polar wavefunction form given here
## Seen in
- [[ph2113/2026-11-16-tutorial-vii-polar-schrodinger-2d-oscillator|tutorial7]] pp. 1–2
<!-- /kurooto:seen -->
