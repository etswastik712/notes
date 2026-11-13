"""CL26: mass ledger / overturning numbers + figure (Joy O6).   .venv/bin/python -I scripts/fig_cl26.py
Stommel two-box model: my own nondimensionalisation.  x = equator-pole temperature difference, y = equator-pole salinity difference,
q = x - y (flow, > 0: sinking at the pole = thermally direct).  dx/dt = 1 - x(1+|q|),  dy/dt = F - |q| y,  F = freshwater forcing."""
import os, sys, math, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import importlib.util
spec = importlib.util.spec_from_file_location("f25", os.path.join(os.path.dirname(os.path.abspath(__file__)), "fig_cl25.py"))
f25 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(f25)
rho, tfreeze = f25.rho, f25.tfreeze

# steady branches
def F_thermal(q): return q * (1 - q - q * q) / (1 + q)       # q > 0
def F_reversed(a): return a / (1 + a) + a * a                # a = |q|, q < 0
qq = np.linspace(1e-4, 0.62, 4000); Ft = F_thermal(qq)
i = int(np.argmax(Ft)); Fmax, qmax = Ft[i], qq[i]
print("thermal branch: F_max = %.4f at q = %.3f ; thermal states exist for 0 < F < F_max; q at F=0.1: stable %.3f unstable %.3f" % (
    Fmax, qmax, qq[(Ft >= 0.1) & (qq > qmax)][-1] if ((Ft >= 0.1) & (qq > qmax)).any() else float('nan'), qq[(Ft >= 0.1) & (qq < qmax)][0]))
from scipy.optimize import brentq
a_at_Fmax = brentq(lambda a: F_reversed(a) - Fmax, 1e-6, 2)
print("reversed state at F=F_max: q = -%.3f (the collapse jumps from q=+%.3f to -%.3f)" % (a_at_Fmax, qmax, a_at_Fmax))
print("reversed branch exists only for F > 0 (F_reversed(a) > 0): the thermal state returns only when F < 0 (pole saltier than the 'average' forcing)")

# slow ramp simulation
def ramp(F0, F1, F2, T=4000.0, dt=0.01, x=None, y=None):
    n = int(T / dt)
    if x is None:
        x, y = 1.0, 0.0
    out = []
    for k in range(n):
        t = k / n
        F = F0 + (F1 - F0) * (2 * t) if t < 0.5 else F1 + (F2 - F1) * (2 * t - 1)
        q = x - y
        x += dt * (1 - x * (1 + abs(q))); y += dt * (F - abs(q) * y)
        if k % 100 == 0: out.append((F, q, t))
    return np.array(out)
r = ramp(0.0, 0.25, -0.05)
up, dn = r[r[:, 2] < 0.5], r[r[:, 2] >= 0.5]
jump_up = next(F for (F, q, t), (F2, q2, t2) in zip(up[:-1], up[1:]) if q > 0 and q2 < 0)
jump_dn = next(F for (F, q, t), (F2, q2, t2) in zip(dn[:-1], dn[1:]) if q < 0 and q2 > 0)
print("hysteresis by simulation (ramp slow): collapse at F = %.3f (analytic F_max %.3f) ; recovery at F = %.3f (analytic: 0)" % (jump_up, Fmax, jump_dn))

# why not the North Pacific
S_np, S_na = 32.8, 35.1
print("N Pacific surface cooled to freezing (%.2f C): sigma %.2f ; deep (2000 m) sigma 27.7 -> S needed at -1.8 C: %.2f (short by %.2f g/kg)" % (tfreeze(S_np), rho(S_np, tfreeze(S_np)) - 1000, next(s for s in np.arange(30, 37, 0.001) if rho(s, -1.8) >= 1027.7), next(s for s in np.arange(30, 37, 0.001) if rho(s, -1.8) >= 1027.7) - S_np))
Tx = next(t for t in np.arange(12, -2, -0.01) if rho(S_na, t) >= 1027.8)
print("N Atlantic (S=35.1) reaches sigma 27.8 at T = %.1f C (Joy: below ~4 C)" % Tx)
print("consistency: 1000 yr x 1 mm/s = %.0f km (Stewart: N Atlantic -> ACC -> N Pacific)" % (1000 * 3.156e7 * 1e-3 / 1e3))
V = 1.335e18   # ocean volume, recalled (used in CL21)
for fr, lab in ((1.0, "whole ocean"), (0.9, "90 %")):
    print("renewal of %s (%.2e m3) at 42 Sv: %.0f yr ; at 27.5 Sv (17.5 N Atl + 10 Antarctic): %.0f yr" % (lab, fr * V, fr * V / 42e6 / 3.156e7, fr * V / 27.5e6 / 3.156e7))
print("tau = C/lambda for 4000 m: 140 yr (all stirred at once) vs observed ~1000 yr")
print("Sv list: NADW formation 15-20 Sv (1.5-2e10 kg/s), Antarctic ~10 Sv, Gulf Stream ~30 Sv (Florida), ACC 125 Sv, RAPID mean 17.0 Sv (2004-2024, slide), Stewart 1st year 18.7+-5.6 Sv (24N)")
print("Greenland 8 C in 40 yr = %.2f K per decade" % (8 / 4))

fig, ax = plt.subplots(1, 3, figsize=(14.2, 4.5))
a = ax[0]
a.plot(F_thermal(qq[qq > qmax]), qq[qq > qmax], color=BLUE, lw=2.2); a.plot(F_thermal(qq[qq <= qmax]), qq[qq <= qmax], color=BLUE, lw=2.2, ls="--")
aa = np.linspace(1e-3, 0.6, 300); a.plot(F_reversed(aa), -aa, color=ORANGE, lw=2.2)
a.axhline(0, color="#888", lw=0.6); a.axvline(0, color="#888", lw=0.6)
a.plot(up[:, 0], up[:, 1], ".", ms=1.5, color=INK); a.plot(dn[:, 0], dn[:, 1], ".", ms=1.5, color=AQUA)
a.annotate("collapse at F ≈ %.2f" % Fmax, (Fmax, 0.3), (0.145, 0.05), fontsize=8, arrowprops=dict(arrowstyle="->"))
a.annotate("returns only when F < 0", (0.0, -0.01), (0.04, -0.25), fontsize=8, arrowprops=dict(arrowstyle="->"))
a.text(0.02, 0.5, "on (stable)", color=BLUE, fontsize=8.5); a.text(0.09, 0.15, "unstable", color=BLUE, fontsize=8); a.text(0.12, -0.4, "reversed / weak (stable)", color=ORANGE, fontsize=8.5)
a.set_xlim(-0.06, 0.25); a.set_ylim(-0.6, 0.65); a.set_xlabel("freshwater forcing F (dimensionless)"); a.set_ylabel("overturning q")
a.set_title("A  two stable states and hysteresis (Stommel box)", fontsize=9.8)
b = ax[1]
Tg = np.linspace(14, -1.9, 100)
b.plot(Tg, [rho(S_na, t) - 1000 for t in Tg], color=ORANGE, lw=2, label="N Atlantic surface, S = 35.1")
b.plot(Tg, [rho(S_np, t) - 1000 for t in Tg], color=AQUA, lw=2, label="N Pacific surface, S = 32.8")
b.axhline(27.8, color=ORANGE, ls=":", lw=1); b.axhline(27.7, color=AQUA, ls=":", lw=1)
b.text(13.8, 27.84, "deep N Atlantic σ 27.8", fontsize=7.6, color=ORANGE); b.text(13.8, 27.60, "deep N Pacific σ 27.7", fontsize=7.6, color=AQUA)
b.invert_xaxis(); b.set_xlabel("surface temperature cooled to (°C)"); b.set_ylabel("surface σ (kg m⁻³)"); b.legend(fontsize=8, frameon=False, loc="lower left")
b.set_title("B  cooled to freezing, only the Atlantic is heavy enough", fontsize=9.8)
c = ax[2]
items = [("NADW formation", 17.5), ("Antarctic bottom water", 10), ("RAPID mean, 26.5°N", 17), ("Gulf Stream (Florida)", 30), ("Drake Passage (ACC)", 125)]
c.barh(range(len(items)), [v for _, v in items], color=[BLUE, BLUE, ORANGE, AQUA, "#6d8bff"], height=0.55)
c.set_yticks(range(len(items))); c.set_yticklabels([k for k, _ in items], fontsize=8.2); c.invert_yaxis(); c.set_xlabel("transport (Sv = 10⁶ m³ s⁻¹)")
for i, (_, v) in enumerate(items): c.text(v + 2, i, ("%g" % v) + (" (15–20)" if i == 0 else ""), va="center", fontsize=8)
c.set_title("C  how big is the overturning?", fontsize=9.8)
fig.subplots_adjust(wspace=0.55)
save(fig, "fig_cl26_overturning")
