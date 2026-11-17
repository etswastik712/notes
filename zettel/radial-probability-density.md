---
id: zettel/radial-probability-density
aliases: ["Radial Probability Density", "P(r)", "radial distribution function"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Radial Probability Density

The probability density of locating a quantum particle within a thin spherical or annular shell of radius r and thickness dr, obtained by integrating the absolute square of the wavefunction over all angular coordinates.

$$P(r) = \int_0^{2\pi} |\psi(r, \theta)|^2 r\, d\theta$$

$$P(r) = \int_0^\pi \int_0^{2\pi} |\psi(r, \theta, \phi)|^2 r^2 \sin\theta\, d\theta d\phi$$

$$P(r) = 2\pi r |\psi(r)|^2$$

$$P(r) = 4\pi r^2 |\psi(r)|^2$$

## Links
- used-in:: [[zettel/two-dimensional-schrodinger-equation-in-polar-coordinates]] — It calculates the physical spatial distribution for wavefunctions that solve the 2D or 3D Schrödinger equation

---
Source: tutorial7, pp. 1–2

<!-- kurooto:seen -->
## Seen in
- [[ph2113/2026-11-16-tutorial-vii-polar-schrodinger-2d-oscillator|tutorial7]] pp. 1–2
<!-- /kurooto:seen -->
