"""CM03 numbers. .venv/bin/python -W ignore scripts/cm03_numbers.py"""
import numpy as np
from scipy.integrate import solve_ivp
g=9.81
print("== particle crossing a potential step (LL §7 problem): m v1 sin th1 = m v2 sin th2")
m=1.0; v1=10.0; dU=20.0; v2=np.sqrt(v1**2-2*dU/m); th1=np.radians(30)
print("v2=%.4f  sin th2=%.5f  th2=%.3f deg ; critical sin th_c = v2/v1 = %.4f -> th_c=%.2f deg"%(v2,v1*np.sin(th1)/v2,np.degrees(np.arcsin(v1*np.sin(th1)/v2)),v2/v1,np.degrees(np.arcsin(v2/v1))))
print("== two particles m1=1,m2=3, v1=(2,0), v2=(-1,1): E = 1/2 M V^2 + E_int (LL 8.4)")
m1,m2=1.,3.; a=np.array([2.,0]); b=np.array([-1.,1.]); M=m1+m2; P=m1*a+m2*b; V=P/M
K=0.5*m1*a@a+0.5*m2*b@b; mu=m1*m2/M; rel=a-b
print("P=",P,"V=",V," K=%.4f  1/2MV^2=%.4f  E_int=%.4f  1/2 mu v_rel^2=%.4f"%(K,0.5*M*V@V,K-0.5*M*V@V,0.5*mu*rel@rel))
print("== Noether boost: M R - P t constant for two particles with spring U=1/2 k |r1-r2|^2")
k=5.0
def f(t,y):
    r1,r2,v1_,v2_=y[0:2],y[2:4],y[4:6],y[6:8]; F=-k*(r1-r2)
    return np.concatenate([v1_,v2_,F/m1,-F/m2])
y0=np.array([0,0, 1,0.5, 0.3,-0.2, -0.1,0.4]); s=solve_ivp(f,[0,20],y0,rtol=1e-11,atol=1e-13,dense_output=True)
t=np.linspace(0,20,5); Y=s.sol(t)
Q=np.array([m1*Y[0:2,i]+m2*Y[2:4,i]-(m1*Y[4:6,i]+m2*Y[6:8,i])*t[i] for i in range(len(t))])
print("M R - P t at t=",t," ->",Q.round(9).tolist()); print("max deviation =%.2e"%np.max(np.abs(Q-Q[0])))
print("== spherical pendulum: conserved p_phi and E (l=1)")
l=1.0
def sp(t,y):
    th,ph,thd,phd=y; return [thd,phd,np.sin(th)*np.cos(th)*phd**2-g/l*np.sin(th),-2*np.cos(th)/np.sin(th)*thd*phd]
y0=[0.8,0,0.5,2.0]; s=solve_ivp(sp,[0,30],y0,rtol=1e-12,atol=1e-13,dense_output=True); t=np.linspace(0,30,3001); th,ph,thd,phd=s.sol(t)
pphi=l**2*np.sin(th)**2*phd; E=0.5*l**2*(thd**2+np.sin(th)**2*phd**2)-g*l*np.cos(th)
print("p_phi drift=%.2e (rel %.2e)  E drift=%.2e (rel %.2e)"%(np.ptp(pphi),np.ptp(pphi)/abs(pphi[0]),np.ptp(E),np.ptp(E)/abs(E[0])))
print("== Kepler: Lz and E in U=-1/r")
def kp(t,y):
    x,yy,vx,vy=y; r=np.hypot(x,yy); return [vx,vy,-x/r**3,-yy/r**3]
s=solve_ivp(kp,[0,40],[1,0,0,0.8],rtol=1e-12,atol=1e-13,dense_output=True); t=np.linspace(0,40,4001); x,yy,vx,vy=s.sol(t)
Lz=x*vy-yy*vx; En=0.5*(vx**2+vy**2)-1/np.hypot(x,yy); print("Lz=%.6f drift %.2e ; E=%.6f drift %.2e"%(Lz[0],np.ptp(Lz),En[0],np.ptp(En)))
print("== hoop (CM02): E vs h along a trajectory, R=0.5, Omega=6, theta(0)=1.0, thetadot=0")
R=0.5;W=6.0
f=lambda t,y:[y[1],np.sin(y[0])*(W**2*np.cos(y[0])-g/R)]
s=solve_ivp(f,[0,3],[1.0,0],rtol=1e-11,atol=1e-13,dense_output=True); t=np.linspace(0,3,301); th,thd=s.sol(t)
h=0.5*R**2*thd**2-0.5*R**2*W**2*np.sin(th)**2-g*R*np.cos(th); Etot=0.5*R**2*thd**2+0.5*R**2*W**2*np.sin(th)**2-g*R*np.cos(th)
print("h range=%.2e  E range=%.4f  (per unit mass)"%(np.ptp(h),np.ptp(Etot)))
