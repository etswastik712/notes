---
title: LS99 Landscapes Practice Problems
aliases: [LS99, Landscapes Practice Problems]
subject: landscapes
type: chapter
chapter: 99
part: X
scope: [taught, extra-book, extra-beyond]
by: [slides, ai-notes, book]
status: draft
tags: [subject/landscapes, type/chapter, taught, extra/book, extra/beyond, src/slides, src/ai-notes, src/book, status/draft]
---
# LS99 · Landscapes Practice Problems

◀ [[LS17 Aeolian Landscapes]] · [[Landscapes and Geomorphology - Course Map|Course Map]] · next: (end)

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught**: slides all of [[pre_ms_landscape_26.pdf|the EC2123 pre-midsem deck]] (Argha Banerjee, IISER Pune; 153 slides). Boxes marked 🟢 **In the slides** derive what the slides derive; boxes marked 🖼 **Reading the diagram** explain each slide figure panel by panel and sit directly under the slide image.
> 🔵 **Extra · beyond**: boxes marked 🔵 **Extra** complete derivations the slides only quote (from Anderson and Anderson, *Geomorphology: the Mechanics and Chemistry of Landscapes*, and Turcotte and Schubert, *Geodynamics*); 🛠 **Tool** boxes derive a mathematical tool from 12th-grade material; 🧮 **Worked example** boxes calibrate orders of magnitude.
> This chapter has 0 sections, 0 derivation boxes, 0 redrawn figures and 0 slide images.

> [!key] After this chapter you can
> - solve the problems in order of the chapters,
> - check each answer against the stated assumptions.

> [!intuition] The one-sentence story
> Problems that turn each chapter's results into numbers: orders of magnitude for flexure, isostasy, diffusion, glaciers and rivers.

```mermaid
flowchart LR
  A["foundations"] --> B["planet, isostasy"]
  B --> C["tectonics"]
  C --> D["surface processes"]
  D --> E["glaciers, rivers"]
```
*Concept map: every box is a section of this chapter.*

Problems are grouped by chapter; each states what is given and asks for a specific quantity, with a full worked solution (not merely an answer) since the exam is open-notes. Numerical values not given on the slides are stated as assumptions.


\addcontentsline{toc}{chapter}{Problem set (worked)}


> [!example] 🧮 Worked example: P2.1 — Stability from a Taylor expansion
> A particle sits in a potential $V(x)=\tfrac14kx^4-\tfrac12k L^2x^2$ ($k,L>0$). Find all equilibria and classify their stability.\\[4pt]
> **Solution.** $F=-V'=-kx^3+kL^2x=kx(L^2-x^2)$. Zero at $x=0,\pm L$. $F'(x)=k(L^2-3x^2)$: at $x=0$, $F'=kL^2>0$ (unstable, as in §2.2); at $x=\pm L$, $F'=k(L^2-3L^2)=-2kL^2<0$ (stable). Physically: a symmetric double-well; the centre is a local energy maximum, the two flanks are minima.


> [!example] 🧮 Worked example: P2.2 — Diffusive penetration depth
> A slab of rock at $10^\circ$C has its surface suddenly raised to $30^\circ$C by a lava flow. Using $\kappa=8\times10^{-7} \mathrm{m^2s^{-1}}$, estimate how deep the temperature has risen by more than $1^\circ$C after (a) 1 day, (b) 1 year.\\[4pt]
> **Solution.** By (5), $T-T_0=20 \mathrm{erfc}(x/2\sqrt{\kappa t})$; “risen by $>1^\circ$C” means $\mathrm{erfc}(\eta)>0.05$, i.e. $\eta<1.39$ (from tables/inverse erfc), so $x<2.78\sqrt{\kappa t}$.
> (a) $t=86400$ s: $\sqrt{\kappa t}=\sqrt{8\times10^{-7}\times86400}=0.263$ m, $x<0.73$ m.
> (b) $t=3.15\times10^7$ s: $\sqrt{\kappa t}=5.02$ m, $x<14$ m. (Consistent with $\propto\sqrt t$: a factor $365$ in time gives $\sqrt{365}=19.1$ in depth, and $0.73\times19.1=14$ m checks.)


> [!example] 🧮 Worked example: P3.1 — Buoyant force by direct pressure integration
> A cube of side $a$ is fully submerged in a fluid of density $\rho_f$ with its top face at depth $d$. Compute the net vertical force from pressure directly (not by quoting Archimedes) and check it equals the weight of displaced fluid.\\[4pt]
> **Solution.** $P(z)=\rho_fg z$ (depth $z$). Top face at depth $d$: downward force $P(d)a^2=\rho_fgd a^2$. Bottom face at depth $d+a$: upward force $\rho_fg(d+a)a^2$. Side faces: horizontal forces cancel by symmetry (and contribute nothing vertically). Net upward: $\rho_fg(d+a)a^2-\rho_fgd a^2=\rho_fg a^3$, exactly $\rho_fg\times(\text{volume})$: the weight of displaced fluid, matching the general proof of §2.4.


> [!example] 🧮 Worked example: P4.1 — Oblateness of a hypothetical planet
> A planet has $R=5000$ km, $\bar\rho=4500  \mathrm{kg m^{-3}}$, rotation period $18$ h, surface density $\rho_s=2700  \mathrm{kg m^{-3}}$. Estimate its flattening and the equator–pole radius difference.\\[4pt]
> **Solution.** $\omega=2\pi/(18\times3600)=9.70\times10^{-5} \mathrm{s^{-1}}$. $g=\tfrac43\pi G\bar\rho R=\tfrac43\pi\times6.674\times10^{-11}\times4500\times5\times10^6=6.29 \mathrm{m s^{-2}}$. By (15): $\Delta R/R=\bar\rho\omega^2R/(2g\rho_s)=4500\times(9.70\times10^{-5})^2\times5\times10^6/(2\times6.29\times2700)=0.0117$. $\Delta R=58.5$ km.


> [!example] 🧮 Worked example: P4.2 — Maximum topography of a hypothetical icy moon
> An icy moon has $R=800$ km, $\bar\rho=1600  \mathrm{kg m^{-3}}$, crust density $\rho_c=950  \mathrm{kg m^{-3}}$ (ice), and rock/ice strength $\tau_y=5 \mathrm{MPa}$ (ice is weaker than rock). Estimate its maximum relief, and compare $R$ with the friction-limited transition radius $R_*$ (§6.3) using $f=0.5$.\\[4pt]
> **Solution.** By (17): $\Delta h_\mathrm{max}=3\tau_y/(2\pi G\rho_c\bar\rho R)=3\times5\times10^6/(2\pi\times6.674\times10^{-11}\times950\times1600\times8\times10^5)=1.5\times10^7/(5.09\times10^2)\cdot 10^{-?}$. Compute denominator: $2\pi\times6.674\times10^{-11}=4.193\times10^{-10}$; $\times950=3.98\times10^{-7}$; $\times1600=6.37\times10^{-4}$; $\times8\times10^5=509.5$. So $\Delta h_\mathrm{max}=1.5\times10^7/509.5=2.94\times10^4$ m $\approx29$ km. $R_*=\sqrt{3\tau_y/(2\pi G\rho_c\bar\rho f)}=\sqrt{1.5\times10^7/(6.37\times10^{-4}\times0.5)}=\sqrt{4.71\times10^{10}}=2.17\times10^5$ m $=217$ km. Since $R=800 \mathrm{km}\gg R_*=217$ km, this moon is comfortably in the strength-limited (not friction-limited) regime, and 29 km is a genuine upper bound, though a $800$-km icy body this relief-capable would be unusual (Melosh's real data, slide 55, show icy bodies with much lower relief/radius, implying weaker effective $\tau_y$ from fracturing).


> [!example] 🧮 Worked example: P5.1 — Airy root for the Andes
> The Andes reach $\bar h=4$ km mean elevation over the plateau. Using $\rho_c=2800$, $\rho_m=3300$, estimate the crustal root and total crustal thickness (reference thickness $c=35$ km).\\[4pt]
> **Solution.** By §7.2, $b_1=\dfrac{\rho_c}{\rho_m-\rho_c}h_1=\dfrac{2800}{500}\times4=22.4$ km. Total thickness $=c+h_1+b_1=35+4+22.4=61.4$ km, close to seismically observed values ($\sim60$–$70$ km) beneath the Altiplano.


> [!example] 🧮 Worked example: P5.2 — Ocean depth at a given age
> Using the half-space cooling result of §7.4, find the age of ocean floor at $5.0$ km depth (take $D_0=2.6$ km, coefficient $0.35 \mathrm{km/\sqrt{Myr}}$ as in the text).\\[4pt]
> **Solution.** $5.0=2.6+0.35\sqrt t\Rightarrow\sqrt t=6.857\Rightarrow t=47$ Myr.


> [!example] 🧮 Worked example: P6.1 — Time for isostatic (viscous) relaxation
> A river valley of half-width $50$ km is rapidly (geologically instantaneously) excavated. Using mantle viscosity $\mu=10^{21}$ Pa s and crustal density $\rho=2800  \mathrm{kg m^{-3}}$, estimate the time for isostatic response, taking the relevant wavelength as $\lambda=4\times(\text{half-width})$.\\[4pt]
> **Solution.** $\lambda=200$ km $=2\times10^5$ m. By (29): $\tau_r=4\pi\mu/(\rho g\lambda)=4\pi\times10^{21}/(2800\times9.8\times2\times10^5)=1.257\times10^{22}/(5.49\times10^9)=2.29\times10^{12}$ s $\approx72 600$ yr: tens of thousands of years, much shorter than typical fluvial incision time scales (§16.4), so the region can be treated as isostatically compensated throughout its erosional history.


> [!example] 🧮 Worked example: P7.1 — Rayleigh number and convective vigour
> A magma chamber of thickness $b=2$ km has $\Delta T=200$ K, $\rho_0=2700  \mathrm{kg m^{-3}}$, $\alpha_v=5\times10^{-5} \mathrm{K^{-1}}$, $\mu=10^{6}$ Pa s, $\kappa=10^{-6} \mathrm{m^2s^{-1}}$. Is it convecting?\\[4pt]
> **Solution.** By (19): $\mathrm{Ra}=\dfrac{2700\times9.8\times5\times10^{-5}\times200\times(2000)^3}{10^6\times10^{-6}}=\dfrac{2700\times9.8\times5\times10^{-5}\times200\times8\times10^9}{1}$. Compute stepwise: $2700\times9.8=26 460$; $\times5\times10^{-5}=1.323$; $\times200=264.6$; $\times8\times10^9=2.12\times10^{12}$. So $\mathrm{Ra}\approx2\times10^{12}\gg\mathrm{Ra}_c\approx658$: vigorously convecting (as expected for a magma chamber of this size).


> [!example] 🧮 Worked example: P8.1 — Fault slip and moment magnitude
> A strike-slip fault ruptures over $80$ km length and $12$ km depth with average slip $1.8$ m. Using $\mu_r=3\times10^{10}$ Pa, find $M_0$ and $M_w$.\\[4pt]
> **Solution.** $A=80 000\times12 000=9.6\times10^8$ m$^2$. $M_0=\mu_rA\Delta=3\times10^{10}\times9.6\times10^8\times1.8=5.18\times10^{19}$ N m. $M_w=\tfrac23(\log_{10}(5.18\times10^{19})-9.1)=\tfrac23(19.71-9.1)=\tfrac23\times10.61=7.08$.


> [!example] 🧮 Worked example: P8.2 — Recurrence interval from slip rate
> A fault slips at the long-term rate $25 \mathrm{mm yr^{-1}}$ and produces earthquakes each releasing $3.5$ m of slip. What is the mean recurrence interval, and (using P8.1's method) the moment magnitude if the rupture is $150\times15$ km?\\[4pt]
> **Solution.** $T=\Delta/u_0=3.5/0.025=140$ yr. $A=150 000\times15 000=2.25\times10^9$ m$^2$; $M_0=3\times10^{10}\times2.25\times10^9\times3.5=2.36\times10^{20}$ N m; $M_w=\tfrac23(\log_{10}2.36\times10^{20}-9.1)=\tfrac23(20.37-9.1)=\tfrac23\times11.27=7.51$.


> [!example] 🧮 Worked example: P9.1 — Dominant fold wavelength
> A $2$-m-thick sandstone bed ($\mu_l=10^{19}$ Pa s) is embedded in shale ($\mu_m=10^{17}$ Pa s) and shortened. Predict the dominant fold wavelength.\\[4pt]
> **Solution.** By (22): $\lambda_d=2\pi h(\mu_l/6\mu_m)^{1/3}=2\pi\times2\times(100/6)^{1/3}=12.57\times(16.67)^{1/3}=12.57\times2.55=32$ m.


> [!example] 🧮 Worked example: P9.2 — Critical taper
> Estimate the surface slope of a fold-and-thrust wedge with internal friction angle $\phi=25^\circ$, basal friction $f_b=0.3$, and a flat base ($\beta=0$).\\[4pt]
> **Solution.** $K=(1+\sin\phi)/(1-\sin\phi)=(1+0.423)/(1-0.423)=1.423/0.577=2.47$. $\alpha=(f_b+\beta)/K=0.3/2.47=0.121$ rad $=7.0^\circ$.


> [!example] 🧮 Worked example: P10.1 — Regolith steady-state thickness
> A hillside has erosion rate $E=15 \mathrm{m Myr^{-1}}$, exponential regolith production with $P_0=80 \mathrm{m Myr^{-1}}$, $h_0=0.45$ m. Find the steady regolith thickness and its e-folding recovery time after a landslide strips it to zero.\\[4pt]
> **Solution.** $H_s=h_0\ln(P_0/E)=0.45\ln(80/15)=0.45\times1.674=0.753$ m. Recovery: near $H=0$, $\dot H=P_0-E$ (production near its bare-rock maximum) until $H$ approaches $H_s$, then relaxes with $\tau_H=h_0/E=0.45/(1.5\times10^{-5})=30 000$ yr (from §11.2); a rough total recovery time is a few $\tau_H$, i.e. $\sim10^5$ yr.


> [!example] 🧮 Worked example: P11.1 — Steady hillslope profile
> A soil-mantled ridge erodes at $\mathcal E=5\times10^{-5} \mathrm{m yr^{-1}}$ with diffusivity $\kappa_h=6\times10^{-3} \mathrm{m^2yr^{-1}}$ and half-width $L=80$ m. Find the ridge-crest height above the base and the basal slope angle.\\[4pt]
> **Solution.** By (25): height $=\mathcal EL^2/(2\kappa_h)=5\times10^{-5}\times6400/(2\times6\times10^{-3})=0.32/0.012=26.7$ m. Basal slope $S=\mathcal EL/\kappa_h=5\times10^{-5}\times80/6\times10^{-3}=0.667$, angle $=\arctan0.667=33.7^\circ$.


> [!example] 🧮 Worked example: P11.2 — Scarp age from its maximum slope
> A fault scarp of height $6$ m has a measured maximum slope of $18^\circ$ ($\tan18^\circ=0.325$). With $\kappa_h=5\times10^{-3} \mathrm{m^2yr^{-1}}$, estimate its age.\\[4pt]
> **Solution.** By the erf result of §12.4: $\kappa_ht=h^2/(4\pi S_\mathrm{max}^2)=36/(4\pi\times0.1056)=36/1.327=27.1$ m$^2$. $t=27.1/0.005=5430$ yr.


> [!example] 🧮 Worked example: P12.1 — Infinite-slope factor of safety
> A colluvial layer, $h=2.5$ m thick, $\rho=1900  \mathrm{kg m^{-3}}$, $\phi=32^\circ$, $C=5$ kPa, rests on a slope $\theta=28^\circ$. Compute FS dry, and again if the layer is saturated with seepage parallel to the slope ($\rho_w=1000$).\\[4pt]
> **Solution.** $\rho gh=1900\times9.8\times2.5=46 550$ Pa. $\sigma=\rho gh\cos^2\theta=46550\times\cos^228^\circ=46550\times0.7796=36 290$ Pa. $\tau=\rho gh\sin\theta\cos\theta=46550\times0.4695\times0.8829=19 300$ Pa. Dry: $\mathrm{FS}=(C+\sigma\tan\phi)/\tau=(5000+36290\times0.625)/19300=(5000+22 680)/19300=27 680/19300=1.43$ (stable). Saturated: $P_w=\rho_wgh\cos^2\theta=1000\times9.8\times2.5\times0.7796=19 100$ Pa. $\mathrm{FS}=(5000+(36290-19100)\times0.625)/19300=(5000+10 740)/19300=15 740/19300=0.82<1$: fails when saturated.


> [!example] 🧮 Worked example: P12.2 — Newmark critical acceleration
> For the dry slope of P12.1 ($\theta=28^\circ$, $\phi=32^\circ$), find the critical horizontal ground acceleration (as a fraction of $g$) for co-seismic failure, ignoring cohesion.\\[4pt]
> **Solution.** $a_c=g\cos\theta(\tan\phi-\tan\theta)=9.8\times0.8829\times(0.625-0.5317)=9.8\times0.8829\times0.0933=0.808 \mathrm{m s^{-2}}=0.082g$: even weak shaking (PGA $>0.08g$) could trigger failure, consistent with this slope being close to its dry angle of repose $\phi$.


> [!example] 🧮 Worked example: P13.1 — Glacier surface speed and basal shear stress
> A glacier is $150$ m thick on a $4^\circ$ slope, ice density $917  \mathrm{kg m^{-3}}$, $A=2.1\times10^{-24} \mathrm{Pa^{-3}s^{-1}}$, $n=3$; assume no sliding. Find the basal shear stress and the surface (deformation) speed.\\[4pt]
> **Solution.** $\tau_b=\rho_igH\sin\theta=917\times9.8\times150\times\sin4^\circ=917\times9.8\times150\times0.0698=94 050\times0.0698\approx... $ compute: $917\times9.8=8987$; $\times150=1.348\times10^6$; $\times0.0698=9.41\times10^4$ Pa $=94.1$ kPa. $U_s=\tfrac14A\tau_b^3H=\tfrac14\times2.1\times10^{-24}\times(9.41\times10^4)^3\times150$. $(9.41\times10^4)^3=8.33\times10^{14}$. So $U_s=0.25\times2.1\times10^{-24}\times8.33\times10^{14}\times150=0.25\times2.1\times8.33\times150\times10^{-10}=655.5\times10^{-10}=6.6\times10^{-8} \mathrm{m s^{-1}}=2.1 \mathrm{m yr^{-1}}$.


> [!example] 🧮 Worked example: P13.2 — Mass balance and glacier length
> A glacier of uniform width $500$ m has balance gradient $\gamma=2.5 \mathrm{m yr^{-1}km^{-1}}$ and ELA at $x_E=4$ km from the head. Find $Q_\mathrm{max}$ and the terminus position (as in §14.2's worked example).\\[4pt]
> **Solution.** By the linear-balance model, terminus at $x=2x_E=8$ km. $Q_\mathrm{max}=W\gamma x_E^2/2=500\times2.5\times10^{-3}\times(4000)^2/2=500\times2.5\times10^{-3}\times8\times10^6=10^7 \mathrm{m^3 yr^{-1}}$.


> [!example] 🧮 Worked example: P14.1 (fluvial) — Slope–area scaling
> A river has $K=2\times10^{-6} \mathrm{m^{1-2m}yr^{-1}}$ with $m=0.5$, $n=1$, under uplift $U=3\times10^{-4} \mathrm{m yr^{-1}}$. Find the required channel slope at a point where drainage area $A=25 \mathrm{km^2}$.\\[4pt]
> **Solution.** By (31): $S=(U/K)A^{-m}=(3\times10^{-4}/2\times10^{-6})\times(25\times10^6)^{-0.5}=150\times(5000)^{-1}=150/5000=0.03$: a $3 %$ ($1.7^\circ$) gradient.


> [!example] 🧮 Worked example: P14.2 (aeolian) — Dune migration speed
> A barchan dune $H=3$ m high experiences a sand flux $Q_s=12 \mathrm{m^2yr^{-1}}$. How far does it migrate in a decade, and how does this compare with a neighbouring $H=15$ m dune under the same wind?\\[4pt]
> **Solution.** $u_d=Q_s/H=12/3=4 \mathrm{m yr^{-1}}$; in $10$ yr, $40$ m. The larger dune: $u_d=12/15=0.8 \mathrm{m yr^{-1}}$, $8$ m in a decade – five times slower, illustrating $u_d\propto1/H$ (§17.3).

## Map of this chapter
> [!connection] How LS99 connects
> **Previous:** [[LS17 Aeolian Landscapes]] · **Next:** (end).
> **Other subjects:** [[Climate - Course Map]] (weathering and the carbon cycle, glaciation, orographic rainfall), [[Thermodynamics - Course Map]] (heat conduction and diffusion), [[Evolution of Earth and Life - Course Map]] (plate tectonics and landscapes through geological time), [[Waves - Course Map]] (diffusion and wave equations).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | slide content, figures read panel by panel | [[pre_ms_landscape_26.pdf]] slides all (images embedded from the PDF, auto-cropped, `scripts/render_slides.py`) | taught |
> | derivations, worked examples, tool boxes, TikZ figures | the AI-written derivation-level notes [[Landscapes_and_Their_Evolution_notes.pdf]] (EC2123 notes; LaTeX source in `landscape-notes-tex-source.tar.gz`), converted with `scripts/tex2vault_ls.py`; cross-checked against Anderson and Anderson and Turcotte and Schubert as cited there | secondary + extra/book |
>
> **Notes.** (1) The text of this chapter is the AI-written reference notes' text, converted to the vault's callout style and equation numbering (chapter-local, so some cross-references read as "(label)"). (2) The slide images were checked against the notes' slide numbers for a sample of slides (e.g. 1–12, 109–120 match). Figure descriptions are the notes', and should be compared with the images beside them. (3) The `[!verify]` items of the notes' last front-matter section ("Two places where the slides need care") are in [[Landscapes Notation and Glossary]].
