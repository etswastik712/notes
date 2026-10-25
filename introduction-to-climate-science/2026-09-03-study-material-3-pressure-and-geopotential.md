---
id: introduction-to-climate-science/2026-09-03-study-material-3-pressure-and-geopotential
aliases: [Study material-3: Pressure and Geopotential, Pressure and Geopotential (Wallace & Hobbs)]
tags: [climate, introduction-to-climate-science, atmospheric-thermodynamics, hydrostatics, geopotential, hypsometric-equation, wallace-and-hobbs]
trust_tier: agent_written
---

# Study material-3: Pressure and Geopotential

## Covered
Source: Wallace, J. M. and Hobbs, P. V., *Atmospheric Science: An Introductory Survey* (2nd ed), Section 3.2: The Hydrostatic Equation, pp. 67–70 (Classroom: Study material-3, 2026-09-03).

### 1. The Hydrostatic Equation
Atmospheric pressure at any height equals the downward force per unit area exerted by the weight of all overlying air.
For an air slab of unit horizontal cross-sectional area between heights $z$ and $z + \delta z$:
- Downward gravitational force: $g \rho \delta z$.
- Net upward pressure force: $-\delta p = p(z) - p(z + \delta z)$.
In the absence of vertical acceleration (hydrostatic balance), upward pressure gradient force exactly balances downward gravity:
$$\frac{\partial p}{\partial z} = -\rho g = -\frac{g}{\alpha}$$
where $\alpha \equiv 1/\rho$ is specific volume. In differential form:
$$g \, dz = -\alpha \, dp$$

**Pressure as vertical column weight:**
Integrating from height $z$ to top of atmosphere ($z \to \infty$ where $p \to 0$):
$$p(z) = \int_z^\infty g \rho \, dz'$$
Standard atmospheric pressure at sea level is $1.013 \times 10^5\text{ Pa} = 1013\text{ hPa} = 1\text{ atm}$.

### 2. Geopotential ($\Phi$) and Geopotential Height ($Z$)
- **Geopotential $\Phi$:**
  Defined as the work required against Earth's gravitational field to raise a unit mass ($1\text{ kg}$) from sea level ($z = 0$) to height $z$:
  $$d\Phi = g \, dz = -\alpha \, dp = -R_d T_v \frac{dp}{p}$$
  $$\Phi(z) = \int_0^z g(z') \, dz'$$
  Units: $\text{J kg}^{-1}$ or $\text{m}^2\text{ s}^{-2}$. The geopotential is a state property depending solely on height, independent of path.
- **Geopotential Height $Z$:**
  Defined by dividing geopotential by standard globally averaged sea-level gravity $g_0 \equiv 9.80665\text{ m s}^{-2}$ (typically taken as $9.81\text{ m s}^{-2}$):
  $$Z \equiv \frac{\Phi(z)}{g_0} = \frac{1}{g_0}\int_0^z g(z') \, dz'$$
  *Geometric vs. Geopotential height:* In the lower atmosphere ($z \le 10\text{ km}$), $g \approx g_0$, so $Z \approx z$ (at $z = 10\text{ km}$, $Z = 9.99\text{ km}$; at $z = 100\text{ km}$, $Z = 98.47\text{ km}$). Geopotential height is the natural vertical coordinate in dynamic meteorology and energy budgets.
- **Geopotential Thickness between isobaric surfaces:**
  Integrating between pressure levels $p_1$ and $p_2$ ($p_1 > p_2$):
  $$\Phi_2 - \Phi_1 = -R_d \int_{p_1}^{p_2} T_v \frac{dp}{p} = R_d \int_{p_2}^{p_1} T_v \frac{dp}{p}$$
  $$Z_2 - Z_1 = \frac{R_d}{g_0} \int_{p_2}^{p_1} T_v \frac{dp}{p} = \frac{R_d}{g_0} \int_{p_2}^{p_1} T_v \, d\ln p$$
  The quantity $\Delta Z = Z_2 - Z_1$ is the **geopotential thickness** of the layer.

### 3. Scale Height ($H$) and the Hypsometric Equation
- **Mean layer virtual temperature $\bar{T}_v$:**
  With respect to $\ln p$:
  $$\bar{T}_v \equiv \frac{\int_{p_2}^{p_1} T_v \, d\ln p}{\int_{p_2}^{p_1} d\ln p} = \frac{\int_{p_2}^{p_1} T_v \, d\ln p}{\ln(p_1 / p_2)}$$
- **The Hypsometric Equation:**
  $$Z_2 - Z_1 = \frac{R_d \bar{T}_v}{g_0} \ln\left(\frac{p_1}{p_2}\right) = \bar{H} \ln\left(\frac{p_1}{p_2}\right)$$
  **Fundamental principle:** Geopotential thickness between two fixed pressure surfaces is directly proportional to the mean virtual temperature of the intervening layer. Warm air columns are buoyant and expand vertically (thick layer); cold air columns contract vertically (thin layer).
- **Scale Height $H$:**
  $$H \equiv \frac{R_d T}{g_0} \approx \frac{287.0}{9.81} T \approx 29.3 \, T\text{ meters}$$
  For mean atmospheric temperature $T \approx 255\text{ K}$, $H \approx 7.5\text{ km}$.
- **Isothermal atmosphere pressure profile:**
  $$p(Z) = p_1 \exp\left( -\frac{Z - Z_1}{H} \right)$$
  Pressure decreases by a factor of $e$ for each altitude increment of one scale height $H$.

### 4. The Turbopause and Diffusive Separation
- **Below the turbopause (~105 km):**
  Intense turbulent and eddy mixing keeps the atmosphere thoroughly mixed. Apparent molecular weight remains constant at $M_d = 28.97\text{ g mol}^{-1}$. Consequently, all gases decrease with altitude at the same rate and share a common bulk scale height $H$.
- **Above the turbopause (>105 km):**
  Molecular diffusion dominates over eddy mixing. Each gaseous species stratifies independently according to its own individual molecular scale height:
  $$H_i = \frac{R_i T}{g} = \frac{R^* T}{M_i g}$$
  Because $H_i \propto 1/M_i$, heavier gases ($\text{N}_2, \text{O}_2$) have smaller scale heights and fall off exponentially faster with altitude, while light gases ($\text{He}, \text{H}$) have large scale heights and dominate the exosphere.

## From the post
(no text)

## Files
- [Circulation_Pressure_and_geopotential_WH_lect2.pdf](https://drive.google.com/file/d/1L16vSi1xnaIRU4VoyI9wQb8sayQU0HJ4/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-circulation-pressure-and-geopotential-wh-lect2-1L16vS.pdf)

## Related
- [[01-Climate/Concepts/Hydrostatic Balance]]: their concept note on hydrostatic equilibrium and scale analysis
- [[01-Climate/Concepts/Geopotential]]: definition of geopotential and geopotential height
- [[01-Climate/Concepts/Hypsometric Equation]]: layer thickness and sounding interpretation
- [[01-Climate/CL06 Hydrostatic Balance and Vertical Structure]]: vertical coordinates, geopotential, and scale heights
- [[introduction-to-climate-science/2026-09-02-study-material-moist-and-dry-air]]: virtual temperature derivation used in the hypsometric equation
