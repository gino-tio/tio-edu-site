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
      btn.textContent=on?'顯示答案':'遮住答案';
      box.querySelectorAll('.k.open').forEach(function(e){e.classList.remove('open')});
    });
    box.addEventListener('click',function(e){
      if(box.classList.contains('hide')&&e.target.classList.contains('k')) e.target.classList.toggle('open');
    });
  }

  /* cfg: {key,kicker,title,rules[],mode:'tf'|'mcq',time,count,questions:[{q,opts[],a,tag,note}],rank(right,n),onReview(tag)} */
  function quiz(root,cfg){
    var TL=cfg.time||20, N=Math.min(cfg.count||10,cfg.questions.length), tf=cfg.mode==='tf';
    var SH=['▲','◆','●','■'];
    var st={}, timer=0;
    function q$(s){return root.querySelector(s)}

    function start(){
      clearInterval(timer);
      var best=lsGet(cfg.key);
      root.innerHTML='<p class="qk">'+esc(cfg.kicker)+'</p><h2 class="qh">'+esc(cfg.title)+'</h2>'
        +'<ul class="qrules">'+cfg.rules.map(function(r){return '<li>'+esc(r)+'</li>'}).join('')+'</ul>'
        +'<p class="qbest">'+(best?'你嘅最高分：'+best:'')+'</p>'
        +'<button class="qbtn" data-act="go">開始</button>';
    }
    function begin(){
      st={list:shuffle(cfg.questions).slice(0,N),i:0,score:0,streak:0,bestStreak:0,right:0,missed:[],t0:0,locked:true,opts:[]};
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
      root.innerHTML='<div class="qtop"><span>第 '+(st.i+1)+' / '+N+' 題</span><span>分數 <b data-r="score">'+st.score+'</b></span></div>'
        +'<div class="qbar"><i data-r="bar"></i></div>'
        +(tf?'<p class="stmt">'+esc(q.q)+'</p>':'<p class="qq">'+esc(q.q)+'</p>')
        +'<div class="'+(tf?'tf':'ans')+'">'+tiles+'</div>'
        +'<div class="qf" data-r="fb" hidden><p class="qft" data-r="ft"></p><p class="qfs" data-r="fs"></p><p class="qfr" data-r="fr"></p><button class="qbtn" data-act="next"></button></div>';
      st.t0=performance.now(); clearInterval(timer);
      timer=setInterval(function(){
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
        pts=Math.round(1000*(1-Math.min(el,TL)/TL/2))+Math.min(st.streak,5)*100;
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
      q$('[data-r="ft"]').textContent=hit?('答啱咗！+'+pts):(idx<0?'時間到':'答錯咗');
      q$('[data-r="fs"]').textContent=(hit&&st.streak>1)?('連續答啱 '+st.streak+' 題'):('答案：'+right);
      q$('[data-r="fr"]').innerHTML=q.note||'';
      q$('[data-act="next"]').textContent=st.i>=N-1?'睇結果':'下一題';
      try{q$('[data-act="next"]').scrollIntoView({block:'nearest',behavior:'smooth'})}catch(e){}
    }
    function finish(){
      var r=st.right, rk=cfg.rank?cfg.rank(r,N):['',''];
      var b=lsGet(cfg.key); if(st.score>b) lsSet(cfg.key,st.score);
      root.innerHTML='<p class="qk">挑戰完成</p><p class="qlv">'+esc(rk[0])+'</p><p class="qlm">'+esc(rk[1])+'</p>'
        +'<div class="qstat"><div><b>'+st.score+'</b>總分</div><div><b>'+r+' / '+N+'</b>答啱</div><div><b>'+st.bestStreak+'</b>最長連續</div></div>'
        +(st.missed.length?'<p class="qmh">答錯嘅位，撳入去睇返重點：</p><div class="qm">'+st.missed.map(function(t){return '<button data-act="review" data-tag="'+esc(t)+'">'+esc(t)+'</button>'}).join('')+'</div>':'')
        +'<button class="qbtn" data-act="go">再玩一次</button>';
    }
    root.addEventListener('click',function(e){
      var t=e.target.closest?e.target.closest('[data-act]'):null; if(!t) return;
      var act=t.getAttribute('data-act');
      if(act==='go') begin();
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

  return {shuffle:shuffle,lsGet:lsGet,lsSet:lsSet,esc:esc,tabs:tabs,mask:mask,quiz:quiz};
})();
