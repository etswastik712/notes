"""CM07 figure. .venv/bin/python -W ignore scripts/fig_cm07.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D  # noqa
fig=plt.figure(figsize=(16,5.0))
from matplotlib.gridspec import GridSpec
gs=GridSpec(2,6,figure=fig,width_ratios=[1.5,1.5,0.9,0.9,0.9,1.9],wspace=0.55,hspace=0.35)
# --- A: polhodes on the angular-momentum sphere, I=(1,2,3)
A=fig.add_subplot(gs[:,0:2],projection="3d"); I=np.array([1.,2.,3.])
def eul(t,M): return [(1/I[2]-1/I[1])*M[1]*M[2],(1/I[0]-1/I[2])*M[2]*M[0],(1/I[1]-1/I[0])*M[0]*M[1]]
u,v=np.mgrid[0:2*np.pi:40j,0:np.pi:20j]
A.plot_surface(np.cos(u)*np.sin(v),np.sin(u)*np.sin(v),np.cos(v),color="#f0efec",alpha=0.35,lw=0)
def path(M0,T=60):
    s=solve_ivp(eul,[0,T],M0,rtol=1e-10,atol=1e-12,max_step=0.02);return s.y
starts=[]
for amp in (0.12,0.3,0.55,0.8):
    for ax,th in ((0,0),(2,0)):
        M0=np.zeros(3);M0[ax]=np.sqrt(1-amp**2);M0[1]=amp;starts.append((M0,BLUE if ax==0 else AQUA))
        M0=np.zeros(3);M0[ax]=-np.sqrt(1-amp**2);M0[1]=-amp;starts.append((M0,BLUE if ax==0 else AQUA))
# separatrix neighbourhood: start near x2 poles
for sgn in (1,-1):
    for d in (1e-5,):
        for oth in ((d,0),(-d,0)):
            M0=np.array([oth[0],sgn*np.sqrt(1-d*d),0.]);starts.append((M0,RED))
for M0,c in starts:
    y=path(M0,80 if c!=RED else 45); A.plot(*y,color=c,lw=1.0)
for ax in range(3):
    for sg in (1,-1):
        p=np.zeros(3);p[ax]=sg;A.scatter(*p,color=INK,s=14)
A.text(1.15,0,0,"$x_1$",fontsize=9);A.text(0,1.15,0,"$x_2$",fontsize=9);A.text(0,0,1.15,"$x_3$",fontsize=9)
A.view_init(24,35);A.set_box_aspect((1,1,1),zoom=1.35);A.set_axis_off();A.set_title("A  Polhodes of $\\vec{M}$ in the body ($I=1,2,3$)",fontsize=10)
fig.text(0.43,0.97,"B  Heavy symmetric top: tip paths on the sphere (LL Fig. 49)",fontsize=10,fontweight="bold",ha="center",va="top")
# --- B: heavy symmetric top tip paths (three small panels)
I1p=1.0;I3=0.4;mgl=1.0;M3=3.2;th0=np.radians(60)
Uef=lambda th,Mz:(Mz-M3*np.cos(th))**2/(2*I1p*np.sin(th)**2)-mgl*(1-np.cos(th))
cases=[(2.5,BLUE,"(a) $\\dot\\phi_0>0$:\nprecession + nutation"),(-0.9,ORANGE,"(b) $\\dot\\phi_0<0$:\nloops"),(0.0,AQUA,"(c) from rest:\ncusps")]
for k,(ph0,c,lab) in enumerate(cases):
    Bk=fig.add_subplot(gs[:,2+k])
    Mz=I1p*np.sin(th0)**2*ph0+M3*np.cos(th0)
    def f(t,y,Mz=Mz):
        th,thd,ph=y;h=1e-6;dUdt=(Uef(th+h,Mz)-Uef(th-h,Mz))/(2*h)
        return [thd,-dUdt/I1p,(Mz-M3*np.cos(th))/(I1p*np.sin(th)**2)]
    s_=solve_ivp(f,[0,9],[th0,0,0],rtol=1e-10,atol=1e-12,max_step=0.005)
    Bk.plot(s_.y[0]*np.cos(s_.y[2]),s_.y[0]*np.sin(s_.y[2]),color=c,lw=1.0);Bk.plot(0,0,"k+")
    Bk.set_aspect("equal");Bk.set_title(lab,fontsize=8.5);Bk.tick_params(labelsize=7)
    if k==0: Bk.set_ylabel("tip: $\\theta\\sin\\phi$ (rad)",fontsize=8)
    Bk.set_xlabel("$\\theta\\cos\\phi$",fontsize=8)
# --- C: instability of the intermediate axis vs stable axes
C=fig.add_subplot(gs[:,5]);t=np.linspace(0,30,3000)
for ax,col,lab in ((0,BLUE,"about $x_1$ (smallest $I$): stable"),(1,RED,"about $x_2$ (intermediate $I$): unstable"),(2,AQUA,"about $x_3$ (largest $I$): stable")):
    Om0=np.zeros(3);Om0[ax]=1;Om0[(ax+1)%3]=1e-3
    f=lambda t,O:[(I[1]-I[2])/I[0]*O[1]*O[2],(I[2]-I[0])/I[1]*O[2]*O[0],(I[0]-I[1])/I[2]*O[0]*O[1]]
    s=solve_ivp(f,[0,30],Om0,rtol=1e-11,atol=1e-13,dense_output=True,max_step=0.01);O=s.sol(t)
    dev=np.sqrt(np.maximum((O**2).sum(0)-O[ax]**2,0));C.semilogy(t,dev+1e-12,color=col,label=lab)
C.set_ylim(1e-4,3);C.set_xlabel("time (units of $1/\\Omega$)");C.set_ylabel("transverse $|\\vec{\\Omega}|/\\Omega$");C.legend(fontsize=7.5,loc="lower right");C.set_title("C  Perturbed rotation about each principal axis",fontsize=10)
fig.suptitle('',y=0.99);save(fig,"fig_cm07_rigid")
