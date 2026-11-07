//META {"title":"Two competitors: isoclines decide who wins","desc":"Lotka–Volterra competition: dN₁/dt = r₁N₁(K₁ − N₁ − α₁₂N₂)/K₁ and the mirror equation for species 2. The zero-growth isoclines are straight lines; which one lies outside the other fixes the outcome: species 1 wins, species 2 wins, stable coexistence (each limits itself more than the other, α₁₂α₂₁ < 1 with the K conditions) or an unstable equilibrium (priority effect). Click anywhere in the plane to start a trajectory.","vault":"EE","chapters":["EE04 Competition and Invasions"],"tryit":"K₁ = 100, K₂ = 80, α₁₂ = 0.5, α₂₁ = 0.6 → stable coexistence at (85.7, 28.6). Set both α = 1.5 → saddle at (16, 56): click on either side of the separatrix and watch the winner change."}
ui.gridOf(1);const P=ui.canvas(380,{xmin:0,xmax:160,ymin:0,ymax:160,xlabel:'species 1 abundance N₁',ylabel:'species 2 abundance N₂',equal:true});
const sK1=ui.slider('K₁',40,160,1,100,reset),sK2=ui.slider('K₂',40,160,1,80,reset),s12=ui.slider('α₁₂ (effect of 2 on 1)',0,2,0.01,0.5,reset),s21=ui.slider('α₂₁ (effect of 1 on 2)',0,2,0.01,0.6,reset);
ui.button('clear trajectories',()=>{trs=[]});ui.button('random starts',()=>{const r=M.rng(Math.floor(Math.random()*1e6));for(let i=0;i<8;i++)addTr(r()*150+5,r()*150+5)});
const out=ui.readout();let trs=[];
function f(K1,K2,a12,a21){return(t,y)=>[y[0]*(K1-y[0]-a12*y[1])/K1,0.8*y[1]*(K2-y[1]-a21*y[0])/K2]}
function addTr(x,y0){const K1=sK1.value,K2=sK2.value,a12=s12.value,a21=s21.value;let y=[x,y0],pts=[[...y]],t=0;const fn=f(K1,K2,a12,a21);for(let i=0;i<2500;i++){y=M.rk4(fn,y,t,0.05);t+=0.05;pts.push([...y]);if(i>2000&&Math.hypot(...fn(0,y))<1e-4)break}trs.push(pts)}
function reset(){trs=[];draw()}
P.c.addEventListener('click',e=>{const r=P.c.getBoundingClientRect(),px=e.clientX-r.left,py=e.clientY-r.top;const x=P.invX?P.invX(px):P.o.xmin+(px-P.o.ml)/(P.w-P.o.ml-P.o.mr)*(P.o.xmax-P.o.xmin),y=P.invY?P.invY(py):P.o.ymax-(py-P.o.mt)/(P.h-P.o.mt-P.o.mb)*(P.o.ymax-P.o.ymin);if(x>0&&y>0){addTr(x,y);draw()}});
function draw(){const K1=sK1.value,K2=sK2.value,a12=s12.value,a21=s21.value;const top=Math.max(K1,K2,K1/Math.max(a12,0.01),K2/Math.max(a21,0.01),50);const lim=Math.min(300,top*1.1);P.set({xmax:lim,ymax:lim});P.clear();
 // vector field
 const fn=f(K1,K2,a12,a21);const nn=15;for(let i=1;i<nn;i++)for(let j=1;j<nn;j++){const x=lim*i/nn,y=lim*j/nn,d=fn(0,[x,y]),n=Math.hypot(d[0],d[1])||1;P.arrow(x,y,x+d[0]/n*lim*0.025,y+d[1]/n*lim*0.025,C.grid,1.2,4)}
 P.line([0,K1],[K1/a12,0].map((v,i)=>i?0:K1/Math.max(a12,1e-6)),C.blue,3);P.line([K1,0].slice(0,0),[],C.blue);
 P.line([0,K1],[K1/Math.max(a12,1e-6),0],C.blue,3);P.line([K2/Math.max(a21,1e-6),0],[0,K2],C.orange,3);
 trs.forEach(pts=>{P.line(pts.map(p=>p[0]),pts.map(p=>p[1]),C.ink,1.5);P.dot(pts[0][0],pts[0][1],C.muted,3);const e=pts[pts.length-1];P.dot(e[0],e[1],C.violet,4)});
 // equilibria
 const D=1-a12*a21;const eq=[[0,0],[K1,0],[0,K2]];let N1s=null,N2s=null;if(Math.abs(D)>1e-9){N1s=(K1-a12*K2)/D;N2s=(K2-a21*K1)/D;if(N1s>0&&N2s>0)eq.push([N1s,N2s])}
 let kind;const c1=K1<K2/Math.max(a21,1e-9),c2=K2<K1/Math.max(a12,1e-9);if(c1&&c2)kind='STABLE COEXISTENCE (each limits itself more than the other)';else if(!c1&&!c2)kind='UNSTABLE interior equilibrium: priority effect, the start decides';else if(!c1&&c2)kind='SPECIES 1 WINS';else kind='SPECIES 2 WINS';
 P.legend([['isocline dN₁/dt = 0: N₁ = K₁ − α₁₂N₂',C.blue],['isocline dN₂/dt = 0: N₂ = K₂ − α₂₁N₁',C.orange]],P.o.ml+8,P.o.mt+14);
 if(N1s!==null&&N1s>0&&N2s>0)P.dot(N1s,N2s,D>0?C.aqua:C.red,7);
 out.textContent=`${kind}\nα₁₂α₂₁ = ${M.fmt(a12*a21,3)} (${a12*a21<1?'<':'>'} 1)   conditions: α₁₂ < K₁/K₂ = ${M.fmt(K1/K2,3)} ${a12<K1/K2?'✓':'✗'},  α₂₁ < K₂/K₁ = ${M.fmt(K2/K1,3)} ${a21<K2/K1?'✓':'✗'}\n${N1s!==null&&N1s>0&&N2s>0?'interior equilibrium (N₁*, N₂*) = ('+M.fmt(N1s,4)+', '+M.fmt(N2s,4)+')  '+(D>0?'(stable if both K-conditions hold)':'(saddle)'):'no interior equilibrium'}\nclick the plane to launch trajectories (violet dot = where each ends)`}
draw();ui.note('EE04 Example 2: K₁ = 100, K₂ = 80, α₁₂ = 0.5, α₂₁ = 0.6 gives (85.7, 28.6); α₁₂ = α₂₁ = 1.5 gives the saddle (16, 56). Species 2 growth rate is fixed at 0.8 r₁ (does not affect the isoclines or the outcome).');
