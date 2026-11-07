//META {"title": "A free Gaussian wave packet: spreading and the uncertainty principle", "desc": "A packet ψ(x,0) ∝ exp(−x²/4σ₀² + ik₀x) evolves freely (ħ = m = 1). The real part (oscillating carrier), the probability density |ψ|² and the momentum-space density |φ(k)|² are shown. The centre moves at the group velocity k₀, the width grows as σ(t) = σ₀√(1 + (t/2σ₀²)²), while the momentum spread 1/(2σ₀) never changes: Δx·Δp ≥ ½.", "vault": "QM", "chapters": ["QM01 From Waves to Probabilities", "QM02 The Schrodinger Equation and Stationary States", "Fourier and Laplace Transforms"], "tryit": "Make σ₀ small: it spreads fast (large momentum spread). Make σ₀ large: nearly rigid. Change k₀ and see the packet move without changing shape."}
ui.gridOf(1);const P1=ui.canvas(300,{xmin:-20,xmax:40,ymin:-0.8,ymax:0.8,xlabel:'x',ylabel:'ψ, |ψ|²'});const P2=ui.canvas(180,{xmin:-3,xmax:3,ymin:0,ymax:1.4,xlabel:'k',ylabel:'|φ(k)|²'});
const ss=ui.slider('initial width σ₀',0.6,4,0.05,1.5,draw),sk=ui.slider('mean wave number k₀',-2,3,0.05,1.5,draw),st=ui.slider('time t',0,40,0.1,0,()=>{running=false;draw()});
const out=ui.readout();let running=true,tt=0;ui.button('restart',()=>{tt=0;st.value=0;running=true});
function psi(x,t,s0,k0){const a=1+t/(2*s0*s0)*0; // complex 1 + i t/(2 s0^2)
 const re=1,im=t/(2*s0*s0);const den=re*re+im*im; // 1/(1+iτ) = (1 - iτ)/(1+τ²)
 const pre=Math.pow(2*Math.PI*s0*s0,-0.25),mod=Math.pow(den,-0.25),argp=-0.5*Math.atan2(im,re);
 const u=(x-k0*t);const e1=-u*u/(4*s0*s0)*(re/den),e2=+u*u/(4*s0*s0)*(im/den); // exp(-u²/(4σ²(1+iτ))) = exp(-u²(1-iτ)/(4σ²(1+τ²)))
 const ph=k0*x-k0*k0*t/2+e2+argp;const amp=pre*mod*Math.exp(e1);return[amp*Math.cos(ph),amp*Math.sin(ph)]}
function draw(){const s0=ss.value,k0=sk.value,t=running?tt:st.value;const xc=k0*t;P1.set({xmin:Math.min(-20,xc-25),xmax:Math.max(40,xc+25)});P1.set({ymax:Math.max(0.5,0.9*Math.pow(2*Math.PI*s0*s0,-0.25))*1.1,ymin:-Math.max(0.5,0.9*Math.pow(2*Math.PI*s0*s0,-0.25))*1.1});P1.clear();
 const xs=M.linspace(P1.o.xmin,P1.o.xmax,900),ps=xs.map(x=>psi(x,t,s0,k0));P1.line(xs,ps.map(p=>p[0]),C.blue,1.6);P1.line(xs,ps.map(p=>p[0]*p[0]+p[1]*p[1]),C.orange,3);
 const sg=s0*Math.sqrt(1+(t/(2*s0*s0))**2);P1.vline(xc,C.muted);P1.legend([['Re ψ',C.blue],['|ψ|²',C.orange]],P1.o.ml+8,P1.o.mt+14);P1.line([xc-sg,xc+sg],[0.05,0.05],C.red,4);
 const skk=1/(2*s0);P2.set({xmin:Math.min(-3,k0-5*skk),xmax:Math.max(3,k0+5*skk),ymax:1.25/(Math.sqrt(2*Math.PI)*skk)});P2.clear();const ks=M.linspace(P2.o.xmin,P2.o.xmax,300);P2.line(ks,ks.map(k=>Math.exp(-((k-k0)**2)/(2*skk*skk))/(Math.sqrt(2*Math.PI)*skk)),C.violet,3);P2.vline(k0,C.muted);
 out.textContent=`t = ${M.fmt(t,3)}   σ(t) = σ₀√(1+(t/2σ₀²)²) = ${M.fmt(sg,4)}   centre x = k₀t = ${M.fmt(xc,3)}   Δp = 1/(2σ₀) = ${M.fmt(1/(2*s0),4)} (constant)   Δx·Δp = ${M.fmt(sg/(2*s0),4)} ≥ 0.5   (minimum at t = 0)`}
loop((dt)=>{if(running){tt+=dt*3;if(tt>40)tt=0;st.value=tt}draw()});draw();
ui.note('Units ħ = m = 1. The packet is the exact solution: ψ(x,t) = (2πσ₀²)^{-1/4}(1+it/2σ₀²)^{-1/2} exp[−(x−k₀t)²/(4σ₀²(1+it/2σ₀²)) + i(k₀x − k₀²t/2)].');
