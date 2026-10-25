"""Orbital geometry and idealised zonal-mean budgets for chapter CL10 (shared by the fig_cl10_*.py scripts).

Insolation: exact daily-mean top-of-atmosphere flux from S, obliquity, eccentricity and the longitude of perihelion,
  Q = S (rho^2/pi) [h0 sin(phi) sin(delta) + cos(phi) cos(delta) sin(h0)],   rho = a/r = (1+e cos(lam-varpi))/(1-e^2).
Annual means use Kepler's second law:  dt = (T/2pi)(1-e^2)^(-1/2) rho^(-2) d(lam), so
  <Q> = (S/pi)(1-e^2)^(-1/2) (1/2pi) * Integral F(phi, delta(lam)) d(lam),   F = h0 sin phi sin delta + cos phi cos delta sin h0.

The zonal-mean TOA budget (absorbed solar, OLR, net) is an IDEALISED, hand-calibrated profile, not satellite data:
it is tuned to the numbers quoted in the course sources (global albedo ~0.29, absorbed tropics/poles ~ 5-6, net radiation
changing sign near 35-40 deg, peak poleward flux 5.8 PW).  Every figure that uses it says so.
"""
import numpy as np

S0 = 1361.0
A_EARTH = 6.371e6
ECC = 0.0167
OBL = np.radians(23.44)
VARPI = np.radians(282.9)          # solar longitude of perihelion (about 3 Jan)


def p2(x):
    return 0.5 * (3 * x**2 - 1)


def p4(x):
    return (35 * x**4 - 30 * x**2 + 3) / 8


def declination(lam, obl=OBL):
    return np.arcsin(np.sin(obl) * np.sin(lam))


def rho(lam, ecc=ECC, varpi=VARPI):
    return (1 + ecc * np.cos(lam - varpi)) / (1 - ecc**2)


def lam_from_day(doy, ecc=ECC, varpi=VARPI, t_peri=3.0, year=365.25):
    """Solar longitude (rad) on day-of-year `doy` (Kepler's equation)."""
    M = 2 * np.pi * (np.asarray(doy, float) - t_peri) / year
    E = M.copy() if isinstance(M, np.ndarray) else M
    for _ in range(30):
        E = E - (E - ecc * np.sin(E) - M) / (1 - ecc * np.cos(E))
    nu = 2 * np.arctan2(np.sqrt(1 + ecc) * np.sin(E / 2), np.sqrt(1 - ecc) * np.cos(E / 2))
    return np.mod(nu + varpi, 2 * np.pi)


def geom(phi, delta):
    """F = h0 sin(phi) sin(delta) + cos(phi) cos(delta) sin(h0) with the polar-day / polar-night limits."""
    phi, delta = np.broadcast_arrays(np.asarray(phi, float), np.asarray(delta, float))
    t = -np.tan(phi) * np.tan(delta)
    h0 = np.where(t >= 1, 0.0, np.where(t <= -1, np.pi, np.arccos(np.clip(t, -1, 1))))   # cos h0 = t; t>=1 polar night, t<=-1 polar day
    return h0 * np.sin(phi) * np.sin(delta) + np.cos(phi) * np.cos(delta) * np.sin(h0)


def daily_insolation(phi, lam, S=S0, obl=OBL, ecc=ECC, varpi=VARPI):
    return S / np.pi * rho(lam, ecc, varpi) ** 2 * geom(phi, declination(lam, obl))


def annual_mean(phi, S=S0, obl=OBL, ecc=ECC, varpi=VARPI, n=2000):
    lam = (np.arange(n) + 0.5) * 2 * np.pi / n
    phi = np.asarray(phi, float)[..., None]
    F = geom(phi, declination(lam, obl))
    return S / np.pi / np.sqrt(1 - ecc**2) * F.mean(axis=-1)


def legendre_p2_coeff(S=S0, **kw):
    """Coefficient S2 in <Q>(phi) = (S/4)[1 + S2 P2(sin phi) + ...]  (c_2 = (5/2) Int f P2 dx on [-1,1])."""
    x = np.linspace(-1, 1, 4001)
    f = annual_mean(np.arcsin(x), S=S, **kw) / (S / 4)
    return 2.5 * np.trapezoid(f * p2(x), x)


# ------------------------------------------------------------------ idealised zonal-mean TOA budget
_X = np.linspace(-1, 1, 4001)
_QX = None


def _qgrid():
    global _QX
    if _QX is None:
        _QX = annual_mean(np.arcsin(_X))
    return _QX


# calibrated by least squares to: global planetary albedo 0.29 (Hartmann), absorbed ~320 (tropics) and ~60 (poles) W m-2 (read
# off slide 10; M&P: ratio 'about six'), net radiation changing sign at ~35-37 deg (slide ~33, Hartmann ~40), peak poleward flux
# 5.8 PW (Hartmann), OLR equatorial dip of ~20 W m-2, flux at 20 deg of ~4 PW (2 atmosphere + 2 ocean, Hartmann)
DEFAULTS = dict(albedo_eq=0.2319, albedo_pole_extra=-0.0143, albedo_x4=0.428, olr_o2=-70.044, olr_dip=37.078, olr_dip_width=9.0)
# result of the fit: albedo 0.290, absorbed eq/pole 319/61 (ratio 5.2), net changes sign at 37 deg, peak flux 5.63 PW,
# net radiation +75 (eq) / -116 (pole), OLR 245 (eq), 263 (25 deg), 177 (pole); flux at 20 deg 4.4 PW


def toa_profiles(phi, albedo_eq=None, albedo_pole_extra=None, albedo_x4=None, olr_o2=None, olr_dip=None, olr_dip_width=None):
    """Return (Q, ASR, OLR, R) in W m-2 on latitudes phi (rad): Q annual-mean insolation, ASR=Q(1-alpha(phi)) with
    alpha = a0 + a1 sin^2 phi + a2 sin^4 phi, OLR = o0 + o2 P2(sin phi) - dip*exp(-(phi/w)^2), o0 fixed so the global-mean net is zero."""
    d = dict(DEFAULTS)
    for k, v in dict(albedo_eq=albedo_eq, albedo_pole_extra=albedo_pole_extra, albedo_x4=albedo_x4, olr_o2=olr_o2, olr_dip=olr_dip,
                     olr_dip_width=olr_dip_width).items():
        if v is not None:
            d[k] = v
    phi = np.asarray(phi, float)
    x = np.sin(phi)
    Q = np.interp(x, _X, _qgrid())
    ASR = Q * (1 - d["albedo_eq"] - d["albedo_pole_extra"] * x**2 - d["albedo_x4"] * x**4)
    shape = d["olr_o2"] * p2(x) - d["olr_dip"] * np.exp(-(np.degrees(phi) / d["olr_dip_width"]) ** 2)
    Qg = _qgrid()
    ASRg = (Qg * (1 - d["albedo_eq"] - d["albedo_pole_extra"] * _X**2 - d["albedo_x4"] * _X**4)).mean()
    ph = np.arcsin(_X)
    shg = (d["olr_o2"] * p2(_X) - d["olr_dip"] * np.exp(-(np.degrees(ph) / d["olr_dip_width"]) ** 2)).mean()
    OLR = (ASRg - shg) + shape
    return Q, ASR, OLR, ASR - OLR


def poleward_flux(phi, R):
    """F(phi) = 2 pi a^2 * Integral_{-pi/2}^{phi} R cos(phi') dphi'   [W], cumulative trapezoid (northward positive)."""
    phi = np.asarray(phi, float)
    integrand = R * np.cos(phi)
    cum = np.concatenate([[0.0], np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(phi))])
    return 2 * np.pi * A_EARTH**2 * cum


def ocean_flux(phi_deg):
    """Schematic ocean transport (PW) through the quoted anchor: 2.0 PW at 20 deg, vanishing at the equator and the poles
    (odd in latitude).  NOT data: a smooth curve through the value Hartmann quotes."""
    a = np.abs(phi_deg) / 20.0
    return np.sign(phi_deg) * 2.0 * a * np.exp(1 - a) * np.cos(np.radians(phi_deg)) / np.cos(np.radians(20.0))
