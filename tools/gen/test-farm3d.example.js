// Smoke test for the 3D Farm Island: node tools/gen/test-farm3d.example.js (server on :8765, needs playwright)
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({args:['--use-gl=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});let bad=0;
for(const [url,lang] of [['/works/geo-farm-3d/','zh'],['/works/en/geo-farm-3d/','en']]){
 const c=await b.newContext({viewport:{width:390,height:800}});await c.addInitScript(l=>{localStorage.setItem('tyLang',l);localStorage.removeItem('farmMode')},lang);
 const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.route(/fonts\.(googleapis|gstatic)/,r=>r.abort());
 await p.goto('http://localhost:8765'+url);await p.waitForTimeout(1200);
 const st=await p.evaluate(()=>window.__farm.state());
 const ov=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1);
 // stops
 for(let i=1;i<=8;i++){await p.click('#next');}
 const stop=await p.evaluate(()=>window.__farm.state().cur);
 // challenge, timer off, tap by 3D picking
 await p.click('#chal');await p.click('[data-t=off]');await p.click('#cgo');await p.waitForTimeout(1500);
 let right=0,asked=0,missing=[];
 for(let q=0;q<8;q++){
   const want=await p.evaluate(()=>window.__farm.q());
   const qtxt=await p.textContent('#cq');
   const pos=await p.evaluate(t=>window.__farm.where(t),want);
   if(!pos){missing.push(want)}else{
     await p.mouse.click(pos[0],pos[1]);await p.waitForTimeout(80);
     const fb=await p.textContent('#cfb');if(/✔|Correct/.test(fb))right++;else missing.push(want+'!'+fb);
   }
   asked++;
   await p.waitForFunction(t=>document.getElementById('cq').textContent!==t||!document.getElementById('qz').hidden,qtxt,{timeout:5000}).catch(()=>{});
 }
 console.log(lang,'missing',missing);
 const end=await p.isVisible('#qcard');
 // 2D mode
 await p.evaluate(()=>{});
 const hasEnd=await p.textContent('#qcard');
 await p.click('#cex');await p.click('#mode');await p.waitForTimeout(300);
 const tiles=await p.$$eval('.tile',e=>e.length);
 await p.click('.tile >> nth=0');
 const stop2=await p.evaluate(()=>window.__farm.state().cur);
 const zhInEN=lang==='en'?((await p.evaluate(()=>document.body.innerText)).replace(/中\s*$/gm,'').match(/[一-鿿]+/g)||[]).slice(0,5):[];
 console.log(lang,'gl',st.hasGL,'cur after 8 next',stop,'overflow',ov,'challenge right',right+'/'+asked,'end card',end,'tiles',tiles,'2d tile->stop',stop2,'zhInEN',zhInEN,'errs',errs);
 if(errs.length||ov||!st.hasGL||tiles<20||zhInEN.length)bad++;
 await c.close();}

// 2D mode + timer on + night theme
{
 const c=await b.newContext({viewport:{width:390,height:800}});await c.addInitScript(()=>{localStorage.setItem('farmMode','2d');localStorage.setItem('tyTimer','on');localStorage.setItem('tyTheme','night')});
 const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.route(/fonts\.(googleapis|gstatic)/,r=>r.abort());
 await p.goto('http://localhost:8765/works/geo-farm-3d/');await p.waitForTimeout(800);
 await p.click('#chal');await p.click('#cgo');
 let right=0;
 for(let q=0;q<8;q++){
   const want=await p.evaluate(()=>window.__farm.q());
   const label={phys:'sunlight',cult:'machines',market:'market',useful:'crops',useless:'animal waste',farmA:'Farm A',farmB:'Farm B',proc:'harvesting'}[want];
   const qtxt=await p.textContent('#cq');
   await p.click('.tile:has-text("'+label+'")');await p.waitForTimeout(60);
   if(/✔/.test(await p.textContent('#cfb')))right++;
   await p.waitForFunction(t=>document.getElementById('cq').textContent!==t||!document.getElementById('qz').hidden,qtxt,{timeout:5000}).catch(()=>{});
 }
 const best=await p.evaluate(()=>localStorage.getItem('farm3dBest'));
 console.log('2D challenge right',right+'/8','best saved',best,'errs',errs);
 if(right<8||!best||errs.length)bad++;
 await c.close();
}
await b.close();process.exit(bad?1:0)})();
