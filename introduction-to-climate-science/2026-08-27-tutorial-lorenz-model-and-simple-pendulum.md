---
id: introduction-to-climate-science/2026-08-27-tutorial-lorenz-model-and-simple-pendulum
aliases: [Tutorial: Lorenz Model and Simple Pendulum]
tags: [climate, introduction-to-climate-science, tutorial, lorenz, pendulum, numerical-methods]
trust_tier: agent_written
---

# Tutorial: Lorenz Model and Simple Pendulum

## Covered
Source: Classroom tutorial code files and Jupyter notebooks (Classroom: announcement 2026-08-27 and follow-up 2026-08-28).

### 1. The Lorenz System (Atmospheric Convection Model)
First developed by Edward Lorenz (1963) with numerical simulations by Ellen Fetter and Margaret Hamilton as a minimal three-variable truncation of thermal fluid convection (Rayleigh–Bénard convection).

**Physical variables:**
- $x$: proportional to the intensity of convective fluid motion (flow rate/velocity).
- $y$: proportional to the horizontal temperature difference between ascending and descending currents.
- $z$: proportional to the distortion of the vertical temperature profile from a conductive linear gradient.

**System of Ordinary Differential Equations (ODEs):**
$$\begin{aligned}
\frac{dx}{dt} &= \sigma (y - x) \\
\frac{dy}{dt} &= x (\rho - z) - y \\
\frac{dz}{dt} &= xy - \beta z
\end{aligned}$$

**Parameters (standard values used in the class code):**
- $\sigma = 10.0$ (Prandtl number $\text{Pr} = \nu / \kappa$, ratio of kinematic viscosity to thermal diffusivity).
- $\rho = 28.0$ (Rayleigh number parameter $r = \text{Ra} / \text{Ra}_c$, ratio of Rayleigh number to critical Rayleigh number).
- $\beta = 8/3$ (geometric aspect ratio parameter $b = 4 / (1 + a^2)$ of the convection roll).

**Dynamical properties:**
- **Nonlinearity:** Bilinear coupling terms $xz$ in $dy/dt$ and $xy$ in $dz/dt$.
- **Dissipative nature:** Divergence of phase-space velocity $\nabla \cdot \mathbf{f} = \frac{\partial \dot{x}}{\partial x} + \frac{\partial \dot{y}}{\partial y} + \frac{\partial \dot{z}}{\partial z} = -\sigma - 1 - \beta = -10 - 1 - 8/3 = -41/3 < 0$. Phase-space volume shrinks exponentially at rate $e^{-(41/3)t}$.
- **Chaotic attractor:** For $\rho = 28$, the system possesses a strange attractor (the butterfly attractor) with fractional dimension $\approx 2.06$. Trajectories are bounded within an ellipsoid but never intersect and never repeat.
- **Sensitive dependence on initial conditions:** Neighboring trajectories diverge exponentially at rate $e^{\lambda_{\max} t}$ with positive leading Lyapunov exponent $\lambda_{\max} \approx 0.905\text{ day}^{-1}$, setting a finite horizon on deterministic weather predictability.

**Numerical implementation:**
- Solved over time interval $t \in [0, 100]$ with initial condition $(x_0, y_0, z_0) = (0.2, 0.2, 0.3)$ using adaptive Runge–Kutta 4th/5th order (`ode45` in MATLAB, `scipy.integrate.solve_ivp` with `method="RK45"` in Python).

---

### 2. The Simple Pendulum (Non-linear Oscillator)
Second-order nonlinear ODE governing the planar motion of a simple pendulum:
$$\frac{d^2\theta}{dt^2} = -\frac{g}{l} \sin\theta$$
where $\theta$ is angular displacement from vertical, $g = 9.8\text{ m s}^{-2}$ is gravitational acceleration, and $l = 2.0\text{ m}$ is pendulum length.

**Reduction to first-order state-space system:**
Let state vector $\mathbf{y} = [y_1, y_2]^T = [\theta, \omega]^T$, where $\omega = \frac{d\theta}{dt}$ is angular velocity:
$$\begin{aligned}
\frac{dy_1}{dt} &= y_2 \\
\frac{dy_2}{dt} &= -\frac{g}{l} \sin(y_1)
\end{aligned}$$

**Simulation specifications:**
- Time interval: $t \in [0, 2\pi]$ (approx. $6.28\text{ s}$).
- Initial state: $\theta(0) = 0\text{ rad}$, $\omega(0) = \pi/4\text{ rad s}^{-1} \approx 0.7854\text{ rad s}^{-1}$.
- Solved with adaptive Runge–Kutta (`ode45` / `RK45`); state trajectories yield periodic closed orbits in phase space $(\theta, \omega)$.

## From the post
Hi everyone,

Please find below the Matlab code for tommorow's tutorial. Please bring your laptops to run the code in the class. If anyone can help us in converting these code to python then please send the python (jupyter file preferably) to one of the TAs via mail.
See you tommorow.

Link to the code:
https://drive.google.com/file/d/1j2eQ2fN9xIkLqWe64nBL84VxsUsSd1MB/view?usp=sharing

PS:
Could you tell the name of the cool figure that is shared below?

There are two .ipynb files we have added

*(Follow-up announcement on 2026-08-28):*
Please find the python code for the simple pendulum file 

## Files
- [simple_pend.m](https://drive.google.com/file/d/1Hkh5-2t-fOh3jVDDWwWCjhNT16-T0eAc/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-simple-pend-1Hkh5-.m): MATLAB function for pendulum ODEs
- [run_simple_pend.m](https://drive.google.com/file/d/1ioFQ3vV98TEKGCs8pEPH2nTXLFqTO0Se/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-run-simple-pend-1ioFQ3.m): MATLAB runner with `ode45`
- [lorenz.m](https://drive.google.com/file/d/1dpHbP3JeCb-VL5POCu7GlmE-isKDOwwF/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-lorenz-1dpHbP.m): MATLAB function for Lorenz ODEs
- [run_lorenz.m](https://drive.google.com/file/d/1h95YA2GX7H-R_qcouJ4U9c_dPlvmOY_Q/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-run-lorenz-1h95YA.m): MATLAB runner plotting 3D trajectory
- [Tutorial_lorenz model.zip](https://drive.google.com/file/d/1j2eQ2fN9xIkLqWe64nBL84VxsUsSd1MB/view?usp=drive_web): zip archive saved locally at `/home/swastik/.local/share/kurooto/data/classroom/introduction-to-climate-science/2026-10-25-tutorial-lorenz-model-1j2eQ2.zip` (binary archive; files extracted and provided individually)
- [Figure_2.png](https://drive.google.com/file/d/1-r5HiCiwCgZpD76dvHDeRp6Z2ktVB_gp/view?usp=drive_web): 3D phase-space plot of the Lorenz butterfly attractor
- [lorenz.ipynb](https://drive.google.com/file/d/1UuPRqmZjMRy3Em-1AbB_7_PsRiQ-u82v/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-lorenz-1UuPRq.ipynb): Python notebook solving Lorenz equations using `scipy.integrate.solve_ivp`
- [pendulam.ipynb](https://drive.google.com/file/d/1G7noNAvArn3OCPTIIzcPuLjyZvcZU3Cn/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-pendulam-1G7noN.ipynb; standalone re-post [pendulam.ipynb](https://drive.google.com/file/d/18z2gVUUm57ijAFFDlail9PG4SOl1VAx6/view?usp=drive_web)): Python notebook solving simple pendulum motion

## Related
- [[01-Climate/CL04 Feedback and Multiple Steady States]]: non-linear feedbacks, multiple steady states, and stability analysis
- [[01-Climate/Concepts/Bistability and Tipping Points]]: tipping points, perturbation response, and stability criteria
- [[01-Climate/CL09 Radiative-Convective Equilibrium]]: atmospheric convection, vertical buoyancy, and fluid instability
- [[introduction-to-climate-science/2026-09-04-tutorial-2-model-experiments-and-molecular-weights]]: Tutorial 2 model experiments testing initial-condition sensitivity on SHM and the Lorenz model

<!-- kurooto:materiale2f17c03 -->
## Concepts in pendulam
[[zettel/simple-pendulum-differential-equation]], [[zettel/state-space-reduction-for-pendulum-simulation]]
<!-- /kurooto:materiale2f17c03 -->
