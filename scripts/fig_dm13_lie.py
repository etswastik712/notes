"""DM13 - the Lie derivative as the velocity of a pulled-back vector, flows that fail to commute by st[V,W], and the log-polar chart of the commuting pair E, R."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(13.8, 4.5), gridspec_kw=dict(width_ratios=[1.0, 1.05, 1.0]))

# A: (L_V W)_p for V = y d_x + d_y, W = x d_y at p = (1, 0.5): curve t -> d(theta_{-t}) W_{theta_t p} in T_p R^2 --------------------------------------------
a = axes[0]
p = np.array([1.0, 0.5])
ts = np.linspace(-1.0, 1.0, 200)
w = p[0] + p[1] * ts + ts ** 2 / 2                      # x-coordinate of theta_t(p), W = x d_y
curve = np.column_stack([-ts * w, w])
a.plot(curve[:, 0], curve[:, 1], color=BLUE, lw=2.2)
for t0, col in ((-0.8, MUTED), (0.8, ORANGE)):
    w0 = p[0] + p[1] * t0 + t0 ** 2 / 2
    a.annotate("", xy=(0, w0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=col, lw=1.3, ls="--"))
    a.scatter([-t0 * w0], [w0], color=col, s=26, zorder=4)
    a.text(-t0 * w0 + (0.06 if t0 > 0 else -0.58), w0 + 0.05, "t = %g" % t0, fontsize=8, color=col)
a.annotate("", xy=(0, 1.0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=INK, lw=2.0))
a.text(0.04, 0.4, "W_p = (0, 1)", fontsize=8.6, color=INK)
a.annotate("", xy=(-1.0 * 0.45, 1.0 + 0.5 * 0.45), xytext=(0, 1.0), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.2))
a.text(-1.03, 1.55, "velocity at t = 0:\n(L_V W)_p = [V,W]_p = (−1, 0.5)", fontsize=8.4, color=RED)
a.set_xlim(-1.35, 0.95); a.set_ylim(-0.1, 2.0); a.set_aspect("equal"); a.axhline(0, color=GRID, lw=1); a.axvline(0, color=GRID, lw=1)
a.set_xlabel("component along ∂ₓ in T_pℝ²"); a.set_ylabel("along ∂ᵧ")
a.set_title("A  t ↦ dθ₋ₜ(W at θₜ(p)) ∈ T_pℝ²", fontsize=9.6)

# B: flows of V = d_x and W = x d_y do not commute ----------------------------------------------------------------------------------------------------
b = axes[1]
p0 = np.array([0.3, 0.2]); t = 1.0; s = 1.0
A1 = p0 + np.array([t, 0.0]); A2 = np.array([A1[0], A1[1] + s * A1[0]])             # theta first, then psi
B1 = np.array([p0[0], p0[1] + s * p0[0]]); B2 = B1 + np.array([t, 0.0])             # psi first, then theta
for src, dst, col in ((p0, A1, BLUE), (A1, A2, BLUE), (p0, B1, ORANGE), (B1, B2, ORANGE)):
    b.annotate("", xy=dst, xytext=src, arrowprops=dict(arrowstyle="-|>", color=col, lw=2.0))
b.scatter([p0[0], A2[0], B2[0]], [p0[1], A2[1], B2[1]], color=INK, s=30, zorder=4)
b.annotate("", xy=A2, xytext=B2, arrowprops=dict(arrowstyle="<->", color=RED, lw=1.8))
b.text(0.05, 0.02, "p", fontsize=9.5); b.text(A2[0] + 0.05, A2[1] + 0.02, "ψ_s θ_t (p)", fontsize=8.6, color=BLUE)
b.text(B2[0] + 0.07, B2[1] - 0.25, "θ_t ψ_s (p)", fontsize=8.6, color=ORANGE)
b.text(1.5, 0.95, "gap = st ∂ᵧ\n= st [V, W]", fontsize=8.8, color=RED)
b.text(0.55, -0.08, "θ_t first", fontsize=8.4, color=BLUE, ha="center"); b.text(-0.12, 0.45, "ψ_s first", fontsize=8.4, color=ORANGE, rotation=90, va="center")
b.set_xlim(-0.35, 2.7); b.set_ylim(-0.3, 2.0); b.set_aspect("equal")
b.set_title("B  [∂ₓ, x∂ᵧ] = ∂ᵧ ≠ 0: the flows do not commute", fontsize=9.6)

# C: the commuting pair E = r d_r, R = d_theta is the coordinate frame of log-polar coordinates ---------------------------------------------------------
c = axes[2]
th = np.linspace(0, 2 * np.pi, 200)
for s1 in np.linspace(-1.2, 1.2, 7):
    c.plot(np.exp(s1) * np.cos(th), np.exp(s1) * np.sin(th), color=GRID, lw=1.0)
for s2 in np.linspace(0, 2 * np.pi, 13)[:-1]:
    r = np.linspace(np.exp(-1.2), np.exp(1.2), 20)
    c.plot(r * np.cos(s2), r * np.sin(s2), color=GRID, lw=1.0)
for s1, s2 in ((0.0, 0.5), (0.6, 2.2), (-0.6, 4.0), (0.3, 5.5), (-0.2, 3.2), (0.9, 0.2), (-0.9, 1.5)):
    P = np.exp(s1) * np.array([np.cos(s2), np.sin(s2)])
    Ev = 0.28 * P; Rv = 0.28 * np.array([-P[1], P[0]])
    c.annotate("", xy=P + Ev, xytext=P, arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.6))
    c.annotate("", xy=P + Rv, xytext=P, arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.6))
c.text(1.0, 3.1, "E = ∂/∂s¹ (radial, blue)", color=BLUE, fontsize=8.6); c.text(1.0, 2.8, "R = ∂/∂s² (angular, orange)", color=ORANGE, fontsize=8.6)
c.set_xlim(-3.6, 3.6); c.set_ylim(-3.6, 3.4); c.set_aspect("equal")
c.set_title("C  [E, R] = 0: log-polar coordinates (s¹, s²)", fontsize=9.6)

fig.tight_layout()
fig.text(0.5, -0.03, "A: V = y∂ₓ + ∂ᵧ, W = x∂ᵧ, p = (1, 0.5); finite-difference check of L_V W = [V,W] at 100 random points: error 3.4×10⁻¹⁰. B: θ_t(ψ_s(p)) − ψ_s(θ_t(p)) = −st ∂ᵧ exactly. "
         "C: dΦ(∂/∂s¹) = E, dΦ(∂/∂s²) = R for Φ(s¹,s²) = (eˢ¹ cos s², eˢ¹ sin s²). Numbers: dm_numbers.py (DM13).", ha="center", fontsize=7.8, color=MUTED)
save(fig, "fig_dm13_lie")
