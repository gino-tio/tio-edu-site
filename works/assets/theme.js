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
    if(b){b.textContent=n==='night'?'☀️ 白天':'🌙 夜間';b.setAttribute('aria-pressed',n==='night'?'true':'false')}
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
    apply(get());
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',mount); else mount();
})();
