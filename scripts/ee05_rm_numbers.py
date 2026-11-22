"""Rosenzweig-MacArthur check for EE05 (saturating predator restores cycles)."""
import numpy as np
from scipy.integrate import solve_ivp
r,a,h,e,m=1.0,0.02,0.5,0.5,0.25
Hs=m/(a*(e-m*h)); KH=2*Hs+1/(a*h)
print(f"H*={Hs:.2f}  Hopf K={KH:.1f}")
def f(t,y,K):
    H,P=y; g=a*H/(1+a*h*H)
    return [r*H*(1-H/K)-g*P, e*g*P-m*P]
for K in (120,150,200,300):
    s=solve_ivp(f,(0,3000),[Hs*1.2,10],args=(K,),rtol=1e-9,atol=1e-9,dense_output=True)
    t=np.linspace(2000,3000,20001); H,P=s.sol(t)
    print(f"K={K}: H range {H.min():.1f}-{H.max():.1f}, P range {P.min():.1f}-{P.max():.1f}")
