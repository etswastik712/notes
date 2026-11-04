"""ED03 numbers: displacement current in a charging capacitor; boundary conditions. .venv/bin/python -W ignore scripts/ed03_numbers.py"""
import numpy as np
mu0=4e-7*np.pi; e0=8.8541878128e-12
print("== charging parallel-plate capacitor R=5 cm, d=2 mm, I=2 A")
R=0.05;d=2e-3;I=2.0
A=np.pi*R**2; C=e0*A/d
dEdt=I/(e0*A)
print("C=%.4e F  dE/dt=%.4e V/m/s"%(C,dEdt))
for r in (0.02,0.05,0.10):
    Bin=mu0*e0*dEdt*r/2 if r<=R else mu0*I/(2*np.pi*r)
    Bwire=mu0*I/(2*np.pi*r)
    print("r=%.2f m  B_gap=%.4e T  (wire formula %.4e T) Id_enclosed/I=%.3f"%(r,Bin,Bwire,min(r/R,1)**2))
print("== field-line refraction at dielectric interface eps1=1, eps2=4 (no free charge); E1 at 60deg from normal")
th1=np.radians(60); e1,e2=1,4
tan2=np.tan(th1)*e2/e1; th2=np.degrees(np.arctan(tan2))
print("theta2=%.3f deg ; check D_n continuity: E2n=E1n*e1/e2"%th2)
E1=1.0; E1n=E1*np.cos(th1); E1t=E1*np.sin(th1)
E2n=E1n*e1/e2; E2t=E1t
print("tan(th2)=E2t/E2n=%.4f = %.4f"%(E2t/E2n,tan2))
print("== magnetic: mu1=1 mu2=1000 (iron), B1 at 10deg from normal in medium 1")
th1=np.radians(10); m1,m2=1,1000
print("theta2=%.4f deg (H_t continuous, B_n continuous: tan2/tan1=mu2/mu1)"%np.degrees(np.arctan(np.tan(th1)*m2/m1)))
print("== Maxwell wave speed 1/sqrt(mu0 e0) = %.6e m/s"%(1/np.sqrt(mu0*e0)))
print("== ratio displacement/conduction  w e/sigma")
print("copper 1 GHz: %.3e"%(2*np.pi*1e9*e0/5.96e7))
print("seawater 1 MHz (eps_r=80, sigma=4 S/m): %.3e"%(2*np.pi*1e6*e0*80/4))
print("== Faraday loop r=5cm, B0=0.1 T, 50 Hz: emf amp = %.4f V"%(2*np.pi*50*0.1*np.pi*0.05**2))
print("== displacement current through disc radius r in gap = I r^2/R^2 : r=2cm -> %.3f A"%(2*(0.02/0.05)**2))

from scipy.special import j0, j1, jn_zeros
print("\n== Jackson-6.14-type capacitor: E_z=E0 J0(kr), B_phi=(E0/c) J1(kr), k=w/c")
for x in (0.1,0.5,1.0,2.0):
    print("x=kr=%.1f  J0/(1-x^2/4)=%.5f   J1/(x/2)=%.5f"%(x,j0(x)/(1-x**2/4),j1(x)/(x/2)))
print("first zero of J0 = %.5f ; Jackson's quoted estimate 2*sqrt2 = %.5f ; ratio %.4f"%(jn_zeros(0,1)[0],2*np.sqrt(2),2*np.sqrt(2)/jn_zeros(0,1)[0]))
print("== relaxation time eps/sigma and crossover frequency sigma/(2 pi eps)")
for name,er,sg in (("copper",1,5.96e7),("seawater",80,4.0)):
    print(name,"tau=%.3e s  f_c=%.3e Hz"%(er*e0/sg, sg/(2*np.pi*er*e0)))
rho=0.23; sg=1/rho; w=2*np.pi*4e8; print("Griffiths Prob 7.40 data: sigma=%.3f S/m  J_cond/J_disp = sigma/(w eps)=%.3f"%(sg,sg/(w*81*e0)))
print("== Griffiths Ex 7.14 shells: Q0=1 nC, sigma=1e-3 S/m (eps0): tau=%.3e s, I(0)=sigma Q0/eps0=%.4f A"%(e0/1e-3, 1e-3*1e-9/e0))
print("== Griffiths Prob 7.12-type loop: a=10cm, loop radius a/2, B0=0.1T, 50 Hz, R=0.1 ohm: emf amp=%.4f V, I amp=%.3f A"%(2*np.pi*50*0.1*np.pi*0.05**2,2*np.pi*50*0.1*np.pi*0.05**2/0.1))
