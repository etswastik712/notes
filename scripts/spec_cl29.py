"""Concept notes for CL29-CL30 (Joy O7 and the carbon-boxes tutorial; added 2026-11-21).   .venv/bin/python -W ignore scripts/spec_cl29.py"""
from mkconcept import write
C29 = "CL29 The Ocean's Ledger VI - Slow Swings and the Ocean's Memory for Carbon"
C30 = "CL30 Tutorials III - Three Boxes of Carbon"
T, EBY = "taught", "extra-beyond"
J = ["joy"]
ITEMS = [
 dict(title="Delayed Oscillator", aliases=["ENSO delayed oscillator", "recharge oscillator", "Kelvin and Rossby waves in ENSO", "why El Nino turns around"], scope=[T], by=J,
  syl={T: "Joy O7 notes §6; Stewart §14.2 pp. 244–245 (read)"},
  intuition="A fast loop that feeds itself plus a slow loop that undoes it, arriving late, makes a swing of its own.",
  key="Weaker trades launch an eastward equatorial **Kelvin wave** (deepens the eastern warm layer: warming, Bjerknes growth) and westward off-equatorial **Rossby waves** (thin the western layer). The Rossby waves **reflect** off the western boundary and return east with the opposite sign, thinning the eastern layer about **six months** later: a **delayed negative feedback**. Period 2–7 years, mean ~4 (not a clock). Wyrtki: a cycle discharges the tropical Pacific's heat, which the trades must slowly recharge.",
  body="Positive feedback + instantaneous negative feedback gives a switch (Stommel); positive + **delayed** negative gives an oscillation (ENSO).",
  used=[C29], related=["Bjerknes Feedback", "ENSO", "Stommel Two-Box Model"]),
 dict(title="Climate Anomaly", aliases=["anomaly", "SST anomaly", "departure from the mean", "running mean"], scope=[T], by=J,
  syl={T: "Joy O7 notes §1–§2"},
  intuition="What is unusual: the value minus its normal value for the same place and time of year.",
  key="Anomaly = value − climatological mean (e.g. 1991–2020, same week). Nov 2026: +3.1 °C in Niño-3.4, +5.4 °C off Peru. A **running mean** averages over a sliding window to show the trend under the swings.",
  used=[C29, "CL20 ENSO and the Walker Circulation"], related=["ENSO", "Low-Pass Filter"]),
 dict(title="Low-Pass Filter", aliases=["moving average", "ocean as a low-pass filter", "red noise from white noise"], scope=[T, EBY], by=J,
  syl={T: "Joy O7 notes §3", EBY: "the 1/√w arithmetic, CL29 §3"},
  intuition="A slow system averages fast forcing: it keeps the slow wiggles and throws away the fast ones.",
  key="An ocean responding to atmospheric noise does roughly $O(t)\\approx\\frac1\\tau\\int_{t-\\tau}^ta\\,dt'$: fast variations removed, slow ones kept, no energy added. A moving average of white noise over $w$ samples has standard deviation $\\propto1/\\sqrt w$ (0.109 for $w=100$, 0.051 for 400).",
  used=[C29, "CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia"], related=["Climate Anomaly", "Climate Response Time"]),
 dict(title="Ocean Carbon Sink and Airborne Fraction", aliases=["airborne fraction", "ocean carbon uptake", "global carbon budget", "where our carbon went"], scope=[T], by=J,
  syl={T: "Joy O7 notes §7; carbon-boxes handout §1"},
  intuition="Of every 100 tonnes of carbon we emitted, about 41 are still in the air; the ocean took 28 and the land 25.",
  key="Global Carbon Budget 2025, 1750–2024: 752 GtC emitted (505 fossil + cement, 248 land use); air 312 GtC (**41 %**), ocean 210 (**28 %**), land 190 (**25 %**), ~5 % other. Ocean uptake today ~3.2 GtC/yr. 1 ppm CO₂ = 2.124 GtC.",
  used=[C29, C30], related=["Revelle Factor", "Carbon Cycle", "Three-Box Carbon Model"]),
 dict(title="Revelle Factor", aliases=["buffer factor", "carbonate buffer", "ocean acidification feedback", "1/B"], scope=[T], by=J,
  syl={T: "Joy O7 notes §7; carbon-boxes handout §2.2"},
  intuition="The ocean's appetite for CO₂ falls as it eats: each tonne absorbed makes the water more acidic and less willing to take the next.",
  key="Seawater holds carbon mostly as HCO₃⁻ and CO₃²⁻: $1/B=1+k_1/[\\mathrm H^+]+k_1k_2/[\\mathrm H^+]^2\\approx170$ pre-industrially (why the ocean holds ~50–60× the air's carbon). Absorbing CO₂ releases H⁺, lowering pH and $1/B$. Consequences: ~22 % of our carbon stays in the air once the ocean catches up; 24 % of a 1000 GtC pulse but 42 % of 5000 GtC; without it (a linear model) only 1.6 %.",
  used=[C29, C30], related=["Ocean Carbon Sink and Airborne Fraction", "Three-Box Carbon Model", "Inorganic Chemistry - Course Map"]),
 dict(title="Carbon Commitment", aliases=["climate commitment", "committed warming", "long tail of CO2", "Archer timescales"], scope=[T], by=J,
  syl={T: "Joy O7 notes §9–§10, 'Read this part'"},
  intuition="Stopping emissions does not undo them: the ocean's slowness keeps CO₂ high and warming going for centuries.",
  key="BEAM: stop in 2025 → CO₂ settles at **334 ppm**, not 280. Archer et al. (2009): ocean uptake over **2–20 centuries** (20–35 % stays), sea-floor CaCO₃ over **3000–7000 yr**, rock weathering over **10⁵ yr**. 'The memory that makes El Niño forecastable is the same memory that commits us to the warming.'",
  used=[C29, C30], related=["Revelle Factor", "Climate Response Time", "Carbon Cycle"]),
 dict(title="Three-Box Carbon Model", aliases=["BEAM", "Bolin and Eriksson model", "Glotter 2014 model", "Three Boxes of Carbon"], scope=[T, EBY], by=J,
  syl={T: "Joy O7 §8, carbon-boxes handout Part 2", EBY: "re-implementation `scripts/cl_carbon_boxes.py`"},
  intuition="Air, upper ocean, deep ocean: three tanks connected in a row, with chemistry that makes the middle tank fill unevenly.",
  key="$\\dot M_{AT}=E-k_a(M_{AT}-AB\\,M_{UP})$, $\\dot M_{UP}=k_a(\\dots)-k_d(M_{UP}-M_{LO}/\\delta)$, $\\dot M_{LO}=k_d(\\dots)$; 595 / 714 / 35 680 GtC; $1/k_a=5$ yr, deep turnover $\\delta/k_d=1000$ yr ($\\delta=50$). Settled level independent of the rates (334 ppm for our emissions); upper ocean catches up in ~4 months, the deep ocean in ~1000 yr. Fits Mauna Loa only with a 200-yr turnover (a fudge: the thermocline is fast, the abyss slow).",
  body="Tool: `cl_three_boxes`.", used=[C30, C29], related=["Revelle Factor", "Stommel Two-Box Model", "Ocean Carbon Sink and Airborne Fraction"]),
]
if __name__ == "__main__":
    write("01-Climate", "climate", ITEMS)
