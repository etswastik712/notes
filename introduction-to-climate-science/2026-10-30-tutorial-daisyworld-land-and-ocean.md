---
id: introduction-to-climate-science/2026-10-30-tutorial-daisyworld-land-and-ocean
aliases: [Tutorial: Daisyworld, land and ocean]
tags: [introduction-to-climate-science, tutorial, feedback, albedo, daisyworld]
trust_tier: agent_written
---

# Tutorial: Daisyworld, land and ocean (30 October 2026)

## Covered
Source: the tutorial handout "Daisyworld, land and ocean: a guide to exploring the app" (EC2113, ocean module) (Classroom: handout PDF, posted 2026-10-30). Only the first part of the handout was read (Part 1 and Runs 1–5, up to the start of the hysteresis table in Run 5). Runs 6–10 (response time and heat storage) and Part 3 (take-aways, what the model leaves out) were not read; see "Files".

**Main message.** The ocean does two things to a planet: it makes it darker, and it makes it slower. Neither gives the planet control over its temperature: more ocean leaves the daisies less to work with, and the planet takes longer to respond to a change.

**The model (Lovelock and Watson, 1983).**
- One temperature for the whole planet (no map, no seasons). A sun of relative brightness $L$ ($L=1$ is the reference sun) brightens slowly. Steady state: $S\,L\,(1-A)=\sigma T^4$, with $S=917$ W m$^{-2}$ and $A$ the planetary albedo. The daisies' only lever on climate is $A$.
- Albedos: white daisies 0.75, bare ground 0.50, black daisies 0.25, ocean 0.10 (adjustable, fixed in time).
- Daisies live only on land, grow best at 22.5 °C, cannot grow below 5 °C or above 40 °C, and die at a fixed rate $\gamma=0.3$ per year.
- All land: $A=a_w\cdot0.75+a_b\cdot0.25+x\cdot0.5$, with $x=1-a_w-a_b$ the bare fraction. With land fraction $f$ and ocean $1-f$: $A=f\,(a_w\cdot0.75+a_b\cdot0.25+x\cdot0.5)+(1-f)\cdot0.1$.
- Patch temperatures (the trick that makes regulation work): $T_{\text{white}}=T+20\,(A-0.75)$ and $T_{\text{black}}=T+20\,(A-0.25)$; the 20 K is $q'$, which sets how little heat patches share. At $A=0.5$ a black patch is 5 °C warmer and a white patch 5 °C cooler than the planet.
- Growth: $\dfrac{da_i}{dt}=a_i\,[\,x\,\beta(T_i)-\gamma\,]$, $\beta(T)=1-0.003265\,(22.5-T)^2$ (zero below 5 °C and above 40 °C). Daisies cannot cover more than 70 % of the land, since at balance $x\beta=\gamma$ and $\beta\le1$ gives $x\ge0.3$.
- Heat store: land and air store little (response in weeks); the ocean mixed layer (50 m by default) stores about 20 times more (response in months); deeper settings stand in for deep-ocean mixing (years).
- A bare twin planet (same land, ocean and sun, no daisies) is the control experiment.

**Mechanism.** Under a dim sun the black patches are the ones warm enough to grow: black daisies spread, $A$ falls, $T$ rises, which helps more black daisies (a positive feedback, the jump at $L\approx0.75$). Under a bright sun the white patches are comfortable: white daisies spread, $A$ rises, the planet cools. Two opposing colours hold $T$ near 22.5 °C.

**Run 1 (all land, slow brightening, $L$ from 0.4 to 1.8 over 600 yr).**
- Bare planet within 5 °C of 22.5 °C only for $L=0.88$–$1.01$. Daisy planet jumps up at $L\approx0.75$ and stays within 5 °C for $L=0.76$–$1.52$, about six times wider; between $L=0.95$ and $1.33$ it even cools slightly (23.4 to 20.9 °C) while the bare planet warms from 22.9 to 48.8 °C.
- At $L\approx1.59$ white daisies collapse (runaway: warmer white patches beyond tolerance, albedo falls, planet warms, more die) and the planet jumps onto the bare-planet line. At the moment of most daisies ($L=1.47$): white cover 69 % of land, planet 24.3 °C, bare planet 56.8 °C.

**Run 2 (30 % and 70 % ocean).**
- Daisies survive: all land $L=0.75$–$1.59$; 30 % ocean $0.63$–$1.15$; 70 % ocean $0.52$–$0.89$.
- Daisy planet within 5 °C of 22.5 °C: $0.76$–$1.52$; $0.64$–$1.01$; $0.55$–$0.61$. Bare planet: $0.88$–$1.01$; $0.71$–$0.82$; $0.57$–$0.65$.
- The window moves to a dimmer sun (dark ocean warms the planet) and narrows. With 70 % ocean the daisy and bare curves nearly overlap: the daisies live on the planet but do not run it.
- Leverage: the albedo swing available to daisies is $0.5\,f$: 0.5 (all land), 0.35 (30 % ocean), 0.15 (70 % ocean).

**Run 3 (separating the two effects with ocean albedo 0.5).** The window no longer moves (starts at $L\approx0.75$ each time), so the shift came from the ocean being dark. It still narrows (daisies survive to 1.44 with 30 % ocean, 1.30 with 70 %; daisy planet within 5 °C: $0.77$–$1.32$ and $0.80$–$1.13$), so the narrowing is leverage alone.

**Run 4 (surviving is not regulating).** At the hot edge of the 70 % ocean run ($L=0.85$) the planet is at 44.8 °C (above the 40 °C limit) yet white daisies cover 47 % of the land: white patches sit at 34.9 °C because with $A\approx0.25$ they are $20\,(0.25-0.75)=-10$ °C below the planet. Land is only 30 % of the planet, so the daisies cannot cool the rest. Table of the hot edge: all land $L=1.55$, planet 30.4 °C, white patches 28.6 °C, $A=0.66$; 30 % ocean $L=1.10$, 35.8 °C, 30.6 °C, 0.49; 70 % ocean $L=0.85$, 44.8 °C, 34.9 °C, 0.25.

**Run 5 (brighten, then dim: hysteresis).** All land, 300 yr up and 300 yr down: daisies die on the way up at $L\approx1.63$ and return on the way down only at $L=1.17$; between them the same sun gives two different planets (hysteresis). The faster sweep gives slightly different numbers from Run 1, a first hint that the rate of change matters. (30 % and 70 % ocean die-off values: 1.18 and 0.91 on the way up; the return values were cut off in the text read.)

**Link to the course.** Daisyworld is a worked example of the albedo feedback and multiple steady states from Lectures 3–4; compare the $S(1-\alpha)/4=\sigma T^4$ balance and the hysteresis there. The ocean's heat storage connects to the land–ocean heat-capacity argument for monsoons (Webster and Fasullo).

## From the post
"Handout for today's tutorial: https://joymonteiro.github.io/intro_climate_science/tutorials/daisyworld-land-ocean/daisyworld_land_ocean_handout.pdf" (Classroom announcement, 2026-10-30)

"Hi all. In today's tutorial, we will explore something called daisyworld. Please bring phones or laptops, because you will need to open the below link." The link opens the app with the settings set in the address bar (Classroom announcement, 2026-10-30):
https://joymonteiro.github.io/intro_climate_science/tutorials/daisyworld-land-ocean/#Lmin=0.4&Lmax=1.8&dur=600&Lb=0.78&La=0.86&Lfix=0.8&yrs=40&ocean=0&Ao=0.1&mld=50&gamma=0.3&qp=20&Topt=22.5&Aw=0.75&Ab=0.25&Ag=0.5&mode=up&logx=0

"Hi guys, Today's tutorial will be happening in NLH!" (Classroom announcement, 2026-10-30)

## Files
- [Daisyworld handout (PDF)](https://joymonteiro.github.io/intro_climate_science/tutorials/daisyworld-land-ocean/daisyworld_land_ocean_handout.pdf): 19 pages; read up to the start of Run 5's table; Runs 6–10 and Part 3 not read (the text was cut off).
- [Daisyworld app](https://joymonteiro.github.io/intro_climate_science/tutorials/daisyworld-land-ocean/): interactive app, not opened (needs a browser).

## Related
- [[introduction-to-climate-science/2026-08-19-lecture-4-sensitivity-and-albedo-feedback]]: ice-albedo feedback, multiple steady states and stability that Daisyworld illustrates
- [[introduction-to-climate-science/2026-08-19-lecture-3-planetary-energy-balance]]: the energy balance $\frac{S}{4}(1-\alpha)=\sigma T^4$ behind the model
- [[introduction-to-climate-science/2026-10-22-advanced-reading-monsoon-dynamical-theory-webster]]: land versus ocean heat capacity
- [[01-climate/concepts/ice-albedo-feedback]]: your concept note on the positive albedo feedback
