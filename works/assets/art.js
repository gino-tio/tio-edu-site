/* 繪本風 SVG 插圖：全部平塗、3px 墨灰線。用 data-art="scene|walker|notebook|camp|cloud" 放入頁面 */
(function(){
  var I='#3E3A39',C='#F2A497',Y='#F6D27A',B='#A8D3E6',G='#B9DAA5',P='#FFFCF6';
  var S='stroke="'+I+'" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"';

  function wavePath(y,amp){
    var d='M-20 '+y+' q15 -'+amp+' 30 0'; for(var i=0;i<16;i++) d+=' t30 0';
    return d+' V260 H-20 Z';
  }
  function cloud(cx,cy,s,withFace){
    /* 兩層：先畫線框，再用同色填返內裡，令重疊位冇線 */
    var g='<g transform="translate('+cx+' '+cy+') scale('+s+')">';
    var shapes='<circle cx="-24" cy="6" r="20"/><circle cx="0" cy="-8" r="26"/><circle cx="26" cy="4" r="20"/><rect x="-24" y="4" width="52" height="22" rx="11"/>';
    g+='<g fill="'+B+'" '+S+'>'+shapes+'</g><g fill="'+B+'" stroke="none">'+shapes+'</g>';
    if(withFace){
      g+='<circle cx="-9" cy="2" r="3.2" fill="'+I+'"/><circle cx="11" cy="2" r="3.2" fill="'+I+'"/>'
        +'<ellipse cx="-19" cy="12" rx="5.5" ry="3.8" fill="'+C+'"/><ellipse cx="21" cy="12" rx="5.5" ry="3.8" fill="'+C+'"/>'
        +'<ellipse cx="1" cy="13" rx="5" ry="6" fill="'+P+'" stroke="'+I+'" stroke-width="2.5"/>';
    }
    return g+'</g>';
  }
  function frame(inner,vb,label,id){
    var w=vb[0],h=vb[1];
    return '<svg class="art" viewBox="0 0 '+w+' '+h+'" role="img" aria-label="'+label+'">'
      +'<defs><clipPath id="'+id+'"><rect x="3" y="3" width="'+(w-6)+'" height="'+(h-6)+'" rx="28"/></clipPath></defs>'
      +'<g clip-path="url(#'+id+')"><rect width="'+w+'" height="'+h+'" fill="'+P+'"/>'+inner+'</g>'
      +'<rect x="3" y="3" width="'+(w-6)+'" height="'+(h-6)+'" rx="28" fill="none" stroke="'+I+'" stroke-width="3"/></svg>';
  }

  var ART={
    scene:function(){
      var t='';
      /* 海 */
      t+='<g class="wave"><path d="'+wavePath(152,12)+'" fill="'+B+'" '+S+'/></g>';
      /* 遠處嘅船 */
      t+='<g class="bob"><path d="M122 150 h44 l-9 13 h-26 Z" fill="'+Y+'" '+S+'/><rect x="138" y="132" width="18" height="18" rx="5" fill="'+P+'" '+S+'/><circle cx="147" cy="141" r="3" fill="'+I+'"/></g>';
      /* 碼頭 */
      t+='<rect x="244" y="170" width="10" height="34" fill="'+C+'" '+S+'/><rect x="292" y="170" width="10" height="34" fill="'+C+'" '+S+'/><rect x="338" y="170" width="10" height="34" fill="'+C+'" '+S+'/>';
      t+='<rect x="232" y="152" width="140" height="18" rx="8" fill="'+Y+'" '+S+'/>';
      t+='<path d="M246 152 v-22 M296 152 v-22 M346 152 v-22 M246 134 H346" fill="none" '+S+'/>';
      /* 招牌 */
      t+='<rect x="274" y="84" width="9" height="68" rx="3" fill="'+I+'"/>';
      t+='<g class="swing" style="transform-origin:278px 88px"><path d="M278 88 v8" fill="none" '+S+'/><rect x="248" y="96" width="62" height="30" rx="10" fill="'+C+'" '+S+'/><circle cx="279" cy="111" r="7" fill="'+Y+'" '+S+'/></g>';
      /* 彎腰嘅樹 */
      var crown='<circle cx="68" cy="88" r="27"/><circle cx="44" cy="102" r="19"/><circle cx="93" cy="100" r="19"/>';
      t+='<g class="sway" style="transform-origin:70px 152px"><rect x="62" y="102" width="16" height="52" rx="7" fill="'+C+'" '+S+'/>'
        +'<g fill="'+G+'" '+S+'>'+crown+'</g><g fill="'+G+'" stroke="none">'+crown+'</g></g>';
      /* 飛走嘅葉 */
      t+='<g class="floaty" style="transform-origin:130px 118px"><ellipse cx="130" cy="118" rx="9" ry="5" fill="'+G+'" '+S+' transform="rotate(-25 130 118)"/></g>';
      t+='<g class="floaty" style="transform-origin:112px 140px;animation-delay:-1.2s"><ellipse cx="112" cy="138" rx="8" ry="4.5" fill="'+G+'" '+S+' transform="rotate(20 112 138)"/></g>';
      /* 反轉嘅雨傘 */
      t+='<g class="floaty" style="transform-origin:108px 50px;animation-delay:-.8s"><path d="M80 36 Q108 70 136 36 Q122 46 108 36 Q94 46 80 36 Z" fill="'+C+'" '+S+'/><path d="M108 56 V82 q0 9 -9 9" fill="none" '+S+'/></g>';
      /* 吹氣嘅颱風雲 */
      t+='<g class="bob">'+cloud(210,56,1.05,true)+'</g>';
      t+='<path class="flow" d="M196 84 q-34 6 -66 -4" fill="none" '+S+'/><path class="flow" d="M200 94 q-24 14 -58 8" fill="none" '+S+' style="animation-delay:-.5s"/>';
      /* 雨 */
      t+='<path class="drop" d="M236 84 l-5 12" stroke="'+B+'" stroke-width="5" stroke-linecap="round"/>'
        +'<path class="drop" style="animation-delay:-.4s" d="M250 90 l-5 12" stroke="'+B+'" stroke-width="5" stroke-linecap="round"/>'
        +'<path class="drop" style="animation-delay:-.8s" d="M224 92 l-5 12" stroke="'+B+'" stroke-width="5" stroke-linecap="round"/>';
      return frame(t,[360,220],'可愛嘅颱風插畫：吹氣嘅雲、反轉嘅雨傘、彎腰嘅樹、搖晃嘅招牌同碼頭','sc1');
    },
    walker:function(){
      var t='';
      /* 小山路 */
      t+='<path d="M-10 150 Q70 120 150 138 T330 128 T380 140 V200 H-10 Z" fill="'+G+'" '+S+'/>';
      /* 腳印 */
      var fx=[28,60,92,124,156,188];
      fx.forEach(function(x,i){t+='<ellipse cx="'+x+'" cy="'+(166-(i%2)*8)+'" rx="7" ry="4.5" fill="'+Y+'" '+S+'/>'});
      /* 風線 */
      t+='<path class="flow" d="M12 60 h42" fill="none" '+S+'/><path class="flow" style="animation-delay:-.4s" d="M24 82 h34" fill="none" '+S+'/><path class="flow" style="animation-delay:-.8s" d="M8 104 h30" fill="none" '+S+'/>';
      /* 碼頭鐵欄同望遠鏡 */
      t+='<rect x="236" y="122" width="116" height="16" rx="8" fill="'+Y+'" '+S+'/><path d="M252 122 v-30 M292 122 v-30 M332 122 v-30 M252 98 H332" fill="none" '+S+'/>';
      t+='<g class="wig" style="transform-origin:300px 74px"><rect x="296" y="52" width="46" height="18" rx="8" fill="'+B+'" '+S+' transform="rotate(-18 300 70)"/><rect x="290" y="64" width="16" height="22" rx="6" fill="'+C+'" '+S+' transform="rotate(-18 300 70)"/></g>';
      /* 細路 */
      t+='<g class="bob">'
        +'<g class="wig" style="transform-origin:150px 66px"><path d="M114 56 Q150 14 186 56 Q168 48 150 56 Q132 48 114 56 Z" fill="'+C+'" '+S+'/><path d="M150 54 L142 108" fill="none" '+S+'/></g>'
        +'<rect x="124" y="92" width="44" height="40" rx="16" fill="'+B+'" '+S+'/>'
        +'<circle cx="146" cy="74" r="22" fill="'+P+'" '+S+'/>'
        +'<path d="M126 70 Q130 52 146 52 Q164 52 166 70 Q150 62 126 70 Z" fill="'+Y+'" '+S+'/>'
        +'<circle cx="138" cy="78" r="2.8" fill="'+I+'"/><circle cx="155" cy="78" r="2.8" fill="'+I+'"/>'
        +'<ellipse cx="131" cy="86" rx="5" ry="3.5" fill="'+C+'"/><ellipse cx="162" cy="86" rx="5" ry="3.5" fill="'+C+'"/>'
        +'<path d="M142 88 q4 3 8 0" fill="none" '+S+'/>'
        +'<ellipse cx="136" cy="138" rx="9" ry="5.5" fill="'+C+'" '+S+'/><ellipse cx="160" cy="138" rx="9" ry="5.5" fill="'+C+'" '+S+'/>'
        +'</g>';
      return frame(t,[360,190],'可愛嘅插畫：細路撐住雨傘，沿着腳印行去碼頭，用望遠鏡望海','sc2');
    },
    notebook:function(){
      var t='';
      t+='<g class="wave"><path d="'+wavePath(132,9)+'" fill="'+B+'" '+S+'/></g>';
      t+='<rect x="52" y="30" width="236" height="96" rx="16" fill="'+G+'" '+S+'/>';
      t+='<path d="M64 40 h104 v74 h-104 Z" fill="'+P+'" '+S+'/><path d="M172 40 h104 v74 h-104 Z" fill="'+P+'" '+S+'/>';
      t+='<path d="M78 58 h72 M78 74 h72 M78 90 h50 M186 58 h72 M186 74 h72 M186 90 h44" fill="none" stroke="'+B+'" stroke-width="3.5" stroke-linecap="round"/>';
      t+='<path d="M132 94 l8 9 l16 -18" fill="none" stroke="'+C+'" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>';
      t+='<g class="wig" style="transform-origin:300px 104px"><g transform="rotate(35 300 78)"><rect x="288" y="36" width="20" height="72" rx="4" fill="'+Y+'" '+S+'/><rect x="288" y="26" width="20" height="14" rx="5" fill="'+C+'" '+S+'/><path d="M288 108 L298 128 L308 108 Z" fill="'+P+'" '+S+'/><path d="M294 120 l4 8 l4 -8 Z" fill="'+I+'"/></g></g>';
      t+='<g class="bob">'+cloud(316,38,.62,true)+'</g>';
      t+='<g class="bob"><path d="M26 124 h34 l-7 11 h-20 Z" fill="'+Y+'" '+S+'/><rect x="36" y="108" width="14" height="16" rx="5" fill="'+P+'" '+S+'/></g>';
      return frame(t,[360,160],'可愛嘅插畫：打開嘅筆記簿、鉛筆、細細朵颱風雲同海上嘅船','sc3');
    },
    camp:function(){
      var t='';
      t+='<circle cx="316" cy="40" r="17" fill="'+Y+'" '+S+'/>';
      t+='<path d="M-10 150 Q90 126 190 144 T380 134 V200 H-10 Z" fill="'+G+'" '+S+'/>';
      t+='<path d="M64 156 L128 68 L192 156 Z" fill="'+C+'" '+S+'/><path d="M128 156 L128 112 L108 156 Z" fill="'+P+'" '+S+'/><path d="M128 156 L128 112 L150 156 Z" fill="'+Y+'" '+S+'/>';
      t+='<path d="M128 68 V40" fill="none" '+S+'/><g class="wig" style="transform-origin:128px 46px"><path d="M128 40 l36 10 l-36 10 Z" fill="'+Y+'" '+S+'/></g>';
      t+='<g class="bob"><g transform="translate(262 104) rotate(-28)"><rect x="18" y="-6" width="40" height="12" rx="6" fill="'+P+'" '+S+'/><circle cx="60" cy="-7" r="8" fill="'+P+'" '+S+'/><circle cx="60" cy="7" r="8" fill="'+P+'" '+S+'/><rect x="52" y="-6" width="10" height="12" fill="'+P+'"/>';
      t+='<ellipse cx="0" cy="0" rx="30" ry="23" fill="'+Y+'" '+S+'/><circle cx="-9" cy="-3" r="3" fill="'+I+'"/><circle cx="9" cy="-3" r="3" fill="'+I+'"/><ellipse cx="-16" cy="6" rx="5" ry="3.4" fill="'+C+'"/><ellipse cx="16" cy="6" rx="5" ry="3.4" fill="'+C+'"/><path d="M-4 5 q4 4 8 0" fill="none" '+S+'/></g></g>';
      t+='<path class="flow" d="M200 80 h36" fill="none" '+S+'/><path class="flow" style="animation-delay:-.6s" d="M212 98 h28" fill="none" '+S+'/>';
      return frame(t,[360,190],'可愛嘅插畫：軍帳、旗同一隻雞肋','sc4');
    },
    cloud:function(){
      return '<svg class="art" style="width:64px;margin:0" viewBox="0 0 90 70" role="img" aria-label="颱風雲"><g class="bob">'+cloud(45,36,1.05,true)+'</g></svg>';
    }
  };
  function mount(){
    document.querySelectorAll('[data-art]').forEach(function(el){
      var f=ART[el.getAttribute('data-art')]; if(f) el.innerHTML=f();
    });
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',mount); else mount();
})();
