---
title: Landscapes Notation and Glossary
aliases: [EC2123 notation, landscapes glossary, landscapes symbol table]
subject: landscapes
type: moc
scope: [taught, extra-beyond]
by: [ai-notes, slides]
status: draft
tags: [subject/landscapes, type/moc, taught, extra/beyond, src/ai-notes, status/draft]
---
# Landscapes: Notation, Symbols, Terminology and Slide Map

Front matter of the EC2123 derivation notes, converted to the vault: how the boxes are used, the conventions, the **symbol table**, the **terminology key**, the **map from slides to chapters** and the **two places where the slides need care** (flagged `[verify]`). Back to [[Landscapes and Geomorphology - Course Map]].

\addcontentsline{toc}{chapter}{How to read these notes (key, notation, glossary)}
\markboth{Key and notation}{Key and notation}


## What this document is

These notes turn the 153-slide deck *Landscapes and Their Evolution* (EC2123, IISER Pune) into a self-contained, derivation-level text. Every equation that appears on a slide is derived, every question posed on a slide is answered, and every figure is read aloud (what is plotted, what the curves mean, what to conclude). Material that the slides only name is developed using **Anderson & Anderson** (*Geomorphology: the Mechanics and Chemistry of Landscapes*, abbreviated A&A) for surface processes and **Turcotte & Schubert** (*Geodynamics*, abbreviated T&S) for geodynamics and geophysics. Melosh (*Planetary Surface Processes*) is cited where the slides do. The order of chapters is *logical* (each chapter uses only what came before), not strictly the slide order; the table at the end of this front matter maps slides to sections.

The fluvial and aeolian chapters (Part IX) are *not* in the slide deck; they belong to the post-mid-semester syllabus and are written from the syllabus and A&A. Practice problems with full solutions are collected in the final appendix.


## Colour key for boxes


> [!derivation] 🟢 In the slides: green: a derivation that is done on the slides
> The slides carry out (or set up) this derivation. Here it is completed line by line.


> [!derivation] 🔵 Extra (not derived in the slides): red: EXTRA
> The slides quote only the *result* (or do not mention it). The derivation is given here anyway, or, if it is too long, the result is stated and marked as quoted.


> [!key] 🛠 Tool: blue: a mathematical or physical tool
> Whenever an argument needs something beyond 12th-grade mathematics/physics (partial derivatives, stress tensors, the Taylor series, similarity solutions, complex exponentials, \dots), the tool is derived once, from 12th-grade material, in a blue box, and referred to afterwards.


> [!example] ❓ Question on the slides: orange: a question asked on a slide
> Every question printed on the slides is answered in a box of this colour.


> [!example] 🖼 Reading the diagram: grey: figure walk-through
> An explanation of what a slide figure shows, panel by panel.


> [!intuition] yellow: intuition
> Used only where the mathematics is hard to *feel*.


> [!example] 🧮 Worked example: teal: worked example
> A numerical calculation with units, to calibrate orders of magnitude.


> [!key] Definition: purple: definition
> A precise definition of a term used later.


## Conventions of language and notation


- **Symbols for “about”**: $A\approx B$ means equal to within a small, controllable error; $A\sim B$ means equal in *order of magnitude* (same power of ten, all dimensionless constants of order one dropped); $A\propto B$ means $A=cB$ with $c$ constant; $A\ll B$ means $A/B\lesssim 0.1$. $\mathcal{O}\!\left(x\right)$ denotes “a quantity of size comparable to $x$”.
- **Equilibrium** means net force (or net flux) is zero. **Steady state** means nothing changes with time ($\partial_t=0$) although fluxes may be non-zero. **Stable** means a small perturbation decays; **unstable** means it grows.
- **Axes**: $z$ is vertical, positive *upward*; $x,y$ horizontal, except on slope problems where $x$ is down-slope and $y$ is normal to the bed (as on the slides).
- **Stress sign**: following the slides, *compressive stress is positive* in force-balance derivations (so $\sigma_{yy}=P$ is a pressure). Where a formula from a book uses the opposite sign this is flagged.
- **Partial derivative** $\partial_x f\equiv\partial f/\partial x$ (derived in the tool box of Chapter 2). $\dot x\equiv \mathrm{d} x/\mathrm{d} t$.
- All quantities are in **SI** unless a unit is written. Geological times: $\mathrm{ka}=10^3$ yr, $\mathrm{Ma}=10^6$ yr; “Myr” is used for durations.
- **Two clashes in the slides' notation are resolved** as follows. The slides use $\mu$ both for viscosity and for the friction coefficient; here $\mu$ is *viscosity* (Pa s) and $f=\tan\phi$ is the *friction coefficient* ($\phi$ the angle of internal friction). $\kappa$ is *thermal* diffusivity; hillslope (landscape) diffusivity is $\kappa_h$.


## Symbol table


| Symbol | Meaning | SI unit |
|---|---|---|
| $g$ | gravitational acceleration ($9.8$ at the Earth's surface) | m s$^{-2}$ |
| $G$ | Newton's gravitational constant, $6.674\times10^{-11}$ | m$^3$kg$^{-1}$s$^{-2}$ |
| $R, M, \bar\rho$ | radius, mass, mean density of a planet | m, kg, kg m$^{-3}$ |
| $\rho, \rho_c, \rho_m, \rho_w, \rho_i$ | density; crust, mantle, water, ice ($\approx 2800, 3300, 1000, 917$) | kg m$^{-3}$ |
| $\omega$ | angular velocity of rotation | rad s$^{-1}$ |
| $f_\mathrm{fl}$ or $\ell$ | flattening $(a-c)/a$ of an ellipsoid | – |
| $P$ | pressure | Pa |
| $\sigma_{ij}$ | stress tensor component (force per area on a face normal to $i$, pointing in $j$) | Pa |
| $\sigma_n, \tau$ | normal and shear stress on a plane | Pa |
| $\epsilon_{ij}, \dot\epsilon_{ij}$ | strain, strain rate | –, s$^{-1}$ |
| $\mu$ | dynamic viscosity | Pa s |
| $f=\tan\phi$ | friction coefficient; $\phi$ = angle of internal friction | –, rad |
| $C$ | cohesion (shear strength at zero normal stress) | Pa |
| $u, v, w, U$ | velocity components / speed | m s$^{-1}$ |
| $Q$ | flux (mass, volume or ice discharge per width, as defined locally) | varies |
| $\kappa, \kappa_h$ | thermal diffusivity ($\sim10^{-6}$); hillslope diffusivity | m$^2$s$^{-1}$; m$^2$yr$^{-1}$ |
| $\alpha_v$ | volumetric thermal expansion coefficient | K$^{-1}$ |
| $\mathrm{Ra}$ | Rayleigh number | – |
| $h, H$ | height / thickness (context stated) | m |
| $\theta$ | slope angle; $S=\tan\theta$ slope gradient | rad, – |
| $b$ | specific mass balance of a glacier (or depth of a crustal root, context stated) | m yr$^{-1}$ |
| $A, n$ | Glen's flow-law rate factor and exponent ($n\approx3$) | Pa$^{-n}$s$^{-1}$, – |
| $P_w$ | pore-water pressure | Pa |
| $E$ | Young's modulus (elastic) or erosion rate (context stated) | Pa or m yr$^{-1}$ |


## Terminology key


| Term | Precise meaning as used in these notes |
|---|---|
| Landscape | The shape of a piece of Earth's (or another planet's) surface, $z(x,y,t)$, together with the processes that shape it. |
| Relief | Difference between highest and lowest elevation over a stated horizontal distance. |
| Datum, geoid, ellipsoid | Reference surfaces from which elevation is measured. Geoid: an equipotential surface of gravity plus rotation approximating mean sea level. Ellipsoid: a smooth mathematical surface (oblate spheroid) fitted to the geoid. |
| DEM | Digital elevation model: elevations tabulated on a regular grid (a raster/matrix). |
| Raster / vector | Raster: values on a regular grid of cells. Vector: geometric objects (points, lines, polygons) with coordinates. |
| GIS | Geographic information system: software that stores, analyses and displays georeferenced raster and vector data (Google Earth, QGIS). |
| Slope, aspect | Magnitude and compass direction of the steepest descent of the surface. |
| Hillshade | Image of the surface shaded as if lit from a chosen direction. |
| Hypsometry | Distribution of area with elevation (histogram or cumulative curve). |
| Drainage basin | Region from which surface water flows to a given outlet. |
| Conformal map | A map projection that preserves local angles (scale is the same in all directions at a point). |
| Continuity (mass conservation) | Mass is neither created nor destroyed: rate of change in a region = inflow $-$ outflow + sources. |
| Flux | Amount of a quantity crossing unit area (or unit width) per unit time. |
| Advection / diffusion | Transport by bulk motion of a carrier / transport down a gradient by random or small-scale motion. |
| Stress | Force per area transmitted across a surface inside a material (Pa). |
| Strain, strain rate | Fractional change of length (or angle); its time derivative. |
| Viscosity, Newtonian | Resistance to shear flow; Newtonian means shear stress is proportional to strain rate. |
| Hydrostatic / lithostatic | Fluid at rest with $\partial_zP=-\rho g$; the same for the weight of overlying rock. |
| Buoyancy | Net upward force on a body immersed in a fluid, equal to the weight of the fluid displaced. |
| Isostasy | Hydrostatic-type balance of columns of crust and mantle above a compensation depth; topography floats. |
| Crust, Moho, mantle | Outer compositional shell ($\sim$7 km oceanic, $\sim$35–70 km continental); the seismic discontinuity at its base; the silicate shell below. |
| Lithosphere / asthenosphere | Cold, strong outer shell that moves as plates (crust + upper mantle) / weak, convecting mantle beneath. |
| Oblateness | Flattening at the poles due to rotation. |
| Cohesion, friction | Shear strength at zero normal load ($C$); shear strength proportional to normal load ($f\sigma_n$). |
| Rayleigh number | Dimensionless ratio measuring whether buoyancy overcomes viscous resistance and thermal diffusion. |
| Fault (normal, reverse, thrust, strike-slip) | A fracture with slip. Normal: hanging wall down (extension). Reverse: hanging wall up (compression); thrust = low-angle reverse. Strike-slip: horizontal slip. |
| Fold (anticline, syncline) | Bending of layers; anticline: arch, oldest rock in the core; syncline: trough, youngest rock in the core. |
| Orogen / passive margin | Mountain belt formed by plate collision / continental edge not at a plate boundary. |
| Uplift, exhumation, denudation | Rock uplift: upward motion of rock relative to the geoid. Exhumation: motion of rock toward the surface (relative to the surface). Denudation: removal of mass from the surface (erosion + chemical loss). |
| Weathering | In-place breakdown of rock: physical (fracturing) and chemical (reaction with water, air, biota). |
| Regolith, saprolite | Regolith: all loose/weathered material above fresh rock; saprolite: chemically weathered rock that still keeps its rock fabric. |
| Corestone | Rounded, less-weathered core of a block inside weathered rock. |
| Erosion, transport | Removal of weathered material from where it formed; its movement downhill. |
| Transport- / weathering-limited | Erosion rate limited by the ability to carry material away / by the rate at which rock is converted to mobile material. |
| Creep | Slow, continuous, slope-dependent downhill movement of regolith. |
| Landslide | Rapid failure and downslope motion of a mass of rock or soil. |
| Pore pressure, liquefaction | Pressure of water in the pores; when it approaches the total normal stress the frictional strength vanishes (liquefaction). |
| Glacier, ELA | Perennial body of flowing ice; the equilibrium-line altitude is where annual mass balance is zero. |
| Accumulation / ablation | Mass gain (snowfall, avalanches) / loss (melt, sublimation, calving) of a glacier. |
| Moraine, erratic, drumlin, esker | Ice-transported debris ridge; ice-transported boulder foreign to its site; streamlined subglacial hill; sinuous ridge of subglacial stream sediment. |
| LGM, GIA | Last Glacial Maximum ($\sim$21 ka); glacial isostatic adjustment: viscous rebound of the mantle after ice unloading. |
| Stream power, knickpoint | Rate of energy dissipation by a river per unit length or area of bed; a steep step in a river profile that migrates upstream. |
| Saltation | Bouncing transport of sand grains by wind (or water). |


## Map of the slides onto the chapters


| Slides | Topic | Chapter |
|---|---|---|
| 1–9 | Motivation; landscapes as dynamic, earth-system objects | 1 |
| 10–20 | Google-Earth tour; exercises; course content | 1 |
| 21–34 | Local landscape; Lecture 1: DEMs, GIS, structure from motion, projections, geoid map | 3, 4 |
| 35–50 | Review of mechanics: Taylor series, force balance, hydrostatics, instability, stress, viscous flow, mass conservation | 2 |
| 40–44, 51 | Why planets are round and oblate; other planets; the geoid | 5 |
| 52–55 | Maximum topography; strength of rock; small bodies | 6 |
| 56–64 | Hypsometry, isostasy, pitch drop, ocean floor, isostatic uplift | 3, 7 |
| 65–75 | Earthquakes, volcanoes, strain rate, stress map, convection, plate speed | 8 |
| 76–95 | Mountain belts, passive margins, folds, faults, earthquake cycle, Himalaya, climate–tectonics coupling | 9, 10 |
| 96–116 | Weathering, regolith, chemical and physical weathering | 11 |
| 117–126 | Hillslope transport, diffusion equation, landslide mechanics and statistics | 12, 13 |
| 127–137 | Landslide case studies (Irshalwadi, Dharali, Chamoli, Sabche, Gorkha) | 13 |
| 138–144 | Glaciers, mass balance, ice flow | 14 |
| 145–153 | Glacial deposits, LGM imprint, Talcher, rebound, raised beaches, coral-reef sea-level record | 15 |
| Not in slides | Fluvial and aeolian landscapes (syllabus items 6, 8) | 16, 17 |


## Two places where the slides need care


1. **Viscous flow down a slope (slide 49).** As printed, the balance reads $-\mu\partial_y^2v_x+g\sin\theta=0$ and the solution $v_x=(g/\mu)\sin\theta (y^2/2-Hy)$, which is *negative* for $0<y<H$, i.e. up-slope. The correct sign, consistent with the sign convention of slide 46 and with slide 144, is $\mu\partial_y^2v_x+\rho g\sin\theta=0$ giving $v_x=(\rho g\sin\theta/\mu)(Hy-y^2/2)>0$ (also the slide divides through by $\rho$). See Chapter 2.
2. **Maximum topography of neighbouring planets (slide 54).** With the formula of slide 53 and the same constants, the “estimated” values of Mars, Venus and the Moon are reproduced ($\approx 21, 9, 49$ km), but Mercury comes out at about $22$ km, not $3.0$ km (Mercury's surface gravity is almost the same as Mars's). The slide's Mercury estimate therefore does not follow from that formula; see Chapter 6.
