---
title: LS14 Glaciers Mass Balance and Ice Flow
aliases: [LS14, Glaciers Mass Balance and Ice Flow]
subject: landscapes
type: chapter
chapter: 14
part: VIII
scope: [taught, extra-book, extra-beyond]
by: [slides, ai-notes, book]
status: draft
tags: [subject/landscapes, type/chapter, taught, extra/book, extra/beyond, src/slides, src/ai-notes, src/book, status/draft]
---
# LS14 · Glaciers Mass Balance and Ice Flow

◀ [[LS13 Landslides]] · [[Landscapes and Geomorphology - Course Map|Course Map]] · next: [[LS15 Glacial Deposits Rebound and Sea Level]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught**: slides 138–144 of [[pre_ms_landscape_26.pdf|the EC2123 pre-midsem deck]] (Argha Banerjee, IISER Pune; 153 slides). Boxes marked 🟢 **In the slides** derive what the slides derive; boxes marked 🖼 **Reading the diagram** explain each slide figure panel by panel and sit directly under the slide image.
> 🔵 **Extra · beyond**: boxes marked 🔵 **Extra** complete derivations the slides only quote (from Anderson and Anderson, *Geomorphology: the Mechanics and Chemistry of Landscapes*, and Turcotte and Schubert, *Geodynamics*); 🛠 **Tool** boxes derive a mathematical tool from 12th-grade material; 🧮 **Worked example** boxes calibrate orders of magnitude.
> This chapter has 3 sections, 3 derivation boxes, 3 redrawn figures and 6 slide images.

> [!key] After this chapter you can
> - write the glacier mass balance and ice flux equation,
> - derive deformation velocity from Glen's flow law,
> - describe sliding and the role of water,
> - read the slide figures on glacier geometry.

> [!intuition] The one-sentence story
> A glacier is a river of ice whose size is set by accumulation against ablation and whose speed comes from viscous deformation (Glen's law) plus sliding.

```mermaid
flowchart LR
  A["open, non-equilibrium system"] --> B["mass balance b(z)"]
  B --> C["ice flux Q"]
  C --> D["Glen flow law (n = 3)"]
  D --> E["sliding, water"]
```
*Concept map: every box is a section of this chapter.*

*[Slides 138–144]*


## A glacier as an open, non-equilibrium system (slides 138–141)


> [!key] Definition: Glacier terms
> A *glacier* is a perennial body of ice that flows under its own weight. *Accumulation*: mass gain (snowfall, avalanching, refreezing). *Ablation*: mass loss (melt, sublimation, calving into water). The *specific mass balance* $b(x,t)$ is the net mass gain per unit area per year, expressed as thickness of ice or water equivalent (positive in the *accumulation zone*, negative in the *ablation zone*). The *equilibrium line* (ELA, equilibrium-line altitude) is the contour where $b=0$ averaged over a year.


Slide 141: a glacier is a *non-equilibrium open system* with accumulation, flow and ablation. Its **steady state** (slide 141): *total accumulation $=$ total ablation $=$ the flux across the ELA*. The size of a glacier tracks the ELA, which varies with precipitation $P$, temperature $T$, radiation.


![[pre_138.jpg|300]] ![[pre_139.jpg|300]] ![[pre_140.jpg|300]]


> [!example] 🖼 Reading the diagram: Slides 138–140: what the images show
> Slide 138: false-colour satellite image of the Baltoro glacier (Karakoram, F. Paul): a long trunk glacier fed by many tributaries; parallel dark stripes are *medial moraines* where the debris of two tributaries meets; snow is cyan, exposed ice grey-blue, debris-covered ice brown; the tongue is lower and debris-covered. Slides 139–140: frames from time-lapse videos of glacier flow, retreat and surging (a valley glacier with crevasses in Alaska; a large outlet glacier from space with blue melt-water lakes and a 4-mile scale), examples of the different responses of a glacier to changing forcing.


![[pre_141.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 141: global distribution, ELA and LGM
> (A) glacier section: a *zone of accumulation* above and a *zone of ablation* below the red equilibrium line. (B) ELA (km) against latitude: the ELA is lowest near the poles and rises to $\sim5$ km in the dry subtropics, with a lower curve (Last Glacial Maximum) offset downward by $\sim1$ km relative to the present (green shading between). (C) polar view of the same: the ELA at glacial maximum and minimum drawn on the globe. Centre and right: the present global glacier distribution (blue dots) and a map of the LGM ice ($\sim21$ ka): the Laurentide and Cordilleran (North America), Greenland, Scandinavian (Fennoscandian), Patagonian and Antarctic ice sheets, with lowered sea level exposing land bridges (Bering, Sunda, Persian Gulf, Sahul). Right: Cuffey and Paterson Fig. 1.6: an Icelandic glacier (Vatnajökull) with the accumulation and ablation zones separated by the equilibrium line (dashed), flow lines (blue arrows, length $\propto$ speed), the cross-section and calving at the terminus.


> [!example] 🧮 Worked example: Sea-level equivalent of the ice-age ice
> Ocean area $A_o=3.6\times10^{14}$ m$^2$. The LGM sea level was $\sim120$ m lower, so water volume $V_w=120\times3.6\times10^{14}=4.3\times10^{16}$ m$^3$ was stored on land as ice of volume $V_i=V_w\rho_w/\rho_i=4.7\times10^{16}$ m$^3$ ($\approx47$ million km$^3$). Conversely, 
>
> $$
> \Delta h_\mathrm{sea}=\rho_iV_i/(\rho_wA_o).
> $$


## Mass balance and ice flux (slide 142)


![[ls_fig29.png]]
*Figure LS14.1. Longitudinal section of a glacier (slide 142, A&A Fig. 8.2, and slide 145): flow lines dive into the ice in the accumulation zone and rise to the surface in the ablation zone.*


> [!derivation] 🟢 In the slides: Slide 142: ice discharge $Q(x)=\int_0^xW(x') b(x') \mathrm{d} x'$
> Let the glacier have width $W(x)$ and thickness $H(x,t)$, so the cross-sectional area is $S=WH$; let $Q=S\bar u$ be the volume of ice crossing a section per unit time ($\bar u$: depth-averaged speed). Conservation of ice volume in the slice $[x,x+\mathrm{d} x]$ (exactly (3) with $n=S$, source $s=Wb$):
>
>
> $$
> \partial_tS=W\,b-\partial_xQ . \tag{27}
> $$
>
>
> Steady state, $\partial_tS=0$: $\partial_xQ=Wb$, and with $Q(0)=0$ at the head,
>
>
> $$
> Q(x)=\int_0^xW(x')b(x')\,\mathrm{d} x' . \tag{28}
> $$
>
>
> $Q$ increases as long as $b>0$, is maximum $Q_\mathrm{max}$ where $b=0$ (the ELA; slide 142: “$Q_\mathrm{max}$”), and decreases again in the ablation zone; the terminus is where $Q=0$, so $\int_0^LWb \mathrm{d} x=0$: total accumulation equals total ablation (slide 141), and $Q_\mathrm{max}$ equals the total accumulation above the ELA = flux across the ELA.


> [!example] 🧮 Worked example: A worked glacier
> Uniform width $W=1$ km and $b(x)=\gamma(x_E-x)$ with $x_E=3$ km and balance gradient $\gamma=2 \mathrm{m yr^{-1} km^{-1}}$ ($=2\times10^{-3}$ yr$^{-1}$). Then $Q(x)=W\gamma (x_Ex-x^2/2)$, zero again at $x=2x_E=6$ km (terminus). $Q_\mathrm{max}=W\gamma x_E^2/2=10^3\times2\times10^{-3}\times(3\times10^3)^2/2=9\times10^6 \mathrm{m^3 yr^{-1}}$. With thickness $H=100$ m: $\bar u=Q/(WH)=90$ m yr$^{-1}$ at the ELA: the flux and the flow speed are linked (see §14.3).


![[ls_fig30.png]]
*Figure LS14.2. The worked example: mass-balance profile (left) and the resulting discharge (right), slide 142's lower panels.*


![[pre_142.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 142: left figure (mass fluxes) and A&A Fig. 8.2
> Left: a glacier plan/section with the pathways of mass: avalanches, snowfall and sublimation on the surface (each with a small seasonal curve of the mass balance against time) and melt at the terminus. Right: (i) elevation profile with the *local mass balance* $b(z)$ curve (blue, from negative at low $z$ to positive above the ELA, increasing with elevation because of both temperature and precipitation), (ii) the surface profile with accumulation and ablation areas separated by the snowline (ELA), (iii) $b(x)$ against distance and (iv) $Q(x)=\int Wb \mathrm{d} x$ increasing to $Q_\mathrm{max}$ at the ELA and falling to zero at the terminus.


## Ice flow: viscous deformation and sliding (slides 143–144)


Slide 144: ice flows by *viscous deformation plus sliding at the bed*. It differs from a Newtonian liquid because the strain rate is a **power law** of stress, with $n\approx3$ (Glen's law).


![[pre_143.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 143: the control element (A&A Fig. 8.7)
> A block of ice of width $w$, thickness $H$, length $\mathrm{d} x$, with a surface layer $b$ (mass balance), volume flux $Q_x$ entering and $Q_{x+\mathrm{d} x}$ leaving. On the right, the velocity profile $u(z)$ has two parts: the deformation velocity (increasing from zero at the bed to $U_\mathrm{def}$ at the surface) and the sliding velocity $U_s$ at the bed (uniform over depth); $u=U_s+U_\mathrm{def}(z)$.


> [!derivation] 🟢 In the slides: Slide 144 (upper): Newtonian flow of ice on an inclined plane
> With $\dot\epsilon_{xz}=\tfrac12 \mathrm{d} U/\mathrm{d} z$ replaced by the slide's convention $\dot\epsilon_{xz}\equiv\mathrm{d} U/\mathrm{d} z=\tau_{xz}/\mu$ (Eq. 8.8), the slab solution (11) of Chapter 2 (with $y\to z$, $\rho\to\rho_i$) gives
>
>
> $$
> U(z)=\frac{\rho_ig\sin\theta}{\mu}\Big(Hz-\frac{z^2}2\Big),\qquad\tau_{xz}=\rho_ig\sin\theta (H-z).
> $$
>
>
> This is exactly the slide's $U(z)=\dfrac{\rho_ig\sin(\theta)}{\mu}\big(Hz-\dfrac{z^2}2\big)$. Surface speed $U_s=\rho_ig\sin\theta H^2/2\mu$, discharge per width $q=\rho_ig\sin\theta H^3/3\mu$.


> [!derivation] 🔵 Extra (not derived in the slides): Glen's flow law: $\mathrm{d} U/\mathrm{d} z=A\tau^n$ (slide 144, lower)
> Ice deforms as $\dot\epsilon=A\tau^n$ ($A$ depends on temperature: $\sim2.4\times10^{-24} \mathrm{Pa^{-3}s^{-1}}$ for temperate ice, $n=3$; quoted from laboratory and field data). The stress balance is unchanged (it does not depend on the rheology): $\tau_{xz}(z)=\rho_ig\sin\theta (H-z)=\tau_b(1-z/H)$ with basal shear stress $\tau_b=\rho_igH\sin\theta$. Then
>
>
> $$
> \dv Uz=A\tau_b^n\Big(1-\frac zH\Big)^n \Longrightarrow U(z)=U_s^{\rm(def)}\Big[1-\Big(1-\frac zH\Big)^{n+1}\Big],\qquad U_s^{\rm(def)}=\frac{A\tau_b^nH}{n+1}.
> $$
>
>
> For $n=3$ expanding $\big[1-(1-\zeta)^4\big]$ with $\zeta=z/H$ gives the polynomial on the slide,
>
>
> $$
> U(z)=A(\rho_ig\sin\theta)^3\Big[H^3z-\tfrac32H^2z^2+Hz^3-\tfrac14z^4\Big],\qquad U(H)=\tfrac14A(\rho_ig\sin\theta)^3H^4 .
> $$
>
>
> Discharge per unit width: $q=\int_0^HU \mathrm{d} z=\dfrac{A\tau_b^nH^2}{n+2}=\dfrac{A}{5}(\rho_ig\sin\theta)^3H^5$ for $n=3$. For $n=1$, $A=1/\mu$ this reduces to the Newtonian result. **Consequences**: (i) the effective viscosity $\mu_\mathrm{eff}=1/(A\tau^{n-1})$ *decreases* as stress increases: near the surface, where $\tau\to0$, the ice is a stiff plug; the deformation is concentrated near the bed (figure); (ii) $U_s\propto H^{n+1}\sin^n\theta$: doubling the thickness raises the speed $16\times$ for $n=3$ (against $4\times$ for Newtonian). *Numbers*: $H=200$ m, $\theta=3^\circ$: $\tau_b=917\times9.8\times0.0523\times200=94$ kPa; $U_s=\tfrac14(2.4\times10^{-24})(470)^3(200)^4=1.0\times10^{-7}$ m s$^{-1}=3$ m yr$^{-1}$; the effective viscosity at $\tau_b=10^5$ Pa is $1/(2.4\times10^{-24}\times10^{10})=4\times10^{13}$ Pa s. Since ice cannot support a shear stress $\gtrsim0.1$ MPa (flow rate becomes huge), $\tau_b\approx50$–$150$ kPa: glaciers adjust their thickness so that $H\approx\tau_b/(\rho_ig\sin\theta)$: $H\approx222$ m for $\theta=3^\circ$, $\tau_b=100$ kPa. For the worked glacier above ($q=9\times10^3$ m$^2$yr$^{-1}=2.9\times10^{-4}$ m$^2$s$^{-1}$, $\theta=5^\circ$): $H=(5q/[A(\rho_ig\sin\theta)^3])^{1/5}\approx260$ m, i.e. the ice discharge fixes the thickness.


![[ls_fig31.png]]
*Figure LS14.3. Normalised deformation-velocity profiles. With $n=3$ the profile is much more concentrated near the bed: the upper ice moves almost as a block.*


|  | Newtonian fluid (slides 47–49) | Glacier ice (Glen) | Mantle (long time scales) |
|---|---|---|---|
| Flow law | $\dot\epsilon=\tau/\mu$ | $\dot\epsilon=A\tau^n$, $n\approx3$ | diffusion creep $n=1$; dislocation creep $n\approx3$–$5$ |
| Surface speed $\propto$ | $H^2\sin\theta$ | $H^4\sin^3\theta$ (deformation) | – |
| Effective viscosity | constant | falls as stress rises, $\sim10^{13}$–$10^{14}$ Pa s | $10^{20}$–$10^{22}$ Pa s |
| Velocity profile | parabolic | plug-like, shear at bed | – |
| Bed condition | no slip | often sliding: $U=U_\mathrm{def}+U_s$ | – |
| Example | lava, mud | valley glaciers, ice sheets | plate tectonics, isostasy (Ch. 7) |

*Newtonian versus power-law flow.*

## Further slides explained one by one
<span class="scope-taught">taught</span> *the slides of this chapter's range that carry no derivation of their own; each image is followed by what it shows*

![[pre_144.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 144: Ice flow: viscous deformation plus sliding
> *Top left:* Newtonian viscous flow over an inclined plane: $dU/dz=\rho g\sin\theta\,(H-z)/\mu$ with parabolic profile $U(z)=(\rho g\sin\theta/\mu)(Hz-z^2/2)$ (A&A Eq. 8.8). *Below:* ice differs because it follows a power law with $n\approx3$ (Glen): $dU/dz=A\tau^n$, giving $U(z)=A[\rho g\sin\theta]^3[H^3z-\tfrac32z^2H^2+z^3H-\tfrac14z^4]$ (Eq. 8.16). *Right:* the sketch of an ice slab of thickness $H$ and width $w$ over planar bedrock with the velocity profile $u(z)$ made of a sliding part $U_s$ at the bed plus the deformation part $U_{\rm def}$, and the flux $Q_x$ into and out of the element (A&A Fig. 8.7).


## Map of this chapter
> [!connection] How LS14 connects
> **Previous:** [[LS13 Landslides]] · **Next:** [[LS15 Glacial Deposits Rebound and Sea Level]].
> **Other subjects:** [[Climate - Course Map]] (weathering and the carbon cycle, glaciation, orographic rainfall), [[Thermodynamics - Course Map]] (heat conduction and diffusion), [[Evolution of Earth and Life - Course Map]] (plate tectonics and landscapes through geological time), [[Waves - Course Map]] (diffusion and wave equations).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | slide content, figures read panel by panel | [[pre_ms_landscape_26.pdf]] slides 138–144 (images embedded from the PDF, auto-cropped, `scripts/render_slides.py`) | taught |
> | derivations, worked examples, tool boxes, TikZ figures | the AI-written derivation-level notes [[Landscapes_and_Their_Evolution_notes.pdf]] (EC2123 notes; LaTeX source in `landscape-notes-tex-source.tar.gz`), converted with `scripts/tex2vault_ls.py`; cross-checked against Anderson and Anderson and Turcotte and Schubert as cited there | secondary + extra/book |
>
> **Notes.** (1) The text of this chapter is the AI-written reference notes' text, converted to the vault's callout style and equation numbering (chapter-local, so some cross-references read as "(label)"). (2) The slide images were checked against the notes' slide numbers for a sample of slides (e.g. 1–12, 109–120 match). Figure descriptions are the notes', and should be compared with the images beside them. (3) The `[!verify]` items of the notes' last front-matter section ("Two places where the slides need care") are in [[Landscapes Notation and Glossary]].
