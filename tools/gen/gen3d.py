import re
import os
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.normpath(os.path.join(HERE,'..','..','works'))+'/'
SRC=ROOT+'typhoon-memory-route/index.html'
DST=ROOT+'yx-3d/index.html'
s=open(SRC,encoding='utf-8').read()
def cut(s,start,end,new,incl_end=False):
    a=s.index(start); b=s.index(end,a)+(len(end) if incl_end else 0)
    return s[:a]+new+s[b:]

STOPS=r'''var STOPS=[
 {name:'軍營・雞肋',seg:'第1–3段',hook:'口訣：現在・近因・詳寫',html:'楊修從暗號「<span class="k">雞肋</span>」推測<span class="k">曹操將退兵</span>，吩咐士兵<span class="k">收拾行裝</span>。結果被判<span class="k">惑亂軍心</span>之罪<span class="k">處死</span>。（發生時間：現在；篇幅較長，屬<span class="k">詳寫</span>）'},
 {name:'過渡句',seg:'第4段',hook:'口訣：上承經過，下啟往事',html:'「<span class="k">原來楊修為人，恃才放曠，數犯曹操之忌</span>」是過渡句：<span class="k">上承</span>楊修被處死的經過和結果，<span class="k">下啟</span>過去楊修與曹操之間的往事，令文章轉折<span class="k">自然</span>。'},
 {name:'園門',seg:'第4段',hook:'口訣：「活」字＝嫌園門太闊',html:'事件二：曹操在門上寫「<span class="k">活</span>」字，楊修猜出是嫌<span class="k">園門太闊</span>，招致曹操的<span class="k">妒忌</span>。（過去；略寫）'},
 {name:'一合酥',seg:'第5段',hook:'口訣：一人一口酥，分來食',html:'事件三：楊修猜中「一合酥」是指「<span class="k">一人一口酥</span>」，把酥餅<span class="k">與眾人分來吃</span>，招致曹操的<span class="k">厭惡</span>。（過去；略寫）'},
 {name:'夢中殺人',seg:'第6段',hook:'口訣：揭穿假夢，更厭惡',html:'事件四：曹操假裝<span class="k">夢中殺人</span>，楊修當眾<span class="k">揭穿</span>，令曹操<span class="k">更感厭惡</span>。（過去；略寫）'},
 {name:'吳質大竹篋',seg:'第7段',hook:'口訣：密告反被暗算，背誣害',html:'事件五：楊修密告曹丕與吳質會談<span class="k">世子繼位</span>的事，反被<span class="k">吳質</span>暗算，背上<span class="k">誣害曹丕</span>之嫌，令曹操<span class="k">更感厭惡</span>。'},
 {name:'鄴城門',seg:'第8段',hook:'口訣：教曹植斬門吏，曹操憤怒',html:'事件六：楊修教曹植出<span class="k">鄴城門</span>的方法，令曹操十分<span class="k">憤怒</span>。（過去；略寫）'},
 {name:'答教書案',seg:'第9段',hook:'口訣：十多條答教，殺意起',html:'事件七：楊修為曹植作「<span class="k">答教</span>」，用以<span class="k">應對曹操的考問</span>，令曹操大怒並萌生<span class="k">殺意</span>，借<span class="k">惑亂軍心</span>的罪名殺了他。'}
];
'''

BUILD=r'''
var C_=0xF2A497,Y_=0xF6D27A,B_=0xA8D3E6,G_=0xB9DAA5,P_=0xFFFCF6,I_=0x3E3A39;
function glyph(text,w,h,fg,bg,rot){
  var W=512,H=Math.max(64,Math.round(512*h/w));
  var c=document.createElement('canvas'); c.width=W; c.height=H;
  var tex=new THREE.CanvasTexture(c);
  function draw(){
    var x=c.getContext('2d'); x.clearRect(0,0,W,H);
    if(bg){x.fillStyle=bg; x.fillRect(0,0,W,H); x.strokeStyle='#3E3A39'; x.lineWidth=10; x.strokeRect(5,5,W-10,H-10);}
    var fs=Math.min(H*0.62,(W-40)/Math.max(1,text.length)*0.95);
    x.fillStyle=fg; x.font=fs+'px "Huninn","Noto Sans TC","PingFang TC","Microsoft JhengHei",sans-serif';
    x.textAlign='center'; x.textBaseline='middle'; x.fillText(text,W/2,H/2+fs*0.06);
    tex.needsUpdate=true;
  }
  draw(); labels.push(draw);
  return new THREE.Mesh(new THREE.PlaneGeometry(w,h),new THREE.MeshBasicMaterial({map:tex,transparent:true,side:THREE.DoubleSide}));
}
function tree2(g,x,z,s){
  var t=new THREE.Group(); t.position.set(x,0,z);
  t.add(cyl(0.18*s,0.26*s,1.6*s,C_,0,0.8*s,0,6));
  t.add(cone(1.3*s,2.4*s,0xA9D08E,0,2.4*s,0));
  t.add(cone(1*s,2*s,G_,0,3.5*s,0));
  g.add(t); return t;
}
function ground(g,w,d,z){g.add(box(w,0.05,d,0xE9E1D1,0,0.025,z||0))}
function b1(g){
  ground(g,11,9,0);
  var tent=new THREE.Mesh(new THREE.ConeGeometry(3.1,3.6,4),M(C_)); tent.position.set(-2.8,1.8,-1.2); tent.rotation.y=Math.PI/4; g.add(tent);
  g.add(cyl(0.05,0.05,2,I_,-2.8,4.6,-1.2,6));
  var flag=new THREE.Group(); flag.position.set(-2.8,5.3,-1.2); flag.add(box(1.1,0.6,0.05,Y_,0.55,0,0)); g.add(flag);
  var dr=new THREE.Group(); dr.position.set(2.8,2.8,0);
  var meat=sph(1.0,Y_,0,0,0); meat.scale.set(1,0.85,0.9); dr.add(meat);
  var bone=cyl(0.17,0.17,1.7,P_,0.9,0.95,0,8); bone.rotation.z=-0.75; dr.add(bone);
  dr.add(sph(0.3,P_,1.55,1.6,0.15)); dr.add(sph(0.3,P_,1.55,1.6,-0.15));
  dr.add(glow(0.16,0.16,0.1,I_,-0.35,0.15,0.9)); dr.add(glow(0.16,0.16,0.1,I_,0.35,0.15,0.9));
  g.add(dr);
  var sol=[person(B_,-0.6,2.4),person(Y_,0.8,3.2),person(G_,-1.8,3.4)];
  sol.forEach(function(p){g.add(p)});
  var bun=[]; [[1.9,2.6],[2.9,3.1],[3.7,2.2]].forEach(function(a,i){var b=box(0.8,0.6,0.7,[C_,Y_,B_][i],a[0],0.33,a[1]); g.add(b); bun.push(b)});
  g.add(cyl(0.06,0.08,2.6,I_,-4.6,1.3,2.4,6)); g.add(glow(0.4,0.4,0.4,Y_,-4.6,2.8,2.4));
  anims.push(function(t){
    dr.rotation.y=t*0.8; dr.position.y=2.8+Math.sin(t*2)*0.2;
    flag.rotation.y=Math.sin(t*3)*0.4;
    sol.forEach(function(p,i){p.position.y=Math.abs(Math.sin(t*4+i*1.3))*0.25});
    bun.forEach(function(b,i){b.rotation.y=Math.sin(t*2+i)*0.2});
  });
}
function b2(g){
  ground(g,11,9,0);
  g.add(box(11,0.3,2.6,Y_,0,0.55,0.8));
  for(var x=-4;x<=4;x+=2) g.add(cyl(0.25,0.25,0.55,I_,x,0.28,0.8,8));
  [-0.3,1.9].forEach(function(z){g.add(box(11,0.1,0.1,I_,0,1.5,z)); for(var x2=-5;x2<=5;x2+=2.5) g.add(box(0.1,0.9,0.1,I_,x2,1.05,z))});
  g.add(box(2.6,3.8,2.4,B_,-4.4,1.9,-2.6)); g.add(box(2.6,2.6,2.4,G_,4.4,1.3,-2.6));
  var a=glyph('現在',2.0,0.9,'#3E3A39','#FFFCF6'); a.position.set(-4.4,3.0,-1.38); g.add(a);
  var b=glyph('過去',2.0,0.9,'#3E3A39','#FFFCF6'); b.position.set(4.4,1.9,-1.38); g.add(b);
  var arrow=new THREE.Group(); arrow.position.set(0,3.0,0.8);
  var sh=cyl(0.2,0.2,2.6,C_,0,0,0,8); sh.rotation.z=Math.PI/2; arrow.add(sh);
  var hd=cone(0.6,1.1,C_,-1.85,0,0); hd.rotation.z=Math.PI/2; arrow.add(hd);
  g.add(arrow);
  var t1=glyph('原來楊修為人，恃才放曠，數犯曹操之忌',8.4,1.0,'#3E3A39','#FFFCF6'); t1.position.set(0,0.8,3.9); g.add(t1);
  var p=person(B_,-2,2.4); g.add(p);
  anims.push(function(t){arrow.position.x=Math.sin(t*1.4)*1.4; arrow.position.y=3.0+Math.sin(t*2.8)*0.12; p.position.x=-2+Math.sin(t*0.8)*2});
}
function b3(g){
  ground(g,11,9,0);
  g.add(box(1,4,1,C_,-3.4,2,0)); g.add(box(1,4,1,C_,3.4,2,0));
  g.add(box(8.2,0.8,1.3,C_,0,4.3,0)); g.add(box(9.2,0.35,2.0,I_,0,4.9,0));
  var board=new THREE.Group(); board.position.set(0,4.0,0.2);
  var bd=glyph('活',1.7,1.7,'#3E3A39','#FFFCF6'); bd.position.set(0,-0.95,0.1); board.add(bd);
  board.add(box(0.06,0.4,0.06,I_,-0.6,-0.1,0)); board.add(box(0.06,0.4,0.06,I_,0.6,-0.1,0));
  g.add(board);
  var w=glyph('嫌園門太闊',3.4,0.8,'#3E3A39','#F6D27A'); w.position.set(0,0.9,3.4); g.add(w);
  var ts=[tree2(g,-2,-3,1.1),tree2(g,2.2,-3.2,1.2),tree2(g,0,-4,0.9)];
  for(var i=-4;i<=4;i+=1) g.add(box(0.08,1.0,0.08,I_,i,0.5,-1.4));
  g.add(box(9,0.08,0.08,I_,0,0.9,-1.4));
  var yx=person(B_,3.6,2.4), cc=person(C_,-3.6,2.4); g.add(yx); g.add(cc);
  anims.push(function(t){board.rotation.z=Math.sin(t*2)*0.08; ts.forEach(function(tr,i){tr.rotation.z=Math.sin(t*1.6+i)*0.03}); yx.position.y=Math.abs(Math.sin(t*3))*0.15});
}
function b4(g){
  ground(g,11,9,0);
  g.add(box(5.6,0.25,2.8,Y_,0,1.3,0));
  [[-2.5,-1.2],[2.5,-1.2],[-2.5,1.2],[2.5,1.2]].forEach(function(a){g.add(box(0.25,1.2,0.25,I_,a[0],0.62,a[1]))});
  g.add(box(1.8,0.7,1.3,C_,0,1.78,0));
  var lid=glyph('一合酥',1.6,0.9,'#3E3A39','#FFFCF6'); lid.rotation.x=-Math.PI/2; lid.position.set(0,2.15,0); g.add(lid);
  var seats=[[-3.4,1.6,B_],[3.4,1.6,G_],[-2.2,-2.6,C_],[2.2,-2.6,Y_]], ps=[], ck=[];
  seats.forEach(function(a){var p=person(a[2],a[0],a[1]); g.add(p); ps.push(p)});
  for(var i=0;i<4;i++){var c=cyl(0.2,0.2,0.12,0xE9C98F,0,2,0,10); g.add(c); ck.push(c)}
  var bub=glyph('一人一口酥',4.6,1.0,'#3E3A39','#F6D27A'); bub.position.set(0,3.7,0.4); g.add(bub);
  anims.push(function(t){
    ck.forEach(function(c,i){var ph=((t*0.5+i*0.25)%1), a=seats[i];
      c.position.x=a[0]*ph; c.position.z=a[1]*ph; c.position.y=2.0-ph*0.4+Math.sin(ph*Math.PI)*0.9});
    ps.forEach(function(p,i){p.position.y=Math.abs(Math.sin(t*3+i))*0.12});
    bub.position.y=3.7+Math.sin(t*2)*0.12;
  });
}
function b5(g){
  ground(g,11,9,0);
  g.add(box(4.6,0.6,2.6,B_,-1.2,0.6,-0.5));
  g.add(box(1,0.3,1.3,P_,-3.0,1.05,-0.5));
  g.add(sph(0.45,0xe3c3a0,-2.9,1.45,-0.5));
  var blk=box(3,0.35,2.4,C_,0.1,1.05,-0.5); g.add(blk);
  var fell=box(1.6,0.12,1.4,C_,2.4,0.08,1.6); fell.rotation.y=0.5; g.add(fell);
  var dream=glyph('夢',1.4,1.4,'#3E3A39','#F6D27A'); dream.position.set(-2.6,3.6,-0.5); g.add(dream);
  var z1=glyph('Z z z',1.8,0.7,'#3E3A39',null); z1.position.set(-2.2,2.7,-0.5); g.add(z1);
  var sword=new THREE.Group(); sword.position.set(1.8,2.3,1.4);
  sword.add(box(0.12,2.2,0.05,0xCFD8DC,0,0.9,0)); sword.add(box(0.5,0.12,0.12,C_,0,-0.2,0)); sword.add(box(0.12,0.5,0.12,I_,0,-0.5,0));
  g.add(sword);
  var att=person(B_,3.4,2.4); g.add(att);
  var t1=glyph('丞相非在夢中，君乃在夢中耳',7.4,1.0,'#3E3A39','#FFFCF6'); t1.position.set(0,0.8,3.9); g.add(t1);
  anims.push(function(t){
    sword.rotation.z=0.7+Math.sin(t*3)*0.5; dream.position.y=3.6+Math.sin(t*1.5)*0.2; z1.position.y=2.7+Math.sin(t*1.5+1)*0.15;
    att.position.z=2.4-Math.abs(Math.sin(t*0.7))*1.6; blk.position.y=1.05+Math.sin(t*1.2)*0.03;
  });
}
function b6(g){
  ground(g,11,9,0);
  g.add(box(4.2,4,3.2,C_,3.8,2,-2.2)); g.add(box(5,0.5,4,I_,3.8,4.2,-2.2));
  var door=glyph('府',1.1,1.5,'#3E3A39','#FFFCF6'); door.position.set(3.8,1.1,-0.58); g.add(door);
  var bk=new THREE.Group(); bk.position.set(-4,0,1.4);
  bk.add(cyl(1.15,1.0,2.4,0xE9C98F,0,1.2,0,14));
  [[C_,-0.4],[B_,0],[G_,0.4]].forEach(function(a){bk.add(cyl(0.28,0.28,1.1,a[0],a[1],2.7,0,8))});
  var tag=glyph('吳質',1.3,0.7,'#3E3A39','#FFFCF6'); tag.position.set(0,1.2,1.12); bk.add(tag);
  g.add(bk);
  var sec=glyph('絹疋',1.5,0.7,'#3E3A39','#F6D27A'); sec.position.set(0,4.1,0); bk.add(sec);
  var yx=person(B_,-0.4,2.8), cp=person(G_,1.4,3.0); g.add(yx); g.add(cp);
  var q=glyph('密告 → 反被暗算',4.8,0.9,'#3E3A39','#FFFCF6'); q.position.set(-0.6,0.8,4.0); g.add(q);
  anims.push(function(t){
    bk.position.x=-4.4+((t*0.9)%7.4); bk.position.y=Math.abs(Math.sin(t*5))*0.06;
    yx.position.y=Math.abs(Math.sin(t*3))*0.15; cp.position.y=Math.abs(Math.sin(t*3+1))*0.15;
  });
}
function b7(g){
  ground(g,11,9,0);
  g.add(box(2.4,4.6,2.6,B_,-3.5,2.3,-1.8)); g.add(box(2.4,4.6,2.6,B_,3.5,2.3,-1.8));
  g.add(box(4.6,1.2,2.6,B_,0,4.0,-1.8));
  var nm=glyph('鄴城門',3.6,0.9,'#3E3A39','#FFFCF6'); nm.position.set(0,4.0,-0.48); g.add(nm);
  var dl=new THREE.Group(); dl.position.set(-2.2,0,-0.6); dl.add(box(2.2,3.2,0.25,Y_,1.1,1.6,0)); g.add(dl);
  var dr=new THREE.Group(); dr.position.set(2.2,0,-0.6); dr.add(box(2.2,3.2,0.25,Y_,-1.1,1.6,0)); g.add(dr);
  var guard=person(C_,-1,0.6), cz=person(G_,2,3.8); g.add(guard); g.add(cz);
  g.add(cyl(0.05,0.05,3,I_,-1.7,1.6,0.6,6));
  var sw=new THREE.Group(); sw.position.set(2.8,1.5,3.6); sw.add(box(0.12,1.8,0.05,0xCFD8DC,0,0.8,0)); sw.add(box(0.45,0.1,0.1,C_,0,-0.1,0)); g.add(sw);
  g.add(cyl(0.06,0.08,2.4,I_,-5,1.2,2.2,6)); g.add(glow(0.4,0.4,0.4,Y_,-5,2.6,2.2));
  g.add(cyl(0.06,0.08,2.4,I_,5,1.2,2.2,6)); g.add(glow(0.4,0.4,0.4,Y_,5,2.6,2.2));
  var q=glyph('吾奉王命，誰敢阻當！',5.2,0.9,'#3E3A39','#F6D27A'); q.position.set(0.4,0.9,4.2); g.add(q);
  anims.push(function(t){
    var o=0.5+0.5*Math.sin(t*0.8); dl.rotation.y=-o*0.5; dr.rotation.y=o*0.5;
    cz.position.z=3.8-((t*0.5)%1)*1.8; sw.rotation.z=Math.sin(t*3)*0.4; guard.position.y=Math.abs(Math.sin(t*2))*0.1;
  });
}
function b8(g){
  ground(g,11,9,0);
  g.add(box(4.2,0.22,2.2,Y_,-1,1.3,0.4));
  [[-2.8,-0.5],[0.8,-0.5],[-2.8,1.3],[0.8,1.3]].forEach(function(a){g.add(box(0.22,1.2,0.22,I_,a[0],0.62,a[1]))});
  var sc=[];
  for(var i=0;i<10;i++){
    var r=i<5?0:1, k=i<5?i:i-5, x=-2.4+k*0.9+(r?0.45:0), y=1.62+r*0.38;
    var c=cyl(0.2,0.2,1.2,P_,x,y,0.4,10); c.rotation.x=Math.PI/2; g.add(c);
    var b=cyl(0.21,0.21,0.18,C_,x,y,0.4,10); b.rotation.x=Math.PI/2; g.add(b); sc.push(c);
  }
  var ds=glyph('答教十多條',3.2,0.8,'#3E3A39','#FFFCF6'); ds.position.set(-1,0.7,1.6); ds.rotation.x=-0.25; g.add(ds);
  var cz=person(G_,-3.6,2.6); g.add(cz);
  var cc=person(C_,3.6,-0.4); cc.scale.set(1.3,1.3,1.3); g.add(cc);
  var bub=glyph('匹夫安敢欺我耶！',5.4,1.1,'#3E3A39','#F2A497'); bub.position.set(2.2,3.2,-0.4); g.add(bub);
  var ang=glyph('怒',1.2,1.2,'#3E3A39','#F6D27A'); ang.position.set(-1.8,3.6,0.4); g.add(ang);
  var pp=[];
  for(var j=0;j<8;j++){var m=box(0.6,0.03,0.8,0xFFFFFF,0,0,0); g.add(m); pp.push(m)}
  anims.push(function(t){
    bub.position.x=2.2+Math.sin(t*14)*0.05; ang.scale.setScalar(1+0.12*Math.sin(t*6)); ang.rotation.z=Math.sin(t*10)*0.1;
    pp.forEach(function(m,i){var a=t*0.6+i*0.785; m.position.set(-1+Math.cos(a)*3.2,2.6+Math.sin(a*2)*0.5,0.4+Math.sin(a)*2.2); m.rotation.y=a; m.rotation.x=Math.sin(a*3)*0.3});
    cc.position.y=Math.abs(Math.sin(t*5))*0.08;
  });
}
var BUILD=[b1,b2,b3,b4,b5,b6,b7,b8];
'''

QS=[
[0,'楊修從暗號「＿＿」推測曹操將退兵。','雞肋',['鴨肋','牛肋','豬肋']],
[0,'楊修因為猜中曹操將退兵，吩咐士兵＿＿。','收拾行裝',['繼續進攻','加強守衛','修築營壘']],
[0,'雞肋事件中，楊修被判＿＿之罪處死。','惑亂軍心',['欺君','通敵','貪污']],
[0,'雞肋事件發生喺「＿＿」，屬於詳寫。','現在',['過去','將來','夢中']],
[1,'第4段嘅過渡句係「原來楊修為人，＿＿，數犯曹操之忌」。','恃才放曠',['自作聰明','目空一切','鋒芒畢露']],
[1,'過渡句上承楊修被處死嘅經過，下啟＿＿。','過去發生嘅往事',['日後嘅打算','曹操嘅計劃','城外嘅戰況']],
[1,'過渡句令文章嘅轉折顯得＿＿。','自然',['突兀','混亂','冗長']],
[2,'曹操喺門上寫咗一個「＿＿」字。','活',['闊','闌','閑']],
[2,'楊修猜出「活」字係嫌＿＿。','園門太闊',['園門太窄','園牆太高','園內太靜']],
[2,'闊門事件招致曹操嘅＿＿。','妒忌',['歡喜','厭惡','憤怒']],
[3,'「一合酥」被楊修理解為「＿＿」。','一人一口酥',['一合一口酥','一人一盒酥','每人一盒酥']],
[3,'楊修把酥餅＿＿。','與眾人分來吃',['獨自吃光','送給曹操','藏起來']],
[3,'一合酥事件令曹操感到＿＿。','厭惡',['妒忌','憤怒','歡喜']],
[4,'曹操常常假裝會喺＿＿殺人。','夢中',['戰場上','營帳外','酒醉時']],
[4,'楊修當眾＿＿曹操假裝夢中殺人。','揭穿',['附和','隱瞞','讚賞']],
[4,'夢中殺人事件令曹操＿＿。','更感厭惡',['十分高興','毫不在意','大怒殺人']],
[5,'楊修密告曹丕與吳質會談嘅事，係關於＿＿。','世子繼位',['軍國大事','出兵計劃','糧草安排']],
[5,'吳質被藏喺＿＿入面。','大竹篋',['馬車','木箱','大籮']],
[5,'楊修因此背上＿＿之嫌。','誣害曹丕',['欺君','謀反','通敵']],
[6,'楊修教曹植出＿＿嘅方法。','鄴城門',['洛陽門','許昌門','朝歌門']],
[6,'楊修教曹植遇到阻擋嘅人，就可以＿＿。','直接斬殺',['好言相勸','轉身回去','另找出路']],
[6,'城門事件令曹操十分＿＿。','憤怒',['高興','妒忌','擔心']],
[7,'楊修替曹植作咗十多條＿＿。','答教',['奏章','詩詞','軍令']],
[7,'曹操憤怒地說：「＿＿」','匹夫安敢欺我耶！',['汝怎敢造言亂我軍心！','雞肋，雞肋！','丞相非在夢中']],
[7,'答教事件令曹操萌生＿＿。','殺意',['歡喜','後悔','退兵之心']],
[1,'由軍營出發，下一站係邊度？','過渡句',['園門','一合酥','鄴城門']],
[7,'最後一站係邊度？','答教書案',['鄴城門','吳質大竹篋','過渡句']],
[5,'邊一站出現「大竹篋」？','吳質大竹篋',['一合酥','鄴城門','園門']],
]
qs='var QS=[\n'+',\n'.join('[%d,%r,%r,%r]'%(a,b,c,d) for a,b,c,d in QS)+'\n];\n'
# python repr uses single quotes with unicode OK
s=cut(s,"var STOPS=[","var N=STOPS.length",STOPS)
s=cut(s,"function b1(g){","var BUILD=[b1,b2,b3,b4,b5,b6,b7,b8];",BUILD,True)
s=cut(s,"var QS=[","var QN=10",qs)
s=s.replace('<title>颱風記憶路線</title>','<title>楊修之死 記憶路線</title>')
s=s.replace('<span class="t">颱風</span><span class="s">內容分析 · 記憶路線</span>','<span class="t">楊修之死</span><span class="s">內容分析 · 記憶路線</span>')
s=s.replace('<p class="qk">颱風問答挑戰</p>','<p class="qk">楊修之死問答挑戰</p>')
s=s.replace('<li>按答啱幾多題，掛起風球</li>','<li>按答啱幾多題，官階愈升愈高</li>')
s=s.replace('八個地點，跟着作者由樓下行到大街。點一站就會飛過去。','八個地點，跟着楊修同曹操嘅故事行一次。點一站就會飛過去。')
s=s.replace("rain.visible=!ov;","rain.visible=false;")
s=s.replace("typhoonBest","yxBest")
s=s.replace("var lv=r>=10?['十號','全對！你就係颱風專家']:r>=9?['九號','幾乎滿分，好叻']:r>=7?['八號','好穩陣，再接再厲']:r>=5?['三號','仲差少少，睇多一次路線']:['一號','由第一站慢慢行返一次'];","var lv=r>=10?['丞相','全對！你就係曹操身邊最強謀士']:r>=9?['軍師','幾乎滿分，好叻']:r>=7?['主簿','好穩陣，再接再厲']:r>=5?['士兵','仲差少少，睇多一次路線']:['新兵','由第一站慢慢行返一次'];")
s=s.replace("$('qlv').textContent=lv[0]+'風球';","$('qlv').textContent=lv[0];")
s=s.replace('href="../part-c/"','href="../part-c/"')
import os; os.makedirs(ROOT+'yx-3d',exist_ok=True)
open(DST,'w',encoding='utf-8').write(s)
print('ok', 'typhoon' in s, s.count('風球'))
