"""CM09 figure. .venv/bin/python -W ignore scripts/fig_cm09.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
fig,ax=plt.subplots(1,3,figsize=(15.5,4.7))
# A: pendulum phase portrait
A=ax[0];q=np.linspace(-2*np.pi,2*np.pi,600);p=np.linspace(-3,3,400);Q,P=np.meshgrid(q,p);H=P**2/2-np.cos(Q)
A.contour(Q,P,H,levels=[-0.8,-0.5,-0.2,0.3,0.6,1.0,1.5,2.0,3.0,4.0],colors=BLUE,linewidths=1.1)
A.contour(Q,P,H,levels=[1.0],colors=RED,linewidths=2.2)
A.plot([-np.pi,np.pi],[0,0],"o",color=RED,ms=5);A.plot([0],[0],"o",color=INK,ms=4)
A.annotate("separatrix $H=1$",(1.4,1.95),color=RED,fontsize=9);A.annotate("libration",(-0.55,0.52),fontsize=9);A.annotate("rotation",(3.5,2.6),fontsize=9)
A.set_xlabel("$q$ (angle)");A.set_ylabel("$p$");A.set_title("A  Pendulum phase portrait, $H=p^2/2-\\cos q$",fontsize=10)
# B: energy error of integrators on the oscillator (exact via matrix powers)
def step_rk4(q,p,h):
    f=lambda s:np.array([s[1],-s[0]]);s=np.array([q,p]);k1=f(s);k2=f(s+h/2*k1);k3=f(s+h/2*k2);k4=f(s+h*k3);return s+h/6*(k1+2*k2+2*k3+k4)
def step_leap(q,p,h): p=p-h/2*q;q=q+h*p;p=p-h/2*q;return np.array([q,p])
def step_euler(q,p,h): return np.array([q+h*p,p-h*q])
B=ax[1];h=0.1;Nper=np.logspace(0,5,40);
for name,st,col in (("explicit Euler",step_euler,RED),("RK4",step_rk4,ORANGE),("leapfrog (symplectic)",step_leap,BLUE)):
    A_=np.array([st(1,0,h),st(0,1,h)]).T;err=[]
    for n in Nper:
        N=int(round(n*2*np.pi/h));S=np.linalg.matrix_power(A_,N);s=S@np.array([1.0,0.0]);err.append(abs(0.5*s@s-0.5)/0.5+1e-12)
    B.loglog(Nper,err,color=col,label=name)
B.set_xlabel("number of periods");B.set_ylabel("relative energy error $|H-H_0|/H_0$");B.set_ylim(1e-9,1e3);B.legend(fontsize=8,loc="upper left");B.set_title("B  Energy error, oscillator, step $h=0.1$",fontsize=10)
# C: phase-space blob after n steps, h=0.3
C=ax[2];h=0.3;n=45;th=np.linspace(0,2*np.pi,300);b0=np.stack([1.0+0.35*np.cos(th),0.35*np.sin(th)],1)
def area(poly): x,y=poly[:,0],poly[:,1];return 0.5*abs(np.dot(x,np.roll(y,-1))-np.dot(y,np.roll(x,-1)))
C.plot(b0[:,0],b0[:,1],color=MUTED,lw=1.2,label="start, area %.3f"%area(b0))
for name,st,col in (("explicit Euler",step_euler,RED),("RK4",step_rk4,ORANGE),("leapfrog",step_leap,BLUE)):
    b=b0.copy()
    for i in range(n): b=np.array([st(x,y,h) for x,y in b])
    C.plot(b[:,0],b[:,1],color=col,lw=1.6,label="%s, area %.3f"%(name,area(b)))
C.set_aspect("equal");C.legend(fontsize=8,loc="lower left");C.set_xlabel("$q$");C.set_ylabel("$p$");C.set_title("C  A blob after %d steps ($h=0.3$): area is conserved\nonly by the symplectic map (Liouville)"%n,fontsize=10)
fig.tight_layout();save(fig,"fig_cm09_hamilton")
