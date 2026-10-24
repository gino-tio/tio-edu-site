/* 白天／夜間模式：全站共用，記住揀咗邊個（localStorage: tyTheme） */
(function(){
  var KEY='tyTheme', root=document.documentElement;
  function get(){try{return localStorage.getItem(KEY)==='night'?'night':'day'}catch(e){return 'day'}}
  function apply(n){
    root.setAttribute('data-theme',n);
    var m=document.querySelector('meta[name="theme-color"]');
    if(!m){m=document.createElement('meta');m.name='theme-color';document.head.appendChild(m)}
    m.content=n==='night'?'#232741':'#FFFCF6';
    var b=document.getElementById('themeBtn');
    if(b){var en=document.documentElement.lang==='en';b.textContent=n==='night'?(en?'☀️ Day':'☀️ 白天'):(en?'🌙 Night':'🌙 夜間');b.setAttribute('aria-pressed',n==='night'?'true':'false')}
  }
  function set(n){try{localStorage.setItem(KEY,n)}catch(e){} apply(n)}
  apply(get());
  window.TYTheme={get:get,set:set};
  function mount(){
    var bar=document.querySelector('.bar');
    if(bar&&!document.getElementById('theme')){
      var b=document.createElement('button');
      b.id='themeBtn';b.type='button';b.className='chip themebtn';
      b.addEventListener('click',function(){set(get()==='night'?'day':'night')});
      bar.appendChild(b);
    }
    var lm=document.querySelector('meta[name="ty-lang"]');
    if(bar&&lm){
      var en=document.documentElement.lang==='en';
      var a=document.createElement('a');a.id='langBtn';a.className='chip themebtn';
      a.textContent=en?'中':'EN';a.setAttribute('aria-label',en?'切換到中文':'Switch to English');
      a.href=twin(en);
      a.addEventListener('click',function(){try{localStorage.setItem('tyLang',en?'zh':'en')}catch(e){}});
      bar.appendChild(a);
    }
    apply(get());
  }
  function twin(en){
    var p=location.pathname;
    return en?p.replace('/works/en/','/works/'):p.replace('/works/','/works/en/');
  }
  (function(){
    var lm=document.querySelector('meta[name="ty-lang"]');
    if(!lm) return;
    var en=document.documentElement.lang==='en',want='zh';
    try{want=localStorage.getItem('tyLang')==='en'?'en':'zh'}catch(e){}
    if(want==='en'&&!en) location.replace(twin(false));
    else if(want==='zh'&&en) location.replace(twin(true));
  })();
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',mount); else mount();
})();
