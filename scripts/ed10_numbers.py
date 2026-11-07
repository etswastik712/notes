"""ED10 numbers (dipole radiation). .venv/bin/python -W ignore scripts/ed10_numbers.py
G = Griffiths Ch.11, J = Jackson Ch.9, 14.2."""
import numpy as np
from scipy.integrate import quad
np.set_printoptions(precision=6,suppress=True)
mu0=4e-7*np.pi;c=2.99792458e8;eps0=1/(mu0*c*c);Z0=mu0*c;qe=1.602176634e-19

print("== 1. finite oscillating dipole (two charges +-q0 cos wt separated by d, joined by a wire): exact retarded potentials vs the far-field formula (G 11.18)")
# units: 1/(4 pi eps0) = 1, c = 1, mu0/(4 pi) = 1
w=2*np.pi;q0=1.0;d=0.02;p0=q0*d
def V(x,z,t):
    out=0.0
    for s,zz in ((+1,d/2),(-1,-d/2)):
        r=np.hypot(x,z-zz);out+=s*q0*np.cos(w*(t-r))/r
    return out
def Az(x,z,t):
    zs=np.linspace(-d/2,d/2,201);r=np.hypot(x,z-zs);f=-q0*w*np.sin(w*(t-r))/r;return np.trapezoid(f,zs)
def E_exact(r,th,t,h=1e-4):
    x,z=r*np.sin(th),r*np.cos(th)
    gx=(V(x+h,z,t)-V(x-h,z,t))/(2*h);gz=(V(x,z+h,t)-V(x,z-h,t))/(2*h);dA=(Az(x,z,t+h)-Az(x,z,t-h))/(2*h)
    Ex,Ez=-gx,-gz-dA;return Ex*np.cos(th)-Ez*np.sin(th)   # E_theta component (theta-hat = (cos th, -sin th) in (x,z))
for r in (3.0,10.0,30.0,100.0):
    th=np.radians(60);t0=0.0
    vals=[(E_exact(r,th,t0+tt/8),-p0*w*w*np.sin(th)/r*np.cos(w*(t0+tt/8-r))) for tt in range(8)]
    err=max(abs(a-b) for a,b in vals);amp=p0*w*w*np.sin(th)/r
    print("   r=%6.1f lambda: max |E_theta(exact) - (11.18)| over 8 phases = %.3e ; amplitude (11.18) = %.4e ; relative error %.3e (~ 1/(k r) = %.3e)"%(r,err,amp,err/amp,1/(w*r)))

print("\n== 2. total power: integrate <S> (G 11.21) over a sphere and compare (11.22); Jackson (9.24); SI numbers p0 = 1e-12 C m at 1 MHz")
p0=1e-12;om=2*np.pi*1e6;k=om/c
Pg=mu0*p0**2*om**4/(12*np.pi*c)
Pj=c*c*Z0*k**4*p0**2/(12*np.pi)
r=10.0;S=lambda th:mu0*p0**2*om**4/(32*np.pi**2*c)*np.sin(th)**2/r**2
Pint=quad(lambda th:S(th)*2*np.pi*r*r*np.sin(th),0,np.pi)[0]
print("   G (11.22) = %.6e W ; J (9.24) = %.6e W ; sphere integral of (11.21) = %.6e W"%(Pg,Pj,Pint))
dPdOmega_G=mu0*p0**2*om**4/(32*np.pi**2*c);dPdOmega_J=c*c*Z0*k**4*p0**2/(32*np.pi**2)
print("   dP/dOmega at theta=90 deg: G %.6e ; J (9.23) %.6e W/sr"%(dPdOmega_G,dPdOmega_J))

print("\n== 3. radiation resistances")
for dl in (0.01,0.05,0.1):
    kd=2*np.pi*dl;RG=Z0*kd**2/(6*np.pi);RJ=Z0*kd**2/(24*np.pi)
    print("   d/lambda=%.2f: uniform current (G 11.3): R = Z0 (kd)^2/6pi = %.4f ohm (790 (d/lambda)^2 = %.4f) ; triangular current (J 9.29): R = Z0 (kd)^2/24 pi = %.4f ohm (5 (kd)^2 = %.4f)"%(dl,RG,790*dl**2,RJ,5*kd**2))
print("   coefficients: Z0 2 pi/3 = %.3f ; Z0/(24 pi) = %.4f ; Z0 = %.4f ohm"%(Z0*2*np.pi/3,Z0/(24*np.pi),Z0))

print("\n== 4. magnetic vs electric dipole power (G 11.41-11.42): b = 1 cm loop, lambda = 1 m, d = pi b")
b=0.01;lam=1.0;ratio=(2*np.pi*b/lam)**2
q0=1e-9;omg=2*np.pi*c/lam;I0=q0*omg;m0=np.pi*b**2*I0;p0=q0*np.pi*b
Pe=mu0*p0**2*omg**4/(12*np.pi*c);Pm=mu0*m0**2*omg**4/(12*np.pi*c**3)
print("   P_mag/P_el from (11.22),(11.40) = %.6e ; (omega b/c)^2 = %.6e"%(Pm/Pe,ratio))

print("\n== 5. blue sky: scattered power scales as omega^4")
print("   450 nm vs 650 nm: (650/450)^4 = %.3f ; 400 nm vs 700 nm: %.3f"%((650/450)**4,(700/400)**4))

print("\n== 6. Larmor (G 11.61 = J 14.22 in SI): P = mu0 q^2 a^2/(6 pi c)")
for a in (1e15,1e18,1e20):
    P=mu0*qe**2*a**2/(6*np.pi*c);print("   electron a = %.0e m/s^2: P = %.4e W   (= q^2 a^2/(6 pi eps0 c^3) = %.4e W)"%(a,P,qe**2*a**2/(6*np.pi*eps0*c**3)))
th=np.linspace(0,np.pi,4001);print("   angular integral: int sin^2 theta dOmega = %.6f (8 pi/3 = %.6f)"%(2*np.pi*np.trapezoid(np.sin(th)**3,th),8*np.pi/3))

print("\n== 7. G Problem 11.8: capacitor discharge radiates a fraction mu0 d^2/(6 pi c R^3 C^2) of Q0^2/2C")
C=1e-12;R=1000.0;dd=1e-4;Q0=1e-9;RC=R*C
Prad=lambda t:mu0/(6*np.pi*c)*(Q0*dd*np.exp(-t/RC)/RC**2)**2
E_rad=quad(Prad,0,40*RC,epsabs=0,epsrel=1e-10)[0];E0=Q0**2/(2*C)
print("   RC = %.1e s ; radiated energy = %.4e J ; initial energy = %.4e J ; fraction = %.4e ; formula %.4e"%(RC,E_rad,E0,E_rad/E0,mu0*dd**2/(6*np.pi*c*R**3*C**2)))
