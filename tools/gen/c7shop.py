# 3D "Shopping Street" for English Unit 1 (Three.js, procedural). Executed per language; writes works[/en]/eng-shop-3d/index.html
import json
_V={}
for _t,_L in VOC:
    for _w,_p,_m in _L: _V[_w]=_m
def _p(t): return '<p>'+t+'</p>'
def _wt(words):
    return '<table class="tb"><tr><th>Word</th><th>Meaning</th></tr>'+''.join('<tr><td><b>%s</b></td><td>%s</td></tr>'%(w,_V[w]) for w in words)+'</table>'
SHOPROWS=[('confectioner',T('糖果店','sweets and chocolate')),('florist’s',T('花店','flowers and bouquets')),('antique shop',T('古董店：舊但保存得好嘅貴重物品','old but well-preserved valuable things')),
 ('optician’s',T('眼鏡店','glasses and contact lenses')),('pharmacy',T('藥房','medicine and plasters')),('cosmetics shop',T('化妝品店','lipstick and foundation')),
 ('electronics shop',T('電器店','headphones and gadgets')),('jeweller’s',T('珠寶店','necklaces and earrings')),('boutique',T('精品服裝店','small shop selling fashionable clothes'))]
STOPS=[
 dict(id='overview',name=T('購物街','Shopping Street'),seg='Unit 1',hook=T('撳數字去逛街，學詞語','Tap the numbers to learn the words'),
  html=_p(T('呢個島係 Unit 1 <span class="k">Why do we shop?</span> 嘅世界：九間店、網購同 big data、<span class="k">Handcrafted!</span> 市集。','This island is the world of Unit 1 <span class="k">Why do we shop?</span>: nine shops, online shopping and big data, and the <span class="k">Handcrafted!</span> market.'))+
       _p(T('拖動轉視角，兩隻手指縮放。撳島上嘅嘢可以睇詞語解釋（解釋跟學校 Glossary）。','Drag to turn and pinch to zoom. Tap things on the island to read the word meanings (from the school glossary).'))+
       _p(T('撳「挑戰」：睇英文解釋，喺島上撳出對應嘅嘢。','Press “Challenge”: read an English meaning and tap the matching thing on the island.'))),
 dict(id='shops',name=T('九種店舖','Nine types of shops'),seg=T('Warming up','Warming up'),hook=T('點樣分：賣咩？','What does each shop sell?'),
  html='<table class="tb"><tr><th>Shop</th><th>'+T('賣咩','Sells')+'</th></tr>'+''.join('<tr><td><b>%s</b></td><td>%s</td></tr>'%(a,b) for a,b in SHOPROWS)+'</table>'+
       _p(T('Text 1 例子：an electronics shop、a jeweller’s、a confectioner、a boutique、an online pharmacy、a cosmetics shop、a florist’s。','Text 1 examples: an electronics shop, a jeweller’s, a confectioner, a boutique, an online pharmacy, a cosmetics shop, a florist’s.'))),
 dict(id='online',name=T('網購同 big data','Online shopping and big data'),seg='Text 1 · p.4-5',hook=T('實體店 vs 網店；數據點樣用','Bricks-and-mortar vs online; how data is used'),
  html=_wt(['bricks-and-mortar','embrace','customize','big data','formulate'])),
 dict(id='mkt',name=T('針對性行銷','Targeted marketing'),seg='Text 1 · para 3',hook=T('Generic 電郵 vs targeted 電郵','Generic emails vs targeted emails'),
  html=_p(T('金色電郵飛去 boutique（targeted）；灰色電郵四散（generic）。','Gold emails fly to the boutique (targeted); grey emails scatter everywhere (generic).'))+
       _wt(['advertising','generic','targeted','individualized','personalized','on-trend','dietary supplement','coincide with'])),
 dict(id='exp',name=T('顧客體驗','Customer experience'),seg='Text 1 · para 4-5',hook=T('暢銷貨品放喺顯眼位置','Bestsellers in a prominent position'),
  html=_wt(['optimize','cumbersome','responsive','bestselling','prominent','lo and behold'])),
 dict(id='craft',name=T('Handcrafted! 市集','The Handcrafted! market'),seg='Text 2 · p.8-9',hook=T('手作、議價、特價','Handmade goods, haggling, special offers'),
  html=_wt(['handcrafted','artisan','sustainable','source','bargain','deal','haggle','vendor','tag','special offer'])),
 dict(id='stalls',name=T('攤位同古物','Stalls and vintage'),seg='Text 2 · para 5',hook=T('Vintage、second-hand、shop around','Vintage, second-hand, shop around'),
  html=_wt(['stall','dealer','second-hand','vintage','shop around']))]
def _q(tag,text): return (tag,T('撳：','Tap: ')+'<b>'+text+'</b>')
QS=[_q('confectioner',T('糖果店（賣糖同朱古力）','the shop that sells sweets and chocolate')),
 _q('florist',T('花店（賣花束）','the shop that sells flowers and bouquets')),
 _q('antique',T('古董店（舊但保存得好嘅貴重物品）','the shop that sells old but well-preserved valuable things')),
 _q('optician',T('眼鏡店','the shop where you buy glasses and contact lenses')),
 _q('pharmacy',T('藥房','the shop that sells medicine and plasters')),
 _q('cosmetics',T('化妝品店','the shop that sells lipstick and foundation')),
 _q('electronics',T('電器店','the shop that sells headphones and electronic things')),
 _q('jeweller',T('珠寶店','the shop that sells necklaces and diamonds')),
 _q('boutique',T('精品服裝店','a small shop that sells fashionable clothes')),
 _q('bigdata',_V['big data']),_q('advertising',_V['advertising']),_q('customize',_V['customize']),_q('targeted',_V['targeted']),_q('generic',_V['generic']),
 _q('bestselling',_V['bestselling']),_q('artisan',_V['artisan']),_q('handcrafted',_V['handcrafted']),_q('haggle',_V['haggle']),_q('vendor',_V['vendor']),
 _q('tag',_V['tag']),_q('specialoffer',_V['special offer']),_q('bargain',_V['bargain']),_q('sustainable',_V['sustainable']),_q('stall',_V['stall']),
 _q('vintage',_V['vintage']),_q('secondhand',_V['second-hand']),_q('dealer',_V['dealer']),_q('shoparound',_V['shop around'])]
TAGNAME={'confectioner':'confectioner','florist':'florist’s','antique':'antique shop','optician':'optician’s','pharmacy':'pharmacy','cosmetics':'cosmetics shop','electronics':'electronics shop','jeweller':'jeweller’s','boutique':'boutique',
 'bigdata':'big data','advertising':'advertising','customize':'customize','targeted':'targeted','generic':'generic','bestselling':'bestselling','artisan':'artisan','handcrafted':'handcrafted','haggle':'haggle','vendor':'vendor','tag':'tag','specialoffer':'special offer','bargain':'bargain','sustainable':'sustainable','stall':'stall','vintage':'vintage','secondhand':'second-hand','dealer':'dealer','shoparound':'shop around'}
TILES=[('confectioner','🍭','confectioner'),('florist','💐','florist’s'),('antique','🏺','antique shop'),('optician','👓','optician’s'),('pharmacy','💊','pharmacy'),('cosmetics','💄','cosmetics shop'),('electronics','🎧','electronics shop'),('jeweller','💎','jeweller’s'),('boutique','👗','boutique'),
 ('bigdata','🗄️','big data'),('customize','👟','customize'),('advertising','📢','advertising'),('targeted','📧','targeted'),('generic','✉️','generic'),('bestselling','📚','bestselling'),
 ('artisan','🧑‍🎨','artisan'),('handcrafted','🏺','handcrafted'),('haggle','🤝','haggle'),('vendor','🧑‍🍳','vendor'),('tag','🏷️','tag'),('specialoffer','🎁','special offer'),('bargain','💸','bargain'),('sustainable','♻️','sustainable'),
 ('stall','🏪','stall'),('vintage','📻','vintage'),('secondhand','🧥','second-hand'),('dealer','🧑‍💼','dealer'),('shoparound','🔍','shop around')]
_shops=['confectioner','florist','antique','optician','pharmacy','cosmetics','electronics','jeweller','boutique']
TGROUP=[('shops',T('九種店舖 Shop types','Shop types'),_shops),('online',T('網購 Online shopping','Online shopping'),['bigdata','customize']),('mkt',T('行銷 Marketing','Marketing'),['advertising','targeted','generic']),
 ('exp',T('顧客體驗 Customer experience','Customer experience'),['bestselling']),('craft',T('Handcrafted! 市集','The Handcrafted! market'),['artisan','handcrafted','haggle','vendor','tag','specialoffer','bargain','sustainable']),('stalls',T('攤位 Stalls','Stalls'),['stall','vintage','secondhand','dealer','shoparound'])]
TAGSTOP={}
for _t in _shops: TAGSTOP[_t]=1
for _t in ['bigdata','customize']: TAGSTOP[_t]=2
for _t in ['advertising','targeted','generic']: TAGSTOP[_t]=3
TAGSTOP['bestselling']=4
for _t in ['artisan','handcrafted','haggle','vendor','tag','specialoffer','bargain','sustainable']: TAGSTOP[_t]=5
for _t in ['stall','vintage','secondhand','dealer','shoparound']: TAGSTOP[_t]=6
VIEWS=[{'t':[0,0,0],'r':30,'w':31,'th':0.5,'ph':1.0},{'t':[0,1.2,-7.2],'r':12,'w':23,'th':0.0,'ph':1.05},{'t':[7.0,1.4,2.4],'r':10,'w':11,'th':0.3,'ph':1.0},{'t':[9.5,2.0,-0.5],'r':11,'w':13,'th':0.5,'ph':0.95},
 {'t':[3.6,1.0,-3.8],'r':8,'w':7,'th':0.1,'ph':1.0},{'t':[-5.9,1.0,3.6],'r':12,'w':14,'th':-0.15,'ph':1.0},{'t':[-5.5,1.2,2.8],'r':9,'w':8,'th':0.15,'ph':1.0}]
MARKS=[None,[0,5.0,-7.0],[8.8,5.2,2.4],[11.2,4.1,-2.6],[3.6,3.4,-3.8],[-8.2,3.8,2.8],[-5.5,3.8,2.4]]
UI=dict(back=T('‹ 英文','‹ English'),title=T('購物街','Shopping Street'),sub='',
 prev=T('上一個','Previous'),next=T('下一個','Next'),chal=T('挑戰','Challenge'),to2d=T('2D 版','2D view'),to3d=T('3D 版','3D view'),ovbtn=T('全島','Whole island'),
 cstart=T('購物街挑戰','Shopping Street challenge'),chead=T('睇英文解釋，喺島上撳出答案','Read the English meaning and tap the answer'),
 crules=[T('一共 8 題：睇解釋，喺島上（或者 2D 版）撳啱嘅嘢','8 questions: read the meaning and tap the right thing on the island (or in the 2D view)'),T('計時可以開或者閂','The timer can be switched on or off'),T('答錯會顯示啱嘅位置','A wrong answer shows you the right place')],
 timer=T('計時','Timer'),on=T('開','On'),off=T('關','Off'),go=T('開始','Start'),best=T('最佳分數','Best score'),
 secs=T('每題 20 秒，答得越快分數越高','20 seconds per question; faster answers score more'),nosecs=T('冇時間限制','No time limit'),
 right=T('✔ 啱！','✔ Correct!'),wrong=T('✘ 唔啱，你撳咗','✘ Not quite. You tapped'),nothing=T('呢度冇嘢，再試','Nothing there; try again'),timeup=T('⏰ 時間到','⏰ Time is up'),
 shown=T('啱嘅位置已經閃出嚟','The right place is flashing'),nextq=T('下一題','Next'),skip=T('跳過','Skip'),
 endh=T('挑戰完成','Challenge complete'),score=T('分數','Score'),ok=T('答啱','Correct'),again=T('再玩一次','Play again'),explore=T('返回探索','Back to exploring'),
 wgl=T('呢部機用唔到 3D，已轉做 2D 版。','3D is not available here, so the 2D view is shown.'),
 hint2d=T('撳一個項目睇解釋；挑戰時撳答案。','Tap an item to read about it; in the challenge, tap the answer.'),
 quiz=T('做詞彙練習 ›','Do the vocabulary practice ›'),qn=T('題','Question'))
DATA=dict(tagstop=TAGSTOP,prio=list(TAGNAME.keys()),best='shop3dBest',views=VIEWS,marks=MARKS,stops=STOPS,qs=QS,tiles=TILES,tgroup=TGROUP,ui=UI,tagname=TAGNAME,lang=LANG)
_TPL=open(HERE+'/c7shop.html',encoding='utf-8').read()
_h=_TPL.replace('__DATA__',json.dumps(DATA,ensure_ascii=False)).replace('__LANG__','en' if LANG=='en' else 'zh-HK')
_h=_h.replace('__TITLE__',T('購物街 3D 詞彙 · 中二英文','Shopping Street 3D · F.2 English')).replace('__ASSET__','../../assets/' if LANG=='en' else '../assets/')
_h=_h.replace('__BACK__','../eng/').replace('__QUIZ__','../eng-vocab/')
os.makedirs(ROOT+'eng-shop-3d',exist_ok=True)
open(ROOT+'eng-shop-3d/index.html','w',encoding='utf-8').write(_h)
