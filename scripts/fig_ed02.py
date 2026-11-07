"""ED02 figure. .venv/bin/python -W ignore scripts/fig_ed02.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
from scipy.special import ellipk,ellipe
fig=plt.figure(figsize=(15.5,4.9));gs=fig.add_gridspec(1,3)
A=fig.add_subplot(gs[0]);x,z=np.meshgrid(np.linspace(-3,3,361),np.linspace(-2.6,2.6,301))
rho=np.abs(x)+1e-9;a=1.0;k2=np.clip(4*a*rho/((a+rho)**2+z**2),0,1-1e-12);K=ellipk(k2);E=ellipe(k2);s=np.sqrt((a+rho)**2+z**2);d=(a-rho)**2+z**2+1e-12
Bz=1/(2*np.pi)/s*(K+(a*a-rho*rho-z*z)/d*E);Br=1/(2*np.pi)*z/(rho*s)*(-K+(a*a+rho*rho+z*z)/d*E);Bx=Br*np.sign(x)
sp=np.array([[x0,0.0] for x0 in (0.05,0.2,0.4,0.6,0.8,0.93,1.07,1.2,1.4,1.7,2.1,2.6)]+[[-x0,0.0] for x0 in (0.05,0.2,0.4,0.6,0.8,0.93,1.07,1.2,1.4,1.7,2.1,2.6)])
A.streamplot(x,z,Bx,Bz,color=BLUE,linewidth=1.0,density=1.2,arrowsize=0.9,start_points=sp,integration_direction="both",maxlength=40)
A.plot([1,-1],[0,0],"o",color=RED,ms=9);A.text(1.07,0.17,"$\\odot$",color=RED,fontsize=13);A.text(-1.28,0.17,"$\\otimes$",color=RED,fontsize=13)
A.set_xlim(-3,3);A.set_ylim(-2.6,2.6);A.set_aspect("equal");A.set_xlabel("$x/a$");A.set_ylabel("$z/a$");A.set_title("A  Field of a circular loop (cross-section)\n$B$ lines are closed; on the axis $B=\\mu_0Ia^2/2(a^2+z^2)^{3/2}$",fontsize=10)
B=fig.add_subplot(gs[1]);rd=np.array([3,10,30]);err=np.array([1.094e-1,1.007e-2,1.121e-3]);B.loglog(rd,err,"o",color=ORANGE,ms=8,label="loop vs pure dipole ($\\theta=60^\\circ$)");xs=np.logspace(0.3,1.9,50);B.loglog(xs,1/xs**2,color=MUTED,ls="--",label="$(a/r)^2$")
from matplotlib.ticker import NullFormatter
B.xaxis.set_minor_formatter(NullFormatter());B.yaxis.set_minor_formatter(NullFormatter())
B.set_xlabel("$r/a$");B.set_ylabel("relative difference of the field vectors");B.legend(fontsize=8);B.set_title("B  How good is the dipole field?\nthe next correction is relative order $(a/r)^2$",fontsize=10)
C=fig.add_subplot(gs[2]);X,Z=np.meshgrid(np.linspace(-3,3,361),np.linspace(-2.6,2.6,301));R=np.sqrt(X**2+Z**2)+1e-9;ct=Z/R;st=X/R
Brr=(2/3)*ct/R**3;Bth=(1/3)*st/R**3;Bxo=Brr*st+Bth*ct;Bzo=Brr*ct-Bth*st
inside=R<1;Bx_=np.where(inside,0.0,Bxo);Bz_=np.where(inside,2/3,Bzo);Hz_=np.where(inside,-1/3,Bzo);Hx_=np.where(inside,0.0,Bxo)
left=X<=0;right=X>=0
sB=np.array([[-x0,0.0] for x0 in (0.15,0.4,0.65,0.9,1.3,1.7,2.3)]);sH=np.array([[x0,0.0] for x0 in (0.15,0.4,0.65,0.9)]+[[x0,y0] for x0,y0 in ((1.1,0.3),(1.3,-0.5),(1.6,0.9),(2.0,-1.0),(1.15,1.2),(1.15,-1.2))])
C.streamplot(X,Z,Bx_,Bz_,color=BLUE,linewidth=1.0,density=1.2,arrowsize=0.9,start_points=sB,integration_direction="both",maxlength=40)
C.streamplot(X,Z,Hx_,Hz_,color=ORANGE,linewidth=1.0,density=1.2,arrowsize=0.9,start_points=sH,integration_direction="both",maxlength=40)
th=np.linspace(0,2*np.pi,300);C.plot(np.cos(th),np.sin(th),color="black",lw=1.5);C.axvline(0,color=GRID,lw=1);C.set_xlim(-3,3);C.set_ylim(-2.6,2.6);C.set_aspect("equal")
C.text(-2.9,2.3,"$B$: closed loops",color=BLUE,fontsize=10);C.text(0.4,2.3,"$H$: ends on surface",color=ORANGE,fontsize=10)
C.set_xlabel("$x/R$");C.set_ylabel("$z/R$");C.set_title("C  Uniformly magnetized sphere ($M\\parallel\\hat z$):\n$B_{\\rm in}=\\frac{2}{3}\\mu_0M$ (parallel), $H_{\\rm in}=-\\frac{1}{3}M$ (antiparallel)",fontsize=10)
fig.tight_layout();save(fig,"fig_ed02_magnetostatics")
