"""Wrap converted EC2123 bodies (tex2vault_ls.py output *.md.body) into vault chapters in 05-Landscapes-Geomorphology/.
python3 scripts/assemble_ls.py <dir with *.md.body>"""
import os
import re
import sys

BODY = sys.argv[1]
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "05-Landscapes-Geomorphology")

CH = [
 # code, title, part, slides, story, abilities, mermaid, links
 ("LS01", "Landscapes as Physical Systems", "I", "1–24", "A landscape is a surface $z(x,y,t)$ that changes by uplift, weathering, erosion and deposition; mapping it, measuring the forces and fluxes on it, and modelling how it evolves are three views of one physical problem.",
  ["state the programme *map, measure, model* and the kinematic bookkeeping $\\partial_tz=U-E$", "list the processes that shape landscapes and give their spatial and temporal scales", "read the Google-Earth tour of slides 10–18 and answer its exercises"],
  'flowchart LR\n  A["map: patterns, scales"] --> B["measure: forces, fluxes"]\n  B --> C["model: mass, force, steady state"]\n  C --> D["processes: uplift, weathering, erosion"]\n  D --> E["scales in space and time"]'),
 ("LS02", "Mechanics and Mathematics Toolkit", "I", "35–38, 45–50", "Almost every landscape equation is one of four things: a Taylor expansion, mass conservation with a flux, a force balance with a stress, or a viscous flow; this chapter derives each once so the rest can use them.",
  ["expand a function in a Taylor series and use order-of-magnitude reasoning", "write mass conservation $\\partial_t\\rho+\\partial_xq=S$ and derive the diffusion equation", "balance forces on a slab and use stress, pressure and viscosity", "solve the Newtonian viscous flow down an incline"],
  'flowchart LR\n  A["orders of magnitude,<br/>dimensions"] --> B["Taylor series,<br/>Newton laws"]\n  B --> C["mass conservation,<br/>flux, diffusion"]\n  C --> D["force balance, stress"]\n  D --> E["viscous flow"]'),
 ("LS03", "Digital Elevation Models and Terrain Analysis", "II", "25, 28, 56–57", "A digital elevation model is a matrix of heights; slopes, curvature, flow directions, drainage basins and the hypsometric curve are just arithmetic on that matrix.",
  ["describe a DEM as a raster and say how elevation is measured (SRTM, LiDAR, photogrammetry)", "compute slope, aspect and curvature on a grid", "extract a river network and a drainage basin", "read and compute a hypsometric curve"],
  'flowchart LR\n  A["DEM = raster of z"] --> B["how z is measured"]\n  B --> C["slope, aspect, curvature"]\n  C --> D["flow routing,<br/>river network, basins"]\n  D --> E["hypsometry"]'),
 ("LS04", "Map Projections and Reference Surfaces", "II", "31–32, 42", "A sphere cannot be flattened without distortion; the Mercator projection preserves angles at the price of area, and the heights on every map are relative to a reference ellipsoid and a datum.",
  ["explain why every map projection distorts", "derive the Mercator projection from conformality", "describe transverse Mercator and UTM", "distinguish geoid, ellipsoid and datum"],
  'flowchart LR\n  A["sphere is not developable"] --> B["Mercator: conformal"]\n  B --> C["transverse Mercator, UTM"]\n  C --> D["ellipsoid and datum"]'),
 ("LS05", "Shape of Planets", "III", "33, 41–42, 51", "Planets are round because gravity beats rock strength, slightly flattened because they rotate, and the geoid is the equipotential surface sea level would follow.",
  ["show that large bodies are spherical (gravity vs strength)", "derive the flattening of a rotating planet", "define the geoid and its relation to the ellipsoid"],
  'flowchart LR\n  A["gravity vs strength:<br/>why round"] --> B["rotation: oblateness"]\n  B --> C["flattening ~ 1/300"]\n  C --> D["geoid vs ellipsoid"]'),
 ("LS06", "Maximum Topography", "III", "52–55", "A column of rock can only stand as tall as its strength allows; comparing strength with the weight of the column gives an upper bound on relief on Earth, Mars and small bodies.",
  ["state the strength of rock and its yield criterion", "derive an upper bound on mountain height", "explain friction-limited relief on small bodies"],
  'flowchart LR\n  A["rock strength"] --> B["weight of a column"]\n  B --> C["upper bound on relief"]\n  C --> D["small bodies: friction limit"]'),
 ("LS07", "Isostasy", "IV", "58–64", "Topography floats: mountains have roots like icebergs, the mantle flows to restore the balance, and an eroding mountain rises again.",
  ["state Airy and Pratt isostasy and compute a root", "explain why isostasy works (mantle flow)", "derive the thermal subsidence of the ocean floor", "compute the isostatic uplift caused by erosion"],
  'flowchart LR\n  A["gravity anomalies"] --> B["Airy isostasy: roots"]\n  B --> C["why it works:<br/>mantle flows"]\n  C --> D["oceans: thermal isostasy"]\n  D --> E["erosion -> rebound"]'),
 ("LS08", "Plate Tectonics Strain Stress and Convection", "V", "65–75", "Plates move because the mantle convects; stress and strain rate in the lithosphere tell where earthquakes and volcanoes occur and how fast the plates go.",
  ["map earthquakes and volcanoes onto plate boundaries", "define strain, strain rate and stress", "state the Rayleigh–Bénard criterion", "estimate a plate speed"],
  'flowchart LR\n  A["earthquakes, volcanoes"] --> B["strain rate"]\n  B --> C["stress in the lithosphere"]\n  C --> D["Rayleigh-Benard convection"]\n  D --> E["plate speed estimate"]'),
 ("LS09", "Faults and Earthquakes", "V", "85–94", "Anderson's theory turns the stress state into a fault type; earthquakes are the stick–slip release of stored elastic strain, and the Himalaya records that cycle on four time scales.",
  ["classify normal, reverse and strike-slip faults by principal stresses (Anderson)", "describe the earthquake cycle as stick–slip", "read InSAR and fault-topography figures", "tell the story of the Himalaya over four time scales"],
  'flowchart LR\n  A["principal stresses"] --> B["fault types (Anderson)"]\n  B --> C["stick-slip: earthquake cycle"]\n  C --> D["finite faults, InSAR"]\n  D --> E["Himalaya: 4 time scales"]'),
 ("LS10", "Folds Flexure and Mountain Building", "V", "76–84, 90, 95", "A plate bends elastically under a load (flexure), layers buckle into folds, a mountain belt is a critical wedge, and climate feeds back on tectonics.",
  ["derive the elastic flexure of a plate under a line load", "describe fold geometry and buckling", "explain critical taper (sandbox and Himalaya)", "state the climate–tectonics coupling"],
  'flowchart LR\n  A["mountain belts,<br/>passive margins"] --> B["elastic flexure"]\n  B --> C["folds, buckling"]\n  C --> D["critical taper: sandbox"]\n  D --> E["climate-tectonic coupling"]'),
 ("LS11", "Weathering and Regolith", "VI", "96–116", "Weathering turns rock into mobile regolith, chemically by dissolution and physically by cracking; regolith thickness is production balanced against removal.",
  ["define weathering and the two limiting regimes (supply- and transport-limited)", "derive regolith thickness from production against erosion", "describe chemical weathering (Arrhenius, Goldich series, rates)", "describe physical weathering (frost cracking, thermal stress, salts)"],
  'flowchart LR\n  A["weathering regimes"] --> B["regolith: production vs erosion"]\n  B --> C["chemical weathering"]\n  B --> D["physical weathering"]\n  C --> E["solute vs sediment load"]\n  D --> E'),
 ("LS12", "Hillslope Transport and the Diffusion Equation", "VII", "117–122", "Soil creeps downhill at a rate proportional to the slope, so the hillslope obeys the diffusion equation and hilltops are convex.",
  ["list slope-dependent transport processes (rain-splash, tree-throw, impacts)", "derive linear flux $q=-\\kappa_h\\partial_xz$", "write and solve the hillslope diffusion equation", "state the nonlinear flux near the angle of repose"],
  'flowchart LR\n  A["slow processes:<br/>flux proportional to slope"] --> B["rain-splash: q ~ S"]\n  A --> C["bioturbation, impacts"]\n  B --> D["mass conservation"]\n  C --> D\n  D --> E["diffusion equation,<br/>convex hilltops"]'),
 ("LS13", "Landslides", "VII", "123–137", "A slope fails when driving stress exceeds the friction and cohesion resisting it; pore pressure lowers the threshold, and runout and size distributions follow.",
  ["derive infinite-slope stability with pore pressure", "distinguish loose and dense initiation", "describe size distribution and runout", "read the case studies (Kedarnath, Kerala, Mars, Moon)"],
  'flowchart LR\n  A["infinite slope: driving vs resisting"] --> B["pore pressure"]\n  B --> C["initiation: loose vs dense"]\n  C --> D["size distribution, runout"]\n  D --> E["case studies"]'),
 ("LS14", "Glaciers Mass Balance and Ice Flow", "VIII", "138–144", "A glacier is a river of ice whose size is set by accumulation against ablation and whose speed comes from viscous deformation (Glen's law) plus sliding.",
  ["write the glacier mass balance and ice flux equation", "derive deformation velocity from Glen's flow law", "describe sliding and the role of water", "read the slide figures on glacier geometry"],
  'flowchart LR\n  A["open, non-equilibrium system"] --> B["mass balance b(z)"]\n  B --> C["ice flux Q"]\n  C --> D["Glen flow law (n = 3)"]\n  D --> E["sliding, water"]'),
 ("LS15", "Glacial Deposits Rebound and Sea Level", "VIII", "145–153", "Glaciers carry debris and leave moraines; their weight depresses the crust and removal makes it rebound, and ice volume sets sea level and coral reefs record it.",
  ["describe debris on a glacier and moraines", "explain the Last Glacial Maximum imprint and Gondwana glaciations", "derive glacial isostatic adjustment", "relate ice volume to sea level and coral terraces"],
  'flowchart LR\n  A["debris, moraines"] --> B["LGM imprint, Gondwana"]\n  B --> C["isostatic adjustment"]\n  C --> D["sea level, coral reefs"]'),
 ("LS16", "Fluvial Landscapes", "IX", "(post-midsem; not in the pre-midsem slides)", "Rivers incise bedrock at a rate set by drainage area and slope (stream power), reach a graded form in alluvium, and respond to base-level change by migrating knickpoints.",
  ["write the stream-power incision law and its steady-state profile", "explain knickpoint migration", "describe alluvial channel geometry and braiding", "define base level and grade"],
  'flowchart LR\n  A["networks, discharge"] --> B["stream power: E = K A^m S^n"]\n  B --> C["knickpoints, transients"]\n  C --> D["alluvial channels, braiding"]\n  D --> E["base level, grade"]'),
 ("LS17", "Aeolian Landscapes", "IX", "(post-midsem; see also l_glacial_aolian.pdf)", "Wind moves sand in hops (saltation) above a threshold shear velocity, and the resulting dunes migrate with a speed inversely proportional to their height.",
  ["derive the threshold for saltation and the sand flux", "classify dune morphologies by wind regime", "compute dune migration rate"],
  'flowchart LR\n  A["threshold shear velocity"] --> B["saltation, sand flux"]\n  B --> C["dune morphology"]\n  C --> D["dune migration"]'),
 ("LS99", "Landscapes Practice Problems", "X", "all", "Problems that turn each chapter's results into numbers: orders of magnitude for flexure, isostasy, diffusion, glaciers and rivers.", ["solve the problems in order of the chapters", "check each answer against the stated assumptions"], 'flowchart LR\n  A["foundations"] --> B["planet, isostasy"]\n  B --> C["tectonics"]\n  C --> D["surface processes"]\n  D --> E["glaciers, rivers"]'),
]
TITLES = {c[0]: c[1] for c in CH}



EXTRA = {
"LS01": [
 (1, "Ganglas, Leh: stories behind landscapes", "Two photographs open the course. *Left:* a wide view from the Ganglas pass down to the Leh valley, the flat floor of the Indus valley with fields and the town, and behind it the snow-capped Stok–Zanskar range: a high-altitude, arid mountain landscape. *Right:* a group photograph of the LIGSS 2026 field party on the ridge. The caption sets the tone of the whole course: every landscape has a story (uplift, glaciation, rivers) that classical mechanics can read."),
 (2, "Ladakh strata and the India–Eurasia collision", "A desert ridge of tilted, light-coloured sedimentary strata dips steeply to the right: bedding rotated by collision-related folding and thrusting. The inset (Martin et al., PNAS 2020) is a tectonic map of the India–Eurasia collision zone: pink = Eurasian-affinity units, blue = Indian-affinity units, the dark line between them the Indus–Yarlung suture where the Tethys ocean closed. It links what you see in the photograph (rock tilted and folded) with the plate-scale cause (§LS08–LS10)."),
 (3, "Irshalwadi landslide", "A rocky basalt hillside in the Western Ghats (Raigad, Maharashtra) with a scar left by the July 2023 Irshalwadi landslide: bare brown rubble above, tree cover at the sides. It is the first of several landslide examples; the mechanics is in [[LS13 Landslides]] and the case studies at the end of that chapter."),
 (14, "Google-Earth tour: Himalayan glaciers", "A Google-Earth view at about 5,300 m (lat 27.97° N, lon 86.8° E, Khumbu region; the label 'Mt Everest' is cut off at the right edge): several debris-covered glacier tongues flow from the snow-covered peaks, with turquoise supraglacial and proglacial lakes. The debris cover (grey-brown) is rock that has fallen onto and out of the ice ([[LS15 Glacial Deposits Rebound and Sea Level]]). Part of the exercise set of slides 10–20."),
 (15, "Google-Earth tour: a braided river leaving the mountains", "A braided gravel-bed river (light bars separated by channels) leaves forested foothills (lat 26.69° N, lon 86.94° E, scale bar 8 km) and spreads on its fan; an abandoned meander loop (circular scar at the centre) shows channel migration. It illustrates fluxes of water and sediment and the lateral mobility of alluvial rivers ([[LS16 Fluvial Landscapes]])."),
 (16, "Google-Earth tour: the Sundarbans delta", "A tidal delta in the Bay of Bengal (lat 21.85° N, lon 89.2° E, scale 26 km): dense mangrove islands separated by branching tidal channels that widen seaward. Landscape evolving at sea level: sediment supply, tides and subsidence control its shape."),
 (17, "Google-Earth tour: a dune field", "A desert dune field: sinuous ridges with slip faces facing one direction and lighter interdune flats. The shape records the wind direction and sand supply ([[LS17 Aeolian Landscapes]]). (The coordinates on the slide are too small to read: location `[verify]`.)"),
 (18, "Google-Earth tour: Lonar crater", "A near-circular impact crater with a raised rim in Deccan basalt and a green saline lake on its floor (lat 19.98° N, lon 76.51° E), with the town of Lonar at the right. An example of a landscape made by a single instantaneous event and then modified slowly (see slide 120 on impacts and the Deccan chapter)."),
 (19, "Google-Earth exercise 2: write a story about a dynamic landscape", "Text slide. Exercise: use Google Earth to tell the story of a *dynamic* landscape in the Indian subcontinent using its tools (distance and area, elevation profile, historical imagery); discuss vertical and horizontal scales, formation and history, whether it is evolving, going up or down or shifting horizontally, the fluxes of wind, water, ice, sediment, rock, human imprint, Earth-system feedbacks and analogues on Mars or the Moon; check recent papers; Sentinel Hub is an alternative tool."),
],
"LS02": [
 (37, "Hydrostatic force balance (steady case)", "A small rectangular element of fluid (orange) between heights $z$ and $z+dz$ with the pressure $P(z)$ pushing up on its bottom face, $P(z+dz)$ pushing down on its top face and gravity $g$ acting down. With zero net force (fluid at rest) $P(z)-P(z+dz)-\\rho g\\,dz=0$, i.e. $dP/dz=-\\rho g$, the hydrostatic equation derived in this chapter and used throughout (isostasy, lithostatic pressure)."),
],
"LS03": [
 (34, "Our neighbourhood in QGIS", "Four panels from the local-landscape exercise. A QGIS window with a DEM classified in a blue–red elevation ramp (left); a contour map with hillshade (brown contour lines on grey relief, top right); and two map views of the local area (a street map and a drainage-network map with a blue lake) bottom right. The slide shows what the exercise delivers: elevation classes, contours and the stream network from one DEM ([[Landscapes and Geomorphology - Course Map]], practicals)."),
],
"LS04": [
 (31, "Mercator and transverse Mercator", "Google-Earth options (left) and the two cylindrical projections. *Top:* a cylinder wrapped around the globe, tangent along the equator: the Mercator map (right) has straight parallel meridians and parallels, preserving angles (conformal) but exaggerating area at high latitudes; the note says the change in spacing of parallels is less than the true Mercator spacing for the version shown, and the equator always touches the cylinder. *Bottom:* the transverse Mercator, the cylinder turned 90° so that it touches a chosen central meridian: a map accurate in direction, distance and area only within about 15° of the central meridian ('no straight rhumb lines'), the basis of UTM zones."),
],
"LS05": [
 (40, "Why are planets spherical?", "Title-style text slide: 'Why are planets spherical? Why are they oblate spheroids?'. The two questions are answered in §1 (gravity against strength) and §2 (rotation) of this chapter."),
 (41, "Why are planets spherical? How oblate?", "The same slide with a third question: how oblate any given planet should be, answered by the balance of centrifugal and gravitational force at the equator ($f\\approx\\omega^2R^3/(GM)\\cdot\\tfrac52$ for a uniform fluid body)."),
 (43, "Earth's oblateness to scale", "A quarter-outline of the Earth (Wikipedia 'Figure of the Earth': *Earth oblateness to scale*). The yellow circle is a perfect sphere, the pink line the true ellipsoid: at this scale (flattening ≈ 1/298) the two are practically indistinguishable, which is why the oblateness is a small perturbation. The slide also gives references on the history of measuring the Earth's shape and the recommended book (Chandrasekhar's *Newton's Principia for the Common Reader*)."),
],
"LS06": [
 (52, "Friction and cohesion: the strength of rock", "*Left:* a block of weight (normal stress $\\sigma$) sliding on a surface under shear stress $\\tau$; the resistance is friction $\\mu\\sigma$ plus cohesion $C$: $\\tau=\\mu N+C$. *Right:* Turcotte & Schubert Fig. 6.7 (Byerlee 1977): the maximum shear stress to start sliding against normal stress, for many rock types and pressures (log–log scatter): all points follow one line, $\\tau_{\\max}\\approx0.85\\,\\sigma$: **Byerlee's law**, a universal friction coefficient $\\mu\\approx0.85$ (with a cohesion offset at high stress). It is the strength used for the maximum-topography estimate of this chapter."),
],
"LS08": [
 (72, "Rayleigh–Bénard convection and the mantle Rayleigh number", "*Left:* the Rayleigh number as the ratio of buoyancy to viscous resistance: $Ra=\\rho g\\alpha\\Delta T h^3/(\\mu\\kappa)=(\\Delta\\rho\\,g/\\mu)\\times h^2/(\\kappa/h)$ (buoyant force × time to diffuse across the cell, over viscous force), with the mantle numbers $\\rho\\sim10^3$, $g\\sim10$, $\\alpha\\sim10^{-5}$, $\\Delta T\\sim10^3$, $h\\sim10^6$ m, $\\mu\\sim10^{20}$ Pa s, $\\kappa\\sim10^{-6}$ m² s$^{-1}$ giving $Ra_{\\rm mantle}\\sim10^6\\gg Ra_{\\rm crit}\\sim10^3$: **the mantle convects vigorously**. *Top right:* a laboratory convection pattern (hexagonal cells in a heated fluid layer). *Bottom right:* the world map of plate motions (arrows) as the surface expression."),
],
"LS10": [
 (78, "Passive-margin escarpments", "*Left:* a world map with passive-margin escarpments (stretching) marked; *right:* a relief map of the Indian west coast (the Western Ghats escarpment above a narrow coastal strip). The text: rifting thins the continental crust and gives normal faulting (McKenzie and Sclater 1971); present-day topography is the sum of past tectonics and continuing sub-aerial processes driven mainly by rivers and hillslopes (Summerfield 1991)."),
 (80, "Compression and folding (Turcotte & Schubert)", "*Left:* (a) compression of a uniform medium shortens it without folding; (b) a layered medium with a strong (competent) layer in a weak matrix buckles into folds whose wavelength is set by the strong layer. *Right:* log–log plot of fold wavelength $\\lambda$ against the thickness $h$ of the dominant member (Currie et al. 1962): data over six orders of magnitude lie on a line of slope 1, $\\lambda\\propto h$ (the fitted constant is about 30). Folds are sinusoidal at small amplitude and scale with the strong layer's thickness."),
],
"LS09": [
 (87, "Strike-slip faults and the San Andreas record (Anderson & Anderson)", "*Left:* a block diagram of a right-lateral strike-slip (transform) fault with the National Park Service explanation; centre-top a hillshade of a fault trace with offset streams; *centre:* Fig. 4.11 (Wallace Creek): a stream channel is offset by successive earthquakes, so the total offset divided by the age of the channel gives the long-term slip rate $D/T_1$; *right:* the palaeoseismic record of the San Andreas fault (dates of past earthquakes against number of earthquakes before the 1857 Fort Tejon event) with an average recurrence interval of order 150 years."),
 (92, "Uplift in the Himalaya over $10^2$–$10^4$ years", "*Left:* river terraces (labelled T2–T6) along a Himalayan river, each a former river bed abandoned as the river incised into rising ground; *right:* (a) terrace elevation against distance from the Main Frontal Thrust (MFT), (b) the inferred uplift rate in mm/yr against distance, peaking where the active fold crests, (c) the cross-section of the frontal fold above the thrust ramp with a convergence rate of about 21.5 mm/yr taken up by the thrust (A&A Fig. 4.26)."),
 (94, "Himalayan great earthquakes and 'aseismic creep'", "A map of the Himalayan arc (A&A Fig. 4.21) with the rupture segments of historical great earthquakes drawn as yellow strips with magnitudes (8.0–8.6) and years (1505, 1803, 1833, 1897, 1905, 1934, 1950...), cities as circles scaled by population (Kabul, Islamabad, Delhi, Dhaka, Kolkata, Bhuj). The title question asks whether the gaps between ruptures are 'aseismic creep' or locked segments that will break (a seismic hazard for tens of millions of people)."),
],
"LS11": [
 (98, "Soil production rate depends on soil thickness", "(a, b) Measured soil production rate (mm per thousand years) against soil depth (cm): production falls as the soil thickens, because a thick soil shields the rock from water and roots (A&A Figs 7.33–34). *Right:* the conceptual humped function: mobile regolith production rate against thickness $H$: zero for bare rock, rising to a maximum at a thin soil (water is retained at the bedrock interface) and falling at large thickness. The decay, $\\dot W=\\dot W_0e^{-H/H_0}$ is used in the regolith-thickness derivation of this chapter."),
],
"LS13": [
 (125, "USGS flume experiment: loose and dense soil", "*Left:* the 95-m-long steep flume at the USGS in Oregon with a debris-flow experiment on 13 Sept 2001. *Right:* (a) loose soil (porosity 0.52): displacement and pore-water pressure head against time: after about 48 minutes of wetting the pressure builds and, within seconds, the slope fails suddenly and catastrophically (displacement jumps); (b) dense soil (porosity 0.41): over four hours the displacement creeps up gradually and the pressure head stays low. Loose soil contracts when sheared, raising pore pressure and liquefying; dense soil dilates and drains. (A&A Fig. 10.30)"),
 (127, "Landslide Atlas of India", "*Left:* NRSC map of India with the landslide inventory 1998–2022 (yellow): clusters in the NW and NE Himalaya and the Western Ghats. *Right:* three news items: the Taliye (Raigad) landslide of July 2021 (49 dead), the Irshalwadi landslide (2023), and the Malin (Pune) landslide of 2014, a mass-fatality mudslide: why landslides matter in India."),
 (128, "Irshalwadi landslide: satellite view", "A satellite image of the hillside above the village after the July 2023 failure: a long, narrow debris track running down a forested basalt slope and spreading into a fan of debris below."),
 (129, "Irshalwadi landslide: the source catchment", "A second Google-Earth view of the same hillside (terraced basalt slopes, forest and cleared land) with the village location marked at the left: the slope above is the source of the debris flow."),
 (130, "Dharali disaster, Uttarakhand, 5 August 2025", "False-colour Sentinel-2 imagery before and after the event (red = vegetation): pre-event (left) shows the settlement of Dharali beside the stream; post-event shows the debris-flow track, deposit and the inundated settlement. *Right:* two high-resolution images (13 June 2024 and 7 Aug 2025) with Dharali circled. The slide points to the Landslide Blog article for the cause (a flood/debris flow from the tributary catchment)."),
 (131, "Chamoli flash flood, Feb 2021 (Ronti Gad, Tapovan)", "Ten video frames (A–J) with times in IST (≈10:30 on 7 Feb 2021) from $t_0+14$ s to $t_0+57$ s: a dust and debris cloud rushes down the Ronti Gad valley and across the Tapovan dam: the rock–ice avalanche from the slope above transformed into a flash flood. The slide cites Shugar et al., *Science* 2021 for the detailed reconstruction."),
 (132, "Chamoli rock–ice avalanche: source and path", "Figures from Shugar et al. (*Science* 2021): a 3-D view of the Ronti peak slope that failed; satellite images before/after (E, F show the cross-section of the detached rock-and-glacier-ice block); elevation-change profiles along the path (G–J) showing the thickness removed from the source and deposited below. The orange label gives the source volume of order $2.7\\times10^7$ m³ (`[verify]` the exponent)."),
 (133, "Massive debris flows and rock avalanches (A&A Figs 10.34, 10.36)", "Examples of very large mass movements: an oblique aerial photo of a lobate rock-avalanche deposit spreading across a desert valley floor (bottom left), a grey-scale view of another long-runout deposit (top left), and Google-Earth views of glacier-covered terrain with debris sheets (right). They show how the runout of large landslides greatly exceeds the fall height."),
 (134, "A giant prehistoric rock avalanche near Pokhara, Nepal", "A map from a *Nature* paper on dated deposits of a huge prehistoric rock avalanche in the Pokhara valley (carbonate-rich Tethyan Himalaya above, High Himalayan gneisses and Lesser Himalayan metasediments below; symbols mark exposure-age, luminescence and radiocarbon samples; the deposits are mapped in yellow and green: breccia, conglomerate, terrace deposits). The orange note dates the event to about 1200 AD and speculates its size might have removed a summit from the list of 8000-m peaks (`[verify]` against the paper)."),
 (135, "Landslides triggered by the 2015 Gorkha earthquake (Roback et al. 2018)", "Fig. 1 of the study: a satellite image of central Nepal with the mapped area (blue outline), the landslides (yellow) and obscured areas (purple), the epicentres of the 25 April (M7.8) and 12 May (M7.3) shocks, and Kathmandu, Barpak, Bhote Koshi and Langtang marked; (B) the inventory over topography; (C) before/after imagery near Barpak showing coseismic landslide scars."),
 (136, "Landslide statistics", "(A) Probability density of landslide area on log–log axes: a power-law tail with a rollover at small areas, fitted by $\\log p=-2.47+0.11\\log A-\\dots$ with a slope near $-2.5$ for large landslides. (B) Slope histograms: landslide source slopes (mean $39.5\\pm9.1^\\circ$) against all hillslopes ($27.5\\pm13.7^\\circ$): failures preferentially occur on steeper slopes. (C) Runout length against landslide volume: runout grows with volume and debris flows run farther than ordinary landslides."),
 (137, "25,000 landslides and the ground motion (Gorkha 2015)", "Map of landslide density across central Nepal against average horizontal peak ground velocity (colour scale 0–70 cm/s), with the April 25 epicentre and the 12 May shock, the main thrusts and a shaded fault-plane projection; (c) landslide counts along a profile away from the epicentre show three peaks: failures correlate with shaking intensity and also with topography (Geophys. Res. Lett. 2022)."),
],
"LS14": [
 (144, "Ice flow: viscous deformation plus sliding", "*Top left:* Newtonian viscous flow over an inclined plane: $dU/dz=\\rho g\\sin\\theta\\,(H-z)/\\mu$ with parabolic profile $U(z)=(\\rho g\\sin\\theta/\\mu)(Hz-z^2/2)$ (A&A Eq. 8.8). *Below:* ice differs because it follows a power law with $n\\approx3$ (Glen): $dU/dz=A\\tau^n$, giving $U(z)=A[\\rho g\\sin\\theta]^3[H^3z-\\tfrac32z^2H^2+z^3H-\\tfrac14z^4]$ (Eq. 8.16). *Right:* the sketch of an ice slab of thickness $H$ and width $w$ over planar bedrock with the velocity profile $u(z)$ made of a sliding part $U_s$ at the bed plus the deformation part $U_{\\rm def}$, and the flux $Q_x$ into and out of the element (A&A Fig. 8.7)."),
],
"LS15": [
 (145, "Deposition by glaciers: where does a fallen rock go?", "Question slide: *what happens to a piece of rock (or a glaciologist) that falls onto the glacier in the accumulation zone?* The sketch is a glacier outline with the equilibrium-line altitude (ELA) drawn across it. Answer: in the accumulation zone snow buries the rock; ice flows down and, because the flow lines dive in the accumulation zone and rise towards the surface in the ablation zone, the rock is carried englacially and re-emerges below the ELA, where it melts out and joins the surface debris (moraines)."),
],
}


def extra_block(code):
    items = EXTRA.get(code, [])
    if not items:
        return ""
    out = ["\n\n## Further slides explained one by one\n<span class=\"scope-taught\">taught</span> *the slides of this chapter's range that carry no derivation of their own; each image is followed by what it shows*\n"]
    for n, ttl, txt in items:
        out.append(f"\n![[pre_{n:03d}.jpg|520]]\n\n> [!example] 🖼 Reading the diagram: Slide {n}: {ttl}\n> {txt}\n")
    return "".join(out)


def link(code):
    return "[[%s %s]]" % (code, TITLES[code])


# front matter note
fb = open(os.path.join(BODY, "LS00.md.body")).read().strip()
fb = re.sub(r"\n> \[!figure\]- [^\n]*\n> [^\n]*\n", "\n", fb)
open(os.path.join(OUT, "Landscapes Notation and Glossary.md"), "w").write("""---
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

""" + fb + "\n")
print("LS00 written")

for i, (code, title, part, slides, story, abil, mer) in enumerate(CH):
    body = open(os.path.join(BODY, code + ".md.body")).read().strip()
    prev = link(CH[i - 1][0]) if i > 0 else "[[Landscapes and Geomorphology - Course Map|Course Map]]"
    nxt = link(CH[i + 1][0]) if i < len(CH) - 1 else "(end)"
    nsec = len(re.findall(r"^## ", body, re.M))
    nder = body.count("[!derivation]")
    nfig = len(re.findall(r"!\[\[ls_fig", body))
    nsl = len(set(re.findall(r"pre_(\d{3})\.jpg", body)))
    fm = f"""---
title: {code} {title}
aliases: [{code}, {title}]
subject: landscapes
type: chapter
chapter: {int(code[2:]) if code != 'LS99' else 99}
part: {part}
scope: [taught, extra-book, extra-beyond]
by: [slides, ai-notes, book]
status: draft
tags: [subject/landscapes, type/chapter, taught, extra/book, extra/beyond, src/slides, src/ai-notes, src/book, status/draft]
---
# {code} · {title}

◀ {prev} · [[Landscapes and Geomorphology - Course Map|Course Map]] · next: {nxt}

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught**: slides {slides} of [[pre_ms_landscape_26.pdf|the EC2123 pre-midsem deck]] (Argha Banerjee, IISER Pune; 153 slides). Boxes marked 🟢 **In the slides** derive what the slides derive; boxes marked 🖼 **Reading the diagram** explain each slide figure panel by panel and sit directly under the slide image.
> 🔵 **Extra · beyond**: boxes marked 🔵 **Extra** complete derivations the slides only quote (from Anderson and Anderson, *Geomorphology: the Mechanics and Chemistry of Landscapes*, and Turcotte and Schubert, *Geodynamics*); 🛠 **Tool** boxes derive a mathematical tool from 12th-grade material; 🧮 **Worked example** boxes calibrate orders of magnitude.
> This chapter has {nsec} sections, {nder} derivation boxes, {nfig} redrawn figures and {nsl} slide images.

> [!key] After this chapter you can
{chr(10).join('> - ' + a + ',' for a in abil).rstrip(',')}.

> [!intuition] The one-sentence story
> {story}

```mermaid
{mer}
```
*Concept map: every box is a section of this chapter.*

"""
    tail = f"""

## Map of this chapter
> [!connection] How {code} connects
> **Previous:** {prev} · **Next:** {nxt}.
> **Other subjects:** [[Climate - Course Map]] (weathering and the carbon cycle, glaciation, orographic rainfall), [[Thermodynamics - Course Map]] (heat conduction and diffusion), [[Evolution of Earth and Life - Course Map]] (plate tectonics and landscapes through geological time), [[Waves - Course Map]] (diffusion and wave equations).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | slide content, figures read panel by panel | [[pre_ms_landscape_26.pdf]] slides {slides} (images embedded from the PDF, auto-cropped, `scripts/render_slides.py`) | taught |
> | derivations, worked examples, tool boxes, TikZ figures | the AI-written derivation-level notes [[Landscapes_and_Their_Evolution_notes.pdf]] (EC2123 notes; LaTeX source in `landscape-notes-tex-source.tar.gz`), converted with `scripts/tex2vault_ls.py`; cross-checked against Anderson and Anderson and Turcotte and Schubert as cited there | secondary + extra/book |
>
> **Notes.** (1) The text of this chapter is the AI-written reference notes' text, converted to the vault's callout style and equation numbering (chapter-local, so some cross-references read as "(label)"). (2) The slide images were checked against the notes' slide numbers for a sample of slides (e.g. 1–12, 109–120 match). Figure descriptions are the notes', and should be compared with the images beside them. (3) The `[!verify]` items of the notes' last front-matter section ("Two places where the slides need care") are in [[Landscapes Notation and Glossary]].
"""
    open(os.path.join(OUT, f"{code} {title}.md"), "w").write(fm + body + extra_block(code) + tail)
    print(code, title)
