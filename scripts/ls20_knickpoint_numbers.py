"""LS20 addition (2026-11-12): knickpoint migration under linear stream power in chi space; what getlocation computes.
    .venv/bin/python -W ignore scripts/ls20_knickpoint_numbers.py"""
import numpy as np
from scipy import integrate

m, h = 0.45, 1.67
L = 30e3                                     # channel length from outlet (x = 0) to divide (x = L)
A_out = 1e8                                  # drainage area at the outlet, 100 km^2
ka = A_out / L ** h
A = lambda x: ka * (L - x) ** h              # Hack-type area along the channel (distance upstream x)
K = 1e-6                                     # m^(1-2m) yr^-1, n = 1
xs = np.linspace(0, L * 0.999, 40001)
chi = np.concatenate([[0], integrate.cumulative_trapezoid(A(xs) ** (-m), xs)])[: len(xs)]   # A0 = 1 m^2, chi in m^(1-?)... (units with A0 = 1)
print("== Knickpoint celerity C = K A^m (n = 1) and chi = int (A0/A)^m dx (A0 = 1 m^2)")
print("  A(x): %.2e m^2 at the outlet, %.2e m^2 at 20 km upstream; C = K A^m: %.4f m/yr at the outlet, %.4f m/yr at 20 km (celerity falls upstream as A falls)" % (A(0), A(20e3), K * A(0) ** m, K * A(20e3) ** m))
def x_of_chi(c):
    return np.interp(c, chi, xs)
for x0 in (0.0, 2e3, 6e3):
    # integrate dx/dt = K A(x)^m for t = 2 Myr
    sol = integrate.solve_ivp(lambda t, y: K * A(y[0]) ** m, [0, 2e6], [x0], rtol=1e-10, atol=1e-6)
    xt = sol.y[0, -1]
    c0 = np.interp(x0, xs, chi)
    xchi = x_of_chi(c0 + K * 2e6)
    print("  knickpoint starting %5.0f m upstream of the outlet: after 2 Myr ODE %9.1f m; from chi(x_t) = chi(x_0) + K t: %9.1f m (difference %.2f m); distance moved %.0f m" % (x0, xt, xchi, abs(xt - xchi), xt - x0))
print("  chi advances by the same amount K t = %.3f (units of chi) for every knickpoint: dchi/dt = A^-m dx/dt = K; equal steps in chi are unequal steps in real distance" % (K * 2e6))
print("\n== what getlocation(S, chi_values) returns: the nodes where chi = a given value (here by interpolation along one stream)")
cvals = np.linspace(chi.min(), chi.max(), 500)
pos = x_of_chi(cvals)
print("  500 chi values between %.1f and %.1f give positions from %.0f m to %.0f m; spacing is LARGE downstream (A large, chi grows slowly with x) and small upstream (equal steps in chi are equal time steps, and the knickpoint covers A^m dchi in distance): the first 100 are spread over %.1f km, the last 100 over %.1f km" % (chi.min(), chi.max(), pos[0], pos[-1], (pos[99] - pos[0]) / 1e3, (pos[-1] - pos[-100]) / 1e3))
print("  m range of natural channels 0.3 to 0.8 (the note): celerity ratio between A = 1e8 and 1e6 m^2: m = 0.3: %.2f, m = 0.45: %.2f, m = 0.8: %.2f" % tuple((1e8 / 1e6) ** mm for mm in (0.3, 0.45, 0.8)))
