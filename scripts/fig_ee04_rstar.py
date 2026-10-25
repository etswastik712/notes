"""EE04 - Tilman's R* rule in a chemostat (TOY, my construction): two species on one limiting resource.
f_i(R) = mu_i R/(k_i + R) (Monod), loss rate m = D = 0.2.  R*_i = m k_i/(mu_i - m).  A grows faster at high R but B has the lower R*.
dN_i/dt = N_i (f_i(R) - m);  dR/dt = D (R_in - R) - sum_i N_i f_i(R)   (one unit of resource per unit of biomass).
"""
from scipy.integrate import solve_ivp

from figlib import *

D = m = 0.2
Rin = 10.0
sp = {"A": dict(mu=0.8, k=2.0, col=ORANGE), "B": dict(mu=0.6, k=1.0, col=BLUE)}
for s in sp.values():
    s["Rstar"] = m * s["k"] / (s["mu"] - m)
f = lambda R, s: s["mu"] * R / (s["k"] + R)


def rhs(t, y):
    NA, NB, R = y
    return [NA * (f(R, sp["A"]) - m), NB * (f(R, sp["B"]) - m), D * (Rin - R) - NA * f(R, sp["A"]) - NB * f(R, sp["B"])]


sol = solve_ivp(rhs, (0, 160), [0.5, 0.5, Rin], dense_output=True, rtol=1e-9, atol=1e-12, max_step=0.2)
t = np.linspace(0, 160, 800); NA, NB, R = sol.sol(t)

fig, axes = plt.subplots(1, 2, figsize=(10.4, 3.9))
a = axes[0]
Rg = np.linspace(0, 4, 300)
for nm, s in sp.items():
    a.plot(Rg, f(Rg, s), color=s["col"], label=f"species {nm}: $\\mu_{{max}}={s['mu']}$, $k={s['k']}$")
    a.plot([s["Rstar"]], [m], "o", color=s["col"], ms=6)
    off, ha = (-0.08, "right") if nm == "B" else (0.08, "left")
    a.annotate(f"$R^*_{nm}$={s['Rstar']:.2f}", (s["Rstar"], m), xytext=(s["Rstar"] + off, m - 0.07), ha=ha, va="top", color=INK, fontsize=8.8,
               arrowprops=dict(arrowstyle="-", color=s["col"], lw=0.9))
a.axhline(m, color=INK, ls=":", lw=1)
a.text(3.95, m + 0.012, "loss rate m", ha="right", fontsize=8.5)
a.set_xlabel("resource level R"); a.set_ylabel("per-capita growth rate f(R)")
a.set_ylim(-0.02, 0.62); a.legend(loc="upper left", fontsize=8.4)
a.set_title("A  each species' break-even level R*", fontsize=10)
b = axes[1]
b.plot(t, NA, color=sp["A"]["col"], label="N$_A$")
b.plot(t, NB, color=sp["B"]["col"], label="N$_B$")
b.plot(t, R, color=MUTED, ls="--", label="resource R")
b.axhline(sp["B"]["Rstar"], color=sp["B"]["col"], lw=0.8, ls=":")
b.set_yscale("log"); b.set_ylim(0.05, 20)
b.set_xlabel("time"); b.set_ylabel("population / resource (log scale)")
b.legend(loc="lower right", fontsize=8.6)
b.set_title("B  B holds R at 0.5, below A's R*, and excludes A", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.04, "Toy chemostat (illustrative parameters, my construction). A has the higher maximum growth rate, but at R = 0.5 its growth (0.16) is below the loss rate (0.20): "
         "the species that can live on less wins.", ha="center", fontsize=7.9, color=MUTED)
save(fig, "fig_ee04_rstar")
print({k: round(v["Rstar"], 4) for k, v in sp.items()}, "final N_A", NA[-1], "N_B", NB[-1], "R", R[-1], "N_B* expected", Rin - sp["B"]["Rstar"])
