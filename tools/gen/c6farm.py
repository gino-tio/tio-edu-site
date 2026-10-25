# 3D "Farm Island" for Geography Food Problems (Three.js r128 from cdnjs, no Blender assets, all procedural).
# Executed once per language by content4.py (LANG='zh'/'en'); writes works[/en]/geo-farm-3d/index.html
import json
def FJ(): pass
_K=lambda t:'<span class="k">%s</span>'%t
def _p(t): return '<p>'+t+'</p>'
STOPS=[
 dict(id='overview',name=T('農場島','Farm Island'),seg='Unit 1-3',hook=T('撳地圖上嘅數字，逐個地方睇','Tap the numbers to visit each part'),
  html=_p(T('呢個島係一個 <span class="k">farming system 農業系統</span>：自然投入同人文投入入面，經過 processes，變成 outputs。','This island is a <span class="k">farming system</span>: physical and cultural inputs go through processes and become outputs.'))+
       _p(T('左邊係大農場 <b>Farm A</b>，右邊係細農場 <b>Farm B</b>。用手指拖動轉視角，兩隻手指放大縮細。圖唔係按比例。','Big <b>Farm A</b> is on the left and small <b>Farm B</b> on the right. Drag to turn, pinch to zoom. The picture is not to scale.'))+
       _p(T('玩熟之後撳「挑戰」，喺島上撳出答案。','When you are ready, press “Challenge” and tap the answers on the island.'))),
 dict(id='phys',name=T('自然投入','Physical inputs'),seg='Unit 1',hook=T('口訣：日、溫、雨、種、地、泥','Sun, temperature, rain, seeds, land, soil'),
  html=_p(T('<b>Physical inputs 自然投入</b>（課本 6 樣）：','<b>Physical inputs</b> (6 in the textbook):'))+
       _p(_K('sunlight')+' · '+_K('air temperature')+' · '+_K('rainfall')+' · '+_K('seeds')+' · '+_K('land')+' · '+_K('soil nutrients'))+
       _p(T('太陽、雨雲、泥土同種子都喺呢度。大自然提供，唔係人造。','The sun, rain cloud, soil and seeds are here. Nature provides them; people do not make them.'))),
 dict(id='cult',name=T('人文投入','Cultural inputs'),seg='Unit 1',hook=T('口訣：錢、肥、藥、技、人、水、機','Capital, fertilizers, pesticides, technology, labour, irrigation, machines'),
  html=_p(T('<b>Cultural inputs 人文投入</b>（課本 7 樣）：','<b>Cultural inputs</b> (7 in the textbook):'))+
       _p(_K('capital')+' · '+_K('fertilizers')+' · '+_K('pesticides')+' · '+_K('technology')+' · '+_K('labour')+' · '+_K('irrigation system')+' · '+_K('machines'))+
       _p(T('拖拉機、肥料袋、噴藥桶、水泵、錢袋同農夫，都係人帶嚟農場嘅投入。','The tractor, fertilizer bags, sprayer, pump, money bag and farmers are all brought in by people.'))),
 dict(id='proc',name=T('過程','Processes'),seg='Unit 1',hook=T('口訣：犁、種、灌、施、除、收','Plough, seed, irrigate, fertilize, weed, harvest'),
  html=_p(T('<b>Processes 過程</b>：農夫對 inputs 做嘅工作。','<b>Processes</b>: the work farmers do with the inputs.'))+
       _p(_K('ploughing')+' → '+_K('seeding')+' → '+_K('irrigating')+' → '+_K('fertilizing')+' → '+_K('weeding')+' → '+_K('harvesting'))+
       _p(T('2024-25 QE：兩張相共同嘅過程 = harvesting。','2024-25 QE: the process shown in both photos = harvesting.'))),
 dict(id='useful',name=T('有用產出同市場','Useful outputs and market'),seg='Unit 1',hook=T('口訣：農產品 → 市場 → 現金 → 反饋','Produce → market → cash → feedback'),
  html=_p(T('<b>Useful outputs 有用產出</b>：','<b>Useful outputs</b>: ')+_K('crops')+' · '+_K('meat')+' · '+_K('milk')+' · '+_K('wool'))+
       _p(T('拎去 <b>market</b> 賣，得到 <b>cash</b>。呢啲 cash 再用嚟買 cultural inputs，叫 <span class="k">feedback 反饋</span>（島上黃色小球由市場流返去農場）。','Sold at the <b>market</b> for <b>cash</b>. The cash buys more cultural inputs: <span class="k">feedback</span> (the yellow balls flow from the market back to the farm).'))+
       _p(T('<b>Cash crop</b> = 種嚟出售；<b>subsistence crop</b> = 種嚟自己食。','<b>Cash crop</b> = grown for sale; <b>subsistence crop</b> = grown for the farmer’s own food.'))),
 dict(id='useless',name=T('無用產出','Useless outputs'),seg='Unit 1',hook=T('口訣：糞、禾稈、污染','Animal waste, crop residues, pollutants'),
  html=_p(T('<b>Useless outputs 無用產出</b>：','<b>Useless outputs</b>: ')+_K('animal waste')+' · '+_K('crop residues')+' · '+_K('pollutants'))+
       _p(T('糞堆、禾稈堆同黑煙都喺呢度。','The manure heap, straw pile and black smoke are here.'))+
       _p(T('2025-26 UT：dairy farm 嘅 useless output = animal waste（milk、meat 係 useful）。','2025-26 UT: the useless output of a dairy farm = animal waste (milk and meat are useful).'))),
 dict(id='farmB',name=T('Farm B（細農場）','Farm B (small farm)'),seg='Unit 2',hook=T('Intensive · Arable · Subsistence · Low-tech','Intensive · Arable · Subsistence · Low-tech'),
  html=_p(T('6 公頃，<b>12</b> 個農民，用人力同水牛，種稻，主要自己食。','6 ha with <b>12</b> farmers, hand labour and a buffalo, growing rice mainly for the family.'))+
       _p(_K('Intensive')+' · '+_K('Arable')+' · '+_K('Subsistence')+' · '+_K('Low-technology'))+
       _p(T('Farmers per unit of land = 12 ÷ 6 = <b>2</b>（每公頃）。例子：印尼稻米（人手收割）。','Farmers per unit of land = 12 ÷ 6 = <b>2</b> per hectare. Example: rice in Indonesia (harvested by hand).'))),
 dict(id='farmA',name=T('Farm A（大農場）','Farm A (big farm)'),seg='Unit 2',hook=T('Extensive · Pastoral · Commercial · High-tech','Extensive · Pastoral · Commercial · High-tech'),
  html=_p(T('300 公頃，只有 <b>3</b> 個農民，用大型機器，養牲畜，主要出售。','300 ha with only <b>3</b> farmers, large machines and livestock, mainly for sale.'))+
       _p(_K('Extensive')+' · '+_K('Pastoral')+' · '+_K('Commercial')+' · '+_K('High-technology'))+
       _p(T('300 公頃 × 0.01 = <b>3</b> 個農民（X = 3）。例子：紐西蘭乳牛、美國中部小麥（大型聯合收割機）。','300 ha × 0.01 = <b>3</b> farmers (X = 3). Examples: dairy farming in New Zealand, wheat in central USA (combine harvester).'))),
 dict(id='cmp',name=T('比較兩個農場','Compare the two farms'),seg='Unit 2',hook=T('每單位土地嘅投入多定少？','Large or small inputs per unit of land?'),
  html='<table class="tb"><tr><th></th><th>Farm A</th><th>Farm B</th></tr>'
       '<tr><td>'+T('投入','Inputs per land')+'</td><td>Extensive</td><td>Intensive</td></tr>'
       '<tr><td>'+T('產出','Output')+'</td><td>Pastoral</td><td>Arable</td></tr>'
       '<tr><td>'+T('用途','Use')+'</td><td>Commercial</td><td>Subsistence</td></tr>'
       '<tr><td>'+T('技術','Technology')+'</td><td>High</td><td>Low</td></tr>'
       '<tr><td>'+T('農場面積','Farm size')+'</td><td>300 ha</td><td>6 ha</td></tr>'
       '<tr><td>'+T('農民','Farmers')+'</td><td>3</td><td>12</td></tr></table>'+
       _p(_K('Farmers per unit of land = number of farmers ÷ farm size'))+
       _p(T('⚠ 老撾高地稻米：課本 Table 4 剔 extensive，但 2025-26 統測標準答案係 labour input per unit area = High（intensive）。以學校標準答案為準。','⚠ Upland rice in Laos: textbook Table 4 ticks extensive, but the 2025-26 UT marking scheme says labour input per unit area = High (intensive). Follow the school’s marking scheme.')))]
TAGNAME={'phys':T('自然投入','a physical input'),'cult':T('人文投入','a cultural input'),'proc':T('農業過程','a farming process'),'useful':T('有用產出','a useful output'),'useless':T('無用產出','a useless output'),'market':T('市場','the market'),'farmA':'Farm A','farmB':'Farm B'}
QS=[
 ('phys',T('撳一樣<b>自然投入</b>（太陽、雨、泥土、種子…）','Tap a <b>physical input</b> (sun, rain, soil, seeds…)')),
 ('cult',T('撳一樣<b>人文投入</b>（機器、肥料、農夫、水泵…）','Tap a <b>cultural input</b> (machine, fertilizer, farmer, pump…)')),
 ('market',T('農夫喺邊度賣農產品賺 <b>cash</b>？','Where does the farmer sell produce to earn <b>cash</b>?')),
 ('useful',T('撳一樣<b>有用產出</b>（農作物、牛奶…）','Tap a <b>useful output</b> (crops, milk…)')),
 ('useless',T('撳一樣<b>無用產出</b>（糞、禾稈、污染）','Tap a <b>useless output</b> (waste, straw, pollution)')),
 ('farmB',T('邊個係 <b>intensive</b> 農場？（細地、多人手）','Which is the <b>intensive</b> farm? (small land, many workers)')),
 ('farmA',T('邊個係 <b>extensive</b> 農場？（大地、少人手）','Which is the <b>extensive</b> farm? (large land, few workers)')),
 ('proc',T('撳一樣<b>農業過程</b>嘅工具（犁、種子、灑水壺、鋤、鐮刀）','Tap a <b>farming process</b> tool (plough, seeds, watering can, hoe, sickle)')),
 ('farmA',T('邊個農場主要<b>養牲畜</b>（pastoral）？','Which farm is mainly <b>pastoral</b> (rearing livestock)?')),
 ('farmB',T('邊個農場主要<b>自給自足</b>（subsistence）？','Which farm is mainly <b>subsistence</b> (for the family)?')),
 ('farmA',T('邊個農場係 <b>high-technology</b>？','Which farm is <b>high-technology</b>?')),
 ('farmB',T('邊個農場喺 6 公頃地上有 <b>12</b> 個農民？','Which farm has <b>12</b> farmers on 6 hectares?'))]
TILES=[
 ('phys','☀️','sunlight'),('phys','🌡️','air temperature'),('phys','🌧️','rainfall'),('phys','🌱','seeds'),('phys','🟫','land'),('phys','🧱','soil nutrients'),
 ('cult','💰','capital'),('cult','🧪','fertilizers'),('cult','☠️','pesticides'),('cult','💻','technology'),('cult','🧑‍🌾','labour'),('cult','💧','irrigation system'),('cult','🚜','machines'),
 ('proc','⛏️','ploughing'),('proc','🌰','seeding'),('proc','🚿','irrigating'),('proc','🧴','fertilizing'),('proc','🪓','weeding'),('proc','🌾','harvesting'),
 ('useful','🥬','crops'),('useful','🥩','meat'),('useful','🥛','milk'),('useful','🧶','wool'),('market','🏪','market'),
 ('useless','💩','animal waste'),('useless','🌾','crop residues'),('useless','🏭','pollutants'),
 ('farmA','🐄','Farm A'),('farmB','🌾','Farm B')]
TGROUP=[('phys',T('自然投入 Physical inputs','Physical inputs'),['phys']),('cult',T('人文投入 Cultural inputs','Cultural inputs'),['cult']),('proc',T('過程 Processes','Processes'),['proc']),('useful',T('有用產出 Useful outputs','Useful outputs'),['useful','market']),('useless',T('無用產出 Useless outputs','Useless outputs'),['useless']),('farms',T('兩個農場 The two farms','The two farms'),['farmA','farmB'])]
UI=dict(back=T('‹ 食物問題','‹ Food Problems'),title=T('農場島','Farm Island'),sub=T('3D 溫習 · Food Problems Unit 1-3','3D revision · Food Problems Units 1-3'),
 prev=T('上一個','Previous'),next=T('下一個','Next'),chal=T('挑戰','Challenge'),to2d=T('2D 版','2D view'),to3d=T('3D 版','3D view'),
 ovbtn=T('全島','Whole island'),
 cstart=T('農場島挑戰','Farm Island challenge'),chead=T('喺島上撳出答案','Tap the answers on the island'),
 crules=[T('一共 8 題，睇到問題就喺島上（或者 2D 版）撳答案','8 questions: tap the answer on the island (or in the 2D view)'),T('計時可以開或者閂','The timer can be switched on or off'),T('答錯會顯示啱嘅位置','A wrong answer shows you the right place')],
 timer=T('計時','Timer'),on=T('開','On'),off=T('關','Off'),go=T('開始','Start'),best=T('最佳分數','Best score'),
 secs=T('每題 20 秒，答得越快分數越高','20 seconds per question; faster answers score more'),nosecs=T('冇時間限制','No time limit'),
 right=T('✔ 啱！','✔ Correct!'),wrong=T('✘ 唔啱，你撳咗','✘ Not quite. You tapped'),nothing=T('呢度冇嘢，再試','Nothing there; try again'),timeup=T('⏰ 時間到','⏰ Time is up'),
 shown=T('啱嘅位置已經閃出嚟','The right place is flashing'),nextq=T('下一題','Next'),skip=T('跳過','Skip'),
 endh=T('挑戰完成','Challenge complete'),score=T('分數','Score'),ok=T('答啱','Correct'),again=T('再玩一次','Play again'),explore=T('返回探索','Back to exploring'),
 wgl=T('呢部機用唔到 3D，已轉做 2D 版。','3D is not available here, so the 2D view is shown.'),
 hint2d=T('撳一個項目睇解釋；挑戰時撳答案。','Tap an item to read about it; in the challenge, tap the answer.'),
 quiz=T('做選擇題 ›','Do the quiz ›'),qn=T('題','Question'))
DATA=dict(tagstop={'phys':1,'cult':2,'proc':3,'useful':4,'market':4,'useless':5,'farmB':6,'farmA':7},prio=['phys','cult','proc','useful','useless','market','farmB','farmA'],best='farm3dBest',views=[{"t": [0, 0, 0], "r": 30, "w": 31, "th": 0.5, "ph": 1.0}, {"t": [-3.6, 0.8, -6.6], "r": 10, "w": 10, "th": 0.35, "ph": 1.05}, {"t": [0.2, 0.7, 1.2], "r": 10, "w": 11, "th": 0.15, "ph": 1.0}, {"t": [0, 0.3, 5.6], "r": 9, "w": 10, "th": 0.0, "ph": 1.0}, {"t": [1, 0.8, 9.2], "r": 9, "w": 10, "th": 0.25, "ph": 1.0}, {"t": [-9, 0.6, 5.6], "r": 9, "w": 9, "th": -0.35, "ph": 1.0}, {"t": [7.6, 0.5, 1.6], "r": 11, "w": 12, "th": 0.55, "ph": 0.95}, {"t": [-7.2, 0.5, -0.5], "r": 12, "w": 13, "th": -0.55, "ph": 0.95}, {"t": [0, 0, 0], "r": 30, "w": 31, "th": 0.0, "ph": 0.7}],marks=[None, [-3.6, 3.4, -6.8], [0.4, 3.6, 0.6], [0, 2.8, 5.6], [0.5, 3.8, 9.8], [-9, 3.2, 5.8], [8, 3.4, 1.6], [-7.2, 4.4, -0.5], None],stops=STOPS,qs=QS,tiles=TILES,tgroup=TGROUP,ui=UI,tagname=TAGNAME,lang=LANG)
_TPL=open(HERE+'/c6farm.html',encoding='utf-8').read()
_h=_TPL.replace('__DATA__',json.dumps(DATA,ensure_ascii=False)).replace('__LANG__','en' if LANG=='en' else 'zh-HK')
_h=_h.replace('__TITLE__',T('農場島 3D 溫習 · 中二地理','Farm Island 3D · F.2 Geography')).replace('__ASSET__','../../assets/' if LANG=='en' else '../assets/')
_h=_h.replace('__BACK__','../geo-food/').replace('__QUIZ__','../geo-food/')
os.makedirs(ROOT+'geo-farm-3d',exist_ok=True)
open(ROOT+'geo-farm-3d/index.html','w',encoding='utf-8').write(_h)
