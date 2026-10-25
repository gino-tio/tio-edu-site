// Smoke test for the 3D pages (Farm Island, Shopping Street): node tools/gen/test-3d.example.js
// needs a server on :8765 (python3 -m http.server 8765) and playwright (NODE_PATH=$(npm root -g))
const {chromium}=require('playwright');
const PAGES=[['geo-farm-3d','farm3dBest'],['eng-shop-3d','shop3dBest']];
(async()=>{const b=await chromium.launch({args:['--use-gl=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});let bad=0;
for(const [page,bestKey] of PAGES){
 for(const lang of ['zh','en']){
  const url='/works/'+(lang==='en'?'en/':'')+page+'/';
  const c=await b.newContext({viewport:{width:390,height:800}});await c.addInitScript(l=>{localStorage.setItem('tyLang',l);localStorage.removeItem('farmMode')},lang);
  const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
  await p.route(/fonts\.(googleapis|gstatic)/,r=>r.abort());
  await p.goto('http://localhost:8765'+url);await p.waitForTimeout(1200);
  const st=await p.evaluate(()=>window.__farm.state());
  const ov=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1);
  const nstops=await p.$$eval('.dot',e=>e.length);
  for(let i=1;i<nstops;i++){await p.click('#next');}
  const stop=await p.evaluate(()=>window.__farm.state().cur);
  await p.click('#chal');await p.click('[data-t=off]');await p.click('#cgo');await p.waitForTimeout(1500);
  let right=0,missing=[];
  for(let q=0;q<8;q++){
    const want=await p.evaluate(()=>window.__farm.q());const qtxt=await p.textContent('#cq');
    const pos=await p.evaluate(t=>window.__farm.where(t),want);
    if(!pos){missing.push(want)}else{await p.mouse.click(pos[0],pos[1]);await p.waitForTimeout(80);if(/✔|Correct/.test(await p.textContent('#cfb')))right++;else missing.push(want+'!')}
    await p.waitForFunction(t=>document.getElementById('cq').textContent!==t||!document.getElementById('qz').hidden,qtxt,{timeout:5000}).catch(()=>{});
  }
  const end=await p.isVisible('#qcard');
  await p.click('#cex');await p.click('#mode');await p.waitForTimeout(300);
  const tiles=await p.$$eval('.tile',e=>e.length);
  await p.click('.tile >> nth=0');const stop2=await p.evaluate(()=>window.__farm.state().cur);
  const zhInEN=lang==='en'?((await p.evaluate(()=>document.body.innerText)).replace(/中\s*$/gm,'').match(/[一-鿿]+/g)||[]).slice(0,5):[];
  console.log(page,lang,'gl',st.hasGL,'stops',nstops,'last',stop,'overflow',ov,'3D challenge',right+'/8','missing',missing,'end card',end,'tiles',tiles,'tile->stop',stop2,'zhInEN',zhInEN,'errs',errs);
  if(errs.length||ov||!st.hasGL||right<8||tiles<20||zhInEN.length||stop!==nstops-1)bad++;
  await c.close();
 }
 // 2D mode, timer on, night theme
 const c=await b.newContext({viewport:{width:390,height:800}});await c.addInitScript(()=>{localStorage.setItem('farmMode','2d');localStorage.setItem('tyTimer','on');localStorage.setItem('tyTheme','night')});
 const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.route(/fonts\.(googleapis|gstatic)/,r=>r.abort());
 await p.goto('http://localhost:8765/works/'+page+'/');await p.waitForTimeout(800);
 await p.click('#chal');await p.click('#cgo');
 let right=0;
 for(let q=0;q<8;q++){
   const want=await p.evaluate(()=>window.__farm.q());const qtxt=await p.textContent('#cq');
   await p.evaluate(t=>window.__farm.tile(t),want);await p.waitForTimeout(60);
   if(/✔/.test(await p.textContent('#cfb')))right++;
   await p.waitForFunction(t=>document.getElementById('cq').textContent!==t||!document.getElementById('qz').hidden,qtxt,{timeout:5000}).catch(()=>{});
 }
 const best=await p.evaluate(k=>localStorage.getItem(k),bestKey);
 console.log(page,'2D challenge',right+'/8','best saved',best,'errs',errs);
 if(right<8||!best||errs.length)bad++;
 await c.close();
}
await b.close();process.exit(bad?1:0)})();
