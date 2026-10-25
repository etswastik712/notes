"""Helpers shared by the CL05/CL06 figures: US Standard Atmosphere 1976 (0-84.852 km, geopotential heights), moist-air formulae."""
import numpy as np

G0 = 9.80665          # m s-2 (standard)
R_STD = 287.053       # J kg-1 K-1 (dry air, as used in the standard atmosphere)
RD = 287.05
EPS = 0.62198         # M_w / M_d
P0 = 1013.25          # hPa
T0 = 288.15           # K

# layer bases (geopotential km) and lapse rates (K per km): US Standard Atmosphere 1976
HB = np.array([0.0, 11.0, 20.0, 32.0, 47.0, 51.0, 71.0, 84.852])
LAPSE = np.array([-6.5, 0.0, 1.0, 2.8, 0.0, -2.8, -2.0])


def _bases():
    T = [T0]
    p = [P0]
    for i, L in enumerate(LAPSE):
        dz = HB[i + 1] - HB[i]
        Tt = T[-1] + L * dz
        if L == 0:
            pt = p[-1] * np.exp(-G0 * dz * 1e3 / (R_STD * T[-1]))
        else:
            pt = p[-1] * (Tt / T[-1]) ** (-G0 / (R_STD * L * 1e-3))
        T.append(Tt)
        p.append(pt)
    return np.array(T), np.array(p)


TB, PB = _bases()


def std_atm(Z):
    """Temperature (K) and pressure (hPa) of the standard atmosphere at geopotential height Z (km, array or scalar)."""
    Z = np.atleast_1d(np.asarray(Z, float))
    T = np.empty_like(Z)
    p = np.empty_like(Z)
    for j, z in enumerate(Z):
        i = min(np.searchsorted(HB, z, side="right") - 1, len(LAPSE) - 1)
        L = LAPSE[i]
        dz = z - HB[i]
        T[j] = TB[i] + L * dz
        if L == 0:
            p[j] = PB[i] * np.exp(-G0 * dz * 1e3 / (R_STD * TB[i]))
        else:
            p[j] = PB[i] * (T[j] / TB[i]) ** (-G0 / (R_STD * L * 1e-3))
    return T, p


def e_sat(Tk):
    """Saturation vapour pressure over water (hPa), Bolton (1980) form."""
    Tc = np.asarray(Tk, float) - 273.15
    return 6.112 * np.exp(17.67 * Tc / (Tc + 243.5))


def q_from_e(e, p):
    """Specific humidity from vapour pressure e and total pressure p (same units)."""
    return EPS * e / (p - (1 - EPS) * e)


def virtual_T(T, q):
    """Exact: T_v = T (1 + (1/eps - 1) q)."""
    return T * (1 + (1 / EPS - 1) * q)
