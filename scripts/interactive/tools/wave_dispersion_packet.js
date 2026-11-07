//META {"title":"Wave packets: phase velocity versus group velocity","desc":"A packet is a superposition of plane waves ψ(x,t) = ∫ A(k) e^{i(kx − ω(k)t)} dk with a Gaussian A(k) centred on k₀. Choose the medium (dispersion relation ω(k)): the carrier ripples move at the phase velocity ω/k, the envelope (and the energy) at the group velocity dω/dk, and with dispersion the packet spreads. Markers show both velocities.","vault":"Waves","chapters":["ED06 Waves in Matter, Reflection and Dispersion","ED07 Guided Waves","QM01 From Waves to Probabilities","LS26 Sea Level and Ocean Waves"],"tryit":"Deep water: v_g = v_p/2 (ripples run through the packet). Waveguide/plasma: v_p·v_g = c², ripples faster than c but the packet slower. Schrödinger: ω = k²/2, v_g = 2v_p. Non-dispersive: nothing spreads."}
ui.gridOf(1);const P=ui.canvas(320,{xmin:-10,xmax:60,ymin:-1.2,ymax:1.2,xlabel:'x',ylabel:'ψ (real part) and envelope'});const P2=ui.canvas(170,{xmin:0,xmax:5,ymin:0,ymax:5,xlabel:'k',ylabel:'ω(k)',title:'dispersion relation'});
const rel=ui.select('medium',[['lin','non-dispersive ω = ck (c=1)'],['deep','deep water ω = √(g k), g=1'],['cap','capillary waves ω = √(k³), σ/ρ=1'],['wg','waveguide / plasma ω = √(1 + k²)'],['sch','Schrödinger ω = k²/2']],reset,'deep');
const sk=ui.slider('carrier wave number k₀',0.5,4,0.05,1.5,reset),sw=ui.slider('packet width in k (σ_k)',0.05,0.5,0.01,0.12,reset),sx=ui.slider('initial position x₀',-5,10,0.5,0,reset);
const out=ui.readout();let t=0;
const om={lin:k=>k,deep:k=>Math.sqrt(k),cap:k=>Math.pow(k,1.5),wg:k=>Math.sqrt(1+k*k),sch:k=>k*k/2};
function reset(){t=0;draw()}
function field(x,t){const k0=sk.value,s=sw.value,w=om[rel.value];const ks=M.linspace(Math.max(0.01,k0-4*s),k0+4*s,121);let re=0,im=0,dk=ks[1]-ks[0];for(const k of ks){const A=Math.exp(-((k-k0)**2)/(2*s*s));const ph=k*(x-sx.value)-w(k)*t;re+=A*Math.cos(ph);im+=A*Math.sin(ph)}const n=Math.sqrt(2*Math.PI)*s/dk;return[re/n,im/n]}
function draw(){const k0=sk.value,w=om[rel.value],h=1e-4,vp=w(k0)/k0,vg=(w(k0+h)-w(k0-h))/(2*h);const xc=sx.value+vg*t;P.set({xmin:xc-30,xmax:xc+30});P.clear();const xs=M.linspace(P.o.xmin,P.o.xmax,800),f=xs.map(x=>field(x,t));
 P.line(xs,f.map(a=>a[0]),C.blue,1.5);const env=f.map(a=>Math.hypot(a[0],a[1]));P.line(xs,env,C.orange,2.5);P.line(xs,env.map(e=>-e),C.orange,2.5);
 P.dot(xc,0,C.red,6);P.text('v_g',xc,0.2,C.red,'center');
 // a ripple crest tracked at phase velocity: crest position where k0 x - w0 t = const ; follow arrow
 const crestX=sx.value+vp*t;const xcr=xc-((xc-crestX)%(2*Math.PI/k0));P.dot(xcr,0.0,C.violet,5);P.legend([['Re ψ (ripples)',C.blue],['|ψ| envelope',C.orange]],P.o.ml+8,P.o.mt+14);
 P2.clear();const ks=M.linspace(0.05,5,200);P2.set({ymax:Math.max(...ks.map(w))*1.05});P2.clear();P2.line(ks,ks.map(w),C.ink,2.5);P2.dot(k0,w(k0),C.orange,6);P2.line([0,k0],[0,w(k0)],C.muted,1.2,[4,3]);
 const slope=vg,t0=w(k0)-vg*k0;P2.line([0,5],[t0,t0+vg*5],C.red,1.5,[5,3]);P2.line([0,5],[0,vp*5],C.violet,1.2,[2,3]);
 const w2=(w(k0+0.02)-2*w(k0)+w(k0-0.02))/(0.02*0.02);
 out.textContent=`ω(k₀) = ${M.fmt(w(k0),4)}   phase velocity v_p = ω/k = ${M.fmt(vp,4)} (violet slope)   group velocity v_g = dω/dk = ${M.fmt(vg,4)} (red slope = tangent)   ratio v_g/v_p = ${M.fmt(vg/vp,4)}\nω″ = ${M.fmt(w2,4)} → ${Math.abs(w2)<1e-3?'no spreading':'packet spreads (width grows ∝ |ω″| t σ_k)'}   t = ${M.fmt(t,3)}`}
loop((dt)=>{t+=dt*2;if(t>40)t=0;draw()});draw();
ui.note('Deep water v_g = ½v_p; capillary v_g = (3/2)v_p; waveguide v_p v_g = c² (ED07); Schrödinger v_g = 2v_p (QM01). The packet is a numerical superposition of 121 plane waves.');
