//META {"title":"Dispersion and absorption: the Lorentz oscillator and the plasma","desc":"Electrons modelled as damped springs give ε(ω) = 1 + ω_P²/(ω₀² − ω² − iγω). Top: refractive index n(ω) and absorption α(ω) near one resonance. Below the resonance n rises with frequency (normal dispersion, blue bends more than red); inside the absorption line n falls (anomalous dispersion). Bottom: a free-electron plasma ω² = ω_p² + c²k², with phase velocity above c and group velocity below c.","vault":"ED","chapters":["ED06 Waves in Matter, Reflection and Dispersion"],"tryit":"Narrow the damping γ and watch the anomalous region shrink onto the absorption peak. Move the probe frequency in the plasma panel below ω_p: k becomes imaginary and the wave cannot propagate."}
ui.gridOf(1);const P1=ui.canvas(270,{xmin:0.8,xmax:1.2,ymin:-1,ymax:1,xlabel:'ω / ω₀',ylabel:'n − 1',title:'Lorentz oscillator: n(ω) and absorption'});
const P2=ui.canvas(260,{xmin:0,xmax:3,ymin:0,ymax:3.5,xlabel:'ck / ω_p',ylabel:'ω / ω_p',title:'plasma dispersion relation'});
const sg=ui.slider('damping γ/ω₀',0.005,0.1,0.001,0.03,draw),sp=ui.slider('strength ω_P²/ω₀² (×0.01)',0.2,10,0.1,2,draw),sw=ui.slider('probe frequency ω / ω_p (plasma)',0.2,3,0.01,1.6,draw);
const out=ui.readout();
function eps(w,g,s){const d=(1-w*w),im=g*w,den=d*d+im*im;return[1+s*d/den,s*im/den]}
function draw(){const g=sg.value,s=sp.value*0.01;P1.clear();const ws=M.linspace(0.8,1.2,500),E=ws.map(w=>eps(w,g,s));
 const nk=E.map(([a,b])=>{const m=Math.hypot(a,b);return[Math.sqrt((m+a)/2),Math.sqrt((m-a)/2)]});
 const nn=nk.map(v=>v[0]-1),mx=Math.max(...nn.map(Math.abs));P1.set({ymin:-mx*1.15,ymax:mx*1.15});P1.clear();P1.hline(0,C.grid);P1.line(ws,nn,C.blue,3);
 const al=nk.map((v,i)=>2*ws[i]*v[1]);const amx=Math.max(...al)||1;P1.line(ws,al.map(a=>a/amx*mx),C.orange,2,[5,3]);P1.legend([['n − 1',C.blue],['α(ω)  (scaled)',C.orange,[5,3]]],P1.o.ml+8,P1.o.mt+14);
 P1.vline(1,C.muted);
 // plasma
 P2.clear();const ks=M.linspace(0,3,200);P2.line(ks,ks.map(k=>Math.sqrt(1+k*k)),C.blue,3);P2.line(ks,ks,C.muted,1.5,[5,3]);P2.hline(1,C.red);P2.text('cutoff ω_p',2.1,1.12,C.red);
 const w=sw.value;const prop=w>1;const k=prop?Math.sqrt(w*w-1):0;
 if(prop){P2.dot(k,w,C.orange,6);P2.line([0,k],[w,w],C.orange,1,[3,3])}else{P2.line([0,3],[w,w],C.orange,2,[4,3]);P2.text('evanescent: k imaginary',1.2,w+0.18,C.orange)}
 const kappa=prop?0:Math.sqrt(1-w*w);
 out.textContent=`Lorentz: peak absorption α_max ≈ ω_P²/(cγ) ∝ ${M.fmt(s/g,4)} (in units ω₀/c); anomalous dispersion width ≈ γ = ${M.fmt(g,3)} ω₀;  static index n(0) = √(1+ω_P²/ω₀²) = ${M.fmt(Math.sqrt(1+s),5)}\nplasma at ω = ${M.fmt(w,3)}ω_p:  ${prop?`k = √(ω²−ω_p²)/c = ${M.fmt(k,4)} ω_p/c   v_p = ω/k = ${M.fmt(w/k,4)} c  (>c)   v_g = c²k/ω = ${M.fmt(k/w,4)} c  (<c)   v_p·v_g = c² ✓`:`below cutoff: field decays as e^{−κz}, κ = ${M.fmt(kappa,4)} ω_p/c, no propagation`}`}
draw();ui.note('Numbers from ED06: N = 2.5×10²⁵ m⁻³ with ω₀ = 1.5×10¹⁶ s⁻¹ gives ω_P²/ω₀² = 3.5×10⁻⁴ (n−1 ≈ 1.9×10⁻⁴ in the visible); ionosphere N = 10¹² m⁻³ gives f_p = 8.98 MHz.');
