---
id: introduction-to-climate-science/2026-08-13-tutorial-2-energy-balance-problems
aliases: [Tutorial 2 (August), Energy balance tutorial]
tags: [climate, introduction-to-climate-science, tutorial, problem-set]
trust_tier: agent_written
---

# Tutorial 2 (August): energy-balance problems and code

Not the same as the September "Tutorial 2" on model experiments and molecular weights ([[introduction-to-climate-science/2026-09-04-tutorial-2-model-experiments-and-molecular-weights]]).

## Covered
Problems (posted 2026-08-13; no due date):
1. Earth's emission temperature is 255 K and its surface temperature 288 K. A volcanic eruption raises the albedo to 47 %. (a) By how much does the effective emission temperature change? (b) If the observed surface temperature falls by 7 K, what is the total greenhouse effect (average increase in temperature of the atmosphere) after the eruption? Practises: $T_e=[S_0(1-\alpha)/(4\sigma)]^{1/4}$ and the greenhouse effect as $T_s-T_e$.
2. (a) Why is 13 May "Zero Shadow Day" in Pune, and what does it mean for solar energy at solar noon (~12:35 PM IST)? (b) Plot the diurnal variation of OLR together with absorbed shortwave (ASR) over 24 h; when is OLR − ASR zero? Plot temperature as well with simplifying assumptions. (c) Solar radiation peaks at 12:35 PM IST but the air temperature peaks near 3 PM; use net energy gain (ASR − OLR) to explain why temperature keeps rising after solar noon (marked important). Practises: solar geometry, energy-balance reasoning, lag between forcing and temperature.
3. (a) Net heat loss of a person in a 25 °C room (body area 2 m$^2$, skin a few degrees below body temperature, reasonable guess). (b) Heat lost in 24 h in kcal. (c) Compare with daily food energy intake. Practises: net radiative exchange $\sigma(T_{skin}^4-T_{room}^4)A$.
4. A leaf temperature is measured on a sunny day by two students with an IR gun, one shading the bush first and one not (short gap). Would they measure the same temperature, and why? With sun heat flux 500 W m$^{-2}$ and the supplied graph, discuss the discrepancy from the actual temperature. Practises: IR thermometry, radiative vs air temperature.
5. Plot in Desmos: (a) $y=x$, (b) $y=x^4$, (c) $y=e^{-x}$, (d) $y=xe^{-x}$, (e) $y=x^4e^{-x}$, (f) $y=x^{-5}\exp\!\big(1/(x-1)\big)$. Practises: shapes of power-law × exponential functions (the form of Planck-type curves).

Tutorial code (2026-08-12): a Colab notebook `intro_clim.ipynb` with Python basics (print, comments, numpy, matplotlib, sympy `solve` and `Symbol`) and a "global mean temperature" exercise. Only the beginning was read.

Logistics (2026-08-13): the LHC 107 group could join any other room (105, 106, 108 or 205); group leaders should return their IR guns.

## From the post
Post (2026-08-12): "PFA tutorial codes for this week below." Post (2026-08-13): "PFA the tutorial problems for this week." Post (2026-08-13): "Dear all, For this tutorial, people in Lhc 107 can join any other room of their choice. (Lhc 105,106,108 or 205). Also, all group leaders are requested to give back your ir guns."

## Files
- [Tutorial 2.pdf](https://drive.google.com/file/d/1RXv5K9Ef6dlp_64m8jT6lu2f8aYc0Rjq/view?usp=drive_web): read in full (the graph for problem 4 is not in the text).
- [intro_clim.ipynb](https://colab.research.google.com/drive/1F6i9ahbPAnePSc5giKTsJWRr8HXbkuub?ouid=102390748340458352584): 1.1 M characters, mostly embedded images; only the first 2 000 characters read.

## Related
- [[introduction-to-climate-science/2026-09-17-study-material-5-radiative-balance]]: emission temperature and greenhouse models
- [[01-climate/concepts/effective-emission-temperature]]: $T_e$ for problem 1
- [[01-climate/cl03-radiation-and-planetary-energy-balance]]: radiation and energy balance chapter
- [[03-thermodynamics/concepts/stefan-boltzmann-law]]: needed for problems 1 and 3

<!-- kurooto:materialbd85b039 -->
Textbook: [[introduction-to-climate-science/books/intro-clim|intro_clim]] (its concepts are listed there).
<!-- /kurooto:materialbd85b039 -->
