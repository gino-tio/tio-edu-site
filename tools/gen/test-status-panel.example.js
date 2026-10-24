const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const [u,l,f] of [['/works/','zh','h'],['/works/geo/','zh','g'],['/works/en/geo/','en','ge']]){
const c=await b.newContext({viewport:{width:390,height:800}});await c.addInitScript(x=>localStorage.setItem('tyLang',x),l);
const p=await c.newPage();const e=[];p.on('pageerror',x=>e.push(x.message));await p.route(/fonts\./,r=>r.abort());
await p.goto('http://localhost:8765'+u);await p.waitForTimeout(400);
const t=await p.$eval('.stat',x=>x.innerText);const ov=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
console.log(f,e,'overflow',ov,t.replace(/\n/g,' | ').slice(0,160));
const el=await p.$('.stat');await el.screenshot({path:'/tmp/pt/stat-'+f+'.png'});await c.close();}
await b.close()})();
