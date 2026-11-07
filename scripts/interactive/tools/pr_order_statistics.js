//META {"title":"Order statistics: the density of the k-th smallest of n","desc":"Draw n independent values from a distribution and sort them: Y₍₁₎ ≤ … ≤ Y₍ₙ₎. The k-th smallest has density n!/((k−1)!(n−k)!) · F(y)^(k−1) · (1 − F(y))^(n−k) · f(y). Pick a distribution, n and k: the thin curves are the exact densities of all n order statistics, the thick curve is your k, and the histogram comes from 4000 simulated samples. On the right, the mean spacing between consecutive order statistics: for the exponential distribution the gap before the k-th point is Expo((n−k+1)λ) (the Rényi representation, which contains the HW5 result Y₍₂₎ − Y₍₁₎ ~ Expo(λ)).","vault":"PR","chapters":["PR08 Order Statistics and the Multinomial Distribution"],"tryit":"Uniform, n = 5: the k-th order statistic is Beta(k, n − k + 1) with mean k/6 (k = 2: 0.3333). Exponential with n = 2: the minimum has mean 1/2 (rate 2) and the second gap has mean 1: the gaps are 1/(n−k+1) = 1/2, 1. Increase n for the exponential: the first gap shrinks like 1/n while the last stays 1, so the maximum grows like the harmonic number H_n ≈ ln n."}
ui.gridOf(2);const P1=ui.canvas(360,{xmin:0,xmax:1,ymin:0,ymax:5,xlabel:'y',ylabel:'density',title:'density of Y₍ₖ₎ (thick) and of all order statistics (thin)'});const P2=ui.canvas(360,{xmin:0.5,xmax:20.5,ymin:0,ymax:1.2,xlabel:'k (position in the sorted sample)',ylabel:'mean spacing E[Y₍ₖ₎ − Y₍ₖ₋₁₎]',title:'mean gap before the k-th point'});
const dist=ui.select('distribution',[['u','Uniform(0, 1)'],['e','Exponential(1)'],['g','Normal(0, 1)']],()=>{rescale();draw(true)},'e');
const sn=ui.slider('n (sample size)',2,20,1,5,()=>{sk.el.max=sn.value;if(sk.value>sn.value)sk.value=sn.value;draw(true)}),sk=ui.slider('k (which order statistic)',1,20,1,2,()=>draw(false));sk.el.max=5;
ui.button('resample',()=>draw(true));
const out=ui.readout();
const phi=x=>Math.exp(-x*x/2)/Math.sqrt(2*Math.PI),Phi=x=>0.5*(1+M.erf(x/Math.SQRT2));
const D={u:{f:x=>x>=0&&x<=1?1:0,F:x=>x<0?0:x>1?1:x,lo:0,hi:1,ymax:6},e:{f:x=>x>=0?Math.exp(-x):0,F:x=>x>=0?1-Math.exp(-x):0,lo:0,hi:7,ymax:3},g:{f:phi,F:Phi,lo:-4,hi:4,ymax:2}};
const lg=n=>{let s=0;for(let i=2;i<=n;i++)s+=Math.log(i);return s};
function opdf(d,n,k,y){const F=d.F(y),f=d.f(y);if(f===0)return 0;return Math.exp(lg(n)-lg(k-1)-lg(n-k))*Math.pow(F,k-1)*Math.pow(1-F,n-k)*f}
function sampleD(d,key,r){const u=r();if(key==='u')return u;if(key==='e')return -Math.log(1-u);return M.gauss(r)}
let seedN=1,cache=null;
function rescale(){const d=D[dist.value];P1.set({xmin:d.lo,xmax:d.hi,ymin:0,ymax:d.ymax})}
function draw(resim){const key=dist.value,d=D[key],n=sn.value,k=Math.min(sk.value,n);sk.el.max=n;
 if(resim||!cache||cache.key!==key||cache.n!==n){const r=M.rng(1000+(seedN++)),S=4000,acc=[];const gapSum=new Array(n).fill(0);for(let s=0;s<S;s++){const a=[];for(let i=0;i<n;i++)a.push(sampleD(d,key,r));a.sort((x,y)=>x-y);acc.push(a);gapSum[0]+=a[0];for(let i=1;i<n;i++)gapSum[i]+=a[i]-a[i-1]}cache={key,n,acc,gap:gapSum.map(v=>v/S)}}
 P1.set({xmin:d.lo,xmax:d.hi,ymin:0,ymax:d.ymax});P1.clear();
 const xs=M.linspace(d.lo,d.hi,500);for(let j=1;j<=n;j++){if(j===k)continue;P1.line(xs,xs.map(y=>opdf(d,n,j,y)),'rgba(120,120,120,0.45)',1.2)}
 // histogram of simulated Y(k)
 const nb=40,h=(d.hi-d.lo)/nb,cnt=new Array(nb).fill(0);for(const a of cache.acc){const b=Math.floor((a[k-1]-d.lo)/h);if(b>=0&&b<nb)cnt[b]++}
 const hx=[],hy=[];for(let b=0;b<nb;b++){const dens=cnt[b]/(cache.acc.length*h);hx.push(d.lo+b*h,d.lo+(b+1)*h);hy.push(dens,dens)}P1.line(hx,hy,C.orange,1.8);
 P1.line(xs,xs.map(y=>opdf(d,n,k,y)),C.blue,3.4);P1.legend([['exact density of Y₍'+k+'₎',C.blue],['simulation (4000 samples)',C.orange]],P1.o.ml+8,P1.o.mt+14);
 // moments
 let m1=0,m2=0;const dx=(d.hi-d.lo)/4000;for(let i=0;i<=4000;i++){const y=d.lo+i*dx,w=opdf(d,n,k,y)*dx;m1+=y*w;m2+=y*y*w}const mean=m1,vr=m2-m1*m1;
 let sm=0,sv=0;for(const a of cache.acc)sm+=a[k-1];sm/=cache.acc.length;for(const a of cache.acc)sv+=(a[k-1]-sm)**2;sv/=cache.acc.length;
 // right: mean gaps
 P2.set({xmin:0.5,xmax:n+0.5,ymin:0,ymax:Math.max(0.3,...cache.gap)*1.25});P2.clear();
 for(let j=1;j<=n;j++){const g=cache.gap[j-1];P2.poly([[j-0.35,0],[j-0.35,g],[j+0.35,g],[j+0.35,0]],j===k?'rgba(235,104,52,0.55)':'rgba(235,104,52,0.25)',C.orange,1.2)}
 const th=[];if(key==='e'){for(let j=1;j<=n;j++)th.push(1/(n-j+1));P2.dots(M.range(n).map(i=>i+1),th,C.blue,5)}else if(key==='u'){for(let j=1;j<=n;j++)th.push(1/(n+1));P2.dots(M.range(n).map(i=>i+1),th,C.blue,5)}
 if(th.length)P2.legend([['simulated mean gap',C.orange],['exact: '+(key==='e'?'1/(n−k+1) (Rényi)':'1/(n+1)'),C.blue]],P2.o.ml+8,P2.o.mt+14);else P2.legend([['simulated mean gap (no closed form)',C.orange]],P2.o.ml+8,P2.o.mt+14);
 const nm={u:'Uniform(0,1)',e:'Exponential(1)',g:'Normal(0,1)'}[key];
 out.textContent=`${nm}, n = ${n}, k = ${k}:   E[Y₍${k}₎] = ${M.fmt(mean,4)} (simulation ${M.fmt(sm,4)}),   Var = ${M.fmt(vr,4)} (simulation ${M.fmt(sv,4)})\n`+(key==='u'?`exact: Beta(${k}, ${n-k+1}) with mean k/(n+1) = ${M.fmt(k/(n+1),4)}`:key==='e'?`exact: E[Y₍${k}₎] = Σ_{j=1}^{${k}} 1/(n−j+1) = ${M.fmt(M.sum(M.range(k).map(j=>1/(n-j))),4)},  Var = Σ 1/(n−j+1)² = ${M.fmt(M.sum(M.range(k).map(j=>1/((n-j)*(n-j)))),4)}`:'no elementary closed form: the density formula is integrated numerically')}
rescale();draw(true);ui.note('PR08 §2–§3. The formula is the multinomial argument: Y₍ₖ₎ ∈ dy needs k−1 points below y, one in dy, n−k above; there are n!/((k−1)!1!(n−k)!) ways. Checked against the script pr08_numbers.py: uniform, n = 5: E[Y₍ₖ₎] = k/6; exponential: gaps 1/5, 1/4, 1/3, 1/2, 1 and E[max] = H₅ = 2.2833.');
