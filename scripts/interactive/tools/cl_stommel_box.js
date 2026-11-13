//META {"title": "Can the Atlantic overturning switch off? The Stommel two-box model", "desc": "A warm salty box and a cold fresher box. In a nondimensional form the equator–pole temperature and salinity differences x and y obey dx/dt = 1 − x(1+|q|) and dy/dt = F − |q| y with flow q = x − y (q > 0: sinking in the cold box) and freshwater forcing F. For 0 < F < F_max = 0.141 there are two thermally driven steady states (one stable, one unstable) and, for every F > 0, one reversed state: the circulation can be on or off for the same forcing. Raise F past F_max and the flow collapses; lower it again and it stays off until F falls below zero (hysteresis).", "vault": "CL", "chapters": ["CL26 The Ocean's Ledger V - Mass, the Overturning and the Switch", "CL04 Feedback and Multiple Steady States"], "tryit": "Start at F = 0 (q = 0.62, on). Slide F slowly up to 0.12: q falls but stays on. Go to 0.15: it drops to the reversed branch (q < 0). Slide F back down to 0.05, then 0.0: it stays off. Only at F slightly below 0 does it switch back on. Press 'ramp up and down' to watch the whole loop."}
ui.gridOf(2);
const PA=ui.canvas(380,{xmin:-0.06,xmax:0.25,ymin:-0.5,ymax:0.7,xlabel:'freshwater forcing F',ylabel:'overturning q = x − y',title:'steady states and the system'});
const PB=ui.canvas(380,{xmin:0,xmax:60,ymin:-0.5,ymax:0.7,xlabel:'time (model units)',ylabel:'q',title:'q(t) as F changes'});
const sF=ui.slider('freshwater forcing F',-0.06,0.25,0.002,0.0,null);
let x=1/(1+0.62)*1, y=0.0; // start on the thermal branch at F=0: q=0.618
let q0=0.618;x=1/(1+q0);y=x-q0;let F=0,hist=[],t=0,ramp=0;
const Fth=q=>q*(1-q-q*q)/(1+q),Frev=a=>a/(1+a)+a*a;
function step(dt){const q=x-y;const f=(xx,yy)=>[1-xx*(1+Math.abs(xx-yy)),F-Math.abs(xx-yy)*yy];
 const s=M.rk4((tt,v)=>f(v[0],v[1]),[x,y],0,dt);x=s[0];y=s[1];}
function draw(){const qa=M.linspace(1e-3,0.62,300);PA.clear();
 PA.line(qa.filter(q=>q>0.297).map(Fth),qa.filter(q=>q>0.297),C.blue,3);PA.line(qa.filter(q=>q<=0.297).map(Fth),qa.filter(q=>q<=0.297),C.blue,2,[6,4]);
 const aa=M.linspace(1e-3,0.6,200);PA.line(aa.map(Frev),aa.map(a=>-a),C.orange,3);PA.hline(0,C.muted);PA.vline(0,C.muted);PA.vline(0.1408,C.red);PA.text('F_max = 0.141',0.1425,0.62,C.red);
 PA.text('on (stable)',0.0,0.55,C.blue);PA.text('unstable',0.09,0.1,C.blue);PA.text('reversed (stable)',0.12,-0.38,C.orange);
 PA.dot(F,x-y,C.ink,7);
 PB.clear();if(hist.length>1){PB.line(hist.map(h=>h[0]),hist.map(h=>h[1]),C.ink,2);PB.line(hist.map(h=>h[0]),hist.map(h=>h[2]*2),C.violet,1.5,[3,3]);}
 PB.legend([['q',C.ink],['F × 2 (forcing, scaled)',C.violet,[3,3]]],PB.o.ml+8,PB.o.mt+14);
 out.textContent=`F = ${M.fmt(F,3)}: q = ${M.fmt(x-y,3)} (${x-y>0?'overturning on':'reversed / off'}),  x = ${M.fmt(x,3)}, y = ${M.fmt(y,3)}.  F_max = 0.141 at q = 0.30. For this F: ${F<0?'only the on state':F<0.1408?'three steady states (on stable, unstable, reversed stable)':'only the reversed state'}.`}
const out=ui.readout();
sF.el.addEventListener('input',()=>{F=sF.value;ramp=0});
ui.button('reset to on, F = 0',()=>{x=1/(1+q0);y=x-q0;F=0;sF.value=0;hist=[];t=0;ramp=0});
ui.button('ramp up and down',()=>{ramp=1;F=sF.value=-0.04});
loop((dt)=>{const n=8;for(let k=0;k<n;k++){if(ramp===1){F+=0.0035*0.04;if(F>0.25)ramp=2}else if(ramp===2){F-=0.0035*0.04;if(F<-0.05)ramp=0}step(0.04);t+=0.04}
 if(ramp)sF.value=F;hist.push([t,x-y,F]);if(hist.length>1500)hist.shift();if(t>60){const t0=hist[0][0];PB.set({xmin:t0,xmax:t0+60})}draw()});
ui.note('CL26 §7. My nondimensionalisation of Stommel (1961); F_max and the branches are checked in scripts/fig_cl26.py. Time units are arbitrary: the ramp is slow compared with the relaxation, so the jumps are at F ≈ F_max and F ≈ 0.');
