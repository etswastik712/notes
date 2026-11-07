//META {"title":"Two coupled oscillators: normal modes and beats","desc":"Two equal masses on springs with a coupling spring. Choose how much of the in-phase mode (frequency ω₁ = √(ω₀² − α)) and the anti-phase mode (ω₂ = √(ω₀² + α)) you start with. Pure modes oscillate rigidly; a mixture beats, passing energy back and forth with period 2π/(ω₂ − ω₁).","vault":"CM","chapters":["CM06 Small Oscillations and Normal Modes"],"tryit":"Start with all of the motion in the in-phase mode, then all in the anti-phase mode, then 50/50 (x=1, y=0): that is the full-transfer beat. Increase the coupling α to speed the beats."}
ui.gridOf(2);const P1=ui.canvas(260,{xmin:-1.5,xmax:1.5,ymin:-0.6,ymax:0.6,axes:false,equal:true});
const P2=ui.canvas(260,{xmin:0,xmax:80,ymin:-1.1,ymax:1.1,xlabel:'t',ylabel:'x, y',title:'displacements'});
const sa=ui.slider('coupling α (ω₀ = 1)',0.02,0.4,0.01,0.1,reset),sm=ui.slider('in-phase mode amplitude',0,1,0.01,0.5,reset),sn=ui.slider('anti-phase mode amplitude',0,1,0.01,0.5,reset);
const out=ui.readout();let t=0,hist=[];
function xy(tt){const a=sa.value,w1=Math.sqrt(1-a),w2=Math.sqrt(1+a),A=sm.value,B=sn.value;return[A*Math.cos(w1*tt)+B*Math.cos(w2*tt),A*Math.cos(w1*tt)-B*Math.cos(w2*tt)]}
function reset(){t=0;hist=[];draw()}
function draw(){const a=sa.value,w1=Math.sqrt(1-a),w2=Math.sqrt(1+a);P1.clear();
 const [x,y]=xy(t);const s=0.8;const x0=-0.7,y0=0.7;P1.line([-1.4,x0+s*x*0.9-0.0],[0,0],C.grid,0);
 P1.line([-1.4,-1.0+0.5*x],[0,0],C.muted,2);P1.line([-1.0+0.5*x,-0.2+0.5*x],[0,0],C.muted,0);
 P1.circle(-0.55+0.5*x,0,12,C.blue,C.ink);P1.circle(0.55+0.5*y,0,12,C.orange,C.ink);P1.line([-0.55+0.5*x+0.09,0.55+0.5*y-0.09],[0,0],C.aqua,3,[5,3]);
 P1.line([-1.4,-0.55+0.5*x-0.09],[0,0],C.muted,2);P1.line([0.55+0.5*y+0.09,1.4],[0,0],C.muted,2);
 P1.ptext('x',P1.X(-0.55+0.5*x),P1.Y(0)-22,C.blue,'center');P1.ptext('y',P1.X(0.55+0.5*y),P1.Y(0)-22,C.orange,'center');
 hist.push([t,x,y]);if(hist.length>3000)hist.shift();
 const t1=Math.max(80,t);P2.set({xmin:t1-80,xmax:t1});P2.clear();P2.line(hist.map(h=>h[0]),hist.map(h=>h[1]),C.blue,1.5);P2.line(hist.map(h=>h[0]),hist.map(h=>h[2]),C.orange,1.5);
 const e1=sm.value**2,e2=sn.value**2;
 out.textContent=`ω₁ = √(1−α) = ${M.fmt(w1,5)}   ω₂ = √(1+α) = ${M.fmt(w2,5)}   beat period 2π/(ω₂−ω₁) = ${M.fmt(2*Math.PI/(w2-w1),4)}   full energy transfer after π/(ω₂−ω₁) = ${M.fmt(Math.PI/(w2-w1),4)}\nnormal coordinates Q₊ = (x+y)/√2, Q₋ = (x−y)/√2 ;  energy share in-phase : anti-phase = ${M.fmt(e1/(e1+e2||1),3)} : ${M.fmt(e2/(e1+e2||1),3)}`}
loop((dt)=>{t+=dt*3;draw()});
// pre-roll
for(let i=0;i<400;i++){t+=0.1;const [x,y]=xy(t);hist.push([t,x,y])}draw();
ui.note('LL §23 Problem 1: (ω₀²−ω²)² = α². With ω₀ = 1, α = 0.1: ω₁ = 0.94868, ω₂ = 1.04881, beat period 62.75, full transfer at 31.38.');
