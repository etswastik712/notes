"""TH09 figure B: dynamics of the postulate - random exchange of quanta, the Boltzmann law from counting, most probable distribution."""
from figlib import *
from math import lgamma, log, comb
from scipy import optimize
def lnC(n, k): return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)
NA_, NB_, q = 300, 200, 100; N = NA_ + NB_
rng = np.random.default_rng(20261104)
osc = np.zeros(N, dtype=int)
for _ in range(q): osc[rng.integers(0, NA_)] += 1
steps = 600000
ii = rng.integers(0, N, size=steps); jj = rng.integers(0, N, size=steps)
cur = int(osc[:NA_].sum()); qA = np.empty(steps + 1, dtype=int); qA[0] = cur
hist = np.zeros(q + 1); occ = np.zeros(60); samples = 0
for t in range(1, steps + 1):
    a_, b_ = ii[t - 1], jj[t - 1]
    if osc[a_] > 0 and a_ != b_:
        osc[a_] -= 1; osc[b_] += 1
        cur += (1 if b_ < NA_ else 0) - (1 if a_ < NA_ else 0)
    qA[t] = cur
    if t > 40000 and t % 20 == 0:
        hist[cur] += 1; samples += 1; np.add.at(occ, np.minimum(osc, 59), 1)
hist /= samples; occ /= occ.sum()
lnOm = lambda x: lnC(x + NA_ - 1, x) + lnC(q - x + NB_ - 1, q - x)
Pex = np.exp(np.array([lnOm(x) for x in range(q + 1)]) - lnC(q + N - 1, q))
fig, axes = plt.subplots(2, 2, figsize=(10.4, 7.8))

a = axes[0, 0]
tt = np.arange(0, 6001)
a.plot(tt, qA[:6001], color=BLUE, lw=0.9)
a.axhspan(60 - 5.36, 60 + 5.36, color=ORANGE, alpha=0.18, label="exact $60\\pm\\sigma$")
a.set_xlabel("steps (one quantum moved per step)"); a.set_ylabel("$q_A(t)$"); a.legend(fontsize=8.5, loc="upper right")
a2 = a.twinx(); a2.plot(tt[::20], [lnOm(x) for x in qA[:6001:20]], color=AQUA, lw=1.4); a2.set_ylabel("$S_{\\rm tot}/k_B$", color=AQUA); a2.set_ylim(215, 270)
a2.spines["right"].set_visible(True)
a.set_title("A  From a very unlikely macrostate to the typical one", fontsize=10)

b = axes[0, 1]
b.bar(range(q + 1), hist, color=BLUE, alpha=0.75, width=0.9, label=f"simulation ({samples} samples)")
b.plot(range(q + 1), Pex, color=ORANGE, lw=1.8, label="exact counting")
b.set_xlim(35, 85); b.set_xlabel("$q_A$"); b.set_ylabel("probability"); b.legend(fontsize=8.5, loc="upper left")
b.set_title("B  Equal weights per microstate reproduce the multiplicity", fontsize=10)

c = axes[1, 0]
n = np.arange(8)
exact = np.array([comb(q - k + N - 2, q - k) / comb(q + N - 1, q) for k in n])
geo = (1 - 1 / 6) * (1 / 6) ** n
c.semilogy(n, occ[:8], "o", color=BLUE, label="simulation")
c.semilogy(n, exact, "-", color=ORANGE, label="exact: $\\binom{q-n+N-2}{q-n}/\\binom{q+N-1}{q}$")
c.semilogy(n, geo, "--", color=MUTED, label="Boltzmann: $(1-r)r^n$, $r=1/6$")
c.set_xlabel("quanta $n$ on one oscillator"); c.set_ylabel("probability"); c.legend(fontsize=8.2)
c.set_title("C  A single oscillator: the Boltzmann law from counting", fontsize=10)

d = axes[1, 1]
eps = np.arange(5)
def occupancies(Ntot, E):
    out = []
    for n4 in range(Ntot + 1):
        for n3 in range(Ntot + 1 - n4):
            for n2 in range(Ntot + 1 - n4 - n3):
                for n1 in range(Ntot + 1 - n4 - n3 - n2):
                    n0 = Ntot - n1 - n2 - n3 - n4
                    if n1 + 2 * n2 + 3 * n3 + 4 * n4 == E: out.append((n0, n1, n2, n3, n4))
    return np.array(out)
f = lambda b: (eps * np.exp(-b * eps)).sum() / np.exp(-b * eps).sum() - 1.0
bb = optimize.brentq(f, 1e-6, 20); fb = np.exp(-bb * eps); fb /= fb.sum()
d.plot(eps, fb, "k-", lw=2, label="Boltzmann, $\\beta\\varepsilon_1=0.566$")
for Nn, col, mk in ((10, AQUA, "o"), (30, BLUE, "s"), (120, ORANGE, "^")):
    occs = occupancies(Nn, Nn)
    lnW = np.array([lgamma(Nn + 1) - sum(lgamma(x + 1) for x in v) for v in occs]); w = np.exp(lnW - lnW.max()); w /= w.sum()
    mean = (w[:, None] * occs).sum(0) / Nn
    d.plot(eps, mean, mk + "--", color=col, label=f"mean over microstates, $N={Nn}$")
d.set_xticks(eps); d.set_xlabel("level $\\varepsilon_i/\\varepsilon_1$"); d.set_ylabel("fraction $N_i/N$ (total energy $=N\\varepsilon_1$)"); d.legend(fontsize=8.2)
d.set_title("D  Equal a priori weights give the Boltzmann distribution", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.012, "Computed in scripts/th09_numbers.py and here (seed 20261104; symmetric move rule, 600 000 steps). After 40 000 steps $\\langle q_A\\rangle=59.9$, $\\sigma=5.1$ (exact 60, 5.36).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_th09b_dynamics")
