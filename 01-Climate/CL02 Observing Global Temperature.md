---
title: CL02 Observing Global Temperature
aliases: [CL02, Global mean temperature, Measuring temperature]
subject: climate
type: chapter
chapter: 2
part: I
scope: [taught, extra-book, extra-beyond]
by: [argha]
status: draft
prereq: ["[[CL01 Earth as a System]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/argha, status/draft]
---
# CL02 · Observing Global Temperature

◀ [[CL01 Earth as a System]] · [[Climate - Course Map|Course Map]] · [[CL03 Radiation and Planetary Energy Balance]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**
> - §1 what we measure and how (Argha L2 sl. 16–17)
> - §2 the IMD measurement protocol (sl. 18)
> - §3 variability and trend from minutes to a century, folding and Fourier analysis, "climate = 30-year average" (sl. 19–20)
> - §4 isotopic thermometers: ice cores and foraminifera (sl. 21–23)
> - §5 spatial variability and the global mean: area-weighted averaging of a sparse correlated field (sl. 24–25)
> - §6 anthropogenic warming beyond natural variability, drivers or forcing, future trajectory (sl. 26–27)
> - §7 Tutorial 1 style problems (sl. 28)
>
> 🟡 **Extra · book**
> - ice-core dating and the climate record of the last millennia: *The Earth System* Ch. 1 (in §4)
>
> 🔵 **Extra · beyond**
> - thermometer response time and radiation error (§1–2)
> - Rayleigh distillation model of δ¹⁸O (§4)
> - sampling theory: effective number of stations and of years (§5–6)
> - GISTEMP analysis with trends and uncertainties (§6)
> - CO₂ forcing arithmetic (§6)

> [!key] After this chapter you can
> - explain what a thermometer actually measures and why standards (screen, height, site) exist,
> - separate a noisy series into a daily cycle, an annual cycle and a trend by **folding** and **Fourier analysis**,
> - define a **global-mean temperature** and compute it correctly with **area weighting**, and say why we use anomalies,
> - read ancient temperatures from **δ¹⁸O**, and say what the proxy does and does not tell you,
> - fit a trend with an honest uncertainty and say what "beyond natural variability" means.

## 1. What is "the temperature of the Earth"?
<span class="scope-taught">taught</span> *Argha L2, slides 16–17*

The quantity is a **field** $T(\bar x,t)$: a temperature at every place and time [[climate_intro_L1_L6.pdf#page=17|(slide 17)]]. A *global mean* will be a single number extracted from it (§5). First, how do we measure it at one point?

**Direct measurement.** The **mercury thermometer** (≈ 1700 CE onward) and the **resistance thermometer** (a metal or semiconductor whose resistance depends on $T$, used in modern automatic stations). **Indirect measurement (proxies)**, for times before instruments: glacier length change, tree rings, proteins, even the **mineral assemblage in a rock** (thermobarometry, which reads the pressure–temperature conditions in which the minerals formed). **Remote sensing**: **thermal radiation** emitted by the surface or atmosphere, which satellites see ([[Stefan-Boltzmann Law]]). The slide suggests reading Wikipedia on the resistance thermometer and on thermobarometry.

> [!intuition] A thermometer reads *itself*
> A thermometer does not measure "the air's temperature": it measures **its own** temperature, which equals the air's only after enough time and only if nothing else (sunshine, the ground, rain) is heating or cooling it. Everything about good practice (shielding, ventilation, siting, §2) is about making the thermometer's own temperature a faithful stand-in for the air's.

> [!derivation]+ Response time of a thermometer (a leaky bucket again)
> Let the sensor have heat capacity $C_s$ [J K⁻¹], surface area $A$, and exchange heat with the air through a coefficient $h$ [W m⁻² K⁻¹]. Then
> $$C_s\frac{\mathrm dT_s}{\mathrm dt}=hA\,(T_a-T_s)\ \Rightarrow\ T_s(t)=T_a+(T_{s0}-T_a)\,e^{-t/\tau},\qquad\tau=\frac{C_s}{hA}.$$
> This is exactly the relaxation of [[CL03 Radiation and Planetary Energy Balance]] §6 ([[Relaxation Time]]). *Example:* a glass bulb of $C_s\approx0.75$ J K⁻¹, $A=1.5$ cm², in still air ($h\approx15$ W m⁻² K⁻¹): $\tau\approx0.75/(15\times1.5\times10^{-4})=330$ s (about 5 min); in a ventilated screen ($h\approx50$): $\approx100$ s. After $3\tau$ it has reached 95 % of a step change. Slow compared with a gust, fast compared with the daily cycle. *(🔵 order-of-magnitude estimate.)*

## 2. Measuring well: the IMD protocol
<span class="scope-taught">taught</span> *Argha L2, slide 18 (Perengiyil et al. 2025)* · <span class="scope-extra-beyond">extra · beyond</span> *why each rule, with numbers*

The India Meteorological Department (IMD) protocol on [[climate_intro_L1_L6.pdf#page=18|slide 18]]:

| rule | slide says | why |
|---|---|---|
| **Sensor height and shielding** | 1.25–2.0 m above ground, inside a **Stevenson screen** or radiation shield, **doors facing north** | the first metres have strong gradients, especially at night; the shield blocks sunlight and rain but lets air through; doors face away from the Sun (in the Northern Hemisphere) so that opening them does not put sun on the thermometer |
| **Site and exposure** | on **short grass** inside a **12 m × 15 m plot**, at least **4× the obstacle height** from tall structures | grass behaves like a natural surface (evaporation, albedo); distance from obstacles avoids shelter and shade |
| **Locations to avoid** | paved surfaces (**30 m buffer**), rooftops, slopes, heat exhausts, waterlogging | each of them adds or removes heat locally and would make the reading unrepresentative of the surroundings |
| **Synoptic network** | **1 station per district** (≈ 50–100 km) | the spacing is a design choice tied to the **spatial correlation length** of temperature (§5): neighbouring stations carry nearly the same information |

> [!example] Worked example: why a screen? The radiation error
> A bare, unshielded sensor in full sun absorbs shortwave. Take sunlight 800 W m⁻², sensor absorptivity $a=0.2$; for a thin cylinder crossing the beam the projected area is $1/\pi$ of its surface, so the absorbed flux per unit surface is $aS/\pi=51$ W m⁻². In equilibrium this equals $h(T_s-T_a)$: with $h=10$ W m⁻² K⁻¹ (still air) the sensor reads **5 K too warm**; ventilated ($h=50$) **1 K**. A screen both shades the sensor and lets air flow past it, cutting the error to a few tenths of a kelvin. *(🔵 my estimate.)*

> [!extra-beyond]- 🔵 Extra (beyond): what the protocol cannot fix
> (i) **Urban heat islands**: a growing city raises temperatures around a once-rural station; trend analyses compare with rural neighbours and apply homogenisation. (ii) **Station moves and instrument changes** introduce steps in the record. (iii) **Ocean temperature** (70 % of the surface) is measured from ships (buckets, engine intakes), moored and drifting buoys and Argo floats, and merged with land data. (iv) **Satellites** measure radiances that are converted to temperature layers. Because of these issues a global record is *constructed*, not read off an instrument; see [[Global Mean Surface Temperature]] and [[Reanalysis Data]].

## 3. Variability in time: minutes to a century
<span class="scope-taught">taught</span> *Argha L2, slides 19–20 (Pune hourly ERA5)* · <span class="scope-extra-beyond">extra · beyond</span> *worked analysis of a synthetic series*

[[climate_intro_L1_L6.pdf#page=19|Slides 19–20]] show **hourly ERA5 reanalysis temperatures for Pune** (1940 onward; see [[Reanalysis Data]]): a dense blue band, from which the observations are:

- **"Noise" at all scales, but the mean and the spread are well defined.**
- **Periodicity at daily and annual scale**: what are the corresponding amplitudes?
- **A 30-year average (of weather) smooths out the cycles relevant to human time scales, so it is defined as "climate".**
- Is there a **warming trend**? What about **extreme values**?
- "Folding or Fourier transforming can reveal periodicity in noisy data."

> [!intuition] Climate is the long-exposure photograph
> A single frame of a street shows one car; a long exposure shows the *road*. Weather is the instantaneous frame; climate is the picture averaged over enough time that the passing noise blurs out and the persistent structure (the mean, the seasonal swing, the extremes' envelope) remains. The question "how long an exposure?" is answered in §3.3.

### 3.1 Folding
To find a cycle of period $P$ in noisy data, **fold** the record: cut it into pieces of length $P$ and average them point by point. The cycle adds up coherently, the noise averages out like $1/\sqrt N$.

> [!intuition] Stacking transparencies
> Draw the same faint wave on 1000 transparencies, each with different random scribbles on top. Stack them against a lamp: the scribbles blur out, the wave gets darker. Folding is stacking: the signal is the same on every sheet, the noise is not.

### 3.2 Fourier analysis
Write the series as a sum of sinusoids, $T(t)=\bar T+\sum_k A_k\cos(2\pi f_kt-\varphi_k)$; the **amplitude spectrum** $A(f)$ shows how much variability sits at each frequency, and cycles appear as **peaks**. For a record of $n$ samples the amplitude of a pure sinusoid is recovered by $A_k=2|X_k|/n$ with $X_k$ the discrete Fourier transform.

> [!intuition] A prism for a time series
> A prism splits white light into colours and shows how much of each there is. The Fourier transform does the same to a time series, splitting it into "tones" (1 year, 1 day, 12 hours …). The noise appears as a broad, low background and the cycles as sharp spikes above it.

![[fig_cl02_fold_fft.png|760]]
*Figure CL2.1. A synthetic Pune-like record (not measurements): annual amplitude 3.5 °C, daily amplitude 6.0 °C plus a 12 h harmonic of 1.2 °C, AR(1) weather noise of 1.8 °C with 2-day memory, ten years of hourly data. See: (1) the daily cycle is visible but wobbly; (2) folding 3,652 days modulo 24 h gives a clean cycle, 31.7 °C at 14:00 and 19.7 °C at 02:00 (half-range 5.99 against the 6.0 put in); (3) the Fourier spectrum shows the three peaks standing 2–3 orders of magnitude above the noise: 3.38 at 1 yr (input 3.5), 6.00 at 1 day, 1.20 at 12 h. Script `fig_cl02_fold_fft.py`.*

> [!example] Worked example: how precisely does folding recover the daily amplitude?
> At a fixed hour of day, the scatter of the 3,652 values is about $\sigma\approx3$ K (annual cycle $3.5/\sqrt2=2.5$ K plus weather 1.8 K). The standard error of the composite mean at that hour is $\sigma/\sqrt N=3/\sqrt{3652}=0.05$ K (larger if consecutive days are correlated). So the daily amplitude is known to ≈ 0.07 K, from a signal 100 times larger than that. With only 100 days of data it would be $3/\sqrt{100}=0.3$ K.

### 3.3 Why "30 years"?
The **climate normal** is conventionally a **30-year** mean (the WMO standard period; the current reference is 1991–2020). It is a compromise: **long enough** that year-to-year fluctuations (El Niño, volcanic years, decadal swings) average out: the standard error of a mean of $N$ independent years of scatter $\sigma$ is $\sigma/\sqrt N$, e.g. $0.1/\sqrt{30}=0.02$ K; and **short enough** that it still follows slow change. If the climate is trending, the normal is a moving target (see the 1991–2020 mean of +0.61 K relative to 1951–80, §6).

> [!extra-beyond]- 🔵 Extra (beyond): the time scale decides what is "signal"
> The Stommel diagram of [[CL01 Earth as a System]] says the same thing: a 1-day mean removes the weather's minutes, a 30-year mean removes the ocean's decades; each average defines a different "climate". Anything slower than the averaging window is a **trend**, anything faster is **variability**. The split is a *choice* tied to the question.

## 4. On longer time scales: isotopic thermometers
<span class="scope-taught">taught</span> *Argha L2, slides 21–23* · <span class="scope-extra-book">extra · book</span> *Kump et al. Ch. 1: ice-core layers, Little Ice Age* · <span class="scope-extra-beyond">extra · beyond</span> *Rayleigh model*

Instrumental records are about 150 years long. To go further back we need **proxies**. The slides use **stable oxygen isotopes** as a thermometer [[climate_intro_L1_L6.pdf#page=21|(slide 21)]]. Drill **cores** through layers of **ice** or of **ocean sediment** (containing the calcium-carbonate shells of **foraminifera**), measure the ratio of the heavy isotope $^{18}$O to the light $^{16}$O, and express it relative to a standard:

$$\delta^{18}\mathrm O=\left(\frac{(^{18}\mathrm O/^{16}\mathrm O)_{\rm sample}}{(^{18}\mathrm O/^{16}\mathrm O)_{\rm standard}}-1\right)\times1000\ \text{‰}.$$

Reconstruct temperature by **calibrating** $\delta^{18}\mathrm O$ against temperature with empirical relations, and use **time markers** to convert depth to time (slide 23). See [[Isotopic Thermometers]].

> [!example] Worked example: the δ-notation
> The standard (VSMOW seawater) has $^{18}$O/$^{16}$O $=2005.2\times10^{-6}$. A polar ice sample measuring $1.905\times10^{-3}$ has $\delta=(1.905/2.0052-1)\times1000=-50.0$ ‰: its heavy-isotope fraction is 5 % *lower* than the standard's. A change of 1 ‰ is a change of 0.1 % in the ratio: a tiny signal, which is why mass spectrometers and careful standards are needed.

**Why does it work? The slide-22 logic.**
1. **Evaporation prefers $^{16}$O** (the lighter water molecule evaporates slightly more readily), so vapour is isotopically *light* and the ocean slightly heavy.
2. On the way to the **cold poles**, the air cools and rains out; **$^{18}$O rains out preferentially**, so the remaining vapour gets progressively lighter. Polar snow has $\delta^{18}\mathrm O\approx-50$ ‰ (range −35 to −55 ‰).
3. The colder the site, the more rain-out, the lighter the snow: **ice $\delta^{18}\mathrm O$ is a thermometer**.
4. When **light ice sheets grow**, they lock up $^{16}$O, so the **ocean** becomes *heavier* (and colder); foraminifera build **heavier CaCO₃** shells; when they die the shells archive the signal in the **ocean bottom** sediment.

> [!intuition] Heavy raindrops fall first, so the cloud gets lighter
> Imagine a bank account that pays out a little more of the "heavy" coins than their share every time you withdraw. As withdrawals continue (each rain-out), the remaining balance becomes steadily lighter in heavy coins. The farther and colder the journey, the more withdrawals have happened, so polar snow is the lightest.

![[fig_cl02_d18o.png|760]]
*Figure CL2.2. Left: $\delta^{18}\mathrm O$ of precipitation from a simple Rayleigh-distillation model against condensation temperature (blue), and the empirical spatial relation of Dansgaard (1964) (orange dashed). See: both fall as it gets colder; the idealised model (no mixing, no kinetic effects) is steeper (1.6 ‰ per °C against 0.7). Right: the fractionation factor $(\alpha-1)\times1000$ grows as it gets colder, and is larger for ice–vapour than for liquid–vapour. Script `fig_cl02_d18o.py`.*

> [!extra-beyond]+ 🔵 Extra (beyond): Rayleigh distillation, derived
> Let $N$ be the amount of water vapour in an air parcel and $R=N_{18}/N_{16}$ its isotope ratio. Equilibrium condensation removes a small amount $\mathrm dN$ of condensate whose ratio is $\alpha R$, where $\alpha>1$ is the **fractionation factor** (heavy isotope favoured in the condensate). Conservation of the heavy isotope gives
> $$\mathrm d(RN)=\alpha R\,\mathrm dN\ \Rightarrow\ N\,\mathrm dR=(\alpha-1)R\,\mathrm dN\ \Rightarrow\ \frac{\mathrm dR}{R}=(\alpha-1)\frac{\mathrm dN}{N}.$$
> With constant $\alpha$ and $F=N/N_0$ the fraction of vapour left, $R=R_0F^{\alpha-1}$, i.e. $\delta_v=(1+\delta_{v0})F^{\alpha-1}-1$, and the precipitation has $R_p=\alpha R$. Since $\alpha-1\approx0.01$–0.02 and $F$ falls to 0.01–0.1 over a trajectory from the tropics to the poles, $F^{\alpha-1}\approx e^{-(\alpha-1)\ln(1/F)}$ shifts $\delta$ by tens of per mil. The fractionation factor itself depends on temperature (Majoube 1970, 1971): $\ln\alpha_{\rm liq-vap}=1137/T^2-0.4156/T-0.0020667$ and $\ln\alpha_{\rm ice-vap}=11.839/T-0.028244$. At 20 °C, $\alpha=1.0098$, so the first vapour has $\delta=(1/1.0098-1)\times1000=-9.7$ ‰ over a 0 ‰ ocean; at −20 °C the ice–vapour value is 18.7 ‰.
> The remaining fraction $F$ is set by cooling: with relative humidity constant the vapour that remains is proportional to the saturation vapour pressure $e_s(T)$ (Clausius–Clapeyron, [[Clausius-Clapeyron Relation]]), $F=e_s(T)/e_s(T_0)$. Integrating the equations numerically from 20 °C gives precipitation $\delta^{18}\mathrm O=-9$ ‰ at 0 °C, −35 ‰ at −20 °C and −72 ‰ at −40 °C (Fig. CL2.2).

> [!verify] Model versus observed slope
> The simple Rayleigh model's slope (1.6 ‰ per °C between −5 and −40 °C) is about twice the empirical spatial slope of Dansgaard (0.695 ‰ per °C, $\delta^{18}\mathrm O=0.695\,T_{\rm ann}-13.6$). Real air masses mix, receive vapour from several sources, do not rain out completely and fractionate kinetically at supersaturation, all of which make $\delta$ less sensitive to $T$; condensation temperature is also higher than the surface temperature in an inversion. Moreover **temporal** slopes (how $\delta$ at one site changes as the climate changes) are different again, typically smaller (≈ 0.3–0.5 ‰ per °C in Greenland) `[verify]`. The slide's phrase "calibrating using empirical relations" therefore matters: the $\delta$–$T$ relation is **an empirical calibration, not a law**.

**The marine record.** Foraminiferal $\delta^{18}\mathrm O$ records two things at once: the **ice-volume** effect (more ice ⇒ heavier ocean) and the **temperature** at which the shell grew (colder ⇒ heavier carbonate, about 0.23 ‰ per °C `[verify]`). Which dominates depends on the species and place: benthic (deep-sea) foraminifera mostly record **ice volume**, since the deep ocean is always cold. Slide 22's lower panels plot an Antarctic ice-core record (EPICA Dome C) and a benthic stack (LR04) over the last 300 kyr; both oscillate with the glacial cycles, mirror images because ice is isotopically light while the ocean is heavy. (The slide credits the figure to Gemini: treat its curves as illustrative; the real records are Jouzel et al. 2007 and Lisiecki & Raymo 2005.)

> [!extra-book]+ 🟡 Extra (book): ice layers and the recent past
> *The Earth System* Chapter 1 explains how **annual layers of snow** in an ice core can be **counted** to date the ice ([[vdoc.pub_the-earth-system.pdf#page=13|PDF p.13]], book p.5) and how the record shows, for example, an unusually cool period between about 1500 and 1850, the **Little Ice Age** ([[vdoc.pub_the-earth-system.pdf#page=15|PDF p.15]], book p.7). This is the "time marker" idea of slide 23: besides counting layers, one uses volcanic ash or sulfate spikes, radiocarbon, reversals of the magnetic field in sediments, and flow models of the ice. *Not shown in the slides.*

## 5. Variability in space, and the global mean
<span class="scope-taught">taught</span> *Argha L2, slides 24–25 (Hansen & Lebedeff 1987)* · <span class="scope-extra-beyond">extra · beyond</span> *derivation of the weights, sampling theory*

[[climate_intro_L1_L6.pdf#page=24|Slide 24]] shows an ERA5 map of temperature at 13:00 UTC on 6 Aug 2025 and asks: **how do we define the global-mean temperature?** The difficulties: **stations are sparse** and **heterogeneously distributed**; so the recipe has two steps:

1. a **time average** (an annual mean, or a particular day);
2. a **spatial average**: by an **arithmetic** or by an **area-weighted** average?

### 5.1 Area weighting
Slide 25: grid the data first, then
$$\bar T=\frac{\sum_iT_iA_i}{\sum_iA_i},$$
where $A_i$ is the area of grid cell $i$. Why this and not the plain mean? A 5° × 5° cell near the equator covers far more surface than one near the pole.

> [!intuition] The map with a giant Greenland
> On a flat map of the world (Mercator) Greenland looks as big as Africa; in reality Africa is 14 times larger. If you averaged the map's pixels you would let Greenland vote as much as Africa. Equal-angle grid cells are the same trap: a ring of cells at 80° latitude is a few percent of the area of one at the equator but would get the same vote.

> [!derivation]+ Why the weight is $\cos\varphi$
> On a sphere of radius $a$ the area element is $\mathrm dA=a^{2}\cos\varphi\,\mathrm d\varphi\,\mathrm d\lambda$ (latitude $\varphi$, longitude $\lambda$). The exact global mean of a field $T(\varphi,\lambda)$ is
> $$\bar T=\frac{1}{4\pi a^{2}}\int_{-\pi/2}^{\pi/2}\!\!\int_0^{2\pi}T\,a^{2}\cos\varphi\,\mathrm d\lambda\,\mathrm d\varphi=\frac{\int T\cos\varphi\,\mathrm d\varphi\,\mathrm d\lambda}{\int\cos\varphi\,\mathrm d\varphi\,\mathrm d\lambda},$$
> since $\int\cos\varphi\,\mathrm d\varphi=2$ and $\int\mathrm d\lambda=2\pi$ give the $4\pi$. A grid cell of size $\Delta\varphi\times\Delta\lambda$ centred at $\varphi_i$ has area $A_i\approx a^{2}\cos\varphi_i\,\Delta\varphi\,\Delta\lambda\propto\cos\varphi_i$, so the discrete form is $\bar T=\sum T_i\cos\varphi_i/\sum\cos\varphi_i$, the slide's formula. See [[Area-Weighted Averaging]].

![[fig_cl02_area_weight.png|760]]
*Figure CL2.3. Left: the relative area of a 5° × 5° cell falls like $\cos\varphi$ (4 % at the poles' cell, 100 % at the equator). Right: for a toy field $T=255+45\cos^2\varphi$ K (300 K at the equator, 255 K at the poles) the area-weighted mean is 285.0 K, the plain average over latitude bands is 277.5 K: a **7.5 K cold bias** from giving the poles too much weight. Script `fig_cl02_area_weight.py`.*

> [!example] Worked example: three bands
> Take the northern hemisphere in three latitude bands, 0–30°, 30–60°, 60–90°, with mean temperatures 297, 277.5 and 258 K. Their areas (as a fraction of the hemisphere) are $\sin\varphi_2-\sin\varphi_1$: $0.500,\ 0.366,\ 0.134$. The arithmetic mean is $(297+277.5+258)/3=277.5$ K; the area-weighted mean is $(297\times0.500+277.5\times0.366+258\times0.134)=284.6$ K. The exact value for the smooth field is 285.0 K, so even this coarse three-band estimate is within 0.4 K, whereas the plain mean is 7.5 K off. In Python:
> ```python
> import numpy as np
> lat = np.arange(-87.5, 90, 5); lon = np.arange(2.5, 360, 5)
> T = 255 + 45*np.cos(np.radians(lat))[:, None]**2 + 0*lon[None, :]   # toy field
> w = np.cos(np.radians(lat))[:, None] * np.ones(lon.size)            # area weights
> print(T.mean(), (T*w).sum()/w.sum())                                # 277.5  284.99
> ```

### 5.2 Why anomalies, and how sparse stations can be enough
**Absolute temperatures are a poor thing to average**: they depend strongly on altitude (about −6.5 K per km) and local setting. If a station is moved from sea level to a hill 500 m higher, its temperature drops by $\approx3.3$ K, although nothing happened to the climate. So analyses such as GISTEMP convert each station to an **anomaly** $T'=T-\bar T_{\rm ref}$ relative to its own reference period (1951–1980 in GISTEMP), and average the *anomalies*.

> [!intuition] Ask the street, not the whole city
> If it is 2 K warmer than usual on your street, it is almost certainly about 2 K warmer than usual on the next street, but the *absolute* temperatures of the two streets (one on a hill, one in a valley) may differ by 5 K. Anomalies are shared over distance; absolute values are not. That shared pattern is the **spatial correlation**, and it is what lets **sparse** stations stand for a large area.

Hansen & Lebedeff (1987) (slide 25–26) quantified this: the correlation between temperature *anomalies* at two stations falls with their separation, and is useful out to about 1000–1200 km at mid and high latitudes (`[verify]` the exact radius for the tropics), so each station can speak for a disc around it and the global mean can be built from several hundred stations in the early record. The NASA page linked on slides 25–27 ("Measuring global temperature") describes the modern version.

> [!extra-beyond]- 🔵 Extra (beyond): sampling error of a correlated field
> If the $N$ samples each have variance $\sigma^{2}$ and every pair has correlation $\rho$, the variance of their mean is
> $$\mathrm{Var}(\bar T)=\frac{\sigma^{2}}{N}\big[1+(N-1)\rho\big]\ \Rightarrow\ N_{\rm eff}=\frac{N}{1+(N-1)\rho}\ \xrightarrow{N\to\infty}\ \frac1\rho .$$
> With $\rho=0.2$ even **1000 stations** give only $N_{\rm eff}=5$ independent pieces of information: *adding stations in the same neighbourhood does not help*; spreading them out does. For a time series with lag-1 autocorrelation $r$ the analogue is $N_{\rm eff}=N(1-r)/(1+r)$ (used in §6). The design of the IMD network (§2) follows this logic: density where the correlation length is short (rainfall: tens of km), sparser where it is long (temperature: hundreds of km).

## 6. Anthropogenic warming: beyond natural variability?
<span class="scope-taught">taught</span> *Argha L2, slides 26–27: area-weighted global mean, "beyond natural variability?", drivers or forcing, future trajectory* · <span class="scope-extra-beyond">extra · beyond</span> *analysis of the real GISTEMP series, trend uncertainty, CO₂ arithmetic*

Slides 26–27 pose the questions: given a global-mean series, **is the warming beyond natural variability?** What are the **drivers or forcings**? What is the **future trajectory**? Let us do the analysis with real data. The global land–ocean temperature **anomaly** (relative to 1951–1980) from NASA GISS (GISTEMP v4), annual mean, 1880–2025:

![[fig_cl02_gistemp.png|720]]
*Figure CL2.4. Real data: NASA GISTEMP v4, global land–ocean annual anomaly, base 1951–1980; file `Assets/data/GISTEMP_GLB_Ts_dSST.txt` fetched 2026-10-23. See: the series is flat to 1910, rises to 1940, is nearly flat to the mid-1970s and then climbs steadily; the 5-year mean (black) follows the linear trend since 1975 (red dashed, 0.21 K per decade). Script `fig_cl02_gistemp.py`.*

**Numbers computed from the file:**
- **Anomalies**: −0.17 K (1880), +1.01 (2016), +1.17 (2023), **+1.28 (2024, the record)**, +1.18 (2025).
- **Climate normal:** the 1991–2020 mean is **+0.61 K** relative to 1951–80 (by construction the 1951–80 mean is 0).
- **Trends** (least squares, K per decade; $\pm$ is the standard error with the autocorrelation correction below): **1975–2025: $0.207\pm0.014$**; 1985–2025: $0.225\pm0.020$; 1880–2025: $0.083\pm0.012$; 1951–1980: $0.051\pm0.025$.
- The year-to-year scatter about the 1975–2025 trend is **0.106 K** (standard deviation); lag-1 autocorrelation of the residual $r=0.32$.

> [!intuition] A dog on a long leash
> A walker (the forced trend) crosses a park while the dog (natural variability: El Niño, volcanoes, chance) runs around her, up to a few tenths of a kelvin away. From one photograph you cannot say where the walker is going; but from decades of photographs the average position of the dog moves steadily, and its zig-zags are small compared with the distance travelled. **Detecting** a trend means showing the walker's displacement is much larger than the dog's wanderings.

> [!derivation]+ Trend and its uncertainty
> Fit $T_i=a+b\,y_i+\epsilon_i$ over $n$ years by least squares. The slope is $b=\sum(y_i-\bar y)(T_i-\bar T)/\sum(y_i-\bar y)^2$, with standard error
> $$\mathrm{SE}(b)=\frac{s}{\sqrt{\sum(y_i-\bar y)^2}},\qquad s^{2}=\frac{\sum\epsilon_i^{2}}{n-2}.$$
> This assumes independent errors. Climate residuals are **autocorrelated** (a warm year tends to be followed by another warm year); with lag-1 correlation $r$ the effective number of independent points is $n_{\rm eff}=n(1-r)/(1+r)$ and the standard error is inflated by $\sqrt{n/n_{\rm eff}}$. *Numbers:* for 1975–2025, $n=51$, $s=0.106$ K, $r=0.32$: $\sum(y-\bar y)^2=51(51^2-1)/12=11{,}050$, so naive SE $=0.106/105=0.0010$ K yr⁻¹ $=0.010$ K per decade; $n_{\rm eff}=26$, inflation $1.4$, SE $=0.014$ K per decade. The trend $0.207$ K per decade is about **15 standard errors** from zero: *detection* is not in doubt.

> [!example] Worked example: a short window is a poor window
> Fit the last ten years, 2016–2025 (1.01, 0.91, 0.85, 0.98, 1.01, 0.85, 0.89, 1.17, 1.28, 1.18). The slope is $0.32$ K per decade with a standard error of $\pm0.13$ (naive): it is *more than the 50-year trend* but far less certain; only 2.4 standard errors from zero, and in a different window it could as easily be near zero. Short trends are dominated by variability (a strong El Niño at the end, or the 1998 spike at the start of a window, changes them a lot). Hence "climate" trends are quoted over 30 years or more.

**Natural variability is real:** the record shows spikes such as 1998 (+0.61 K against +0.47 in 1997 and +0.38 in 1999, a strong El Niño) and dips after large volcanic eruptions (1982–83 after El Chichón; **1992 after Pinatubo: +0.22 K against +0.41 in 1991**, ≈ −0.2 K as sulfate aerosols reflected sunlight). These are of the order 0.1–0.3 K: **comparable to the whole warming of the 1900s but small against the 1.2 K of today.** The *detection* of change (is it unusual compared with natural variability?) is thus easy for the global mean over decades; *attribution* (what *caused* it?) needs physics: the energy balance of [[CL03 Radiation and Planetary Energy Balance]] and [[CL04 Feedback and Multiple Steady States]].

**Drivers or forcing? (slide 27)** A **radiative forcing** $F$ is a change in the net energy input at fixed temperature ([[Radiative Forcing]]). The main anthropogenic drivers are the **long-lived greenhouse gases** (CO₂, CH₄, N₂O), **aerosols** (cooling), land-use change (albedo); natural ones are **solar** variations and **volcanoes**. A simple link is CL04's relation $\Delta T\approx\Lambda\,F$.

> [!example] Worked example: how much warming does the CO₂ increase alone suggest?
> The CO₂ forcing is well approximated by $F=5.35\ln(C/C_0)$ W m⁻² (Myhre et al. 1998). With $C_0=280$ ppm (pre-industrial) and $C\approx420$ ppm: $F=5.35\ln1.5=2.17$ W m⁻². With the sensitivities of CL04, $\Lambda_P=0.27$–0.30 K per W m⁻² without feedbacks, and a gain of about 2 with them ($\Lambda\approx0.5$–0.6): $\Delta T\approx2.17\times0.5=1.1$ K, about the observed 1.2 K (observed $\approx$ 0.4 K per W m⁻² of total forcing, as in CL04 §1). The agreement in order of magnitude, from a one-line physical estimate, is the core of the attribution argument; the detailed attribution (GHGs vs aerosols vs natural) uses climate models. *(🔵 illustration, not a detection-and-attribution study; CO₂ values from NOAA `[verify]`.)*

**Future trajectory** depends on emissions scenarios and on the feedbacks of CL04; for the climate model hierarchy see [[Zero-Dimensional Energy Balance Model]] (bottom rung) upward. The slide only poses the question.

## 7. Tutorial 1: numerical problems and a time-series analysis
<span class="scope-taught">taught</span> *Argha L2, slide 28: numerical problems, analysis of the Pune temperature series*

Slide 28 announces **Tutorial 1**: numerical problems and an analysis of the Pune time series. The problems and data are not in the slides, so the exercises below are written here in the same spirit, with **full solutions**. To rehearse the Pune analysis on a record of your own, use these steps (with ERA5 hourly data for a point, [[Reanalysis Data]]): (1) fold modulo 24 h and modulo one year; (2) FFT and check the peaks at 1/day and 1/yr; (3) subtract the two cycles to get anomalies; (4) compute annual means and a trend with its autocorrelation-corrected error; (5) look at the extremes (95th and 99th percentiles) per decade.

> [!pitfall] Typical mistakes in this chapter
> - Averaging temperatures over **latitude** without weighting by $\cos\varphi$.
> - Averaging **absolute** temperatures from stations at different altitudes (use anomalies).
> - Quoting a trend without the **window** and the **uncertainty**; or calling a trend "significant" using the naive error on autocorrelated data.
> - Treating $\delta^{18}\mathrm O$ as a universal thermometer: the slope is a calibration, differing between space and time and between ice and ocean.
> - Folding with a period that is not exactly right (24 h is fine; one year is 365.25 days).

## Map of this chapter
> [!connection] How CL02 connects
> **Builds on:** [[CL01 Earth as a System]] (weather vs climate, time scales)
> **Leads to:** [[CL03 Radiation and Planetary Energy Balance]] (what sets the global mean $T$: the 255 K and the 33 K) → [[CL04 Feedback and Multiple Steady States]] (how $\Delta T$ responds to forcing) → CL10 (latitudinal structure of $T$)
> **Concepts:** [[Global Mean Surface Temperature]] · [[Area-Weighted Averaging]] · [[Isotopic Thermometers]] · [[Radiative Forcing]] · [[Climate vs Weather]] · [[Reanalysis Data]] · [[Relaxation Time]] · [[Clausius-Clapeyron Relation]] · [[Planck Sensitivity]] · [[Climate Feedback Factor]]
> **Other subjects:** [[Probability - Course Map]] (sampling, autocorrelation, standard error, confidence intervals) · [[Waves - Course Map]] (Fourier analysis) · [[Thermodynamics and Statistical Mechanics - Course Map]] (blackbody emission used by satellites; Clausius–Clapeyron) · [[Evolution of Earth and Life - Course Map]] (paleoclimate proxies) · [[Landscapes and Geomorphology - Course Map]] (glaciers as thermometers)

> [!connection] Statistics, signal processing
> Folding is *averaging over an ensemble of cycles*, the Fourier transform is a change of basis, and the trend uncertainty is a regression with correlated noise: all ordinary probability and statistics ([[Probability - Course Map]], [[Waves - Course Map]] for Fourier). The central message, **error ∝ $1/\sqrt{N_{\rm eff}}$ and $N_{\rm eff}<N$**, applies equally to stations in space and years in time.

> [!connection] Isotopes and thermodynamics
> The temperature dependence of the fractionation factor is a statistical-mechanics result about the vibrational energies of heavy and light water molecules (quantum mechanics, [[Quantum Mechanics - Course Map]]), and the amount of vapour left depends on [[Clausius-Clapeyron Relation]].

## Summary
> [!summary] Cheat-sheet
> - $T(\bar x,t)$ is a field; a thermometer measures *itself* ($\tau=C_s/hA$); screen, 1.25–2 m height, grass site, ≥4× obstacle distance, 30 m from pavement, 1 station per district (IMD).
> - Time: noise at all scales; daily and annual cycles; **climate = 30-year average** (1991–2020 = +0.61 K vs 1951–80). **Fold** (error $\propto1/\sqrt N$) and **Fourier** ($A=2|X_k|/n$) reveal cycles.
> - **δ¹⁸O** $=(R/R_{\rm std}-1)\times1000$ ‰ (VSMOW 2005.2×10⁻⁶); evaporation favours $^{16}$O; $^{18}$O rains out first ⇒ colder = lighter snow (≈ −50 ‰ polar); ice sheets light ⇒ ocean and forams heavy; calibration is empirical (spatial slope 0.69 ‰ per °C); depth→time by markers.
> - **Global mean:** area-weighted, $\bar T=\sum T_iA_i/\sum A_i$, $A_i\propto\cos\varphi_i$; arithmetic over latitude is biased (7.5 K in the toy). Use **anomalies**; correlation (~1000 km) lets sparse stations suffice; $N_{\rm eff}=N/(1+(N-1)\rho)$.
> - **Trend:** 0.207 ± 0.014 K per decade (1975–2025, AR(1)-corrected); short windows are unreliable; natural variability ±0.1–0.3 K (El Niño, volcanoes).
> - **Forcing:** $F_{\rm CO_2}=5.35\ln(C/C_0)=2.17$ W m⁻² for 280→420 ppm; $\Delta T\approx\Lambda F\approx1.1$ K.

## Practice
1. **Thermometer.** A sensor has $C_s=0.4$ J K⁻¹, $A=1$ cm², $h=20$ W m⁻² K⁻¹. Find $\tau$ and the time to get within 5 % of a step change.
2. **Radiation error.** A sensor of absorptivity 0.3 sits unshielded in 900 W m⁻² sunlight, $h=12$ W m⁻² K⁻¹, cylinder geometry. Estimate the error. What ventilation ($h$) cuts it below 0.5 K?
3. **Folding.** A series $T=20+5\cos[2\pi(h-15)/24]+\epsilon$ with $\epsilon$ of standard deviation 3 K is observed for 100 days. What is the standard error of the composite at each hour, and how many days would give ±0.1 K?
4. **Area weighting.** Southern-hemisphere bands 0–30°, 30–60°, 60–90° have means 296, 280, 245 K. Compute the area-weighted mean and the plain mean. Which is higher, and why?
5. **Altitude.** A station moves from 100 m to 700 m. Absolute temperature change at 6.5 K km⁻¹? Why is the anomaly (almost) unaffected?
6. **δ¹⁸O.** (a) A sample has $^{18}$O/$^{16}$O $=1.9253\times10^{-3}$. Find $\delta$. (b) Using $\delta=0.695T-13.6$ estimate the annual mean temperature of the site where it fell.
7. **Trend.** Show that for $n$ equally spaced years $\sum(y-\bar y)^2=n(n^{2}-1)/12$ and use it to find the naive standard error of the slope for $n=30$, $s=0.1$ K.
8. **Sampling.** 400 stations, mean pairwise correlation 0.25. Find $N_{\rm eff}$. How many independent stations would it take to halve the error if $\rho=0$?
9. **CO₂.** Calculate $F=5.35\ln(C/C_0)$ for a doubling, and the equilibrium warming with $\Lambda=0.8$ K per W m⁻².
10. **Conceptual.** Why is a 50-year trend of the *global mean* far better determined than a 50-year trend of the temperature at one station?

> [!example]- Solutions
> 1. $\tau=0.4/(20\times10^{-4})=200$ s; within 5 %: $e^{-t/\tau}=0.05\Rightarrow t=3.0\tau=600$ s (10 min).
> 2. $aS/\pi=0.3\times900/\pi=86$ W m⁻²; $\Delta T=86/12=7.2$ K. Need $h>86/0.5=172$ W m⁻² K⁻¹: unrealistically high for a bare sensor, hence the screen/shade.
> 3. SE $=3/\sqrt{100}=0.3$ K; for ±0.1 K: $N=(3/0.1)^2=900$ days.
> 4. Areas: $0.500,0.366,0.134$. Weighted: $296\times0.5+280\times0.366+245\times0.134=148+102.5+32.8=283.3$ K. Plain: $(296+280+245)/3=273.7$ K. The weighted value is higher because the warm tropics have more area than the cold polar band.
> 5. $\Delta z=0.6$ km ⇒ $-3.9$ K absolute (a step in the record). The anomaly is measured relative to the station's own reference period at the *same* altitude, so the offset cancels (a break in the record still needs homogenisation).
> 6. (a) $1.9253/2.0052-1=-0.0398\Rightarrow\delta=-39.8$ ‰. (b) $T=(\delta+13.6)/0.695=(-39.8+13.6)/0.695=-37.7$ °C.
> 7. $\sum(y-\bar y)^2=2\sum_{k=1}^{n/2}\big(k-\tfrac12\big)^2=n(n^2-1)/12$ (check $n=3$: $1+0+1=2=3\cdot8/12$ ✓). For $n=30$: $30\times899/12=2247$; SE $=0.1/\sqrt{2247}=0.0021$ K yr⁻¹ $=0.021$ K per decade.
> 8. $N_{\rm eff}=400/(1+399\times0.25)=3.98\approx4$. For $\rho=0$ the error is $\sigma/\sqrt N$; to halve it you need 4× the independent stations: with $N_{\rm eff}=4$, going to 16 *independent* ones. Adding correlated stations does nothing.
> 9. $F=5.35\ln2=3.71$ W m⁻²; $\Delta T=0.8\times3.71=3.0$ K.
> 10. The global mean averages out much of the local variability (weather noise is partly independent across regions, so it falls roughly like $1/\sqrt{N_{\rm eff}}$ with the number of independent regions), whereas a single station keeps all of its local variability (≈ 1 K year-to-year) on top of the same forced trend: a worse signal-to-noise ratio.

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (8): the other tool's concept notes from the lectures, unreviewed
> [[zettel/area-weighted-mean-temperature|Area-Weighted Mean Temperature]] · [[zettel/glacial-ice-volume-effect-on-seawater-isotopes|Glacial Ice Volume Effect on Seawater Isotopes]] · [[zettel/liquid-in-glass-thermometer-calibration|Liquid-in-Glass Thermometer Calibration]] · [[zettel/multi-scale-temperature-variability|Multi-Scale Temperature Variability]] · [[zettel/oxygen-isotope-paleothermometry|Oxygen Isotope Paleothermometry]] · [[zettel/secular-temperature-trend-estimation|Secular Temperature Trend Estimation]] · [[zettel/stevenson-screen-standard-measurement|Stevenson Screen Standard Measurement]] · [[zettel/surface-temperature-field-survey|Surface Temperature Field Survey]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | $T(\bar x,t)$, measurement methods (mercury, resistance, proxies, thermal radiation) | [[climate_intro_L1_L6.pdf#page=17\|Argha L2 sl. 16–17]] | taught |
> | IMD protocol | [[climate_intro_L1_L6.pdf#page=18\|Argha L2 sl. 18]] (Perengiyil et al. 2025) | taught |
> | variability and trend, Pune ERA5, folding/Fourier, climate = 30-year mean | [[climate_intro_L1_L6.pdf#page=19\|Argha L2 sl. 19–20]] | taught |
> | isotopic thermometers, $\delta^{18}$O, ice sheets and forams, depth→time | [[climate_intro_L1_L6.pdf#page=21\|Argha L2 sl. 21–23]] | taught |
> | spatial variability, global mean, area-weighted averaging, Hansen & Lebedeff | [[climate_intro_L1_L6.pdf#page=24\|Argha L2 sl. 24–25]] | taught |
> | anthropogenic warming beyond natural variability, drivers/forcing, future | [[climate_intro_L1_L6.pdf#page=26\|Argha L2 sl. 26–27]] | taught |
> | Tutorial 1 | [[climate_intro_L1_L6.pdf#page=28\|Argha L2 sl. 28]] (problems not in the deck; written here) | taught (topic) |
> | ice-core layer counting; Little Ice Age | [[vdoc.pub_the-earth-system.pdf#page=13\|Kump et al. Ch. 1]] | extra/book |
> | thermometer time constant; radiation-error estimate | derived here | extra/beyond |
> | Rayleigh-distillation model; Majoube fractionation; Dansgaard slope | derived here; Majoube (1970, 1971); Dansgaard (1964) | extra/beyond |
> | cos φ weights; sampling theory $N_{\rm eff}$ | derived here | extra/beyond |
> | GISTEMP analysis (trends, SE, anomalies); CO₂ forcing | NASA GISS GISTEMP v4 (fetched 2026-10-23); Myhre et al. 1998 | extra/beyond |
>
> **Cross-checks and discrepancies:** the AI notes `argha-climate.pdf` and `climate_intro_notes_L1_L6.pdf` agree with the slides on L2. Slide 22's plots are credited to Gemini and look coarse and schematic; the real records (EPICA Dome C, Jouzel et al. 2007; LR04, Lisiecki & Raymo 2005) differ in detail. Slides 25 and 26 show the same area-weighting formula (the second slide's heading adds the anthropogenic-warming question); merged here.
> **Dropped as redundant:** slides 19 and 20 repeat the same bullets (different figures); slides 21 and 23 repeat the δ¹⁸O definition.

**References.** Hansen, J. & Lebedeff, S. (1987) *J. Geophys. Res.* 92, 13345 · Dansgaard, W. (1964) *Tellus* 16, 436 · Majoube, M. (1970, 1971) *Nature* 226, 1242; *J. Chim. Phys.* 68, 1423 · Myhre, G. et al. (1998) *Geophys. Res. Lett.* 25, 2715 · Jouzel, J. et al. (2007) *Science* 317, 793 · Lisiecki, L. E. & Raymo, M. E. (2005) *Paleoceanography* 20, PA1003 · Perengiyil, A. et al. (2025) *(IMD protocol, slide 18)* · NASA GISS GISTEMP v4 (Lenssen et al. 2019), data.giss.nasa.gov/gistemp · Kump, Kasting & Crane, *The Earth System*, Ch. 1.
