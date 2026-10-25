---
id: introduction-to-climate-science/2026-09-17-study-material-6-radiative-convective-equilibrium
aliases: [Study material 6: Radiative-convective equilibrium, Marshall & Plumb Ch 4: Radiative-Convective Equilibrium]
tags: [climate, introduction-to-climate-science, convection, radiative-convective-equilibrium, lapse-rate, tropopause, buoyancy-frequency]
trust_tier: agent_written
---

# Study material 6: Radiative-convective equilibrium

## Covered
Source: Marshall and Plumb, *Atmosphere, Ocean, and Climate Dynamics*, Chapter 4, Sections 4.7–4.9: "Radiative-Convective Equilibrium" (Classroom: study material 2026-09-17).

### 1. Terminology Key
- **Radiative-Convective Equilibrium (RCE):** The composite vertical equilibrium state of the atmosphere wherein the lower layer (troposphere) is governed by turbulent convective heat transport maintaining convective neutrality, and the upper layer (stratosphere) is governed by radiative equilibrium.
- **Tropopause ($z_T$):** The boundary interface separating the convectively determined troposphere below from the radiatively determined stratosphere above.
- **Convective Neutrality:** A state where vertical displacement of an air parcel results in zero net buoyant restoring force; characterized by constant moist potential temperature ($\theta_e$) in the moist tropical troposphere, or constant potential temperature ($\theta$) in dry convection.
- **Buoyancy Frequency ($N$, Brunt–Väisälä Frequency):** The intrinsic angular frequency of vertical buoyant oscillations executed by an air parcel displaced adiabatically within a stably stratified environment:
  $$N^2 \equiv \frac{g}{\theta}\frac{d\theta}{dz}$$
- **Dry Adiabatic Lapse Rate ($\Gamma_d$):** The rate of temperature decrease with altitude for an unsaturated parcel undergoing adiabatic expansion:
  $$\Gamma_d \equiv \frac{g}{c_p} \approx 9.8\text{ K km}^{-1} \approx 9.8 \times 10^{-3}\text{ K m}^{-1}$$

---

### 2. Mechanics of Radiative-Convective Equilibrium

#### A. Inevitability of Convection
1. **Surface Temperature Discontinuity in Pure Radiative Equilibrium:**
   Because the atmosphere is relatively transparent to incoming solar radiation while strongly absorbing terrestrial infrared radiation, solar energy is deposited primarily at the planetary surface. Pure radiative equilibrium models predict a ground surface temperature $T_s$ substantially warmer than the adjacent atmospheric layer ($T_s \gg T_{\text{air}}(0^+)$), producing an abrupt temperature discontinuity at the boundary.
2. **Convective Overturning:**
   This discontinuity creates a superadiabatic temperature lapse rate ($-\partial T/\partial z > \Gamma_d$) in the lower atmosphere, which is violently buoyant and statically unstable.
3. **Restoration of Neutrality:**
   Convective plumes and thermals carry sensible and latent heat upward from the surface. Mixing with the environmental air warms the middle and upper troposphere until the environmental lapse rate relaxes to the convective neutral lapse rate ($\Gamma \approx \Gamma_m \approx 6.5\text{ K km}^{-1}$ in moist air).
4. **Troposphere–Stratosphere Dual Structure:**
   - **Troposphere ($0 \le z \le z_T$):** Convectively controlled thermal profile; lapse rate constrained by moist adiabatic neutrality; net radiative divergence (cooling) balanced by vertical convective heat convergence.
   - **Stratosphere ($z > z_T$):** Dynamically stable stratification ($N^2 > 0$); negligible vertical convection; thermal profile governed strictly by local radiative balance (solar UV heating by $\text{O}_3$ balancing longwave IR cooling by $\text{CO}_2$ and $\text{H}_2\text{O}$).

#### B. Tropical vs. Mid-Latitude Regimes
- **Tropical Troposphere:** Close to continuous moist convective neutrality. Deep convection penetrates directly to the tropical tropopause ($z_T \approx 16–17\text{ km}$). Outgoing Longwave Radiation (OLR) displays stark spatial contrast:
  - Deep convective cloud tops: $T_c \approx 220\text{ K} \implies \text{OLR} = \sigma T_c^4 \approx 133\text{ W m}^{-2}$ (very low).
  - Clear subtropical deserts and oceans: radiation escapes directly from warm lower levels ($T_s \approx 300\text{ K} \implies \text{OLR} \approx 459\text{ W m}^{-2}$).
- **Mid-Latitudes:** Local convection is intermittent (e.g. shallow daytime cumulus, squall lines, cold front passages). Vertical and horizontal heat transports are dominated by large-scale synoptic baroclinic waves rather than purely 1D local convection.

---

### 3. Worked Analytical Problems (Section 4.9)

#### Problem 1: Buoyancy Frequency in Terms of Environmental Temperature Profile
- **Task:** Show that the squared buoyancy frequency $N^2$ can be expressed as:
  $$N^2 = \frac{g}{T_E}\left( \frac{dT_E}{dz} + \Gamma_d \right)$$
- **Rigorous Derivation:**
  1. By definition, potential temperature $\theta_E$ is:
     $$\theta_E = T_E \left( \frac{p_0}{p} \right)^{R/c_p}$$
  2. Taking the natural logarithm:
     $$\ln \theta_E = \ln T_E + \frac{R}{c_p} \ln p_0 - \frac{R}{c_p} \ln p$$
  3. Differentiating with respect to altitude $z$:
     $$\frac{1}{\theta_E} \frac{d\theta_E}{dz} = \frac{1}{T_E}\frac{dT_E}{dz} - \frac{R}{c_p p}\frac{dp}{dz}$$
  4. In the atmosphere, the large-scale pressure field satisfies hydrostatic equilibrium $\frac{dp}{dz} = -\rho g$. Using the ideal gas law $p = \rho R T_E \implies \frac{1}{\rho} = \frac{R T_E}{p}$:
     $$-\frac{R}{c_p p}\frac{dp}{dz} = -\frac{R}{c_p p}(-\rho g) = \frac{R \rho g}{c_p p} = \frac{g}{c_p T_E} = \frac{\Gamma_d}{T_E}$$
     where $\Gamma_d \equiv \frac{g}{c_p}$.
  5. Substituting this into the logarithmic derivative of $\theta_E$:
     $$\frac{1}{\theta_E}\frac{d\theta_E}{dz} = \frac{1}{T_E}\left( \frac{dT_E}{dz} + \Gamma_d \right)$$
  6. Recalling $N^2 \equiv \frac{g}{\theta_E}\frac{d\theta_E}{dz}$:
     $$N^2 = \frac{g}{T_E}\left( \frac{dT_E}{dz} + \Gamma_d \right) \quad \blacksquare$$
  - **Stability Criterion:**
    - Stable ($N^2 > 0$): $\frac{dT_E}{dz} > -\Gamma_d$ (lapse rate $\Gamma < \Gamma_d$).
    - Neutral ($N^2 = 0$): $\frac{dT_E}{dz} = -\Gamma_d$ (lapse rate $\Gamma = \Gamma_d$).
    - Unstable ($N^2 < 0$): $\frac{dT_E}{dz} < -\Gamma_d$ (superadiabatic lapse rate $\Gamma > \Gamma_d$).

#### Problem 2: Tropical Atmospheric Profile Estimation
Given observed tropical temperature sounding $T(z)$:
- (a) **Tropospheric Lapse Rate:** Between surface ($1000\text{ hPa}$, $T \approx 300\text{ K}$) and tropopause ($100\text{ hPa}$, $z \approx 16\text{ km}$, $T \approx 195\text{ K}$):
  $$\Gamma = -\frac{\Delta T}{\Delta z} \approx \frac{300\text{ K} - 195\text{ K}}{16\text{ km}} \approx 6.5\text{ K km}^{-1}$$
  This is significantly smaller than the dry adiabatic rate $\Gamma_d = 9.8\text{ K km}^{-1}$, confirming that latent heat release in moist convective updrafts maintains a moist adiabatic lapse rate $\Gamma_m < \Gamma_d$.
- (b) **Pressure Scale Height:**
  $$H = \frac{R T_0}{g}$$
  For mean layer temperature $T_0 \approx 255\text{ K}$ between $700\text{ mbar}$ and $300\text{ mbar}$:
  $$H = \frac{(287\text{ J kg}^{-1}\text{ K}^{-1})(255\text{ K})}{9.81\text{ m s}^{-2}} \approx 7460\text{ m} \approx 7.5\text{ km}$$
- (c) **Buoyancy Oscillation Period:**
  In the mid-troposphere, with $T_E \approx 260\text{ K}$, $\frac{dT_E}{dz} \approx -6.5 \times 10^{-3}\text{ K m}^{-1}$, $\Gamma_d \approx 9.8 \times 10^{-3}\text{ K m}^{-1}$:
  $$N^2 = \frac{9.81}{260}\left( -6.5 \times 10^{-3} + 9.8 \times 10^{-3} \right) = (0.0377)(3.3 \times 10^{-3}) \approx 1.24 \times 10^{-4}\text{ s}^{-2}$$
  $$N \approx 0.0111\text{ s}^{-1}$$
  Buoyancy period:
  $$\tau = \frac{2\pi}{N} \approx \frac{2\pi}{0.0111} \approx 566\text{ s} \approx 9.4\text{ minutes}$$

#### Problem 3: Laboratory Convection Tank Model (GFD Lab II)
- **Model Configuration:**
  - Tank fluid of density $\rho$ and specific heat capacity $c_p$.
  - Initial linear stable temperature stratification: $T_{\text{initial}}(z) = T_0 + T_z z$, with constant stratification gradient $T_z \equiv \frac{dT}{dz} > 0$.
  - Bottom heating pad supplies constant upward heat flux $H$ ($\text{W m}^{-2}$).
  - Convective turbulence rapidly homogenizes the convecting bottom layer of depth $h(t)$, maintaining a uniform temperature $T(t)$ that joins continuously onto the undisturbed linear stratification at $z = h(t)$:
    $$T(t) = T_{\text{initial}}(h) = T_0 + T_z h(t)$$
- **Thermodynamic Derivation:**
  The horizontally averaged thermodynamic energy equation for the well-mixed layer of depth $h$ is:
  $$\rho c_p \frac{dT}{dt} = \frac{H}{h}$$
  Since $T(t) = T_0 + T_z h(t)$, differentiating with respect to time $t$ gives:
  $$\frac{dT}{dt} = T_z \frac{dh}{dt}$$
  Substituting into the thermodynamic equation:
  $$\rho c_p T_z \frac{dh}{dt} = \frac{H}{h} \implies \rho c_p T_z h \frac{dh}{dt} = H$$
  Using the chain rule $h \frac{dh}{dt} = \frac{1}{2}\frac{d(h^2)}{dt}$:
  $$\frac{1}{2} \rho c_p T_z \frac{d(h^2)}{dt} = H \quad \blacksquare$$
- **Analytical Solution:**
  Integrating both sides from initial state $h(0) = 0$:
  $$h^2(t) = \frac{2 H}{\rho c_p T_z} t \implies h(t) = \left( \frac{2 H}{\rho c_p T_z} \right)^{1/2} t^{1/2}$$
  The layer temperature evolves as:
  $$T(t) = T_0 + T_z h(t) = T_0 + \left( \frac{2 H T_z}{\rho c_p} \right)^{1/2} t^{1/2}$$
- **Physical Interpretation:**
  Both the penetration depth $h(t)$ of the convective boundary layer and the temperature anomaly $T(t) - T_0$ grow strictly with $\sqrt{t}$. This $\sqrt{t}$ encroachment rate is consistent with laboratory observations and atmospheric boundary-layer growth under daytime solar heating.

## From the post
*(No post text)*

## Files
- [Radiative_convective_equilibrium_Marshall_and_plumb.pdf](https://drive.google.com/file/d/1upcA2JoX8hcS_5vuYW1aYzqPtcUaojMO/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-radiative-convective-equilibrium-marshall-and-plum-1upcA2.pdf)

## Related
- [[introduction-to-climate-science/2026-09-17-study-material-5-radiative-balance]]: pure radiative equilibrium background and the surface temperature discontinuity
- [[introduction-to-climate-science/2026-09-10-reading-manabe-and-strickler-1964]]: Manabe and Strickler (1964) numerical implementation of convective adjustment
- [[01-climate/cl09-radiative-convective-equilibrium]]: radiative-convective equilibrium, tropopause dynamics, and tropical stability
- [[01-climate/concepts/convective-adjustment]]: convective adjustment definition, lapse rate criteria, and numerical formulation
- [[01-climate/concepts/lapse-rate]]: environmental lapse rate vs. adiabatic lapse rates
- [[01-climate/concepts/dry-adiabatic-lapse-rate]]: definition and value $\Gamma_d = g/c_p \approx 9.8\text{ K km}^{-1}$
