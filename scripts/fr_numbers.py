"""Numbers for the 'Further Research' paper chapters.   .venv/bin/python -W ignore scripts/fr_numbers.py"""
import math
g = 9.81; rho = 1000.0; rs = 2650.0
print("== FR01: Egozi & Ashmore flume (as described in Olsen 2021): W=0.5 m initial channel, h=1.5 cm, S=0.015, d50=1.2 mm, d90=3.6 mm, Q=1.4/2.1/2.8 L/s ==")
S = 0.015; d = 1.2e-3; W = 0.5; h = 0.015
for Q in (1.4e-3, 2.1e-3, 2.8e-3):
    # same initial channel, normal depth not recomputed: use geometry given for the first stage, then scale depth by Manning-like h ~ Q^(3/5) (wide channel)
    pass
U = 1.4e-3/(W*h); Fr = U/math.sqrt(g*h); tau = rho*g*h*S; ts = tau/((rs-rho)*g*d); tau_c = 0.045*(rs-rho)*g*d
print(f"  U = Q/(W h) = {U:.3f} m/s; Froude = {Fr:.3f}; bed shear stress tau = rho g h S = {tau:.2f} Pa; Shields number = {ts:.3f}; critical (0.045) tau_c = {tau_c:.2f} Pa -> tau/tau_c = {tau/tau_c:.2f}")
us = math.sqrt(tau/rho); print(f"  shear velocity u* = {us:.3f} m/s; aspect ratio W/h = {W/h:.1f}; beta = W/(2h) = {W/(2*h):.1f}")
ws = {"1.2 mm": 0.16}; print("  settling velocity of 1.2 mm sand ~ 0.15 m/s (recalled) >> u*: bedload-dominated; Rouse number ~", 0.16/(0.41*us))
qs = 0.05*rs*U**2*math.sqrt(d/(g*(rs/rho-1)))*(tau/(g*(rs-rho)*d))**1.5
print(f"  Engelund-Hansen (Olsen eq. 3): q_s = {qs:.4f} kg/(m s) = {qs*3600:.1f} kg/(m h); over W=0.5 m: {qs*W*3600:.1f} kg/h = {qs*W*3600/rs*1e3:.2f} L/h of sand")
print("  exponent check: q_s ~ U^2 * (Shields)^(3/2): doubling the Shields number multiplies q_s by", 2**1.5)
print("  run time 210 h at dt = 4 s ->", 210*3600/4, "time steps (paper: 189,000)")
print("  grid: 18 m / 4 cm =", 18/0.04, "cells long (paper: fine grid 450 x 120: 3 m / 2.5 cm =", 3/0.025, ")")
print("== FR03: Gomati bend (Das & Biswal 2023): B=42.7 m, S=0.0006, Q=68 and 102 m3/s, reported mean U = 0.56 and 0.77 m/s, tau = 27.99 and 35.62 Pa ==")
B = 42.7; S = 0.0006
for Q, Urep, taurep in [(68, 0.56, 27.99), (102, 0.77, 35.62)]:
    hh = Q/(Urep*B); tau_u = rho*g*hh*S; n_imp = hh**(2/3)*S**0.5/Urep
    print(f"  Q={Q}: depth from continuity h = Q/(U B) = {hh:.2f} m; uniform-flow shear stress rho g h S = {tau_u:.1f} Pa vs reported {taurep}; implied Manning n = h^(2/3) S^(1/2)/U = {n_imp:.3f}")
    # Manning-predicted depth for n = 0.03
    for n in (0.02, 0.03, 0.04):
        h_n = (Q*n/(B*S**0.5))**0.6; print(f"     with n={n}: uniform depth {h_n:.2f} m, U = {Q/(B*h_n):.2f} m/s, tau = {rho*g*h_n*S:.1f} Pa")
    Fr = Urep/math.sqrt(g*hh); print(f"     Froude (reported U, continuity depth) = {Fr:.2f}")
print("  sinuosity 94.62/53.16 =", 94.62/53.16, " (paper: 1.78); radius/width = 60.22/42.7 =", 60.22/42.7)
print("  secondary-flow intensity ~ h/R: 2.84/60.22 =", 2.84/60.22, "; Olsen's 2D closure: tan(delta) = -K1 h/R with K1 = 7 -> delta =", math.degrees(math.atan(7*2.84/60.22)), "deg")
print("== FR04: recurrence = slip / (coupling * convergence rate) ==")
for slip in (3, 6, 10):
    for V in (17, 20):
        for chi in (1.0, 0.8):
            print(f"  slip {slip} m, V={V} mm/yr, coupling {chi}: {slip/(chi*V/1000):.0f} yr")
M0 = 10**(1.5*7.8+9.1); print("  Gorkha Mw 7.8: M0 =", f"{M0:.2e}", "N m")
print("  great Mw 8.5: M0 =", f"{10**(1.5*8.5+9.1):.2e}", "N m; ratio to Gorkha:", 10**(1.5*0.7))
print("  Himalaya elevation range 7000-8000 m vs plateau 4500-5000 m: difference 2000-3500 m")
print("== FR02/FR03: superelevation across a bend dh = U^2 B / (g R) (transverse surface slope g S_r = U^2/R) ==")
for U in (0.56, 0.77): print(f"  U = {U} m/s, B = 42.7 m, R = 60.22 m: dh = {U*U*42.7/(9.81*60.22)*100:.1f} cm")
print("  Froude number u/sqrt(g h) at outer bank: 0.8 m/s, 3.1 m ->", 0.8/math.sqrt(9.81*3.1))
print("  pi/2 =", math.pi/2, " (Njenga et al. quote phase-shift thresholds 1.56, 1.55, 1.53, 1.46 in the text)")
