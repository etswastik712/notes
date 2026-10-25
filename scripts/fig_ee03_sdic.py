"""EE03 - sensitive dependence on initial conditions in the Ricker map (r=3.0, K=100): two runs 1e-6 apart, and the growth of the gap."""
from figlib import *

K, r = 100.0, 3.0
f = lambda n: n * np.exp(r * (1 - n / K))
df = lambda n: np.exp(r * (1 - n / K)) * (1 - r * n / K)
# Lyapunov exponent from a long orbit
x = 20.0
for _ in range(2000): x = f(x)
s = 0.0
for _ in range(200000):
    s += np.log(abs(df(x))); x = f(x)
lam = s / 200000
N = 90
a, b = [50.0], [50.0 + 1e-6]
for _ in range(N):
    a.append(f(a[-1])); b.append(f(b[-1]))
a, b = np.array(a), np.array(b)
gap = np.abs(a - b)
fig, (p, q) = plt.subplots(1, 2, figsize=(10.4, 3.8))
t = np.arange(N + 1)
p.plot(t, a, "-o", color=BLUE, ms=3, lw=1.1, label=r"$N_0=50$")
p.plot(t, b, "-o", color=ORANGE, ms=2.5, lw=1.0, alpha=0.9, label=r"$N_0=50.000001$")
p.set_xlabel("generation t"); p.set_ylabel(r"$N_t$"); p.set_ylim(0, 290)
p.set_title("Two runs that start 10⁻⁶ apart", fontsize=10)
p.legend(loc="upper left", ncol=2, fontsize=8.5)
q.semilogy(t, gap, "-o", color=RED, ms=3, lw=1.1)
tt = np.linspace(0, 45, 50)
q.semilogy(tt, 1e-6 * np.exp(lam * tt), color=INK, lw=1.4, ls="--")
q.annotate(f"slope = Lyapunov exponent λ = {lam:.2f} per generation", (24, 1e-6 * np.exp(lam * 24)), xytext=(-30, 36), textcoords="offset points", fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED))
q.axhline(100, color=MUTED, ls=":", lw=1)
q.annotate("gap saturates at the size of the attractor", (50, 130), fontsize=8.3, color=MUTED)
q.set_xlabel("generation t"); q.set_ylabel(r"gap  $|N_t-N_t'|$ (log scale)")
q.set_ylim(1e-7, 1e3)
q.set_title("The gap grows like e^{λt} until it fills the attractor", fontsize=10)
fig.tight_layout(); save(fig, "fig_ee03_sdic")
print("lambda", lam, "first t with gap>10:", int(np.argmax(gap > 10)))
