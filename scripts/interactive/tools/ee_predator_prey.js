//META {"title":"Predator–prey cycles: closed orbits and damped spirals","desc":"Lotka–Volterra: dH/dt = rH(1 − H/K) − pHP, dP/dt = apHP − mP. With K = ∞ (prey growth exponential) every orbit is a closed curve around (H*, P*) = (m/ap, r/p); a conserved quantity V labels them. Turn on a finite carrying capacity K and the centre becomes a stable spiral: the cycles damp. Left: phase plane with isoclines and the vector field; right: time series, with the predator peak lagging the prey peak.","vault":"EE","chapters":["EE05 Predation"],"tryit":"Defaults r=1, p=0.02, a=0.5, m=0.5 give (H*,P*) = (50,50) and period 8.9 for small cycles; the large orbit from (30,30) has period 9.26. Set K = 200: the equilibrium moves to (50, 37.5), eigenvalues −0.125 ± 0.60i. Double r: predators double, prey unchanged."}
ui.gridOf(2);const P1=ui.canvas(340,{xmin:0,xmax:140,ymin:0,ymax:140,xlabel:'prey H',ylabel:'predators P',title:'phase plane'});const P2=ui.canvas(340,{xmin:0,xmax:40,ymin:0,ymax:140,xlabel:'time',ylabel:'abundance',title:'time series'});
const sr=ui.slider('prey growth r',0.2,2,0.01,1,restart),sp=ui.slider('predation p',0.005,0.05,0.001,0.02,restart),sa=ui.slider('conversion a',0.1,1,0.01,0.5,restart),sm=ui.slider('predator mortality m',0.1,1.5,0.01,0.5,restart),sK=ui.slider('prey carrying capacity K (0 = unlimited)',0,400,5,0,restart),sH=ui.slider('start H₀',5,140,1,30,restart),sP=ui.slider('start P₀',5,140,1,30,restart);
const out=ui.readout();let traj=[],tmax=0,y,t;
function f(t_,y_){const r=sr.value,p=sp.value,a=sa.value,m=sm.value,K=sK.value;const H=y_[0],P=y_[1];return[r*H*(K>0?1-H/K:1)-p*H*P,a*p*H*P-m*P]}
function restart(){y=[sH.value,sP.value];t=0;traj=[[0,y[0],y[1]]]}
restart();
function draw(){const r=sr.value,p=sp.value,a=sa.value,m=sm.value,K=sK.value;const Hs=m/(a*p),Ps=K>0?r/p*(1-Hs/K):r/p; P1.set({xmax:Math.max(140,Math.max(...traj.map(q=>q[1]))*1.1,Hs*2),ymax:Math.max(140,Math.max(...traj.map(q=>q[2]))*1.1,Ps*2)});P1.clear();
 // vector field
 const nx=14,ny=14;for(let i=1;i<nx;i++)for(let j=1;j<ny;j++){const H=P1.o.xmax*i/nx,P=P1.o.ymax*j/ny;const d=f(0,[H,P]);const n=Math.hypot(d[0]/P1.o.xmax,d[1]/P1.o.ymax)||1;const L=0.018;P1.arrow(H,P,H+d[0]/P1.o.xmax/n*L*P1.o.xmax,P+d[1]/P1.o.ymax/n*L*P1.o.ymax,C.grid,1.2,4)}
 // isoclines
 P1.vline(Hs,C.violet);if(K>0)P1.line([0,K],[r/p,0],C.aqua,2.2);else P1.line([0,P1.o.xmax],[r/p,r/p],C.aqua,2.2);
 P1.line(traj.map(q=>q[1]),traj.map(q=>q[2]),C.blue,2.2);const e=traj[traj.length-1];P1.dot(e[1],e[2],C.orange,6);P1.dot(Hs,Ps,C.red,6);
 P1.legend([['predator isocline H = m/ap',C.violet],['prey isocline',C.aqua],['trajectory',C.blue]],P1.o.ml+8,P1.o.mt+14);
 P2.set({xmax:Math.max(40,t),ymax:Math.max(100,Math.max(...traj.map(q=>Math.max(q[1],q[2])))*1.1)});P2.clear();P2.line(traj.map(q=>q[0]),traj.map(q=>q[1]),C.blue,2.4);P2.line(traj.map(q=>q[0]),traj.map(q=>q[2]),C.orange,2.4);P2.legend([['prey H',C.blue],['predators P',C.orange]],P2.o.ml+8,P2.o.mt+14);
 const V=a*p*e[1]-m*Math.log(e[1])+p*e[2]-r*Math.log(e[2]);
 let eig='';if(K>0){const tr=-r*Hs/K,det=a*p*p*Hs*Ps;const disc=tr*tr-4*det;eig=disc<0?`eigenvalues ${M.fmt(tr/2,4)} ± ${M.fmt(Math.sqrt(-disc)/2,4)} i (damped spiral, amplitude halves every ${M.fmt(Math.log(2)/Math.abs(tr/2),3)})`:`eigenvalues ${M.fmt((tr+Math.sqrt(disc))/2,4)}, ${M.fmt((tr-Math.sqrt(disc))/2,4)} (node)`}else eig=`eigenvalues ± i√(rm) = ± ${M.fmt(Math.sqrt(r*m),4)} i (neutral), small-cycle period 2π/√(rm) = ${M.fmt(2*Math.PI/Math.sqrt(r*m),4)}`;
 out.textContent=`equilibrium (H*, P*) = (m/ap, ${K>0?'(r/p)(1 − H*/K)':'r/p'}) = (${M.fmt(Hs,4)}, ${M.fmt(Ps,4)})${K>0&&Hs>=K?'  (K < H*: predators cannot persist)':''}\n${eig}\n${K>0?'conserved quantity no longer exists (prey self-limitation damps the orbit)':'V = apH − m ln H + pP − r ln P = '+M.fmt(V,6)+' (constant on the orbit: this is why it closes)'}`}
function advance(dt){const steps=Math.ceil(dt/0.01),h=dt/steps;for(let i=0;i<steps;i++){y=M.rk4(f,y,t,h);t+=h;if(y[0]<1e-6)y[0]=1e-6;if(y[1]<1e-6)y[1]=1e-6}traj.push([t,y[0],y[1]]);if(traj.length>6000)traj.shift()}
for(let i=0;i<90;i++)advance(0.2);
loop((dt)=>{advance(dt);draw()});draw();
ui.note('EE05: with r = 1, p = 0.02, a = 0.5, m = 0.5 and start (30, 30) the prey range over 19.5–102.5, predators 26.4–84.6, period 9.26, predator peak lags the prey peak by 1.7. With K = 200 the equilibrium is (50, 37.5).');
