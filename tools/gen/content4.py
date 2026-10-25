# ---------- Geography F.2 ----------
LANG='zh'
def T(zh,en): return en if LANG=='en' else zh
RANK_EN="rank:function(r,n){return r>=n?['Signal 10','Perfect! Rock solid']:r>=n*0.9?['Signal 9','Almost perfect']:r>=n*0.7?['Signal 8','Solid']:r>=n*0.5?['Signal 3','Nearly there, review the notes']:['Signal 1','Go back to the notes first']},"
def mcq(key,M,tagmap,count,title):
    j=mcqjs(key,M,tagmap,count,title)
    if LANG=='en':
        j=j.replace(RANK,RANK_EN).replace("kicker:'選擇題'","kicker:'Multiple choice'").replace("rules:['每題 25 秒','答得越快分數越高','錯咗會話你知係邊一題要溫習']","rules:['25 seconds per question','Faster answers score more','Missed topics are listed at the end']")
    return j
def gpage(folder,title,sub,art,tabs,panes,js,back=('../geo/','Geography'),bar='Geography',desc=None):
    page(folder,title,sub,art,tabs,panes,js,False,back,bar,'')
    p=ROOT+folder+'/index.html'
    h=open(p,encoding='utf-8').read()
    h=h.replace('<script src="../assets/theme.js">','<meta name="ty-lang" content="bi">\n<script src="../assets/theme.js">',1)
    h=h.replace('content="《楊修之死》','content="').replace('<title>楊修之死 ','<title>')
    import re
    h=re.sub(r'<meta name="description" content="[^"]*"','<meta name="description" content="%s"'%(desc or T('中二地理上學期統一測驗溫習。','F.2 Geography first-term uniform test revision.')),h,1)
    if LANG=='en': h=postEN(h)
    open(p,'w',encoding='utf-8').write(h)
def postEN(h):
    return (h.replace('<html lang="zh-HK">','<html lang="en">').replace('"../assets/','"../../assets/')
            .replace('>遮住答案<','>Hide answers<').replace('aria-label="溫習方式"','aria-label="Study modes"'))
def gt(s): return s
def kv(en,zh): return '<b>%s</b>　<small>%s</small>'%(en,zh)
_ROOT0=ROOT
_body=open(HERE+'/c4body.py',encoding='utf-8').read()
for LANG in ['zh','en']:
    ROOT=_ROOT0+('en/' if LANG=='en' else '')
    exec(_body)
ROOT=_ROOT0
LANG='zh'
# ---------- English F.2 ----------
_body5=open(HERE+'/c5body.py',encoding='utf-8').read()
for LANG in ['zh','en']:
    ROOT=_ROOT0+('en/' if LANG=='en' else '')
    exec(_body5)
ROOT=_ROOT0
LANG='zh'
