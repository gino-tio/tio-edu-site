const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const [url,lang] of [['/works/geo-food/','zh'],['/works/en/geo-food/','en']]){
const c=await b.newContext();await c.addInitScript(l=>localStorage.setItem('tyLang',l),lang);
const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route(/fonts\.(googleapis|gstatic)/,r=>r.abort());
await p.goto('http://localhost:8765'+url);await p.waitForTimeout(500);
const items=await p.$$eval('#p-ref .item,#p-ref details',e=>e.length);
const txt=await p.$eval('#p-ref',e=>e.innerText);
console.log(lang,'items',items,'has Table4',/Table 4/.test(txt),'15%',/15%/.test(txt),'self-suff',/self-sufficiency/i.test(txt),'zhInEN',lang=='en'?(txt.match(/[一-鿿]+/g)||[]).slice(0,8):'-');
await p.click('text=/配對遊戲|Match/').catch(()=>{});
await p.click('text=/選擇題|Quiz/').catch(()=>{});
console.log('errs',errs);await c.close();}
await b.close();})();
