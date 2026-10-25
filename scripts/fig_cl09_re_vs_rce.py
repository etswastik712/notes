"""CL09 - pure radiative equilibrium vs radiative-convective equilibrium in a grey-gas column (model: cl09_rce.py).

All absorbed sunlight (238.2 W m-2) is absorbed at the ground; longwave grey absorber with optical depth
tau(p)= tau_s [0.2 p* + 0.8 p*^4], tau_s = 2.5, diffusivity factor 1.66.  Convective adjustment to 9.8 or 6.5 K/km.
Left: temperature vs height.  Right: lapse rate vs height (dry adiabatic value dotted).
"""
from cl09_rce import *
from figlib import *

Fs, TAU = 238.2, 2.5
re = run_cached("re", Fs=Fs, tau_s=TAU)
d98 = run_cached("d98", Fs=Fs, tau_s=TAU, Gc=9.8e-3)
d65 = run_cached("d65", Fs=Fs, tau_s=TAU, Gc=6.5e-3)
Te = (Fs / SIG) ** 0.25
skin = Te / 2**0.25


def prof(r):
    """height (km), T (K) including the ground point at z=0, and lapse rate (K/km) at layer mids."""
    z = r["z"] / 1e3
    o = np.argsort(z)
    z, T = z[o], r["T"][o]
    lr = -np.gradient(T, z)
    return z, T, lr


def tropopause(r, Gc):
    z, T, lr = prof(r)
    below = np.where(lr >= 0.9 * Gc * 1e3)[0]
    return z[below.max()] if len(below) else 0.0


for nm, r, Gc in (("RE", re, None), ("RCE 9.8", d98, 9.8e-3), ("RCE 6.5", d65, 6.5e-3)):
    z, T, lr = prof(r)
    zt = tropopause(r, Gc) if Gc else float("nan")
    print(f"{nm}: Tg={r['Tg']:.1f} K  T(lowest layer, z={z[0]:.2f} km)={T[0]:.1f}  max lapse={lr[:10].max():.1f} K/km  convective top ~{zt:.1f} km  min T={T.min():.1f} K  OLR={r['Fu'][0]:.1f}")
print(f"skin temperature Te/2^(1/4) = {skin:.1f} K ; Te={Te:.1f} K")
z, T, lr = prof(re)
print("RE lapse rate in lowest 3 layers (K/km):", np.round(lr[:3], 1), " z (km):", np.round(z[:3], 2))

fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 5.0), gridspec_kw={"width_ratios": [1.25, 1]})
zmax = 28
for r, c, ls, lab, Gc in ((re, ORANGE, "-", "pure radiative equilibrium", None),
                          (d98, AQUA, "--", "RCE, adjusted to 9.8 K/km (dry adiabat)", 9.8e-3),
                          (d65, BLUE, "-", "RCE, adjusted to 6.5 K/km (observed)", 6.5e-3)):
    z, T, lr = prof(r)
    a.plot(np.r_[r["Tg"], T], np.r_[0, z], color=c, ls=ls, label=lab)
    a.plot([r["Tg"]], [0], "o", color=c, ms=6)
    b.plot(lr, z, color=c, ls=ls)
a.axvline(skin, color=MUTED, lw=0.9, ls=":")
a.annotate("skin temperature\n$T_e/2^{1/4}$ = %.0f K" % skin, (skin - 1.5, 21), ha="right", fontsize=8.0, color=MUTED)
a.annotate(f"ground {re['Tg']:.0f} K", (re["Tg"], 0), xytext=(-4, 12), textcoords="offset points", ha="right", fontsize=8.5)
zr, Tr, _ = prof(re)
a.annotate(f"air just above: {Tr[0]:.0f} K\n(jump of {re['Tg']-Tr[0]:.0f} K)", (Tr[0], zr[0]), xytext=(-44, 36), textcoords="offset points", fontsize=8.5,
           arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
a.set_xlim(190, 350)
a.set_ylim(0, zmax)
a.set_xlabel("temperature (K)")
a.set_ylabel("height (km)")
a.set_title("Temperature profiles", fontsize=10.5)
a.legend(loc="upper right", fontsize=8.0)
b.axvline(9.8, color=MUTED, lw=1.0, ls=":")
b.annotate(r"$\Gamma_d$ = 9.8", (9.8, 26.2), xytext=(4, 0), textcoords="offset points", fontsize=8.5, color=MUTED)
b.axvline(6.5, color=MUTED, lw=0.8, ls=":")
b.set_xlim(-1, 26)
b.set_ylim(0, zmax)
b.set_xlabel(r"lapse rate $-\mathrm{d}T/\mathrm{d}z$ (K km$^{-1}$)")
b.set_title("Lapse rates", fontsize=10.5)
lrr = prof(re)[2]
zz = prof(re)[0]
b.annotate("%.0f K/km at the ground:\nsuper-adiabatic, unstable" % lrr[0], (lrr[0], zz[0]), xytext=(-8, 52), textcoords="offset points", ha="right", fontsize=8.5, color=ORANGE,
           arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.8))
for lim in (9.8, 6.5):
    k = np.where(lrr < lim)[0][0]
    zc = zz[k - 1] + (zz[k] - zz[k - 1]) * (lrr[k - 1] - lim) / (lrr[k - 1] - lrr[k])
    print(f"RE lapse rate falls below {lim} K/km at z = {zc:.1f} km")
fig.tight_layout()
save(fig, "fig_cl09_re_vs_rce")
