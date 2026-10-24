var TYEN=document.documentElement.lang==='en';function L(z,e){return TYEN?e:z}
window.TY=(function(){
  function shuffle(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),x=a[i];a[i]=a[j];a[j]=x}return a}
  function lsGet(k){try{return +localStorage.getItem(k)||0}catch(e){return 0}}
  function lsSet(k,v){try{localStorage.setItem(k,String(v))}catch(e){}}
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}

  function tabs(nav,onChange){
    var btns=nav.querySelectorAll('[role="tab"]');
    function sel(id){
      btns.forEach(function(b){
        var on=b.getAttribute('data-pane')===id;
        b.setAttribute('aria-selected',on?'true':'false');
        document.getElementById(b.getAttribute('data-pane')).hidden=!on;
      });
      if(onChange) onChange(id);
    }
    btns.forEach(function(b){b.addEventListener('click',function(){sel(b.getAttribute('data-pane'))})});
    return sel;
  }

  function mask(btn,box){
    btn.addEventListener('click',function(){
      var on=!box.classList.contains('hide');
      box.classList.toggle('hide',on);
      btn.setAttribute('aria-pressed',on?'true':'false');
      btn.textContent=on?L('顯示答案','Show answers'):L('遮住答案','Hide answers');
      box.querySelectorAll('.k.open').forEach(function(e){e.classList.remove('open')});
    });
    box.addEventListener('click',function(e){
      if(box.classList.contains('hide')&&e.target.classList.contains('k')) e.target.classList.toggle('open');
    });
  }

  /* cfg: {key,kicker,title,rules[],mode:'tf'|'mcq',time,count,questions:[{q,opts[],a,tag,note}],rank(right,n),onReview(tag)} */
  function quiz(root,cfg){
    var TL=cfg.time||20, N=Math.min(cfg.count||10,cfg.questions.length), tf=cfg.mode==='tf';
    var hasHard=cfg.questions.some(function(q){return q.h});
    function pget(k,d){try{return localStorage.getItem(k)||d}catch(e){return d}}
    function pset(k,v){try{localStorage.setItem(k,v)}catch(e){}}
    var tmOn=pget('tyTimer','on')!=='off', lvHard=hasHard&&pget('tyLevel','hard')!=='all';
    function bkey(){return cfg.key+(tmOn?'':'_nt')+(lvHard?'_h':'')}
    var SH=['▲','◆','●','■'];
    var st={}, timer=0;
    function q$(s){return root.querySelector(s)}

    function start(){
      clearInterval(timer);
      var best=lsGet(bkey());
      root.innerHTML='<p class="qk">'+esc(cfg.kicker)+'</p><h2 class="qh">'+esc(cfg.title)+'</h2>'
        +'<ul class="qrules">'+cfg.rules.map(function(r){return '<li>'+esc(r)+'</li>'}).join('')+'</ul>'
        +'<div class="qopt"><span>'+L('計時','Timer')+'</span><button class="chip" data-act="tm" data-v="on" aria-pressed="'+tmOn+'">'+L('開','On')+'</button><button class="chip" data-act="tm" data-v="off" aria-pressed="'+!tmOn+'">'+L('關','Off')+'</button></div>'
        +(hasHard?'<div class="qopt"><span>'+L('題目','Questions')+'</span><button class="chip" data-act="lv" data-v="hard" aria-pressed="'+lvHard+'">'+L('挑戰題','Challenge')+'</button><button class="chip" data-act="lv" data-v="all" aria-pressed="'+!lvHard+'">'+L('全部（包括基本）','All')+'</button></div>':'')
        +'<p class="qbest">'+(best?L('你嘅最高分：','Your best: ')+best:'')+'</p>'
        +'<button class="qbtn" data-act="go">'+L('開始','Start')+'</button>';
    }
    function begin(){
      var pool=lvHard?cfg.questions.filter(function(q){return q.h}):cfg.questions; N=Math.min(cfg.count||10,pool.length);
      st={list:shuffle(pool).slice(0,N),i:0,score:0,streak:0,bestStreak:0,right:0,missed:[],t0:0,locked:true,opts:[]};
      ask();
    }
    function ask(){
      var q=st.list[st.i]; st.locked=false;
      var o=q.opts.map(function(t,i){return {t:t,c:i===q.a}});
      st.opts=tf?o:shuffle(o);
      var tiles=st.opts.map(function(x,i){
        if(tf) return '<button class="a '+(i===0?'t':'f')+'" data-act="pick" data-i="'+i+'">'+esc(x.t)+'</button>';
        return '<button class="a c'+i+'" data-s="'+SH[i]+'" data-act="pick" data-i="'+i+'">'+esc(x.t)+'</button>';
      }).join('');
      root.innerHTML='<div class="qtop"><span>'+L('第 '+(st.i+1)+' / '+N+' 題','Question '+(st.i+1)+' / '+N)+'</span><span>'+L('分數','Score')+' <b data-r="score">'+st.score+'</b></span></div>'
        +(tmOn?'<div class="qbar"><i data-r="bar"></i></div>':'<div style="height:14px"></div>')
        +(tf?'<p class="stmt">'+esc(q.q)+'</p>':'<p class="qq">'+esc(q.q)+'</p>')
        +'<div class="'+(tf?'tf':'ans')+'">'+tiles+'</div>'
        +'<div class="qf" data-r="fb" hidden><p class="qft" data-r="ft"></p><p class="qfs" data-r="fs"></p><p class="qfr" data-r="fr"></p><button class="qbtn" data-act="next"></button></div>';
      st.t0=performance.now(); clearInterval(timer);
      if(tmOn) timer=setInterval(function(){
        if(!root.offsetParent){st.t0+=100;return}
        var el=(performance.now()-st.t0)/1000;
        var bar=q$('[data-r="bar"]'); if(bar) bar.style.width=Math.max(0,(1-el/TL)*100)+'%';
        if(el>=TL) answer(-1);
      },100);
    }
    function answer(idx){
      if(st.locked) return; st.locked=true; clearInterval(timer);
      var q=st.list[st.i], el=(performance.now()-st.t0)/1000, hit=idx>=0&&st.opts[idx].c, pts=0;
      if(hit){
        pts=(tmOn?Math.round(1000*(1-Math.min(el,TL)/TL/2)):1000)+Math.min(st.streak,5)*100;
        st.score+=pts; st.streak++; st.right++; if(st.streak>st.bestStreak) st.bestStreak=st.streak;
      }else{
        st.streak=0; if(q.tag&&st.missed.indexOf(q.tag)<0) st.missed.push(q.tag);
      }
      root.querySelectorAll('[data-act="pick"]').forEach(function(b,i){
        if(st.opts[i].c) b.classList.add('ok');
        else if(i===idx) b.classList.add('bad');
        else b.classList.add('dim');
      });
      q$('[data-r="score"]').textContent=st.score;
      var f=q$('[data-r="fb"]'); f.hidden=false; f.className='qf '+(hit?'good':'miss');
      var right=''; q.opts.forEach(function(t,i){if(i===q.a) right=t});
      q$('[data-r="ft"]').textContent=hit?(L('答啱咗！+','Correct! +')+pts):(idx<0?L('時間到','Time up'):L('答錯咗','Wrong'));
      q$('[data-r="fs"]').textContent=(hit&&st.streak>1)?(L('連續答啱 '+st.streak+' 題',st.streak+' in a row')):(L('答案：','Answer: ')+right);
      q$('[data-r="fr"]').innerHTML=q.note||'';
      q$('[data-act="next"]').textContent=st.i>=N-1?L('睇結果','See result'):L('下一題','Next');
      try{q$('[data-act="next"]').scrollIntoView({block:'nearest',behavior:'smooth'})}catch(e){}
    }
    function finish(){
      var r=st.right, rk=cfg.rank?cfg.rank(r,N):['',''];
      var b=lsGet(bkey()); if(st.score>b) lsSet(bkey(),st.score);
      root.innerHTML='<p class="qk">'+L('挑戰完成','Challenge complete')+'</p><p class="qlv">'+esc(rk[0])+'</p><p class="qlm">'+esc(rk[1])+'</p>'
        +'<div class="qstat"><div><b>'+st.score+'</b>'+L('總分','Score')+'</div><div><b>'+r+' / '+N+'</b>'+L('答啱','Correct')+'</div><div><b>'+st.bestStreak+'</b>'+L('最長連續','Best streak')+'</div></div>'
        +(st.missed.length?'<p class="qmh">'+L('答錯嘅位，撳入去睇返重點：','Missed topics, tap to review:')+'</p><div class="qm">'+st.missed.map(function(t){return '<button data-act="review" data-tag="'+esc(t)+'">'+esc(t)+'</button>'}).join('')+'</div>':'')
        +'<button class="qbtn" data-act="go">'+L('再玩一次','Play again')+'</button>';
    }
    root.addEventListener('click',function(e){
      var t=e.target.closest?e.target.closest('[data-act]'):null; if(!t) return;
      var act=t.getAttribute('data-act');
      if(act==='go') begin();
      else if(act==='tm'){tmOn=t.getAttribute('data-v')==='on';pset('tyTimer',tmOn?'on':'off');start()}
      else if(act==='lv'){lvHard=t.getAttribute('data-v')==='hard';pset('tyLevel',lvHard?'hard':'all');start()}
      else if(act==='pick') answer(+t.getAttribute('data-i'));
      else if(act==='next'){st.i++; if(st.i>=N) finish(); else ask()}
      else if(act==='review'&&cfg.onReview) cfg.onReview(t.getAttribute('data-tag'));
    });
    document.addEventListener('keydown',function(e){
      if(!root.offsetParent||st.locked||!st.opts||!st.opts.length) return;
      var n=parseInt(e.key,10);
      if(n>=1&&n<=st.opts.length&&q$('[data-act="pick"]')) answer(n-1);
    });
    start();
  }

  /* 填空：FQ=[{t,p:'文字 {0} {1}',b:[[答案,可接受…],…]}] */
  function norm(s){return String(s).replace(/[\s，。、「」！？,.!?]/g,'')}
  function okAns(v,list){
    v=norm(v); if(!v) return false;
    return list.some(function(a){return v===a||(v.length>a.length&&v.indexOf(a)>=0&&v.length<=a.length+2)});
  }
  function fill(host,FQ){
    FQ.forEach(function(q){
      var box=document.createElement('div'); box.className='fq';
      var html=esc(q.p).replace(/\{(\d+)\}/g,function(m,n){
        var len=q.b[+n][0].length;
        return '<input class="blank" type="text" data-b="'+n+'" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="'+L('第'+(+n+1)+'個空格','blank '+(+n+1))+'" style="--w:'+(len*1.15+1.6).toFixed(1)+'em" placeholder="'+len+L('字',' letters')+'">';
      });
      box.innerHTML='<h3>'+esc(q.t)+'</h3><div class="fill">'+html+'</div>'
        +'<div class="fbtns"><button class="main" data-f="check">'+L('檢查','Check')+'</button><button data-f="hint">'+L('提示','Hint')+'</button><button data-f="show">'+L('睇答案','Show')+'</button><button data-f="clear">'+L('重做','Reset')+'</button></div>'
        +'<p class="fres" aria-live="polite"></p>';
      host.appendChild(box);
      var inputs=box.querySelectorAll('input.blank'), res=box.querySelector('.fres');
      function check(){
        var n=0;
        inputs.forEach(function(inp){
          var o=okAns(inp.value,q.b[+inp.getAttribute('data-b')]);
          inp.classList.toggle('ok',o); inp.classList.toggle('bad',!o&&norm(inp.value)!=='');
          if(o) n++;
        });
        res.className='fres'+(n===inputs.length?' good':'');
        res.textContent=n===inputs.length?L('全部答啱！好叻！','All correct! Well done!'):(L('答啱 '+n+' / '+inputs.length+'，紅色嘅再試下。',n+' / '+inputs.length+' correct. Try the red ones again.'));
      }
      box.addEventListener('click',function(e){
        var b=e.target.closest('[data-f]'); if(!b) return; var f=b.getAttribute('data-f');
        if(f==='check') check();
        else if(f==='hint'){
          var shown=false;
          inputs.forEach(function(inp){
            if(shown||okAns(inp.value,q.b[+inp.getAttribute('data-b')])) return;
            inp.value=q.b[+inp.getAttribute('data-b')][0].charAt(0); shown=true; inp.focus();
          });
          res.className='fres'; res.textContent=shown?L('已經填咗第一個字，繼續寫下去。','First letter filled in. Keep going.'):L('已經全部啱晒。','All correct already.');
        }else if(f==='show'){
          inputs.forEach(function(inp){inp.value=q.b[+inp.getAttribute('data-b')][0]}); check();
          res.className='fres'; res.textContent=L('答案已填好，再試一次自己寫就更好。','Answers filled in. Try writing them yourself next time.');
        }else if(f==='clear'){
          inputs.forEach(function(inp){inp.value='';inp.classList.remove('ok','bad')}); res.textContent=''; res.className='fres';
        }
      });
      inputs.forEach(function(inp){inp.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();check()}})});
    });
  }

  /* 配對：cfg={sets:[{name,help,pairs:[[左,右],…]}]} 左右一一對應 */
  function match(root,cfg){
    var cur=0, done=0, miss=0, t0=0, SETS=cfg.sets;
    root.innerHTML=(SETS.length>1?'<div class="mset" data-m="sets">'+SETS.map(function(s,i){return '<button class="chip" data-set="'+i+'" aria-pressed="'+(i===0)+'">'+esc(s.name)+'</button>'}).join('')+'</div>':'')
      +'<p class="sub" data-m="help"></p><div class="mg" data-m="grid"></div>'
      +'<div class="mres" data-m="res" hidden><p data-m="rt"></p><button class="qbtn" data-m="again">'+L('再玩一次','Play again')+'</button></div>';
    function q$(k){return root.querySelector('[data-m="'+k+'"]')}
    var grid=q$('grid');
    function build(){
      var set=SETS[cur].pairs; done=0; miss=0; t0=Date.now();
      q$('res').hidden=true; q$('help').textContent=SETS[cur].help||L('先撳左邊，再撳右邊相配嘅一項。','Tap one on the left, then its match on the right.');
      var R, tries=0; do{R=shuffle(set.map(function(p,i){return {i:i,t:p[1]}})); tries++}while(tries<50&&set.length>1&&R.some(function(x,k){return x.i===k}));
      var html='';
      for(var k=0;k<set.length;k++){
        html+='<button class="mt l" data-i="'+k+'" data-side="l">'+esc(set[k][0])+'</button>';
        html+='<button class="mt" data-i="'+R[k].i+'" data-side="r">'+esc(R[k].t)+'</button>';
      }
      grid.innerHTML=html;
      root.querySelectorAll('[data-set]').forEach(function(c){c.setAttribute('aria-pressed',(+c.getAttribute('data-set')===cur)?'true':'false')});
    }
    grid.addEventListener('click',function(e){
      var b=e.target.closest('.mt'); if(!b||b.classList.contains('done')) return;
      var side=b.getAttribute('data-side'), same=grid.querySelector('.mt.sel[data-side="'+side+'"]');
      if(same) same.classList.remove('sel');
      b.classList.add('sel');
      var l=grid.querySelector('.mt.sel[data-side="l"]'), r=grid.querySelector('.mt.sel[data-side="r"]');
      if(l&&r){
        if(l.getAttribute('data-i')===r.getAttribute('data-i')){
          l.classList.remove('sel'); r.classList.remove('sel'); l.classList.add('done'); r.classList.add('done'); done++;
          if(done===SETS[cur].pairs.length){
            var s=Math.round((Date.now()-t0)/1000);
            q$('rt').textContent=L('全部配對完成！用咗 '+s+' 秒，錯咗 '+miss+' 次。','All matched! '+s+' s, '+miss+' mistakes. ')+(miss===0?L('一次過全中，好叻！','Perfect!'):L('再玩一次，爭取零失誤。','Play again for zero mistakes.'));
            q$('res').hidden=false;
          }
        }else{
          miss++; l.classList.add('wrong'); r.classList.add('wrong');
          setTimeout(function(){l.classList.remove('wrong','sel'); r.classList.remove('wrong','sel')},400);
        }
      }
    });
    root.addEventListener('click',function(e){
      var c=e.target.closest('[data-set]'); if(c){cur=+c.getAttribute('data-set'); build(); return}
      if(e.target.closest('[data-m="again"]')) build();
    });
    build();
  }

  function derange(arr){var r,t=0;do{r=shuffle(arr);t++}while(t<50&&arr.length>1&&r.some(function(x,k){return x.i===k}));return r}
  /* 「只睇考試範圍」：標咗 data-out 嘅內容會收埋，題目亦會過濾 */
  function scopeOn(){try{return localStorage.getItem('tyScope')==='exam'}catch(e){return false}}
  function scopeInit(){
    var on=scopeOn(); document.documentElement.setAttribute('data-scope',on?'exam':'all');
    var nav=document.getElementById('tabs'); if(!nav) return;
    var row=document.createElement('div'); row.className='row';
    row.innerHTML='<span class="scopehint"></span><button class="chip" id="scopeBtn" type="button" aria-pressed="'+on+'"></button>';
    nav.parentNode.insertBefore(row,nav);
    function paint(){row.querySelector('.scopehint').textContent=on?L('而家淨係顯示考試範圍','Showing exam scope only'):L('而家顯示晒所有內容（包括唔考嘅）','Showing everything (including non-exam)');
      row.querySelector('#scopeBtn').textContent=on?L('顯示全部','Show all'):L('只睇考試範圍','Exam scope only')}
    paint();
    row.querySelector('#scopeBtn').addEventListener('click',function(){
      try{localStorage.setItem('tyScope',on?'all':'exam')}catch(e){}
      location.reload();
    });
  }

  return {scopeOn:scopeOn,scopeInit:scopeInit,derange:derange,fill:fill,match:match,shuffle:shuffle,lsGet:lsGet,lsSet:lsSet,esc:esc,tabs:tabs,mask:mask,quiz:quiz};
})();
