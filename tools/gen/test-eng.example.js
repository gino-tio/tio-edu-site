// Smoke test for the English pages: node tools/gen/test-eng.example.js (server on :8765, needs playwright)
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();let bad=0;
for(const lang of ['zh','en']){for(const f of ['eng','eng-adj','eng-cond','eng-tense']){
 const url=(lang=='en'?'/works/en/':'/works/')+f+'/';
 const c=await b.newContext({viewport:{width:390,height:800}});await c.addInitScript(l=>localStorage.setItem('tyLang',l),lang);
 const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.route(/fonts\.(googleapis|gstatic)/,r=>r.abort());
 await p.goto('http://localhost:8765'+url);await p.waitForTimeout(400);
 const txt=await p.evaluate(()=>document.body.innerText);
 const zhInEN=lang=='en'?(txt.replace(/中\s*$/gm,'').match(/[一-鿿]+/g)||[]):[];
 const ov=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1);
 let tabs=0;
 for(const t of await p.$$('#tabs button')){await t.click();tabs++;}
 const note=f=='eng'?'':await p.$$eval('#p-ref .item',e=>e.length);
 if(errs.length||zhInEN.length||ov)bad++;
 console.log(lang,f,'errs',errs.length,'tabs',tabs,'notes',note,'zhInEN',zhInEN.slice(0,3),'overflow',ov);
 await c.close();}}
await b.close();process.exit(bad?1:0)})();
