"""ED05 numbers. .venv/bin/python -W ignore scripts/ed05_numbers.py"""
import numpy as np
mu0=4e-7*np.pi; e0=8.8541878128e-12; c=1/np.sqrt(mu0*e0); Z0=np.sqrt(mu0/e0)
print("c=%.6e  Z0=%.4f ohm"%(c,Z0))
print("== sunlight I=1300 W/m^2 (Griffiths Prob 9.10 data)")
I=1300.; E0=np.sqrt(2*I/(c*e0)); print("E0=%.2f V/m  B0=%.3e T  u_avg=%.3e J/m3  pressure absorber=%.3e Pa reflector=%.3e Pa ; fraction of 101325 Pa: %.2e"%(E0,E0/c,I/c,I/c,2*I/c,I/c/101325))
print("== laser 1 W, 1 mm^2 spot: I=%.3e W/m2 E0=%.3e V/m  force absorbed = P/c = %.3e N"%(1/1e-6,np.sqrt(2*1e6/(c*e0)),1/c))
print("== H0 for E0=100 V/m: %.4f A/m"%(100/Z0))
print("== general-direction wave k=(1,1,1)/sqrt3, n=(1,0,-1)/sqrt2: check Maxwell numerically")
lam=500e-9; k=2*np.pi/lam; w=c*k; kh=np.array([1,1,1])/np.sqrt(3); n=np.array([1,0,-1])/np.sqrt(2); b=np.cross(kh,n); print("khat x n =",(b*np.sqrt(6)).round(6),"/sqrt6")
E0=100.
E=lambda r,t:E0*np.cos(k*kh@r-w*t)*n; B=lambda r,t:(E0/c)*np.cos(k*kh@r-w*t)*b
def curl(F,r,t,h=lam/2000):
    J=np.zeros((3,3))
    for j in range(3):
        d=np.zeros(3); d[j]=h; J[:,j]=(F(r+d,t)-F(r-d,t))/(2*h)
    return np.array([J[2,1]-J[1,2],J[0,2]-J[2,0],J[1,0]-J[0,1]])
def div(F,r,t,h=lam/2000):
    s=0
    for j in range(3):
        d=np.zeros(3); d[j]=h; s+=(F(r+d,t)[j]-F(r-d,t)[j])/(2*h)
    return s
r0=np.array([0.3e-6,0.1e-6,0.2e-6]); t0=1e-16; dt=1e-18
dBdt=(B(r0,t0+dt)-B(r0,t0-dt))/(2*dt); dEdt=(E(r0,t0+dt)-E(r0,t0-dt))/(2*dt)
print("div E=%.2e (scale %.2e) div B=%.2e"%(div(E,r0,t0),E0*k,div(B,r0,t0)))
print("curl E + dB/dt: |res|/|dB/dt| = %.2e ; curl B - mu0 e0 dE/dt: |res|/|..| = %.2e"%(np.linalg.norm(curl(E,r0,t0)+dBdt)/np.linalg.norm(dBdt),np.linalg.norm(curl(B,r0,t0)-mu0*e0*dEdt)/np.linalg.norm(mu0*e0*dEdt)))
print("k=%.4e rad/m  omega=%.4e rad/s"%(k,w))
print("== Stokes: a1=3,a2=4,delta=60deg")
a1,a2,d=3,4,np.radians(60); s=[a1**2+a2**2,a1**2-a2**2,2*a1*a2*np.cos(d),2*a1*a2*np.sin(d)]; print("s0..s3=",np.round(s,4)," s0^2=%.2f  s1^2+s2^2+s3^2=%.2f"%(s[0]**2,s[1]**2+s[2]**2+s[3]**2))
print("== elliptical: E+ = 1, E- = r e^{i sigma}; axes ratio (1+r)/(1-r)")
for r in (0,0.2,0.5,1.0): print("r=%.1f ratio=%s"%(r,"inf" if r==1 else "%.3f"%((1+r)/(1-r))))
print("== circular wave: |E|=E0 constant, S=c e0 E0^2 (no oscillation) vs linear avg 1/2 c e0 E0^2, E0=100: S_circ=%.4f W/m2, S_lin_avg=%.4f"%(c*e0*100**2,0.5*c*e0*100**2))
