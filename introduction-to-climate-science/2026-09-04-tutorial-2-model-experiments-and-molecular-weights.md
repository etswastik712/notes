---
id: introduction-to-climate-science/2026-09-04-tutorial-2-model-experiments-and-molecular-weights
aliases: [Tutorial 2: Model experiments and molecular weights]
tags: [climate, introduction-to-climate-science, tutorial, lorenz, chaos, molecular-weight, moist-air]
trust_tier: agent_written
---

# Tutorial 2: Model experiments and molecular weights

## Covered
Source: Tutorial 2 problem sheet, `Tutorial2.pdf` (Classroom: announcement 2026-09-04).

### Part 1: Model Experiments (SHM vs. Lorenz Chaos)
Numerical experiments comparing the stability and predictability of linear/harmonic motion versus non-linear chaotic convection.

#### 1. Simple Harmonic Motion (SHM) / Simple Pendulum Experiments
- **Question 1:** Find the phase of the SHM at different time instances using the numerical model for the given initial conditions and plot it against time.
- **Question 2:** Repeat Question 1 by slightly changing one of the initial conditions (e.g. initial angle $\theta(0) \to \theta(0) + \delta\theta$ or angular velocity $\omega(0) \to \omega(0) + \delta\omega$).
- **Dynamical outcome:** In simple harmonic motion ($\ddot{\theta} + \omega_0^2 \theta = 0$), trajectories in phase space are closed ellipses. Trajectories starting from slightly displaced initial states remain closely parallel for all time. The phase difference grows at most linearly; there is no exponential separation.

#### 2. Lorenz Convection Model Experiments
- **Question 3:** Run the Lorenz model ($\sigma = 10, \rho = 28, \beta = 8/3$) for the given initial condition $(x_0, y_0, z_0) = (0.2, 0.2, 0.3)$. Pick one of the state variables (e.g., $x(t)$ or $z(t)$) and plot it against time.
- **Question 4:** Run the Lorenz model again with a slightly different initial condition (e.g., $x_0 = 0.2001$). Pick the same variable and plot it against time.
- **Dynamical outcome:** Demonstrates deterministic chaos and the "butterfly effect."
  - For small $t$, the two solutions are visually indistinguishable.
  - Because the leading Lyapunov exponent $\lambda_{\max} > 0$, the trajectory separation $\delta \mathbf{x}(t)$ grows exponentially:
    $$|\delta \mathbf{x}(t)| \approx |\delta \mathbf{x}(0)| e^{\lambda_{\max} t}$$
  - Beyond the predictability horizon (Lyapunov time $t \sim \lambda_{\max}^{-1} \ln(1/|\delta \mathbf{x}(0)|)$), the two trajectories diverge completely to opposite lobes of the attractor. This demonstrates why detailed atmospheric weather forecasting is fundamentally limited to ~10–14 days regardless of observational precision.

---

### Part 2: Molecular Weights of Dry and Moist Air
Fundamental thermodynamic definitions:
- **Dry air:** Atmospheric air containing no water vapor.
- **Moist air:** Binary mixture of dry air and water vapor.

#### Question 1: Molecular Weight of Dry Air from Mole Fractions
Given mole fractions $\chi_i \equiv n_i / n$ of constituent gases:
$$M_d = \sum_i \chi_i M_i$$
Using standard atmospheric composition:
- $\text{N}_2$: $\chi = 0.7808$, $M = 28.013\text{ g mol}^{-1}$
- $\text{O}_2$: $\chi = 0.2095$, $M = 31.999\text{ g mol}^{-1}$
- $\text{Ar}$: $\chi = 0.0093$, $M = 39.948\text{ g mol}^{-1}$
- $\text{CO}_2$: $\chi = 0.0004$, $M = 44.010\text{ g mol}^{-1}$
Calculation:
$$M_d \approx (0.7808)(28.013) + (0.2095)(31.999) + (0.0093)(39.948) + (0.0004)(44.010) = 28.97\text{ g mol}^{-1}$$

#### Question 2: Molecular Weight of Moist Air from Mole Fractions
Let $\chi_v$ be the mole fraction of water vapor in moist air, and $\chi_d = 1 - \chi_v$ be the dry air fraction:
$$M = (1 - \chi_v) M_d + \chi_v M_v$$
where $M_v = 18.016\text{ g mol}^{-1}$ and $M_d = 28.97\text{ g mol}^{-1}$.
Because $M_v < M_d$:
$$M = M_d - \chi_v (M_d - M_v) < M_d$$
Moist air has a strictly smaller mean molecular weight than dry air.

#### Question 3: Formulations using Mass Fractions and Mixing Ratios
- **From mass fractions $q_i \equiv m_i / m$:**
  Total mass is $m = \sum m_i$; total moles are $n = \sum n_i = \sum \frac{m_i}{M_i}$.
  Apparent molecular weight is:
  $$M = \frac{m}{n} = \frac{m}{\sum_i \frac{m_i}{M_i}} = \frac{1}{\sum_i \frac{m_i / m}{M_i}} = \frac{1}{\sum_i \frac{q_i}{M_i}}$$
  For dry air:
  $$\frac{1}{M_d} = \sum_{i} \frac{q_{i,d}}{M_i}$$
  For moist air with specific humidity $q_v = m_v / m$ and dry air fraction $q_d = 1 - q_v$:
  $$\frac{1}{M} = \frac{1 - q_v}{M_d} + \frac{q_v}{M_v} = \frac{1}{M_d}\left[ 1 - q_v\left(1 - \frac{M_d}{M_v}\right) \right] = \frac{1}{M_d}\left[ 1 + q_v\left(\frac{1 - \epsilon}{\epsilon}\right) \right]$$
  where $\epsilon \equiv M_v / M_d \approx 0.622$.
- **From mass mixing ratio $w \equiv m_v / m_d$:**
  $$M = \frac{m_d + m_v}{\frac{m_d}{M_d} + \frac{m_v}{M_v}} = \frac{1 + w}{\frac{1}{M_d} + \frac{w}{M_v}} = M_d \frac{1 + w}{1 + \frac{w}{\epsilon}}$$

## From the post
PFA today's Tutorial

## Files
- [Tutorial2.pdf](https://drive.google.com/file/d/1mLXcEFlJLLQJ8A6MJ-PCxjFsfF4P_loZ/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-tutorial2-1mLXcE.pdf)

## Related
- [[introduction-to-climate-science/2026-08-27-tutorial-lorenz-model-and-simple-pendulum]]: simulation code, ODE systems, and Runge–Kutta solvers for SHM and the Lorenz model
- [[introduction-to-climate-science/2026-09-02-study-material-moist-and-dry-air]]: Wallace and Hobbs Chapter 3 on dry air molecular weight, water vapor constants, and virtual temperature
- [[01-Climate/Concepts/Atmospheric Composition]]: dry air composition, mole fractions, and dry air molar mass
