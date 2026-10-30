---
id: zettel/particle-in-a-box-momentum-expectation-value
aliases: ["Particle in a Box Momentum Expectation Value", "momentum expectation value in infinite well", "mean momentum in a box"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Particle in a Box Momentum Expectation Value

The expected value of momentum for a stationary state in an infinite square well. Acting with the derivative operator on the sinusoidal standing wave converts it to a cosine, producing an integrand whose integral over [0, a] identically vanishes.

$$\hat{p} = -i\hbar \frac{d}{dx}$$

$$\langle p \rangle_n = \int_0^a \psi_n^*(x) \left(-i\hbar \frac{d}{dx}\right) \psi_n(x) \, dx = 0$$

## Links

---
Source: Particle_in_a_box, pp. 1–10

<!-- kurooto:seen -->
- generalises:: [[zettel/quantum-expectation-value]] — The general expectation-value note defines the Born-weighted average that this note applies to momentum in the infinite well, which is a special case of it
- needs:: [[zettel/infinite-square-well-potential]] — The momentum expectation value is computed on the standing-wave eigenstates of the box, so this note depends on the infinite well potential and its boundary conditions
- contrasts-with:: [[zettel/plane-wave-momentum-eigenstate]] — This note's vanishing momentum expectation follows because the real standing wave cos(kx) is not a momentum eigenstate, whereas the plane wave e^{ikx} is an exact eigenstate with eigenvalue ħk
- contrasts-with:: [[zettel/particle-in-a-box-position-expectation-value]] — Both are expectation values for the same box eigenstates, but the position result is obtained from reflection symmetry about the midpoint while the momentum result comes from an integrand that vanishes identically
## Seen in
- [[ph2113/2026-10-12-tutorial-ii-harmonic-oscillator-ladder-operators|Particle_in_a_box]] pp. 1–10
<!-- /kurooto:seen -->
