# English F.2 pages. Exam paper is in English: notes are English; the zh build adds Chinese glosses via G(en,zh).
# Sources: school glossaries (Unit 1, Unit 2), Oxford English Forward 2A Unit 2 Text 2, Success in Grammar 2 Units 1-3.
import random
def G(en,zh): return en+('<br><small>'+zh+'</small>' if LANG=='zh' and zh else '')
def TB(head,rows):
    return '<table class="tb"><tr>'+''.join('<th>%s</th>'%h for h in head)+'</tr>'+''.join('<tr>'+''.join('<td>%s</td>'%c for c in r)+'</tr>' for r in rows)+'</table>'
EBACK=('../eng/','English')
def eng_page(folder,key,title,sub,art,notes,sets,fills,mcqs,tagprefix,banner,desc):
    # mcqs rows: (question, options [correct first], noteIndex, explanation, hard=0, ai=1)
    ref=''.join(item('%s%d'%(tagprefix,i),'%d. %s'%(i+1,h),b,['','s2','s3','s4'][i%4]) for i,(h,b) in enumerate(notes))
    ref=refpane('<p class="sub">'+banner+'</p>'+ref,T('黃色字係重點，撳開睇','Highlighted text = key points. Tap to open'))
    rnd=random.Random(sum(map(ord,key)))
    M=[]
    for r in mcqs:
        q,o,tg,note=r[:4];hard=r[4] if len(r)>4 else 0;ai=r[5] if len(r)>5 else 1
        idx=list(range(len(o)));rnd.shuffle(idx)
        row=[(AIL if ai else '')+q,[o[j] for j in idx],idx.index(0),'%s%d'%(tagprefix,tg),T('答案：','Answer: ')+'<b>%s</b>　%s'%(o[0],note)]
        if hard: row.append(1)
        M.append(row)
    tagmap={m[3]:m[3] for m in M}
    fq=[{'t':t,'p':p,'b':b} for t,p,b in fills]
    sl=[{'name':n,'help':T('先撳左邊，再撳相配嘅右邊。','Tap a left item, then its match.'),'pairs':ps} for n,ps in sets]
    js=MASK+matchjs(sl)+filljs(fq)+mcq(key,M,tagmap,10,T('十條題，四揀一','10 questions, 4 choices'))
    gpage(folder,title,sub,art,
      [('p-ref',T('重點速覽','Notes')),('p-match',T('配對遊戲','Match')),('p-fill',T('寫字填空','Fill in')),('p-mcq',T('選擇題','Quiz'))],
      [('p-ref',ref),('p-match','<div id="matchroot"></div>'),('p-fill',FILLPANE2),('p-mcq','<div id="mcqroot"></div>')],js,
      back=EBACK,bar='English',desc=desc)
SIGB=T('筆記跟 <i>Success in Grammar 2</i>（SIG）；填空標「SIG」嘅係跟課本練習改寫，選擇題係【AI 出題】。','Notes follow <i>Success in Grammar 2</i> (SIG). Fill-in items marked “SIG” are adapted from its exercises; quiz questions are AI-made.')
GDESC=T('中二英文上學期統一測驗文法溫習。','F.2 English first-term uniform test grammar revision.')

# ---------- Unit 1 A/B: adjectives (SIG Unit 1 A, B) ----------
ADJN=[
('Comparative adjectives'+T(' 比較級',''),
 '<p>'+K('comparative + than')+'</p>'+
 P(G('Compare one person or thing with another: <b>Derek is a better player than Samuel.</b> <b>This book is more interesting than the other one.</b>','用 comparative + than 比較兩個人或事物。'))+
 P(G('<b>than</b> can be left out if it is clear what we compare: <i>Abby has become a more popular singer recently.</i>','睇得明比較對象時可以省略 than。'))+
 P(G('Object or subject pronoun after than: <i>Maggie is taller than me.</i> / <i>taller than I (am)</i> (more formal).','than 後面可用賓格或主格代名詞（主格較正式）。'))+
 P(G(K('and')+' = change: <i>I am getting heavier and heavier.</i> <i>more and more popular</i>','兩個比較級用 and 連接＝越來越…；長形容詞用 more and more。'))+
 P(G(K('the … the …')+' = two things change together: <i>The taller he grew, the slimmer he became.</i>','the + 比較級 … the + 比較級＝越…越…。'))),
('Superlative adjectives and forms'+T(' 最高級同變化規則',''),
 '<p>'+K('the + superlative + in / of …')+'</p>'+
 P(G('Compare one with a <b>group</b>: <i>Christine is the most intelligent girl in our class.</i>','同一組人或事物比較用 the + superlative。'))+
 TB(['Adjective','Comparative','Superlative'],[
  ['most short adj.','+ er (taller)','+ est (tallest)'],
  ['short, ends in e','+ r (nicer)','+ st (nicest)'],
  ['consonant + y','y → ier (heavier)','y → iest (heaviest)'],
  ['vowel + consonant','double + er (fitter)','double + est (fittest)'],
  ['3+ syllables','more expensive','most expensive'],
  ['-ed, -ful, -ing, -less','more crowded / cheerful / boring / careless','most …'],
  ['good','better','best'],['bad','worse','worst'],['far','farther / further','farthest / furthest']])+
 '<p><span class="k">Common error</span> '+G('No <i>more</i> with -er, no <i>most</i> with -est: ✘ more higher, ✘ the most tallest.','-er 前面唔再加 more；-est 前面唔再加 most。')+'</p>'),
('Comparing quantities'+T(' 比較數量',''),
 '<p>'+K('more / most　·　fewer / fewest　·　less / least')+'</p>'+
 TB(['Noun','Comparative','Superlative'],[['countable','more / fewer','most / fewest'],['uncountable','more / less','most / least']])+
 EG('Sue collected more shells than her brother, but her father collected the most shells.')+
 EG('Sam made fewer mistakes than May, but Chris made the fewest mistakes.')+
 EG('Crystal has less money than Phoebe, but Sally has the least money.')),
('as … as, the same as, different from, like, alike'+T(' 作出比較',''),
 '<p>'+K('as + adj + as　·　not as + adj + as')+'</p>'+
 P(G('<b>as … as</b> = the same: <i>I am as tall as my father.</i>　<b>not as … as</b> = not the same: <i>Martin is not as hard-working as Aaron.</i> (= Aaron is more hard-working.)','as … as＝一樣；not as … as＝唔及。'))+
 '<p><span class="k">Common error</span> '+G('Use the plain adjective in as … as: ✘ as tastier as → ✔ as tasty as.','as … as 中間用原級：唔可以用比較級。')+'</p>'+
 P(G('<b>the same (…) as</b>: <i>Jacky is the same age as me.</i>　<b>different from</b>: <i>Maggie is very different from her sister.</i>','the same … as＝一樣；different from＝唔同。'))+
 P(G('<b>like</b> + noun / pronoun: <i>My dog looks like yours.</i>　<b>alike</b> (no noun after it): <i>Our styles of writing are very much alike.</i>','like 後面跟名詞或代名詞；alike 後面唔跟名詞。')))]
ADJSETS=[('Forms',[['good','better / best'],['bad','worse / worst'],['far','farther, further / farthest, furthest'],['heavy','heavier / heaviest'],['fit','fitter / fittest'],['expensive','more expensive / most expensive']]),
 ('Quantities',[['more … than','greater in quantity'],['the most','greatest in quantity'],['fewer … than','smaller (countable)'],['the fewest','smallest (countable)'],['less … than','smaller (uncountable)'],['the least','smallest (uncountable)']]),
 ('Comparisons',[['as … as','the same in some way'],['not as … as','not the same'],['the same … as','e.g. the same age as'],['different from','not the same'],['like','+ noun or pronoun'],['alike','no noun after it']])]
ADJFILL=[
('SIG forms 1','This shop’s opening hours are {0} (long) than that shop’s.',[['longer']]),
('SIG forms 2','Fred’s cat is {0} (cute) than mine.',[['cuter']]),
('SIG forms 3','Jenny’s room is now {0} (tidy) than her brother’s room.',[['tidier']]),
('SIG forms 4','Angel thinks roses are {0} (beautiful) than daisies.',[['more beautiful']]),
('SIG forms 5','This comedy is {0} (funny) than the one we watched last month.',[['funnier']]),
('SIG super 1','Jack is very impolite. He is {0} (rude) person among my classmates.',[['the rudest']]),
('SIG super 2','It was {0} (exciting) match of the year.',[['the most exciting']]),
('SIG super 3','Sloths are {0} (slow) animals in the world.',[['the slowest']]),
('SIG super 4','Jane is a very able student. She is {0} (able) student in our class.',[['the ablest']]),
('Irregular','I got a bad result, but Peter had an even {0} (bad) result.',[['worse']]),
('SIG quantity 1','Sam made {0} mistakes than May in the test.',[['fewer']]),
('SIG quantity 2','Crystal has {0} money than Phoebe.',[['less']]),
('SIG quantity 3','Among all the friends, Martin brought {0} cash to the fair. (the smallest amount of cash)',[['the least']]),
('SIG as … as 1','Martin is not {0} hard-working {1} Aaron.',[['as'],['as']]),
('SIG same / different','Jacky is {0} same age {1} me.',[['the'],['as']]),
('SIG like / alike 1','Eddie’s handwriting is {0} David’s.',[['like']]),
('SIG like / alike 2','Kate and Janet are {0} in their hairstyles.',[['alike']])]
ADJMCQ=[
('Mount Everest is ___ mountain in the world.',['the highest','higher','the most high','highest'],1,''),
('My bag is ___ than yours.',['heavier','more heavy','heavyer','the heaviest'],1,'consonant + y → -ier.'),
('This puzzle is ___ than that one.',['more difficult','difficulter','most difficult','the more difficult'],1,'Long adjective → more.'),
('Ben is ___ student in our class.',['the tallest','taller','the most tall','tallest than'],1,''),
('The weather today is ___ than yesterday.',['worse','badder','more bad','the worst'],1,'bad → worse → worst.'),
('This shop is ___ the other one. (crowded)',['more crowded than','crowdeder than','the most crowded','as more crowded as'],1,'-ed adjectives take more.'),
('Peter has ___ books than Ann. (countable)',['fewer','less','the fewest','the least'],2,'Countable → fewer.'),
('There is ___ milk in my cup than in yours. (uncountable)',['less','fewer','the fewest','few'],2,'Uncountable → less.'),
('Tom is 150 cm and Mary is 150 cm. Tom is ___ Mary.',['as tall as','taller than','the tallest','as taller as'],3,''),
('The red bag is $50 and the blue bag is $80. The red bag is ___ the blue bag.',['not as expensive as','as expensive as','more expensive than','the least expensive of'],3,''),
('Her bag is ___ mine. (They do not look alike.)',['different from','different with','different as','same different'],3,''),
('Our classmates are ___ brothers and sisters.',['like','alike','likes','as alike'],3,'like + noun.'),
('The two brothers look very much ___.',['alike','like','likes','as like'],3,'alike: no noun after it.'),
('Which sentence is correct?',['The price is higher than expected.','The price is more higher than expected.','The price is the higher than expected.','The price is most high than expected.'],1,'Common error: no more with -er.',1),
('Which sentence is correct?',['The cheesecake is as tasty as the chocolate cake.','The cheesecake is as tastier as the chocolate cake.','The cheesecake is as more tasty as the chocolate cake.','The cheesecake is as tasty than the chocolate cake.'],3,'Plain adjective in as … as.',1),
('Which sentence is correct?',['The taller he grew, the slimmer he became.','The taller he grew, slimmer he became.','Taller he grew, the slimmer he became.','The more tall he grew, the slimmer he became.'],0,'the + comparative … the + comparative.',1),
('Anna is 12, Ben is 14 and Cara is 13. Which sentence is correct?',['Ben is the oldest of the three and Anna is the youngest.','Cara is the oldest of the three.','Anna is older than Cara.','Ben is younger than Cara.'],1,'',1),
('Proofreading: “This is the more interesting book that I have ever read.” Which correction is right?',['“the more interesting” → “the most interesting”','“interesting” → “more interesting”','“that” → “than”','“ever” → “never”'],1,'Three or more things → the most.',1)]
eng_page('eng-adj','mcqBestEngAdj','Adjectives '+T('比較級、最高級同比較',''),T('Unit 1 (A)(B)：比較級、最高級、作出比較','Unit 1 (A)(B): comparative and superlative adjectives, making comparisons'),'notebook',ADJN,ADJSETS,ADJFILL,ADJMCQ,'ea-i',SIGB,GDESC)

# ---------- Unit 1 C / Unit 3 C: conditionals (SIG Unit 1 C, Unit 3 C) ----------
CONDN=[
('Type 1 — possible situations'+T(' 可能發生嘅情況',''),
 '<p>'+K('If + simple present, simple future (will)')+'</p>'+
 P(G('Talk about a <b>possible</b> situation: <i>If it rains, we will cancel the outing.</i>　<i>If they have time, they will go to the cinema.</i>','講有可能發生嘅情況：if 子句用現在簡單式，主句用將來簡單式。'))+
 P(G('Either clause can come first. <b>Main clause first → no comma</b>: <i>We will cancel the outing if it rains.</i>','兩個子句次序可以對調；主句喺前面就唔使逗號。'))+
 '<p><span class="k">Common error</span> '+G('No <i>will</i> in the if-clause: ✘ If you will join … → ✔ If you join the programme, you will get a 10% discount.','if 子句入面唔可以用 will。')+'</p>'),
('Modals in Type 1'+T(' 主句用情態動詞',''),
 '<p>'+K('If + simple present, modal + base verb')+'</p>'+
 TB(['Modal','Use','Example'],[
  ['can / may','permission','The tourists can/may see the exhibition if they pay.'],
  ['may','possible','If we forget our books, the teacher may punish us.'],
  ['should / must','necessary (must = stronger)','If you want to borrow books, you must bring your card.'],
  ['should / must','advice','You should practise hard if you want to join the team.']])+
 EG('If you get up late, you may miss the bus.')),
('Type 0 — facts'+T(' 事實',''),
 '<p>'+K('If + simple present, simple present')+'</p>'+
 P(G('Talk about <b>facts or general truths</b>: <i>If it rains, the ground gets wet.</i>　<i>If flowers do not get enough water, they die.</i>','講事實或一般真理：兩個子句都用現在簡單式。'))+
 P(G('Order can change: <i>The ground gets wet if it rains.</i>','次序可以對調。'))+
 P(G(K('when')+' can replace <i>if</i>: <i>When flowers do not get enough water, they die.</i>','Type 0 入面 when 可以代替 if。'))+
 EG('If you press this button, the rice cooker starts cooking.　Ice melts if you take it out of the freezer.'))]
CONDSETS=[('Type 0',[['If you press this button','the rice cooker starts cooking'],['If you mix red and blue','you get purple'],['If the air becomes hot','the hot-air balloon rises'],['Ice melts','if you take it out of the freezer'],['If we heat water to its boiling point','evaporation takes place'],['If the elevator is overloaded','the alarm rings']]),
 ('Type 1',[['If it rains,','we will cancel the outing'],['If they have time,','they will go to the cinema'],['If you join the programme,','you will get a 10% discount'],['I will buy that dress','if I have enough money'],['If I see Peter,','I will ask him to call you back'],['If Grandma does not take the medicine,','she will not get better']]),
 ('Modals',[['If you are a member,','you can/may join our courses'],['If you take sick leave,','you should/must submit a certificate'],['If Ada is absent,','we may ask Sandy to play the piano'],['If Tim wants to be a police officer,','he must pass the physical test'],['If I feel bored,','I may listen to some music'],['If Sam feels tired,','he should stop working for a while']])]
CONDFILL=[
('SIG Type 1 a','If the calculator {0} (not work), I {1} (buy) a new one.',[["doesn't work",'does not work'],['will buy',"'ll buy"]]),
('SIG Type 1 b','We {0} (give) them a surprise if they {1} (come) to our party.',[['will give',"'ll give"],['come']]),
('SIG Type 1 c','Grandad {0} (not hear) you if you {1} (speak) too softly.',[["won't hear",'will not hear'],['speak']]),
('SIG Type 1 d','John {0} (get) fat if he {1} (eat) so much food at every meal.',[['will get',"'ll get"],['eats']]),
('SIG Type 1 e','If we {0} (not hurry), we {1} (miss) the bus.',[["don't hurry",'do not hurry'],['will miss',"'ll miss"]]),
('SIG modal 1','If you are a member, you {0} join our courses. (permission: can / may)',[['can','may']]),
('SIG modal 2','If Tim wants to be a police officer, he {0} pass the physical test. (necessary, strong)',[['must']]),
('SIG Type 0 a','If you {0} (press) this button, the rice cooker {1} (start) cooking the rice.',[['press'],['starts']]),
('SIG Type 0 b','If you {0} (connect) your phone to a computer, it {1} (get) charged.',[['connect'],['gets']]),
('SIG Type 0 c','If more people {0} (share) a cake, each person {1} (receive) a smaller portion.',[['share'],['receives']]),
('SIG Type 0 d','If we {0} (mix) red and blue, we {1} (get) purple.',[['mix'],['get']]),
('SIG Type 0 e','Ice {0} (melt) if you {1} (take) it out of the freezer.',[['melts'],['take']])]
CONDMCQ=[
('If it ___ tomorrow, we will stay at home.',['rains','will rain','would rain','rained'],0,'Type 1: simple present in the if-clause.'),
('If I ___ enough money, I will buy a new bike.',['have','will have','had','would have'],0,''),
('If you don’t study hard, you ___ the test.',['will fail','would fail','failed','are failing'],0,''),
('If you ___ the project, you will get a 10% discount.',['join','will join','joined','would join'],0,'No will in the if-clause.'),
('If you get up late, you ___ the bus.',['may miss','missed','will missing','may to miss'],1,'modal + base form.'),
('If you want to borrow books from the library, you ___ bring your library card.',['must','might','would','did'],1,'must = necessary.'),
('The tourists ___ see the exhibition if they pay the entrance fee. (permission)',['can','must not','will not','did'],1,''),
('If you heat water to 100°C, it ___.',['boils','boiled','is boiled','would boil'],2,'Type 0: a fact.'),
('Ice ___ if the temperature rises above 0°C.',['melts','melted','would melt','melting'],2,'Type 0.'),
('If flowers ___ enough water, they die.',['do not get','will not get','did not get','are not get'],2,''),
('The ground ___ wet if it rains.',['gets','got','will getting','would get'],2,'Type 0: simple present.'),
('Which sentence is correct?',['If it is sunny tomorrow, we will go swimming.','If it will be sunny tomorrow, we will go swimming.','If it is sunny tomorrow, we would go swimming.','If it sunny tomorrow, we go will swimming.'],0,'',1),
('Which sentence is punctuated correctly?',['If it rains, we will cancel the outing.','If it rains we will cancel the outing.','We will cancel the outing, if it rains.','If, it rains we will cancel the outing.'],0,'If-clause first → comma; main clause first → no comma.',1),
('Which sentence states a general fact (Type 0)?',['If you mix red and blue, you get purple.','If I see Tom tomorrow, I will tell him.','If it rains this afternoon, we will cancel the game.','If you pass the exam, I will buy you a gift.'],2,'',1),
('Proofreading: “If you will visit Japan next year, you will see cherry blossoms.” Which correction is right?',['“will visit” → “visit”','“will see” → “see”','“next year” → “last year”','“If” → “Unless”'],0,'',1)]
eng_page('eng-cond','mcqBestEngCond','Conditionals '+T('條件句',''),T('Unit 1 (C) Type 1 · Unit 3 (C) Type 0','Unit 1 (C) Type 1 · Unit 3 (C) Type 0'),'cloud',CONDN,CONDSETS,CONDFILL,CONDMCQ,'ec-i',SIGB,GDESC)

# ---------- Unit 2 A: past continuous (SIG Unit 2 A) + past perfect (teacher notes needed) ----------
TENSEN=[
('Past continuous'+T(' 過去進行式',''),
 '<p>'+K('was / were + verb-ing')+'</p>'+
 P(G('An action <b>was going on</b> at a given time or over a period in the past: <i>We were travelling in Europe last month.</i> <i>David was reading the whole afternoon.</i>','過去某個時間或一段時間內「進行緊」嘅動作。'))+
 TB(['Form','Example'],[['+','I/He/She/It was playing; You/We/They were playing'],['−','was not (wasn’t) / were not (weren’t) playing'],['Yes/No ?','Was he running? — Yes, he was. / No, he wasn’t.'],['Wh- ?','What were you doing at 9 p.m.?']])+
 TB(['Verb','-ing form'],[['most verbs','sing → singing'],['ends in e','make → making'],['ends in ie','die → dying'],['vowel + consonant (short)','run → running; begin → beginning']])+
 '<p><span class="k">Tip</span> '+G('Usually NOT used with <i>belong, prefer, know, seem</i>.','belong、prefer、know、seem 通常唔用進行式。')+'</p>'),
('while and when'+T('',''),
 '<p>'+K('two long actions: while … while　·　long + short: when')+'</p>'+
 EG('While Leo was watching TV, Rebecca was reading a book.　(two actions at the same time → past continuous for both, usually while)')+
 EG('While/When we were swimming, a shark suddenly appeared.　(past continuous for the longer action, simple past for the shorter action)')+
 EG('Crystal was quarrelling with her brother when their parents came home.')+
 P(G('<b>while / when</b> can go with the longer action; use <b>when</b> for the shorter action.','長動作可以用 while 或 when；短動作只用 when。'))),
('Past perfect'+T(' 過去完成式（老師筆記 + SIG 3A）',''),
 '<p>'+K('had + past participle')+'</p>'+
 P(G('<b>1. Two past events:</b> the <b>earlier</b> action → past perfect; the later action or the specific time → simple past. <i>The train had already left when Tim arrived at the station.</i> <i>Sandy had written three novels by the time she was eleven.</i>','兩件過去嘅事：先發生用 past perfect，後發生用 past simple。'))+
 P(G('<b>2. Reported speech:</b> simple past → past perfect; present perfect → past perfect; past perfect stays. <i>“I was a bad student,” said Mrs Au. → Mrs Au said (that) she had been a bad student.</i> <i>“We haven’t finished,” said Tom and Kit. → They said they hadn’t finished.</i>','間接引語：simple past／present perfect 都變 past perfect；past perfect 不變。'))+
 P(G('<b>3. wish</b> (regret about the past): <i>I wish I’d gone to the cinema.</i> <i>She wishes she hadn’t stayed up late last night.</i>','wish ＋ past perfect：對過去嘅事感到後悔。'))+
 P(G(K('Time words')+' just, already, yet, ever, never, when, after, before, by the time.','常見時間詞。'))+
 EG('I left when Terence arrived. (I saw him, then I left.)　Sam had left when Terence arrived. (Sam was already gone.)')+
 EG('The man had gone before she opened the door.　Miss Lee emailed us after she had received the parcel.')+
 TB(['Form','Example'],[['+','I/He/She/They had (’d) left.'],['−','had not (hadn’t) brought her passport'],['Yes/No ?','Had they finished dinner? — Yes, they had. / No, they hadn’t.']])+
 TB(['Past perfect','Simple past','Present perfect'],[
  ['two past actions, one before the other: My grandpa had passed away before I was born.','one past action / exact time: My grandpa passed away twenty years ago.','action continues to now: I have been ill for a week.']])+
 TB(['Verb','Past participle'],[['go','gone'],['eat','eaten'],['see','seen'],['take','taken'],['swim','swum'],['fly','flown'],['dig','dug'],['break','broken'],['write','written'],['begin','begun'],['do','done']]))]
TENSESETS=[('Past continuous',[['Past continuous','was / were + verb-ing'],['wasn’t / weren’t','negative form'],['Was he running?','Yes/No question'],['What were you doing?','Wh- question'],['die','dying'],['run','running']]),
 ('while / when',[['two long actions at the same time','while … while'],['long action + short action','past continuous + simple past'],['shorter action','when'],['While Leo was watching TV,','Rebecca was reading a book'],['Crystal was quarrelling with her brother','when their parents came home'],['While we were swimming,','a shark suddenly appeared']]),
 ('Past perfect',[['Past perfect','had + past participle'],['an earlier past action','had done'],['go','gone'],['eat','eaten'],['write','written'],['begin','begun']])]
TENSEFILL=[
('SIG 1','Luckily, it {0} (not rain) during the marathon.',[["wasn't raining",'was not raining']]),
('SIG 2','My friends {0} (chat) about the new book when I came.',[['were chatting']]),
('SIG 3','From 2010 to 2015, Mr Chan {0} (live) in London.',[['was living']]),
('SIG 4','I was sick yesterday. I {0} (lie) in bed all day.',[['was lying']]),
('SIG 5','When he {0} (get) onto the bus, the person behind {1} (push) him forward.',[['was getting'],['pushed']]),
('SIG 6','They {0} (play) chess when they {1} (hear) the noise.',[['were playing'],['heard']]),
('SIG 7','James {0} (study) while his sister {1} (watch) TV.',[['was studying'],['was watching']]),
('SIG 8','While Fiona {0} (perform) on the stage, her parents {1} (take) photos of her.',[['was performing'],['were taking']]),
('SIG 9','{0} you {1} (take) the lift when the electricity went out this morning?',[['Were'],['taking']]),
('SIG 10','What {0} Timmy and Anna {1} (find) at recess?',[['were'],['finding']]),
('SIG PP 1','The man fell asleep after he {0} (take) the medicine.',[['had taken']]),
('SIG PP 2','They {0} (swim) in the Dead Sea before they went on their trip to Israel.',[['had swum']]),
('SIG PP 3','The astronaut was nervous because he {0} (not fly) in space before.',[["hadn't flown",'had not flown']]),
('SIG PP 4','You {0} (misunderstand) Kenneth. He was not that kind of person.',[['had misunderstood']]),
('SIG PP 5','Mary {0} (throw) away some clothes before she bought some new ones.',[['had thrown']]),
('SIG PP 6','The worker stopped the machine after he {0} (dig) a hole.',[['had dug']]),
('SIG PP 7','I missed the plane because my passport {0} (expire).',[['had expired']]),
('SIG PP 8','The film {0} (begin) before we arrived at the cinema.',[['had begun']]),
('SIG PP 9','Bob could not drive a car because he {0} (not turn) 18 yet.',[["hadn't turned",'had not turned']]),
('SIG PP 10','By the time William finally {0} (apologize) to Carrie, she {1} (not talk) to him for a week.',[['apologized','apologised'],["hadn't talked",'had not talked']]),
('SIG PP 11','Dad’s car {0} (break) down on the road, so he {1} (go) to the airport by taxi.',[['had broken'],['went']]),
('SIG PP 12','We {0} (finish) dinner when Dad {1} (come) home from work last night.',[['had finished'],['came']]),
('SIG PP 13','I {0} (not return) the book by the time the library {1} (close).',[["hadn't returned",'had not returned'],['closed']]),
('SIG PP 14','The boat {0} (sink) before the rescue team {1} (arrive).',[['had sunk'],['arrived']]),
('SIG PP 15','Sandy and I {0} (sit) down before the drama {1} (begin).',[['had sat'],['began']]),
('SIG PP 16','The woman started to feel unwell after she {0} (come) back from Thailand.',[['had come']]),
('SIG PP 17','Cosmetics {0} (exist) long before modern cosmetic technology {1} (appear) in the 20th century.',[['had existed'],['appeared']]),
('SIG PP 18','Cosmetics {0} (contain) toxic chemicals before people {1} (start) to innovate safer formulas.',[['had contained'],['started']]),
('SIG PP 19','I {0} (try) out this new mascara that I {1} (not use) before.',[['tried'],["hadn't used",'had not used']]),
('SIG PP 20','It {0} (not rain) for three weeks before the shower today.',[["hadn't rained",'had not rained']]),
('SIG PP 21','I {0} (apply) the mascara before I {1} (go) out.',[['had applied'],['went']]),
('SIG PP 22','By the time I {0} (arrive) at the venue, the party {1} (start).',[['arrived'],['had started']]),
('SIG PP 23','{0} they {1} (finish) dinner when she came home?',[['Had'],['finished']]),
('Reported speech 1','“I was a bad student,” said Mrs Au. → Mrs Au said (that) she {0} a bad student. (be)',[['had been']]),
('Reported speech 2','“We haven’t finished our homework yet,” said Tom and Kit. → They said (that) they {0} their homework yet. (not finish)',[["hadn't finished",'had not finished']]),
('wish 1','I’m bored. I wish I {0} (go) to the cinema with my friends.',[['had gone',"'d gone",'’d gone']]),
('wish 2','Jean is really tired. She wishes she {0} (not stay) up late last night.',[["hadn't stayed",'had not stayed']])]
TENSEMCQ=[
('At 7 p.m. yesterday, I ___ dinner.',['was having','am having','have had','were having'],0,''),
('They ___ football when it started to rain.',['were playing','played','are playing','had played'],1,'long action + short action.'),
('What ___ you doing at 9 o’clock last night?',['were','was','did','are'],0,''),
('___ the boy listening to his teacher at that time?',['Was','Were','Did','Is'],0,'Yes/No question.'),
('While my mother ___ dinner, I was doing homework.',['was cooking','cooked','cooks','had cooked'],1,'two actions at the same time.'),
('It was raining ___ the boys went out yesterday.',['when','while','because','as if'],1,'Short action (went out) → when.'),
('Sam didn’t hear the phone because he ___ a shower.',['was taking','takes','has taken','had took'],0,''),
('Which verb is NOT usually used in the past continuous?',['know','play','read','cook'],0,'belong, prefer, know, seem.'),
('The -ing form of “run” is ___.',['running','runing','runninging','runs'],0,'Short verb: double the consonant.'),
('When I got to the cinema, the film ___.',['had already started','has already started','will already start','already starts'],2,'Earlier past action.'),
('I had never ___ sushi before I went to Japan.',['eaten','ate','eat','eating'],2,'had + past participle.'),
('Which sentence is correct?',['When Amy arrived, the lesson had already begun.','When Amy arrived, the lesson already begins.','When Amy arrived, the lesson has already begun.','When Amy had arrived, the lesson already begin.'],2,'',1),
('Proofreading: “They were sleeping when their parents were leaving home.” Which correction is right?',['“were leaving” → “left”','“were sleeping” → “slept”','“when” → “while”','“their” → “there”'],1,'Short action → simple past.',1),
('Proofreading: “Molly was cooking while her brother watched TV.” Which correction is right?',['“watched” → “was watching”','“was cooking” → “cooked”','“while” → “when”','“her” → “she”'],1,'Both actions went on at the same time.',1),
('Tim arrived at the station at 8:10 and the train left at 8:05. Which sentence is correct?',['The train had already left when Tim arrived.','Tim had arrived when the train had already left.','The train already left when Tim had arrived.','The train has left when Tim arrived.'],2,'First action = had left.',0),
('“We haven’t finished our homework yet,” said Tom and Kit. Which is the correct reported speech?',['Tom and Kit said they hadn’t finished their homework yet.','Tom and Kit said they haven’t finished their homework yet.','Tom and Kit said they didn’t finished their homework yet.','Tom and Kit said they weren’t finish their homework yet.'],2,'Present perfect → past perfect.',1),
('Jean stayed up late last night and now she is tired. Which sentence is correct?',['Jean wishes she hadn’t stayed up late last night.','Jean wishes she didn’t stay up late last night.','Jean wishes she hasn’t stayed up late last night.','Jean wishes she wasn’t staying up late last night.'],2,'wish + past perfect (regret about the past).',1),
('I ___ the book by the time the library closed.',['hadn’t returned','didn’t returned','haven’t returned','wasn’t returned'],2,'By the time + simple past → past perfect for the earlier action.',0),
('Miss Lee emailed us after she ___ the parcel.',['had received','has received','was receiving','receives'],2,'after + past perfect (first action).',0),
('Proofreading: “She had went to bed before I came home.” Which correction is right?',['“had went” → “had gone”','“came” → “had come”','“before” → “after”','“to bed” → “in bed”'],2,'',1)]
eng_page('eng-tense','mcqBestEngTense','Tenses '+T('過去進行式同過去完成式',''),T('Unit 2 (A) 過去進行式 · 補充：過去完成式','Unit 2 (A) past continuous · extra notes: past perfect'),'camp',TENSEN,TENSESETS,TENSEFILL,TENSEMCQ,'et-i',T('筆記跟 <i>Success in Grammar 2</i> Unit 2 (A) 同老師過去完成式筆記（含 SIG Unit 3 A）；填空標「SIG」係跟課本練習改寫，選擇題係【AI 出題】。','Notes follow SIG Unit 2 (A) and the teacher’s past-perfect notes (with SIG Unit 3 A); fill-in items marked “SIG” are adapted from the exercises; quiz questions are AI-made.'),GDESC)

# ---------- Vocabulary: school glossaries Unit 1 and Unit 2 ----------
VOC=[
('Unit 1 Text 1 — How big data improves online shopping (p.4-5)',[
('advertising','n.','the activity and industry of advertising things to people on television, in newspapers, on the internet, etc.'),
('bestselling','adj.','describing a product, usually a book, which is bought by large numbers of people'),
('big data','n.','sets of information that are too large or too complex to handle, analyse or use with standard methods'),
('bricks-and-mortar','adj.','a business that operates from a shop or a building that customers visit, rather than only online'),
('coincide with','phr. v.','(of two or more events) to take place at the same time'),
('cumbersome','adj.','large and heavy'),
('customize','v.','to make or change something to suit the needs of the owner or user'),
('dietary supplement','n.','vitamins and other foods eaten in addition to what you usually eat'),
('embrace','v.','to accept an idea, a proposal, a set of beliefs, etc.'),
('formulate','v.','to create or prepare something carefully, giving particular attention to the details'),
('generic','adj.','shared by, including or typical of a whole group of things; not specific'),
('individualized','adj.','designed for a particular person or thing; connected with a particular person or thing'),
('lo and behold','phr.','used for calling attention to a surprising or annoying thing'),
('on-trend','adj.','very fashionable'),
('optimize','v.','to make something as good as it can be'),
('personalized','adj.','designed or changed so that it is suitable for the needs of a particular person'),
('prominent','adj.','easily seen'),
('responsive','adj.','reacting quickly and in a positive way'),
('targeted','adj.','aimed at a particular place or group of people')]),
('Unit 1 Text 2 — Support local artisans at Handcrafted! (p.8-9)',[
('artisan','n.','a person who does work that needs a special skill, making things with their hands'),
('bargain','n.','a thing bought for less than the usual price'),
('deal','n.','an agreement, especially in business, on particular conditions for buying or doing something'),
('dealer','n.','a person whose business is buying and selling a product'),
('haggle','v.','to argue with somebody to reach an agreement, especially about the price of something'),
('handcrafted','adj.','made with skill by hand, not by machine'),
('second-hand','adj.','owned by somebody else before'),
('shop around','phr. v.','to compare the quality or prices of goods or services offered by different shops or companies so that you can choose the best'),
('source','n.','a place, person or thing that you get something from'),
('special offer','n. phr.','a product that is sold at less than its usual price'),
('stall','n.','a table or small shop with an open front that people sell things from, especially at a market'),
('sustainable','adj.','involving the use of natural products and energy in a way that does not harm the environment'),
('tag','n.','a small piece of paper, cloth, plastic, etc. attached to something to identify it or give information about it'),
('vendor','n.','a company that sells a particular product'),
('vintage','adj.','typical of a period in the past and of high quality')]),
('Unit 2 Text 2 — Watching your step (p.40-41)',[
('assume','v.','to think or accept that something is true but without having proof of it'),
('access','n.','the right to enter a place, use something, see someone etc.'),
('bombard','v.','to attack somebody with a lot of questions, criticisms, etc. or by giving them too much information'),
('browse','v.','to look at a lot of things in a shop rather than looking for one particular thing'),
('consequence','n.','a result of something that has happened, especially an unpleasant result'),
('digital footprint','n.','the information about a particular person that exists on the internet as a result of their online activity'),
('doxing','n.','the act of publicly providing personally identifiable information about an individual or organization, usually via the Internet'),
('eavesdrop','v.','to listen secretly to what other people are saying'),
('extend to','phr. v.','to include or affect someone or something'),
('hack','v.','to secretly find a way of looking at and/or changing information on somebody else’s computer system without permission (n.: hacker)'),
('harass','v.','to annoy or worry somebody by putting pressure on them or saying or doing unpleasant things'),
('innocent','adj.','not guilty of a particular crime'),
('long-lasting','adj.','continuing for a long period of time'),
('misleading','adj.','causing someone to believe something that is not true'),
('permission','n.','if someone is given permission to do something, they are allowed to do it'),
('privacy','n.','the right that someone has to keep their personal life or personal information secret or known only to a small group of people'),
('reliance','n.','the state of depending on or trusting in something or someone'),
('severe','adj.','extremely bad or serious'),
('snippet','n.','a small piece of information or news'),
('stir','v.','to make somebody excited or make them feel something strongly'),
('track','v.','to follow a person by looking for proof that they have been somewhere, or by using electronic equipment'),
('trace','n.','a mark, an object or a sign that shows that somebody or something existed or was present')]),
('Unit 2 Life skill — How can social media improve our world? (p.44)',[
('at risk of','phr.','in a dangerous situation'),
('community','n.','the people living in one particular area or people who are considered as a unit because of their common interests, social group, or nationality'),
('direct message','n. phr.','a private message sent on a social media website, that only the person it is sent to can see'),
('effective','adj.','successful, and working in the way that was intended'),
('hashtag','n.','a word in a Twitter message with # in front of it, which indicates what the message is about'),
('informative','adj.','providing many useful facts or ideas'),
('invade','v.','to get involved in something in an unwanted and annoying way'),
('keep up with','phr. v.','to write to, telephone, or meet a friend regularly, so that you do not forget each other'),
('like-minded','adj.','having similar interests and opinions'),
('look out for','phr. v.','to take care of somebody and make sure nothing bad happens to them'),
('meme','n.','an image, a video, a piece of text etc. that is passed very quickly from one internet user to another, often with slight changes that make it humorous'),
('on a daily basis','phr.','doing something every day, regularly, or as part of a usual routine'),
('spark','v.','to cause the start of something, especially an argument or fighting'),
('thread','n.','a connected group of pieces of writing on the internet, where people are talking about a particular subject'),
('troll','n.','someone who leaves offensive or upsetting messages on the Internet, just in order to get a reaction'),
('uplifting','adj.','making you feel happier and more hopeful'),
('go viral','v. phr.','spreading or becoming popular very quickly through communication from one person to another, especially on the internet')])]
VNOTES=[(t,TB(['Word','Meaning'],[['<b>%s</b><br><small>%s</small>'%(w,p),m] for w,p,m in L])) for t,L in VOC]
VSETS=[('Types of shops (1)',[['confectioner','sells sweets and chocolate'],['florist’s','sells flowers and bouquets'],['antique shop','old but well-preserved valuables'],['optician’s','glasses and contact lenses'],['pharmacy','medicine and plasters'],['boutique','a small shop selling fashionable clothes']]),
 ('Types of shops (2)',[['cosmetics shop','lipstick and foundation'],['electronics shop','headphones'],['jeweller’s','necklaces and earrings'],['confectioner','lollipops'],['florist’s','roses'],['pharmacy','plasters']])]
for gi,(t,L) in enumerate(VOC):
    nm=['U1 Text 1','U1 Text 2','U2 Text 2','U2 Life skill'][gi]
    for k in range(0,len(L),6):
        chunk=L[k:k+6]
        if len(chunk)<4: chunk=L[-6:]
        VSETS.append(('%s (%d)'%(nm,k//6+1),[[w,m] for w,p,m in chunk]))
rv=random.Random(77)
VMCQ=[]
for gi,(t,L) in enumerate(VOC):
    for w,p,m in L:
        others=[x[0] for x in L if x[0]!=w]
        rv.shuffle(others)
        VMCQ.append(('Which word or phrase means: “%s”'%m,[w]+others[:3],gi,'',0,0))
VMCQ+=[
('Shoppers like to ___ at the market to get a lower price.',['haggle','browse','track','bombard'],1,'haggle = argue about the price.',1,1),
('She found a great ___: the coat was half price.',['bargain','vendor','tag','stall'],1,'bargain = bought for less than the usual price.',1,1),
('The company uses ___ ads aimed at young adults.',['targeted','generic','cumbersome','bestselling'],0,'',1,1),
('The website wants to ___ delivery times so customers get goods faster.',['optimize','haggle','embrace','coincide'],0,'',1,1),
('The sale will ___ the school holiday, so many families can come.',['coincide with','embrace','formulate','customize'],0,'',1,1),
('Companies ___ us with messages every day.',['bombard','browse','eavesdrop','haggle'],2,'',1,1),
('It is rude to ___ on other people’s private conversations.',['eavesdrop','trace','spark','invade'],2,'',1,1),
('Her kind words were ___ and cheered everyone up.',['uplifting','misleading','severe','cumbersome'],3,'',1,1),
('The suspect was ___, so he was set free.',['innocent','severe','targeted','prominent'],2,'',1,1),
('The police could not ___ the phone call.',['trace','stir','extend','assume'],2,'trace = find the source.',1,1)]
VFILL=[
('Text 1 a','The company spends millions on {0} to promote its new phone.',[['advertising']]),
('Text 1 b','Her new book is a {0} novel; millions of copies have been sold.',[['bestselling']]),
('Text 1 c','Can you {0} the app so that it suits your needs?',[['customize','customise']]),
('Text 1 d','The suitcase was too {0} to carry up the stairs.',[['cumbersome']]),
('Text 2 a','My uncle likes to {0} at the market to get a lower price.',[['haggle']]),
('Text 2 b','I bought this jacket in a {0} shop; someone else owned it before.',[['second-hand','secondhand','second hand']]),
('Text 2 c','Before you buy a laptop, you should {0} to compare prices.',[['shop around']]),
('Text 2 d','This cup is {0}; the potter made it by hand.',[['handcrafted']]),
('Text 2 e','A coat for half price is a real {0}!',[['bargain']]),
('Text 2 f','He set up a {0} at the market to sell fruit.',[['stall']]),
('U2 Text 2 a','Do not {0} that she knows the answer without asking her.',[['assume']]),
('U2 Text 2 b','Hackers tried to {0} into the school’s computer system.',[['hack']]),
('U2 Text 2 c','I like to {0} the shelves in the bookshop with no plan.',[['browse']]),
('U2 Text 2 d','Spending too long online can have bad {0}.',[['consequences']]),
('U2 Text 2 e','You must ask for {0} before you use someone else’s photo.',[['permission']]),
('U2 Text 2 f','The singer’s video went {0} overnight and millions watched it.',[['viral']]),
('Life skill a','Many people share funny {0} that spread quickly online.',[['memes']]),
('Life skill b','Please send me a {0} instead of posting on my page.',[['direct message']]),
('Life skill c','After a sad week, the happy song was very {0}.',[['uplifting']])]
eng_page('eng-vocab','mcqBestEngVocab','Vocabulary '+T('詞彙',''),T('Unit 1 同 Unit 2 詞彙表：配對、填空、選擇題','Unit 1 and Unit 2 glossaries: match, fill in and quiz'),'scroll',VNOTES,VSETS,VFILL,VMCQ,'ev-i',
 T('詞彙同解釋來自學校 Unit 1 / Unit 2 Glossary；填空句子同「挑戰題」係【AI 出題】。','Words and meanings come from the school Unit 1 / Unit 2 glossaries; the fill-in sentences and challenge questions are AI-made.'),
 T('中二英文上學期統一測驗詞彙溫習。','F.2 English first-term uniform test vocabulary revision.'))

# ---------- Reading: Unit 2 Text 2 "Watching your step" (p.40-43) ----------
RDN=[
('Text 2 in short — paragraphs 1-3'+T(' 段落重點',''),
 P(G(K('Para 1')+' Derek Shum chats with his wife about a holiday while they prepare breakfast. Soon his social media is bombarded with ads for cruises, tours and package holidays, because their new smart speaker was eavesdropping on them.','第 1 段：智能喇叭偷聽，Derek 之後收到度假廣告。'))+
 P(G(K('Para 2')+' Because we rely on the Internet, our lives are no longer private: websites track our online behaviour, mobile devices record our movements, smart speakers listen in, and people hack into websites and steal information. We have very little control over who has access to it.','第 2 段：我哋依賴互聯網，私隱冇咗。'))+
 P(G(K('Para 3')+' Companies track us to deliver targeted ads that match our interests. Targeted ads can be helpful, but the writer feels uncomfortable because the information is used without our knowledge or permission.','第 3 段：公司追蹤瀏覽習慣送出針對性廣告；作者唔舒服係因為資料未經同意被使用。'))),
('Text 2 in short — paragraphs 4-5'+T('',''),
 P(G(K('Para 4')+' When information falls into the wrong hands the consequences can be severe: people have been threatened, harassed and attacked because of doxing. Pictures are easy to share but can be misleading when taken out of context, so innocent people have become targets. The damage can be long-lasting and extend to family and friends.','第 4 段：資料落入壞人手中後果嚴重（doxing）；圖片斷章取義會誤導。'))+
 P(G(K('Para 5')+' Protect ourselves: know that our digital footprint can be impossible to remove completely, be careful what we share online, respect other people’s privacy, and always assume that somebody is watching.','第 5 段：保護自己嘅方法。')))]
RDSETS=[('Phrases in Text 2',[['browsing habits','how we look at information on the internet'],['targeted ads','ads that match our interests'],['falls into the wrong hands','gets into the control of bad people'],['doxing','making a person’s private information public'],['taken out of context','used without the situation around it'],['digital footprint','traces of our online activity']])]
RDFILL=[
('Vocabulary 1','I hate it when my parents {0} me with questions first thing in the morning!',[['bombard']]),
('Vocabulary 2','Tina and Jodie caught me trying to {0} on their conversation.',[['eavesdrop']]),
('Vocabulary 3','I’ll go to the bookshop and {0} through the magazines while I wait for you.',[['browse']]),
('Vocabulary 4','The parents found their missing daughter by {0} her digital footprint.',[['tracing','tracking']]),
('Life skill 1','Sharing positive {0} can spread positive messages and build community.',[['hashtags']]),
('Life skill 2','Positive and uplifting posts often go {0}, spreading very quickly.',[['viral']]),
('Life skill 3','Funny cat {0} bring joy into people’s lives on a daily basis.',[['memes']]),
('Life skill 4','Online communities where people post helpful and informative {0}.',[['threads']]),
('Life skill 5','{0} sometimes invade these communities and post unhelpful comments.',[['Trolls','trolls']]),
('Life skill 6','If someone is at risk of being {0}, send them a direct message to warn them.',[['doxed']])]
RDMCQ=[
('What were Derek and his wife talking about?',['their holiday plans','their favourite music','their new smart speaker','what to have for breakfast'],0,'Para 1.',0,0),
('Why did Derek’s social media show ads for cruises and tours?',['The smart speaker was eavesdropping on their talk.','He searched for cruises online.','His friends shared the ads.','Websites chose them at random.'],0,'Para 1.',0,0),
('Why did Derek think nobody was listening?',['Only he and his wife were there.','The speaker was switched off.','He did not own a smart speaker.','He was talking on the phone.'],0,'Para 1: he was chatting with his wife.',0,0),
('Paragraph 2: “It is impossible to break into a website.” This is …',['False','True','Not Given'],0,'People hack into websites.',0,0),
('Paragraph 2: “Mobile devices can be used to track our location.” This is …',['True','False','Not Given'],0,'Devices record our movements.',0,0),
('Paragraph 2: “It is possible to buy smart speakers that do not monitor your conversations.” This is …',['Not Given','True','False'],0,'The text does not say.',0,0),
('In paragraph 2, “they” (line 11) refers to …',['people who have access to our information','smart speakers','mobile devices only','Derek and his wife'],0,'who has access to that information, or what they do with it.',0,0),
('What makes it easier for companies to sell goods and services?',['Our browsing habits help them deliver targeted ads.','Smart speakers talk to customers.','People trust all online ads.','Hackers share ads.'],0,'Para 3.',0,0),
('Why does the writer feel uncomfortable in paragraph 3?',['Her information is used without her knowledge.','Ads affect her browsing.','She is upset about being asked for permission.','She is worried about being hacked.'],0,'Para 3.',0,0),
('Find a word in paragraph 4 that means “small pieces”.',['snippets','consequences','emotions','victims'],1,'snippet = a small piece of information.',0,0),
('Why are some people wrongly accused online?',['Pictures can be misleading when taken out of context.','Hackers always tell the truth.','Companies track their ads.','Smart speakers listen to them.'],1,'Para 4.',0,0),
('Which of the following does the article recommend?',['all of the above','assuming that your online conversations are being monitored','being careful with what you post online','treating your friends’ information with respect'],2,'Para 5.',0,0),
('What is the best alternative headline for this article?',['Privacy under attack','Smart speakers are a terrible idea','The rise and fall of online shopping','Watch out for online criminals!'],2,'',1,0)]
eng_page('eng-read','mcqBestEngRead','Reading '+T('閱讀理解',''),T('Unit 2 Text 2 Watching your step · Life skill 詞彙運用','Unit 2 Text 2 Watching your step · Life skill vocabulary in use'),'camp',RDN,RDSETS,RDFILL,RDMCQ,'er-i',
 T('跟課本 Unit 2 Text 2（p.40-43）同 Life skill（p.44）；題目改寫自課本 Comprehension 2，答案對返文章同老師批改。Unit 1 兩篇文章仲未有。','Based on Unit 2 Text 2 (pp.40-43) and the Life skill page (p.44); questions are adapted from Comprehension 2 with answers checked against the text and the teacher’s corrections. The two Unit 1 texts are still missing.'),
 T('中二英文上學期統一測驗閱讀理解溫習。','F.2 English first-term uniform test reading revision.'))

# ---------- Proofreading (SIG Unit 1 Consolidation, Unit 2 Practice 8 + common errors) ----------
PFN=[
('How to proofread'+T(' 改錯方法',''),
 P(G(K('1')+' Read the whole sentence. Find the ONE wrong word or phrase.','先睇成句，搵出一個錯處。'))+
 P(G(K('2')+' Ask: which grammar point is it? comparative / superlative, as … as, if-clause (will?), past continuous or simple past, subject–verb agreement, spelling of the form.','諗吓係邊個文法點。'))+
 P(G(K('3')+' Write the corrected word(s) only, and read the sentence again.','只寫改正嘅字，再讀一次。'))),
('Common errors from the textbook'+T(' 課本常見錯誤',''),
 TB(['✘ Wrong','✔ Right'],[
  ['The price is more higher than expected.','The price is higher than expected.'],
  ['Jeffrey is the most tallest of the four boys.','Jeffrey is the tallest of the four boys.'],
  ['The cheesecake is as tastier as the chocolate cake.','The cheesecake is as tasty as the chocolate cake.'],
  ['If you will join the programme, you will get a discount.','If you join the programme, you will get a discount.'],
  ['Tom was making a model when the fire was breaking out.','Tom was making a model when the fire broke out.'],
  ['Many people was queuing up outside the cafe.','Many people were queuing up outside the cafe.'],
  ['No two flea markets are like.','No two flea markets are alike.']])),
('Clues to look for'+T(' 搵線索',''),
 TB(['Clue','Check'],[
  ['more / most + word ending in -er / -est','delete more / most'],
  ['less + countable noun','fewer'],
  ['will in an if-clause','simple present'],
  ['as + comparative + as','plain adjective'],
  ['when (short action) + was/were + -ing','simple past'],
  ['while + two actions at once','past continuous both'],
  ['like / alike','like + noun; alike alone']]))]
PFSETS=[('Fix the error',[['more higher','higher'],['the most tallest','the tallest'],['as tastier as','as tasty as'],['If you will join','If you join'],['the remarkablest','the most remarkable'],['more good','better']]),
 ('Fix the error 2',[['less people','fewer people'],['the least items','the fewest items'],['different as','different from'],['are like (No two are like.)','are alike'],['was breaking out','broke out'],['many people was','many people were']])]
def PF(t,sent,wrong,ans): return (t,sent+'  (Wrong: “%s”)  Correct: {0}'%wrong,[ans])
PFFILL=[
PF('SIG U2 1','Tom was making a model when the fire was breaking out.','was breaking',['broke']),
PF('SIG U2 2','Molly was cooking while her brother watched TV.','watched',['was watching']),
PF('SIG U2 3','Michael was daydreaming while he heard the thunder.','while',['when']),
PF('SIG U2 4','They were sleeping when their parents were leaving home.','were leaving',['left']),
PF('SIG U2 5','David was taking a shower when the water was running out.','was running',['ran']),
PF('SIG U2 6','What did Cindy doing while it was raining outside?','did',['was']),
PF('SIG U2 7','Was the boy listening to his teacher when she was talking to him?','when',['while']),
PF('SIG U2 8','When we arrived, many people was queuing up outside the cafe.','was',['were']),
PF('SIG U2 9','Were you taking the lift when the electricity was going out this morning?','was going',['went']),
PF('SIG U1 1','I’ve always thought it’s more interesting kind of market in the world.','more interesting',['the most interesting']),
PF('SIG U1 2','There are probably most curious things in a flea market than in any department store.','most',['more']),
PF('SIG U1 3','If you go there just once, you are agree with me.','are',['will']),
PF('SIG U1 4','I went to the one most close to my home.','most close',['closest']),
PF('SIG U1 5','I chose a weekday as there would be less people.','less',['fewer']),
PF('SIG U1 6','If you will observe carefully, you will notice that every flea market has its own characteristics.','will observe',['observe']),
PF('SIG U1 7','It probably has the least items among the flea markets, but the items are more good.','the least',['the fewest']),
PF('SIG U1 8','It’s quite different as the ones we’re using.','as',['from']),
PF('SIG U1 9','I think the rotary dial is the remarkablest.','the remarkablest',['the most remarkable']),
PF('SIG U1 10','It was the same height from a tall man.','from',['as']),
PF('SIG U1 11','It was as heavier as ten people!','heavier',['heavy']),
PF('SIG U1 12','You will probably found something that interests you.','found',['find']),
PF('SIG U1 13','I think the most good part of a flea market is the nice surprises it offers.','the most good',['the best']),
PF('SIG U1 14','No two flea markets are like.','like',['alike']),
PF('SIG U3 1','Before potato crisps emerged, people had enjoy potato chips as snacks.','had enjoy',['had enjoyed']),
PF('SIG U3 2','A customer kept sending back the chips that Crum has prepared.','has prepared',['had prepared']),
PF('SIG U3 3','By the 1920s, potato crisps not gain widespread popularity.','not gain',["hadn't gained",'had not gained']),
PF('SIG U3 4','After entrepreneur Laura Scudder invent an innovative method of sealing crisps, the snack began to sell well.','invent',['invented']),
PF('SIG U3 5','Potato crisps have been in their original flavour before Tayto invented the seasoning technology.','have been',['had been'])]
PFMCQ=[
('Which sentence is correct?',['The price is higher than expected.','The price is more higher than expected.','The price is the higher than expected.','The price is most high than expected.'],1,'',0,1),
('Which sentence is correct?',['Jeffrey is the tallest of the four boys.','Jeffrey is the most tallest of the four boys.','Jeffrey is the more tall of the four boys.','Jeffrey is tallest than the four boys.'],1,'',0,1),
('Which sentence is correct?',['If you join the programme, you will get a discount.','If you will join the programme, you will get a discount.','If you joined the programme, you will get a discount.','If you joins the programme, you will get a discount.'],1,'',0,1),
('Which sentence is correct?',['Fewer people came yesterday than today.','Less people came yesterday than today.','Few people came yesterday than today.','The fewer people came yesterday than today.'],0,'Countable noun → fewer.',0,1),
('Which sentence is correct?',['They were sleeping when their parents left home.','They were sleeping when their parents were leaving home.','They slept when their parents were leaving home.','They were sleeping while their parents left home.'],1,'Short action → simple past.',0,1),
('Which sentence is correct?',['While I was taking a shower, my brother took some books.','While I took a shower, my brother was taking some books.','While I was taking a shower, my brother was took some books.','When I was taking a shower, my brother taking some books.'],1,'',0,1),
('Which sentence is correct?',['No two flea markets are alike.','No two flea markets are like.','No two flea markets alike are.','No two flea markets are likes.'],2,'',0,1),
('Which sentence is correct?',['My room is not as big as my brother’s.','My room is not as bigger as my brother’s.','My room is not so bigger than my brother’s.','My room not as big as my brother’s.'],0,'',1,1),
('Which sentence is correct?',['Many people were queuing up outside the cafe when we arrived.','Many people was queuing up outside the cafe when we arrived.','Many people queuing up outside the cafe when we arrived.','Many people were queue up outside the cafe when we arrived.'],0,'',1,1),
('Which sentence is correct?',['Were you taking the lift when the electricity went out?','Were you taking the lift when the electricity was going out?','Was you taking the lift when the electricity went out?','Did you taking the lift when the electricity went out?'],0,'',1,1)]
eng_page('eng-proof','mcqBestEngProof','Proofreading '+T('改錯',''),T('SIG Unit 1 綜合練習、Unit 2 Practice 8：搵錯處同改正','SIG Unit 1 consolidation and Unit 2 Practice 8: find and fix the error'),'notebook',PFN,PFSETS,PFFILL,PFMCQ,'ep-i',
 T('改錯句子改寫自 SIG Unit 1 綜合練習同 Unit 2 Practice 8（標「SIG」）；選擇題係【AI 出題】。','Error sentences are adapted from the SIG Unit 1 consolidation and Unit 2 Practice 8 (marked “SIG”); quiz questions are AI-made.'),
 T('中二英文上學期統一測驗改錯溫習。','F.2 English first-term uniform test proofreading revision.'))

# ---------- Reading Unit 1 (Oxford English Forward 2A pp.4-11) ----------
R1N=[
('Text 1 — How big data improves online shopping (p.4-5)'+T('',''),
 P(G(K('Para 1')+' Amazon began by selling books online; today online shopping is commonplace. The writer thinks it gives a far more customized experience than bricks-and-mortar shops.','第 1 段：網購好普遍，作者認為比實體店更貼身。'))+
 P(G(K('Para 2')+' Every click is tracked; this data is combined with information from social media and search engine queries to create big data. Companies analyse it to find patterns and trends, formulate strategies and drive sales.','第 2 段：追蹤每一下點擊，同社交媒體、搜尋資料結合成 big data。'))+
 P(G(K('Para 3')+' Marketing can match customers’ preferences: targeted emails instead of generic ones (boutique, online pharmacy, cosmetics shop, florist). The writer believes individualized marketing beats blanket advertising.','第 3 段：針對性電郵，作者唔鍾意收到唔相關嘅電郵。'))+
 P(G(K('Para 4')+' Businesses optimize site design from data; asking customers directly was lengthy and cumbersome. They can be more responsive and give bestselling products a more prominent position.','第 4 段：用數據取代又長又麻煩嘅問卷。'))+
 P(G(K('Para 5')+' Customer service: the writer’s problem at an online optician’s was solved by a message with a link to his basket, plus a free-shipping coupon — a favourable impression.','第 5 段：網上眼鏡店嘅好服務經驗。'))+
 P(G(K('Para 6')+' The writer would rather visit online shops that tailor the experience to his specific needs than shops that treat everyone the same.','第 6 段：作者寧願去度身訂造嘅網店。'))),
('Text 2 — Support local artisans at Handcrafted! (p.8-9)'+T('',''),
 P(G('A leaflet for a monthly market (8 a.m.–8 p.m., first Sunday of every month, West Kowloon Cultural District) selling locally designed, handmade products.','宣傳單張：每月第一個星期日，西九文化區。'))+
 P(G(K('Reasons to visit')+' sustainable shopping (local sources, recycled materials); bargain hunters find great deals on unique items; vendors are happy to haggle; special offer: a free reusable shopping bag if you spend $200 or more.','來嘅理由。'))+
 P(G(K('What you’ll find')+' 132 stalls (snacks, gifts, homeware, stylish furniture by young local artisans), a few second-hand dealers selling rare vintage items, workshops (try your hand at making accessories), game stalls and live music from local indie bands.','會見到咩。'))+
 P(G(K('Getting there / contact')+' MTR to Kowloon Station (Tung Chung Line) or Green Minibus 77M to Austin Road West; website and phone for enquiries.','交通同查詢。')))]
R1SETS=[('Text 1 phrases',[['bricks-and-mortar shops','physical shops (not online)'],['big data','very large sets of information'],['targeted emails','aimed at a particular group'],['generic emails','general, not specific'],['lengthy and cumbersome','too long and troublesome'],['favourable impression','a good feeling about the shop']]),
 ('Text 2 phrases',[['bargain hunters','people looking for things at low prices'],['vendors','companies or people who sell things'],['haggle','argue about the price'],['special offer','sold at less than the usual price'],['vintage items','typical of a period in the past, high quality'],['try your hand at','do something for the first time']])]
R1FILL=[
('Text 1 a','Some footwear companies let you {0} your shoes — you can choose the colours.',[['customize','customise']]),
('Text 1 b','The shop was so busy that the staff served customers {0}. (without stopping)',[['non-stop','nonstop']]),
('Text 1 c','The stationery shop’s sale was timed to {0} with the start of school.',[['coincide']]),
('Text 1 d','Online shopping lets people shop quickly and {0}.',[['efficiently']]),
('Text 1 e','The department store’s new layout has been {0} for younger shoppers.',[['tailored']]),
('Text 2 a','As people become more environmentally conscious, many seek to shop more {0}.',[['sustainably']]),
('Text 2 b','I got a good {0} on this laptop during a flash sale.',[['deal']]),
('Text 2 c','The staff at the bookshop did not like it when I tried to {0} with them over their prices.',[['haggle']]),
('Text 2 d','Do you like my {0} dress? I bought it at a second-hand market!',[['vintage']]),
('Text 2 e','Can you recommend a shop that sells {0}? We are updating everything from sofas to kitchen utensils.',[['homeware']])]
R1MCQ=[
('Paragraph 1: which is NOT true about online shopping?',['None of the above','It is not uncommon to shop online nowadays.','Online shops can suit the needs of individual customers.','People can buy a wide range of products online.'],0,'A, B and C are all true.',0,0),
('Find a word or phrase in paragraph 1 similar in meaning to “physical”.',['bricks-and-mortar shops','commonplace','customized','online shopping'],0,'',0,0),
('According to paragraph 2, where does big data come from?',['Tracking online behaviour combined with social media and search engine queries','Only from emails the shops send','Only from the shops’ staff','Government records'],0,'',0,0),
('Paragraph 2: “Some countries have laws about data tracking and big data.” This is …',['Not Given','True','False'],0,'',0,0),
('Paragraph 2: “Most companies do not care about their customers’ preferences.” This is …',['False','True','Not Given'],0,'Companies analyse big data to find trends.',0,0),
('Paragraph 2: “Your data can be tracked even if you never shop online.” This is …',['True','False','Not Given'],0,'Teacher’s answer: True.',1,0),
('In paragraph 2, “them” (line 16) refers to …',['companies that analyse big data','customers','online shops only','patterns and trends'],0,'',0,0),
('In paragraph 3, the writer says he dislikes …',['receiving emails that do not match his needs','individualized marketing','receiving emails that advertise blankets','special occasions'],0,'',0,0),
('What is the main idea of paragraph 3?',['how companies use big data to market products','how florists take advantage of online tracking','when different types of shops use big data','why companies no longer use traditional marketing'],0,'',0,0),
('Find two words in paragraph 4 showing the writer’s negative attitude to traditional feedback.',['lengthy and cumbersome','responsive and prominent','automatic and various','directly and efficient'],0,'',0,0),
('The optician’s helped the writer solve his problem by …',['sending him a message with a special link','offering him a coupon code','offering him free shipping','recommending a few items to him'],0,'',0,0),
('What is the writer’s attitude towards big data in online shopping?',['Positive: it makes shopping more personalized','Negative: it wastes his time','Neutral: he does not mind','Worried about his privacy'],0,'Paragraph 6.',0,0),
('What is the purpose of the Handcrafted! leaflet?',['to promote the market and give visitors useful information','to sell products online','to warn people about prices','to recruit artisans'],1,'',0,0),
('Paragraph 1: “Handcrafted! is held in Kowloon Tong.” This is …',['False','True','Not Given'],1,'It is held at West Kowloon Cultural District.',0,0),
('Paragraph 1: “Handcrafted! is held every weekend.” This is …',['False','True','Not Given'],1,'First Sunday of every month.',0,0),
('Paragraph 1: “Handcrafted! is organized by a group of local artisans.” This is …',['Not Given','True','False'],1,'',0,0),
('Why does buying locally made goods help the environment?',['Everything comes from local sources and many items use recycled materials.','The market is held at night.','Shoppers pay in cash.','The goods are imported.'],1,'',0,0),
('According to paragraphs 2 and 3, which is true about the market?',['Visitors can choose from a large range of items.','All visitors get a free reusable bag.','Some items are imported from overseas.','Items are sold at fixed prices.'],1,'',0,0),
('Which word in paragraph 3 suggests the goods are very special?',['unique','amazing','friendly','cheaper'],1,'',0,0),
('How will the vendors feel about customers bargaining with them?',['Positive','Negative','Neutral'],1,'They are happy to haggle.',0,0),
('There are ___ a hundred stalls in the market.',['more than','nearly','less than','almost'],1,'132 stalls.',0,0),
('Which is the least likely to be found in the market?',['a performance by a band from Japan','a stall selling collectibles from the 1980s','a stool made from local wood','a workshop on making bracelets'],1,'Local indie bands play.',1,0),
('Which of the following does the leaflet NOT contain?',['background information about the stallholders','details about the types of goods','how to contact the organizers','transport information'],1,'',1,0),
('Find a phrase in paragraph 6 that means “to do something for the first time”.',['try your hand','enquire about','shop around','coincide with'],1,'',0,0)]
eng_page('eng-read1','mcqBestEngRead1','Reading '+T('Unit 1 閱讀理解',' — Unit 1'),T('Unit 1 Text 1《How big data improves online shopping》· Text 2《Handcrafted!》','Unit 1 Text 1 “How big data improves online shopping” · Text 2 “Handcrafted!”'),'farm',R1N,R1SETS,R1FILL,R1MCQ,'er1-i',
 T('跟課本 Unit 1（p.4-11）；題目改寫自 Comprehension 1 同 2，答案對返文章同老師批改。','Based on Unit 1 (pp.4-11); questions adapted from Comprehension 1 and 2, answers checked against the texts and the teacher’s corrections.'),
 T('中二英文上學期統一測驗 Unit 1 閱讀溫習。','F.2 English first-term uniform test Unit 1 reading revision.'))

# ---------- School past-paper practice (answers + parallel practice) ----------
PPN=[
('The practice paper'+T(' 試卷格式',''),
 TB(['Section','Marks'],[['A Reading Comprehension','20'],['B Vocabulary (first letters given)','10'],['C Tenses','10'],['D Gap Filling (conditionals)','10'],['E Cloze Passage (comparatives / superlatives)','10'],['F MC Cloze','10'],['G Proofreading (on the answer sheet)','10'],['H Bonus (not compulsory)','10']])+
 P(G('1 hour · 80 marks (pass 40) · bonus 10 marks · write answers on the answer sheet · “Make sure your answers are grammatically correct.”','1 小時、80 分（合格 40）、另加 10 分 bonus；要寫文法正確嘅答案。'))),
('Answers A–B: Reading and Vocabulary'+T('',''),
 P('<b>A (“When Renting Homes Takes a Turn for the Worse”)</b>: 1 A · 2 disappointed · 3 (a) F (b) NG (c) T · 4 (a) ruined (b) deterred (c) promptly · 5 rubbish everywhere; many dirty dishes in the sink; a flooded kitchen that ruined his sneakers · 6 (a) shocked (b) privacy · 7 the beds · 8 No: the losses were not made up for in the end · 9 do research beforehand; buy travel insurance · 10 open answer · 11 B (cautious).')+
 P('<b>B</b> (words from Oxford English Forward 2A Units 1-2): 1 formulated · 2 big data · 3 sources · 4 sparked · 5 cumbersome · 6 eavesdrop · 7 reliance · 8 assumed · 9 consequences/consequence · 10 embrace.')),
('Answers C–F: Grammar sections'+T('',''),
 P('<b>C Tenses</b>: 1 started · 2 had moved · 3 had already bought · 4 was looking · 5 were walking · 6 were taking · 7 were riding · 8 had explored · 9 will visit (are going to visit) · 10 enjoy.')+
 P('<b>D Conditionals</b>: 1 will violate (violate) · 2 have · 3 will not be allowed (are not allowed) · 4 need · 5 will find · 6 is · 7 are not · 8 should avoid · 9 follow · 10 will enjoy.')+
 P('<b>E Cloze</b> (each adjective once): 1 the most popular · 2 farther/further · 3 easier · 4 more crowded · 5 less fit · 6 taller than · 7 worse than · 8 rarer · 9 the least expensive · 10 the most memorable.')+
 P('<b>F MC cloze</b>: 1 D · 2 A · 3 B · 4 B · 5 A · 6 C · 7 C · 8 C · 9 C · 10 D.')),
('H Bonus'+T('',''),
 P('Comprehension: 1 rising rates of anxiety and depression · 2 late-night scrolling or disruptive notifications disrupt sleep · 3 it is vital for physical and mental health, brain growth, cognitive growth and emotional regulation. Response (7 marks): give ONE rule (e.g. no phone after 9 p.m.), a reason and how it helps.')+
 P(G('The paper itself is not copied here (school paper); these are answer notes made from it. Section G Proofreading has no text in the PDF.','試卷原文唔放上網；呢度只係答案筆記。G 部改錯喺答案紙，PDF 冇原文。')))]
PPSETS=[('Section E skills',[['one of the ___ ski villages','the most popular'],['70 km from Beijing, ___ than other resorts','farther / further'],['It is a lot ___ to ski on thin snow','easier'],['not as ___ as my sister','less fit'],['___ than my sister (long legs)','taller than'],['the ___ ski village I have ever visited (cheapest)','the least expensive']]),
 ('Section F skills',[['___ watching a concert','the same as'],['they are ___ in their love for music','alike'],['among global cities, offers ___ spots','the fewest'],['treats us ___ seasoned artists','like'],['earns ___ money than before','less'],['___ forms of performances in the past','fewer']])]
PPFILL=[
('C Tenses 1','Last Sunday our morning {0} (start) at the pier. Before my brother, who {1} (move) out recently, arrived, Mum {2} (already / buy) tickets.',[['started'],['had moved'],['had already bought']]),
('C Tenses 2','Dad {0} (look) for a restaurant while we {1} (wait) for him.',[['was looking'],['were waiting']]),
('C Tenses 3','While we {0} (walk) along the waterfront, tourists {1} (take) photos.',[['were walking'],['were taking']]),
('C Tenses 4','We {0} (ride) the escalator when it began to rain.',[['were riding']]),
('C Tenses 5','By the time the rain stopped, we {0} (explore) the old station.',[['had explored']]),
('C Tenses 6','Next weekend, we {0} (visit) the Peak. We always {1} (enjoy) exploring the city.',[['will visit',"'ll visit",'are going to visit'],['enjoy']]),
('D Conditionals 1','If you {0} (not remove) your shoes before entering, you {1} (violate) a basic rule.',[["don't remove",'do not remove'],['will violate','violate']]),
('D Conditionals 2','If you {0} (have) tattoos, you {1} (not allow) to enter the facility.',[['have'],['will not be allowed','are not allowed',"won't be allowed"]]),
('D Conditionals 3','When you visit, you {0} (need) to wash before entering. If you {1} (be, not) well, you {2} (avoid) hot baths.',[['need'],['are not',"aren't"],['should avoid']]),
('D Conditionals 4','If you {0} (follow) these rules, you {1} (enjoy) a peaceful experience.',[['follow'],['will enjoy']])]
PPMCQ=[
('Some people think a live show is ___ watching a video of it.',['the same as','alike','likes','the same of'],3,'',0,1),
('Live music brings ___ energy to the city.',['more','most','less','least'],3,'',0,1),
('Singers and dancers come from all backgrounds, but they are ___ in their love for music.',['alike','like','the same as','as eager as'],3,'',0,1),
('Among the cities in Asia, our city offers ___ public pianos. (the smallest number)',['the fewest','fewer','less','the least'],3,'',1,1),
('The audience treats us ___ seasoned artists.',['like','alike','as same as','more'],3,'',0,1),
('Performing in a hall gives her ___ satisfaction than busking.',['less','least','fewer','more satisfying'],3,'',0,1),
('Their reactions are totally ___ those in a theatre.',['as exciting as','different of','more exciting','different'],3,'',1,1),
('She earns ___ money per hour than she did teaching.',['less','fewer','the least','least'],3,'Money is uncountable.',0,1),
('There were ___ forms of performances in the past.',['fewer','fewest','less','the least'],3,'Forms are countable.',0,1),
('This is ___ skiing trip I have ever had. (the best experience)',['the most memorable','more memorable','memorable than','most memorable than'],3,'',1,1)]
eng_page('eng-paper','mcqBestEngPaper','Past paper '+T('歷屆試卷練習',''),T('學校 Form 2 練習卷：答案筆記同仿卷練習','School Form 2 practice paper: answer notes and parallel practice'),'notebook',PPN,PPSETS,PPFILL,PPMCQ,'epp-i',
 T('答案係根據學校練習卷（未有標準答案）自己計出；填空同選擇題係仿卷【AI 出題】，唔係原題。','Answers were worked out from the school practice paper (no marking scheme was given); fill-in and quiz items are AI-made parallels, not the original questions.'),
 T('中二英文上學期統一測驗歷屆試卷練習。','F.2 English first-term uniform test past-paper practice.'))

# ---------- hub ----------
def card(n,href,title,d,tags):
    return '  <a class="hub h%dc" href="../%s/"><strong>%s</strong><span class="d">%s</span>%s</a>\n'%((n%3)+1,href,title,d,''.join('<span class="tag">%s</span>'%t for t in tags))
CARDS=''.join([
 card(0,'eng-vocab','Vocabulary',T('Unit 1 同 Unit 2 詞彙表：73 個詞語（另加 Unit 1 店舖類型），配對、填空、選擇題。','Unit 1 and Unit 2 glossaries: 73 words with match, fill-in and quiz.'),['Unit 1','Unit 2']),
 card(1,'eng-read1','Reading — Unit 1',T('Unit 1 Text 1 同 Text 2 閱讀理解（24 條題）。','Unit 1 Text 1 and Text 2 comprehension (24 questions).'),['Text 1','Text 2']),
 card(2,'eng-read','Reading — Unit 2',T('Unit 2 Text 2《Watching your step》閱讀理解同 Life skill 詞彙運用。','Unit 2 Text 2 “Watching your step” comprehension and Life skill vocabulary in use.'),['Unit 2 Text 2']),
 card(2,'eng-adj','Adjectives',T('比較級、最高級、比較數量、as … as、like／alike。','Comparative and superlative adjectives, quantities, as … as, like / alike.'),['Unit 1 (A)(B)']),
 card(0,'eng-cond','Conditionals',T('Type 1（可能情況、情態動詞）同 Type 0（事實）。','Type 1 (possible situations, modals) and Type 0 (facts).'),['Unit 1 (C)','Unit 3 (C)']),
 card(1,'eng-tense','Tenses',T('過去進行式、when／while、過去完成式（補充）。','Past continuous, when / while, past perfect (extra).'),['Unit 2 (A)','Past perfect']),
 card(2,'eng-proof','Proofreading',T('SIG 改錯練習：搵出錯處再改正。','SIG error-correction practice: find and fix the mistake.'),['Proofreading']),
 card(0,'eng-paper','Past paper',T('學校 Form 2 練習卷：答案筆記同仿卷練習。','School Form 2 practice paper: answer notes and parallel practice.'),['A–H'])])
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
%(cards)s  <div class="stat"><h2>%(sth)s</h2><ul>%(stl)s</ul></div>
  <footer>%(foot)s</footer>
</div>
<script src="../assets/art.js"></script>
</body>
</html>
'''
hub=ENGHUB%dict(home=T('首頁','Home'),h1=T('中二英文','(Form 2)'),
 desc=T('中二英文上學期統一測驗溫習。','F.2 English first-term uniform test revision.'),
 scope=T('範圍','Syllabus'),cards=CARDS,
 scopetxt=T('<i>Oxford English Forward 2A</i> Unit 1-2；<i>Success in Grammar 2</i> Unit 1 (A)(B)(C)、Unit 2 (A)、Unit 3 (C)；過去完成式補充筆記。題型：Reading、Vocabulary、Tenses、Gap Filling、Cloze、MC Cloze、Proofreading、Bonus。','<i>Oxford English Forward 2A</i> Units 1-2; <i>Success in Grammar 2</i> Unit 1 (A)(B)(C), Unit 2 (A), Unit 3 (C); extra notes on the past perfect. Sections: Reading, Vocabulary, Tenses, Gap filling, Cloze, MC cloze, Proofreading, Bonus.'),
 sth=T('資料狀態','Material status'),
 stl=''.join('<li><span class="st %s">%s</span>%s</li>'%x for x in [
  ('',T('已對照','Checked'),T('文法筆記：跟 Success in Grammar 2 Unit 1-3 對照','Grammar notes: checked against Success in Grammar 2 Units 1-3')),
  ('',T('已對照','Checked'),T('詞彙：Unit 1、Unit 2 學校 Glossary 全部詞語','Vocabulary: every word in the school Unit 1 and Unit 2 glossaries')),
  ('',T('已對照','Checked'),T('閱讀：Unit 2 Text 2 同 Life skill（課本 p.40-44）','Reading: Unit 2 Text 2 and Life skill (textbook pp.40-44)')),
  ('',T('已對照','Checked'),T('過去完成式：老師筆記 + SIG Unit 3 A（含間接引語、wish）','Past perfect: teacher’s notes + SIG Unit 3 A (incl. reported speech and wish)')),
  ('',T('已對照','Checked'),T('閱讀：Unit 1 Text 1、Text 2（p.4-11）','Reading: Unit 1 Text 1 and Text 2 (pp.4-11)')),
  ('',T('已有','Done'),T('學校 Form 2 練習卷：答案筆記同仿卷練習（試卷冇標準答案，答案係自己計）','School Form 2 practice paper: answer notes and parallel practice (no marking scheme was given; answers were worked out)')),
  ('t',T('未收到','Missing'),T('其他年份歷屆試卷、練習卷 G 部改錯原文','Other past papers and the Section G proofreading text of the practice paper')) ]),
 foot=T('選擇題同挑戰題係【AI 出題】；其餘跟課本同學校資料。','Quiz and challenge questions are AI-made; everything else follows the textbook and school handouts.'))
if LANG=='en': hub=postEN(hub).replace('href="../../">','href="../../../">')
os.makedirs(ROOT+'eng',exist_ok=True)
open(ROOT+'eng/index.html','w',encoding='utf-8').write(hub)
