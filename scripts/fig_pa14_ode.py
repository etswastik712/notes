"""PA14 - Picard iterates, blow-up and non-uniqueness, and the pendulum phase portrait (state-space reduction)."""
from figlib import *
from scipy.integrate import solve_ivp

fig = plt.figure(figsize=(13.4, 4.6))
gs = fig.add_gridspec(2, 3, width_ratios=[1, 1, 1.05], hspace=0.55, wspace=0.28)

# A: Picard iteration for x' = x -------------------------------------------------------------------------------------------
a = fig.add_subplot(gs[:, 0])
tt = np.linspace(0, 2, 300)
a.plot(tt, np.exp(tt), color=INK, lw=2.2, label="e^t (exact)")
poly = np.ones_like(tt)
term = np.ones_like(tt)
cols = [ORANGE, AQUA, VIOLET, BLUE]
for k in range(1, 5):
    term = term * tt / k
    poly = poly + term
    a.plot(tt, poly, color=cols[k - 1], lw=1.3, label=f"iterate {k}")
a.set_ylim(0.8, 8); a.set_xlabel("t"); a.legend(fontsize=8.2, loc="upper left")
a.text(0.02, 6.1, "x_{k+1}(t) = 1 + ∫₀ᵗ x_k\nthe k-th iterate is the\nTaylor polynomial of e^t", fontsize=8.6, color=INK, va="top", transform=a.transData)
a.set_title("A  Picard iteration for x′ = x", fontsize=10)

# B1: blow-up --------------------------------------------------------------------------------------------------------------------
b1 = fig.add_subplot(gs[0, 1])
for x0, c in ((0.5, AQUA), (1.0, BLUE), (2.0, ORANGE)):
    t_ = np.linspace(0, 0.985 / x0, 300)
    b1.plot(t_, x0 / (1 - x0 * t_), color=c, lw=1.8, label=f"x₀ = {x0:g}, escapes at t = {1 / x0:g}")
    b1.axvline(1 / x0, color=c, lw=0.8, ls=":")
b1.set_ylim(0, 40); b1.set_xlim(0, 2.1); b1.legend(fontsize=7.6, loc="upper right")
b1.set_title("B  x′ = x²: no solution after 1/x₀", fontsize=9.6)

# B2: non-uniqueness -------------------------------------------------------------------------------------------------------------
b2 = fig.add_subplot(gs[1, 1])
t_ = np.linspace(0, 3, 300)
b2.plot(t_, np.zeros_like(t_), color=MUTED, lw=2, label="x = 0")
for c0, col in ((0, BLUE), (1, ORANGE), (2, AQUA)):
    tc = np.linspace(c0, 3, 200)
    b2.plot(tc, (tc - c0) ** 2 / 4, color=col, lw=1.6)
b2.text(1.55, 1.6, "x = (t − c)²/4, c ≥ 0", fontsize=8.4, color=INK)
b2.legend(fontsize=7.8, loc="upper left"); b2.set_xlabel("t")
b2.set_title("x′ = √|x|, x(0) = 0: not unique", fontsize=9.6)

# C: pendulum phase portrait -----------------------------------------------------------------------------------------------------
c = fig.add_subplot(gs[:, 2])
for th0 in (0.4, 0.9, 1.5, 2.1, 2.7, 3.0):
    sol = solve_ivp(lambda _, s: [s[1], -np.sin(s[0])], (0, 60), [th0, 0], rtol=1e-10, atol=1e-12, max_step=0.05)
    c.plot(sol.y[0], sol.y[1], color=BLUE, lw=1.1)
th = np.linspace(-np.pi, np.pi, 400)
c.plot(th, 2 * np.cos(th / 2), color=RED, lw=1.8); c.plot(th, -2 * np.cos(th / 2), color=RED, lw=1.8)
for v0 in (2.3, 2.8):
    sol = solve_ivp(lambda _, s: [s[1], -np.sin(s[0])], (0, 6), [-np.pi, v0], rtol=1e-10, atol=1e-12, max_step=0.05)
    c.plot(sol.y[0], sol.y[1], color=VIOLET, lw=1.0)
    c.plot(-sol.y[0], -sol.y[1], color=VIOLET, lw=1.0)
c.text(-3.05, 2.55, "separatrix ω = ±2 cos(θ/2)", color=RED, fontsize=8.4)
c.text(-3.05, -2.75, "θ″ = −sin θ  ⇔  (θ, ω)′ = (ω, −sin θ)\nperiods (g/l = 1): 6.2871 (6°), 7.4163 (90°), 10.3232 (143°)", fontsize=8.2, color=INK)
c.set_xlim(-3.3, 3.3); c.set_ylim(-3.1, 3.0); c.set_xlabel("θ"); c.set_ylabel("ω")
c.set_title("C  pendulum as a first-order system", fontsize=10)

fig.text(0.5, -0.02, "A: iterates of the Picard map; B: finite escape time and non-uniqueness when the Lipschitz condition fails; C: the state-space reduction "
         "of a second-order equation. Numbers: pa14_numbers.py.", ha="center", fontsize=8, color=MUTED)
save(fig, "fig_pa14_ode")
