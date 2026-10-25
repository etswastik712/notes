---
id: introduction-to-climate-science/2026-09-09-study-material-4-pressure-gradient-force
aliases: [Study material 4: Pressure gradient force, Pressure gradient force (Holton & Hakim)]
tags: [climate, introduction-to-climate-science, dynamic-meteorology, pressure-gradient-force, fundamental-forces, holton-and-hakim]
trust_tier: agent_written
---

# Study material 4: Pressure gradient force

## Covered
Source: Holton, J. R. and Hakim, G. J., *An Introduction to Dynamic Meteorology* (5th ed, 2013), Chapter 1: Introduction, Section 1.4: Fundamental Forces, pp. 5–7 (Classroom: Study material 4, 2026-09-09).

### 1. Classification of Atmospheric Forces
In dynamic meteorology, forces governing fluid parcel motion are classified into:
- **Body forces:** Act directly on the center of mass of the fluid parcel. Their magnitudes are proportional to the parcel's mass (e.g., gravitational attraction).
- **Surface forces:** Act across the boundary surface separating a fluid parcel from surrounding fluid. Their magnitudes are proportional to surface area and independent of the parcel's mass (e.g., normal pressure force, tangential viscous shear stress).

### 2. Fundamental Forces and Reference Frames
- **Inertial frame fundamental forces:**
  By Newton's second law of motion ($\mathbf{a} = \sum \mathbf{F}/m$), three fundamental forces govern atmospheric motions:
  1. Pressure gradient force
  2. Gravitational force
  3. Frictional / viscous force
- **Rotating Earth frame:**
  Because the Earth rotates with angular velocity $\boldsymbol{\Omega}$, it is a non-inertial frame. Applying Newton's second law requires including apparent inertial forces:
  - Centrifugal force: directed radially outward from the axis of rotation ($\boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r})$).
  - Coriolis force: acts perpendicularly to velocity ($-2\boldsymbol{\Omega} \times \mathbf{v}$).

### 3. Scales of Atmospheric Motions (Holton & Hakim Table 1.4)
Horizontal motion in the atmosphere spans 14 orders of magnitude:
- Molecular mean free path: $10^{-7}\text{ m}$
- Minute turbulent eddies: $10^{-2}\text{ to }10^{-1}\text{ m}$
- Small eddies: $10^{-1}\text{ to }1\text{ m}$
- Dust devils: $1\text{ to }10\text{ m}$
- Gusts: $10\text{ to }10^2\text{ m}$
- Tornadoes: $10^2\text{ m}$
- Cumulonimbus clouds: $10^3\text{ m}$
- Fronts, squall lines: $10^4\text{ to }10^5\text{ m}$
- Hurricanes (tropical cyclones): $10^5\text{ m}$
- Synoptic cyclones (extratropical weather systems): $10^6\text{ m}$
- Planetary waves (Rossby waves): $10^7\text{ m}$

### 4. Derivation of the Pressure Gradient Force (PGF)
Consider an infinitesimal fluid parcel $\delta V = \delta x \delta y \delta z$ centered at $(x_0, y_0, z_0)$ with central pressure $p_0$.
Momentum is transferred normal to the boundaries by random molecular collisions.
- **Pressure at face A ($x_0 + \delta x/2$):**
  Expanding in a Taylor series about $(x_0, y_0, z_0)$ and retaining first-order terms:
  $$p_A = p_0 + \frac{\partial p}{\partial x} \frac{\delta x}{2}$$
  The area of face A is $\delta y \delta z$. The pressure force points inward ($-x$ direction):
  $$F_{Ax} = -\left( p_0 + \frac{\partial p}{\partial x} \frac{\delta x}{2} \right) \delta y \delta z$$
- **Pressure at face B ($x_0 - \delta x/2$):**
  $$p_B = p_0 - \frac{\partial p}{\partial x} \frac{\delta x}{2}$$
  The pressure force points inward ($+x$ direction):
  $$F_{Bx} = +\left( p_0 - \frac{\partial p}{\partial x} \frac{\delta x}{2} \right) \delta y \delta z$$
- **Net force in $x$-direction:**
  $$F_x = F_{Ax} + F_{Bx} = -\frac{\partial p}{\partial x} \delta x \delta y \delta z$$
- **Force per unit mass:**
  With parcel mass $m = \rho \delta V = \rho \delta x \delta y \delta z$:
  $$\frac{F_x}{m} = -\frac{1}{\rho}\frac{\partial p}{\partial x}$$
- **Three-dimensional vector form:**
  By identical derivations along $y$ and $z$:
  $$\frac{F_y}{m} = -\frac{1}{\rho}\frac{\partial p}{\partial y}, \qquad \frac{F_z}{m} = -\frac{1}{\rho}\frac{\partial p}{\partial z}$$
  $$\frac{\mathbf{F}_{pg}}{m} = -\frac{1}{\rho} \nabla p = -\frac{1}{\rho} \left( \frac{\partial p}{\partial x}\mathbf{i} + \frac{\partial p}{\partial y}\mathbf{j} + \frac{\partial p}{\partial z}\mathbf{k} \right)$$
- **Physical principle:** The force per unit mass depends on the spatial gradient of pressure ($\nabla p$), not on the ambient pressure magnitude $p$. Parcels are accelerated down the gradient from high pressure to low pressure.

### 5. Gravitational Force
Newton's law of universal gravitation between Earth (mass $M$) and fluid element (mass $m$) separated by distance $r$ along position vector $\mathbf{r}$ directed from Earth center to parcel:
$$\mathbf{F}_g = -\frac{G M m}{r^2} \frac{\mathbf{r}}{r}$$
where $G = 6.674 \times 10^{-11}\text{ N m}^2\text{ kg}^{-2}$ is the universal gravitational constant.
Gravitational force per unit mass (true gravity $\mathbf{g}^*$):
$$\mathbf{g}^* \equiv \frac{\mathbf{F}_g}{m} = -\frac{G M}{r^2}\frac{\mathbf{r}}{r}$$
At the Earth's surface ($r = a \approx 6.37 \times 10^6\text{ m}$), $g^* \approx 9.81\text{ m s}^{-2}$.

## From the post
Reference: Holton and Hakim (2013) Dynamic Meteorology. 

## Files
- [Atmos_Circulation_Pressure_gradient_force_letc4.pdf](https://drive.google.com/file/d/1nBjYr42_J-FBCCpGJC2cQfymTvZh5dXh/view?usp=drive_web) (saved as introduction-to-climate-science/2026-10-25-atmos-circulation-pressure-gradient-force-letc4-1nBjYr.pdf)

## Related
- [[01-Climate/Concepts/Pressure Gradient Force]]: their concept note on PGF derivation and scaling
- [[01-Climate/Concepts/Scales of Atmospheric Motion]]: horizontal scales of motion from turbulent eddies to planetary waves
- [[01-Climate/CL06 Hydrostatic Balance and Vertical Structure]]: vertical component of PGF balancing gravity ($-\frac{1}{\rho}\frac{\partial p}{\partial z} - g = 0$)
- [[01-Climate/CL12 Rotating Frames and the Coriolis Force]]: apparent forces in rotating reference frames
- [[01-Climate/CL13 Horizontal Motion - Geostrophic Balance and Friction]]: horizontal balance between PGF and Coriolis force
