---
id: introduction-to-climate-science/2026-10-14-study-material-11-transformation-from-a-rotating-to-an-inertial-coordinate
aliases: [Study material 11: Transformation from a rotating to an inertial coordinate, Marshall & Plumb Ch 6: Equations of motion for a rotating fluid]
tags: [climate, introduction-to-climate-science, fluid-dynamics, rotating-frames, coriolis-force, centrifugal-force, geopotential, solid-body-rotation]
trust_tier: agent_written
---

# Study material 11: Transformation from a rotating to an inertial coordinate

## Covered
Source: Marshall and Plumb, *Atmosphere, Ocean and Climate Dynamics*, Chapter 6: "The equations of fluid motion", Sections 6.6.1–6.6.4 ("Equations of motion for a rotating fluid") (Classroom: study material 2026-10-14).

### 1. Terminology Key
- **Inertial Reference Frame:** A non-accelerating coordinate system in which Newton's laws of motion hold in their fundamental form without the introduction of fictitious or apparent forces.
- **Rotating Reference Frame:** A coordinate system rotating at constant angular velocity vector $\boldsymbol{\Omega}$ relative to an inertial frame, in which apparent inertial accelerations (Coriolis and centrifugal) arise.
- **Material Derivative Operator ($D/Dt$):** The rate of change following a fluid parcel; identical in both frames when operating on a scalar ($\frac{D\phi}{Dt}$), but differing when operating on a vector ($\frac{D\mathbf{A}}{Dt}$) because rotating coordinate basis vectors change direction in space over time.
- **Coriolis Acceleration ($-2\boldsymbol{\Omega} \times \mathbf{u}$):** Apparent acceleration perpendicular to both the rotation vector $\boldsymbol{\Omega}$ and the relative velocity $\mathbf{u}$, deflecting moving parcels to the right in the Northern Hemisphere ($\Omega > 0$) and to the left in the Southern Hemisphere.
- **Centrifugal Acceleration ($-\boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r})$):** Outward apparent acceleration perpendicular to the axis of rotation, derivable from a scalar potential $\nabla(\frac{1}{2}\Omega^2 r^2)$.
- **Effective Gravitational Potential ($\Phi$):** The modified geopotential combining Newtonian gravitational potential $gz$ and the centrifugal potential $-\frac{1}{2}\Omega^2 r^2$.
- **Cyclonic vs. Anticyclonic Swirl:** Cyclonic swirl rotates in the same sense as the background planetary/system rotation ($\Omega > 0$, anticlockwise in NH); anticyclonic swirl rotates in the opposite sense ($\Omega < 0$, clockwise in NH).

---

### 2. General Vector Transformation Between Frames

#### A. Position and Velocity Relation
Let $\mathbf{r}$ be the position vector of a fluid parcel from an origin located on the rotation axis $\boldsymbol{\Omega}$.
The absolute velocity in the inertial frame $\mathbf{u}_{\text{in}}$ and the relative velocity in the rotating frame $\mathbf{u}_{\text{rot}}$ are related by:
$$\mathbf{u}_{\text{in}} = \mathbf{u}_{\text{rot}} + \boldsymbol{\Omega} \times \mathbf{r}$$
where $\boldsymbol{\Omega} \times \mathbf{r}$ represents the linear velocity of a point fixed in the rotating frame at position $\mathbf{r}$.

#### B. Rate of Change of Basis Vectors
In the rotating frame, let $(\hat{\mathbf{x}}, \hat{\mathbf{y}}, \hat{\mathbf{z}})$ be orthogonal unit basis vectors. Any arbitrary vector $\mathbf{A}(t)$ can be decomposed as:
$$\mathbf{A} = \hat{\mathbf{x}} A_x + \hat{\mathbf{y}} A_y + \hat{\mathbf{z}} A_z$$
In the rotating frame, the unit vectors are stationary:
$$\left( \frac{D\mathbf{A}}{Dt} \right)_{\text{rot}} = \hat{\mathbf{x}} \frac{DA_x}{Dt} + \hat{\mathbf{y}} \frac{DA_y}{Dt} + \hat{\mathbf{z}} \frac{DA_z}{Dt}$$
However, viewed from the inertial frame, the coordinate axes rotate at angular velocity $\boldsymbol{\Omega}$. In time $\delta t$, each unit vector rotates by angle $\delta\theta = \Omega \, \delta t$, so their inertial time derivatives are:
$$\left( \frac{D\hat{\mathbf{x}}}{Dt} \right)_{\text{in}} = \boldsymbol{\Omega} \times \hat{\mathbf{x}}, \quad \left( \frac{D\hat{\mathbf{y}}}{Dt} \right)_{\text{in}} = \boldsymbol{\Omega} \times \hat{\mathbf{y}}, \quad \left( \frac{D\hat{\mathbf{z}}}{Dt} \right)_{\text{in}} = \boldsymbol{\Omega} \times \hat{\mathbf{z}}$$

#### C. General Operator Transformation Rule
Differentiating $\mathbf{A}$ in the inertial frame via the product rule:
$$\left( \frac{D\mathbf{A}}{Dt} \right)_{\text{in}} = \left( \hat{\mathbf{x}} \frac{DA_x}{Dt} + \hat{\mathbf{y}} \frac{DA_y}{Dt} + \hat{\mathbf{z}} \frac{DA_z}{Dt} \right) + \left( A_x \frac{D\hat{\mathbf{x}}}{Dt} + A_y \frac{D\hat{\mathbf{y}}}{Dt} + A_z \frac{D\hat{\mathbf{z}}}{Dt} \right)_{\text{in}}$$
Substituting the basis derivatives:
$$\left( \frac{D\mathbf{A}}{Dt} \right)_{\text{in}} = \left( \frac{D\mathbf{A}}{Dt} \right)_{\text{rot}} + \boldsymbol{\Omega} \times \left( \hat{\mathbf{x}} A_x + \hat{\mathbf{y}} A_y + \hat{\mathbf{z}} A_z \right)$$
which establishes the fundamental transformation operator:
$$\left( \frac{D\mathbf{A}}{Dt} \right)_{\text{in}} = \left( \frac{D\mathbf{A}}{Dt} \right)_{\text{rot}} + \boldsymbol{\Omega} \times \mathbf{A}$$

- Setting $\mathbf{A} = \mathbf{r}$: Since $\left(\frac{D\mathbf{r}}{Dt}\right)_{\text{in}} = \mathbf{u}_{\text{in}}$ and $\left(\frac{D\mathbf{r}}{Dt}\right)_{\text{rot}} = \mathbf{u}_{\text{rot}}$, this recovers the velocity relation $\mathbf{u}_{\text{in}} = \mathbf{u}_{\text{rot}} + \boldsymbol{\Omega} \times \mathbf{r}$.

---

### 3. Transformation of Acceleration and Equations of Motion

#### A. Derivation of Inertial Acceleration
To find the acceleration following a fluid parcel in the rotating frame, apply the transformation operator to the inertial velocity vector $\mathbf{A} = \mathbf{u}_{\text{in}}$:
$$\left( \frac{D\mathbf{u}_{\text{in}}}{Dt} \right)_{\text{in}} = \left( \frac{D\mathbf{u}_{\text{in}}}{Dt} \right)_{\text{rot}} + \boldsymbol{\Omega} \times \mathbf{u}_{\text{in}}$$
Substitute $\mathbf{u}_{\text{in}} = \mathbf{u}_{\text{rot}} + \boldsymbol{\Omega} \times \mathbf{r}$:
$$\left( \frac{D\mathbf{u}_{\text{in}}}{Dt} \right)_{\text{in}} = \left[ \frac{D}{Dt} \left( \mathbf{u}_{\text{rot}} + \boldsymbol{\Omega} \times \mathbf{r} \right) \right]_{\text{rot}} + \boldsymbol{\Omega} \times \left( \mathbf{u}_{\text{rot}} + \boldsymbol{\Omega} \times \mathbf{r} \right)$$
Assuming $\boldsymbol{\Omega}$ is uniform and constant in time ($D\boldsymbol{\Omega}/Dt = 0$):
$$\left( \frac{D\mathbf{u}_{\text{in}}}{Dt} \right)_{\text{in}} = \left( \frac{D\mathbf{u}_{\text{rot}}}{Dt} \right)_{\text{rot}} + \boldsymbol{\Omega} \times \left( \frac{D\mathbf{r}}{Dt} \right)_{\text{rot}} + \boldsymbol{\Omega} \times \mathbf{u}_{\text{rot}} + \boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r})$$
Since $(D\mathbf{r}/Dt)_{\text{rot}} = \mathbf{u}_{\text{rot}}$, the second and third terms combine to give $2\boldsymbol{\Omega} \times \mathbf{u}_{\text{rot}}$:
$$\left( \frac{D\mathbf{u}_{\text{in}}}{Dt} \right)_{\text{in}} = \left( \frac{D\mathbf{u}_{\text{rot}}}{Dt} \right)_{\text{rot}} + 2\boldsymbol{\Omega} \times \mathbf{u}_{\text{rot}} + \boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r})$$

#### B. Navier–Stokes Equation in a Rotating Frame
In the inertial frame, the equation of motion for a fluid parcel is:
$$\left( \frac{D\mathbf{u}_{\text{in}}}{Dt} \right)_{\text{in}} = -\frac{1}{\rho}\nabla p - g\hat{\mathbf{z}} + \mathbf{F}$$
where $-\frac{1}{\rho}\nabla p$ is the pressure gradient force, $-g\hat{\mathbf{z}}$ is true Newtonian gravity, and $\mathbf{F}$ represents viscous friction.
Substituting the acceleration transformation and dropping the subscript "rot" (so $\mathbf{u} \equiv \mathbf{u}_{\text{rot}}$):
$$\frac{D\mathbf{u}}{Dt} + \frac{1}{\rho}\nabla p + g\hat{\mathbf{z}} = \underbrace{-2\boldsymbol{\Omega} \times \mathbf{u}}_{\text{Coriolis acceleration}} \underbrace{-\boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r})}_{\text{Centrifugal acceleration}} + \mathbf{F}$$

---

### 4. Properties of the Apparent Accelerations

#### A. Centrifugal Acceleration and Modified Gravity ($\Phi$)
- **Direction:** $-\boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r}) = \Omega^2 \mathbf{r}_\perp$, directed perpendicularly outward from the rotation axis.
- **Potential Representation:**
  Because $\mathbf{r}_\perp = \nabla(r^2 / 2)$, centrifugal acceleration can be expressed as the gradient of a scalar potential:
  $$-\boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r}) = \nabla \left( \frac{\Omega^2 r^2}{2} \right)$$
  where $r$ is the perpendicular distance from the axis of rotation.
- **Modified Gravitational Potential (Geopotential):**
  Centrifugal acceleration is combined with true Newtonian gravity ($g\hat{\mathbf{z}} = \nabla(gz)$):
  $$\nabla\Phi = \nabla(gz) - \nabla\left( \frac{\Omega^2 r^2}{2} \right) = \nabla \left( gz - \frac{\Omega^2 r^2}{2} \right)$$
  where:
  $$\Phi = gz - \frac{\Omega^2 r^2}{2}$$
  is the **effective geopotential** measured on the rotating platform.
- **Compact Rotating Navier–Stokes Equation:**
  $$\frac{D\mathbf{u}}{Dt} + \frac{1}{\rho}\nabla p + \nabla\Phi = -2\boldsymbol{\Omega} \times \mathbf{u} + \mathbf{F}$$

#### B. Coriolis Acceleration ($-2\boldsymbol{\Omega} \times \mathbf{u}$)
- **Direction and Sense:**
  - In an anticlockwise rotating system ($\boldsymbol{\Omega} > 0$, Northern Hemisphere), $-2\boldsymbol{\Omega} \times \mathbf{u}$ acts perpendicularly to the right of the velocity vector $\mathbf{u}$.
  - In a clockwise rotating system ($\boldsymbol{\Omega} < 0$, Southern Hemisphere), it acts to the left.
- **Workless Property:**
  Taking the scalar product of the Coriolis force per unit mass with the relative velocity $\mathbf{u}$:
  $$\left( -2\boldsymbol{\Omega} \times \mathbf{u} \right) \cdot \mathbf{u} \equiv 0$$
  by vector orthogonality.
  **Fundamental Consequence:** The Coriolis force does zero work on fluid parcels. It cannot alter the kinetic energy ($d(u^2/2)/dt = 0$ from Coriolis), acting purely to deflect the direction of motion.

---

### 5. Parabolic Equipotential Surface in Solid-Body Rotation (GFD Lab IV)

Consider a tank of fluid rotating at constant angular rate $\Omega$ around a vertical axis.
- When left undisturbed, friction eliminates relative motion ($\mathbf{u} = 0, \mathbf{F} = 0$), establishing **solid-body rotation**.
- The equation of motion reduces to:
  $$\frac{1}{\rho}\nabla p + \nabla\Phi = 0$$
- For an incompressible fluid ($\rho = \text{constant}$):
  $$\nabla \left( \frac{p}{\rho} + \Phi \right) = 0 \implies \frac{p}{\rho} + \Phi = \text{constant}$$
  Surfaces of constant pressure ($p = \text{constant}$) must coincide exactly with surfaces of constant effective geopotential ($\Phi = \text{constant}$).
- **Free Surface Equation:**
  At the free surface, atmospheric pressure is uniform ($p = 0$). Setting $\Phi = \text{constant}$:
  $$gz - \frac{\Omega^2 r^2}{2} = \text{constant}$$
  At the rotation axis ($r = 0$), let the water depth be $z = h(0)$:
  $$\text{constant} = g h(0)$$
  Solving for the free surface height $z(r)$:
  $$z(r) = h(0) + \frac{\Omega^2 r^2}{2g}$$
  The free surface of a fluid in solid-body rotation deforms into a perfect **paraboloid of revolution**, rising toward the outer rim.

---

### 6. Summary Comparison Table

| Term | Mathematical Expression | Nature | Conserved / Work Property | Direction |
| :--- | :--- | :--- | :--- | :--- |
| **Material Derivative** | $(D\mathbf{A}/Dt)_{\text{in}} = (D\mathbf{A}/Dt)_{\text{rot}} + \boldsymbol{\Omega} \times \mathbf{A}$ | Kinematic transformation | Invariant for scalars; extra cross product for vectors | Along vector rate of change |
| **Centrifugal Acceleration** | $-\boldsymbol{\Omega} \times (\boldsymbol{\Omega} \times \mathbf{r}) = \nabla(\frac{1}{2}\Omega^2 r^2)$ | Apparent inertial acceleration | Conservative; combined into geopotential $\Phi = gz - \frac{1}{2}\Omega^2 r^2$ | Radially outward from rotation axis |
| **Coriolis Acceleration** | $-2\boldsymbol{\Omega} \times \mathbf{u}$ | Apparent inertial acceleration | Strictly workless: $(-2\boldsymbol{\Omega}\times\mathbf{u})\cdot\mathbf{u} = 0$ | Normal to $\mathbf{u}$ (right in NH, left in SH) |
| **Solid-Body Rotation Surface** | $z(r) = h(0) + \frac{\Omega^2 r^2}{2g}$ | Hydrostatic balance in rotating frame | Isobars align with equipotential surfaces ($\nabla(p/\rho + \Phi) = 0$) | Parabolic elevation upward with radius |

---

## From the post
Reference: Atmosphere, Ocean and Climate dynamics by J. Marshall and A. Plumb

## Files
- [Transformstion_from_rotating_to_inertial_coordinate_Marshall_and_Plumb.pdf](https://drive.google.com/file/d/1C9LONEMXPJk8FMUPMI7eqE4eNg7e-VhB/view?usp=drive_web)

## Related
- [[01-climate/cl12-rotating-frames-and-the-coriolis-force]]: detailed chapter note on rotating frames, the Coriolis acceleration, and laboratory demonstrations.
- [[01-climate/concepts/coriolis-force]]: dedicated concept card for Coriolis dynamics and the Rossby number.
- [[01-climate/cl13-horizontal-motion-geostrophic-balance-and-friction]]: next chapter note covering geostrophic balance resulting from Coriolis-PGF equilibrium.
