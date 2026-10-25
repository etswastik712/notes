---
id: introduction-to-climate-science/exam-prep
aliases: ["Exam prep: Introduction to Climate Science"]
tags: [exam-prep, introduction-to-climate-science]
trust_tier: agent_written
---

# Exam prep: Introduction to Climate Science

<!-- kurooto:exam-prep (kept current by Kurooto from your courses; write your own notes outside these markers) -->
## Next assessment
Not announced yet in the Classroom posts.

## Covered so far
- [[introduction-to-climate-science/2026-08-27-tutorial-lorenz-model-and-simple-pendulum]]: Lorenz convection model (3D non-linear ODEs, parameters $\sigma=10, \rho=28, \beta=8/3$, strange attractor, deterministic chaos) and simple pendulum (non-linear equation, state-space reduction).
- [[introduction-to-climate-science/2026-09-02-study-material-2-atmospheric-composition]]: Eulerian vs. Lagrangian frames; kinematic constraints of gravity; dry air composition, trace radiatively active gases, Dalton's law of partial pressures and volumes, mean molar weight, mixing ratios as material tracers, and hydrostatic balance foundation.
- [[introduction-to-climate-science/2026-09-02-study-material-moist-and-dry-air]]: Gas laws, apparent molecular weights ($M_d = 28.97\text{ g mol}^{-1}$, $M_w = 18.016\text{ g mol}^{-1}$), specific gas constants ($R_d = 287.0\text{ J K}^{-1}\text{ kg}^{-1}$, $R_v = 461.51\text{ J K}^{-1}\text{ kg}^{-1}$), ratio $\epsilon \equiv R_d/R_v \approx 0.622$, and derivation of virtual temperature ($T_v$).
- [[introduction-to-climate-science/2026-09-03-study-material-3-pressure-and-geopotential]]: Hydrostatic equation, column mass origin of pressure, geopotential $\Phi$, geopotential height $Z$, hypsometric equation, scale height $H$, and diffusive separation above the turbopause (~105 km).
- [[introduction-to-climate-science/2026-09-04-tutorial-2-model-experiments-and-molecular-weights]]: Tutorial 2: Numerical experiments contrasting regular SHM phase evolution with exponential divergence on the Lorenz attractor (Lyapunov time); derivations of dry and moist air molecular weights from mole fractions and mass fractions.
- [[introduction-to-climate-science/2026-09-09-study-material-4-pressure-gradient-force]]: Fundamental forces (body vs. surface forces), rotating frame apparent forces (Coriolis, centrifugal), derivation of 3D pressure gradient force per unit mass ($-\frac{1}{\rho}\nabla p$), true gravitational force, and horizontal scales of atmospheric motion.

## Must know
- **Eulerian vs. Lagrangian descriptions:** Eulerian represents atmospheric behavior in terms of field properties (PDEs at fixed space points); Lagrangian tracks the state and composition of individual moving fluid parcels of fixed matter (Classroom: Salby, pp. 1–2).
- **Kinematic constraint of gravity:** Gravity confines $>90\%$ of atmospheric mass to a shallow layer ($<10\text{ km}$, $<0.15\%$ of Earth's radius). Consequently, large-scale motions ($L > 100\text{ km}$) are strictly quasi-horizontal ($w \ll u, v$); vertical displacements equal horizontal scales only in small convective cells and fronts ($L \sim 10\text{ km}$) (Classroom: Salby, p. 2; your notes: [[01-Climate/CL06 Hydrostatic Balance and Vertical Structure]]).
- **Dry air apparent molecular weight:** $M_d = \sum_i \chi_i M_i = 28.97\text{ g mol}^{-1}$ (using $\chi_{\text{N}_2} = 0.7808, \chi_{\text{O}_2} = 0.2095, \chi_{\text{Ar}} = 0.0093, \chi_{\text{CO}_2} = 0.0004$) (Classroom: Wallace & Hobbs, p. 65; Tutorial 2).
- **Specific gas constant for dry air:** $R_d = 1000 \frac{R^*}{M_d} = 1000 \frac{8.3145}{28.97} = 287.0\text{ J K}^{-1}\text{ kg}^{-1}$; equation of state: $p_d = \rho_d R_d T$ (Classroom: Wallace & Hobbs, p. 65).
- **Water vapor specific gas constant and $\epsilon$:** $M_w = 18.016\text{ g mol}^{-1} \implies R_v = 1000 \frac{R^*}{M_w} = 461.51\text{ J K}^{-1}\text{ kg}^{-1}$. The ratio $\epsilon \equiv \frac{R_d}{R_v} = \frac{M_w}{M_d} \approx 0.622$ (Classroom: Wallace & Hobbs, p. 66).
- **Moist air density:** Because $M_w < M_d$, replacing dry air molecules with water vapor at identical $T$ and $p$ lowers mixture density: moist air is less dense than dry air (Classroom: Wallace & Hobbs, p. 66).
- **Virtual temperature exact formula:** $T_v \equiv \frac{T}{1 - \frac{e}{p}(1 - \epsilon)}$. First-order approximation: $T_v \approx T\left(1 + 0.378 \frac{e}{p}\right) \approx T(1 + 0.61 w)$, where $w \approx \epsilon \frac{e}{p}$ is mass mixing ratio. Equation of state for moist air: $p = \rho R_d T_v$. By definition, $T_v \ge T$ always (Classroom: Wallace & Hobbs, p. 67; your notes: [[01-Climate/Concepts/Virtual Temperature]]).
- **Material tracer conservation:** A passive constituent ($\dot{m}_i = 0$) has a materially conserved mass mixing ratio: $\frac{Dr_i}{Dt} = 0$, where $r_i = m_i / m_d$. Molar fraction and volume mixing ratio satisfy $N_i \approx r_i / \epsilon_i$ with $\epsilon_i = M_i / M_d$ (Classroom: Salby, pp. 6–7).
- **Hydrostatic balance equation:** In the absence of vertical acceleration ($dw/dt = 0$), vertical pressure gradient balances gravity: $\frac{\partial p}{\partial z} = -\rho g = -\frac{g}{\alpha}$. Pressure at altitude $z$ is the column weight per unit area: $p(z) = \int_z^\infty \rho g \, dz'$ (Classroom: Wallace & Hobbs, p. 68; Holton & Hakim, p. 7).
- **Geopotential and Geopotential Height:** $d\Phi = g \, dz = -\alpha \, dp$. $\Phi(z) = \int_0^z g(z') \, dz'$ ($\text{J kg}^{-1}$). Geopotential height: $Z \equiv \Phi(z) / g_0$, with $g_0 \equiv 9.80665\text{ m s}^{-2}$ (Classroom: Wallace & Hobbs, pp. 68–69; your notes: [[01-Climate/Concepts/Geopotential]]).
- **Hypsometric equation:** Geopotential thickness $\Delta Z = Z_2 - Z_1 = \frac{R_d \bar{T}_v}{g_0} \ln\left(\frac{p_1}{p_2}\right) = \bar{H} \ln\left(\frac{p_1}{p_2}\right)$. Thickness is strictly proportional to mean layer virtual temperature $\bar{T}_v$ (Classroom: Wallace & Hobbs, p. 69; your notes: [[01-Climate/Concepts/Hypsometric Equation]]).
- **Atmospheric scale height:** $H \equiv \frac{R_d T}{g_0} \approx 29.3 \, T\text{ m}$; for $T \approx 255\text{ K}$, $H \approx 7.5\text{ km} \approx 8\text{ km}$. Isothermal barometric law: $p(Z) = p_1 e^{-(Z - Z_1)/H}$ (Classroom: Wallace & Hobbs, p. 69; Salby, p. 7).
- **Turbopause (~105 km):** Below 105 km, eddy mixing maintains constant mean molecular weight $M_d = 28.97$ and a common scale height $H$. Above 105 km, molecular diffusion separates gases by individual molecular scale heights $H_i = R^* T / (M_i g)$, so heavier gases ($\text{N}_2, \text{O}_2$) decay faster than lighter gases ($\text{He}, \text{H}$) (Classroom: Wallace & Hobbs, pp. 69–70).
- **Pressure gradient force (PGF) per unit mass:** Derived from Taylor expansion on an infinitesimal volume $\delta V = \delta x \delta y \delta z$: $\frac{\mathbf{F}_{pg}}{m} = -\frac{1}{\rho}\nabla p$. PGF is proportional to the gradient of pressure, not pressure magnitude, accelerating fluid from high to low pressure (Classroom: Holton & Hakim, pp. 5–7; your notes: [[01-Climate/Concepts/Pressure Gradient Force]]).
- **Classification of forces:** Body forces act on parcel mass (gravity $\mathbf{g}^* = -\frac{GM}{r^2}\frac{\mathbf{r}}{r}$); surface forces act across parcel boundaries (pressure, viscosity). In rotating frames, apparent inertial forces (Coriolis $-2\boldsymbol{\Omega}\times\mathbf{v}$, centrifugal $\boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r})$) must be included (Classroom: Holton & Hakim, pp. 5–7).
- **Lorenz convection equations:** $\dot{x} = \sigma(y - x)$, $\dot{y} = x(\rho - z) - y$, $\dot{z} = xy - \beta z$ with standard parameters $\sigma = 10, \rho = 28, \beta = 8/3$. Dissipative volume contraction $\nabla \cdot \mathbf{f} = -(\sigma + 1 + \beta) = -41/3 < 0$. Trajectories are bounded on a strange attractor with sensitive dependence on initial conditions ($\lambda_{\max} > 0$), limiting deterministic prediction (Classroom: announcement 2026-08-27, Tutorial 2).

## Typical questions
- **Mean molecular weight from mole fractions:** Given atmospheric mole fractions $\chi_i$, compute $M = \sum \chi_i M_i$. Example: dry air with $\text{N}_2, \text{O}_2, \text{Ar}, \text{CO}_2$ yields $M_d = 28.97\text{ g mol}^{-1}$ ([[introduction-to-climate-science/2026-09-04-tutorial-2-model-experiments-and-molecular-weights]] Q1).
- **Mean molecular weight from mass fractions:** Compute $M = 1 / \sum (q_i / M_i)$ for dry or moist air given specific humidity $q_v$ ([[introduction-to-climate-science/2026-09-04-tutorial-2-model-experiments-and-molecular-weights]] Q3).
- **Moist air total pressure:** Given dry air density $\rho_d'$ and water vapor density $\rho_v'$ at temperature $T$, compute total pressure via Dalton's law $p = \rho_d' R_d T + \rho_v' R_v T$ ([[introduction-to-climate-science/2026-09-02-study-material-moist-and-dry-air]], Wallace & Hobbs Exercise 3.1).
- **Virtual temperature calculation:** Given temperature $T$, pressure $p$, and vapor pressure $e$ (or mixing ratio $w$), compute $T_v = T / [1 - (e/p)(1 - \epsilon)] \approx T(1 + 0.61 w)$ ([[introduction-to-climate-science/2026-09-02-study-material-moist-and-dry-air]]).
- **Layer geopotential thickness / Hypsometric equation:** Given bounding pressure levels $p_1, p_2$ and mean virtual temperature $\bar{T}_v$, calculate $\Delta Z = \frac{R_d \bar{T}_v}{g_0}\ln(p_1/p_2)$ ([[introduction-to-climate-science/2026-09-03-study-material-3-pressure-and-geopotential]]).
- **Pressure gradient acceleration:** Given spatial pressure difference $\Delta p$ across distance $\Delta x$ and density $\rho$, compute acceleration $a_x = -\frac{1}{\rho}\frac{\partial p}{\partial x}$ ([[introduction-to-climate-science/2026-09-09-study-material-4-pressure-gradient-force]]).
- **Numerical ODE state-space reduction:** Convert non-linear second-order equations ($\ddot{\theta} = -(g/l)\sin\theta$) into first-order systems $\dot{y}_1 = y_2$, $\dot{y}_2 = -(g/l)\sin y_1$ for numerical integration ([[introduction-to-climate-science/2026-08-27-tutorial-lorenz-model-and-simple-pendulum]]).

## Gaps
- The file `Tutorial_lorenz model.zip` was downloaded as a binary archive without direct text extraction (individual code files were provided separately in the post).
- No syllabus, grading policy, or future quiz/exam schedule has been posted in Classroom yet.
- Study Material 1 was not posted in this batch (materials begin at Study Material-2).
<!-- /kurooto:exam-prep -->
