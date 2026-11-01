"""DM12 - the time-t maps of V = y d_x + d_y (HW7 Q5), finite-time blow-up of x^2 d_x, and the helicoid flowout."""
from figlib import *
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

fig = plt.figure(figsize=(13.6, 4.6))

# A: the flow of V = y d_x + d_y: images of the unit square under theta_t, t = 0, 1, 2 ---------------------------------------------------------------------
a = fig.add_subplot(1, 3, 1)
th = lambda t, x, y: (x + y * t + t * t / 2, y + t)
u = np.linspace(0, 1, 60)
sq = np.concatenate([np.column_stack([u, 0 * u]), np.column_stack([1 + 0 * u, u]), np.column_stack([1 - u, 1 + 0 * u]), np.column_stack([0 * u, 1 - u])])
for t, col in zip((0.0, 1.0, 2.0), (MUTED, BLUE, ORANGE)):
    X, Y = th(t, sq[:, 0], sq[:, 1])
    a.fill(X, Y, color=col, alpha=0.22)
    a.plot(X, Y, color=col, lw=1.8, label="θ_%g(square)" % t if t else "unit square")
for x0, y0 in ((-0.5, -0.5), (0.0, -0.5), (0.5, -0.5), (1.5, -0.5), (2.5, -0.5)):
    ts = np.linspace(0, 3.2, 80)
    X, Y = th(ts, x0, y0)
    a.plot(X, Y, color=GRID, lw=1.0)
    a.annotate("", xy=(X[-1], Y[-1]), xytext=(X[-5], Y[-5]), arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.0))
a.set_xlim(-1, 7); a.set_ylim(-0.7, 3.4); a.set_aspect("equal"); a.legend(fontsize=7.8, loc="upper left")
a.set_title("A  flow of y∂ₓ + ∂ᵧ: θ_t are diffeomorphisms", fontsize=9.6)

# B: x^2 d_x blows up in finite time; x d_x does not ---------------------------------------------------------------------------------------------------
b = fig.add_subplot(1, 3, 2)
cols = {2.0: BLUE, 1.0: ORANGE, 0.5: AQUA, -2.0: VIOLET}
for x0, col in cols.items():
    t_end = 1 / x0 - 0.012 if x0 > 0 else 1.9
    ts = np.linspace(-0.4, t_end, 400)
    xs = x0 / (1 - x0 * ts)
    m = np.abs(xs) < 12
    b.plot(ts[m], xs[m], color=col, lw=2.0, label=("x₀ = %g" % x0) + ("  (blows up at t = %g)" % (1 / x0) if x0 > 0 else "  (exists for all t > −1/2)"))
    if x0 > 0:
        b.axvline(1 / x0, color=col, lw=0.8, ls=":")
b.set_ylim(-6, 12); b.set_xlim(-0.5, 2.1); b.axhline(0, color=GRID, lw=1)
b.set_xlabel("t"); b.set_ylabel("x(t)")
b.legend(fontsize=7.6, loc="upper right")
b.set_title("B  W = x²∂ₓ is not complete: x₀/(1 − x₀t)", fontsize=9.6)

# C: helicoid flowout of the half-axis S along V = -y d_x + x d_y + d_z -------------------------------------------------------------------------------------
c = fig.add_subplot(1, 3, 3, projection="3d")
tt, ss = np.meshgrid(np.linspace(-2 * np.pi, 2 * np.pi, 90), np.linspace(0.05, 2, 12))
c.plot_surface(ss * np.cos(tt), ss * np.sin(tt), tt, color=BLUE, alpha=0.30, linewidth=0, antialiased=True)
for s0 in (0.6, 1.2, 2.0):
    t1 = np.linspace(-2 * np.pi, 2 * np.pi, 200)
    c.plot(s0 * np.cos(t1), s0 * np.sin(t1), t1, color=ORANGE, lw=1.3)
c.plot([0, 2.1], [0, 0], [0, 0], color=RED, lw=3.0)
c.text(2.1, 0, 0.4, "S", color=RED, fontsize=10)
c.view_init(elev=18, azim=-58)
c.set_xticks([]); c.set_yticks([]); c.set_zticks([-2 * np.pi, 0, 2 * np.pi]); c.set_zticklabels(["−2π", "0", "2π"], fontsize=7.5)
c.set_title("C  flowout of S: Φ(t,s) = (s cos t, s sin t, t)", fontsize=9.6)

fig.tight_layout()
fig.text(0.5, -0.02, "A: unit square and its images under θ₁, θ₂ (diffeomorphisms; area preserved). B: the finite-time blow-up that makes x²∂ₓ incomplete (escape lemma: x leaves every compact set). "
         "C: Φ is an immersion (smallest singular value of dΦ is 1) with dΦ(∂_t) = V∘Φ. Numbers: dm_numbers.py (DM12).", ha="center", fontsize=7.8, color=MUTED)
save(fig, "fig_dm12_flows")
