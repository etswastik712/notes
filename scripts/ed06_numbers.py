"""ED06 numbers. .venv/bin/python -W ignore scripts/ed06_numbers.py"""
import numpy as np
mu0=4e-7*np.pi; e0=8.8541878128e-12; c=1/np.sqrt(mu0*e0); q=1.602176634e-19; me=9.1093837e-31
print("== normal incidence air->glass n1=1 n2=1.5")
n1,n2=1.0,1.5; r=(n1-n2)/(n1+n2); t=2*n1/(n1+n2); print("E_R/E_I=%.3f E_T/E_I=%.3f R=%.4f T=%.4f"%(r,t,r**2,4*n1*n2/(n1+n2)**2))
def fresnel(th,n1,n2):
    ti=np.radians(th); st=n1/n2*np.sin(ti); ct=np.sqrt(1-st**2+0j)
    # E perpendicular (Jackson 7.39, mu=mu'): t=2 n1 cos i/(n1 cos i + n2 cos r), r=(n1 cos i - n2 cos r)/(...)
    rp=(n1*np.cos(ti)-n2*ct)/(n1*np.cos(ti)+n2*ct)
    # E parallel (Griffiths 9.109): alpha=cos t/cos i, beta=n2/n1 : r=(alpha-beta)/(alpha+beta)
    al=ct/np.cos(ti); be=n2/n1; rpar=(al-be)/(al+be)
    return rp,rpar
for th in (0,30,56.31,70):
    rp,rpar=fresnel(th,1,1.5); print("theta=%.2f  R_perp=%.4f  R_par=%.4f"%(th,abs(rp)**2,abs(rpar)**2))
print("Brewster arctan(1.5)=%.3f deg ; critical glass->air arcsin(1/1.5)=%.3f deg"%(np.degrees(np.arctan(1.5)),np.degrees(np.arcsin(1/1.5))))
# energy check with cos factors for parallel pol at 30 deg
th=30; ti=np.radians(th); st=np.sin(ti)/1.5; tt=np.arcsin(st); al=np.cos(tt)/np.cos(ti); be=1.5; E_R=(al-be)/(al+be); E_T=2/(al+be)
IR=E_R**2; IT=(1.5*np.cos(tt))/(1*np.cos(ti))*E_T**2; print("parallel, 30 deg: R=%.5f T=%.5f R+T=%.6f"%(IR,IT,IR+IT))
print("== evanescent wave and Goos-Hanchen: glass (n=1.5) lambda0=600 nm, i=60 deg")
lam_g=600e-9/1.5; k=2*np.pi/lam_g; si0=1/1.5; i=np.radians(60); root=np.sqrt(np.sin(i)**2-si0**2)
print("lambda in glass=%.1f nm  delta=1/(k sqrt(sin^2 i - sin^2 i0))=%.4e m ; D_perp=(lam/pi) sin i/root=%.4e m"%(lam_g*1e9,1/(k*root),lam_g/np.pi*np.sin(i)/root))
print("== conductors: skin depth, copper sigma=5.96e7")
sg=5.96e7
def kk(w,eps,mu,sg):
    kt=np.sqrt(mu*eps*w**2+1j*mu*sg*w); return kt.real,kt.imag
for f in (50,1e6,1e10):
    w=2*np.pi*f; k_,ka=kk(w,e0,mu0,sg); d=1/ka
    print("f=%.0e Hz: d=%.4e m  lambda=2pi/k=%.4e m  v=w/k=%.4e m/s  (air lambda=%.4e m)  B0/E0=|k~|/w=%.4e s/m  phase lag=atan(kappa/k)=%.3f deg"%(f,d,2*np.pi/k_,w/k_,c/f,np.hypot(k_,ka)/w,np.degrees(np.arctan2(ka,k_))))
print("relaxation time eps0/sigma copper = %.3e s ; glass (sigma~1e-12): %.1f s"%(e0/sg,e0/1e-12))
print("== reflection from a conductor: silver sigma=6e7, w=4e15 (Griffiths Prob 9.22 data), eps=eps0, mu=mu0")
w=4e15; sgs=6e7; kt=np.sqrt(mu0*e0*w**2+1j*mu0*sgs*w); beta=c/w*kt; r=(1-beta)/(1+beta); print("beta~=%.3f%+.3fi  R=|r|^2=%.4f ; sigma/(eps w)=%.1f"%(beta.real,beta.imag,abs(r)**2,sgs/(e0*w)))
print("copper optical skin depth: sigma=1e7, w=1e15: d=%.2f nm ; lambda/2pi check"%(1/kk(1e15,e0,mu0,1e7)[1]*1e9))
print("== Lorentz model: dilute gas, N=2.5e25 m^-3, f=1, omega0=1.5e16, gamma=1e14")
N=2.5e25; w0=1.5e16; gam=1e14; wp2=N*q**2/(me*e0)
print("N q^2/(m eps0)=%.3e s^-2"%wp2)
for lam in (400e-9,540e-9,700e-9):
    w=2*np.pi*c/lam; n=1+0.5*wp2*(w0**2-w**2)/((w0**2-w**2)**2+gam**2*w**2); print("lambda=%.0f nm: n-1=%.4e"%(lam*1e9,n-1))
print("peak absorption at w0: alpha=wp2/(c gamma)=%.3e 1/m -> length %.3e m"%(wp2/(c*gam),c*gam/wp2))
print("== Drude: copper N=8e28, sigma=5.9e7 -> gamma=N e^2/(m sigma)=%.3e s^-1 (Jackson ~4e13)"%(8e28*q**2/(me*5.9e7)))
print("== plasma frequency w_p^2=N e^2/(eps0 m): ionosphere N=1e12: w_p=%.3e rad/s f_p=%.3e Hz ; lab N=1e18: %.3e ; 1e22: %.3e ; copper N=8e28: %.3e rad/s"%(np.sqrt(1e12*q**2/(e0*me)),np.sqrt(1e12*q**2/(e0*me))/2/np.pi,np.sqrt(1e18*q**2/(e0*me)),np.sqrt(1e22*q**2/(e0*me)),np.sqrt(8e28*q**2/(e0*me))))
print("plasma at w=2 w_p: v_p/c=%.4f v_g/c=%.4f  v_p v_g=c^2: %.4f"%(2/np.sqrt(3),np.sqrt(3)/2,2/np.sqrt(3)*np.sqrt(3)/2))
print("static attenuation 2 w_p/c for N=1e18: %.3e 1/m -> length %.2e m"%(2*np.sqrt(1e18*q**2/(e0*me))/c,c/(2*np.sqrt(1e18*q**2/(e0*me)))))
