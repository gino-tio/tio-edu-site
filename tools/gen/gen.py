import json,os
import os
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.normpath(os.path.join(HERE,'..','..','works'))+'/'
def K(t): return '<span class="k">%s</span>'%t
def item(id,h,body,cls=''):
    return '<div class="item %s" id="%s"><h3>%s</h3>%s</div>'%(cls,id,h,body)
def P(t): return '<p>%s</p>'%t
def EG(t): return '<p class="eg">%s</p>'%t
def Q(t): return '<p class="eg" style="border:0;margin:0;padding:0">%s</p>'%t

def page(folder,title,sub,art,tabs,panes,js,scope=False,back=('../part-c/','丙部'),bar='楊修之死',pfx='楊修之死 '):
    tabhtml=''.join('<button role="tab" data-pane="%s" aria-selected="%s">%s</button>'%(pid,'true' if i==0 else 'false',name) for i,(pid,name) in enumerate(tabs))
    panehtml=''
    for i,(pid,html) in enumerate(panes):
        panehtml+='<section id="%s"%s>%s</section>\n'%(pid,'' if i==0 else ' hidden',html)
    out='''<!doctype html>
<html lang="zh-HK">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>楊修之死 %s</title>
<meta name="description" content="《楊修之死》%s溫習。">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Huninn&display=swap">
<link rel="stylesheet" href="../assets/base.css">
<script src="../assets/theme.js"></script>
</head>
<body>
<div class="wrap">
  <div class="bar"><a href="../part-c/">‹ 丙部</a><b>楊修之死</b></div>
  <h1>%s</h1>
  <p class="sub">%s</p>
  <div data-art="%s"></div>
  <nav class="tabs" id="tabs" aria-label="溫習方式">%s</nav>
%s</div>
<script src="../assets/art.js"></script>
<script src="../assets/shared.js"></script>
<script>
(function(){
  var show=TY.tabs(document.getElementById('tabs'));
%s%s
})();
</script>
</body>
</html>
'''%(title,title,title,sub,art,tabhtml,panehtml,('  TY.scopeInit();\n' if scope else ''),js)
    out=out.replace('<a href="../part-c/">‹ 丙部</a><b>楊修之死</b>','<a href="%s">‹ %s</a><b>%s</b>'%(back[0],back[1],bar)).replace('<title>楊修之死 ','<title>'+pfx)
    os.makedirs(ROOT+folder,exist_ok=True)
    open(ROOT+folder+'/index.html','w',encoding='utf-8').write(out)

def refpane(inner,note='黃色字就係要背嘅答案'):
    return '<div class="row"><span>%s</span><button class="chip" id="mk" aria-pressed="false">遮住答案</button></div>\n<div id="refbox">%s</div>'%(note,inner)

RANK="rank:function(r,n){return r>=n?['十號風球','全對！背得好熟']:r>=n*0.9?['九號風球','幾乎滿分']:r>=n*0.7?['八號風球','好穩陣']:r>=n*0.5?['三號風球','仲差少少，睇多次重點']:['一號風球','返去重點睇返先']},"
def tfjs(key,rows,tagmap,count):
    qs=json.dumps([[r[0],1 if r[1] else 0,r[2],r[3]]+([1] if len(r)>4 and r[4] else []) for r in rows],ensure_ascii=False)
    return '''  var T=%s;
  if(TY.scopeOn()) T=T.filter(function(t){return !t[4]});
  var QS=T.map(function(t){return {q:t[0],opts:['對','錯'],a:t[1]?0:1,tag:t[2],note:t[3]}});
  var tagPane=%s;
  TY.quiz(document.getElementById('tfroot'),{
    key:'%s',mode:'tf',time:12,count:%d,
    kicker:'對錯快答',title:'%d 句說話，判斷對定錯',
    rules:['每句 12 秒，撳「對」或「錯」','答得越快分數越高','連續答啱有額外加分'],
    questions:QS,
    %s
    onReview:function(tag){show('p-ref');var id=tagPane[tag];setTimeout(function(){var el=document.getElementById(id);if(el)el.scrollIntoView({behavior:'smooth',block:'start'})},60)}
  });
'''%(qs,json.dumps(tagmap,ensure_ascii=False),key,count,count,RANK)
def mcqjs(key,rows,tagmap,count,title):
    qs=json.dumps(rows,ensure_ascii=False)
    return '''  var M=%s;
  var QS2=M.map(function(m){return {q:m[0],opts:m[1],a:m[2],tag:m[3],note:m[4],h:m[5]||0}});
  var tagPane2=%s;
  TY.quiz(document.getElementById('mcqroot'),{
    key:'%s',mode:'mcq',time:25,count:%d,
    kicker:'選擇題',title:'%s',
    rules:['每題 25 秒','答得越快分數越高','錯咗會話你知係邊一題要溫習'],
    questions:QS2,
    %s
    onReview:function(tag){show('p-ref');var id=tagPane2[tag];setTimeout(function(){var el=document.getElementById(id);if(el)el.scrollIntoView({behavior:'smooth',block:'start'})},60)}
  });
'''%(qs,json.dumps(tagmap,ensure_ascii=False),key,count,title,RANK)
def filljs(fq):
    return '  var FQ=%s;\n  if(TY.scopeOn()) FQ=FQ.filter(function(q){return !q.o});\n  TY.fill(document.getElementById("fills"),FQ);\n'%json.dumps(fq,ensure_ascii=False)
def matchjs(sets):
    return '  TY.match(document.getElementById("matchroot"),{sets:%s});\n'%json.dumps(sets,ensure_ascii=False)
MASK="  TY.mask(document.getElementById('mk'),document.getElementById('refbox'));\n"
FILLPANE='<p class="sub">喺空格入面打字，撳「檢查」睇對唔對。唔肯定可以撳「提示」。</p><div id="fills"></div>'
exec(open(HERE+'/content.py',encoding='utf-8').read())
exec(open(HERE+'/content2.py',encoding='utf-8').read())
exec(open(HERE+'/content3.py',encoding='utf-8').read())
exec(open(HERE+'/content4.py',encoding='utf-8').read())
