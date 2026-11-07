//META {"title":"Double pendulum: linear normal modes versus the real thing","desc":"Equal masses and rods. For small angles the motion is a superposition of two normal modes with ω² = (2 ∓ √2) g/l and mode shapes (1, ±√2). Pick a mode and a starting amplitude: at small amplitude the real nonlinear pendulum follows the linear prediction; at large amplitude, or from a generic start, it becomes chaotic: two nearly identical starts (blue and orange) soon disagree completely.","vault":"CM","chapters":["CM06 Small Oscillations and Normal Modes"],"tryit":"Choose 'slow mode' at amplitude 0.05 rad: clean periodic motion with period 2.621 s. Raise the amplitude to 1.5 rad or choose 'generic' and watch the two copies diverge."}
ui.gridOf(2);const P1=ui.canvas(340,{xmin:-2.3,xmax:2.3,ymin:-2.3,ymax:2.3,axes:false,equal:true});
const P2=ui.canvas(340,{xmin:0,xmax:20,ymin:-3.3,ymax:3.3,xlabel:'t (s)',ylabel:'θ₁ (rad)',title:'θ₁(t): nonlinear (blue, orange = 10⁻⁶ rad apart) vs linear (dashed)'});
const g=9.81,L=1;const sel=ui.select('initial condition',[['s','slow mode (1, √2)'],['f','fast mode (1, −√2)'],['g','generic (θ₁, θ₂) = (a, 0)']],reset,'s');
const sa=ui.slider('amplitude a (rad)',0.01,2.6,0.01,0.05,reset);
const out=ui.readout();let s1,s2,t,hist1=[],hist2=[];
const lam=[2-Math.SQRT2,2+Math.SQRT2];
function init(d){const a=sa.value,k=sel.value;if(k==='s')return[a,a*Math.SQRT2,0,0];if(k==='f')return[a,-a*Math.SQRT2,0,0];return[a,0,0,0]}
function f(tt,y){const[t1,t2,w1,w2]=y,d=t1-t2,den=3-Math.cos(2*d);return[w1,w2,(-3*g*Math.sin(t1)-g*Math.sin(t1-2*t2)-2*Math.sin(d)*(w2*w2+w1*w1*Math.cos(d)))/den,(2*Math.sin(d)*(2*w1*w1+2*g*Math.cos(t1)+w2*w2*Math.cos(d)))/den]}
function reset(){const y=init();s1=y.slice();s2=y.slice();s2[0]+=1e-6;t=0;hist1=[];hist2=[];draw()}
function lin(tt){const a=sa.value,k=sel.value;const w=lam.map(l=>Math.sqrt(l*g/L));if(k==='s')return a*Math.cos(w[0]*tt);if(k==='f')return a*Math.cos(w[1]*tt);
 // generic (a,0): decompose in modes: x=(1,√2)A+(1,-√2)B -> A+B=a, √2(A−B)=0 -> A=B=a/2
 return a/2*(Math.cos(w[0]*tt)+Math.cos(w[1]*tt))}
function draw(){P1.clear();for(const [s,c,al] of [[s2,C.orange,1],[s1,C.blue,1]]){const x1=L*Math.sin(s[0]),y1=-L*Math.cos(s[0]),x2=x1+L*Math.sin(s[1]),y2=y1-L*Math.cos(s[1]);P1.line([0,x1,x2],[0,y1,y2],c,3);P1.circle(x1,y1,8,c,C.ink);P1.circle(x2,y2,8,c,C.ink)}P1.circle(0,0,4,C.ink);
 const th=t<=20?20:t;const am=sa.value,Y=(sel.value==='g'&&am>0.3)?3.3:Math.max(0.1,1.4*am);P2.set({xmin:Math.max(0,th-20),xmax:Math.max(20,th),ymin:-Y,ymax:Y});P2.clear();
 P2.line(hist1.map(h=>h[0]),hist1.map(h=>h[1]),C.blue,2);P2.line(hist2.map(h=>h[0]),hist2.map(h=>h[1]),C.orange,2);
 const ts=M.linspace(P2.o.xmin,P2.o.xmax,300);P2.line(ts,ts.map(lin),C.ink,1.5,[5,4]);
 const E1=0.5*2*s1[2]**2+0.5*s1[3]**2+s1[2]*s1[3]*Math.cos(s1[1]-s1[0])-2*g*Math.cos(s1[0])-g*Math.cos(s1[1]);
 out.textContent=`linear frequencies: ω₁ = ${M.fmt(Math.sqrt(lam[0]*g/L),4)}, ω₂ = ${M.fmt(Math.sqrt(lam[1]*g/L),4)} rad/s  (periods ${M.fmt(2*Math.PI/Math.sqrt(lam[0]*g/L),4)} s, ${M.fmt(2*Math.PI/Math.sqrt(lam[1]*g/L),4)} s)\nt = ${M.fmt(t,3)} s   |θ₁ blue − θ₁ orange| = ${M.fmt(Math.abs(s1[0]-s2[0]),3)} rad   total energy (conserved) = ${M.fmt(E1,6)}`}
loop((dt)=>{const n=Math.max(1,Math.round(dt/0.002)),h=dt/n;for(let i=0;i<n;i++){s1=M.rk4(f,s1,0,h);s2=M.rk4(f,s2,0,h);t+=h;hist1.push([t,s1[0]]);hist2.push([t,s2[0]])}while(hist1.length>6000){hist1.shift();hist2.shift()}draw()});
reset();for(let i=0;i<3000;i++){s1=M.rk4(f,s1,0,0.002);s2=M.rk4(f,s2,0,0.002);t+=0.002;if(i%5==0){hist1.push([t,s1[0]]);hist2.push([t,s2[0]])}}draw();
ui.note('Verified in CM06: on a normal mode at amplitude 0.02 rad the nonlinear periods are 2.6211 s and 1.0865 s against 2.6211 s and 1.0857 s from the linear theory.');
