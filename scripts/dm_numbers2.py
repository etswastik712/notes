"""Differential Geometry vault, DM16-DM17 (Frobenius, foliations, weakly embedded submanifolds, Lie subgroups): numbers quoted, recomputed.

    .venv/bin/python -W ignore scripts/dm_numbers2.py            # DM16 and DM17
    .venv/bin/python -W ignore scripts/dm_numbers2.py DM17

Added 2026-11-07 after the MT3184 slides DG27-DG30 and HW10 arrived (they follow Lee Ch. 19-20).
"""
import sys

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

x, y, z = sp.symbols("x y z", real=True)
COORDS = (x, y, z)


def apply(V, f):
    """V = (V^x, V^y, V^z) acting on f."""
    return sum(V[i] * sp.diff(f, COORDS[i]) for i in range(3))


def bracket(V, W):
    return tuple(sp.simplify(apply(V, W[i]) - apply(W, V[i])) for i in range(3))


def coords_in(frame, vec):
    """Solve vec = sum a_i frame_i pointwise (least squares symbolic); returns coefficients or None."""
    a = sp.symbols("a0:%d" % len(frame))
    eqs = [sp.simplify(sum(a[i] * frame[i][j] for i in range(len(frame))) - vec[j]) for j in range(3)]
    sol = sp.solve(eqs, a, dict=True)
    return sol[0] if sol else None


def dm16():
    print("== DM16 Distributions, Involutivity and the Frobenius Theorem")
    # 1. Lee Example 19.1(d): X = d_x + y d_z, Y = d_y  -> [X,Y] = -d_z, not in D
    X = (1, 0, y)
    Y = (0, 1, 0)
    B = bracket(X, Y)
    M = sp.Matrix([X, Y, B])
    print("  Lee 19.1(d): D = span{d_x + y d_z, d_y}; [X,Y] = %s; det[X,Y,[X,Y]] = %s -> not involutive" % (B, sp.simplify(M.det())))
    # the pairing with the defining form omega = dz - y dx :  omega(X) = y - y = 0, omega(Y) = 0
    # d omega = -dy ^ dx = dx ^ dy ; omega ^ d omega = dz ^ dx ^ dy = +dx dy dz  (cyclic) -> nonzero
    print("  omega = dz - y dx annihilates X,Y; d(omega) = dx^dy; omega^d omega = dz^dx^dy = +1 dx^dy^dz != 0  (Frobenius criterion fails)")

    # 2. Lee Example 19.14
    X = (x, 1, x * (y + 1))
    Y = (1, 0, y)
    B = bracket(X, Y)
    c = coords_in([X, Y], B)
    print("  Lee 19.14: X = x d_x + d_y + x(y+1) d_z, Y = d_x + y d_z;  [X,Y] = %s = %s  (= -Y: involutive)" % (B, c))
    V = Y
    W = tuple(sp.simplify(X[i] - x * Y[i]) for i in range(3))
    print("    V = Y, W = X - xY = %s" % (W,))
    print("    [V,W] = %s (commute)" % (bracket(V, W),))
    w = z - x * y
    print("    w = z - xy:  X(w) = %s, Y(w) = %s, V(w) = %s, W(w) = %s -> level sets of w are integral manifolds" % (sp.simplify(apply(X, w)), sp.simplify(apply(Y, w)), sp.simplify(apply(V, w)), sp.simplify(apply(W, w))))
    # flows alpha_t(x,y,z) = (x+t, y, z+ty), beta_t = (x, y+t, z+tx)
    t = sp.symbols("t")
    alpha = (x + t, y, z + t * y)
    beta = (x, y + t, z + t * x)
    print("    alpha_t: d/dt = %s (should equal V at alpha_t = %s)" % (tuple(sp.diff(a, t) for a in alpha), tuple(v.subs({x: alpha[0], y: alpha[1], z: alpha[2]}) if hasattr(v, "subs") else v for v in V)))
    print("    beta_t : d/dt = %s (should equal W at beta_t = %s)" % (tuple(sp.diff(a, t) for a in beta), tuple(v.subs({x: beta[0], y: beta[1], z: beta[2]}) if hasattr(v, "subs") else v for v in W)))
    u, v, ww = sp.symbols("u v w")
    Phi = tuple(sp.simplify(a.subs({x: x, y: y, z: z})) for a in alpha)  # placeholder to keep shapes
    # Phi(u,v,w) = alpha_u(beta_v(0,0,w)) = alpha_u(0, v, w) = (u, v, w + u v)
    b0 = tuple(a.subs({x: 0, y: 0, z: ww, t: v}) for a in beta)
    Phi = tuple(sp.simplify(a.subs({x: b0[0], y: b0[1], z: b0[2], t: u})) for a in alpha)
    print("    Phi(u,v,w) = alpha_u o beta_v (0,0,w) = %s;  inverse (x,y,z - xy)" % (Phi,))
    # check numerically that the level set w = const is tangent to D at random points
    rng = np.random.default_rng(3)
    err = 0.0
    for _ in range(200):
        p = rng.normal(size=3)
        grad = np.array([-p[1], -p[0], 1.0])  # gradient of z - xy
        for F in (X, Y):
            Fp = np.array([float(sp.N(f.subs({x: p[0], y: p[1], z: p[2]}))) if hasattr(f, "subs") else float(f) for f in F])
            err = max(err, abs(grad @ Fp))
    print("    max |dw(X)|,|dw(Y)| at 200 random points: %.1e" % err)

    # 3. contact distribution: horizontal lift of a closed loop in the xy-plane for D = span{d_x, d_y + c x d_z}: dz = c x dy
    def lift(path_fn, c, T=1.0):
        # path_fn(s) -> (x, y, dx/ds, dy/ds); dz/ds = c x dy/ds
        def rhs(s, u):
            xx, yy, zz = u
            px, py, dx, dy = path_fn(s)
            return [dx, dy, c * xx * dy]
        sol = solve_ivp(rhs, [0, T], [0.0, 0.0, 0.0], rtol=1e-11, atol=1e-13)
        return sol.y[:, -1]

    def square(e):
        # four legs: +x, +y, -x, -y, each of duration 1/4 (speed 4e)
        def f(s):
            k = int(min(s * 4, 3.999999))
            vel = [(4 * e, 0), (0, 4 * e), (-4 * e, 0), (0, -4 * e)][k]
            return (0, 0, vel[0], vel[1])
        return f
    for e in (0.5, 0.25, 0.1):
        # integrate leg by leg for accuracy
        pos = np.zeros(3)
        legs = [(e, 0), (0, e), (-e, 0), (0, -e)]
        for (dx, dy) in legs:
            sol = solve_ivp(lambda s, u: [dx, dy, 1.0 * u[0] * dy], [0, 1], pos, rtol=1e-12, atol=1e-14)
            pos = sol.y[:, -1]
        print("  contact distribution c=1, square loop of side %.2f: end point %s, gap in z = %.6f (= area %.6f)" % (e, np.round(pos, 6), pos[2], e * e))
    # circle of radius r: gap = c * pi r^2 (by Stokes: oint x dy = area)
    for r in (0.5, 0.25):
        sol = solve_ivp(lambda s, u: [-r * 2 * np.pi * np.sin(2 * np.pi * s), r * 2 * np.pi * np.cos(2 * np.pi * s), u[0] * r * 2 * np.pi * np.cos(2 * np.pi * s)], [0, 1], [r, 0, 0], rtol=1e-12, atol=1e-14)
        print("  circle radius %.2f (starting at (r,0)): gap = %.6f vs pi r^2 = %.6f" % (r, sol.y[2, -1], np.pi * r * r))

    # 4. Lee Problem 19-4: D = span{X = y d_z - z d_y, Y = z d_x - x d_z} on the positive octant
    X = (0, -z, y)
    Y = (z, 0, -x)
    B = bracket(X, Y)
    c = coords_in([X, Y], B)
    print("  Lee Problem 19-4: [X,Y] = %s = %s -> involutive; r^2 = x^2+y^2+z^2: X(r^2) = %s, Y(r^2) = %s -> leaves = spheres" % (B, c, sp.simplify(apply(X, x**2 + y**2 + z**2)), sp.simplify(apply(Y, x**2 + y**2 + z**2))))

    # 5. thermodynamics: delta Q = dU + P dV, P = 2U/(3V) (monatomic ideal gas, U = (3/2) n R T): integrating factor 1/U (i.e. 1/T)
    U, V = sp.symbols("U V", positive=True)
    om = (sp.Integer(1), 2 * U / (3 * V))  # coefficients of dU, dV
    dom = sp.diff(om[1], U) - sp.diff(om[0], V)  # coefficient of dU^dV in d(om)
    om2 = (om[0] / U, om[1] / U)
    dom2 = sp.simplify(sp.diff(om2[1], U) - sp.diff(om2[0], V))
    print("  delta Q = dU + (2U/3V) dV: d(delta Q) = %s dU^dV (not closed); delta Q / U has d(...) = %s -> exact: S/(nR) = (3/2) ln U + ln V" % (sp.simplify(dom), dom2))
    R = 8.314462618
    print("    one mole, V doubles at fixed T: Delta S = R ln 2 = %.3f J/K; U triples at fixed V: Delta S = (3/2) R ln 3 = %.3f J/K" % (R * np.log(2), 1.5 * R * np.log(3)))

    # 6. generic distributions are not involutive: random polynomial frames
    rng = np.random.default_rng(5)
    nonivl = 0
    trials = 400
    for _ in range(trials):
        cf = rng.normal(size=(2, 3, 3))
        Xr = tuple(sum(cf[0, i, k] * COORDS[k] for k in range(3)) + 1 * (i == 0) for i in range(3))
        Yr = tuple(sum(cf[1, i, k] * COORDS[k] for k in range(3)) + 1 * (i == 1) for i in range(3))
        p = rng.normal(size=3)
        sub = {x: p[0], y: p[1], z: p[2]}
        Bv = bracket(Xr, Yr)
        Mm = np.array([[float(f.subs(sub)) if hasattr(f, "subs") else float(f) for f in vec] for vec in (Xr, Yr, Bv)])
        if abs(np.linalg.det(Mm)) > 1e-9:
            nonivl += 1
    print("  random affine frames on R^3 (rank 2): %d of %d have [X,Y] outside span{X,Y} at the sample point (involutivity is a non-generic condition)" % (nonivl, trials))


def dm17():
    print("== DM17 Foliations, Weakly Embedded Submanifolds and Lie Subgroups")
    # 1. the linear foliation of T^2 with slope theta: leaf t -> (t mod 1, theta t mod 1)
    th = np.sqrt(2.0)
    print("  irrational slope sqrt2: crossings of the circle x = 1/2 (a transversal in a flat chart) by one leaf, after N turns")
    for N in (10, 100, 1000, 10000, 100000):
        pts = np.sort((th * (0.5 + np.arange(N))) % 1.0)
        gaps = np.diff(np.concatenate([pts, [pts[0] + 1.0]]))
        print("    N = %6d: max gap = %.3e (N * max gap = %.3f), distinct gap sizes (to 1e-9) = %d" % (N, gaps.max(), N * gaps.max(), len(set(np.round(gaps, 9)))))
    p, q = 3, 5
    pts = np.sort(np.unique(np.round(((p / q) * (0.5 + np.arange(1000))) % 1.0, 12)))
    print("  rational slope 3/5: the crossings repeat after q = 5 turns; distinct crossing points = %d (spacing %.3f)" % (len(pts), 1 / q))
    # 2. figure eight
    beta = lambda tt: np.array([np.sin(2 * tt), np.sin(tt)])
    eps = 1e-3
    t1, t2 = 1.5 * np.pi - eps, 1.5 * np.pi + eps
    print("  figure eight G(t) = (sin 2t, sin t): G(3pi/2 - eps) = %s, G(3pi/2 + eps) = %s (close in the plane); on S with beta on (-pi/2, 3pi/2), beta^-1(G) = %.4f then %.4f: jump 2pi" % (np.round(beta(t1), 4), np.round(beta(t2), 4), t1, t2 - 2 * np.pi))
    # 3. so(2,1): F = x^2 + y^2 - z^2 on R^3 minus origin, fields tangent to level sets
    F = x**2 + y**2 - z**2
    Rz = (y, -x, 0)   # rotation about z
    B1 = (z, 0, x)    # boost in xz
    B2 = (0, z, y)    # boost in yz
    for name, Vv in (("R", Rz), ("B1", B1), ("B2", B2)):
        print("    %s(F) = %s" % (name, sp.simplify(apply(Vv, F))))
    print("    [R,B1] = %s,  [R,B2] = %s,  [B1,B2] = %s  (so(2,1) relations)" % (bracket(Rz, B1), bracket(Rz, B2), bracket(B1, B2)))
    print("    level sets of F: c > 0 one sheet (connected), c = 0 minus origin: 2 cone nappes, c < 0: 2 sheets (z^2 = x^2+y^2-c >= -c > 0 so z != 0 and sign(z) separates)")
    # check rank of D = ker dF equals 2 away from the origin and det of (R,B1,B2) = 0
    Mm = sp.Matrix([Rz, B1, B2])
    print("    det[R,B1,B2] = %s (the three fields are dependent; they span the rank-2 distribution ker dF)" % sp.factor(Mm.det()))
    # 4. Aff(1)+ example: left-invariant fields and subgroups
    a, b = sp.symbols("a b", real=True)
    # group law (a,b)(a',b') = (a a', a b' + b); left-invariant fields X1 = a d_a, X2 = a d_b
    L = lambda g, h: (g[0] * h[0], g[0] * h[1] + g[1])
    h = (sp.symbols("a1", positive=True), sp.symbols("b1", real=True))
    g = (a, b)
    gh = L(g, h)
    # d/ds at h=e in direction (da,db) -> left-invariant field value at g: (a*da, a*db)
    print("  Aff(1)+ with (a,b)(a',b') = (aa', ab'+b): left-invariant fields X1 = a d_a, X2 = a d_b; leaf of span{X1} through e: b = 0, closed under product: %s" % (L((a, 0), (h[0], 0)),))
    print("    exp(t(X1+X2)) via matrices [[a,b],[0,1]]: generator [[1,1],[0,0]] -> exp = [[e^t, e^t-1],[0,1]]: the subgroup {b = a - 1}")
    from scipy.linalg import expm
    for tt in (0.0, 0.7, -1.3):
        E = expm(tt * np.array([[1.0, 1.0], [0.0, 0.0]]))
        print("      t = %5.2f: (a,b) = (%.6f, %.6f), b - (a - 1) = %.1e" % (tt, E[0, 0], E[0, 1], E[0, 1] - (E[0, 0] - 1)))
    # 5. HW10 Q1: connectedness is needed. G = Z/2, Phi = trivial, Psi = sign: same differential (0)
    print("  HW10 Q1: G = {+1,-1} = Z/2, H = {+1,-1}; Phi = trivial, Psi = id: both have Phi_* = Psi_* = 0 (Lie(G) = 0), Phi != Psi: connectedness of G is needed")
    # 6. dense line in T^2 as the connected Lie subgroup of h = span(1, sqrt2); {X : exp(tX) in H for all t}
    print("  dense line H = {(s, sqrt2 s) mod Z^2}: H + Z^2 = {(u,v): v - sqrt2 u in Z + sqrt2 Z}; X = (a,b) has exp(tX) in H for all t iff (b - sqrt2 a) t in the countable set Z + sqrt2 Z for all t iff b = sqrt2 a")
    # 7. Dirichlet-type density of the irrational line: closest approach of H to a target after |s| <= T
    rng = np.random.default_rng(1)
    targets = rng.random((6, 2))
    for T in (10, 100, 1000, 10**4, 10**5):
        worst = 0.0
        for (ta, tb) in targets:
            m = np.arange(0, T + 1)
            s = ta + m  # first coordinate = ta (mod 1)
            v = (th * s) % 1.0
            d = np.abs(((v - tb + 0.5) % 1.0) - 0.5).min()
            worst = max(worst, d)
        print("    T = %6d: worst distance of the leaf to 6 random targets (first coordinate fixed) = %.2e" % (T, worst))


CHAPTERS = {"DM16": dm16, "DM17": dm17}

if __name__ == "__main__":
    which = sys.argv[1:] or sorted(CHAPTERS)
    for k in which:
        CHAPTERS[k]()
