"""ED07 numbers. .venv/bin/python -W ignore scripts/ed07_numbers.py"""
import numpy as np
mu0=4e-7*np.pi; e0=8.8541878128e-12; c=1/np.sqrt(mu0*e0)
a,b=2.28e-2,1.01e-2   # Griffiths Problem 9.29 dimensions (a = height in his notation, b = width)
print("== rectangular guide a=2.28 cm, b=1.01 cm: cutoffs f_mn=(c/2) sqrt((m/a)^2+(n/b)^2)")
modes=[]
for m in range(0,5):
    for n in range(0,5):
        if m==n==0: continue
        modes.append((np.hypot(m/a,n/b)*c/2,m,n))
for f,m,n in sorted(modes)[:7]: print("TE%d%d: f_c=%.3f GHz  (wavelength in vacuum %.3f cm)"%(m,n,f/1e9,c/f*100))
f0=1.7e10; print("at f=17.0 GHz propagating TE modes:",[f"TE{m}{n}" for f,m,n in sorted(modes) if f<f0])
f10=c/(2*a); f20=c/a; print("single-mode band TE10 only: %.3f to %.3f GHz  (free-space wavelengths %.2f to %.2f cm)"%(f10/1e9,f20/1e9,c/f20*100,c/f10*100))
print("== at 10 GHz, TE10")
f=10e9; fc=f10; r=np.sqrt(1-(fc/f)**2); k=2*np.pi*f/c*r
print("k=%.2f rad/m  lambda_g=2pi/k=%.4f cm (lambda0=%.2f) ; v_p=c/r=%.4f c ; v_g=c r=%.4f c ; v_p v_g=c^2: %.6f ; bounce angle cos th=%.4f th=%.2f deg"%(k,2*np.pi/k*100,c/f*100,1/r,r,(1/r)*r,r,np.degrees(np.arccos(r))))
print("== below cutoff at 5 GHz: evanescent kappa=(2pi/c) sqrt(fc^2-f^2)")
f=5e9; kap=2*np.pi/c*np.sqrt(fc**2-f**2); print("kappa=%.2f 1/m ; 1/kappa=%.3f cm ; attenuation over 10 cm: e^-%.2f = %.2e in amplitude, %.1f dB in power"%(kap,100/kap,kap*0.1,np.exp(-kap*0.1),20*np.log10(np.exp(kap*0.1))))
print("== TE10 fields from Griffiths (9.180): Bz=B0 cos(pi x/a); numeric Maxwell check at f=10 GHz")
w=2*np.pi*10e9; kz=k; kx=np.pi/a; K2=(w/c)**2-kz**2
def fields(x,y,z,t):
    ph=np.exp(1j*(kz*z-w*t)); Bz=np.cos(kx*x)*ph; dBz=-kx*np.sin(kx*x)*ph
    Bx=1j*kz/K2*dBz; By=0*Bz; Ex=0*Bz; Ey=-1j*w/K2*dBz; Ez=0*Bz
    return np.array([Ex,Ey,Ez]),np.array([Bx,By,Bz])
def curl(F,r,t,h=1e-6):
    J=np.zeros((3,3),complex)
    for j in range(3):
        d=np.zeros(3); d[j]=h; J[:,j]=(F(*(r+d),t)-F(*(r-d),t))/(2*h)
    return np.array([J[2,1]-J[1,2],J[0,2]-J[2,0],J[1,0]-J[0,1]])
E_=lambda x,y,z,t:fields(x,y,z,t)[0]; B_=lambda x,y,z,t:fields(x,y,z,t)[1]
r0=np.array([0.4e-2,0.3e-2,0.7e-2]); t0=0.0
dB=-1j*w*B_(*r0,t0); dE=-1j*w*E_(*r0,t0)
print("|curl E + dB/dt|/|dB/dt| = %.2e ; |curl B - dE/dt/c^2|/|..| = %.2e"%(np.linalg.norm(curl(E_,r0,t0)+dB)/np.linalg.norm(dB),np.linalg.norm(curl(B_,r0,t0)-dE/c**2)/np.linalg.norm(dE/c**2)))
print("boundary: E_y at x=0,a:",abs(E_(0,0.3e-2,0.7e-2,0)[1]),abs(E_(a,0.3e-2,0.7e-2,0)[1])," B_x at walls:",abs(B_(0,0.3e-2,0.7e-2,0)[0]),abs(B_(a,0.3e-2,0.7e-2,0)[0]))
xs=np.linspace(0,a,4001); ys=np.linspace(0,b,401)
Ey=np.abs(-1j*w/K2*(-kx*np.sin(kx*xs))); Bx=np.abs(1j*kz/K2*(-kx*np.sin(kx*xs))); Bz=np.abs(np.cos(kx*xs))
# time averaged flux and energy per length: S=1/(2 mu0) Re(E x B*) ; u = 1/4 (eps0|E|^2 + |B|^2/mu0)
Sz=0.5/mu0*Ey*Bx   # Ex=0, E_y B_x* contributes -E_y B_x* to z? (E x B)_z = Ex By - Ey Bx ; use magnitude with sign
Sz_int=np.trapezoid(0.5/mu0*(-(-1j*w/K2*(-kx*np.sin(kx*xs)))*np.conj(1j*kz/K2*(-kx*np.sin(kx*xs)))).real,xs)*b
u_int=np.trapezoid(0.25*(e0*Ey**2+(Bx**2+Bz**2)/mu0),xs)*b
print("P=%.4e W/B0^2  U=%.4e J/m /B0^2  P/U=%.5e m/s  v_g=%.5e m/s  ratio %.6f"%(Sz_int,u_int,Sz_int/u_int,c*r,Sz_int/u_int/(c*r)))
print("== coax: Z = (mu0 c/2pi) ln(b/a) = 59.96 ohm * ln(b/a)")
Z0=mu0*c/(2*np.pi); print("Z0/2pi=%.3f ohm ; b/a=3.5 -> %.2f ohm ; 50 ohm needs b/a=%.3f ; 75 ohm needs b/a=%.3f"%(Z0,Z0*np.log(3.5),np.exp(50/Z0),np.exp(75/Z0)))
print("with dielectric eps_r=2.25: Z=Z0/sqrt(eps_r) -> v=c/1.5, Z(b/a=3.5)=%.2f ohm"%(Z0*np.log(3.5)/1.5))
print("== ratios of cutoff to TE10 for a=2b (Jackson table): TE01 %.2f TE11 %.2f TE20 %.2f TE02 %.2f TE12 %.2f"%(np.hypot(0,1/0.5)/1,np.hypot(1,2),2.0,4.0,np.hypot(2,2)/1*0+np.hypot(1,4)))
