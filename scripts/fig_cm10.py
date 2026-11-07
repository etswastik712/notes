"""CM10 figure. .venv/bin/python -W ignore scripts/fig_cm10.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
from scipy.integrate import solve_ivp
fig,ax=plt.subplots(1,3,figsize=(15.5,4.8))
# A: pendulum blob
A=ax[0]
def flow(pts,T):
    def f(t,y):
        n=len(y)//2;return np.concatenate([y[n:],-np.sin(y[:n])])
    y0=np.concatenate([pts[:,0],pts[:,1]]);sol=solve_ivp(f,[0,T],y0,rtol=1e-10,atol=1e-12,max_step=0.01);n=len(pts);return np.stack([sol.y[:n,-1],sol.y[n:,-1]],1)
def area(b): x,y=b[:,0],b[:,1];return 0.5*abs(np.dot(x,np.roll(y,-1))-np.dot(y,np.roll(x,-1)))
th=np.linspace(0,2*np.pi,3000,endpoint=False);b0=np.stack([1.5+0.4*np.cos(th),0.3+0.4*np.sin(th)],1)
qs=np.linspace(-4*np.pi/2*1.0,4*np.pi/2*1.0,600);A.plot(qs,np.sqrt(2*(1+np.cos(qs))),color=GRID,lw=1.5);A.plot(qs,-np.sqrt(2*(1+np.cos(qs))),color=GRID,lw=1.5)
for T,col in ((0,MUTED),(4,BLUE),(8,ORANGE),(12,RED)):
    b=flow(b0,T) if T>0 else b0;b=np.where(np.abs(b[:,:1]-np.pi*np.round(b[:,:1]/(2*np.pi))*2)>0,b,b)
    qq=(b[:,0]+np.pi)%(2*np.pi)-np.pi;A.plot(qq,b[:,1],".",ms=0.8,color=col,label="$t=%d$: boundary area %.4f"%(T,area(b)))
A.set_xlim(-np.pi,np.pi);A.set_ylim(-2.6,2.6);A.set_xlabel("$q$ (mod $2\\pi$)");A.set_ylabel("$p$");A.legend(fontsize=7.5,loc="lower left",markerscale=12);A.set_title("A  Pendulum: a blob stretches into a filament;\nits area stays 0.5027 (Liouville)",fontsize=10)
# B: action-angle map
B=ax[1]
for r in np.sqrt(2*np.array([0.2,0.5,1.0,1.6,2.4])):
    a=np.linspace(0,2*np.pi,400);qq=r*np.sin(a);pp=r*np.cos(a);Q=np.arctan2(qq,pp);P=(pp**2+qq**2)/2
    B.plot(Q,P,".",ms=1.5,color=BLUE)
for ang in np.linspace(-np.pi,np.pi,13)[:-1]:
    rr=np.linspace(0.05,2.2,50);qq=rr*np.sin(ang);pp=rr*np.cos(ang);Q=np.arctan2(qq,pp);P=(pp**2+qq**2)/2;B.plot(Q,P,color=ORANGE,lw=1.0)
B.set_xlabel("angle variable $Q=\\arctan(q/p)$");B.set_ylabel("action variable $P=(p^2+q^2)/2$");B.set_title("B  Oscillator in action-angle variables:\nellipses $\\to$ horizontal lines, $H'=\\omega P$",fontsize=10)
# C: unit square under three maps
C=ax[2];s=np.linspace(0,1,60);sq=np.concatenate([np.stack([s,0*s],1),np.stack([1+0*s,s],1),np.stack([1-s,1+0*s],1),np.stack([0*s,1-s],1)])+np.array([0.5,0.5])
def ar(b): x,y=b[:,0],b[:,1];return 0.5*abs(np.dot(x,np.roll(y,-1))-np.dot(y,np.roll(x,-1)))
maps=(("canonical shear $Q=q,\\ P=p+2q$",lambda q,p:(q,p+2*q),BLUE),("canonical $Q=q^2,\\ P=p/2q$",lambda q,p:(q**2,p/(2*q)),AQUA),("not canonical $Q=q^2,\\ P=p$",lambda q,p:(q**2,p),RED))
C.plot(sq[:,0],sq[:,1],color=MUTED,lw=1.5,label="unit square, area %.3f"%ar(sq))
for lab,f,col in maps:
    Q,P=f(sq[:,0],sq[:,1]);C.plot(Q,P,color=col,lw=1.6,label="%s: area %.3f"%(lab,ar(np.stack([Q,P],1))))
C.set_xlabel("$Q$ (or $q$)");C.set_ylabel("$P$ (or $p$)");C.legend(fontsize=7.5,loc="upper left");C.set_title("C  Areas: canonical maps preserve them",fontsize=10)
fig.tight_layout();save(fig,"fig_cm10_canonical")
