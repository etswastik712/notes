# O4: The ocean's ledger · O4 · Nansen's answer

(34 frames, 120 elements; deck file lectures/ocean-ledger-o4/index.html)

## Frame 1: Why we are here  [fr_3]
NOTES: O4 · NANSEN'S ANSWER: WHAT THE WIND DOES TO A ROTATING OCEAN (Wed 11 Nov, 50 min). Opening (≈1 min, Smooth). Where we left the heat budget. The net heat flux into the ocean, 2011 (ocean reanalysis): the map from last week. The accountant and the data scientist have done their jobs: the ocean gains heat where it is cold (the cold tongue, Somalia and Oman).
  TEXT: Still open: the ocean gains heat where it is cold
  TEXT: The heat budget, as we left it last week
  TEXT: Data scientist’s hat · heat budget
  FIGURES: f_heating.svg, k_heating.svg

## Frame 2: Three hats, twice  [fr_9]
NOTES: (≈1 min, Smooth.) O1's three hats. For the heat budget we have worn the accountant's (which budget?) and the data scientist's (what does it look like?). Today is the physicist's: why does it gain heat where it is cold? Because cold water keeps arriving from below.
  TEXT: Where we are
  FIGURES: hats_heat.svg

## Frame 3: A new budget  [fr_12]
NOTES: Hold: but water can only arrive if it moves, and what moves it is a momentum budget. So the physicist's question about heat opens a new ledger, with its own three hats. Accountant: the wind's stress goes in; where does it go? Data scientist: maps of the stress, the sea height, the currents. Physicist: Coriolis and geostrophy. Labels in the corner of later slides say which hat we have on.
  TEXT: Where we are
  FIGURES: hats_heat.svg, hats_mom.svg

## Frame 4: Week 3: Nansen's question  [fr_14]
NOTES: Beat 1 (≈2 min, Cut). Not a recap: this is where last lecture stopped.
- Nansen, on the Fram (1893-96), saw the Arctic ice drift 20-40° to the right of the wind (Stewart §9.2). He asked Bjerknes to set a student on it; Ekman's answer came in 1905.
- Last lecture: the wind's push alone would take ~60 days to bring a 50 m layer to wind speed. It never gets there: rotation stops it first. Today: how.
  TEXT: Nansen’s question
  TEXT: The ice drifted 20–40° to the right of the wind.
  TEXT: Why to the right? And why not straight downwind?
  TEXT: Today: the answer, and what it does to the whole upper ocean.
  FIGURES: ekman_ice.svg

## Frame 5: A free-body diagram?  [fr_20]
NOTES: (≈1 min, Smooth.) The natural first move, and Nansen's own: three forces on the ice, wind W, friction F opposite its motion, Coriolis C at right angles to it, and W + F + C = 0 for steady motion (Stewart §9.2, Fig 9.2; this drawing is ours, to scale for 30°). It even gets the side right.
  TEXT: Physicist’s hat · momentum budget
  TEXT: A free-body diagram?
  TEXT: The natural first move, and Nansen’s own: wind, friction and Coriolis on the ice must balance.
  TEXT: It even gets the side right: the ice veers to the right of the wind.
  FIGURES: ice_fbd.svg

## Frame 6: Why the analogy breaks  [fr_26]
NOTES: Hold: why this picture misleads (our argument). The friction on the ice comes from the water under it, and what that water is doing is the thing we don't know, so the diagram hands the problem on to the water. And the object is the wrong size: a floe is a few metres thick, on tens of metres of stirred water spread over thousands of kilometres. Most of the mass that feels Coriolis is water.
  TEXT: Physicist’s hat · momentum budget
  TEXT: The analogy breaks
  TEXT: The friction comes from the water, and what the water is doing is exactly what we don’t know.
  TEXT: A few metres of ice ride on tens of metres of water.
  FIGURES: ice_layer.svg

## Frame 7: A passive tracer  [fr_31]
NOTES: Hold: so go to larger scales: a budget for the whole layer, over a region far bigger than any floe. Treat the ice as a passive tracer: a marker on the water that shows us what the top of the layer is doing.
- Caveat if asked: ice isn't strictly passive. The wind pushes on it directly, and Nansen's diagram has that force in it; sea-ice models keep a force balance for the ice. "Passive tracer" is the right first picture because the turning comes from the water beneath it, not because the other forces vanish.
  TEXT: Physicist’s hat · momentum budget
  TEXT: The analogy breaks
  TEXT: The friction comes from the water, and what the water is doing is exactly what we don’t know.
  TEXT: A few metres of ice ride on tens of metres of water.
  TEXT: So go to larger scales: a budget for the whole layer. Treat the ice as a passive tracer: it shows us what the water is doing.
  FIGURES: ice_layer.svg

## Frame 8: Add up the whole layer  [fr_33]
NOTES: Beat 2 (≈12 min, Smooth). Can be done on the board instead; the slide then is a summary.
- Start from Suhas's rotating-frame momentum equations. Steady (no acceleration), no pressure gradient (the sea surface is flat for now). What's left: Coriolis against friction. Friction here is the vertical change of the horizontal stress τ that turbulence carries down from the wind.
- x: −f v = (1/ρ) ∂τˣ/∂z. y: f u = (1/ρ) ∂τʸ/∂z. Each thin slab of water: Coriolis on it balances the difference between the stress on its top and on its bottom.
- Sign check: u east, v north, z up; f > 0 in the north.
- The accountant's hat: this is a momentum budget for a box. And the box is the mixed layer from the last two lectures: the same wind that stirs it passes the stress down, and the stress dies out where the stratification stops the stirring (O3 §2). The Ekman depth of the theory and the observed mixed-layer depth are different numbers; what matters here is only that the stress is gone below the stirred water.
  TEXT: Accountant’s hat · momentum budget
  TEXT: Add up the whole stirred layer: the mixed layer again
  TEXT: Steady, and the sea surface flat: only Coriolis and the stress are left.
  FIGURES: ek_layer.svg, eq_ek_mom.svg

## Frame 9: Integrate over the layer  [fr_40]
NOTES: Hold: integrate both from below the stirred layer, where τ = 0, to the surface, where τ is the wind's stress. ∫ ∂τ/∂z dz = τ(top) − τ(bottom) = wind stress − 0.
- M = ∫ u dz is the transport: cubic metres per second through a strip one metre wide, from the surface to below the layer (Stewart §9.3 uses the mass transport, ρ × this; same thing).
- Only the two ends of the integral are left, and we know both.
  TEXT: Accountant’s hat · momentum budget
  TEXT: Add up the whole stirred layer: the mixed layer again
  FIGURES: ek_layer.svg, eq_ek_mom.svg, eq_ek_int.svg

## Frame 10: 90 degrees to the right  [fr_42]
NOTES: Hold: the answer. M_y = −τˣ/(ρf), M_x = τʸ/(ρf) (Stewart eq. 9.26; Hartmann §7.5.1).
- Wind to the east (τˣ > 0): transport to the south, M_y < 0. 90° to the right of the wind in the north.
- South of the equator f < 0, so it's 90° to the left.
  TEXT: Physicist’s hat · momentum budget
  TEXT: Add up the whole stirred layer: the mixed layer again
  FIGURES: ek_layer.svg, eq_ek_mom.svg, eq_ek_int.svg, eq_ek_res.svg

## Frame 11: Only the top counts  [fr_44]
NOTES: Hold: the punchline. We never said how turbulence carries the stress down: eddy viscosity, breaking waves, convection. The answer doesn't care. Only the stress at the top and the fact that it dies out below. That's why Ekman transport is robust while the details of the current inside the layer are not (Stewart §9.3: transports are "much more robust" than velocities in the layer).
  TEXT: Physicist’s hat · momentum budget
  TEXT: Add up the whole stirred layer: the mixed layer again
  TEXT: It doesn’t matter how the turbulence passes the push down. Only the push at the top counts.
  FIGURES: ek_layer.svg, eq_ek_mom.svg, eq_ek_int.svg, eq_ek_res.svg

## Frame 12: How much water?  [fr_46]
NOTES: Beat 3 (≈3 min, Smooth). The same answer as a force balance on the whole layer: two forces on it, the wind's stress along the wind and Coriolis at 90° to its motion. They can only cancel if it moves 90° to the right of the wind. Note the object: the layer, not a floe. This diagram is the budget redrawn, so it is safe where the ice's wasn't.
- Size: τ = 0.1 N/m², ρ = 1025 kg/m³, f = 10⁻⁴ s⁻¹ (about 43°): M = 0.98 m²/s (✓). Over a 50 m layer that's ~2 cm/s.
  TEXT: How much water?
  TEXT: As forces on the layer: the wind’s push and Coriolis cancel only if it moves 90° to the right.
  TEXT: τ = 0.1 N/m², f = 10⁻⁴ s⁻¹: / τ / ρf ≈ 1 m²/s / About a cubic metre a second through each metre of width. Over a 50 m mixed layer, just 2 cm/s.
  FIGURES: ekman_force.svg

## Frame 13: Measured  [fr_51]
NOTES: Hold: does the ocean agree? Chereskin & Roemmich (1991), across 11°N in the Atlantic: 12.0 ± 5.5 Sv northward measured with a ship's current profiler, against 8.8 ± 1.9 Sv from the winds measured at the time using τ/(ρf), and 13.5 ± 0.3 Sv from long-term mean winds (Stewart §9.3, p. 144). Agreement within the errors.
  TEXT: How much water?
  TEXT: As forces on the layer: the wind’s push and Coriolis cancel only if it moves 90° to the right.
  TEXT: τ = 0.1 N/m², f = 10⁻⁴ s⁻¹: / τ / ρf ≈ 1 m²/s / About a cubic metre a second through each metre of width. Over a 50 m mixed layer, just 2 cm/s.
  TEXT: Measured: across 11°N in the Atlantic, the current and the wind give the same transport, within the errors.
  FIGURES: ekman_force.svg

## Frame 14: Ekman's spiral  [fr_53]
NOTES: Beat 4 (≈7 min, Smooth). What happens inside the layer depends on how the turbulence works. Ekman (1905) assumed the simplest thing: a constant eddy viscosity. Then the surface current is 45° to the right of the wind, and below it the current weakens exponentially and turns further right: a spiral (Stewart §9.2, Fig 9.3). Drawn from his solution; the form is in the notes, no algebra on screen.
- Ekman depth (where the current has reversed): typically 45-300 m, more for strong winds and low latitudes (Stewart Table 9.3, from his eq. 9.16; ✓ 45-299 m). There the speed is e^−π ≈ 4% of the surface's.
- Back to the mixed layer: the Arabian Sea's went from 20 m in April to 62 m in July (O3). The spiral's depth is set by an assumed viscosity and takes no notice of stratification, which is one more reason to trust the total and not the spiral.
  TEXT: Inside the layer
  TEXT: Ekman (1905) took the simplest turbulence: a constant viscosity.
  TEXT: The surface water goes 45° right of the wind. Deeper, it is slower and turned further: a spiral, gone within 45–300 m.
  FIGURES: ekman_spiral.svg

## Frame 15: Add up the arrows  [fr_58]
NOTES: Hold: add up the arrows (the area under the spiral, as vectors): exactly 90° to the right, the same as the integral, whatever the viscosity. The spiral depends on the turbulence; the total doesn't.
  TEXT: Inside the layer
  TEXT: Ekman (1905) took the simplest turbulence: a constant viscosity.
  TEXT: The surface water goes 45° right of the wind. Deeper, it is slower and turned further: a spiral, gone within 45–300 m.
  TEXT: Add the arrows up: 90°. The spiral depends on the turbulence. The total doesn’t.
  FIGURES: ekman_spiral.svg, ekman_spiral_net.svg

## Frame 16: Why 20 to 40 degrees?  [fr_61]
NOTES: Hold: so why did Nansen see 20-40° and not 90°? The ice is a tracer of the very top of the layer, so it shows the surface angle, not the 90° of the whole layer. Why not exactly 45°? Real turbulence isn't a constant viscosity, and the ice isn't quite passive: the wind pushes on it directly as well (Stewart §9.2). Clean spirals are hard to see in measurements; the transport is easy to see (Stewart §9.2-9.3).
  TEXT: Inside the layer
  TEXT: Ekman (1905) took the simplest turbulence: a constant viscosity.
  TEXT: The surface water goes 45° right of the wind. Deeper, it is slower and turned further: a spiral, gone within 45–300 m.
  TEXT: Add the arrows up: 90°. The spiral depends on the turbulence. The total doesn’t.
  TEXT: Nansen’s 20–40°: the ice marks the very top of the layer, so it shows the surface angle, not the total.
  FIGURES: ekman_spiral.svg, ekman_spiral_net.svg

## Frame 17: Spreading apart, piling up  [fr_63]
NOTES: Beat 5 (≈10 min, Smooth). If the wind is the same everywhere, the transport is the same everywhere: water arrives as fast as it leaves. But the wind changes from place to place. Where more leaves than arrives, water has to come up from below; where more arrives than leaves, it has to go down. Mass conservation: Ekman pumping.
  TEXT: Ekman pumping
  TEXT: If the wind changes from place to place, so does the transport.
  TEXT: Where more water leaves than arrives, it is replaced from below the mixed layer. Where more arrives, it is pushed down.
  FIGURES: ekman_pump.svg

## Frame 18: How fast?  [fr_68]
NOTES: Hold: how fast, as an order of magnitude (our sum). The stress changes by 0.1 N/m² over 1,500 km (trades to westerlies): the transport changes by 0.1/(ρf) ≈ 1 m²/s over that distance, so w ≈ 0.1/(1025 × 10⁻⁴ × 1.5 × 10⁶) ≈ 6.5 × 10⁻⁷ m/s ≈ 21 m a year (✓). In general w = curl(τ/ρf) (Stewart eq. 9.29; Hartmann eq. 7.11).
- Tiny as a speed, but it goes on all year, every year, over whole ocean basins.
  TEXT: Ekman pumping
  TEXT: If the wind changes from place to place, so does the transport.
  TEXT: Where more water leaves than arrives, it is replaced from below the mixed layer. Where more arrives, it is pushed down.
  TEXT: 0.1 N/m² of change over 1,500 km: / w ≈ 20 m a year
  TEXT: Slow, but all year, every year, across whole basins.
  FIGURES: ekman_pump.svg

## Frame 19: The wind's push  [fr_71]
NOTES: Back to the map (Smooth). Last lecture's wind stress, 2011 mean (ocean reanalysis). Look where it changes: trades to westerlies, across the Southern Ocean's belt.
  TEXT: The wind’s push changes from place to place
  TEXT: So the water it moves sideways spreads apart in some places and piles up in others
  TEXT: Data scientist’s hat · momentum budget
  FIGURES: f_tau.svg, k_tau.svg

## Frame 20: Ekman pumping map  [fr_77]
NOTES: Hold: w = curl(τ/ρf) from that stress (2011 annual mean, 3.5° box smoothing; blank within 5° of the equator, where f → 0, and next to coasts).
- Subtropical gyres: pushed down ~35 m/yr (N Pacific), ~30 (N Atlantic), ~25 (S Pacific). Subpolar N Pacific: pulled up ~15. Southern Ocean 50-62°S: pulled up ~25 (box means, ✓).
- Not on this map: upwelling right at a coast (a wall, not a curl; Hartmann p. 219) and at the equator (masked). Next.
  TEXT: So water is pulled up or pushed down: tens of metres a year
  TEXT: Ekman pumping from the 2011 wind stress. Blank near the equator and at the coasts, where this sum doesn’t apply.
  TEXT: subpolar: up
  TEXT: subtropics: down ~35 m/yr
  TEXT: Southern Ocean: up ~25 m/yr
  TEXT: Data scientist’s hat · momentum budget
  FIGURES: f_wek.svg, land_grey.svg, k_wek.svg

## Frame 21: At a coast  [fr_86]
NOTES: Three places, a picture each (students have read these in O3's notes; ~1 min each). Coast (Snappy into the section): the monsoon blows along the Somali coast; transport is to its right, offshore; the water is replaced from below. Same recipe off Oman, Peru (SH: to the left, still offshore) and California. The world's great fisheries.
  TEXT: At a coast
  TEXT: Wind along the coast, transport offshore, water from below. Somalia and Oman in the monsoon; Peru; California.
  FIGURES: up_coast.svg

## Frame 22: At the equator  [fr_90]
NOTES: Equator (Snappy): f changes sign. Under the trades the transport is to the right just north of the equator and to the left just south: away from the equator on both sides. Cold water rises: the cold tongue, which gains heat because cold water keeps arriving (O3's puzzle). This year's El Niño: weaker trades, weaker upwelling (CPC; check the November discussion, due ~12 Nov).
  TEXT: At the equator
  TEXT: Coriolis changes sign. Under the trades, water goes away from the equator on both sides, and cold water rises: the cold tongue.
  FIGURES: up_eq.svg

## Frame 23: The slab gets a new term  [fr_94]
NOTES: (≈1 min, Smooth.) Back to the mixed-layer slab of the last two lectures, C dT/dt = what crosses the surface. It only stored heat; no water went anywhere. At a coast or the equator that fails: cold water from below the mixed layer keeps entering it, and the surface has to warm that water. So the slab's heat budget needs a term for water moving through it.
  TEXT: Physicist’s hat · heat budget
  TEXT: The slab’s new term
  TEXT: Last week’s mixed-layer slab only stored heat. No water moved.
  TEXT: Now cold water keeps arriving from below the mixed layer, and the surface has to warm it.
  FIGURES: slab_term.svg

## Frame 24: The puzzle, answered  [fr_100]
NOTES: (≈1 min, Smooth.) The same map we opened with. The ocean gains heat where it is cold because cold water keeps arriving: wind stress → Ekman transport → water from below the mixed layer. The physicist's answer to the heat budget's question, and it took a momentum budget to get there.
  TEXT: It gains heat where it is cold because cold water keeps arriving
  TEXT: The heat budget’s question, answered by the momentum budget
  TEXT: Somalia, Oman: a coast
  TEXT: cold tongue: the equator
  TEXT: Physicist’s hat · heat budget
  FIGURES: f_heating.svg, k_heating.svg

## Frame 25: In the subtropics  [fr_108]
NOTES: Subtropics (Smooth): poleward transport under the trades, equatorward under the westerlies. They meet near 30°: the water piles up and is pushed down (the orange on the pumping map). A hill of water, about a metre high.
  TEXT: In the subtropics
  TEXT: Under the trades, water goes poleward. Under the westerlies, equatorward. Where they meet it piles up and is pushed down.
  TEXT: On a turning Earth, water runs around a hill, not down it. That should bother you.
  FIGURES: hill.svg

## Frame 26: Water on a hill  [fr_113]
NOTES: (≈1 min, Smooth.) The physicist's hat. A hill in the sea surface means higher pressure under it than beside it, so there is a horizontal force pushing the water downhill. Ask the class what the water should do. Everything we know from pouring water says: run down, and the hill flattens.
  TEXT: Physicist’s hat · momentum budget
  TEXT: Water on a hill
  TEXT: A slope in the sea surface is a pressure push downhill.
  TEXT: Every instinct says the water runs down and the hill flattens.
  FIGURES: geo_hill.svg, geo_push.svg

## Frame 27: It turns  [fr_120]
NOTES: Hold: as soon as the water moves, Coriolis acts to the right of its motion. It keeps turning until the Coriolis force exactly opposes the pressure force, which can only happen when it runs along the contours. Suhas's wind around a high, in water. (The drawing is a schematic: real adjustment overshoots and oscillates about the balance.)
  TEXT: Physicist’s hat · momentum budget
  TEXT: Water on a hill
  TEXT: But the moment it moves, Coriolis turns it to the right.
  TEXT: It keeps turning until it is running along the hill.
  FIGURES: geo_hill.svg, geo_turn.svg

## Frame 28: At right angles to the push  [fr_124]
NOTES: Hold: the counterintuitive part, stated plainly. The water flows perpendicular to the pressure gradient that is pushing on it, with the high side on its right in the north. Pressure pushes out, Coriolis pushes in, they cancel, and the water keeps going round. Nothing flows downhill, so the hill doesn't flatten. This holds to about one part in a thousand for flows larger than about 50 km and longer than a few days (Stewart p. 152). Geostrophic: u = −(1/fρ) ∂p/∂y, v = (1/fρ) ∂p/∂x (Stewart eq. 10.7a).
  TEXT: Physicist’s hat · momentum budget
  TEXT: At right angles
  TEXT: The water flows perpendicular to the force pushing it. Pressure pushes out, Coriolis pushes in.
  TEXT: Nothing runs downhill, so the hill stays up.
  FIGURES: geo_hill.svg, geo_bal.svg

## Frame 29: Same form as Ekman  [fr_129]
NOTES: Hold: the same form as the layer's budget earlier. Ekman: Coriolis against the stress, motion at 90° to the wind. Geostrophy: Coriolis against the pressure slope, motion at 90° to the push. Surface speed = (g/f) × slope (Stewart eq. 10.10). A 1 m hill over 1,500 km: 9.8/10⁻⁴ × 1/(1.5 × 10⁶) ≈ 7 cm/s (our sum, ✓). Stewart's 1 m per 100 km, "typical of strong currents": ≈ 1 m/s (Fig 10.2, ✓). Steep slopes mean fast currents, which is why the fast flow is narrow.
  TEXT: Physicist’s hat · momentum budget
  TEXT: At right angles
  TEXT: The water flows perpendicular to the force pushing it. Pressure pushes out, Coriolis pushes in.
  TEXT: Nothing runs downhill, so the hill stays up.
  TEXT: Same form as Ekman: motion at 90° to the push.
  TEXT: 1 m over 1,500 km: ≈ 7 cm/s. / 1 m over 100 km: ≈ 1 m/s.
  FIGURES: geo_hill.svg, geo_bal.svg

## Frame 30: The hills are real  [fr_132]
NOTES: Beat 6 (≈4 min, Smooth; if short of time, one sentence: "read the gyres in O3's notes"). Sea-surface height, ocean reanalysis 2011, global mean removed. Subtropical hills ~0.9 m above the subpolar ocean (N Pacific 0.93, N Atlantic 0.94, S Pacific 1.05 m, box means, ✓). Satellite altimetry sees them (Stewart §10.3).
  TEXT: The hills are real: about 1 m high, thousands of km across
  TEXT: Sea-surface height, ocean reanalysis, 2011
  TEXT: Data scientist’s hat · momentum budget
  FIGURES: f_ssh.svg, k_ssh.svg

## Frame 31: Around the hills  [fr_139]
NOTES: Hold: surface currents, 2011 mean, 3° box means. Around the hills, at right angles to the pressure push: clockwise in the north, anticlockwise in the south (geostrophic, as we just saw). The fast flow is on the west side: Gulf Stream, Kuroshio, Agulhas. Why the west: the change of f with latitude (Stommel 1948), one sentence only; in O3's notes.
  TEXT: The hills are real: about 1 m high, thousands of km across
  TEXT: Sea-surface height, ocean reanalysis, 2011
  TEXT: Gulf Stream
  TEXT: Kuroshio
  TEXT: Agulhas
  TEXT: Data scientist’s hat · momentum budget
  FIGURES: f_ssh.svg, f_cur.svg, k_cur.svg

## Frame 32: No coast in the way  [fr_145]
NOTES: Hold: where does the wind's momentum finally go? Into coasts and the sea floor. In the Southern Ocean no continent blocks the way round at Drake Passage's latitudes, so the Antarctic Circumpolar Current runs all the way round: ~125 Sv through Drake Passage (Hartmann p. 225), the strongest current there is. Its momentum reaches the sea floor over undersea ridges. That closes the momentum ledger.
- Hook for the next lectures: the Southern Ocean was teal on the pumping map. Under the ACC, deep water comes up. Why was it down there? Salt.
  TEXT: Where does the wind’s momentum finally go?
  TEXT: Into coasts and the sea floor. And under the current with no coast, deep water comes up. Why was it down there? Next: salt.
  TEXT: Antarctic Circumpolar Current: ~125 million m³/s, with no coast in the way
  TEXT: Accountant’s hat · momentum budget
  FIGURES: f_ssh.svg, f_cur.svg

## Frame 33: To take home: the Arabian Sea  [fr_149]
NOTES: Beat 7 (≈1 min, Smooth; changed 11 Nov to pay for the geostrophy and the opening). Put the question up and leave it with them. Stop here unless there is time: the next step shows the pieces. The answer goes in the notes.
- The question as fixed in week 2: the Arabian Sea is not coolest in summer (coldest Jan-Feb, 25.8 °C), but it cools in the middle of it. 10-20°N, 60-70°E, CERES surface temperature from upwelling LW: 29.9 °C in May, 26.7 °C in August, 28.3 °C in October (✓).
- It is the mixed-layer slab's budget again: a deeper layer, and cold water coming in from below it.
  TEXT: To take home
  TEXT: Why does the Arabian Sea cool down in the middle of summer?
  TEXT: 29.9 °C in May → 26.7 °C in August

## Frame 34: The pieces  [fr_153]
NOTES: Hold: the pieces, once the class has worked on it. Monsoon winds, the strongest of the year (O3). A mixed layer stirred deeper: 20 m in April to 62 m in July (O3). Ekman transport off Somalia and Oman: coastal upwelling (today), and offshore of the jet's axis, Ekman pumping (today; Hartmann Fig 7.9). Monsoon clouds cut the sunlight. Then in autumn the winds drop and it warms again, before winter cools it.
  TEXT: To take home
  TEXT: Why does the Arabian Sea cool down in the middle of summer?
  TEXT: 29.9 °C in May → 26.7 °C in August
  TEXT: The pieces: monsoon winds · a deeper mixed layer · upwelling off Somalia and Oman · clouds
