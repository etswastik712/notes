Daisyworld with an Ocean

Daisyworld with an Ocean

Build a planet one part at a time, from bare land to an ocean with daisies and grazers, and see how each part changes the way its temperature varies, from month to month and from century to century.

 Model
 How it works

 

 Keep this run each run stays, dashed, under the next

 

 
 
 Ocean
 
Ocean fraction 

 
Mixed-layer depth 
 
Deeper = more heat stored, slower response.

 Deep ocean
 
 
 Life
 
 Daisies
 Grazers

 
 
 Weather
 
Weather size 
 
Random pushes, the same over land and ocean.

 Day and seasons
 
Sunlight follows the day and the year, and the weather lasts a few days.

 
New weatherweather no. 

 
 
 Sun and run
 

 Brighten the sun
 at year 
 

 
Makes the sun 5% brighter at that year.

 
Run length 
 
Shown after 1500 hidden years that let it settle.

 
 
 More settings
 
Grazers' taste for white daisies 

 
Grazers' best temperature 

 
Grazers' tolerance 
 
How far from their best temperature grazers still eat well.

 
Sun brightness 

 
Reset this preset

 
 
 
 

Starting…

 

 

 

 Show
 
 10 years
 50 years
 300 years
 1000 years
 the whole run
 
 
 

 

 
Populations over time

 

 
 
 

 

 

 

Temperatures over time

 
Yearly averagesMonthly

 

 
 

 

 
The planet 

 

 

 

 

 

 

 

 ocean 
 bare ground 
 white daisies 
 black daisies 
 

 

 

 
Move over or tap a chart to pick a moment.

 

 

How much does temperature vary at each timescale?

 
BarsSpectrum

 

 
 
 

 

 

 

 

Things to try

 
 
Land only. Press Monthly and show 10 years: how big are the seasons? Then look at the month, year, decade and century bars. Do they follow the "weather alone" line? Why does averaging wash the weather out?

 
Add a mixed layer. The seasons shrink and the jitter disappears. Where did it go? Is the planet calmer at every timescale, or only at short ones?

 
Add a deep ocean. Press Brighten the sun. How long until the planet stops warming? Now turn the deep ocean off and try again. Why the difference?

 
Add life. Find three busts of different sizes. What was the ocean temperature doing just before each one?

 
Compare: grazers, all land. Same grazers, same weather, no ocean. Why are there no long busts?

 
Compare: grazers, no weather. Every bust is the same size. So where does the variety in step 4 come from?

 
Clockwork cycle. Change the mixed-layer depth. What happens to the time from one dip in the grazer chart to the next, and why? (Time the dips, not the circles: circles are kept at least 12 years apart, so here only every other dip gets one.)

 
 
 

Download

 
CSV files open in Excel, Google Sheets or Python: one row per month, column names in row 1. Columns for parts that aren't in this run are left empty.

 
Download whole run

 
Download ±20 years around this bust

 
Download all busts (stacked)

 
Download settingsevery setting and a link that reruns this run in the same browser (with daisies and grazers, another browser gives the same kind of run, with busts at different times)

 
 
 

This page explains what the model on the Model tab does: what the planet is made of, the rules each part follows, how the computer turns those rules into a run, and how to read the charts. You need no maths beyond school algebra: every symbol is explained where it first appears, and every number the model uses is listed in the box alongside (at the end on a narrow screen).

1. The planet's parts, and how fast each one forgets

Picture the planet as a few separate stores of heat, each with one temperature. A part that holds a lot of heat warms and cools slowly, so it remembers warm and cold spells for a long time. A part that holds little heat follows whatever is happening now, and soon forgets it.

 

Land

The ground and the air above it: 30% of the planet.

Heat capacity C_(L) = 1×10⁷ J m⁻² K⁻¹

Forgets in about 2 months

 

Mixed layer

The top 75 m of the ocean, stirred by wind and waves so it warms as one: 70% of the planet.

C_(m) = 4.2×10⁶ × 75 ≈ 3.2×10⁸ J m⁻² K⁻¹, about 30 times the land

Forgets in about 5 years

 

Deep ocean

About 1000 m of water under the mixed layer. It swaps heat only with the mixed layer, and slowly.

C_(d) = 4.2×10⁹ J m⁻² K⁻¹, 420 times the land

Forgets in about 190 years

Heat capacity is how many joules it takes to warm one square metre of a part (the whole column, top to bottom) by one degree. Response time is how long a part takes to settle after something warms or cools it:

response time = heat capacity ÷ how fast the part loses heat when it is warmer than usual

 
Land: for each degree it is warmer, it sends b = 2.09 W m⁻² more heat to space. 1×10⁷ ÷ 2.09 ≈ 4.8 million seconds, about 2 months. Next to an ocean it also loses 15 W m⁻² per degree to the sea, so it is pulled along with the ocean within about a week.

 
Mixed layer: 3.2×10⁸ ÷ 2.09 ≈ 150 million seconds, about 5 years. A deeper mixed layer remembers longer: about 8 months at 10 m, about 19 years at 300 m.

 
Deep ocean: it loses heat only to the mixed layer, at γ_(o) = 0.7 W m⁻² per degree. 4.2×10⁹ ÷ 0.7 = 6×10⁹ seconds, about 190 years.

These three response times are the dotted lines on the Model tab's spectrum. The deep ocean shows itself most clearly when the sun brightens: about 80% of the warming arrives within 10 years as the mixed layer catches up, and the rest creeps in over centuries as the deep ocean warms. Turn the deep ocean off and about 95% arrives within 10 years.

2. The energy budget of each part

A part warms when more energy comes in than goes out, and cools when less comes in. How fast it warms depends on its heat capacity. So every part follows the same kind of budget:

heat capacity × how fast the temperature changes = energy in − energy out

Energy flows are measured per square metre, in W m⁻² (joules per second on each square metre). Two flows appear in both the land's and the mixed layer's budgets.

Sunlight in, heat out

 
Sunlight. The sun delivers Q = 342 × L W m⁻², where L = 1.05 is the sun's brightness, so Q ≈ 359 W m⁻². A surface reflects a fraction of it, called its albedo A, and absorbs the rest, Q(1 − A). Albedos (clouds above included): white daisies 0.50, bare ground 0.32, ocean 0.28, black daisies 0.15.

 
Heat to space. A warmer surface sends out more heat: a + b·T, with a = 203.3 W m⁻², b = 2.09 W m⁻² K⁻¹ and T in °C. Each degree warmer sends 2.09 W m⁻² more to space. At 19 °C that is 243 W m⁻², close to the 244 W m⁻² that bare ground absorbs, which is why bare land on its own (Land only) settles near 19.5 °C. Next to the darker ocean (albedo 0.28) the land settles warmer, near 24 °C; with daisies it comes back to about 19 °C.

 
Day and seasons (on in the first three presets, or tick Day and seasons). Sunlight then rises and sets every day, peaking at noon, and through the year swings 30% above and below its average, highest on 21 June. Its average over the year stays Q. Bare land on its own then runs from about −5 °C in February to 44 °C in August, a range of 49 K. Next to the ocean the land's range is about 9 K, and the mixed layer's about 3 K, warmest in September, nearly three months after the sun. Day and night differ by about 1 K on land and 0.04 K in the mixed layer. Real bare ground swings far more between day and night, because a day's warmth reaches only its top 10 cm or so; the model's land is one block sized for the year's swing.

Land

In wordsThe land's stored heat changes by the sunlight it absorbs, minus the heat it sends to space, minus the heat it passes to the ocean, plus whatever the weather adds.

C_(L) · dT_(L)/dt = Q(1 − A_(L)) − (a + b·T_(L)) − k(T_(L) − T_(m)) + weather

 
dT_(L)/dt how fast the land temperature T_(L) is changing (kelvin per second)

 
A_(L) the land's albedo, a mix of what covers it: A_(L) = a_(w)·A_(w) + a_(b)·A_(b) + g·A_(g), where a_(w) and a_(b) are the fractions of land under white and black daisies and g = 1 − a_(w) − a_(b) is bare

 
k(T_(L) − T_(m)) heat passed to the ocean, k = 15 W m⁻² for each degree the land is warmer than the mixed layer (T_(m)); with no ocean this term is left out

Mixed layer

In wordsThe same budget with the ocean's albedo, plus the heat that arrives from the land, minus the heat passed down to the deep ocean, plus the same weather as over the land.

C_(m) · dT_(m)/dt = Q(1 − A_(o)) − (a + b·T_(m)) + k·(1 − f_(o))/f_(o)·(T_(L) − T_(m)) − γ_(o)(T_(m) − T_(d)) + weather

 
(1 − f_(o))/f_(o) the ocean covers f_(o) = 0.7 of the planet and the land 0.3, so the heat leaving each square metre of land is shared over 0.7/0.3 ≈ 2.3 square metres of ocean

 
γ_(o)(T_(m) − T_(d)) heat passed down to the deep ocean (T_(d)), γ_(o) = 0.7 W m⁻² per degree; with the deep ocean off, γ_(o) = 0

Deep ocean

In wordsThe deep ocean gets no sunlight and sends nothing to space. It only swaps heat with the mixed layer above it.

C_(d) · dT_(d)/dt = γ_(o)(T_(m) − T_(d))

3. Daisies and grazers

Life touches the climate in one way only: it changes the colour of the land. The climate touches life in one way only: temperature sets how fast daisies grow and how hungry the grazers are. Rates here are per day.

Colour and patch temperature

A patch of white daisies absorbs less sunlight than the land around it, so it is cooler; a patch of black daisies is warmer. With q = 20 K:

T_(w) = T_(L) + q(A_(L) − A_(w))  T_(b) = T_(L) + q(A_(L) − A_(b))

On mostly bare land (A_(L) ≈ 0.32), white patches are 3.6 K cooler than the land and black patches 3.4 K warmer.

Growth and crowding

Daisies grow best at T_(opt) = 22.5 °C, more slowly either side, and not at all below 5 °C or above 40 °C (w_(d) = 17.5 K either side of the best). Each patch uses its own temperature:

β(T) = 1 − ((T − T_(opt))/w_(d))²  (zero when this is below 0)

Daisies can only spread onto bare ground, so growth is multiplied by the bare fraction g: as the land fills up, growth stops. Daisies also die at a steady rate, and grazers eat some (G_(w), G_(b), below):

da_(w)/dt = a_(w)(r·β(T_(w))·g − γ) − G_(w)  and the same for black daisies

r = 0.1 per day is the fastest growth and γ = 0.03 per day the death rate. At the best temperature on half-bare land, cover grows by 0.1 × 0.5 − 0.03 = 0.02 of itself per day. With life switched off (the first three presets), r = 0 and the land is bare ground.

Grazers' appetite

Grazers (Z, a relative amount) eat fastest at their favourite land temperature, T_(g) = 25 °C, and less when the land is colder or warmer:

g_(max) = g_(0)·exp(−((T_(L) − T_(g))/w_(g))²)

g_(0) = 0.12 per day is the top appetite and w_(g) = 6 K sets how quickly it falls away. The land usually sits near 19 °C, 6 K below their best, where the appetite is 0.044 per day, and colder land means they eat even less.

Grazing

Grazers eat more when there is more food, but they can only eat so fast. When daisies are scarce, eating rises with the amount of daisies; when daisies are plentiful, each grazer eats at its top speed.

G_(w) = g_(max)·s_(w)·a_(w)·Z / (K + s_(w)·a_(w) + s_(b)·a_(b))  and the same for black daisies

K = 0.08 sets where "plentiful" begins. The taste for each colour is s_(w) = 2p and s_(b) = 2(1 − p). With p = 0.3 the grazers prefer black daisies: s_(b) = 1.4 against s_(w) = 0.6.

Eating and starving

Grazers multiply on what they eat and die off at a steady rate:

dZ/dt = e(G_(w) + G_(b)) − m·Z

Half of what grazers eat becomes new grazers (e = 0.5), and grazers die at m = 0.015 per day. With no food, half of them are gone in about 46 days.

4. The loop: how the boom–bust and the climate drive each other

Put sections 2 and 3 together and the daisies, the grazers and the temperature push each other round in a loop. Take the Add life preset: grazers prefer black daisies (p = 0.3) and grow best at 25 °C, warmer than the land's usual 19 °C. With the weather switched off (Compare: grazers, no weather), the loop repeats every 8 years. One turn:

The loop: boom, bust, white bloom, slow cooling, black daisies spread, rewarming, and back to boom. One turn takes about 8 years without weather.

one turn
about 8 years
without weather
1Boomplanet warmest
2Bustgrazers starve
3White bloomplanet brightest
4Slow coolingocean slows it
5Black daisiesspread in the cold
6Rewarmingland darkens

planet warmplanet coldturning

 
Boom. Grazers peak and strip the land of daisies, black ones first (their favourite). Bare ground (albedo 0.32) is darker than white daisies, so the land is dark and the planet is at its warmest.

 
Bust. With the food gone, grazers starve and crash within about 8 months.

 
White bloom. Free of grazing, white daisies spread over the empty land (up to 64% cover about a year after the grazer peak). The planet is at its brightest.

 
Slow cooling. The planet cools, but the ocean holds its heat, so the coldest point comes 2.5–3.5 years after the brightest. This delay is the ocean's memory.

 
Cold suits black daisies, not grazers. On cold land, black-daisy patches stay near the daisies' favourite temperature, so black daisies spread. Grazers eat less in the cold, because 19 °C is below their 25 °C best.

 
Rewarming and the next boom. More black daisies darken the land, and the planet warms. Warmth and plenty of their favourite food let the grazers boom again.

 
Biology → climate: who covers the land sets how much sunlight is reflected.

 
Climate → biology: temperature sets how fast each daisy grows and how hungry the grazers are.

 
The ocean: delays the temperature response by years, so the loop overshoots and keeps cycling instead of settling down.

5. Weather as random pushes, and why the ocean adds them up

Real weather brings sunny spells and cloudy ones, warm winds and cold ones. The model has no storms or clouds of its own. Instead, the weather adds a random push of energy, sometimes in and sometimes out. Without Day and seasons, a fresh push comes every quarter-day, drawn like a roll of dice with no link to the one before. With Day and seasons, the push changes every hour but lasts: nearly three-quarters of today's push is still there tomorrow, and it fades over about 3 days, as a weather system passes. Either way the weather has no slow swings of its own. The pushes are sized so that a day's average push has a spread of σ = 30 W m⁻² (the Weather size slider). Land and ocean share one atmosphere, so both get the same push at the same moment.

A push that lasts 3 days moves the temperature further than three separate one-day pushes that partly cancel. So with the same σ, lasting weather makes every part of the planet vary about 2.6 times more, at every timescale longer than a few days. The patterns below don't change.

Why the ocean adds them up

The same push moves the land about 30 times more than the mixed layer, because the land holds 30 times less heat: a day of typical weather warms or cools the land by about 0.26 K, the mixed layer by only 0.008 K. But the land forgets each push within weeks, while the mixed layer keeps it for about 5 years. Over those years warm and cold pushes mostly cancel, but never exactly. A spell with a few more cold pushes than warm ones leaves a colder ocean, and the ocean then wanders slowly, warm for some years and cool for others, though nothing in the weather swings slowly.

Think of a bath with a slow leak, with cupfuls of water tipped in or scooped out at random: the level wanders slowly. A cup with the same random splashes would only jitter.

So the ocean does not make the planet more variable. It makes the variability slower. From Land only to Add a mixed layer, the year-to-year spread falls from about 1.8 K to about 0.7 K, while the spread of 100-year averages stays about the same. The ocean shrinks the seasons for the same reason: a season is a slow push, but not slow enough for the mixed layer to catch up with it.

With life: busts of every size

Weather adds random warm and cold spells to the loop in section 4. The land forgets them within weeks; the ocean adds them up, so a run of cold years leaves a cold ocean. A colder ocean going into a bust means a deeper, longer bust: across many busts, the colder the ocean in the three years before, the deeper the bust (a correlation of about −0.8, where −1 would be a perfect match). So busts come in every size. In a typical bust the grazers fall about 10 times; in the largest tenth they fall about 200 times or more. Temperature then varies over decades and centuries, though nothing in the weather or in the biology alone has those timescales.

On the grazer chart a circle marks each bust, bigger for a deeper one. Circles are kept at least 12 years apart, so when the grazers cycle faster than that, as in Compare: grazers, no weather and Clockwork cycle, only every other dip gets a circle. To time the cycle, measure from dip to dip.

6. How the computer solves it

The equations say how fast each quantity is changing right now, not where it will be in a hundred years. The computer gets there by taking many small steps.

Small steps, adding up changes

At each step the computer works out every rate of change from the current values, then moves each quantity on by its rate times the step:

new value = old value + rate of change × time step

If the land is warming at 0.1 K per day, a quarter-day later it is 0.025 K warmer. Then the rates are worked out again from the new values, and so on.

Why a quarter-day, or an hour

Each step pretends the rates stay fixed for the whole step. That is only fair if the step is short compared with the fastest change in the model: the land, tied to the ocean, settles in about a week, and daisies and grazers change by a few percent a day. A step of a quarter-day (6 hours) is short enough for both; much longer steps would make the land temperature overshoot back and forth. That makes 1460 steps per year: a 2000-year run with its hidden start is about 5 million steps, done in the background while the progress bar fills. With Day and seasons the sun rises and sets, and a quarter-day step can't follow that, so the step is an hour: 8760 steps per year, about 30 million for a run, which takes a second or two.

One weather push per step, shared

At each step the computer draws one random number. That single number gives the same push, in W m⁻², to the land and to the mixed layer; each temperature then moves by push × time step ÷ its heat capacity. Without Day and seasons, the push for one step has a spread of 2σ = 60 W m⁻²: four independent pushes averaged over a day have a spread √4 = 2 times smaller, which is σ. With Day and seasons, each hour keeps 98.6% of the last hour's push and adds a small new one, so the push fades over 3 days. (The same square-root rule comes back in section 7.) New weather picks a new random sequence; the same weather number always gives the same run in the same browser. With daisies and grazers, another browser or device can give a run that behaves the same overall but has its busts at different times, because different browsers can work out the same maths very slightly differently in the last digit, and the busts magnify those tiny differences.

The hidden start

Every run starts from a made-up state: all temperatures 20 °C, 30% white and 30% black daisies, grazers 0.05. The deep ocean needs several of its 190-year response times to forget that start. So the computer first runs 1500 hidden years, about eight deep-ocean response times, and shows only what comes after. The run you see starts settled, with no drift left over from the start.

Floors

Daisy cover never falls below 0.0001 of the land (a seed bank), and grazers never fall below 0.00001 (a few wanderers arrive from elsewhere). Without these floors, nothing can come back after a bust.

Why runs must be long

To see how much 100-year averages vary, you need many 100-year averages. A 2000-year run holds only 20 of them, and with daisies and grazers the century bar can move by a sixth or more when you change the weather; a 500-year run holds only 5. Busts come about once every 25 years on average and the deep ones are rare, so a short run may not show them. That is why the default run is 2000 years, and you can go up to 4000.

7. How to read the timescale bars and the spectrum

The temperature chart shows wiggles of every length at once. The bars pull them apart by asking: after averaging over a month, a year, a decade or a century, how much do those averages still vary?

The timescale bars

Take the whole planet's temperature, one value per month. With an ocean that is 30% land and 70% mixed layer, (1 − f_(o))·T_(L) + f_(o)·T_(m); with no ocean it is the land. Cut the run into blocks of 1 month, 1 year, 10 years or 100 years and average each block. A bar's height is the spread of those block averages: roughly how far a typical block sits from the run's overall average (the standard deviation). The scale goes up 10 times per step.

With Day and seasons, the seasons would swamp the 1-month bar, and they repeat every year, so they are taken out first. For each month of the year, the computer works out its average over the whole run (the run's average January, average February, and so on) and subtracts it. What is left is how far each month sits from a normal month of its kind: the departures from the average year. The bars and the spectrum use those departures. This is how climate scientists talk about an unusually warm month.

The weather-alone line

Averaging washes out values that are independent of each other: average N independent values and the spread shrinks by √N. The dashed line starts at this run's 1-month bar, then shrinks by √12 ≈ 3.5 from month to year (12 months), by √10 ≈ 3.2 from year to decade, and by √10 again to the century. It is what the bars would be if each month were independent of the last, like the weather.

 
A bar on the line: the months behave like the weather, with no memory beyond a month.

 
A bar above the line: the planet carries warmth or cold from month to month, so averaging washes out less.

 
A bar below the line: something pulls the temperature back towards its usual value, as daisies do when they regulate.

On Land only the bars fall about as fast as the line. With a mixed layer the year bar barely drops from the month bar, because the ocean keeps a month's warmth for years. With grazers as well, the decade and century bars sit far above the line.

The spectrum

The Spectrum button shows the same idea in finer detail. It splits the temperature record into swings of different lengths (periods) and shows how much of the variation sits in each band of periods: fast swings on the left, slow ones on the right, both axes 10 times per gridline. The dashed line is weather alone again. Independent months spread their variation evenly over all frequencies, and a band of long periods covers fewer frequencies than a band of short ones, so the line falls 10 times for every period 10 times longer: the same falling-off as the bars' dashed line. Where the curve sits above the line, averaging over that period washes out less than it would for the weather, just as with a bar above its line. Each part of the planet smooths away swings that are fast compared with its response time and passes slower ones on, so the curve sits below the line on the left, rises above it near that part's dotted line, and falls off again at much longer periods. The dotted lines are the response times from section 1, and they move when you change the mixed-layer depth. A sharp peak is a regular cycle: with no weather, the grazers give a peak at 8 years.

8. What the model leaves out

 
Geography. One land box and one ocean box: no continents, no equator or poles, no currents carrying heat from place to place.

 
Days and seasons, done simply. With Day and seasons, the sun follows one place's day and year: every day is 12 hours long, and the land is one block, so its day–night swing is far too small. Without it, the sun shines steadily.

 
Real weather. Storms, clouds and winds are replaced by random pushes. With Day and seasons they last a few days; without it they have no memory of their own.

 
Climate feedbacks. Ice, snow, clouds, water vapour and carbon dioxide do not change with temperature; the straight line a + b·T stands in for all of them.

 
Richer life. Two kinds of daisy and one kind of grazer, living only on land, and nothing evolves.

 
Earth's real numbers. The numbers are chosen to show the ideas clearly, not to match Earth.

So the model is not a forecast. It shows one idea clearly: a planet made of parts with different memories can swing slowly, over decades and centuries, even when nothing pushing it swings slowly.

Numbers the model uses

Defaults; presets and sliders change some of them.

Sun and heat

 L1.05sun brightness
 Q342L ≈ 359sunlight, W m⁻²
 A_(w), A_(b)0.50, 0.15albedo of white, black daisies
 A_(g), A_(o)0.32, 0.28albedo of bare ground, ocean
 a, b203.3, 2.09heat to space

Heat stores

 C_(L)1×10⁷land, J m⁻² K⁻¹
 C_(m)4.2×10⁶·Hmixed layer, depth H = 75 m
 C_(d)4.2×10⁹deep ocean, about 1000 m
 k15land–ocean exchange, W m⁻² K⁻¹
 γ_(o)0.7mixed layer–deep exchange
 f_(o)0.7ocean share of the planet

Daisies and grazers (rates per day)

 r, γ0.1, 0.03daisy growth, death
 T_(opt), w_(d)22.5 °C, 17.5 Kdaisies' best, width
 q20 Kpatch contrast
 g_(0)0.12grazers' top appetite
 T_(g), w_(g)25 °C, 6 Kgrazers' best, tolerance
 p0.3taste for white daisies
 K0.08where eating levels off
 e0.5food made into grazers
 m0.015grazer death rate

Weather and method

 σ30 W m⁻²weather size, daily
 step0.25 dayone weather push per step
 seasons±30%with day and seasons
 weather3 dayshow long a push lasts, with day and seasons
 step1 hourwith day and seasons
 start1500 yearshidden, then 2000 shown
 floors10⁻⁴, 10⁻⁵daisy cover, grazers