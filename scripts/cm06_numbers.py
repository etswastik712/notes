"""CM06 numbers. .venv/bin/python -W ignore scripts/cm06_numbers.py"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import eigh
g=9.81;l=1.0
print("== double pendulum m1=m2=m, l1=l2=l: M=ml^2[[2,1],[1,1]], K=mgl[[2,0],[0,1]]")
M=np.array([[2,1],[1,1.]]); K=np.array([[2,0],[0,1.]])
w2,V=eigh(K,M); print("omega^2/(g/l)=",w2.round(6)," expected 2-sqrt2=%.6f, 2+sqrt2=%.6f"%(2-np.sqrt(2),2+np.sqrt(2)))
print("omega1=%.4f sqrt(g/l)=%.4f rad/s ; omega2=%.4f sqrt(g/l)=%.4f rad/s"%(np.sqrt(w2[0]),np.sqrt(w2[0]*g/l),np.sqrt(w2[1]),np.sqrt(w2[1]*g/l)))
for j in range(2): v=V[:,j]/V[0,j]; print("mode %d shape (theta1,theta2) = (1, %.4f)"%(j+1,v[1]))
# nonlinear integration (full equations) starting on a normal mode
def dp(t,y):
    th1,th2,w1,w2_=y; d=th1-th2
    den=3-np.cos(2*d)
    a1=(-3*g*np.sin(th1)-g*np.sin(th1-2*th2)-2*np.sin(d)*(w2_**2+w1**2*np.cos(d)))/den
    a2=(2*np.sin(d)*(2*w1**2+2*g*np.cos(th1)+w2_**2*np.cos(d)))/den
    return [w1,w2_,a1,a2]
def energy(y):
    th1,th2,w1,w2_=y; return 0.5*2*w1**2+0.5*w2_**2+w1*w2_*np.cos(th2-th1)-2*g*np.cos(th1)-g*np.cos(th2)
def period(y0,T=20):
    s=solve_ivp(dp,[0,T],y0,rtol=1e-12,atol=1e-13,dense_output=True,max_step=0.002); t=np.linspace(0,T,200001); th1=s.sol(t)[0]
    zc=t[1:][(th1[:-1]>0)&(th1[1:]<=0)]; Y=s.sol(t); E=energy(Y); print("   energy drift %.2e"%(E.max()-E.min())); return np.mean(np.diff(zc))
for k,name in ((0,"slow mode"),(1,"fast mode")):
    a=0.02; v=V[:,k]/V[0,k]; P=period([a,a*v[1],0,0]); print("%s: measured period (nonlinear, amplitude 0.02 rad)=%.5f s ; 2pi/omega=%.5f s"%(name,P,2*np.pi/np.sqrt(w2[k]*g/l)))
print("== coupled oscillators (LL §23 Problem 1): xdd+w0^2 x=a y, ydd+w0^2 y=a x ; w0=1, a=0.1")
w0=1.;a=0.1; w1_=np.sqrt(w0**2-a); w2_=np.sqrt(w0**2+a); print("w1=%.5f w2=%.5f  beat period 2pi/(w2-w1)=%.3f ; full transfer at pi/(w2-w1)=%.3f"%(w1_,w2_,2*np.pi/(w2_-w1_),np.pi/(w2_-w1_)))
f=lambda t,y:[y[2],y[3],-w0**2*y[0]+a*y[1],-w0**2*y[1]+a*y[0]]
s=solve_ivp(f,[0,70],[1,0,0,0],rtol=1e-12,atol=1e-13,dense_output=True); t=np.linspace(0,70,70001); x,y_=s.sol(t)[:2]
tn=np.pi/(w2_-w1_); print("x(t) at the predicted full-transfer time %.3f: %.5f ; y there: %.5f"%(tn,s.sol(tn)[0],s.sol(tn)[1]))
print("== forced resonance xdd+w^2 x=cos(gam t), w=2: gam=w -> x=(t/(2w)) sin(wt)")
w=2.;ff=lambda gam:(lambda t,y:[y[1],-w**2*y[0]+np.cos(gam*t)])
s=solve_ivp(ff(2.0),[0,10],[0,0],rtol=1e-12,atol=1e-13,dense_output=True); tt=np.linspace(0,10,100001); xx=s.sol(tt)[0]
print("resonance: max|x| near t=10 = %.4f ; envelope t/(2w)=%.4f ; at t=pi*... exact formula check x(10)=%.6f vs %.6f"%(np.max(np.abs(xx[tt>9])),10/(2*w),s.sol(10)[0],10/(2*w)*np.sin(w*10)))
print("beats gam=2.1: x=(cos(gam t)-cos(w t))/(w^2-gam^2)")
s=solve_ivp(ff(2.1),[0,70],[0,0],rtol=1e-12,atol=1e-13,dense_output=True); tt=np.linspace(0,70,140001); xx=s.sol(tt)[0]
print("max|x|=%.4f (predicted 2/|w^2-gam^2|=%.4f); beat envelope period 2pi/(gam-w)=%.2f"%(np.max(np.abs(xx)),2/abs(w**2-2.1**2),2*np.pi/0.1))
print("== 3 equal masses, 4 equal springs: omega^2/(k/m)")
K3=np.array([[2,-1,0],[-1,2,-1],[0,-1,2.]]); ev,evec=np.linalg.eigh(K3); print("omega^2 =",ev.round(6)," (2-sqrt2, 2, 2+sqrt2)=",[round(2-np.sqrt(2),6),2.0,round(2+np.sqrt(2),6)])
print("== forced coupled oscillators: force F cos(gam t) on x only; w0=1, a=0.1 -> amplitudes x=(F/2)[1/(w2^2-g^2)+1/(w1^2-g^2)], y=(F/2)[1/(w2^2-g^2)-1/(w1^2-g^2)] with w1^2=0.9, w2^2=1.1")
for gam in (0.5,0.9,1.0,1.05,1.5):
    A=np.array([[w0**2-gam**2,-a],[-a,w0**2-gam**2]]); u=np.linalg.solve(A,[1,0]); print("gamma=%.2f  x=%.4f  y=%.4f (per unit F)"%(gam,u[0],u[1]))
