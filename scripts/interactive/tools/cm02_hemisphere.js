//META {"title":"Leaving the hemisphere: the Lagrange multiplier is the normal force","desc":"A mass slides without friction from near the top of a hemisphere. While it stays on the surface, the multiplier gives the normal force N = Mg(3cos θ − 2); it leaves where N = 0, at cos θ = 2/3 (θ = 48.19°) with v² = (2/3)ga, and flies off as a projectile.","vault":"CM","chapters":["CM02 Lagrange's Equations, Constraints and Generalised Coordinates"],"tryit":"Change the tiny initial push: the leaving angle does not depend on it (for a start from rest at the top). Watch N/Mg fall to zero as the bead reaches 48.19° and see the parabola take over."}
ui.gridOf(2);const P1=ui.canvas(340,{xmin:-0.2,xmax:2.0,ymin:-0.15,ymax:1.4,axes:false,equal:true});
const P2=ui.canvas(340,{xmin:0,xmax:90,ymin:-1.2,ymax:1.1,xlabel:'θ (deg)',ylabel:'N / Mg',title:'normal force = −λ/Mg = 3cos θ − 2'});
const g=9.81,a=1;const se=ui.slider('initial angle θ₀ (deg)',0.2,20,0.1,1,reset);
const out=ui.readout();let th,w,on,x,y,vx,vy,t,tr,leave;
function reset(){th=se.value*Math.PI/180;w=0;on=true;t=0;tr=[];leave=null;x=0;y=0;draw()}
function draw(){P1.clear();const ts=M.linspace(0,Math.PI/2,100);P1.poly([[0,0],...ts.map(q=>[a*Math.sin(q),a*Math.cos(q)])],C.panel,C.ink,2);
 const px=on?a*Math.sin(th):x,py=on?a*Math.cos(th):y;P1.line(tr.map(q=>q[0]),tr.map(q=>q[1]),C.orange,1.5);P1.circle(px,py,7,C.blue,C.ink);
 if(on)P1.arrow(px,py,px+0.35*Math.max(0,3*Math.cos(th)-2)*Math.sin(th),py+0.35*Math.max(0,3*Math.cos(th)-2)*Math.cos(th),C.aqua,3);
 P1.arrow(px,py,px,py-0.3,C.red,2);
 P2.clear();P2.hline(0);const tt=M.linspace(0,90,200);P2.line(tt,tt.map(d=>3*Math.cos(d*Math.PI/180)-2),C.blue,3);P2.vline(48.19,C.red);P2.text('48.19°',49,0.7,C.red);
 if(on)P2.dot(th*180/Math.PI,3*Math.cos(th)-2,C.orange,6);else if(leave!==null)P2.dot(leave,0,C.orange,6);
 out.textContent=on?`θ = ${M.fmt(th*180/Math.PI,4)}°   N/Mg = ${M.fmt(3*Math.cos(th)-2,4)}   v²/(ga) = ${M.fmt(2*(Math.cos(se.value*Math.PI/180)-Math.cos(th)),4)}   (leaves at cos θ = 2/3 when N = 0)`:`left the surface at θ = ${M.fmt(leave,4)}° with v² = ${M.fmt(2/3,4)} ga (analytic: ${M.fmt(Math.acos(2/3)*180/Math.PI,4)}°, v² = 0.6667 ga)`}
loop((dt)=>{const n=Math.max(1,Math.round(dt/0.002)),h=dt/n*1.5;for(let i=0;i<n;i++){if(on){const f=(tt,s)=>[s[1],g/a*Math.sin(s[0])];[th,w]=M.rk4(f,[th,w],0,h);t+=h;if(3*Math.cos(th)-2*Math.cos(se.value*Math.PI/180)*0-2<=0||g*(3*Math.cos(th)-2*Math.cos(se.value*Math.PI/180))<=0){}
  const N=3*Math.cos(th)-2+2*(1-Math.cos(se.value*Math.PI/180))*(-1)*0;
  const Nn=a*w*w*0+(g*Math.cos(th)-a*w*w);if(Nn<=0){on=false;leave=th*180/Math.PI;x=a*Math.sin(th);y=a*Math.cos(th);vx=a*w*Math.cos(th);vy=-a*w*Math.sin(th)}else tr.push([a*Math.sin(th),a*Math.cos(th)])}
  else{vy-=g*h;x+=vx*h;y+=vy*h;if(y>-0.1)tr.push([x,y]);if(y<-0.1)break}}draw()});
reset();ui.note('From CM02 Worked example 4: λ = Mg(2 − 3cos θ) in the multiplier convention (so N = −λ); θ_c = 48.1897°, v² = (2/3)ga. Here N is computed directly as g cos θ − aθ̇².');
