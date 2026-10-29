---
id: zettel/dynamical-amplification-of-quantum-uncertainty
aliases: ["Dynamical Amplification of Quantum Uncertainty", "balanced pencil problem", "inverted pendulum quantum instability", "Dynamical Amplification of Quantum Uncertainty in an Inverted Oscillator"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Dynamical Amplification of Quantum Uncertainty

The mechanism whereby initial microscopic quantum uncertainties in position and momentum, constrained by the Heisenberg uncertainty relation, undergo exponential growth under classically unstable equations of motion to produce macroscopic indeterminacy on observable timescales.

$$s^2 = (\Delta x)^2 + \frac{(\Delta p)^2}{M^2 \omega^2}$$

$$\Delta x_{\text{min}} = \sqrt{\frac{\hbar}{2M\omega}}, \quad \Delta p = \sqrt{\frac{\hbar M \omega}{2}}, \quad s_{\text{min}} = \sqrt{\frac{\hbar}{M\omega}}$$

$$t \simeq \frac{1}{\omega} \ln\left(\frac{2 \times 10^{-3}}{s_{\text{min}}}\right)$$

## Links
- needs:: [[zettel/position-momentum-uncertainty-relation-from-fourier-transform]] — Relies on the minimum uncertainty bound Delta x * Delta p >= hbar / 2 to determine the minimum initial phase-space spread s_min
- used-in:: [[zettel/gaussian-wave-packet-minimum-uncertainty]] — Initial state saturates the uncertainty inequality Delta x * Delta p = hbar / 2 to optimize survival time against exponential divergence

---
Source: PH2113_tutorial_solutions, pp. 1–5

<!-- kurooto:seen -->
## Seen in
- [[ph2113/2026-09-08-tutorial-states-interference-uncertainty|PH2113_tutorial-pdf]] pp. 1–2
- [[ph2113/2026-09-10-tutorial-solutions-states-interference-uncertainty|PH2113_tutorial_solutions]] pp. 1–5

### Added from class
- PH2113_tutorial-pdf pp. 1–2: Formulates the minimum initial quantum seed metric s^2 = (Δx)^2 + (Δp/(Mω))^2 and proves optimal saturation at Δx = sqrt(ħ/(2Mω)) and Δp = sqrt(ħMω/2).
<!-- /kurooto:seen -->
