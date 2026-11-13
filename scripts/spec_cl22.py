"""Concept notes for CL22-CL28 (Joy Monteiro's 2026 ocean module).   .venv/bin/python -W ignore scripts/spec_cl22.py"""
from mkconcept import write

C22 = "CL22 The Ocean's Ledger I - Accounting for Energy"
C23 = "CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia"
C24 = "CL24 The Ocean's Ledger III - Wind and the Momentum Ledger"
C25 = "CL25 The Ocean's Ledger IV - Salt, Density and Water Masses"
C26 = "CL26 The Ocean's Ledger V - Mass, the Overturning and the Switch"
C27 = "CL27 Tutorials I - Daisyworld with Land and Ocean"
C28 = "CL28 Tutorials II - Earth's Energy Budget from Space (CERES)"
T, EB, EBY = "taught", "extra-book", "extra-beyond"
J = ["joy"]
JB = ["joy", "book"]


def src(slide, extra=""):
    return f"Joy {slide} (2026)" + (f"; {extra}" if extra else "")


ITEMS = [
 dict(title="Climate as Accounting", aliases=["three hats", "energy ledger", "ledgers"], scope=[T], by=J, syl={T: src("O1 handout §1, §7")},
  intuition="A planet's climate is a set of account books (energy, momentum, mass, salt, carbon); winds and currents are how they are kept balanced.",
  key="Four ledgers, one a week: energy, momentum, mass and salt, carbon. Each with three hats: **accountant** (which budget, what goes in and out), **data scientist** (what does it look like), **physicist/biologist** (why). The budgets are coupled: salt ↔ water ↔ latent heat ↔ momentum.",
  body="Joy's thesis: Argha's energy balance and Suhas's circulation are one subject.", used=[C22], related=["Earth System", "Poleward Energy Transport", "Top-of-Atmosphere Radiation Budget"]),
 dict(title="Cloud Radiative Effect", aliases=["CRE", "cloud effect"], scope=[T], by=J, syl={T: src("CERES tutorial, Exercise 4")},
  intuition="Clouds reflect sunlight (cooling) and trap infrared (warming); the net is the difference between the all-sky and clear-sky flux.",
  key="CRE = (net flux, all skies) − (net flux, clear skies), separately SW, LW and total. CERES EBAF 2010–2024 global mean: **SW −45.0, LW +25.4, net −19.6 W m⁻²** (without clouds the Earth would gain +20.9 instead of +1.26). Stratocumulus (low, bright) cool strongly (−69 off Peru); deep convection nearly cancels (SW −59, LW +50, net −9 over the warm pool); over snow clouds warm (up to +39).",
  body="Cooling ≈ 15× the planetary imbalance, so small cloud changes matter.", used=[C28, C22], related=["Albedo", "Outgoing Longwave Radiation", "Top-of-Atmosphere Radiation Budget"]),
 dict(title="Thermal Diffusivity and Penetration Depth", aliases=["heat equation", "skin depth", "d = sqrt(2 kappa / omega)"], scope=[T], by=J, syl={T: src("Week 2 deck frames 12–17; O2 handout §5")},
  intuition="Heat soaks into soil only as deep as √(diffusivity × period): about 10 cm in a day, 2 m in a year.",
  key="$\\partial_tT=\\kappa\\partial_z^2T$, $\\kappa=k/\\rho c\\approx(0.3\\text{–}1)\\times10^{-6}$ m² s⁻¹. A periodic surface swing gives $T'=Ae^{-z/d}\\cos(\\omega t-z/d)$, $d=\\sqrt{2\\kappa/\\omega}$: day 9/12/17 cm, year 1.7/2.2/3.2 m for κ = 0.3/0.5/1×10⁻⁶; as a slab $C=\\rho c\\,d/\\sqrt2$ ≈ 3–6 cm and 0.6–1.1 m of water. Still water κ = 1.4×10⁻⁷: 6 cm and 1.2 m.",
  body="Hartmann's (4.10) omits the factor 2, so his depth is ours ÷ √2. Reach grows as √period.", used=[C23], related=["Mixed Layer", "Eddy Diffusivity", "Ocean Heat Capacity and Seasonal Storage"]),
 dict(title="Eddy Diffusivity", aliases=["turbulent mixing coefficient", "mixing below the mixed layer"], scope=[T], by=J, syl={T: src("Week 2 deck frames 19–28")},
  intuition="Turbulent eddies mix heat 10⁴–10⁶ times faster than molecules, but stratification cuts it by orders of magnitude below the mixed layer.",
  key="Mixed layer: well mixed to its base. Thermocline: $K\\sim10^{-5}$–$10^{-4}$ m² s⁻¹; reach $\\sqrt{2K/\\omega}$: 1 yr 10/32 m, 10 yr 32/100 m, 100 yr 100/317 m for K = 10⁻⁵/10⁻⁴. No water moves sideways: mixing up and down alone sets the ocean's active thermal inertia.",
  body="Tracer-release experiments (Ledwell et al. 1993, as Joy cites) give ≈ 10⁻⁵.", used=[C23], related=["Mixed Layer", "Thermocline and Pycnocline", "Thermal Diffusivity and Penetration Depth"]),
 dict(title="Climate Response Time", aliases=["tau = C/lambda", "slab equation", "thermal inertia", "effective heat capacity"], scope=[T], by=J, syl={T: src("Week 2 deck frames 29–31; O3 handout §3")},
  intuition="Heat capacity divided by the radiative restoring strength is how long a surface takes to forget a push.",
  key="Slab: $C\\,dT'/dt=F'(t)-\\lambda T'$, $\\tau=C/\\lambda$. With λ = 3.8 W m⁻² K⁻¹: land (≈ 1 m water) 12 d, atmosphere (2.4 m) 1 month, mixed layer (50 m) 1.7 yr, full ocean (4,000 m) 140 yr. Seasonal range: Yakutsk 57, Delhi 23, Pune 9, Mumbai 5, Arabian Sea 5, equatorial Pacific 2 K.",
  body="Heat capacity changes the path, not the destination (set dT/dt = 0 and C drops out).", used=[C23, C27], related=["Planck Sensitivity", "Ocean Heat Capacity and Seasonal Storage", "Mixed Layer"]),
 dict(title="Hasselmann Stochastic Climate Model", aliases=["weather noise", "red noise climate", "depth sets the timescale"], scope=[T], by=J, syl={T: src("Week 2 deck frames 33–38; O3 handout")},
  intuition="Fast random weather, integrated by a slow slab, makes slow climate wandering with nothing slow driving it.",
  key="For a white push F′ on a slab: power ∝ 1/(ω²C² + λ²). Fast swings: power ∝ 1/C² (mixed layer ≈ 990× below land for the app's numbers); slow swings: λ sets it and C drops out (ratio 0.99 at 100–1000 yr); the bend is at period 2πτ. **Depth sets the timescale, not the size of the slow swings.** A deep ocean calms the slowest swings (≈ ×0.6).",
  body="Hasselmann (1976), cited by Joy, not read.", used=[C23, C27], related=["Climate Response Time", "Mixed Layer", "Climate vs Weather"]),
 dict(title="Wind Stress", aliases=["surface stress", "momentum flux to the ocean"], scope=[T], by=J, syl={T: src("Week 2 deck frames 51–53")},
  intuition="The shear force per unit area the wind exerts on the sea; the ocean's input to the momentum ledger.",
  key="τ ≈ 0.1 N m⁻² typical (bulk formula $\\tau=\\rho_aC_DU_{10}^2$). Trades push the water west, westerlies east, strongest in the Southern Ocean (≈ 50°S). A stress change across a stirred layer is what accelerates it: $F=\\tfrac1\\rho\\partial_z\\tau$; τ/(ρH) ≈ 2×10⁻⁶ m s⁻² on 50 m.",
  body="Ekman transport is $\\tau/\\rho f$ per metre of width.", used=[C24], related=["Ekman Transport", "Planetary Boundary Layer and Friction", "Trade Winds and Westerlies"]),
 dict(title="Sea-Surface Height", aliases=["hills of water", "dynamic topography", "gyre height"], scope=[T], by=J, syl={T: src("O4 deck frames 25–31")},
  intuition="Ekman convergence piles water 1 m high in the subtropics; geostrophy sends the flow around the hill, not down it.",
  key="Subtropical gyres stand ≈ 0.9 m above the subpolar ocean (N Pacific 0.93, N Atlantic 0.94, S Pacific 1.05 m). Surface geostrophic speed $u=(g/f)\\,\\text{slope}$: 1 m over 1,500 km ≈ 6.5 cm s⁻¹; 1 m over 100 km ≈ 1 m s⁻¹ (Gulf Stream). Clockwise N, anticlockwise S; fast flow on the west side (Stommel 1948).",
  body="Floating debris collects in the middle of the hills (garbage patches).", used=[C24], related=["Geostrophic Balance", "Subtropical Gyre", "Western Boundary Current"]),
 dict(title="Sverdrup (Unit)", aliases=["Sv", "sverdrup"], scope=[T], by=J, syl={T: src("O3 handout §7")},
  intuition="One million cubic metres of water per second: the only sensible unit for ocean currents.",
  key="1 Sv = 10⁶ m³ s⁻¹ ≈ 10⁹ kg s⁻¹. Gulf Stream off Florida ≈ 30 Sv (100 km × 600 m × 0.5 m s⁻¹); Atlantic deep-water formation 15–20 Sv; Antarctic ≈ 10 Sv; Drake Passage 125 ± 11 Sv (Stewart p. 229); AMOC at 26.5°N ≈ 17 Sv.",
  body="Named after Harald Sverdrup.", used=[C22, C24, C26], related=["Antarctic Circumpolar Current", "Thermohaline Circulation"]),
 dict(title="Evaporation Minus Precipitation", aliases=["E - P", "E-P", "salt budget"], scope=[T], by=J, syl={T: src("O5 deck frames 2–8; O5 handout §2–5")},
  intuition="Salt stays when water evaporates or freezes, so surface salinity records E − P.",
  key="Salinity ≈ 35 g kg⁻¹ (mean 34.7). A 50 m layer losing 1 m yr⁻¹ gets saltier by 0.7 g kg⁻¹ yr⁻¹ unless currents carry the salt away. Box means (2010–2020): N Atlantic subtropics +2.8 mm day⁻¹ (S 37.2), S Pacific +3.3 (36.2), E Pacific rain band −3.9 (33.8), W Pacific warm pool −3.6 (34.5), Arabian Sea +2.6 (36.2), Bay of Bengal −1.1 plus rivers (32.9). Atlantic exports 0.32 Sv of vapour (≈ Amazon) to the Pacific: 35.6 vs 34.6.",
  body="Subtropics win twice (clear, dry sinking air); ITCZ loses twice.", used=[C25], related=["Seawater Salinity", "Hadley Cell", "Intertropical Convergence Zone"]),
 dict(title="Potential Density", aliases=["sigma", "sigma-theta", "density anomaly", "equation of state of seawater"], scope=[T], by=JB, syl={T: src("O5 deck frames 10–13; O5 handout §6")},
  intuition="Density of a water sample brought adiabatically to the surface, quoted as ρ − 1000 so waters from different depths can be compared.",
  key="σ = ρ − 1000 kg m⁻³ (surface ≈ 27). Colder or saltier is denser. At 25 °C, S = 35: ρα = 0.30 kg m⁻³ per K, ρβ = 0.74 per g/kg (cooling 3.3 K ≡ 1.4 g/kg); at 0 °C: 0.054 and 0.80 (18 K ≡ 1.2 g/kg): warm water is ruled by temperature, cold water by salt. Seawater with S > 24.7 has no 4 °C maximum; freezing point −1.92 °C at S = 35.",
  body="Hartmann (p. 199) and Stewart ch. 6; values TEOS-10 (Joy), reproduced with EOS-80 in the vault.", used=[C25], related=["Water Mass and T-S Diagram", "Seawater Salinity", "Brine Rejection"]),
 dict(title="North Atlantic Deep Water", aliases=["NADW"], scope=[T], by=J, syl={T: src("O5 handout §8; O6 deck")},
  intuition="Salty water cooled in the Nordic and Labrador Seas until it sinks, then spreads south at 2–3 km.",
  key="≈ 4 °C, S ≈ 35.0 (σ ≈ 27.8); a salinity maximum at 1,750–3,000 m in the 30°W section; formation by **cooling** of salty Gulf Stream water (not brine), 15–20 Sv. Becomes Circumpolar Deep Water in the Southern Ocean, then rises where isopycnals reach the surface near 60°S.",
  body="No counterpart in the North Pacific: its surface is 2.3 g/kg fresher.", used=[C25, C26], related=["Deep Water Formation", "Antarctic Intermediate Water", "Antarctic Bottom Water"]),
 dict(title="Antarctic Intermediate Water", aliases=["AAIW"], scope=[T], by=J, syl={T: src("O5 handout §8")},
  intuition="Cold fresh surface water of the Southern Ocean, pushed down at the polar front and sent north at 1 km.",
  key="≈ 3.3 °C, S ≈ 34.15 (σ ≈ 27.2); forms near 50–55°S (rain > evaporation, melting ice); pushed down by Ekman convergence equatorward of the westerlies; salinity minimum 34.2–34.5 at 700–900 m from 40°S to the equator.",
  body="Stewart writes AIW.", used=[C25], related=["North Atlantic Deep Water", "Antarctic Bottom Water", "Ekman Pumping"]),
 dict(title="Antarctic Bottom Water", aliases=["AABW"], scope=[T], by=J, syl={T: src("O5 handout §8")},
  intuition="The densest water in the ocean, made on the Antarctic shelves by cold and brine.",
  key="≈ 0.4 °C, S ≈ 34.67 (σ ≈ 27.8); Weddell and Ross Seas; katabatic winds, polynyas, brine rejection; flows north on the floor (Atlantic 50°S–30°N) and into the Indian and Pacific basins. Colder and denser than NADW but **not saltier**.",
  body="About 10 Sv.", used=[C25, C26], related=["Brine Rejection", "Deep Water Formation", "Katabatic Wind and Polynya"]),
 dict(title="Katabatic Wind and Polynya", aliases=["katabatic", "polynya", "coastal polynya"], scope=[T], by=J, syl={T: src("O5 handout §7")},
  intuition="Cold dense air pours off the Antarctic ice dome, chills the sea and blows the new ice away, so more ice forms.",
  key="A katabatic wind is dense air flowing downhill off an ice sheet. It cools the water and drives sea ice offshore, leaving open water (**polynyas**) where ice forms fast and rejects brine (Hartmann p. 224, as Joy cites it): the densest water in the ocean forms against the coast.",
  body="Can be modelled in a tank with salty coloured water on a ramp.", used=[C25], related=["Brine Rejection", "Sea Ice", "Antarctic Bottom Water"]),
 dict(title="Stommel Two-Box Model", aliases=["Stommel box", "salt-advection feedback", "AMOC bistability"], scope=[T], by=J, syl={T: src("O6 deck frames 19–23")},
  intuition="A warm salty box and a cold fresher box: the flow carries salt north, which keeps the north heavy, which keeps the flow going.",
  key="Positive salt feedback; in a nondimensional form $\\dot x=1-x(1+|q|)$, $\\dot y=F-|q|y$, $q=x-y$: thermal branch $F=q(1-q-q^2)/(1+q)$ with maximum 0.141 at q = 0.30; a reversed state exists for every F > 0; collapse at F_max, recovery only at F < 0. Two stable states for the same forcing, **hysteresis**.",
  body="Stommel (1961); Stewart pp. 215–218 (not read). A caricature: shows possibility, not that the ocean has it.", used=[C26], related=["Hysteresis", "Ice-Albedo Feedback", "Atlantic Meridional Overturning Circulation"]),
 dict(title="Atlantic Meridional Overturning Circulation", aliases=["AMOC", "RAPID array", "MOC"], scope=[T], by=JB, syl={T: src("O6 deck frames 16–25", "Stewart p. 229 read")},
  intuition="Warm water flows north in the upper Atlantic and returns cold at depth; a mooring array has measured it since 2004.",
  key="RAPID-MOCHA at 26.5°N (since April 2004): mean 17.0 Sv, 10-day values −4 to 32 Sv, yearly means 14.9–19.1 Sv (slide); Stewart's early 24°N array: 18.7 ± 5.6 Sv. IPCC AR6 SPM C.3.4: very likely to weaken this century, medium confidence of no abrupt collapse before 2100; a collapse would shift the tropical rain belt south and weaken the African and Asian monsoons.",
  body="Twenty years cannot show a trend in a system with a 1,000-year memory.", used=[C26], related=["Thermohaline Circulation", "Stommel Two-Box Model", "Deep Water Formation"]),
 dict(title="Hysteresis", aliases=["multiple equilibria", "bistability", "path dependence"], scope=[T], by=J, syl={T: src("O6 deck frames 21–22; Daisyworld tutorial Run 5")},
  intuition="Where the system is depends on how it got there: the same forcing, two states.",
  key="With two stable branches over a range of forcing, increasing the forcing past the edge of one branch makes the state jump; reversing the forcing leaves it on the other branch until a different edge. Daisyworld all land: daisies die at L ≈ 1.63 and return at 1.17; AMOC box model: collapse at F_max, return only at F < 0. Transient version: forcing faster than the response gives path-dependent states.",
  body="Same structure as Argha's snowball multiple equilibria.", used=[C26, C27], related=["Snowball Earth", "Ice-Albedo Feedback", "Stommel Two-Box Model"]),
 dict(title="Daisyworld", aliases=["Daisyworld land and ocean", "Lovelock Watson model"], scope=[T], by=J, syl={T: src("tutorials 1 and 2")},
  intuition="A planet whose only life, black and white daisies, steers its temperature by changing its colour, without any plan.",
  key="$A=f(a_wA_w+a_bA_b+xA_g)+(1-f)A_o$; $C\\,dT/dt=SL(1-A)-\\sigma T^4$; patches $T_i=T+q'(A-A_i)$; $da_i/dt=a_i[x\\beta(T_i)-\\gamma]$. Ocean: **darker** (shifts life's window to dimmer sun), **slower** ($\\tau=C/\\lambda$), and smaller leverage ($0.5f$). Surviving is not regulating; fast physics plus slow biology gives an overshoot.",
  body="With grazers and an ocean's delay the loop becomes a boom–bust cycle (≈ 8 yr).", used=[C27, "CL04 Feedback and Multiple Steady States"], related=["Causal Loop Diagram", "Ice-Albedo Feedback", "Climate Response Time"]),
 dict(title="Causal Loop Diagram", aliases=["balancing loop", "reinforcing loop", "delay"], scope=[T], by=J, syl={T: src("Daisyworld part 2 handout §1.2")},
  intuition="Arrows with + or − show how variables push each other; the count of minus signs round a loop tells you if it pushes back.",
  key="An arrow A → B with + means they move together, − opposite. A loop with an odd number of − signs is **balancing** (resists change), even or none is **reinforcing**. ‖ marks a delay. A balancing loop with a long delay overshoots and cycles (the shower with a long pipe).",
  body="Daisyworld: B1 white-daisy thermostat, B2 black-daisy thermostat, B3 and B4 food; the path land T → grazers → white daisies → land T has two minus signs: reinforcing.", used=[C27], related=["Daisyworld", "Climate Feedback Factor", "Hysteresis"]),
]

write("01-Climate", "climate", ITEMS)
