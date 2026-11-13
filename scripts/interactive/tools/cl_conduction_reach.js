//META {"title": "How deep does a swing reach? Conduction in soil versus stirring in the ocean", "desc": "A periodic surface swing of angular frequency ω in a medium of diffusivity κ gives T′(z,t) = A e^(−z/d) cos(ωt − z/d) with d = √(2κ/ω): it fades with depth and lags. Soil (κ ≈ 5×10⁻⁷ m² s⁻¹) reaches ≈ 12 cm in a day and ≈ 2.2 m in a year; still water (1.4×10⁻⁷) is no better; the same formula with an eddy diffusivity K = 10⁻⁵–10⁻⁴ m² s⁻¹ gives the reach below the mixed layer: 10–32 m in a year, 100–317 m in a century. The stirred mixed layer (tens of metres) is the real source of the ocean's inertia.", "vault": "CL", "chapters": ["CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia"], "tryit": "Choose soil and the period 365 days: d = 2.24 m. Choose a day: 11.7 cm. Switch to 'eddy K = 1e-4' and 100 years: 317 m. Notice d scales as the square root of the period: 100× the period gives only 10× the depth."}
ui.gridOf(2);
const P1=ui.canvas(400,{xmin:-1,xmax:1,ymin:3,ymax:0,xlabel:"temperature swing T′ / A",ylabel:'depth (m)',title:'profiles at eight phases of the cycle'});
const P2=ui.canvas(400,{xmin:-2.5,xmax:3,ymin:-2,ymax:3,xlabel:'log₁₀ period (yr)',ylabel:'log₁₀ reach d (m)',title:'reach against period'});
const med=ui.select('medium',[['5e-7','soil  κ = 5×10⁻⁷ m² s⁻¹'],['3e-7','dry soil  κ = 3×10⁻⁷'],['1e-6','wet soil  κ = 10⁻⁶'],['1.4e-7','still water  κ = 1.4×10⁻⁷'],['1e-5','below the mixed layer  K = 10⁻⁵'],['1e-4','below the mixed layer  K = 10⁻⁴']],draw,'5e-7');
const sp=ui.slider('log₁₀ period (days)',0,5.6,0.05,2.56,draw,v=>M.fmt(Math.pow(10,v),3)+' d');const out=ui.readout();
const DAY=86400,YR=3.156e7;
function draw(){const kap=parseFloat(med.value),P=Math.pow(10,sp.value)*DAY,om=2*Math.PI/P,d=Math.sqrt(2*kap/om);
 P1.set({ymax:0,ymin:3*d,xmin:-1,xmax:1});P1.clear();const zs=M.linspace(0,3*d,200);
 P1.line(zs.map(z=>Math.exp(-z/d)),zs,C.muted,1.5,[5,3]);P1.line(zs.map(z=>-Math.exp(-z/d)),zs,C.muted,1.5,[5,3]);
 for(let k=0;k<8;k++){const ph=k*Math.PI/4;P1.line(zs.map(z=>Math.exp(-z/d)*Math.cos(ph-z/d)),zs,k===0?C.red:C.blue,k===0?3:1.5)}
 P1.hline(d,C.orange);P1.text('d',0.85,d*0.92,C.orange);
 const lp=M.linspace(-2.5,3,100);P2.clear();for(const [kk,cc] of [[3e-7,C.orange],[5e-7,C.orange],[1.4e-7,C.aqua],[1e-5,C.blue],[1e-4,C.blue]])P2.line(lp,lp.map(l=>Math.log10(Math.sqrt(2*kk/(2*Math.PI/(Math.pow(10,l)*YR))))),cc,kk===kap?4:1.5);
 P2.dot(Math.log10(P/YR),Math.log10(d),C.red,7);P2.hline(Math.log10(50),C.muted);P2.text('50 m',-2.4,1.78,C.muted);
 const slab=2e6*d/Math.SQRT2/4.2e6;
 out.textContent=`period ${M.fmt(P/DAY,3)} d: d = √(2κ/ω) = ${d<1?M.fmt(d*100,3)+' cm':M.fmt(d,3)+' m'};  the swing falls by a factor e and lags by 1 rad (${M.fmt(P/2/Math.PI/DAY,3)} d) for every ${d<1?M.fmt(d*100,3)+' cm':M.fmt(d,3)+' m'} of depth;  as a slab (soil ρc = 2×10⁶): ${slab<1?M.fmt(slab*100,3)+' cm':M.fmt(slab,3)+' m'} of water.`}
draw();
ui.note('CL23 §3–4. The thick curve is the selected medium. Verified against scripts/joy_inertia_numbers.py (9/12/17 cm and 1.7/2.2/3.2 m; 10/32, 32/100, 100/317 m).');
