//META {"title":"Driven damped oscillator: resonance curve, phase and transient","desc":"x'' + b x' + ω₀²x = cos(γt), ω₀ = 2. Left: the steady-state amplitude and phase lag as a function of the driving frequency γ, with the current γ marked. Right: the actual motion from rest, which is the steady state plus a decaying transient (beats when damping is small, linear growth at resonance with b = 0).","vault":"CM","chapters":["CM06 Small Oscillations and Normal Modes"],"tryit":"Set b = 0 and γ = ω₀: the amplitude grows ∝ t sin ω₀t. Put γ = 2.1 for beats with period 62.8. Then add damping and see the peak height ~ 1/(bω₀)."}
const w0=2;
ui.gridOf(2);const P1=ui.canvas(320,{xmin:0,xmax:4,ymin:0,ymax:6,xlabel:'driving frequency γ',ylabel:'amplitude',title:'steady-state response'});
const P2=ui.canvas(320,{xmin:0,xmax:60,ymin:-6,ymax:6,xlabel:'t',ylabel:'x(t)',title:'motion from rest'});
const sg=ui.slider('driving frequency γ',0.2,4,0.01,1.9,reset),sb=ui.slider('damping b',0,1.5,0.01,0.1,reset);
const out=ui.readout();let hist,s,t;
function amp(g,b){return 1/Math.sqrt((w0*w0-g*g)**2+(b*g)**2)}
function reset(){s=[0,0];t=0;hist=[];const g=sg.value,b=sb.value;const f=(tt,y)=>[y[1],-w0*w0*y[0]-b*y[1]+Math.cos(g*tt)];const h=0.01;let mx=0;for(let i=0;i<6000;i++){s=M.rk4(f,s,t,h);t+=h;hist.push([t,s[0]])}P2.set({ymin:-Math.max(1,Math.max(...hist.map(a=>Math.abs(a[1]))))*1.1,ymax:Math.max(1,Math.max(...hist.map(a=>Math.abs(a[1]))))*1.1});draw()}
function draw(){const g=sg.value,b=sb.value;const gs=M.linspace(0.02,4,400);const A=gs.map(x=>amp(x,b));const top=Math.min(30,Math.max(1,Math.max(...A)*1.1));P1.set({ymax:top});P1.clear();P1.line(gs,A,C.blue,3);P1.vline(g,C.orange);P1.vline(w0,C.muted,[2,4]);P1.dot(g,Math.min(top,amp(g,b)),C.orange,6);
 const ph=gs.map(x=>Math.atan2(b*x,w0*w0-x*x)/Math.PI*top);P1.line(gs,ph,C.aqua,1.5,[5,3]);P1.ptext('phase lag (dashed, 0 → π)',P1.w-12,P1.o.mt+14,C.aqua,'right');
 P2.clear();P2.line(hist.map(h=>h[0]),hist.map(h=>h[1]),C.blue,1.6);
 const env=b>0?amp(g,b):null;if(env){P2.hline(env,C.orange,[4,3]);P2.hline(-env,C.orange,[4,3])}
 const Q=b>0?w0/b:Infinity;out.textContent=`γ = ${M.fmt(g,3)}  ω₀ = 2  b = ${M.fmt(b,3)}   steady amplitude = ${b===0&&Math.abs(g-w0)<1e-9?'∞ (resonance, grows ∝ t)':M.fmt(amp(g,b),5)}   phase lag = ${M.fmt(Math.atan2(b*g,w0*w0-g*g)*180/Math.PI,4)}°\npeak amplitude ≈ 1/(bω₀) = ${b>0?M.fmt(1/(b*w0),4):'∞'}   quality factor Q = ω₀/b = ${M.fmt(Q,3)}   ${b===0&&Math.abs(g-w0)>1e-6?'beats: period 2π/|γ−ω₀| = '+M.fmt(2*Math.PI/Math.abs(g-w0),4):''}`}
reset();ui.note('Checks (CM06 Worked example 2): b = 0, γ = 2 → x(10) = 2.282363 = (10/4) sin 20 (not drawn here: slide t to 10); γ = 2.1 → maximum amplitude 2/|ω²−γ²| = 4.878.');
