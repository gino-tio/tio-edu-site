var islandG;
function sign(text,w,h,fg,bg){
  var c=document.createElement('canvas');c.width=256;c.height=Math.max(48,Math.round(256*h/w));var x=c.getContext('2d');
  x.fillStyle=bg;x.fillRect(0,0,c.width,c.height);x.lineWidth=8;x.strokeStyle='#3E3A39';x.strokeRect(4,4,c.width-8,c.height-8);
  var fs=Math.round(c.height*0.52);x.font='bold '+fs+'px "Huninn",sans-serif';
  while(x.measureText(text).width>c.width-26&&fs>10){fs-=2;x.font='bold '+fs+'px "Huninn",sans-serif'}
  x.fillStyle=fg;x.textAlign='center';x.textBaseline='middle';x.fillText(text,c.width/2,c.height/2+2);
  var m=new THREE.Mesh(new THREE.PlaneGeometry(w,h),new THREE.MeshBasicMaterial({map:new THREE.CanvasTexture(c)}));return m;
}
function torus(r,t,c,x,y,z,arc){var m=mesh(new THREE.TorusGeometry(r,t,6,18,arc||6.283),c,x,y,z);return m}
function stripedAwning(g,w,d,c1,c2,x,y,z,tilt){
  var n=6;for(var i=0;i<n;i++){var s=box(w/n,0.08,d,i%2?c1:c2,x-w/2+w/n*(i+0.5),y,z);s.rotation.x=tilt;g.add(s)}
}
function buildIsland(){
  var g=new THREE.Group();
  var geo=new THREE.CylinderGeometry(14.2,13.4,1.5,44,1);wob(geo,0.05);
  var top=new THREE.Mesh(geo,[M(0xA77F5A),M(0xA9D08E),M(0xA77F5A)]);top.position.y=-0.75;g.add(top);
  var sg=new THREE.CylinderGeometry(15.1,14.4,0.34,44,1);wob(sg,0.05);g.add(mesh(sg,0xF3E3B5,0,-0.2,0));
  var rk=mesh(flat(new THREE.ConeGeometry(12.5,8,10)),0x8B7766,0,-5.5,0);rk.rotation.x=Math.PI;g.add(rk);
  var pl=new THREE.Mesh(new THREE.CircleGeometry(11.6,48),new THREE.MeshBasicMaterial({color:0xD9CDB4}));pl.rotation.x=-Math.PI/2;pl.position.y=0.012;g.add(pl);
  var pl2=new THREE.Mesh(new THREE.CircleGeometry(11.0,48),new THREE.MeshBasicMaterial({color:0xE9E1D1}));pl2.rotation.x=-Math.PI/2;pl2.position.y=0.016;g.add(pl2);
  return g;
}
var SHOPS=[['confectioner',0xF4A6C0,'CONFECTIONER'],['florist',0x8FD19E,"FLORIST'S"],['antique',0xC59A6A,'ANTIQUE SHOP'],['optician',0x8EC5E8,"OPTICIAN'S"],['pharmacy',0xF4F7F2,'PHARMACY'],['cosmetics',0xD9A6E8,'COSMETICS'],['electronics',0xB4BBC4,'ELECTRONICS'],['jeweller',0x6F87C9,"JEWELLER'S"],['boutique',0xF6D27A,'BOUTIQUE']];
function shopIcon(k,g){
  var c=[0xE2796B,0xF6D27A,0x6FA8DC,0x7FBF6A,0xF2A497,0xB69CE0];
  if(k==='confectioner'){
    g.add(cyl(0.04,0.04,0.9,0xFFFCF6,-0.6,0.45,1.5,6));
    [0.34,0.26,0.18].forEach(function(r,i){var d=cyl(r,r,0.05+i*0.01,[0xF2A497,0xFFFCF6,0xE2796B][i],-0.6,1.05,1.5+i*0.03,18);d.rotation.x=Math.PI/2;g.add(d)});
    g.add(cyl(0.28,0.28,0.55,0xCDE8F2,0.55,0.3,1.5,12));for(var i=0;i<7;i++)g.add(sph(0.09,c[i%6],0.55+(i%3-1)*0.12,0.18+Math.floor(i/3)*0.17,1.5+((i*7)%3-1)*0.08));
  }else if(k==='florist'){
    [-0.55,0.5].forEach(function(x,j){g.add(cyl(0.26,0.2,0.4,0xB48C62,x,0.2,1.45,10));for(var i=0;i<5;i++){var fx=x+(i-2)*0.1;g.add(cyl(0.018,0.018,0.5,0x4E9E3E,fx,0.62,1.45,4));g.add(sph(0.1,c[(i+j)%6],fx,0.92+(i%2)*0.08,1.45))}});
  }else if(k==='antique'){
    g.add(box(0.7,0.5,0.5,0x8A6A4A,0,0.25,1.45));var w=cyl(0.36,0.36,0.08,0xFFFCF6,0,0.95,1.45,20);w.rotation.x=Math.PI/2;g.add(w);g.add(torus(0.36,0.04,0xE8C96A,0,0.95,1.46));
    g.add(box(0.04,0.26,0.02,0x3E3A39,0,1.04,1.5));g.add(box(0.2,0.04,0.02,0x3E3A39,0.08,0.95,1.5));g.add(cyl(0.05,0.05,0.12,0xE8C96A,0,1.36,1.45,8));
  }else if(k==='optician'){
    var gl=grp(0,3.55,0.6);gl.add(torus(0.34,0.06,0x3E3A39,-0.4,0,0));gl.add(torus(0.34,0.06,0x3E3A39,0.4,0,0));gl.add(box(0.2,0.06,0.06,0x3E3A39,0,0.05,0));g.add(gl);
    anims.push(function(t){gl.rotation.y=Math.sin(t*0.8)*0.3});
  }else if(k==='pharmacy'){
    var cr=grp(0,3.5,0.6);cr.add(glow(0.7,0.22,0.1,0x2EAE5A,0,0,0));cr.add(glow(0.22,0.7,0.1,0x2EAE5A,0,0,0));g.add(cr);
    g.add(cyl(0.14,0.14,0.4,0xF2A497,-0.5,0.2,1.5,10));g.add(cyl(0.1,0.1,0.1,0xFFFCF6,-0.5,0.45,1.5,10));g.add(box(0.36,0.1,0.18,0xE8D5B0,0.4,0.06,1.5));g.add(box(0.36,0.1,0.18,0xE8D5B0,0.45,0.17,1.5));
  }else if(k==='cosmetics'){
    var l=grp(0.5,0,1.5);l.add(cyl(0.16,0.16,0.35,0x3E3A39,0,0.18,0,10));l.add(cyl(0.12,0.12,0.4,0xE2796B,0,0.55,0,10));l.add(cone(0.12,0.3,0xD94A5E,0,0.9,0,8));l.scale.set(1.5,1.5,1.5);g.add(l);
    g.add(cyl(0.3,0.3,0.06,0xF4F7F2,-0.5,0.4,1.5,16));g.add(box(0.35,0.12,0.2,0xE8D5B0,-0.5,0.04,1.5));
  }else if(k==='electronics'){
    var hp=grp(0,3.5,0.6);hp.add(torus(0.4,0.06,0x3E3A39,0,0,0,3.14));[-0.4,0.4].forEach(function(x){hp.add(cyl(0.16,0.16,0.14,0x6FA8DC,x,-0.05,0,12))});hp.rotation.z=0;g.add(hp);
    anims.push(function(t){hp.rotation.y=Math.sin(t*0.9)*0.4});
    g.add(box(0.8,0.5,0.06,0x2B2F36,0,0.9,1.3));g.add(glow(0.7,0.4,0.06,0x8EC5E8,0,0.9,1.34));g.add(box(0.1,0.35,0.1,0x2B2F36,0,0.5,1.3));
  }else if(k==='jeweller'){
    var dm=new THREE.Mesh(flat(new THREE.OctahedronGeometry(0.42,0)),new THREE.MeshLambertMaterial({color:0xBFE9FF}));dm.position.set(0,3.45,0.6);dm.scale.set(1,1.3,1);g.add(dm);anims.push(function(t){dm.rotation.y=t*1.2});
    var nk=torus(0.3,0.03,0xE8C96A,0,0.95,1.35);g.add(nk);g.add(sph(0.08,0xE2796B,0,0.64,1.36));g.add(box(0.7,0.4,0.4,0x3C5C8C,0,0.2,1.4));
  }else if(k==='boutique'){
    var dr=grp(0,0,1.5);dr.add(cyl(0.05,0.05,1.0,0x3E3A39,0,0.5,0,6));dr.add(cone(0.42,0.9,0xE2796B,0,0.9,0,10));dr.add(sph(0.12,0xE3C3A0,0,1.5,0));dr.add(cyl(0.2,0.2,0.05,0x3E3A39,0,0.03,0,10));g.add(dr);
  }
}
function buildShops(){
  var g=grp(0,0,0);
  SHOPS.forEach(function(S,i){
    var x=-9.2+i*2.3,b=tag(grp(x,0,-7.2),S[0]);blob(b,0,0.2,1.9);
    b.add(box(2.05,2.2,1.8,S[1],0,1.1,0));b.add(box(2.25,0.2,2.0,0x6B5B4E,0,2.3,0));
    b.add(box(0.5,1.0,0.06,0x8A6A4A,-0.55,0.5,0.93));b.add(glow(0.7,0.65,0.06,0xFFF1B8,0.45,1.15,0.93));
    stripedAwning(b,2.2,0.85,0xFFFCF6,0xE2796B,0,1.78,1.18,-0.42);
    var sn=sign(S[2],2.0,0.5,'#3E3A39','#FFFCF6');sn.position.set(0,2.75,0.4);b.add(sn);b.add(box(0.05,0.5,0.05,0x3E3A39,-0.9,2.5,0.4));b.add(box(0.05,0.5,0.05,0x3E3A39,0.9,2.5,0.4));
    shopIcon(S[0],b);g.add(b);
  });
  return g;
}
function envelope(c,x,y,z){var e=grp(x,y,z);e.add(box(0.42,0.05,0.28,c,0,0,0));e.add(box(0.2,0.055,0.1,0xFFFCF6,0,0.005,0));return e}
function buildOnline(){
  var g=grp(0,0,0);
  // big data tower
  var tw=tag(grp(8.8,0,2.4),'bigdata');blob(tw,0,0,1.8);
  var lights=[];
  for(var i=0;i<5;i++){tw.add(box(1.5,0.5,1.1,i%2?0x3A4150:0x2B2F36,0,0.3+i*0.55,0));for(var k=0;k<4;k++){var l=glow(0.1,0.1,0.06,[0x7FFFB0,0xF6D27A,0x6FC3FF,0xF2A497][(i+k)%4],-0.5+k*0.24,0.3+i*0.55,0.57);tw.add(l);lights.push(l)}}
  tw.add(cyl(0.04,0.04,1.6,0x3E3A39,0.6,3.4,0,5));tw.add(sph(0.12,0xE2796B,0.6,4.2,0));
  var mon=grp(0,3.5,0);mon.add(box(1.7,0.95,0.08,0x2B2F36,0,0,0));var bars=[];[0.3,0.55,0.4,0.7,0.5].forEach(function(h,i){var b=glow(0.18,h,0.06,0x7FD3FF,-0.55+i*0.28,-0.3+h/2,0.06);mon.add(b);bars.push(b)});tw.add(mon);
  anims.push(function(t){bars.forEach(function(b,i){var s=0.6+0.4*Math.abs(Math.sin(t*1.2+i));b.scale.y=s});lights.forEach(function(l,i){l.visible=((Math.floor(t*3+i))%3)!==0})});
  g.add(tw);
  // sparkle dots flowing into the tower (data)
  var dots=[];for(var d=0;d<10;d++){var p=new THREE.Mesh(new THREE.SphereGeometry(0.1,8,6),new THREE.MeshBasicMaterial({color:0x7FD3FF}));tag(p,'bigdata');g.add(p);dots.push(p)}
  anims.push(function(t){dots.forEach(function(p,i){var u=((t*0.2+i/10)%1),a=i*0.63;p.position.set(8.8+Math.cos(a)*(5-u*4.4),0.5+u*2.4,2.4+Math.sin(a)*(5-u*4.4))})});
  // customize station
  var cu=tag(grp(5.3,0,2.4),'customize');blob(cu,0,0,1.4);cu.add(cyl(0.7,0.8,0.5,0xE8D5B0,0,0.25,0,14));
  var sh=grp(0,0.9,0);sh.add(box(1.1,0.22,0.45,0xF4F7F2,0,-0.15,0));sh.add(box(0.8,0.4,0.42,0xE2796B,0.15,0.08,0));sh.add(box(0.3,0.22,0.42,0xFFFCF6,-0.3,0.02,0));[0,1,2].forEach(function(i){sh.add(box(0.05,0.04,0.44,0xFFFCF6,0.0+i*0.15,0.3,0))});cu.add(sh);anims.push(function(t){sh.rotation.y=t*0.6;sh.children[1].material.color.setHex([0xE2796B,0x6FA8DC,0x7FBF6A,0xF6D27A][Math.floor(t*0.5)%4])});
  [0xE2796B,0x6FA8DC,0x7FBF6A,0xF6D27A,0xB69CE0].forEach(function(c,i){cu.add(box(0.28,0.28,0.28,c,-0.9+i*0.45,0.14,1.0))});
  g.add(cu);
  return g;
}
function buildMarketing(){
  var g=grp(0,0,0);
  // billboard
  var bb=tag(grp(11.2,0,-2.6),'advertising');blob(bb,0,0,1.8);bb.rotation.y=-0.5;
  bb.add(box(0.15,2.4,0.15,0x3E3A39,-1.3,1.2,0));bb.add(box(0.15,2.4,0.15,0x3E3A39,1.3,1.2,0));
  var bd=sign('SALE 50%',3.2,1.5,'#E2496B','#F6D27A');bd.position.set(0,2.6,0.1);bb.add(bd);var bd2=bd.clone();bd2.rotation.y=Math.PI;bd2.position.z=-0.1;bb.add(bd2);g.add(bb);
  // envelopes: targeted (gold) fly to the boutique, generic (grey) drift everywhere
  var tg=[];for(var i=0;i<4;i++){var e=tag(envelope(0xF2A497,0,0,0),'targeted');g.add(e);tg.push(e)}
  anims.push(function(t){tg.forEach(function(e,i){var u=((t*0.16+i/4)%1),a=[8.8,2.8,2.4],b=[9.2,1.6,-5.6];e.position.set(a[0]+(b[0]-a[0])*u,a[1]+(b[1]-a[1])*u+Math.sin(u*3.14)*3.2,a[2]+(b[2]-a[2])*u);e.rotation.y=u*6;e.rotation.z=Math.sin(u*9)*0.3})});
  var ge=[];for(var j=0;j<7;j++){var e=tag(envelope(0xB9C2C9,0,0,0),'generic');g.add(e);ge.push(e)}
  anims.push(function(t){ge.forEach(function(e,i){var u=((t*0.1+i/7)%1),a=i*0.9+1,r=1+u*10;e.position.set(8.8+Math.cos(a)*r*0.7,2.2-u*1.7+Math.sin(u*8+i)*0.3,2.4+Math.sin(a)*r*0.7);e.rotation.y=t+i;e.rotation.x=Math.sin(t*2+i)*0.4})});
  return g;
}
function buildExperience(){
  var g=grp(0,0,0);
  var sf=grp(3.6,0,-3.8);blob(sf,0,0,1.9);
  var fr=box(2.4,1.7,0.5,0x8A6A4A,0,0.85,0);sf.add(fr);sf.add(box(2.2,0.06,0.45,0x6B4E36,0,0.9,0.02));
  var cols=[0x6FA8DC,0x7FBF6A,0xB69CE0,0xF2A497,0xA8D3E6,0xF6D27A,0x8FD19E];
  for(var r=0;r<2;r++)for(var i=0;i<7;i++){var hh=0.5+((i*7+r*3)%4)*0.05;sf.add(box(0.26,hh,0.34,cols[(i+r)%7],-0.9+i*0.3,(r?0.98:0.1)+hh/2,0.12))}
  // bestselling book: bigger, golden, in a prominent spot on top
  var bk=tag(grp(0,1.8,0.1),'bestselling');bk.add(box(0.8,1.0,0.16,0xF6D27A,0,0.5,0));bk.add(box(0.7,0.9,0.18,0xE2796B,0,0.5,0.0));var st=grp(0,0.55,0.12);st.add(glow(0.4,0.12,0.04,0xFFFCF6,0,0,0));st.add(glow(0.12,0.4,0.04,0xFFFCF6,0,0,0));bk.add(st);
  var no1=sign('No.1',0.8,0.35,'#3E3A39','#F6D27A');no1.position.set(0,1.28,0.12);bk.add(no1);
  sf.add(bk);anims.push(function(t){bk.position.y=1.8+Math.sin(t*2)*0.06;st.rotation.z=t});
  g.add(sf);
  return g;
}
function person2(c,x,z,s){return person(c,x,z,false,s||1.1)}
function buildMarketStalls(){
  var g=grp(0,0,0);
  var pat=box(11.6,0.03,5.6,0xE8D9B8,-5.9,0.025,3.6);g.add(pat);
  var xs=[-10.3,-7.9,-5.5,-3.1,-0.7],z=2.4;
  function counter(i,col){
    var s=tag(grp(xs[i],0,z),'stall');blob(s,0,0,1.6);
    s.add(box(1.9,0.9,0.8,0xB48C62,0,0.45,0));s.add(box(2.0,0.08,0.9,0xE8D5B0,0,0.92,0));
    [[-0.95,-0.35],[0.95,-0.35]].forEach(function(p){s.add(box(0.07,2.2,0.07,0x8A6A4A,p[0],1.1,p[1]))});[[-0.95,0.4],[0.95,0.4]].forEach(function(p){s.add(box(0.07,1.9,0.07,0x8A6A4A,p[0],0.95,p[1]))});
    stripedAwning(s,2.2,1.2,0xFFFCF6,col,0,2.15,0.02,-0.3);
    g.add(s);return s;
  }
  var c0=[0x6FA8DC,0x7FBF6A,0xF2A497,0xB69CE0,0xF6D27A];
  for(var i=0;i<5;i++)counter(i,c0[i]);
  // S1: pottery + artisan
  var pots=tag(grp(xs[0],0,z),'handcrafted');[[-0.6,0.6],[0.0,0.5],[0.6,0.6]].forEach(function(p,j){pots.add(cyl(0.22+j*0.02,0.17,0.4+j*0.05,[0xE2796B,0x6FA8DC,0xF6D27A][j],p[0],1.15+j*0.02,0,12));pots.add(cyl(0.12,0.2,0.1,[0xE2796B,0x6FA8DC,0xF6D27A][j],p[0],1.4,0,12))});g.add(pots);
  var ar=tag(grp(xs[0]-0.1,0,z+1.5),'artisan');var wh=cyl(0.45,0.5,0.4,0xB48C62,0,0.2,0.0,14);ar.add(wh);var clay=cyl(0.2,0.25,0.35,0xE2796B,0,0.55,0,12);ar.add(clay);ar.add(person(0xF6D27A,-0.2,0.8,false,1.15));ar.add(box(0.5,0.12,0.2,0xE3C3A0,0,0.7,0.35));g.add(ar);anims.push(function(t){clay.rotation.y=t*3;clay.scale.y=1+Math.sin(t*1.5)*0.2});
  // S2: homeware, bargain, price tags
  var hw=grp(xs[1],0,z);hw.add(box(0.7,0.5,0.6,0xE8D5B0,-0.4,1.25,0));hw.add(cyl(0.25,0.3,0.45,0x7FBF6A,0.4,1.17,0,12));
  var ch=tag(grp(0,0,1.1),'handcrafted');ch.add(box(0.5,0.08,0.5,0xB48C62,0,0.5,0));[[-0.2,-0.2],[0.2,-0.2],[-0.2,0.2],[0.2,0.2]].forEach(function(p){ch.add(box(0.06,0.5,0.06,0xB48C62,p[0],0.25,p[1]))});ch.add(box(0.5,0.5,0.06,0xB48C62,0,0.8,-0.22));hw.add(ch);
  var bg=tag(grp(-0.4,1.5,0.25),'bargain');bg.add(box(0.6,0.34,0.05,0xE2496B,0,0,0));var pc=sign('-50%',0.55,0.28,'#FFFCF6','#E2496B');pc.position.z=0.03;bg.add(pc);hw.add(bg);
  g.add(hw);
  // S3: vintage / second-hand dealer
  var vt=tag(grp(xs[2],0,z),'vintage');var rad=box(0.7,0.4,0.3,0x8A6A4A,-0.5,1.15,0);vt.add(rad);vt.add(cyl(0.12,0.12,0.04,0xE8C96A,-0.65,1.15,0.17,10));vt.children[1].rotation.x=Math.PI/2;vt.add(cyl(0.02,0.02,0.4,0x3E3A39,-0.3,1.5,0,4));
  var ck=cyl(0.28,0.28,0.1,0xFFFCF6,0.4,1.4,0,18);ck.rotation.x=Math.PI/2;vt.add(ck);vt.add(torus(0.28,0.04,0xB48C62,0.4,1.4,0.0));vt.add(box(0.03,0.2,0.02,0x3E3A39,0.4,1.45,0.07));
  g.add(vt);
  var sh2=tag(grp(xs[2],0,z),'secondhand');sh2.add(box(0.5,0.3,0.4,0xB9C2C9,0.1,1.1,0.1));sh2.add(box(0.2,0.12,0.2,0x3E3A39,0.1,1.32,0.12));g.add(sh2);
  var dl=tag(grp(xs[2]+0.2,0,z-0.8),'dealer');dl.add(person(0xB69CE0,0,0,true,1.2));g.add(dl);
  // S4: special offer + sustainable bag
  var so=tag(grp(xs[3],0,z),'specialoffer');var ss=sign('FREE BAG',1.5,0.5,'#FFFCF6','#E2496B');ss.position.set(0,2.65,0.35);so.add(ss);var ss2=sign('SPEND $200',1.5,0.42,'#3E3A39','#F6D27A');ss2.position.set(0,3.15,0.35);so.add(ss2);g.add(so);
  var rb=tag(grp(xs[3],0,z),'sustainable');rb.add(box(0.5,0.5,0.22,0x7FBF6A,0,1.2,0.1));rb.add(torus(0.15,0.025,0x4E9E3E,0,1.5,0.1,3.14));var rc=sign('♻',0.3,0.3,'#FFFCF6','#4E9E3E');rc.position.set(0,1.2,0.23);rb.add(rc);rb.add(box(0.5,0.5,0.22,0x6FA8DC,0.7,1.2,0.1));g.add(rb);
  // S5: vendor with crafts
  var s5=grp(xs[4],0,z);var bs=tag(grp(0,0,0),'handcrafted');bs.add(cyl(0.3,0.22,0.3,0xD9B26F,-0.4,1.1,0,10));bs.add(cyl(0.26,0.2,0.28,0xE9CE7A,0.2,1.1,0.1,10));bs.add(box(0.4,0.3,0.4,0x8A6A4A,0.65,1.1,-0.1));s5.add(bs);g.add(s5);
  var vn=tag(grp(xs[4]-0.1,0,z-0.8),'vendor');vn.add(person(0xE2796B,0,0,false,1.2));g.add(vn);
  var vn2=tag(grp(xs[1]+0.3,0,z-0.8),'vendor');vn2.add(person(0x6FA8DC,0,0,false,1.2));g.add(vn2);
  // price tags (tag)
  [[xs[0]+0.5,1.55,z+0.45],[xs[1]-0.9,1.5,z+0.4],[xs[2]+0.95,1.55,z+0.4],[xs[4]+0.7,1.35,z+0.4]].forEach(function(p,i){var t=tag(grp(p[0],p[1],p[2]),'tag');t.add(box(0.3,0.2,0.03,0xFFFCF6,0,0,0));t.add(box(0.22,0.04,0.035,0xE2496B,0,0.03,0));t.add(cyl(0.01,0.01,0.2,0x3E3A39,0,0.2,0,3));g.add(t);anims.push(function(tm){t.rotation.z=Math.sin(tm*2+i)*0.18})});
  // haggle pair
  var hg=tag(grp(-8.4,0,5.2),'haggle');var cu=person(0x6FA8DC,-0.45,0,false,1.15),vd=person(0xE2796B,0.45,0,false,1.15);cu.rotation.y=Math.PI/2;vd.rotation.y=-Math.PI/2;hg.add(cu);hg.add(vd);
  var b1=sign('$ ?',0.6,0.4,'#3E3A39','#FFFCF6');b1.position.set(-0.45,1.9,0);hg.add(b1);var b2=sign('$$$',0.6,0.4,'#E2496B','#FFFCF6');b2.position.set(0.45,2.0,0);hg.add(b2);
  g.add(hg);anims.push(function(t){cu.position.y=Math.abs(Math.sin(t*2.4))*0.06;vd.position.y=Math.abs(Math.sin(t*2.4+1.5))*0.06;b1.visible=Math.floor(t*0.8)%2===0;b2.visible=!b1.visible});
  // shop around walker
  var sa=tag(grp(-5,0,5.4),'shoparound');sa.add(person(0xB69CE0,0,0,true,1.15));var lens=grp(0.0,2.0,0);lens.add(torus(0.17,0.03,0x3E3A39,0,0,0));lens.add(box(0.05,0.28,0.04,0x3E3A39,0.14,-0.2,0));sa.add(lens);g.add(sa);
  anims.push(function(t){var u=Math.sin(t*0.25);sa.position.x=-5.5+u*5;sa.rotation.y=Math.cos(t*0.25)>=0?Math.PI/2:-Math.PI/2;lens.rotation.z=Math.sin(t*3)*0.2});
  return g;
}
function buildScenery(){
  var g=new THREE.Group();
  for(var i=0;i<26;i++){var a=i/26*6.283+0.1,r=12.0+rnd(i)*0.9,x=Math.cos(a)*r,z=Math.sin(a)*r;if(z<-6.2&&Math.abs(x)<11)continue;if(i%3===0)tree(g,x,z,0.9+rnd(i)*0.4,i%2?0xD98F4E:undefined);else if(i%3===1)bush(g,x,z,1.1);else rock(g,x,z,1.0)}
  // lamp posts
  [[-4,-3],[4,-1],[-11,0],[11,5],[0,5.5],[-2.6,6.2]].forEach(function(p){var l=grp(p[0],0,p[1]);l.add(cyl(0.05,0.07,2.2,0x3E3A39,0,1.1,0,6));l.add(glow(0.28,0.28,0.28,0xFFE39A,0,2.3,0));g.add(l)});
  [[-1.4,-4.5,0],[1.4,-4.5,0]].forEach(function(p){var b=grp(p[0],0,p[1]);b.add(box(1.0,0.12,0.35,0x8A6A4A,0,0.4,0));b.add(box(0.08,0.4,0.3,0x6B4E36,-0.4,0.2,0));b.add(box(0.08,0.4,0.3,0x6B4E36,0.4,0.2,0));g.add(b)});
  [[-10.8,-3.4],[10.6,-5.2]].forEach(function(p){var pl=grp(p[0],0,p[1]);pl.add(box(0.6,0.4,0.6,0xB48C62,0,0.2,0));pl.add(sph(0.4,0x7FBF6A,0,0.7,0,1,0.9,1));g.add(pl)});
  [[22,18,0.4],[-24,-10,2.2]].forEach(function(b,i){var s=grp(b[0],-1,b[1]);s.rotation.y=b[2];s.add(box(2.2,0.45,0.8,0xFFFCF6,0,0.2,0));var sl=cone(0.8,2.6,0xF2A497,0,1.7,0,3);sl.scale.set(1,1,0.12);s.add(sl);s.add(cyl(0.04,0.04,2.8,0x3E3A39,0,1.6,0,5));g.add(s);anims.push(function(t){s.position.y=-0.85+Math.sin(t*1.2+i)*0.08;s.rotation.z=Math.sin(t*1.0+i)*0.06})});
  return g;
}
