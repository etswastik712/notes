---
id: introduction-to-climate-science/2026-10-22-study-material-13-geostrophic-motion
aliases: [Study material 13: Geostrophic motion]
tags: [climate, ec2113, balanced-flow, geostrophic]
trust_tier: agent_written
---

# Study material 13: Geostrophic motion

## Covered
Source: Marshall & Plumb, *Atmosphere, Ocean and Climate Dynamics*, Ch. 7 "Balanced flow", §7.1 (pp. 110–115 of the PDF). (Classroom: Study material 13)

- **Scaling of the horizontal momentum equation** (free atmosphere/ocean, friction negligible): $\frac{D\mathbf{u}}{Dt}+f\hat{\mathbf{z}}\times\mathbf{u}=-\frac{1}{\rho}\nabla p$. The acceleration terms scale as $\partial\mathbf u/\partial t\sim \mathcal U/\mathcal T$ and $\mathbf u\cdot\nabla\mathbf u\sim\mathcal U^2/L$; the Coriolis term scales as $f\mathcal U$. Typical large-scale values: $\mathcal U\sim10$ m s$^{-1}$, $L\sim10^6$ m, $\mathcal T\sim10^5$ s, so $\mathcal U/\mathcal T\approx\mathcal U^2/L\sim10^{-4}$ m s$^{-2}$ (the advective time scale is $L/\mathcal U$). Vertical advection contributes negligibly to $\mathbf u\cdot\nabla\mathbf u$.
- **Rossby number:** $R_o=\dfrac{\mathcal U}{fL}$, the ratio of acceleration to Coriolis terms. At mid-latitudes ($\sim45^\circ$) $f=2\Omega/\sqrt2\simeq1.03\times10^{-4}$ s$^{-1}$, so $R_o\simeq0.1$ for the atmosphere and $R_o\simeq10^{-3}$ for large-scale ocean circulation (§9.3). The small-$R_o$ assumption breaks down near the equator where $f\to0$.
- **Geostrophic balance** (small $R_o$): $f\hat{\mathbf z}\times\mathbf u+\frac1\rho\nabla p=0$. Defining the geostrophic wind as the velocity that exactly satisfies this, $\mathbf u\simeq\mathbf u_g$ with
  $$\mathbf u_g=\frac{1}{f\rho}\hat{\mathbf z}\times\nabla p,\qquad (u_g,v_g)=\Big(-\frac{1}{f\rho}\frac{\partial p}{\partial y},\ \frac{1}{f\rho}\frac{\partial p}{\partial x}\Big).$$
- **Direction and magnitude:** the flow is normal to the pressure gradient, i.e. along isobars. For $f>0$ it is clockwise around a high and anticlockwise around a low (opposite in the Southern Hemisphere). **Buys-Ballot's law:** with your back to the wind in the Northern Hemisphere, low pressure is on your left (right in the Southern Hemisphere). $|\mathbf u_g|=\frac{1}{f\rho}|\nabla p|=\frac{1}{f\rho}\frac{\delta p}{\delta s}\propto(\delta s)^{-1}$: the flow is strongest where isobars are closest together; it does not cross isobars (like a river between banks).
- **Non-divergence:** for $f$ nearly constant (scales $\lesssim1000$ km), $\frac{\partial u_g}{\partial x}+\frac{\partial v_g}{\partial y}=0$. By continuity $\partial w_g/\partial z=0$, so with $w_g=0$ at a flat boundary the geostrophic flow is horizontal. Variations of $f$ matter for planetary-scale motions (§10.2.1).
- **Geostrophic wind in pressure coordinates (§7.1.1):** using hydrostatic balance, $(\partial p/\partial x)_z=g\rho(\partial z/\partial x)_p$ (and the same for $y$), so
  $$\mathbf u_g=\frac gf\hat{\mathbf z}_p\times\nabla_pz,\qquad (u_g,v_g)=\Big(-\frac gf\frac{\partial z}{\partial y},\ \frac gf\frac{\partial z}{\partial x}\Big),$$
  in which $\rho$ does not appear. In pressure coordinates $\nabla_p\cdot\mathbf u_g=0$ for constant $f$, with streamfunction $\psi_g=\frac gf z$ ($u_g=-\partial\psi_g/\partial y$, $v_g=\partial\psi_g/\partial x$). Height contours are therefore **streamlines of the geostrophic flow** on pressure surfaces.
- **Worked estimates:**
  - 500 mb surface slopes down by $\Delta z=800$ m over $L=5000$ km (Fig. 5.13): $u=\frac gf\frac{\Delta z}{L}=\frac{9.81}{10^{-4}}\times\frac{800}{5\times10^6}\approx15$ m s$^{-1}$, enough to balance the poleward pressure force from the pole-to-equator temperature gradient.
  - Synoptic chart (500 mb, 21 June 2003, Fig. 7.4), point near 43° N, 133° W: height falls 60 m in 250 km (1° latitude = 111 km), $f=9.7\times10^{-5}$ s$^{-1}$, giving $g\Delta z/(fL)=\frac{9.81}{9.7\times10^{-5}}\times\frac{60}{2.5\times10^5}=24$ m s$^{-1}$, against the observed 25 m s$^{-1}$. $R_o=|\mathbf u\cdot\nabla\mathbf u|/|f\mathbf u|\approx0.1$ over most of the region but approaches 1 in strong cyclones (Fig. 7.5).
- **Vertical component:** $w_g=0$ is not deducible from the horizontal balance alone; it follows from the continuity argument above.
- The chapter also announces the thermal wind equation, density-varying fluids and ageostrophic flow near boundaries; the file read here ends before those sections.

## From the post
Reference: Atmosphere, Ocean, Climate Dynamics: J. Marshall, and A. Plumb

## Files
- [Geostrophic_motion_Marshall_and_Plumb.pdf](https://drive.google.com/file/d/1MfwAOGLD4q0qHoD2etSeaXHh8PE_sT_f/view?usp=drive_web): read as page images (text did not extract); equations typed from the page images, so check against the PDF.

## Related
- [[introduction-to-climate-science/2026-10-14-study-material-11-transformation-from-a-rotating-to-an-inertial-coordinate]]: the Coriolis term $-2\boldsymbol\Omega\times\mathbf u$ whose balance with the pressure gradient is used here
- [[introduction-to-climate-science/2026-09-09-study-material-4-pressure-gradient-force]]: the pressure gradient force per unit mass
- [[introduction-to-climate-science/2026-09-03-study-material-3-pressure-and-geopotential]]: hydrostatic balance and geopotential, used to go to pressure coordinates
- [[introduction-to-climate-science/2026-10-22-study-material-12-large-scale-circulation-patterns]]: the observed circulation patterns that geostrophic balance explains
