---
id: introduction-to-climate-science/2026-09-02-study-material-2-atmospheric-composition
aliases: [Study Material-2: Atmospheric composition, Atmospheric composition (Salby)]
tags: [climate, introduction-to-climate-science, atmospheric-composition, gas-laws, hydrostatics, salby]
trust_tier: agent_written
---

# Study Material-2: Atmospheric composition

## Covered
Source: Salby, M. L., *Physics of the Atmosphere and Climate*, Chapter 1: The Earth-atmosphere system, pp. 1–7 (Classroom: Study Material-2, 2026-09-02).

### 1. Descriptions of Atmospheric Behavior
The atmosphere is governed by the laws of continuum mechanics applied to infinitesimal fluid parcels (fixed collections of matter).
- **Eulerian description:** Represents atmospheric behavior in terms of field properties (instantaneous spatial distributions of velocity, temperature, constituents) governed by partial differential equations. Well suited for numerical simulations.
- **Lagrangian description:** Follows the trajectory and state transformations of individual air parcels. Mass transfer across parcel boundaries (molecular diffusion, turbulent mixing) is slow enough to be neglected for many large-scale applications. Essential for thermodynamic transformations and material tracer conservation.

### 2. Physical Mechanisms Influencing the Atmosphere
- **Gravity:** Confines atmospheric mass to a shallow shell (<10 km contains ~90% of atmospheric mass, <0.15% of Earth's radius $a \approx 6371\text{ km}$). Mass and constituents are vertically stratified. Large-scale circulations (horizontal scale $L > 100\text{ km}$) are constrained to be quasi-horizontal ($w \ll u, v$); vertical displacements are comparable to horizontal displacements only in small convective cells and fronts ($L \sim 10\text{ km}$).
- **Compressibility:** Parcel volume expands/contracts under ambient pressure changes, causing density and absolute concentrations to vary even if the constituent molecule count is fixed.
- **Earth's Rotation:** Non-inertial reference frame introduces apparent accelerations (Coriolis, centrifugal). Inhibits meridional (north–south) motion, thereby imposing meridional stratification in heat and tracer distributions.

### 3. Atmospheric Composition (Salby Table 1.1)
- **Primary constituents (Dry Air):**
  - Molecular Nitrogen ($\text{N}_2$): $78.08\%$ volume mixing ratio, homogeneous, controlled by vertical mixing.
  - Molecular Oxygen ($\text{O}_2$): $20.95\%$ volume mixing ratio, homogeneous, controlled by vertical mixing.
  - Argon ($\text{Ar}$): $0.93\%$ volume mixing ratio, homogeneous, controlled by vertical mixing.
- **Variable and radiatively active trace constituents:**
  - Water vapor ($\text{H}_2\text{O}$): $\le 0.030$ ($\le 3\%$) in troposphere, highly variable, sharply decreases with height in troposphere; controlled by evaporation, condensation, transport, and photochemical oxidation of $\text{CH}_4$ in stratosphere.
  - Carbon dioxide ($\text{CO}_2$): $380\text{ ppmv}$ (in 2006 table; current $>417\text{ ppmv}$), homogeneous in troposphere, produced by surface/anthropogenic respiration/combustion.
  - Ozone ($\text{O}_3$): up to $10\text{ ppmv}$ in stratosphere; photochemical production via Chapman cycle; destroys UV radiation; secondarily present in tropospheric photochemical smog.
  - Methane ($\text{CH}_4$): $1.8\text{ ppmv}$, homogeneous in troposphere, surface production, oxidation produces $\text{H}_2\text{O}$.
  - Nitrous oxide ($\text{N}_2\text{O}$): $320\text{ ppbv}$, homogeneous in troposphere, surface/anthropogenic production, photolysis in middle atmosphere produces $\text{NO}$ (catalytic $\text{O}_3$ destruction).
  - Carbon monoxide ($\text{CO}$): $70\text{ ppbv}$, decreases upward in troposphere, anthropogenic and $\text{CH}_4$ oxidation product.
  - Halocarbons: $\text{CFC-11}$ ($0.2\text{ ppbv}$), $\text{CFC-12}$ ($0.5\text{ ppbv}$), $\text{HFC-134a}$ ($30\text{ pptv}$).

### 4. Equation of State for Pure Gases and Mixtures
- **Ideal gas equation (pure gas):**
  $$pV = n R^* T = \frac{m}{M} R^* T = m R T$$
  $$p = \rho R T, \qquad p v = R T \quad \left(v = \frac{1}{\rho}\right)$$
  where universal gas constant $R^* = 8.3145\text{ J K}^{-1}\text{ mol}^{-1}$, and specific gas constant $R = R^* / M$.
- **Mixtures and Dalton's Law:**
  The partial pressure $p_i$ and partial volume $V_i$ of constituent $i$ satisfy:
  $$p_i V = m_i R_i T, \qquad p V_i = m_i R_i T$$
  Dalton's law of partial pressures: $p = \sum_i p_i$.
  Dalton's law of partial volumes: $V = \sum_i V_i$.
  Equation of state for the mixture:
  $$pV = m R T \quad \text{with} \quad R = \frac{\sum_i m_i R_i}{m} = \frac{R^*}{M}$$
  where the mean molar weight $M$ is:
  $$M = \frac{m}{n} = \frac{\sum_i m_i}{\sum_i (m_i / M_i)} = \frac{1}{\sum_i (r_i / M_i)} = \sum_i N_i M_i$$

### 5. Absolute vs. Relative Concentration Measures
- **Absolute measures (volume-dependent):**
  - Density $\rho_i = m_i / V$.
  - Number density $[i] = n_i = \frac{N_A}{M_i} \rho_i$ (where $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$).
  - Partial pressure $p_i$.
  *Limitation:* In an expanding/compressing parcel, absolute concentrations change without any chemical source/sink.
- **Relative measures (volume-independent):**
  - Molar fraction (volume fraction): $N_i = n_i / n = p_i / p = V_i / V$.
  - Mass mixing ratio: $r_i = m_i / m_d$, where $m_d$ is the invariant mass of dry air in the parcel.
  - Trace species relation: For a species with $m_i \ll m_d$,
    $$N_i \approx \frac{r_i}{\epsilon_i}, \qquad \epsilon_i = \frac{M_i}{M_d}$$
    Volume mixing ratio (ppmv, ppbv) is approximately equal to molar fraction $N_i$.
  - **Material tracer property:** If a constituent undergoes no phase change or chemical reactions ($\dot{m}_i = 0$), its mass mixing ratio $r_i$ is materially conserved:
    $$\frac{Dr_i}{Dt} = 0$$
    Tracking $r_i$ maps fluid parcel trajectories.

### 6. Vertical Stratification and Hydrostatic Balance
- **Hydrostatic balance:** For large-scale flow where vertical accelerations are negligible ($dw/dt \ll g$ by 2–3 orders of magnitude), vertical momentum equation balances downward gravity against upward pressure gradient:
  $$\frac{dp}{dz} = -\rho g$$
- **Origin of atmospheric pressure:** The pressure at altitude $z$ equals the total weight per unit area of the overlying atmospheric column:
  $$p(z) = \int_z^\infty \rho(z') g \, dz'$$
- **Barometric law (isothermal column with scale height $H(z') = R(z')T(z')/g$):**
  $$\frac{p(z)}{p_s} = \exp\left( -\int_{z_s}^z \frac{dz'}{H(z')} \right)$$

### Further Reading
- *The Earth System*, by Lee Kump, J. Kasting, and R. Crane (3rd ed), pp. 58–62: Atmospheric composition, vertical thermal structure (troposphere, stratosphere, mesosphere, thermosphere), and radiative roles of greenhouse gases (Classroom announcement 2026-09-02).

## From the post
Reference:  Physics of the Atmosphere and Climate, M. L. Salby

## Files
- [Atmospheric_composition_Salby_lect1.pdf](https://drive.google.com/file/d/1tz4qtIguYFm4VFCQzLUVvGzhhtsiy4Il/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-atmospheric-composition-salby-lect1-1tz4qt.pdf)

## Related
- [[01-Climate/Concepts/Atmospheric Composition]]: their concept note on composition of dry air, abundance measures, and well-mixed vs trace gases
- [[01-Climate/CL05 Thermodynamic State of the Atmosphere]]: thermodynamic state, equations of state, and dry air constants
- [[01-Climate/Concepts/Ideal Gas Law]]: equation of state for air parcels
- [[01-Climate/Concepts/Mixing Ratio and Humidity]]: definition and conservation of mass mixing ratio
- [[introduction-to-climate-science/2026-09-02-study-material-moist-and-dry-air]]: Wallace and Hobbs Chapter 3 on dry and moist air thermodynamics and virtual temperature
