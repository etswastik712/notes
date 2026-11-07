//META {"title":"Blackbody spectra: why sunlight is shortwave and Earth glows in the infrared","desc":"Planck's law B_λ(T) on a log wavelength axis for any temperature, with the visible band shaded. The Sun (≈5772 K) peaks in the visible near 0.5 µm; the Earth (≈288 K) peaks near 10 µm. Wien's displacement law λ_max T = 2898 µm K and the Stefan–Boltzmann law F = σT⁴ are read off live. The overlap of the two curves is tiny, which is what lets us treat shortwave and longwave separately.","vault":"CL","chapters":["CL03 Radiation and Planetary Energy Balance","CL07 Optical Properties of the Atmosphere"],"tryit":"Drag T from 288 K to 5772 K and watch the peak slide through the visible; compare the areas (T⁴)."}
ui.gridOf(1);const P=ui.canvas(340,{xmin:-1,xmax:2.2,ymin:0,ymax:1.1,xlabel:'log₁₀ [ λ / µm ]',ylabel:'B_λ, each curve normalised to its own peak'});
const sT=ui.slider('temperature of body 2 (K)',100,8000,1,288,draw);const out=ui.readout();
const h=6.62607e-34,c=2.99792e8,k=1.380649e-23,sig=5.670374e-8;
function B(l,T){const L=l*1e-6;return 2*h*c*c/Math.pow(L,5)/(Math.exp(h*c/(L*k*T))-1)}
function draw(){const T2=sT.value,Ts=5772;P.clear();const xs=M.linspace(-1,2.2,500),ls=xs.map(x=>Math.pow(10,x));
 P.poly([[Math.log10(0.4),0],[Math.log10(0.4),1.1],[Math.log10(0.7),1.1],[Math.log10(0.7),0]],'rgba(240,200,60,0.20)',null);
 for(const [T,col,nm] of [[Ts,C.gold,'Sun 5772 K'],[T2,C.red,'body 2: '+M.fmt(T2,4)+' K']]){const y=ls.map(l=>B(l,T)),m=Math.max(...y);P.line(xs,y.map(v=>v/m),col,3);const lm=2898/T;P.dot(Math.log10(lm),1,col,5);P.text(nm+'  (peak '+M.fmt(lm,3)+' µm)',Math.log10(lm)+0.05,0.97-(col===C.gold?0:0.07),col)}
 // tick labels in µm
 [0.1,1,10,100].forEach(v=>{P.vline(Math.log10(v),C.grid);P.text(v+' µm',Math.log10(v)+0.03,0.04,C.muted,'left','11px system-ui')});
 // overlap fraction of Earth emission below 4 µm
 let tot=0,sw=0;const lg=M.linspace(-1,3,2000);for(let i=0;i<lg.length-1;i++){const l=Math.pow(10,lg[i]),dl=Math.pow(10,lg[i+1])-l,v=B(l,T2)*dl;tot+=v;if(l<4)sw+=v}
 let tots=0,sws=0;for(let i=0;i<lg.length-1;i++){const l=Math.pow(10,lg[i]),dl=Math.pow(10,lg[i+1])-l,v=B(l,Ts)*dl;tots+=v;if(l>4)sws+=v}
 out.textContent=`Wien: λ_max = 2898/T = ${M.fmt(2898/T2,4)} µm for ${M.fmt(T2,4)} K (Sun: ${M.fmt(2898/Ts,4)} µm)   Stefan–Boltzmann: F = σT⁴ = ${M.fmt(sig*Math.pow(T2,4),5)} W/m² (Sun ${M.fmt(sig*Math.pow(Ts,4)/1e6,4)} MW/m²)\nfraction of body-2 emission at λ < 4 µm = ${M.fmt(sw/tot*100,3)} %   fraction of solar emission at λ > 4 µm = ${M.fmt(sws/tots*100,3)} %  (the 4 µm line separates 'shortwave' from 'longwave')`}
draw();ui.note('B_λ(T) = (2hc²/λ⁵)/(exp(hc/λkT) − 1). The flux F = σT⁴ is π times the integral of B_λ over λ. At T = 255 K the emission temperature gives F = 239 W m⁻² (CL03).');
