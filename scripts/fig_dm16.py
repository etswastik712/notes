"""DM16 - Frobenius in pictures: flat coordinates for Lee Example 19.14, the failure of integrability for Lee Example 19.1(d), holonomy = area."""
from figlib import *
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from scipy.integrate import solve_ivp

fig = plt.figure(figsize=(14.2, 4.8))

# A: integral surfaces z = xy + c of D = span{x d_x + d_y + x(y+1) d_z, d_x + y d_z}; flows alpha_t, beta_t from the z-axis ---------------------------
a = fig.add_subplot(1, 3, 1, projection="3d")
g = np.linspace(-1, 1, 21)
GX, GY = np.meshgrid(g, g)
for c, col in ((-1.0, BLUE), (0.0, AQUA), (1.0, ORANGE)):
    a.plot_surface(GX, GY, GX * GY + c, color=col, alpha=0.22, linewidth=0, antialiased=True)
w0 = 0.0
u = np.linspace(-1, 1, 40)
# the coordinate curves of the flat chart through (0,0,w0): beta_v then alpha_u
bv = np.array([(0, v, w0) for v in u])
a.plot(bv[:, 0], bv[:, 1], bv[:, 2], color=INK, lw=1.8)
for v in (-0.6, 0.0, 0.6):
    au = np.array([(uu, v, w0 + uu * v) for uu in u])
    a.plot(au[:, 0], au[:, 1], au[:, 2], color=RED, lw=1.5)
a.text(0.0, 0.95, w0 + 0.08, "β-flow", color=INK, fontsize=8.4)
a.text(0.85, -0.55, w0 - 0.65, "α-flows", color=RED, fontsize=8.4)
a.set_xlim(-1, 1); a.set_ylim(-1, 1); a.set_zlim(-2.1, 2.1)
a.view_init(elev=18, azim=-62)
a.set_xlabel("x", fontsize=8); a.set_ylabel("y", fontsize=8); a.set_zlabel("z", fontsize=8)
a.set_title("A  Lee 19.14: leaves  z − xy = −1, 0, 1", fontsize=9.8)

# B: Lee 19.1(d): D = span{d_x + y d_z, d_y}: two routes from the origin to the same (x,y) end at different heights ---------------------------------
b = fig.add_subplot(1, 3, 2, projection="3d")
s = t = 0.7
tt = np.linspace(0, 1, 40)
# route 1: X for time s (y = 0, dz = 0) then Y for time t
r1 = np.vstack([np.c_[s * tt, 0 * tt, 0 * tt], np.c_[s + 0 * tt, t * tt, 0 * tt]])
# route 2: Y for time t (dz = 0 since X absent) then X for time s at height y = t: dz = y dx = t dx
r2 = np.vstack([np.c_[0 * tt, t * tt, 0 * tt], np.c_[s * tt, t + 0 * tt, t * s * tt]])
b.plot(r1[:, 0], r1[:, 1], r1[:, 2], color=BLUE, lw=2.6)
b.plot(r2[:, 0], r2[:, 1], r2[:, 2], color=ORANGE, lw=2.6)
b.plot([s, s], [t, t], [0, s * t], color=RED, lw=3.2)
b.scatter([0, s, s], [0, t, t], [0, 0, s * t], color=INK, s=22)
b.text(s - 0.52, t + 0.05, s * t / 2 + 0.07, "gap st = −[X,Y]·st", color=RED, fontsize=8.4)
b.text(0.35, -0.02, 0.0, "X then Y", color=BLUE, fontsize=8.4)
b.text(0.0, 0.36, 0.26, "Y then X", color=ORANGE, fontsize=8.4)
b.set_xlim(0, 0.9); b.set_ylim(0, 0.9); b.set_zlim(0, 0.6)
b.view_init(elev=24, azim=-58)
b.set_xlabel("x", fontsize=8); b.set_ylabel("y", fontsize=8); b.set_zlabel("z", fontsize=8)
b.set_title("B  Lee 19.1(d): no integral surface", fontsize=9.8)

# C: holonomy of the lift of a loop = c * area ----------------------------------------------------------------------------------------------------------
c = fig.add_subplot(1, 3, 3)
def gap_square(e, k):
    pos = np.zeros(3)
    for (dx, dy) in ((e, 0), (0, e), (-e, 0), (0, -e)):
        sol = solve_ivp(lambda s_, u_: [dx, dy, k * u_[0] * dy], [0, 1], pos, rtol=1e-12, atol=1e-14)
        pos = sol.y[:, -1]
    return pos[2]
def gap_circle(r, k):
    sol = solve_ivp(lambda s_, u_: [-r * 2 * np.pi * np.sin(2 * np.pi * s_), r * 2 * np.pi * np.cos(2 * np.pi * s_), k * u_[0] * r * 2 * np.pi * np.cos(2 * np.pi * s_)], [0, 1], [r, 0, 0], rtol=1e-12, atol=1e-14)
    return sol.y[2, -1]
for k, col in ((1.0, BLUE), (2.0, ORANGE)):
    es = np.linspace(0.05, 0.6, 7)
    c.plot(es ** 2, [gap_square(e, k) for e in es], "o", color=col, ms=5, label="squares, c = %g" % k)
    rs = np.linspace(0.05, 0.4, 6)
    c.plot(np.pi * rs ** 2, [gap_circle(r, k) for r in rs], "s", color=col, ms=5, mfc="none", label="circles, c = %g" % k)
    A = np.linspace(0, 0.5, 3)
    c.plot(A, k * A, color=col, lw=1.2, ls="--")
c.set_xlabel("area enclosed by the loop in the (x, y)-plane"); c.set_ylabel("height gap  Δz after the horizontal lift")
c.legend(fontsize=8, loc="upper left", frameon=False)
c.set_title("C  Δz = c · area  for  D = span{∂ₓ, ∂ᵧ + c x ∂_z}", fontsize=9.8)

fig.tight_layout()
fig.text(0.5, -0.03, "A: the flat coordinates (u,v,w) = (x, y, z − xy) of §4: u-curves are flows of V, v-curves flows of W, the surfaces w = const are the leaves.  "
         "B: with X = ∂ₓ + y∂_z, Y = ∂ᵧ the two routes (X then Y; Y then X) from the origin differ by st in z: [X,Y] = −∂_z ∉ D (§2).  "
         "C: horizontal lifts of closed loops (ODE) end Δz = c · area, linear to 1e-6 (Stokes: ∮ x dy = area).  Numbers: dm_numbers2.py (DM16).",
         ha="center", fontsize=7.6, color=MUTED, wrap=True)
save(fig, "fig_dm16_frobenius")
