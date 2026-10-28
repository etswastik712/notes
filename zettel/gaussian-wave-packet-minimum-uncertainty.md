---
id: zettel/gaussian-wave-packet-minimum-uncertainty
aliases: ["Gaussian Wave Packet Minimum Uncertainty", "Gaussian wave packet saturation", "minimum-uncertainty state"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Gaussian Wave Packet Minimum Uncertainty

A wave packet with a Gaussian spatial profile whose position-space and momentum-space standard deviations exactly saturate the Heisenberg uncertainty bound Delta x Delta p = hbar / 2.

$$\psi(x) = \frac{1}{(2\pi\sigma^2)^{1/4}} \exp\left( -\frac{(x - x_0)^2}{4\sigma^2} + ik_0 x \right)$$

$$\langle p^2 \rangle = \hbar^2 k_0^2 + \frac{\hbar^2}{4\sigma^2}, \quad \Delta p = \frac{\hbar}{2\sigma}$$

$$\Delta x \Delta p = \frac{1}{2} |\langle [\hat{x}, \hat{p}] \rangle| = \frac{\hbar}{2}$$

## Links
- special-case-of:: [[zettel/position-momentum-uncertainty-relation-from-fourier-transform]] — Directly evaluates Delta x = sigma and Delta p = hbar / (2 sigma) to prove equality in Delta x * Delta p >= hbar / 2
- needs:: [[zettel/square-integrability-of-wave-functions]] — Normalization prefactor (2 pi sigma^2)^{-1/4} guarantees unit integral of probability density over real space

---
Source: PH2113_tutorial_solutions, pp. 1–5

<!-- kurooto:seen -->
## Seen in
- [[ph2113/2026-09-10-tutorial-solutions-states-interference-uncertainty|PH2113_tutorial_solutions]] pp. 1–5
<!-- /kurooto:seen -->
