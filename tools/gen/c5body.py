# English F.2 grammar pages (exam paper is in English; notes are English with zh glosses in the zh build)
import random
def G(en,zh): return en+('<br><small>'+zh+'</small>' if LANG=='zh' and zh else '')
def TB(head,rows):
    return '<table class="tb"><tr>'+''.join('<th>%s</th>'%h for h in head)+'</tr>'+''.join('<tr>'+''.join('<td>%s</td>'%c for c in r)+'</tr>' for r in rows)+'</table>'
EBACK=('../eng/','English')
def eng_page(folder,key,title,sub,art,notes,sets,fills,mcqs,tagprefix):
    ref=''.join(item('%s%d'%(tagprefix,i),'%d. %s'%(i+1,h),b,['','s2','s3','s4'][i%4]) for i,(h,b) in enumerate(notes))
    ref=refpane('<p class="sub">'+T('全部題目都係【AI 出題】，跟 Oxford English Forward 2A 同 Success in Grammar 2 嘅範圍；未對過課本。','All questions are AI-made for the syllabus. Not yet checked against Oxford English Forward 2A / Success in Grammar 2.')+'</p>'+ref,T('黃色字係重點，撳開睇','Highlighted text = key points. Tap to open'))
    rnd=random.Random(hash(key)%1000 if False else sum(map(ord,key)))
    M=[]
    for q,o,tg,note,*h in mcqs:
        idx=list(range(len(o)));rnd.shuffle(idx)
        row=[AIL+q,[o[j] for j in idx],idx.index(0),'%s%d'%(tagprefix,tg),T('答案：','Answer: ')+'<b>%s</b>　%s'%(o[0],note)]
        if h and h[0]: row.append(1)
        M.append(row)
    tagmap={m[3]:m[3] for m in M}
    fq=[{'t':t,'p':p,'b':b} for t,p,b in fills]
    sl=[{'name':n,'help':T('先撳左邊，再撳相配嘅右邊。','Tap a left item, then its match.'),'pairs':ps} for n,ps in sets]
    js=MASK+matchjs(sl)+filljs(fq)+mcq(key,M,tagmap,10,T('十條題，四揀一（包括挑戰題）','10 questions, 4 choices (with challenge questions)'))
    gpage(folder,title,sub,art,
      [('p-ref',T('重點速覽','Notes')),('p-match',T('配對遊戲','Match')),('p-fill',T('寫字填空','Fill in')),('p-mcq',T('選擇題','Quiz'))],
      [('p-ref',ref),('p-match','<div id="matchroot"></div>'),('p-fill',FILLPANE2),('p-mcq','<div id="mcqroot"></div>')],js,
      back=EBACK,bar='English',desc=T('中二英文上學期統一測驗文法溫習。','F.2 English first-term uniform test grammar revision.'))

# ---------- Unit 1 A/B: adjectives ----------
ADJN=[
('Comparative and superlative forms'+T(' 比較級同最高級',''),
 '<p>'+K('1 syllable: -er / -est　·　2+ syllables: more / most')+'</p>'+
 TB(['Rule','Adj.','Comparative','Superlative'],[
  ['1 syllable','tall','taller','the tallest'],
  ['ends in -e','large','larger','the largest'],
  ['double the consonant','big','bigger','the biggest'],
  ['consonant + y','happy','happier','the happiest'],
  ['2+ syllables','expensive','more expensive','the most expensive'],
  ['irregular','good','better','the best'],
  ['irregular','bad','worse','the worst'],
  ['irregular','far','farther / further','the farthest / furthest'],
  ['irregular','little','less','the least']])),
('Using comparatives and superlatives'+T(' 用法',''),
 '<p>'+K('comparative + than　·　the + superlative + in / of')+'</p>'+
 P(G('Compare <b>two</b> things: <b>Tom is taller than Ben.</b>','比較兩樣嘢用 comparative + than。'))+
 P(G('Compare <b>three or more</b>: <b>Tom is the tallest in the class. / the tallest of the three.</b>','三樣或以上用 the + superlative（in + 一個地方／組別；of + 一組人或物）。'))+
 P(G('Make it stronger or weaker with <b>much / far / a lot / a bit / slightly</b> + comparative: <b>far bigger</b>, <b>slightly cheaper</b>.','加強或減弱用 much／far／a lot／a bit／slightly。'))+
 P(G(K('Never')+' say <i>very bigger</i>, <i>more bigger</i> or <i>the more big</i>.','唔可以講 very bigger、more bigger。'))),
('Making comparisons'+T(' 作出比較',''),
 '<p>'+K('as … as　·　not as … as　·　less … than　·　the same … as　·　different from　·　similar to')+'</p>'+
 TB(['Pattern','Example','Meaning'],[
  ['as + adj + as','Lily is as tall as Amy.','equal'],
  ['not as + adj + as','The red bag is not as expensive as the blue bag.','red is cheaper'],
  ['less + adj + than','The red bag is less expensive than the blue bag.','same meaning as above'],
  ['the same + noun + as','Tom is the same age as Ben.','equal'],
  ['different from','My bag is different from yours.','not alike'],
  ['similar to','My bag is similar to yours.','almost alike'],
  ['twice as + adj + as','The new library is twice as big as the old one.','2 × the size']]))]
ADJSETS=[('Forms',[['good','better / the best'],['bad','worse / the worst'],['far','farther (further) / the farthest (furthest)'],['happy','happier / the happiest'],['big','bigger / the biggest'],['expensive','more expensive / the most expensive']]),
 ('Patterns',[['as … as','equal'],['not as … as','less than'],['the same … as','e.g. the same age as'],['different from','not alike'],['similar to','almost alike'],['the + superlative','best of three or more']])]
ADJFILL=[
('Forms 1','My brother is {0} (tall) than me.',[['taller']]),
('Forms 2','This is the {0} (good) film I have ever seen.',[['best']]),
('Forms 3','Maths is {0} (difficult) than English for Tom.',[['more difficult']]),
('Forms 4','Today is the {0} (hot) day of the year.',[['hottest']]),
('Forms 5','Ice cream is {0} (cheap) than cake.',[['cheaper']]),
('Forms 6','This is the {0} (beautiful) park in the city.',[['most beautiful']]),
('Compare 1','Lily is {0} tall {1} Amy. (They are both 160 cm.)',[['as'],['as']]),
('Compare 2','The red bag is not {0} expensive {1} the blue bag.',[['as'],['as']]),
('Compare 3','Cats and dogs are different {0} each other.',[['from']]),
('Compare 4','Her school bag is similar {0} mine.',[['to']])]
ADJMCQ=[
('Mount Everest is ___ mountain in the world.',['the highest','higher','the most high','highest'],0,''),
('My bag is ___ than yours.',['heavier','more heavy','heavyer','the heaviest'],0,''),
('This puzzle is ___ than that one.',['more difficult','difficulter','most difficult','the more difficult'],0,''),
('Ben is ___ student in our class.',['the tallest','taller','the most tall','tallest than'],0,''),
('The weather today is ___ than yesterday.',['worse','badder','more bad','the worst'],0,''),
('Tom is 150 cm and Mary is 150 cm. Tom is ___ Mary.',['as tall as','taller than','the tallest','less tall as'],2,''),
('This shirt costs $80 and that one costs $120. This shirt is ___ that one.',['less expensive than','more expensive than','as expensive as','the least expensive than'],2,''),
('My phone is ___ yours. (Both are the same model.)',['the same as','same with','similar with','as same as'],2,''),
('Her bag is ___ mine. (They do not look alike.)',['different from','different with','different as','same different'],2,''),
('Which sentence is correct?',['Tokyo is far bigger than Hong Kong.','Tokyo is very bigger than Hong Kong.','Tokyo is more bigger than Hong Kong.','Tokyo is the bigger than Hong Kong.'],0,'far + comparative.',1),
('Anna is 12, Ben is 14 and Cara is 13. Which sentence is correct?',['Ben is the oldest of the three and Anna is the youngest.','Cara is the oldest of the three.','Anna is older than Cara.','Ben is younger than Cara.'],1,'',1),
('The old library is 500 m². The new library is twice as big as the old one. The new library is ___.',['1,000 m²','250 m²','500 m²','1,500 m²'],2,'twice as big as = 2 ×.',1),
('Proofreading: “This is the more interesting book that I have ever read.” Which correction is right?',['“the more interesting” → “the most interesting”','“interesting” → “more interesting”','“that” → “than”','“ever” → “never”'],0,'Three or more things → the most.',1)]
eng_page('eng-adj','mcqBestEngAdj','Adjectives '+T('比較級、最高級同比較',''),T('Unit 1 (A)(B)：比較級、最高級、作出比較','Unit 1 (A)(B): comparative and superlative adjectives, making comparisons'),'notebook',ADJN,ADJSETS,ADJFILL,ADJMCQ,'ea-i')

# ---------- Unit 1 C / Unit 3 C: conditionals ----------
CONDN=[
('Type 0 — facts'+T(' 事實',''),
 '<p>'+K('If + present simple, present simple')+'</p>'+
 P(G('Use it for <b>facts</b> and things that are <b>always true</b>.','講事實或者一定會發生嘅嘢。'))+
 EG('If you heat ice, it melts.　If you press this button, the machine stops.')+
 P(G('<b>When</b> can replace <b>if</b> in Type 0: <i>When you heat ice, it melts.</i>','Type 0 入面 when 可以代替 if。'))),
('Type 1 — possible situations'+T(' 可能發生嘅情況',''),
 '<p>'+K('If + present simple, will + base verb')+'</p>'+
 P(G('Use it for a <b>possible</b> situation in the future and its result.','講將來有可能發生嘅事同結果。'))+
 EG('If it rains tomorrow, we will stay at home.')+
 P(G(K('No will')+' in the if-clause: <i>If it rains</i>, not <i>If it will rain</i>.','if 後面唔可以用 will。'))+
 P(G('The main clause can also use <b>can / may / might / should</b> or an imperative: <i>If you are free, come and help me.</i>','主句可以用 can／may／might／should 或者祈使句。'))),
('if, unless and punctuation'+T(' if、unless 同標點',''),
 '<p>'+K('unless = if … not')+'</p>'+
 EG('Unless you hurry, you will miss the bus. = If you don’t hurry, you will miss the bus.')+
 P(G('Do not use a negative verb after <i>unless</i>.','unless 後面唔再用否定。'))+
 P(G('If the <b>if-clause comes first</b>, put a comma: <i>If it rains, we will stay.</i> No comma when it comes second: <i>We will stay if it rains.</i>','if 子句喺前面要加逗號，喺後面就唔使。')))]
CONDSETS=[('If-clauses',[['If you heat ice','it melts'],['If it rains tomorrow','we will stay at home'],['If you mix red and yellow','you get orange'],['If you study hard','you will pass the test'],['If water freezes','it becomes ice'],['If I see Anna later','I will say hello']]),
 ('Terms',[['Type 0','If + present simple, present simple'],['Type 1','If + present simple, will + base verb'],['unless','= if … not'],['Type 0 is for','general facts, always true'],['Type 1 is for','possible future situations'],['if-clause first','comma after it']])]
CONDFILL=[
('Type 0 a','If you {0} (heat) ice, it {1} (melt).',[['heat'],['melts']]),
('Type 0 b','If the alarm {0} (ring), everybody leaves the building.',[['rings']]),
('Type 1 a','If it {0} (rain) this weekend, we {1} (not go) hiking.',[['rains'],["won't go",'will not go']]),
('Type 1 b','If you {0} (not eat) breakfast, you {1} (feel) hungry in class.',[["don't eat",'do not eat'],['will feel']]),
('Type 1 c','If Tom {0} (come), I {1} (tell) him the news.',[['comes'],['will tell',"'ll tell"]]),
('unless','We will miss the bus {0} we hurry.',[['unless']]),
('if','{0} you finish your homework, you can watch TV.',[['If']])]
CONDMCQ=[
('If you heat water to 100°C, it ___.',['boils','boiled','is boiled','would boil'],0,'Type 0: a fact.'),
('If it ___ tomorrow, we will stay at home.',['rains','will rain','would rain','rained'],1,'Type 1: present simple in the if-clause.'),
('If I ___ enough money, I will buy a new bike.',['have','will have','had','would have'],1,''),
('If you don’t study hard, you ___ the test.',['will fail','would fail','failed','are failing'],1,''),
('Ice ___ if the temperature rises above 0°C.',['melts','melted','would melt','melting'],0,'Type 0.'),
('___ you press this button, the machine stops.',['If','Unless','Although','Because'],0,''),
('I will go to the park ___ it rains.',['unless','if','because','although'],2,'I will go if it does not rain.'),
('Which sentence is Type 1?',['If Mary comes, we will start the meeting.','If Mary came, we would start the meeting.','If Mary had come, we would have started.','If Mary comes, we start the meeting.'],1,''),
('We won’t go on the picnic unless the weather ___ fine.',['is','will be','was','would be'],2,'No will after unless.',1),
('Which sentence is correct?',['If it is sunny tomorrow, we will go swimming.','If it will be sunny tomorrow, we will go swimming.','If it is sunny tomorrow, we would go swimming.','If it sunny tomorrow, we go will swimming.'],1,'',1),
('Which sentence means the same as “Unless you hurry, you will miss the bus.”?',['If you don’t hurry, you will miss the bus.','If you hurry, you will miss the bus.','If you don’t hurry, you would miss the bus.','Unless you don’t hurry, you will miss the bus.'],2,'unless = if … not.',1),
('Proofreading: “If you will visit Japan next year, you will see cherry blossoms.” Which correction is right?',['“will visit” → “visit”','“will see” → “see”','“next year” → “last year”','“If” → “Unless”'],1,'',1),
('Which sentence states a general fact?',['If you mix red and blue, you get purple.','If I see Tom tomorrow, I will tell him.','If it rains this afternoon, we will cancel the game.','If you pass the exam, I will buy you a gift.'],1,'Type 0 = fact.',1)]
eng_page('eng-cond','mcqBestEngCond','Conditionals '+T('條件句',''),T('Unit 1 (C) Type 1 · Unit 3 (C) Type 0','Unit 1 (C) Type 1 · Unit 3 (C) Type 0'),'cloud',CONDN,CONDSETS,CONDFILL,CONDMCQ,'ec-i')

# ---------- Unit 2 A + past perfect ----------
TENSEN=[
('Past continuous'+T(' 過去進行式',''),
 '<p>'+K('was / were + verb-ing')+'</p>'+
 P(G('An action <b>in progress</b> at a time in the past: <i>At 8 p.m. last night, I was doing my homework.</i>','過去某個時間「進行緊」嘅動作。'))+
 TB(['Form','Example'],[['+','I was doing / They were playing'],['−','I wasn’t doing / They weren’t playing'],['?','Was he sleeping? / What were you doing?']])+
 P(G('Verbs such as <i>know, like, want</i> are not usually used in the continuous.','know、like、want 呢類動詞通常唔用進行式。'))),
('when and while'+T('',''),
 '<p>'+K('while + past continuous　·　when + past simple')+'</p>'+
 EG('I was walking home when it started to rain.　(long action interrupted by a short one)')+
 EG('While Dad was cooking, Mum was reading a book.　(two actions at the same time)')),
('Past perfect'+T(' 過去完成式',''),
 '<p>'+K('had + past participle')+'</p>'+
 P(G('The <b>earlier</b> of two past actions: <i>When I arrived, the film had already started.</i>','兩件過去嘅事，先發生嗰件用 had + past participle。'))+
 P(G('Time words: <b>already, just, never … before, by the time, before, after</b>.','常見時間詞。'))+
 TB(['Form','Example'],[['+','She had finished.'],['−','She hadn’t finished.'],['?','Had you seen it before?']])+
 TB(['Verb','Past participle'],[['go','gone'],['eat','eaten'],['see','seen'],['take','taken'],['write','written'],['begin','begun'],['do','done']])),
('Choosing the tense'+T(' 點揀時態',''),
 P(G('Past simple = a finished action: <i>I watched TV.</i>','過去簡單式＝完咗嘅動作。'))+
 P(G('Past continuous = in progress at that time: <i>I was watching TV at 8.</i>','過去進行式＝當時進行緊。'))+
 P(G('Past perfect = happened <b>before</b> another past time: <i>I had watched TV before Dad came home.</i>','過去完成式＝喺另一個過去時間之前已經發生。')))]
TENSESETS=[('Past participles',[['go','gone'],['eat','eaten'],['write','written'],['begin','begun'],['take','taken'],['see','seen']]),
 ('Uses',[['Past continuous','was / were + verb-ing'],['Past perfect','had + past participle'],['in progress at a past time','was doing'],['an earlier past action','had done'],['while','long background action'],['when','short action that interrupts']])]
TENSEFILL=[
('Continuous 1','At 8 p.m. last night, I {0} (do) my homework.',[['was doing']]),
('Continuous 2','They {0} (watch) TV when the lights went out.',[['were watching']]),
('Continuous 3','While Dad {0} (cook), Mum {1} (read) a book.',[['was cooking'],['was reading']]),
('Continuous 4','What {0} you {1} (do) when I called?',[['were'],['doing']]),
('Perfect 1','When we arrived, the show {0} (already / start).',[['had already started','had started already']]),
('Perfect 2','She {0} (not / finish) her homework before dinner.',[["hadn't finished",'had not finished']]),
('Perfect 3','I {0} (see) that film before, so I didn’t go again.',[['had seen']])]
TENSEMCQ=[
('At 7 p.m. yesterday, I ___ dinner.',['was having','am having','have had','were having'],0,''),
('They ___ football when it started to rain.',['were playing','played','are playing','had played'],0,''),
('What ___ you doing at 9 o’clock last night?',['were','was','did','are'],0,''),
('While my mother ___ dinner, I was doing homework.',['was cooking','cooked','cooks','had cooked'],0,''),
('When I got to the cinema, the film ___.',['had already started','has already started','will already start','already starts'],1,'Earlier past action.'),
('She was tired because she ___ all day.',['had worked','has worked','works','was worked'],1,''),
('Sam didn’t hear the phone because he ___ a shower.',['was taking','takes','has taken','had took'],0,''),
('I had never ___ sushi before I went to Japan.',['eaten','ate','eat','eating'],1,'had + past participle.'),
('Which sentence is correct?',['When Amy arrived, the lesson had already begun.','When Amy arrived, the lesson already begins.','When Amy arrived, the lesson has already begun.','When Amy had arrived, the lesson already begin.'],1,'',1),
('“By the time we reached the station, the train had left.” What happened first?',['The train left.','We reached the station.','They happened at the same time.','We cannot tell.'],2,'had left = earlier.',1),
('Proofreading: “While I did my homework, my brother was playing games.” Which correction is right?',['“did” → “was doing”','“was playing” → “played”','“While” → “After”','“my” → “me”'],2,'',1),
('Proofreading: “She had went to bed before I came home.” Which correction is right?',['“had went” → “had gone”','“came” → “had come”','“before” → “after”','“to bed” → “in bed”'],2,'',1),
('Which sentence uses the past continuous correctly?',['The children were singing when the teacher walked in.','The children was singing when the teacher walked in.','The children were sing when the teacher walked in.','The children singing when the teacher walked in.'],2,'',1)]
eng_page('eng-tense','mcqBestEngTense','Tenses '+T('過去進行式同過去完成式',''),T('Unit 2 (A) 過去進行式 · 補充：過去完成式','Unit 2 (A) past continuous · extra notes: past perfect'),'camp',TENSEN,TENSESETS,TENSEFILL,TENSEMCQ,'et-i')

# ---------- hub ----------
ENGHUB='''<!doctype html>
<html lang="zh-HK">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>English %(h1)s</title>
<meta name="description" content="%(desc)s">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Huninn&display=swap">
<link rel="stylesheet" href="../assets/base.css">
<meta name="ty-lang" content="bi">
<script src="../assets/theme.js"></script>
</head>
<body>
<div class="wrap">
  <div class="bar"><a href="../../">‹ %(home)s</a><b>English</b></div>
  <h1>English %(h1)s</h1>
  <p class="sub">First Term Uniform Test 2026-2027 · 1 hour · 80 marks + 10 bonus</p>
  <div data-art="notebook"></div>
  <p class="grp">%(scope)s</p>
  <p class="sub">%(scopetxt)s</p>
  <a class="hub h1c" href="../eng-adj/"><strong>Adjectives</strong><span class="d">%(d1)s</span><span class="tag">Unit 1 (A)(B)</span></a>
  <a class="hub h2c" href="../eng-cond/"><strong>Conditionals</strong><span class="d">%(d2)s</span><span class="tag">Unit 1 (C)</span><span class="tag">Unit 3 (C)</span></a>
  <a class="hub h3c" href="../eng-tense/"><strong>Tenses</strong><span class="d">%(d3)s</span><span class="tag">Unit 2 (A)</span><span class="tag">Past perfect</span></a>
  <div class="stat"><h2>%(sth)s</h2><ul>%(stl)s</ul></div>
  <footer>%(foot)s</footer>
</div>
<script src="../assets/art.js"></script>
</body>
</html>
'''
hub=ENGHUB%dict(home=T('首頁','Home'),h1=T('中二英文','(Form 2)'),
 desc=T('中二英文上學期統一測驗溫習。','F.2 English first-term uniform test revision.'),
 scope=T('範圍','Syllabus'),
 scopetxt=T('<i>Oxford English Forward 2A</i> Unit 1-2；<i>Success in Grammar 2</i> Unit 1 (A)(B)(C)、Unit 2 (A)、Unit 3 (C)；過去完成式補充筆記。題型：Comprehension、Vocabulary、Grammar、Proofreading、Bonus。','<i>Oxford English Forward 2A</i> Units 1-2; <i>Success in Grammar 2</i> Unit 1 (A)(B)(C), Unit 2 (A), Unit 3 (C); extra notes on the past perfect. Sections: Comprehension, Vocabulary, Grammar, Proofreading, Bonus.'),
 d1=T('比較級、最高級、as … as、the same as、different from。','Comparative and superlative adjectives, as … as, the same as, different from.'),
 d2=T('Type 0（事實）同 Type 1（可能情況）、unless。','Type 0 (facts) and Type 1 (possible situations), unless.'),
 d3=T('過去進行式、when／while、過去完成式。','Past continuous, when / while, past perfect.'),
 sth=T('資料狀態','Material status'),
 stl=''.join('<li><span class="st %s">%s</span>%s</li>'%x for x in [
  ('p',T('未對課本','Not checked'),T('三個文法頁：只跟考試範圍同一般文法整理，題目全部係 AI 出題','Three grammar pages: built from the syllabus and standard grammar only; every question is AI-made')),
  ('t',T('未收到','Missing'),T('Oxford English Forward 2A Unit 1-2 課文（Comprehension）同詞彙表（Vocabulary）','Oxford English Forward 2A Units 1-2 reading texts (Comprehension) and word lists (Vocabulary)')),
  ('t',T('未收到','Missing'),T('Success in Grammar 2 練習、過去完成式筆記、歷屆試卷（Proofreading、Bonus 題型）','Success in Grammar 2 exercises, past-perfect notes and past papers (Proofreading and Bonus styles)'))]),
 foot=T('文法規則係一般英文文法；請對返課本同老師筆記。','Grammar rules are standard English grammar; please check them against the textbook and class notes.'))
if LANG=='en': hub=postEN(hub).replace('href="../../">','href="../../../">')
os.makedirs(ROOT+'eng',exist_ok=True)
open(ROOT+'eng/index.html','w',encoding='utf-8').write(hub)
