---
id: zettel/hydrogen-atom-radial-wavefunctions
aliases: ["Hydrogen Atom Radial Wavefunctions", "R_{n,l}(r)", "Coulomb radial eigenfunctions"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Hydrogen Atom Radial Wavefunctions

The bound-state radial eigenfunctions of the hydrogen atom, expressed as an exponential decay multiplied by a power of r and an associated Laguerre polynomial.

$$\psi_{n,l,m}(r, \theta, \phi) = N_{n,l} e^{-r/na} \left(\frac{2r}{na}\right)^l L_{n-l-1}^{2l+1}(2r/na) Y_{lm}(\theta, \phi)$$

$$R_{1,0}(r) = 2\left(\frac{1}{a}\right)^{3/2} e^{-r/a}$$

$$R_{2,0}(r) = \frac{1}{\sqrt{2}}\left(\frac{1}{a}\right)^{3/2} \left(2 - \frac{r}{a}\right) e^{-r/2a}$$

$$R_{2,1}(r) = \frac{1}{\sqrt{24}}\left(\frac{1}{a}\right)^{3/2} \frac{r}{a} e^{-r/2a}$$

## Links
- used-in:: [[zettel/radial-probability-density]] — Constructs the radial distribution function P(r) = 4πr^2 |R_{n,0}(r)|^2 for evaluating electron localization shells

---
Source: Hydrogen_atom, pp. 1–8

<!-- kurooto:seen -->
- needs:: [[zettel/hydrogen-atom-radial-equation]] — The radial wavefunctions R_{n,l}(r) are the solutions of the radial Schrödinger equation for the Coulomb potential, so the equation is the source from which these functions are obtained
- used-in:: [[zettel/spherical-harmonics]] — The full hydrogen wavefunction ψ_{n,l,m} is the product of the radial factor in this note and the angular factor Y_{lm}(θ, φ), which is the spherical harmonic
- part-of:: [[zettel/hydrogen-spectrum-and-degeneracy]] — The quantum numbers n and l that index the radial wavefunctions are the same ones that set the bound-state energies E_n and the n² degeneracy discussed in the spectrum note
## Seen in
- [[ph2113/2026-11-16-tutorial-vii-polar-schrodinger-2d-oscillator|Hydrogen_atom]] pp. 1–8
<!-- /kurooto:seen -->
