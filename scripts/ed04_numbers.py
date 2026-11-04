"""ED04 numbers. .venv/bin/python -W ignore scripts/ed04_numbers.py"""
import numpy as np
from scipy.integrate import quad, dblquad
mu0=4e-7*np.pi; e0=8.8541878128e-12; c=1/np.sqrt(mu0*e0); k=1/(4*np.pi*e0)
print("== Griffiths Ex 8.1 setting: copper wire a=1 mm, L=1 m, I=10 A")
a=1e-3;L=1.0;I=10.0; rho=1.68e-8; R=rho*L/(np.pi*a**2); V=I*R
S=V*I/(2*np.pi*a*L)
print("R=%.4e ohm V=%.4e V P=I^2R=%.4f W  S(surface)=%.2f W/m^2 ; S*2 pi a L=%.4f W"%(R,V,I*I*R,S,S*2*np.pi*a*L))
print("== charging capacitor R=5cm d=2mm I=2A (t=1 ns): Poynting flux into gap vs dU/dt")
Rc=0.05;d=2e-3;I=2.0;t=1e-9
E=I*t/(e0*np.pi*Rc**2); Bedge=mu0*I/(2*np.pi*Rc); Sedge=E*Bedge/mu0
P=Sedge*2*np.pi*Rc*d; dUdt=e0*E*(I/(e0*np.pi*Rc**2))*np.pi*Rc**2*d
print("E=%.4e V/m  V=Ed=%.3f V  S_edge=%.4e W/m2  P_in=%.4f W  dU/dt=%.4f W  VI=%.4f W"%(E,E*d,Sedge,P,dUdt,E*d*I))
print("== Griffiths Ex 8.2: force on northern hemisphere of uniformly charged ball, Q=1 nC, R=1 cm")
Q=1e-9;Rr=1e-2
bowl=0.5*e0*(Q/(4*np.pi*e0*Rr**2))**2*2*np.pi*Rr**2*quad(lambda t:np.sin(t)*np.cos(t),0,np.pi/2)[0]
Edisk=lambda r: Q*r/(4*np.pi*e0*Rr**3)
disk=0.5*e0*2*np.pi*quad(lambda r:Edisk(r)**2*r,0,Rr)[0]
print("bowl=%.4e (formula k Q^2/(8R^2)=%.4e)  disk=%.4e (k Q^2/(16 R^2)=%.4e)  total=%.4e N  formula 3kQ^2/(16R^2)=%.4e"%(bowl,k*Q*Q/(8*Rr**2),disk,k*Q*Q/(16*Rr**2),bowl+disk,3*k*Q*Q/(16*Rr**2)))
print("== coax momentum p=IVl/c^2: V=100 V, I=10 A, l=1 m -> %.4e kg m/s"%(100*10*1/c**2))
print("== Griffiths Ex 8.4 setting: n=1000/m, I=1 A, Q=1 uC, R=2 cm, a=1 cm: L_em=-1/2 mu0 n I Q (R^2-a^2) = %.4e J s"%(-0.5*mu0*1000*1*1e-6*(0.02**2-0.01**2)))
print("== energy densities: E=1e6 V/m -> u_e=%.3f J/m3 ; B=1 T -> u_m=%.3e J/m3 ; equal when E=cB: B=1 T <-> E=%.3e V/m"%(0.5*e0*1e12,0.5/mu0,c))
print("== momentum density g=S/c^2 for S=1 kW/m2 (sunlight): g=%.3e kg m^-2 s^-1 ; radiation pressure (absorbed) S/c=%.3e Pa"%(1e3/c**2,1e3/c))
