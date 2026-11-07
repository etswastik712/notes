"""CM08 figure. .venv/bin/python -W ignore scripts/fig_cm08.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
from scipy.integrate import solve_ivp
fig,ax=plt.subplots(1,3,figsize=(15.5,4.7))
# A: one free particle, two descriptions
A=ax[0];Om=0.8;t=np.linspace(0,6.5,2000);r0=np.array([1.0,-1.5]);v0=np.array([0.0,0.9])
rin=r0[None,:]+v0[None,:]*t[:,None]
c,s_=np.cos(Om*t),np.sin(Om*t);rrot=np.stack([c*rin[:,0]+s_*rin[:,1],-s_*rin[:,0]+c*rin[:,1]],1)
A.plot(rin[:,0],rin[:,1],color=BLUE,lw=2,label="inertial frame: straight line");A.plot(rrot[:,0],rrot[:,1],color=ORANGE,lw=2,label="rotating frame: curved path")
A.plot(*r0,"ko");A.plot(0,0,"+",color=INK,ms=10)
for k in (0,500,1000,1500):
    A.plot(rin[k,0],rin[k,1],"o",color=BLUE,ms=4);A.plot(rrot[k,0],rrot[k,1],"o",color=ORANGE,ms=4)
A.set_aspect("equal");A.legend(fontsize=8,loc="lower left");A.set_title("A  Free particle seen from a frame rotating at $\\Omega=0.8$",fontsize=10)
# B: eastward deflection of a falling body
B=ax[1];g=9.81;OmE=7.2921e-5;h=np.linspace(0,500,60)
for lat,col in ((0,BLUE),(45,ORANGE),(80,AQUA)):
    y=(1/3)*g*OmE*np.cos(np.radians(lat))*np.sqrt(2*h/g)**3
    B.plot(h,100*y,color=col,label="latitude $%d^\\circ$"%lat)
O=OmE*np.array([np.cos(np.radians(45)),0,np.sin(np.radians(45))])
pts=[]
for hh in (100,200,300,400,500):
    f=lambda t,s_:np.concatenate([s_[3:],np.array([0,0,-g])+2*np.cross(s_[3:],O)+np.cross(O,np.cross(s_[:3],O))])
    ev=lambda t,s_:s_[2];ev.terminal=True;ev.direction=-1
    sol=solve_ivp(f,[0,60],[0,0,hh,0,0,0],events=ev,rtol=1e-12,atol=1e-14);pts.append((hh,-100*sol.y_events[0][0][1]))
B.plot(*zip(*pts),"ko",ms=5,label="full integration (45°)");B.set_xlabel("height of fall $h$ (m)");B.set_ylabel("eastward deflection (cm)");B.legend(fontsize=8,loc="upper left");B.set_title("B  Deflection of a falling body: $y=\\frac{1}{3} g\\Omega\\cos\\lambda\\,t^3$",fontsize=10)
# C: Foucault pendulum path (rotation rate exaggerated)
C=ax[2];w=2*np.pi;Oz=0.04*w
f=lambda t,s_:[s_[2],s_[3],-w*w*s_[0]+2*Oz*s_[3],-w*w*s_[1]-2*Oz*s_[2]]
Tend=2*np.pi/Oz*0.5;sol=solve_ivp(f,[0,Tend],[1,0,0,0],rtol=1e-11,atol=1e-13,dense_output=True,max_step=0.01);tt=np.linspace(0,Tend,40000);z=sol.sol(tt)
C.plot(z[0],z[1],color=BLUE,lw=0.6);C.plot(1,0,"ko");C.set_aspect("equal")
C.annotate("",xy=(0.0,-0.0),xytext=(0,0))
C.set_title("C  Foucault pendulum: the plane turns at $-\\Omega\\sin\\lambda$\n(rotation rate exaggerated: $\\Omega_z/\\omega=0.04$, half a turn shown)",fontsize=10)
C.set_xlabel("$x$");C.set_ylabel("$y$")
fig.tight_layout();save(fig,"fig_cm08_noninertial")
