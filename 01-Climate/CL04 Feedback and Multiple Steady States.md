---
title: CL04 Feedback and Multiple Steady States
aliases: [CL04, Climate sensitivity and feedback, Ice-albedo feedback chapter]
subject: climate
type: chapter
chapter: 4
part: I
scope: [taught, extra-book, extra-beyond]
by: [argha]
status: draft
prereq: ["[[CL03 Radiation and Planetary Energy Balance]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/argha, status/draft]
---
# CL04 · Feedback and Multiple Steady States

◀ [[CL03 Radiation and Planetary Energy Balance]] · [[Climate - Course Map|Course Map]] · [[CL05 Thermodynamic State of the Atmosphere]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**
> - §1 sensitivity of $T_e$ to $S$ and $\alpha$ (Argha L4 sl. 41–42)
> - §2 forcing, $\Lambda_P$, chain rule, $\Lambda=\Lambda_P/(1-\sum f_i)$ (sl. 43–44)
> - §3 temperature-dependent albedo, steady states, stability (sl. 45–47)
> - §4 Snowball Earth (sl. 48)
>
> 🟡 **Extra · book**
> - Wallace & Hobbs §10.3 beyond the slides: LGM example, transient vs equilibrium response, water-vapour feedback (in §2)
> - Daisyworld (in §3)
> - Snowball in *The Earth System* Ch. 12 (in §4)
>
> 🔵 **Extra · beyond**
> - what $\varepsilon=0.6$ means and why it matters (§3)
> - relaxation times and the potential ("ball in a valley") picture (§3)
> - hysteresis diagram and fold values (§3)
> - critical slowing down (§3)
> - Budyko–Sellers history (§3)
> - escape CO₂ (§4)

> [!key] After this chapter you can
> - compute how $T_e$ responds to a change in $S$, $\alpha$ or an added forcing $F$, and quote the **Planck sensitivity** $\Lambda_P=1/4\sigma T^3$,
> - derive $\Lambda=\Lambda_P/(1-\sum f_i)$ with the chain rule and say what $f\ge1$ means,
> - find steady states of $S(1-\alpha(T))/4=\varepsilon\sigma T^4$ graphically, **classify their stability**, and explain hysteresis and tipping,
> - tell the Snowball Earth story: evidence, trigger, escape.

## 1. How sensitive is the steady state?
<span class="scope-taught">taught</span> *Argha L4, slides 41–42*

Start from the no-atmosphere balance of [[CL03 Radiation and Planetary Energy Balance]],
$$\frac{S(1-\alpha)}{4}=\sigma T^{4}.$$
Take logarithms and differentiate (slide 41, "Derive"): $\ln S+\ln(1-\alpha)-\ln4=\ln\sigma+4\ln T$, so

$$\boxed{4\,\frac{\Delta T}{T}=\frac{\Delta S}{S}-\frac{\Delta\alpha}{1-\alpha}}\tag{CL4.1}$$

> [!intuition] Why the factor $\tfrac14$? Temperature is a "gear-down"
> Because emission goes as the *fourth power* of $T$, a small change in temperature changes the outgoing flux four times as fast, in fractional terms. Turn it round: to rebalance a 1 % change in absorbed sunlight the planet only has to change its temperature by **0.25 %** (≈ 0.64 K). The same planet is a stiff, well-damped thermostat. (Logarithmic differentiation of a power law $y\propto x^{p}$ always gives $\Delta y/y=p\,\Delta x/x$: see [[Linearisation and Sensitivity]].)

Fractional changes in $S$ and in $(1-\alpha)$ are equivalent. Numbers from the slides [[climate_intro_L1_L6.pdf#page=41|(slides 41–42)]], $T=255$ K:

| change | effect | $\Delta T$ |
|---|---|---|
| $\Delta\alpha\approx+0.07$ (0.30 → 0.37) | $\Delta\alpha/(1-\alpha)=0.10$ | **−6 K** |
| $\Delta S=-136$ W m⁻² (−10 %) | $\Delta S/S=0.10$ | **−6 K** |
| sunspot cycle $\Delta S\sim1$ W m⁻² | $T/4\cdot\Delta S/S$ | ≈ 0.05 K, negligible |
| warming of +1.5 K | needs $\Delta S\approx32$ W m⁻², i.e. absorbed $\Delta S(1-\alpha)/4\approx6$ W m⁻² | — |

The last row is the useful one: it compares with the **observed radiative forcing since 1750, ~3 W m⁻²** (Forster et al. 2023, slide 41; IPCC AR6 SPM, slide 42). The observed warming is ≈ 1.1–1.2 K, i.e. ≈ 0.4 K per W m⁻² (my arithmetic, and a transient rather than equilibrium value), **more than the 0.27 K per W m⁻² this model gives**. The model therefore *underestimates* the sensitivity — the missing piece is feedback.

> [!example] Worked example: the cost of a cloudier planet
> If a small increase in low cloud raised Earth's albedo from 0.30 to 0.31, (CL4.1) gives $\Delta T=-\tfrac{255}{4}\cdot\tfrac{0.01}{0.70}=-0.9$ K, equivalent to a sudden loss of $\Delta S(1-\alpha)/4=\tfrac{1361\times0.01}{4}=3.4$ W m⁻² of absorbed sunlight. That is roughly the size of the whole anthropogenic forcing since 1750 with the opposite sign. A one-percent change in albedo is climatically large.

## 2. Forcing, the Planck response, and feedback factors
<span class="scope-taught">taught</span> *Argha L4, slides 43–44; Wallace & Hobbs Eqs. 10.5–10.10 (cited on slide 44)*

Define a **radiative forcing** $F$ [W m⁻²] as an extra net energy input at fixed temperature. The balance becomes

$$\frac{S(1-\alpha)}{4}+F=\sigma T^{4}.$$

**No feedbacks** ($S,\alpha$ constant). Differentiate with respect to $F$: $1=4\sigma T^{3}\,\mathrm dT/\mathrm dF$, so

$$\boxed{\Lambda_P\equiv\frac{\partial T}{\partial F}=\frac{1}{4\sigma T^{3}}}\ \approx0.27\ \mathrm{K\,(W\,m^{-2})^{-1}}\quad(T=255\ \text{K}),$$

i.e. about **3.76 W m⁻² per kelvin** ([[climate_intro_L1_L6.pdf#page=43|slide 43]]). Physically the planet "pays" $4\sigma T^3$ more emission per degree, and this restoring term is why the steady state is stable ([[Planck Sensitivity]]).

> [!verify] 0.28 or 0.27?
> Slide 43 writes $\Lambda_P=0.28$ K (W m⁻²)⁻¹ together with "1 K needs 3.8 W m⁻²". The two are inconsistent by 4 %: $1/(4\sigma(255)^3)=0.2659$ and $4\sigma(255)^3=3.76$. Wallace & Hobbs Exercise 10.3 (the source the slides cite) gets 0.266 K (W m⁻²)⁻¹ and 3.76 W m⁻² per K ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=462|p.445]]). **This vault uses 0.27.** For the real surface ($T_s=288$ K) the same formula gives only 0.18.

**With feedbacks.** Let auxiliary variables $y_i$ (albedo, water vapour, clouds, …) depend on temperature, $y_i=y_i(T)$. The total sensitivity by the chain rule [[climate_intro_L1_L6.pdf#page=44|(slide 44)]]:

$$\Lambda\equiv\frac{\mathrm dT}{\mathrm dF}=\frac{\partial T}{\partial F}+\sum_i\frac{\partial T}{\partial y_i}\frac{\mathrm dy_i}{\mathrm dF}
=\Lambda_P+\sum_i\underbrace{\frac{\partial T}{\partial y_i}\frac{\mathrm dy_i}{\mathrm dT}}_{f_i}\,\Lambda .$$

(using $\mathrm dy_i/\mathrm dF=(\mathrm dy_i/\mathrm dT)(\mathrm dT/\mathrm dF)$). Solving for $\Lambda$:

$$\boxed{\Lambda=\frac{\Lambda_P}{1-\sum_if_i}},\qquad f_i\equiv\frac{\partial T}{\partial y_i}\frac{\mathrm dy_i}{\mathrm dT}\tag{CL4.2}$$

- $f_i>0$: **positive feedback** (amplifies), $f_i<0$: negative (damps). The $f_i$ add.
- $f\to1$: $\Lambda\to\infty$; $f\ge1$: the linear response blows up — there is no nearby stable state, the system *moves to a different one* (slide 44: "What if $f_i$ is large, 1 or more?").

> [!intuition] Feedback is an echo, or a microphone near its loudspeaker
> You warm the planet by $\Delta T_0=\Lambda_PF$. That warming changes the ice, humidity or clouds, which warms it again by a fraction $f$ of the original kick; that second warming triggers a third of size $f^2$, and so on:
> $$\Delta T=\Delta T_0\,(1+f+f^2+f^3+\cdots)=\frac{\Delta T_0}{1-f}\qquad(|f|<1).$$
> Each pass round the loop is an echo that is weaker if $f<1$. If $f\ge1$ each echo is as loud as or louder than the last: the series diverges. That is the **howl** of a microphone placed too near its loudspeaker: the loop gain exceeds 1 and the amplifier saturates, i.e. moves to a quite different state. A negative $f$ is the opposite: the echo comes back with a flipped sign and *cancels* part of the original (the thermostat).

![[fig_cl04_feedback_gain.png|760]]
*Figure CL4.1. Left: gain $\Lambda/\Lambda_P=1/(1-f)$. See: it is nearly linear near $f=0$, doubles at $f=0.5$, diverges at $f\to1$. Right: the Planck sensitivity falls as $T^{-3}$, so cold planets are touchier than warm ones.*

**Albedo feedback with constant slope.** Let $\mathrm d\alpha/\mathrm dT=-a$ ($a>0$: warmer → less ice → lower albedo). Then $\partial T/\partial\alpha=-S/(16\sigma T^3)=-\tfrac S4\Lambda_P$ (from (CL4.1)), so

$$f_\alpha=\frac{\partial T}{\partial\alpha}\frac{\mathrm d\alpha}{\mathrm dT}=\frac{aS}{16\sigma T^{3}}=a\,\frac S4\,\Lambda_P,\qquad\Lambda=\frac{\Lambda_P}{1-\dfrac{aS}{16\sigma T^{3}}}.$$

Less than 3.8 W m⁻² then suffices for a 1 K rise, which is the slide's conclusion.

![[Ice-Albedo Feedback Loop.svg|620]]
*Figure CL4.2. The ice–albedo feedback ($f_\alpha>0$) and the Planck response (stabilising) that it fights. See: the four "+" links make a loop that reinforces itself. Editable version: [[Ice-Albedo Feedback Loop.excalidraw]].*

> [!example] Worked example: total sensitivity with realistic feedback factors
> Take $f_{\rm water\ vapour}=0.5$, $f_{\rm albedo}=0.1$, $f_{\rm cloud}=0.1$, $f_{\rm lapse\ rate}=-0.2$ (illustrative values of the right size; see [[Climate Feedback Factor]]). Then $f=0.5$, so $\Lambda=2\Lambda_P$. With $\Lambda_P=0.27$ (airless) $\Lambda=0.54$ K/(W m⁻²); a CO₂ doubling ($F=3.7$ W m⁻²) gives 2.0 K. Using the greenhouse-corrected Planck value $\Lambda_P=0.30$ (see the box on $\varepsilon=0.6$ below) gives $2\times0.30\times3.7=2.2$ K. Both are in the right range (the IPCC likely range is 2.5–4 K): the sum of feedbacks is what separates models.

> [!extra-book]+ 🟡 Extra (book): what Wallace & Hobbs §10.3 adds beyond the slides
> The slides take Eqs. 10.5–10.10 (chain rule, $f_i$, gain $1/(1-f)$) from this section. The book continues with material that was **not** shown:
> - **Example 10.4, apparent sensitivity at the Last Glacial Maximum:** $\Delta T_s=5$ K colder, forcing $=3.7+3.4$ W m⁻² (CO₂ at 180 ppmv plus extra ice albedo), so $\Delta T/\Delta F=0.70$ K (W m⁻²)⁻¹, i.e. feedbacks amplify the Planck response by $0.70/0.266=2.7$ ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=463|p.446]]).
> - **§10.3.1 Transient vs equilibrium response.** For a slab of heat capacity $c$: $c\,\mathrm dT/\mathrm dt=-T/\Lambda+Q$, giving $T=\Lambda Q\,(1-e^{-t/\tau})$ with $\tau=c\Lambda$. Positive feedback raises $\Lambda$ and **lengthens the response time**. Check with CL03: $\tau=c\Lambda_P=2\times10^8/3.76=1.7$ yr for a 50 m mixed layer; the whole ocean is ~50× larger (centuries). So the climate observed at any time lags its equilibrium ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=463|pp.446–447]]).
> - **§10.3.2 Feedbacks.** Water vapour: saturation vapour pressure rises ≈7 % K⁻¹ (Clausius–Clapeyron); at constant relative humidity $f\approx0.5$, a gain of 2. Clouds can be positive or negative depending on height and thickness. ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=464|p.447]]). These return in [[CL08 Greenhouse Models]] and [[CL09 Radiative-Convective Equilibrium]].
> - **Definition of $F$** uses the tropopause after the stratosphere has adjusted (footnote 19, p.444).

## 3. Multiple steady states
<span class="scope-taught">taught</span> *Argha L4, slides 45–47* · <span class="scope-extra-beyond">extra · beyond</span> *potential picture, hysteresis, slowing down: derived here*

Suppose $\alpha$ itself depends on $T$ ([[climate_intro_L1_L6.pdf#page=45|slide 45]]). Motivation: when the planet is cold, snow and ice cover a lot of it and $\alpha$ is large (0.7); when it is warm, it is ice-free (ocean, land, cloud: 0.2); in between the ice line retreats gradually. A piece-wise linear model:

$$\alpha(T)=\begin{cases}0.7&T<253\ \mathrm K\\[2pt]0.7-\dfrac{0.5\,(T-253)}{40}&253\le T\le293\ \mathrm K\\[4pt]0.2&T>293\ \mathrm K\end{cases}$$

Steady states are the crossings of **absorbed solar** $S(1-\alpha(T))/4$ and **emitted** $\varepsilon\sigma T^4$.

> [!intuition] Why a *ramp*, and why does it make two climates possible?
> Cold planet: white ⇒ reflects ⇒ stays cold. Warm planet: dark ⇒ absorbs ⇒ stays warm. Both are self-confirming. In the middle the ice edge moves: every kelvin of warming removes a strip of ice, raising absorbed sunlight faster than emission rises: *positive* feedback stronger than the Planck damping. Positive feedback in the middle + damping at the ends = two stable states with an unstable divider, exactly a light switch with a spring: it rests firmly "on" or "off", and the halfway position is where you can only balance for an instant.

> [!pitfall] The slide's formula omits a factor 0.6
> Slides 45–47 state the steady-state condition as $S(1-\alpha)/4=\sigma T^4$, but the Mathematica code printed on slide 45 plots `.6 σ T^4`, i.e. an **effective emissivity $\varepsilon=0.6$**, and the plot on slide 47 (circles at ≈235, 274 and 299 K) uses it. With $\varepsilon=1$ and the albedo above, $S(1-\alpha)/4\le272$ W m⁻² can never reach $\sigma T^4$ for $T>260$ K and **only the snowball state exists** (206 K). So a greenhouse effect is *required* for the ice-free state. This vault uses $\varepsilon=0.6$ (script `fig_cl04_steady_states.py` prints both cases).

> [!extra-beyond]+ 🔵 Extra (beyond): what $\varepsilon=0.6$ means, and why it is the *right* number
> $\varepsilon$ is the fraction of the surface's blackbody emission that actually reaches space (the rest is absorbed by the atmosphere and re-emitted from colder levels). Balance with $\varepsilon$: $\tfrac S4(1-\alpha)=\varepsilon\sigma T_s^4$, so $T_s=T_e\,\varepsilon^{-1/4}$. At today's albedo $T_e=254.6$ K and $\varepsilon=0.6$ give $T_s=289$ K, close to the real 288 K. So $\varepsilon=0.6$ is not arbitrary: it is the value that reproduces the observed greenhouse effect (a one-layer atmosphere absorbing 80 % of surface emission has $\varepsilon=1-0.8/2=0.6$, [[CL08 Greenhouse Models]]).
> It also repairs the sensitivity: $\Lambda_P=1/(4\varepsilon\sigma T^3)$ at 289 K is **0.30 K per W m⁻²** (3.3 W m⁻² per K), matching the value ≈ 3.2 W m⁻² K⁻¹ for the Planck feedback in full climate models (`[verify]` against IPCC AR6 Ch. 7), whereas the bare $\varepsilon=1$ airless planet gave 0.27 and 0.18 at 288 K.

![[fig_cl04_steady_states.png|620]]
*Figure CL4.3. Top: absorbed vs emitted flux with the three crossings. Bottom: net heating $N(T)=\text{absorbed}-\text{emitted}\propto\mathrm dT/\mathrm dt$; arrows show which way the temperature drifts. See: each stable crossing (filled) has arrows pointing **towards** it, the unstable one (open) has arrows pointing **away**.*

| steady state | $T^*$ (K) | $\alpha$ | slope $\mathrm dN/\mathrm dT$ (W m⁻² K⁻¹) | verdict |
|---|---|---|---|---|
| snowball | 234 | 0.70 | −1.74 | **stable** |
| middle | 274 | 0.43 | **+1.45** | **unstable** |
| ice-free | 299 | 0.20 | −3.64 | **stable** |

### Stability of a steady state
Write $T=T^*+\theta$ and linearise $C\,\dot T=N(T)$: $C\dot\theta=N'(T^*)\,\theta$, so $\theta\propto e^{N'(T^*)t/C}$. The steady state is **stable iff $N'(T^*)<0$**: warmer than $T^*$ ⇒ net loss ⇒ cools back. Graphically, a stable crossing is where emitted crosses absorbed *from below* (emission rises faster). This is the general test of [[Fixed Points and Linear Stability]].

> [!intuition] The ball in the valley
> Write the dynamics as $C\dot T=N(T)=-\mathrm dU/\mathrm dT$. Then the temperature is a **ball rolling downhill on a landscape $U(T)$ with strong friction**. Stable steady states are **valley bottoms**; the unstable one is the **hilltop** between two valleys; $N'<0$ means the valley is curved up (a restoring slope), $N'>0$ means a hill (a nudge grows). Which valley you end up in depends on which side of the hill you start. As the Sun dims, the landscape tilts and the warm valley becomes shallower and then disappears (next figure).

![[fig_cl04_potential.png|760]]
*Figure CL4.4. The potential $U(T)=-\int N\,\mathrm dT$ at three values of the solar constant (script `fig_cl04_potential.py`). See: with today's Sun there are two valleys separated by a hill; at 94 % the warm valley is a shallow dimple; at 90 % it has been filled in and the ball can only roll into the snowball valley.*

In feedback language $N'=\,\mathrm{d(ASR)}/\mathrm dT-\mathrm{d(OLR)}/\mathrm dT$, so with $f=\mathrm{d(ASR)}/\mathrm dT\big/\mathrm{d(OLR)}/\mathrm dT$ the condition $N'<0$ is exactly $f<1$ of (CL4.2). At 274 K: $\mathrm d(\mathrm{ASR})/\mathrm dT=\tfrac S4\cdot0.0125=4.25$ W m⁻² K⁻¹ and $\mathrm d(\mathrm{OLR})/\mathrm dT=4\cdot0.6\,\sigma T^3=2.81$, so $f_\alpha=1.51>1$: **the ice-albedo feedback wins in the transition zone**, the middle state is a watershed between two basins of attraction.

> [!example] Worked example: locating the unstable state by Newton's method
> On the ramp, $N(T)=\tfrac S4\,[0.3+0.0125(T-253)]-0.6\sigma T^4$ and $N'(T)=4.253-2.4\sigma T^3$. Start from $T=270$ K:
> | iteration | $T$ (K) | $N$ (W m⁻²) | $N'$ |
> |---|---|---|---|
> | 0 | 270.00 | −6.43 | 1.574 |
> | 1 | 274.08 | −0.25 | 1.451 |
> | 2 | 274.26 | 0.00 | 1.446 |
>
> Converged: $T^*=274.26$ K, $\alpha=0.7-0.5\times21.26/40=0.434$ and $N'=+1.45>0$: unstable ✓. Check: ASR $=340.25\times0.566=192.6$ W m⁻²; OLR $=0.6\sigma(274.26)^4=192.6$ ✓.

> [!example] How long does it take?
> With a 50 m ocean layer ($C=2\times10^8$ J m⁻² K⁻¹) the e-folding times $C/|N'|$ are 3.6 yr (snowball), 1.7 yr (ice-free) and an *escape* time of 4.4 yr from the unstable state. A nudge of a few tenths of a kelvin around 274 K sends the planet to either basin within decades.

### Hysteresis and tipping points
Now let the Sun vary. For each $S$ solve for the steady states: the stable and unstable branches form an S-shaped curve.

![[fig_cl04_hysteresis.png|640]]
*Figure CL4.5. Equilibrium temperature against solar constant (script `fig_cl04_hysteresis.py`). See: start on the upper (ice-free) branch and lower $S$ to the left end of that branch at $S=1254$ W m⁻² (92 % of today): there the warm state ends and the planet must drop to the lower branch. To climb back one must go right to the end of the snowball branch at $S=1858$ W m⁻² (136 %), a far larger step. The two end-points are the **tipping points**; they sit at the kinks of the piecewise-linear $\alpha$.*

> [!intuition] Hysteresis: the way back is not the way there
> Tip a canoe: it takes a small lean to go over the edge, but a *huge* effort to right it again, because the stable positions are on either side of a barrier and the barrier is not symmetric. The system "remembers" which side it is on: the same sunlight (the same lean) corresponds to *either* state depending on history.

Implications (the slide's "Implication?"): (i) the same external conditions can support two different climates; (ii) a gradual change can trigger an **abrupt** and **hard-to-reverse** transition; (iii) once frozen, restoring the old climate needs much more than reversing the cause. The same S-shaped structure appears in [[Bistability and Tipping Points]], connecting this chapter to lake eutrophication and other regime shifts in [[Ecology and Evolution - Course Map]].

> [!extra-beyond]- 🔵 Extra (beyond): early warning: critical slowing down
> At a smooth fold the slope $N'$ of the disappearing state tends to 0, so the relaxation time $C/|N'|\to\infty$: the system recovers from small kicks ever more slowly just before it tips, a measurable early-warning signal (rising variance and autocorrelation). In the piecewise-linear toy this *does not happen* (the state vanishes at a kink with $N'$ still $-3.4$, so $\tau$ stays ~1.8 yr). With a smooth albedo $\alpha(T)=0.45-0.25\tanh[(T-273)/12]$ and $\varepsilon=0.6$ (three steady states at $S_0$: 234, 273, 298 K) the warm-state relaxation time rises as the Sun dims:
> | $S/S_0$ | 1.00 | 0.95 | 0.92 | 0.90 | 0.89 |
> |---|---|---|---|---|---|
> | $\tau_{\rm warm}$ (yr, $C=2\times10^8$) | 2.0 | 2.4 | 3.1 | 4.8 | 25.8 |
>
> (the warm state disappears just below 0.89). See [[Bistability and Tipping Points]] and [[Relaxation Time]].

> [!extra-beyond]- 🔵 Extra (beyond): the real history of this idea
> Budyko (1969) and Sellers (1969) built latitude-dependent energy-balance models with an ice line and found that a ~2 % decrease in the solar constant could drive the model to a completely ice-covered state; North (1975) analysed the stability of these models analytically (the "small ice cap instability"). The zero-dimensional toy of the slides cannot represent the ice line, but it captures the topology: a fold bifurcation pair. Beyond the slides, notice the asymmetry in Fig. CL4.5: leaving the snowball needs a much larger perturbation than entering it, which is why a CO₂ build-up (a greenhouse forcing, shifting $\varepsilon$), not the Sun, ends the glaciation in §4.

> [!extra-book]- 🟡 Extra (book): Daisyworld, a biological albedo feedback
> *The Earth System* (Kump, Kasting & Crane) Chapter 2 introduces **Daisyworld**, a planet with black and white daisies whose growth depends on temperature and whose albedo changes the temperature: a feedback loop between a population and a planet ([[vdoc.pub_the-earth-system.pdf#page=34|PDF p.34 ff.]]). It is the cleanest link between this chapter and the population models of [[Ecology and Evolution - Course Map]].

## 4. Snowball Earth
<span class="scope-taught">taught</span> *Argha L4, slide 48*

[[climate_intro_L1_L6.pdf#page=48|Slide 48]] applies the bistable picture to the **Cryogenian Period** (~720–635 Ma, two events). See [[Snowball Earth]].

| | what the slide gives |
|---|---|
| **Evidence** | glacial sediments distributed globally, even at paleolatitudes $<15^\circ$; thick **cap carbonates** above the glacial deposits; a drop in $\delta^{13}$C reflecting a global crash in primary productivity |
| **Triggers** (lowering of CO₂ ⇒ the system crosses the cold fold) | break-up of a supercontinent; emplacement of a large igneous province |
| **Escape** | with the surface ice-covered, *silicate weathering* (the CO₂ sink) shuts off while *volcanism continues*, so CO₂ accumulates until the greenhouse effect overtakes the albedo effect |

The slide links the review by Hoffman et al. (2017, *Science Advances* 3, e1600983), "Snowball Earth climate dynamics and Cryogenian geology–geobiology".

> [!intuition] A planet-sized mirror and a slow trickle
> Once the planet is a white mirror it throws 60–70 % of the sunlight back, so no amount of ordinary warming will thaw it. But volcanoes keep breathing CO₂ and nothing (no rock weathering under ice, no rain) removes it. The CO₂ builds up for millions of years, like water filling behind a dam, until the greenhouse effect is strong enough to melt the ice at the equator; then the albedo feedback runs in reverse, *fast*, and the planet snaps to the hot state (the cap carbonates are the aftermath of an extremely hot, CO₂-rich, acid-rain world).

> [!extra-beyond]- 🔵 Extra (beyond): order-of-magnitude of the escape greenhouse
> Because $\alpha\approx0.6$–0.7 when frozen, absorbed sunlight is only $\sim100$ W m⁻², and the surface must warm to $\sim273$ K before ice melts; the CO₂ needed is of order **0.1 bar**, i.e. hundreds of times the present level (Pierrehumbert 2004; Hoffman & Schrag 2002) `[verify]` exact value. Accumulation at a volcanic outgassing rate of order $10^{12}$–$10^{13}$ mol yr⁻¹ takes millions of years (0.1 bar ≈ $1.2\times10^{19}$ mol; at $6\times10^{12}$ mol yr⁻¹ that is ~2 Myr), which fits the ~5–58 Myr durations of the Cryogenian glaciations quoted by Hoffman et al. 2017.
> The terminal "cap carbonates" are the signature of the post-glacial supergreenhouse: the huge CO₂ amount makes rain acidic, weathering is intense, and carbonate precipitates rapidly. (Link: [[Evolution of Earth and Life - Course Map]], where the carbonate–silicate cycle is the long-term thermostat.)

> [!extra-book]- 🟡 Extra (book): Earth System, Chapter 12
> The Snowball Earth sections of *The Earth System* are in Chapter 12, "Long-Term Climate Regulation" ([[vdoc.pub_the-earth-system.pdf#page=251|PDF pp.251–254]]); this is where the carbonate–silicate negative feedback is developed.

## 5. What we have, what is missing
<span class="scope-taught">taught</span> *synthesis*

1. A **zero-d model** with sensitivity $\Lambda_P=0.27$ K (W m⁻²)⁻¹ and the machinery $\Lambda=\Lambda_P/(1-f)$ to include any feedback whose strength we can estimate.
2. A nonlinear model with **bistability** and tipping.
3. Still unexplained: the 33 K greenhouse offset, the vertical structure that determines how a gas changes $\varepsilon$, and the physical origin of the water-vapour and lapse-rate feedbacks. Next, [[CL05 Thermodynamic State of the Atmosphere]] and [[CL06 Hydrostatic Balance and Vertical Structure]] set up the atmosphere itself, then radiation returns in [[CL07 Optical Properties of the Atmosphere]] and [[CL08 Greenhouse Models]].

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Ice–albedo feedback: multiple climates from one Sun
> Zero-dimensional energy balance: absorbed sunlight S(1 − α(T))/4 against emitted radiation εσT⁴, with the planetary albedo α rising when the surface freezes.
>
> ![[cl_ebm_albedo.png|720]]
>
> **Try:** Set S/S₀ = 1: warm climate near 290 K and a cold, ice-covered state near 247 K, separated by an unstable state. Reduce S/S₀ until the warm state vanishes (jump to snowball); raise it back: the return jump happens at a much higher S/S₀.
>
> [▶ Open the tool in your browser](../Assets/interactive/cl_ebm_albedo.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/cl_ebm_albedo.html) · all tools and coverage: [[Interactive Tools]]

> [!interactive]+ Interactive: A one-dimensional energy-balance model: heat transport and the ice line
> Each latitude band balances absorbed sunlight (with the annual-mean insolation Q(φ) = (S/4)[1 − 0.477 P₂(sin φ)]), outgoing infrared A + BT and the diffusive transport of heat D ∂²T/∂φ²: C ∂T/∂t = Q(φ)(1 − α(T)) − (A + BT) + D∇²T.
>
> ![[cl_ebm_latitude.png|720]]
>
> **Try:** At S/S₀ = 1 two steady states coexist: warm (global mean 16.6 °C, equator 26 °C, pole −2 °C, ice-free) and frozen (−35.5 °C). From the warm state lower S/S₀: the ice cap appears near 0.92 and by 0.90 the planet is frozen (−41.6 °C). From frozen you must raise S/S₀ above about 1.24–1.26 to melt it: hysteresis. Diffusion D = 0, 0.3, 0.65, 1.5 gives an equator–pole contrast of 109, 62, 28.5, 15.3 K.
>
> [▶ Open the tool in your browser](../Assets/interactive/cl_ebm_latitude.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/cl_ebm_latitude.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How CL04 connects
> **Builds on:** [[CL03 Radiation and Planetary Energy Balance]]
> **Leads to:** [[CL05 Thermodynamic State of the Atmosphere]] → [[CL08 Greenhouse Models]] (what $\varepsilon$ is) · [[CL09 Radiative-Convective Equilibrium]] (lapse-rate and water-vapour feedbacks) · [[CL10 Global Energy Balance and Meridional Structure]] (ice line and latitude)
> **Concepts:** [[Planck Sensitivity]] · [[Climate Feedback Factor]] · [[Ice-Albedo Feedback]] · [[Albedo]] · [[Snowball Earth]] · [[Zero-Dimensional Energy Balance Model]] · [[Relaxation Time]] · [[Fixed Points and Linear Stability]] · [[Linearisation and Sensitivity]] · [[Bistability and Tipping Points]]
> **Other subjects:** [[Ecology and Evolution - Course Map]] (regime shifts, Daisyworld) · [[Evolution of Earth and Life - Course Map]] (Cryogenian, carbonate–silicate cycle) · [[Landscapes and Geomorphology - Course Map]] (weathering) · [[Thermodynamics and Statistical Mechanics - Course Map]] (Clausius–Clapeyron)

> [!connection] Dynamical systems and ecology
> A steady state with $N'<0$ is a **stable fixed point**; $N'>0$ an unstable one; two stable points separated by an unstable one is **bistability**. The mathematics is [[Fixed Points and Linear Stability]]; the same S-shaped curve describes clear vs turbid shallow lakes and the Allee effect ([[Bistability and Tipping Points]]).

> [!connection] Measuring sensitivity: calculus
> (CL4.1) is *logarithmic differentiation*, and $\Lambda$ is a total derivative evaluated with the chain rule: [[Linearisation and Sensitivity]].

> [!connection] Geology
> Snowball Earth, cap carbonates, silicate weathering: [[Evolution of Earth and Life - Course Map]], and the landscape side (weathering rates, supercontinent breakup) in [[Landscapes and Geomorphology - Course Map]].

## Summary
> [!summary] Cheat-sheet
> - $4\,\Delta T/T=\Delta S/S-\Delta\alpha/(1-\alpha)$: 1 % in sunlight ⇒ 0.25 % in $T$ (0.64 K); $\Delta\alpha=0.01\Rightarrow-0.9$ K.
> - Forcing $F$; $\Lambda_P=1/4\sigma T^3=0.27$ K/(W m⁻²) (3.76 W m⁻² per K); 0.18 at 288 K; 0.30 with $\varepsilon=0.6$.
> - $f_i=\dfrac{\partial T}{\partial y_i}\dfrac{\mathrm dy_i}{\mathrm dT}$, additive; $\boxed{\Lambda=\Lambda_P/(1-\sum f_i)}$; $f\ge1$ ⇒ runaway. $f_\alpha=aS/(16\sigma T^3)$.
> - Ramp albedo (0.7 / ramp / 0.2) + emissivity 0.6 ⇒ **three** steady states 234 K (stable), 274 K (unstable), 299 K (stable). With $\varepsilon=1$ only the snowball state.
> - Stable ⇔ $N'(T^*)<0$ ⇔ $f<1$; ball-in-valley picture; hysteresis: warm state lost at $S\approx0.92S_0$, snowball lost only at $\approx1.36S_0$.
> - Snowball (Cryogenian ~720–635 Ma): low-latitude glacials, cap carbonates, $\delta^{13}$C drop; escape by CO₂ accumulation while weathering is off.

## Practice
1. Show (CL4.1) from $S(1-\alpha)/4=\sigma T^4$. What albedo change cools Earth by 1 K?
2. Compute $\Lambda_P$ at 255 K and at 288 K. Which is more sensitive, and why does a colder planet respond more strongly to the same forcing?
3. If the feedbacks have $f_{\text{water vapour}}=0.8$, $f_{\text{albedo}}=0.2$ and $f_{\text{cloud}}=0.1$, find $\Lambda$ and the warming for a doubling of CO₂ ($F=3.7$ W m⁻²).
4. For the ramp albedo with $\varepsilon=0.6$, show that **every** steady state on the ramp is unstable. Check the value $+1.45$ in the table.
5. With $\varepsilon=1$ find the single steady state analytically. What value of $\varepsilon$ is needed for the ice-free state to exist at $S_0$?
6. **Conceptual.** Explain why the Planck feedback is called a *negative* feedback even though it is not in the sum $\sum f_i$ of (CL4.2).
7. In the ramp model, find the solar constant at which the ice-free state disappears, using the corner $T=293$ K.
8. Show that the echo series $1+f+f^2+\dots$ gives $\Lambda_P/(1-f)$, and use it to explain why $f=0.9$ gives a 10-fold amplification with a very long equilibration time.

> [!example]- Solutions
> 1. $\ln S+\ln(1-\alpha)=\ln4\sigma+4\ln T$ ⇒ $\Delta S/S-\Delta\alpha/(1-\alpha)=4\Delta T/T$. For $\Delta T=-1$ K: $\Delta\alpha=4(1-\alpha)(1\ \mathrm K/T)=4\times0.7/255=+0.011$.
> 2. $\Lambda_P(255)=0.266$, $\Lambda_P(288)=0.185$ K/(W m⁻²). The colder planet radiates less per kelvin ($\propto T^3$) so it needs a bigger temperature rise to dump the same extra watt.
> 3. $f=1.1\ge1$! The sum exceeds 1: **runaway** in the linear model, no finite $\Lambda$. (With $f_{\rm WV}=0.5$ instead, $f=0.8$, $\Lambda=0.266/0.2=1.33$, $\Delta T=4.9$ K.) The point: feedbacks near 1 make the result hypersensitive.
> 4. On the ramp $N'=\tfrac S4(0.0125)-4\varepsilon\sigma T^3=4.25-2.4\sigma T^3$, positive until $T^3=4.25/(2.4\sigma)$, i.e. $T<315$ K. The ramp is 253–293 K, so $N'>0$ throughout: any steady state there is unstable. At 274.3 K: $4.253-2.4\times5.67\times10^{-8}\times274.3^3=1.45$ ✓.
> 5. $340.25\times0.3=102.1=\sigma T^4$ ⇒ $T=206$ K. Warm state at the corner: $\tfrac S4\times0.8=\varepsilon\sigma(293)^4$ ⇒ $272.2=\varepsilon\times417.9$ ⇒ $\varepsilon\le0.65$.
> 6. $\Lambda_P$ is the response with *all* other variables frozen, the baseline. Its sign is already built in: a warmer planet emits more, opposing the warming. We call the *additional* terms $f_i$ "feedbacks"; in IPCC bookkeeping the Planck term is counted as the negative feedback $\lambda_P\approx-3.2$ W m⁻² K⁻¹.
> 7. At $T=293$: $\tfrac S4\times0.8=0.6\sigma(293)^4$ ⇒ $S=4\times250.8/0.8=1254$ W m⁻² (92 % of 1361) ✓ equals the fold of Fig. CL4.5.
> 8. Geometric series for $|f|<1$: $1/(1-f)$. For $f=0.9$ the gain is 10 and the series converges slowly (each echo is 0.9 of the last), which is why the climate takes ~10× longer ($\tau=C\Lambda$) to settle.

## PDF handout
Second page of the shared CL03–CL04 handout (sensitivity, feedback, steady-state figure and table, checks): [[climate-part1-energy-balance-handout.pdf#page=2|open at page 2]].

![[climate-part1-energy-balance-handout.pdf#page=2&height=460]]

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (12): the other tool's concept notes from the lectures, unreviewed
> [[zettel/cap-carbonates|Cap Carbonates]] · [[zettel/cryogenian-geological-glaciation-proxies|Cryogenian Geological Glaciation Proxies]] · [[zettel/ice-albedo-feedback|Ice-Albedo Feedback]] · [[zettel/infrared-flux-temperature-feedback|Infrared Flux-Temperature Feedback]] · [[zettel/multiple-climate-equilibria-in-energy-balance-models|Multiple Climate Equilibria in Energy Balance Models]] · [[zettel/parameter-sensitivity-via-logarithmic-differentiation|Parameter Sensitivity via Logarithmic Differentiation]] · [[zettel/piecewise-linear-albedo-model|Piecewise Linear Albedo Model]] · [[zettel/runaway-ice-albedo-instability|Runaway Ice-Albedo Instability]] · [[zettel/silicate-weathering-feedback|Silicate Weathering Feedback]] · [[zettel/snowball-earth|Snowball Earth]] · [[zettel/snowball-earth-deglaciation-via-volcanic-outgassing|Snowball Earth Deglaciation via Volcanic Outgassing]] · [[zettel/temperature-dependent-ice-albedo-feedback|Temperature-Dependent Ice-Albedo Feedback]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | sensitivity of $T_e$ to $S$ and $\alpha$ | [[climate_intro_L1_L6.pdf#page=41\|Argha L4 sl. 41–42]] | taught |
> | $\Lambda_P$, chain-rule feedback, $\Lambda=\Lambda_P/(1-\sum f_i)$ | [[climate_intro_L1_L6.pdf#page=43\|Argha L4 sl. 43–44]]; Wallace & Hobbs Eqs. 10.5–10.10 | taught |
> | multiple steady states, stability | [[climate_intro_L1_L6.pdf#page=45\|Argha L4 sl. 45–47]] | taught |
> | snowball Earth | [[climate_intro_L1_L6.pdf#page=48\|Argha L4 sl. 48]] | taught |
> | hysteresis diagram, potential picture, relaxation times, Newton solve, fold values | computed here | extra/beyond |
> | what $\varepsilon=0.6$ means; critical slowing down (smooth albedo) | computed here | extra/beyond |
> | LGM example, transient response, water-vapour feedback, forcing definition | Wallace & Hobbs §10.3 pp.444–447 | extra/book |
> | Daisyworld; Snowball in Ch. 12 | Kump et al. | extra/book |
> | Budyko/Sellers/North history; escape CO₂ | literature | extra/beyond |
>
> **Corrections to the slides:** $\Lambda_P=0.27$ not 0.28; the factor 0.6 (emissivity) in the steady-state plot is missing from the printed equation.

**References.** Budyko, M. I. (1969) *Tellus* 21, 611 · Sellers, W. D. (1969) *J. Appl. Meteorol.* 8, 392 · North, G. R. (1975) *J. Atmos. Sci.* 32, 2033 · Hoffman, P. F. & Schrag, D. P. (2002) *Terra Nova* 14, 129 · Pierrehumbert, R. T. (2004) *Nature* 429, 646 · Hoffman, P. F. et al. (2017) *Sci. Adv.* 3, e1600983 · Forster, P. et al. (2023) *Earth Syst. Sci. Data* 15, 2295 · Wallace & Hobbs (2006) §10.3.
