//META {"title":"Bead on a rotating hoop: a pitchfork bifurcation","desc":"A smooth bead on a hoop of radius R that spins about its vertical diameter at Ω. The effective potential U(θ) = −gR cos θ − ½R²Ω² sin²θ has one minimum at the bottom for Ω below √(g/R) and two off-centre minima above it. Drop the bead and watch it settle (with a little friction) or oscillate.","vault":"CM","chapters":["CM02 Lagrange's Equations, Constraints and Generalised Coordinates","CM03 Symmetries, Noether's Theorem and Conservation Laws"],"tryit":"Sweep Ω through √(g/R) = 4.43 rad/s and watch the bottom of the hoop become a maximum while two new minima appear at cos θ₀ = g/(Ω²R)."}
const g=9.81,R=0.5;
ui.gridOf(2);const P1=ui.canvas(340,{xmin:-1.3,xmax:1.3,ymin:-1.4,ymax:1.4,axes:false,equal:true});
const P2=ui.canvas(340,{xmin:-3.2,xmax:3.2,ymin:-12,ymax:8,xlabel:'θ (rad)',ylabel:'U(θ) per unit mass',title:'effective potential'});
const sO=ui.slider('hoop spin Ω (rad/s)',0,10,0.05,6,reset),s0=ui.slider('start angle θ₀ (rad)',-3,3,0.01,1.0,reset),sb=ui.slider('friction b',0,2,0.01,0.3,()=>{});
const out=ui.readout();let th=1,w=0,phi=0;
function reset(){th=s0.value;w=0;draw()}
function U(t,Om){return -g*R*Math.cos(t)-0.5*R*R*Om*Om*Math.sin(t)**2}
function draw(){const Om=sO.value,Oc=Math.sqrt(g/R);
 P1.clear();const c='#888';P1.circle(0,0,P1.X(1)-P1.X(0),null,C.muted,3);
 // hoop shown in its rotating plane: bead at angle th from bottom
 const x=Math.sin(th),y=-Math.cos(th);P1.arrow(0,-1.25,0,1.25,C.grid,1);
 P1.ptext('hoop in its own plane (θ from the bottom)',P1.w/2,12,C.muted,'center');
 P1.circle(x,y,9,C.orange,C.ink);P1.circle(0,0,3,C.ink);
 P1.arrow(-0.9,1.0,-0.9,0.6,C.blue,2);P1.ptext('g',P1.X(-0.9)+8,P1.Y(0.8),C.blue);
 P2.clear();const ts=M.linspace(-3.2,3.2,300);P2.line(ts,ts.map(t=>U(t,Om)),C.blue,3);P2.dot(th,U(th,Om),C.orange,6);
 if(Om>Oc){const t0=Math.acos(g/(Om*Om*R));P2.vline(t0,C.aqua);P2.vline(-t0,C.aqua);P2.text('θ₀=±'+M.fmt(t0*180/Math.PI,3)+'°',t0,5,C.aqua)}
 const E=0.5*R*R*w*w+U(th,Om);
 out.textContent=`Ω = ${M.fmt(Om,3)} rad/s   critical Ω_c = √(g/R) = ${M.fmt(Oc,4)} rad/s   →  ${Om<Oc?'bottom is the only stable equilibrium':'bottom unstable; stable equilibria at cos θ₀ = g/(Ω²R) = '+M.fmt(g/(Om*Om*R),4)+'  (θ₀ = '+M.fmt(Math.acos(g/(Om*Om*R))*180/Math.PI,4)+'°)'}\nθ = ${M.fmt(th,4)}   ω_θ = ${M.fmt(w,4)}   energy per unit mass in the rotating frame h = ${M.fmt(E,4)}${Om>Oc?'   small-oscillation frequency about θ₀: Ω sin θ₀ = '+M.fmt(Om*Math.sin(Math.acos(g/(Om*Om*R))),4)+' rad/s':''}`}
loop((dt)=>{const Om=sO.value,b=sb.value,n=Math.max(1,Math.round(dt/0.002));const h=dt/n;for(let i=0;i<n;i++){const f=(t,y)=>[y[1],Math.sin(y[0])*(Om*Om*Math.cos(y[0])-g/R)-b*y[1]];[th,w]=M.rk4(f,[th,w],0,h)}draw()});
reset();ui.note('Linearising about θ₀: δθ̈ = −Ω² sin²θ₀ δθ (CM02 §7). With Ω = 6, R = 0.5: θ₀ = 56.98°, ω = 5.031 rad/s.');
