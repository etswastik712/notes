---
title: LS07 Isostasy
aliases: [LS07, Isostasy]
subject: landscapes
type: chapter
chapter: 7
part: IV
scope: [taught, extra-book, extra-beyond]
by: [slides, ai-notes, book]
status: draft
tags: [subject/landscapes, type/chapter, taught, extra/book, extra/beyond, src/slides, src/ai-notes, src/book, status/draft]
---
# LS07 · Isostasy

◀ [[LS06 Maximum Topography]] · [[Landscapes and Geomorphology - Course Map|Course Map]] · next: [[LS08 Plate Tectonics Strain Stress and Convection]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught**: slides 58–64 of [[pre_ms_landscape_26.pdf|the EC2123 pre-midsem deck]] (Argha Banerjee, IISER Pune; 153 slides). Boxes marked 🟢 **In the slides** derive what the slides derive; boxes marked 🖼 **Reading the diagram** explain each slide figure panel by panel and sit directly under the slide image.
> 🔵 **Extra · beyond**: boxes marked 🔵 **Extra** complete derivations the slides only quote (from Anderson and Anderson, *Geomorphology: the Mechanics and Chemistry of Landscapes*, and Turcotte and Schubert, *Geodynamics*); 🛠 **Tool** boxes derive a mathematical tool from 12th-grade material; 🧮 **Worked example** boxes calibrate orders of magnitude.
> This chapter has 5 sections, 7 derivation boxes, 3 redrawn figures and 7 slide images.

> [!key] After this chapter you can
> - state Airy and Pratt isostasy and compute a root,
> - explain why isostasy works (mantle flow),
> - derive the thermal subsidence of the ocean floor,
> - compute the isostatic uplift caused by erosion.

> [!intuition] The one-sentence story
> Topography floats: mountains have roots like icebergs, the mantle flows to restore the balance, and an eroding mountain rises again.

```mermaid
flowchart LR
  A["gravity anomalies"] --> B["Airy isostasy: roots"]
  B --> C["why it works:<br/>mantle flows"]
  C --> D["oceans: thermal isostasy"]
  D --> E["erosion -> rebound"]
```
*Concept map: every box is a section of this chapter.*

*[Slides 58–64]*


## The idea and the data (slides 58–60)


> [!key] Definition: Isostasy
> *Isostatic equilibrium* is hydrostatic equilibrium for the crust–mantle system: on a long enough time scale the mantle behaves as a fluid (§7.3), so at some depth of compensation $Z$ the pressure is the same beneath every column, i.e. every column of overlying material has the same weight per unit area. Then topography “floats” on the mantle exactly as an iceberg floats on water (Archimedes, Chapter 2).


![[pre_058.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 58: elevation and crustal thickness maps
> Top right: a global elevation map (colour scale $-10$ to $+8$ km; purple = deep ocean, red-yellow = high land). Below it: crustal thickness on a $2^\circ\times2^\circ$ grid (0–70 km; blue = thin, red = thick). Correlate the two: crust is thin ($\sim$5–10 km) beneath the ocean basins, $\sim$30–40 km under continental interiors, and reaches $\sim$60–70 km under Tibet/Himalaya and the Andes — exactly where the elevation is highest. Thick crust $\leftrightarrow$ high topography is the signature of isostasy (§7.2). The slide poses the question “over the oceans?” – see §7.4.


<!-- ls-depth:LS07:1 -->
> [!intuition] Context: Gilbert's lake and the idea that the Earth flows
> The best natural experiment for isostasy was recognised in 1890. G. K. Gilbert noticed that the **Lake Bonneville** shoreline (Utah, formed in a geologically instant 14.5 kyr ago) is not level today: it has been raised by **more than 50 m** in the middle of the former lake, tracing a bull's-eye. The lake's weight depressed the crust; when the water went away the crust rebounded, but not instantly, because the mantle below has to *flow* back (A&A ch. 3, [[geomorphology-the-mechanics-and-chemistry-of-landscapes-9780521519786-0521519780_compress.pdf#page=62|PDF pp.61–62]]). The lesson in A&A's words: *"the timescale is determined by the viscosity of the fluid and hence serves as a probe of the mantle viscosity... for mantle materials, of the order of several thousand years"*, and **larger loads probe deeper mantle**. T&S credit Haskell (1935) with the first quantitative treatment (T&S, Bookos copy, PDF p.21: Fennoscandian beach terraces).
> *Sanity check.* Full Airy compensation of a lake $\sim300$ m deep (its maximum depth, recalled) would depress the crust by $(\rho_w/\rho_m)h=\tfrac{1000}{3300}\times300\approx91$ m, and the rebound would undo that. The observed uplift is >50 m. Do not read the shortfall as "rebound still in progress". A relaxation time of a few kyr (derived below) means that 14.5 kyr is several relaxation times, so the rebound is essentially complete. The shortfall has two other causes. (i) 300 m is the *maximum* depth; averaged over the basin the water was much shallower. (ii) The lake was only ~$10^2$ km across, a load narrow enough that the elastic lithosphere carried part of its weight instead of letting it sink fully into the mantle (flexure, [[LS10 Folds Flexure and Mountain Building]]). Both make the equilibrium depression, and hence the rebound, smaller than 91 m.


## Airy isostasy (slides 60–61)

> [!figure]- 🖼 Slides 60–61: open to see the slides this section explains
> ![[pre_060.jpg|300]] ![[pre_061.jpg|300]]


> [!derivation] 🟢 In the slides: Slide 60: a floating crustal block
> A continental block of density $\rho_c$ and total thickness $h$ floats in mantle of density $\rho_m>\rho_c$; let $b$ be the depth of its base below the surrounding mantle surface (the reference level in the slide's figure). Archimedes: weight of block $=$ weight of displaced mantle,
>
>
> $$
> \rho_c g h=\rho_m g b\quad\Longrightarrow\quad\rho_c h=\rho_m b .
> $$
>
>
> The height of the block above the reference level is
>
>
> $$
> h-b=h-\frac{\rho_c}{\rho_m}h=h\Big(1-\frac{\rho_c}{\rho_m}\Big). \tag{18}
> $$
>
>
> With $\rho_c=2800$, $\rho_m=3300$: $h-b=0.152 h$: only $15 %$ of a crustal block sticks out, $85 %$ is a root. (Equal to the iceberg rule: 8/9 hidden for ice on water.)


![[ls_fig14.png]]
*Figure LS07.1. Slide 61 (Airy compensation). Column (a) is the reference of thickness $c\approx35$ km; (b) a mountain belt of elevation $h_1$ with a crustal root $b_1$ extending below the reference Moho; (c) a marine basin of water depth $h_2$ underlain by thinned crust: the mantle rises by $b_2$ above the reference Moho. Vertical positions drawn to scale for $h_1=5$ km, $h_2=4$ km.*


> [!derivation] 🟢 In the slides: Slide 61: mountain root and basin thinning
> Equate the weight of every column above the depth of compensation $Z$ (below the deepest root).
>
> *Mountain belt.* Reference: $\rho_cc+\rho_m(Z-c)$. Mountain: crust of thickness $h_1+c+b_1$ (elevation, reference thickness, root) and mantle $Z-c-b_1$: $\rho_c(h_1+c+b_1)+\rho_m(Z-c-b_1)$. Equal:
>
>
> $$
> \rho_c(h_1+b_1)=\rho_mb_1 \Longrightarrow \boxed{b_1=\frac{\rho_c}{\rho_m-\rho_c}h_1}=5.6 h_1\quad(\rho_c=2800,\rho_m=3300).
> $$
>
>
> A $5$ km high plateau needs a $28$ km root: crust of $35+5+28\approx68$ km, the value seen under Tibet on slide 58.
>
> *Marine basin.* Water $h_2$, crust of thickness $c-h_2-b_2$, mantle from depth $c-b_2$: $\rho_wh_2+\rho_c(c-h_2-b_2)+\rho_m(Z-c+b_2)=\rho_cc+\rho_m(Z-c)$, so $(\rho_w-\rho_c)h_2+(\rho_m-\rho_c)b_2=0$:
>
>
> $$
> \boxed{b_2=\frac{\rho_c-\rho_w}{\rho_m-\rho_c}h_2}=3.6 h_2 .
> $$
>
>
> A $4$ km deep basin has crust thinned by $4+14.4\approx18$ km (to $\sim$17 km), the mantle up-bulging by $14$ km.


> [!derivation] 🔵 Extra (not derived in the slides): Pratt isostasy and the elastic-plate alternative
> **Pratt**: all columns extend to the same depth $D$ below sea level, but the density varies: column of elevation $h_i$ has density $\rho_i$ with $\rho_i(D+h_i)=\rho_0D$, i.e. $\rho_i=\rho_0D/(D+h_i)$: high topography is made of low-density rock. **Airy** (above): constant density, varying thickness. **Flexural**: the lithosphere has elastic strength, so loads are supported over a horizontal length scale (§9.5). The ocean floor, whose depth increases with age (thermal contraction of a lithosphere of fixed crustal thickness), is a Pratt-type case (§7.4).


| Model | Assumption | Predicts | Applies to |
|---|---|---|---|
| Airy (T&S Ch. 2) | constant $\rho_c$, variable thickness | root $b_1=5.6h_1$ (crust–mantle values above) | orogens, plateaus (Tibet, Andes) |
| Pratt | constant compensation depth, variable density | $\rho_i=\rho_0D/(D+h_i)$ | oceans (thermal density), swells |
| Flexural (T&S Ch. 3) | elastic lithosphere of rigidity $D_f$ | deflection over $\alpha=(4D_f/\Delta\rho g)^{1/4}$ | loads narrower than $\sim\alpha$; foreland basins, escarpments |
| Dynamic topography | mantle flow supports the surface | departures from isostasy of $\sim\pm1$ km | broad swells, subduction zones |

*Comparison of isostatic models.*


## Why isostasy works: the mantle flows (slide 59)

> [!figure]- 🖼 Slide 59: open to see the slides this section explains
> ![[pre_059.jpg|300]]


> [!example] ❓ Question on the slides: Slide 59: why should isostasy work? pitch drop experiment; viscosity of pitch? what about the mantle?
> Rock is a solid on human time scales but a viscous fluid on geological ones, just as pitch is: the “pitch drop experiment” (Univ. of Queensland, running since 1927; slide 59 shows the funnel and the black brittle solid pitch shattering under a hammer) shows a substance that shatters when struck yet flows in a funnel at $\sim0.1$ drops per year. A viscosity estimate follows from the flow rate through the stem.


> [!derivation] 🔵 Extra (not derived in the slides): Viscosity of pitch (Hagen–Poiseuille) and the time scale of viscous relaxation
> **Flow in a tube.** In a steady flow along a tube of radius $a$ and length $L$ with pressure drop $\Delta P$, a cylinder of fluid of radius $r$ has pressure force $\pi r^2\Delta P$ balanced by the shear on its surface, $2\pi rL\tau$; so $\tau=\Delta Pr/2L$. With $\tau=-\mu \mathrm{d} v/\mathrm{d} r$: $v=\Delta P(a^2-r^2)/4\mu L$ (no slip at $r=a$), and the volume flow
>
>
> $$
> Q=\int_0^av 2\pi r \mathrm{d} r=\frac{\pi a^4\Delta P}{8\mu L},\qquad\text{so}\qquad\mu=\frac{\pi a^4\Delta P}{8LQ}.
> $$
>
>
> *Numbers (assumed geometry, order of magnitude only)*: $a=4$ mm, $L=3$ cm, head of pitch $5$ cm so $\Delta P\approx\rho gH=1100\cdot9.8\cdot0.05=540$ Pa; one drop of $\sim1 \mathrm{cm^3}$ per $10$ yr gives $Q=10^{-7} \mathrm{m^3/yr}=3\times10^{-15} \mathrm{m^3/s}$. Then $\mu\approx6\times10^8$ Pa s; careful measurements give $\sim2\times10^8$ Pa s ($\sim2\times10^{11}$ times water). The mantle is $\sim10^{13}$ times more viscous than pitch and yet deforms because it has $10^{9}$–$10^{10}$ years.
>
> **Relaxation of topography on a viscous half-space.** The answer to “how fast does isostasy respond” needs the normal force a moving viscous fluid exerts on its boundary. Let the fluid occupy $z>0$ and let its boundary move with vertical velocity $V\cos kx$ ($V>0$ into the fluid) with no shear stress on the boundary. Use a stream function $\psi$ with $u=\partial_z\psi$, $w=-\partial_x\psi$ (this automatically satisfies $\partial_xu+\partial_zw=0$). The Stokes equations reduce to $\nabla^4\psi=0$. The solution decaying at depth is $\psi=(A+Bz)\mathrm{e}^{-kz}\sin kx$. Boundary conditions at $z=0$: (i) $w=V\cos kx\Rightarrow-kA=V$; (ii) zero shear traction $\partial_z u+\partial_xw=\partial_z^2\psi-\partial_x^2\psi=0\Rightarrow(k^2A-2kB)+k^2A=0\Rightarrow B=kA$. So $\psi=-\tfrac Vk(1+kz)\mathrm{e}^{-kz}\sin kx$. Then $u=\partial_z\psi=Vkz \mathrm{e}^{-kz}\sin kx$ and $w=-\partial_x\psi=V(1+kz)\mathrm{e}^{-kz}\cos kx$. The pressure follows from the $x$-momentum equation $\partial_xP=\mu\nabla^2u$ (the perturbation pressure, hydrostatic part removed): $\partial_x^2u=-k^2u$ and $\partial_z^2u=Vk(k^2z-2k)\mathrm{e}^{-kz}\sin kx$ add to $\nabla^2u=-2Vk^2\mathrm{e}^{-kz}\sin kx$, so $P=2\mu Vk \mathrm{e}^{-kz}\cos kx$, i.e. $P(0)=2\mu kV\cos kx$. At $z=0$ the vertical strain rate $\partial_zw=-Vk^2z \mathrm{e}^{-kz}\cos kx$ vanishes, so the normal stress the fluid exerts on the boundary is $\sigma_{zz}=-P+2\mu\partial_zw=-2\mu kV\cos kx$ (tension positive), a compression: *the fluid resists a boundary moving into it with a pressure $2\mu k$ times the boundary velocity*.
>
> Now a topographic load: surface elevation $w(x,t)=w_0(t)\cos kx$ of a fluid of density $\rho$ (crust/mantle). The excess weight per area $\rho gw$ presses on the fluid below and is balanced by the viscous resistance $2\mu k |\dot w|$ as the surface sinks ($\dot w<0$):
>
>
> $$
> \rho g w=-2\mu k \dot w \Longrightarrow w=w_0\mathrm{e}^{-t/\tau_r},\qquad\boxed{ \tau_r=\frac{2\mu k}{\rho g}=\frac{4\pi\mu}{\rho g\lambda} }\quad(\lambda=2\pi/k).
> $$
>
>
> Scaling check: the same result to within $4\pi$ follows from “viscous stress $\mu\dot w/\lambda\sim$ load $\rho gw$” (cf. slide 48). **Numbers**: $\mu=10^{21}$ Pa s, $\rho=3300$: $\lambda=1000$ km gives $\tau_r=1.2\times10^4$ yr; $\lambda=3000$ km gives $4\times10^3$ yr; $\lambda=100$ km gives $1.2\times10^5$ yr. Broad features are isostatically compensated within $10^3$–$10^4$ yr, i.e. almost instantly on geological time scales; short-wavelength features (mountains) are held up by the elastic strength of the lithosphere (flexure) instead of flowing away.


<!-- ls-depth:LS07:2 -->
> [!derivation] 🔵 Extra (computed): which description is right, elastic or viscous? Relaxation time versus Maxwell time
> The viscous half-space result of this chapter, $\tau_r=4\pi\mu/(\rho g\lambda)$, assumes the mantle is a pure fluid. The Maxwell model of [[LS02 Mechanics and Mathematics Toolkit]] says it is a fluid only on time scales longer than $\tau_M=\mu/G\approx450$ yr. Compare the two:
> $$\frac{\tau_r}{\tau_M}=\frac{4\pi G}{\rho g\lambda}=\frac{27\,200\ \mathrm{km}}{\lambda}\qquad(G=70\ \mathrm{GPa},\ \rho=3300).$$
> | $\lambda$ | $\tau_r$ ($\mu=10^{21}$ Pa s) | $\tau_r/\tau_M$ |
> |---|---|---|
> | 100 km | $1.2\times10^5$ yr | 272 |
> | 300 km | $4.1\times10^4$ yr | 91 |
> | 1000 km | $1.2\times10^4$ yr | 27 |
> | 3000 km | $4.1\times10^3$ yr | 9 |
> The ratio exceeds 1 for any $\lambda$ less than $27\,000$ km, so **at every geophysical wavelength the viscous treatment is self-consistent**: by the time the load has relaxed, the mantle has long forgotten its elasticity ($De=\tau_M/\tau_r\ll1$). (Only at wavelengths approaching the Earth's circumference would the elastic response matter.)
> **A counter-intuitive feature.** $\tau_r\propto1/\lambda$: *large* loads relax **faster**. Why: the driving stress is the excess weight $\rho gw$, the same for a broad or a narrow load of equal height. But the flow it drives reaches down to a depth of order $\lambda$ (the stream function above decays as $e^{-kz}$), so the velocity changes over a distance $\sim\lambda$. The velocity gradients, and therefore the viscous resistance, are of order $\mu\dot w/\lambda$. Balancing the same driving stress against a resistance $\propto\dot w/\lambda$ gives $\dot w\propto\lambda$: a broad load can sink faster because it shears the mantle more gently. This is why A&A call large loads better probes of *deep* viscosity: they reach the whole half-space. For **short** wavelengths, however, the plate's elastic strength takes over (the flexure filter of [[Fourier and Laplace Transforms]] §6.3: loads shorter than $\sim260$ km are carried by the plate and do not compensate at all), so $\tau_r$ is only meaningful in the compensated band $\lambda\gtrsim300$ km.

> [!question] Check yourself (answers below)
> 1. How much would a 3 km ice sheet depress the crust at isostatic equilibrium, and approximately how long would 63 % of the rebound take for $\lambda=2000$ km?
> 2. If the mantle viscosity were $10^{22}$ Pa s, how would the Fennoscandian rebound time change?
> 3. Why is the elastic response of the plate to a lake instantaneous while the mantle's is not?
> 4. Does a larger or smaller load relax faster on a viscous half-space? Does the same hold for a thin viscous layer?
> *Answers.* (1) Airy: $(\rho_i/\rho_m)h=\tfrac{917}{3300}\times3000=833$ m; $\tau_r=4\pi\times10^{21}/(3300\times9.81\times2\times10^6)=1.94\times10^{11}$ s $\approx6.1$ kyr. (2) $\tau_r\propto\mu$: ten times longer (60 kyr); that Fennoscandia rebounds in a few kyr is the evidence for $\mu\sim10^{21}$. (3) The elastic wave crosses the plate at the speed of sound; the mantle must move mass, and viscosity limits the speed. (4) Larger loads relax faster on a half-space ($\tau_r\propto1/\lambda$); for a thin layer (thickness $\ll\lambda$) the opposite is true, because flow must be squeezed laterally over longer distances.

> [!connection] Where else this appears
> - **Relaxation time and low-pass filtering:** [[LS01 Landscapes as Physical Systems]] (response time), [[Fourier and Laplace Transforms]] (transfer function $1/(1+\tau s)$; the pole at $-1/\tau$).
> - **Flexure** as a wavelength-dependent compensation: [[LS10 Folds Flexure and Mountain Building]]; the same $\mu$ controls post-glacial sea-level change in [[LS15 Glacial Deposits Rebound and Sea Level]] and the earthquake cycle's post-seismic flow in [[LS09 Faults and Earthquakes]].
> - **Climate:** the isostatic response to ice sheets is a feedback on sea level ([[Climate - Course Map]]).


## Oceans: thermal isostasy (slides 62–63)


> [!example] ❓ Question on the slides: Slide 58: over the oceans does isostasy also explain the topography?
> Yes, but the density variation is *thermal*: oceanic crust has nearly uniform thickness ($\sim$7 km), yet the seafloor deepens from $\sim2.6$ km at mid-ocean ridges to $\sim6$ km at $\sim100$ Myr, because the lithosphere cools, contracts and becomes denser (Pratt-type isostasy).


![[pre_062.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 62: age of the ocean floor and the ridge diagram
> Left: global map of ocean-floor age, from red at the ridges ($0$ Ma) through yellow, green to blue/purple ($>180$ Ma), symmetric about the spreading centres (Mid-Atlantic and Indian ridges, East Pacific Rise); the oldest floor is $\sim180$ Ma. Top right (T&S Fig. 4-44): a ridge in cross-section. Water depth $D$ increases away from the axis; below it the cold lithosphere (hatched, thickness $L$ increasing with age) overlies the asthenosphere (isotherms $1200^\circ$–$1600^\circ$C); columns at distances $x_1,x_2$ of ages $t_i=x_i/u$ have different $L$ and different $D$; the caption: isostasy requires the ocean to deepen with age to offset thermal contraction.


> [!derivation] 🟢 In the slides: Slide 62: $D(t)=D_0+\dfrac{\rho_L-\rho_m}{\rho_m-\rho_w}\sqrt{\kappa t}$
> Column of water depth $D$ and lithosphere of thickness $L$ (mean density $\rho_L>\rho_m$) must weigh the same as a ridge column of mantle of the same total depth $D+L$ (the slide's equation):
>
>
> $$
> \rho_m(D+L)=\rho_LL+\rho_wD \Longrightarrow D(\rho_m-\rho_w)=(\rho_L-\rho_m)L \Longrightarrow D=D_0+\frac{\rho_L-\rho_m}{\rho_m-\rho_w}L
> $$
>
>
> (with $D_0$ the ridge-crest depth). The lithosphere is the region cooled by conduction, obeying the heat equation $\partial_tT=\kappa\partial_z^2T$, identical to (4); by (5) its thickness grows as $L\sim\sqrt{\kappa t}$. Hence $D=D_0+\frac{\rho_L-\rho_m}{\rho_m-\rho_w}\sqrt{\kappa t}$. **Numbers** (slide): $\rho_L=3.39$, $\rho_m=3.3$, $\rho_w=1.0$ g cm$^{-3}$, $\kappa=10^{-6}$ m$^2$s$^{-1}$, $t=100$ Myr $=100\times10^6\times3.1\times10^7$ s:
>
>
> $$
> D=2600+\frac{3.39-3.3}{3.3-1}\sqrt{10^{-6}\cdot100\cdot10^6\cdot3.1\cdot10^7}=2600+0.039\times5.6\times10^4 \mathrm m\approx2600+2100 \mathrm m.
> $$
>
>
> So the depth is $\approx4.7$ km at 100 Myr (observed $\sim6$ km; the deficit is an $\mathcal{O}\!\left(1\right)$ factor from replacing the thermal thickness by $\sqrt{\kappa t}$; below).


> [!derivation] 🔵 Extra (not derived in the slides): Half-space cooling and the plate model: exact coefficients
> **Half-space cooling (HSCM).** Mantle at $T_m$ suddenly cooled to $0^\circ$C at the surface, $T(0,t)=0$: by (5) with $n\to T_m-T$: $T=T_m \mathrm{erf}\big(z/2\sqrt{\kappa t}\big)$. Density $\rho=\rho_m[1+\alpha_v(T_m-T)]$. Equal-weight condition against a ridge column (water plus lithosphere above a common depth):
>
>
> $$
> (\rho_m-\rho_w)(D-D_0)=\int_0^\infty\rho_m\alpha_v(T_m-T) \mathrm{d} z=\rho_m\alpha_vT_m\int_0^\infty\mathrm{erfc}\!\Big(\frac z{2\sqrt{\kappa t}}\Big)\mathrm{d} z=\rho_m\alpha_vT_m 2\sqrt{\frac{\kappa t}\pi},
> $$
>
>
> using $\int_0^\infty\mathrm{erfc} (s) \mathrm{d} s=1/\sqrt\pi$ (integrate by parts). So
>
>
> $$
> D(t)=D_0+\frac{2\rho_m\alpha_vT_m}{\rho_m-\rho_w}\sqrt{\frac{\kappa t}{\pi}}\approx2.6+0.35\sqrt{t/\mathrm{Myr}}  \mathrm{km}
> $$
>
>
> ($\alpha_v=3\times10^{-5}$ K$^{-1}$, $T_m=1300$ K): $6.1$ km at $100$ Myr, $\propto\sqrt t$ without limit.
>
> **Plate model.** Real seafloor flattens at old ages (slide 63): heat is supplied from below. Fix the temperature at the base of a plate of thickness $y_L$, $T(y_L)=T_m$. The solution of $\partial_tT=\kappa\partial_z^2T$ with $T=0$ at $z=0$ is $T=T_m\big[z/y_L+\tfrac2\pi\sum_{n\ge1}\tfrac1n\mathrm{e}^{-n^2\pi^2\kappa t/y_L^2}\sin(n\pi z/y_L)\big]$ (check: at $t=0$ the series is the Fourier expansion of $1-z/y_L$ so $T=T_m$; as $t\to\infty$, linear geotherm). Then $D(t)=D_0+\dfrac{\alpha_v\rho_mT_my_L}{\rho_m-\rho_w}\Big[\tfrac12-\tfrac4{\pi^2}\sum_{n\text{ odd}}\tfrac1{n^2}\mathrm{e}^{-n^2\pi^2\kappa t/y_L^2}\Big]$, tending to $D_\infty=D_0+\dfrac{\alpha_v\rho_mT_my_L}{2(\rho_m-\rho_w)}$: $5.3$ km for $y_L=95$ km and $6.1$ km for $y_L=125$ km.


![[ls_fig15.png]]
*Figure LS07.2. Slide 63 (T&S Fig. 4-45): seafloor depth against age. The half-space model keeps deepening as $\sqrt t$; plate models flatten to $D_\infty$. Observed depths (Atlantic, Pacific, Indian) follow the half-space curve to $\sim70$ Myr then flatten, favouring $y_L=95$–$125$ km. Parameters: $D_0=2.6$ km, $\alpha_v=3\times10^{-5}$, $T_m=1300$ K.*


![[pre_063.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 63
> The scatter is depth against age from deep-sea drilling sites (three symbols for the three oceans) corrected for sediment. The solid curve (HSCM) rises indefinitely; the dotted and dashed curves (PM 95 and PM 125) level off near $5.2$ and $6.0$ km. Data follow HSCM at young age and the plate curves at old age.


## Isostatic uplift from erosion (slide 64)


> [!derivation] 🔵 Extra (not derived in the slides): Erosion unloading and why peaks can rise while the mean elevation falls
> *Uniform erosion.* Remove a layer of thickness $e$ from a column in Airy equilibrium. By (18) the mean elevation is $h_\mathrm{mean}=(1-\rho_c/\rho_m)\times(\text{crustal thickness})$ plus const, so after the crustal thickness falls by $e$ the elevation falls by only $\Delta h=-(1-\rho_c/\rho_m)e=-0.15 e$, while the Moho rises by $\Delta H=+0.85 e$: $85 %$ of the removed thickness is replaced by isostatic uplift (slide 64: “$dT$” removed, “$\Delta h$”, “$\Delta H$”).
>
> *Non-uniform erosion (valley incision).* The isostatic response averages the load over the flexural wavelength (tens of km), so it responds to the *mean* removal. Suppose a fraction $f$ of the area is incised by depth $d$, peaks are untouched. Mean removal $=fd$, uniform isostatic uplift $=0.85 fd$. Peaks: $\Delta h_\mathrm{peak}=+0.85 fd$ (they rise!). Valley floors: $\Delta h_\mathrm{valley}=-d+0.85 fd$. Mean surface: $-fd+0.85fd=-0.15 fd$. For $f=0.5$, $d=1$ km: peaks $+425$ m, valley floors $-575$ m, mean $-75$ m: relief increases although the average elevation decreases (A&A Fig. 3.13: “greater erosion in valleys \dots may result in the uplift of peaks”; cf. Molnar & England 1990).


![[ls_fig16.png]]
*Figure LS07.3. Schematic of A&A Fig. 3.13(b) for $f=0.5$, $d=2$ units: incision removes valley rock, the whole column rebounds by $0.85 fd$, so summits rise.*


![[pre_064.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 64: Glacial isostatic adjustment map
> The globe at top right (NASA Blue Marble style) and the world map of vertical crustal motion in mm yr$^{-1}$ (colour scale about $-4$ to $+16$): high uplift rates (red–magenta) over Hudson Bay and the Baltic (former ice-sheet centres), and a ring of subsidence (blue) around them – the collapsing forebulge. This is isostatic uplift due to the removal of ice loads, treated in Chapter 15 with the viscous relaxation time $\tau_r$ derived above.

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Elastic plates: flexure under a load, and the plate as a low-pass filter
> A lithospheric plate of elastic thickness T_e and flexural rigidity D = E T_e³/12(1−ν²) floating on the mantle bends under a line load: w(x) = w₀ e^(−x/α)[cos(x/α) + sin(x/α)] with flexural parameter α = (4D/Δρg)^(1/4), a depression with a small forebulge.
>
> ![[ls_flexure.png|720]]
>
> **Try:** T_e = 25 km, Δρ = 3300: D ≈ 9.7×10²² N m and half-compensation at λ ≈ 262 km (D = 10²³ N m gives 263 km). Increase T_e (10, 30, 50, 70 km): the depression widens and shallows and the forebulge moves outward. Fill the basin with sediment (Δρ smaller) and α grows.
>
> [▶ Open the tool in your browser](../Assets/interactive/ls_flexure.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/ls_flexure.html) · all tools and coverage: [[Interactive Tools]]

> [!interactive]+ Interactive: Airy isostasy: why mountains have roots, and glacial rebound
> Columns of crust float on the denser mantle like blocks of wood in water.
>
> ![[ls_isostasy.png|720]]
>
> **Try:** With ρ_c = 2800, ρ_m = 3300 the root is 5.6 × the height: a 5 km plateau has a 28 km root and a 68 km crust. Raise ρ_c toward ρ_m and the roots get enormous; lower it and they shrink. In the rebound panel, make the mantle less viscous and watch τ shrink.
>
> [▶ Open the tool in your browser](../Assets/interactive/ls_isostasy.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/ls_isostasy.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How LS07 connects
> **Previous:** [[LS06 Maximum Topography]] · **Next:** [[LS08 Plate Tectonics Strain Stress and Convection]].
> **Other subjects:** [[Climate - Course Map]] (weathering and the carbon cycle, glaciation, orographic rainfall), [[Thermodynamics and Statistical Mechanics - Course Map]] (heat conduction and diffusion), [[Evolution of Earth and Life - Course Map]] (plate tectonics and landscapes through geological time), [[Waves - Course Map]] (diffusion and wave equations).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | slide content, figures read panel by panel | [[pre_ms_landscape_26.pdf]] slides 58–64 (images embedded from the PDF, auto-cropped, `scripts/render_slides.py`) | taught |
> | derivations, worked examples, tool boxes, TikZ figures | the AI-written derivation-level notes [[Landscapes_and_Their_Evolution_notes.pdf]] (EC2123 notes; LaTeX source in `landscape-notes-tex-source.tar.gz`), converted with `scripts/tex2vault_ls.py`; cross-checked against Anderson and Anderson and Turcotte and Schubert as cited there | secondary + extra/book |
>
> **Notes.** (1) The text of this chapter is the AI-written reference notes' text, converted to the vault's callout style and equation numbering (chapter-local, so some cross-references read as "(label)"). (2) The slide images were checked against the notes' slide numbers for a sample of slides (e.g. 1–12, 109–120 match). Figure descriptions are the notes', and should be compared with the images beside them. (3) The `[!verify]` items of the notes' last front-matter section ("Two places where the slides need care") are in [[Landscapes Notation and Glossary]].

<!-- ls-depth:LS07:3 -->
> [!provenance]- Depth-layer sources (added 2026-10-28)
> | Topic | Source | Priority |
> |---|---|---|
> | Lake Bonneville, Gilbert 1890, mantle response times, deflection $>50$ m, 14.5 ka | A&A PDF pp.61–62 (read) | b · primary book |
> | Haskell 1935 and Fennoscandian terraces | T&S (Bookos copy) PDF p.21 (found by search; the sentence read) | b · primary book |
> | $\tau_r=4\pi\mu/\rho g\lambda$ | already derived in this chapter (agrees with A&A's statement of several kyr) | a · AI notes |
> | $\tau_r/\tau_M=4\pi G/\rho g\lambda$, table, Airy ice example, Bonneville lake depth (300 m) | my computation, `scripts/ls_depth_numbers.py` (`LS07`); lake depth recalled, `[verify]` | extra · beyond |
