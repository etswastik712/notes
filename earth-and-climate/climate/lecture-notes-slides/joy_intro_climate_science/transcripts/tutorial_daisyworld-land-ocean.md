Daisyworld: Land and Ocean

 
Daisyworld, land and ocean

 
A planet of land and ocean. Black and white daisies grow only on the land, so they can change the colour of the land but not of the sea. The ocean is dark, and it stores far more heat than land. That changes how far the daisies can steer the climate, and how fast the planet responds when the sun changes. A bare planet with the same land and ocean runs alongside for comparison.

 

 

 
 The planet
 

 All land
 30% ocean
 70% ocean
 

 
Ocean fraction 
 

 
Ocean albedo 

 
Ocean mixed-layer depth 
 
Water that warms and cools with the surface. Real mixed layers are 20–100 m; deeper values stand in for the deep ocean.

 

 

 
 The sun
 

 Slow brightening
 Brighten, then dim
 Sudden change
 Steady
 

 

 
Starting brightness 

 
Final brightness 

 
Run length 
 
A short run is a fast change of sun. Can the planet keep up?

 

 

 
Brightness before 

 
Brightness after 
 
The planet settles under the first sun, then at year 0 the sun jumps to the second.

 Log time axis (days, months and decades side by side)
 

 

 
Brightness 
 
The daisies start from a few seeds and spread.

 

 
Years to show 

 
Brightness is relative to the classic model's reference sun (L = 1).

 

 
 More settings: daisies and albedos
 
Daisy death rate γ 

 
Heat sharing between patches q′ 
 
0 = every patch at the planet's temperature. Larger = dark patches stay warmer than light ones.

 
Daisies' favourite temperature 

 
White daisy albedo 

 
Black daisy albedo 

 
Bare ground albedo 

 
Reset everything

 
 

 

 
 

 

 Keep this run to compareClear kept run
 Keep a run, then change the planet: both show on the charts, the kept run faint.
 

 

 
Planet temperature

 

 
 

 

 
Who covers the land

 

 
 

 

 
The planet at the cursor 

 

 

 

 

 

 

 

 ocean 
 bare ground 
 white daisies 
 black daisies 
 

 

 
Move or tap on either chart to pick a moment. Without a pick, this shows the moment of most daisies (or the end of the run).

 
Download data (CSV)Download settings

 

 

 

 

 

 
Things to try

 
 
All land, slow brightening. Compare the daisy planet with the bare planet. Over what range of sun does the daisy planet stay near the daisies' favourite temperature?

 
Add ocean. Switch to 30% ocean, then 70%. What happens to that range: does it get wider, narrower, or move? At 70% ocean, are the daisies still in control? Tap the chart where they are most common and compare the two planets.

 
Two reasons. More ocean means less land for the daisies, and a darker planet. Set the ocean albedo to 0.5, the same as bare ground. Which change came from the darker ocean, and which from less land?

 
Sudden change, all land. How long does the bare planet take to warm? What does the daisy planet do in the first months, and over the next ten years? Press "Keep this run to compare" above the charts.

 
Sudden change, 30% ocean. Compare with the kept run. Turn on the log time axis. How much slower is the warming now, and why? Read the response time under the planet settings.

 
A deeper ocean. Keep the 30% ocean run, then set the mixed layer to 200 m. Is the daisy planet's peak warming bigger or smaller? Who gets more time to react?

 
Sudden change, 70% ocean. How long does the bare planet take to warm? And the daisy planet? When is its warming over?

 
Too fast to follow. Brighten, then dim, with a 30-year run and a 300 m mixed layer. Does the planet keep up with the sun? Compare with a 600-year run.

 
 
 

 
How the model works

 
The whole planet is one box with one temperature T. Daisies cover fractions a_(w) (white) and a_(b) (black) of the land; the rest of the land, x, is bare. The ocean, a fraction 1 − f of the planet, has a fixed albedo.

albedoA = f·(a_w A_w + a_b A_b + x A_g) + (1−f)·A_o

energyC dT/dt = S·L·(1−A) − σT⁴

storageC = f·C_land + (1−f)·ρc·h

patchesT_w = T + q′(A − A_w), T_b = T + q′(A − A_b)

growthβ(T) = 1 − 0.003265 (T_opt − T)² (zero outside ±17.5 °C)

daisiesda_i/dt = a_i [ x β(T_i) − γ ]

 
The heat capacity C decides how fast the planet responds. If the sun changes suddenly, the temperature moves most of the way to its new value in about τ = C / (4σT³). Land plus air has C_land = 10⁷ J m⁻² K⁻¹, so τ is about 3 weeks. A 50 m ocean mixed layer stores about 20 times as much, so τ is many months. The daisies take years to spread or die back.

 
f = land fraction; h = mixed-layer depth; ρc = 4.1 × 10⁶ J m⁻³ K⁻¹ (sea water); S = 917 W m⁻²; time in years. The response time shown under the planet settings uses T = 15 °C. Daisy cover never falls below 1% of land (seeds). In this one-box model the land feels the same temperature as the ocean. On Earth the land warms faster than the ocean, but each is held back by the other through the air.

 
 

 
Sources

 
Watson, A. J. and Lovelock, J. E. (1983). Biological homeostasis of the global environment: the parable of Daisyworld. Tellus 35B, 284–289. The growth curve, albedos, S, γ = 0.3 and q′ = 20 K follow this paper.

 
The ocean and the heat capacity here are simple teaching choices, not taken from that paper.