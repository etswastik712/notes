"""Numbers for LS29 (the fluvial lecture slides, worked through)."""
import numpy as np, math
z=np.array([[78,72,69,71,58,49],[74,67,56,49,46,50],[69,53,44,37,38,48],
            [64,58,55,22,31,24],[68,61,47,21,16,19],[74,53,34,12,11,12]],float)
slide=np.array([[2,2,2,4,4,8],[2,2,2,4,4,8],[1,1,2,4,8,4],[128,128,1,2,4,8],[2,2,1,4,4,4],[1,1,1,1,4,16]])
# ESRI coding: E=1, SE=2, S=4, SW=8, W=16, NW=32, N=64, NE=128
nb={1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1),64:(-1,0),128:(-1,1)}
n,m=z.shape; d=np.zeros_like(slide); drops={}
for i in range(n):
  for j in range(m):
    best,bc=-1e9,0
    for c,(di,dj) in nb.items():
      a,b=i+di,j+dj
      if 0<=a<n and 0<=b<m:
        dist=math.sqrt(2) if di and dj else 1
        g=(z[i,j]-z[a,b])/dist
        if g>best: best,bc=g,c
    d[i,j]=bc if best>0 else 0
print("D8 computed:\n",d); print("matches slide where interior:", (d==slide).sum(),"/36")
print("mismatch cells:",[(i,j,int(d[i,j]),int(slide[i,j])) for i in range(n) for j in range(m) if d[i,j]!=slide[i,j]])
# accumulation (number of upstream cells) using computed directions
acc=np.ones_like(z)
order=sorted([(z[i,j],i,j) for i in range(n) for j in range(m)],reverse=True)
for _,i,j in order:
  c=d[i,j]
  if c:
    a,b=i+nb[c][0],j+nb[c][1]; acc[a,b]+=acc[i,j]
print("accumulation:\n",acc.astype(int))
# overland flow: q=(R-I)x ; Manning h=(n q/S^0.5)^0.6 ; tau=rho g h S
R,I=50e-3/3600,10e-3/3600   # 50 mm/hr rain, 10 mm/hr infiltration
nM=0.04; rho,g=1000,9.81
for S in (0.05,0.1,0.2):
  for x in (10,50,100):
    q=(R-I)*x; h=(nM*q/S**0.5)**0.6; tau=rho*g*h*S
    print(f"S={S} x={x}: q={q:.2e} m2/s h={h*1000:.2f} mm tau={tau:.2f} Pa")
tc=5.0
for S in (0.05,0.1,0.2,0.4):
  # tau=rho g S (nM (R-I) x / S^.5)^.6 = tc -> x
  x=((tc/(rho*g*S))**(1/0.6)*S**0.5/(nM*(R-I)))
  print(f"channel head for tau_c={tc} Pa at S={S}: x_c={x:.1f} m")
print("Horton check b+f+m:",0.5+0.4+0.1)
# effective discharge: frequency ~ Q^-a for Q>Q0, transport ~ (Q-Qc)^1.5
Q=np.linspace(1,400,4000); f=Q**-2.5*np.exp(-5/Q); qs=np.clip(Q-20,0,None)**1.5
prod=f*qs; print("toy effective discharge Q* =",Q[prod.argmax()])
# Bengal fan
V=12.5e6*1e9; rhos=2000; supply=700e9  # kg/yr
print("Bengal fan mass kg:",V*rhos," years at 700 Mt/yr:",V*rhos/supply/1e6,"Myr")
# Niagara
print("Niagara retreat ~11 km/12.5 kyr:",11e3/12.5e3,"m/yr")
