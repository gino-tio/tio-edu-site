FOOD=[
(T('Farming system 農業系統','Farming system'),'<p>'+K('Inputs → Processes → Outputs')+'</p>'+
 P(T('<b>Physical inputs 自然投入：</b>','<b>Physical inputs:</b> ')+'sunlight, air temperature, rainfall, seeds, land, soil nutrients'+T('（課本 6 樣）','')+'')+
 P(T('<b>Cultural inputs 人文投入：</b>','<b>Cultural inputs:</b> ')+'capital, fertilizers, pesticides, technology, labour, irrigation system, machines'+T('（課本 7 樣）','')+'')+
 P(T('<b>Processes 過程：</b>','<b>Processes:</b> ')+'ploughing, seeding, irrigating, fertilizing, weeding, harvesting')+
 P(T('<b>Useful outputs 有用產出：</b>','<b>Useful outputs:</b> ')+'farm produce（crops, meat, milk, wool）→ sold at the market → cash')+
 P(T('<b>Feedback 反饋：</b>賣農產品得到嘅 cash 再投入農場（買 cultural inputs）。<br><b>Cash crop 經濟作物</b> = 種嚟出售；<b>subsistence crop 自給作物</b> = 種嚟自己食。','<b>Feedback:</b> the cash earned from selling produce goes back into the farm (to buy cultural inputs).<br><b>Cash crop</b> = grown for sale; <b>subsistence crop</b> = grown for the farmer’s own food.'))+
 P(T('<b>Useless outputs 無用產出：</b>','<b>Useless outputs:</b> ')+'animal waste, crop residues, pollutants')+
 EG(T('2025-26 UT：dairy farm 嘅 useless output = animal waste（milk、meat 係 useful）。','2025-26 UT: the useless output of a dairy farm = animal waste (milk and meat are useful).'))),
(T('Types of farming 農業類型（四種分法）','Types of farming (four ways to classify)'),'<table class="tb"><tr><th>'+T('準則','Criterion')+'</th><th>'+T('類型','Type')+'</th><th>'+T('特點','Features')+'</th></tr>'
 '<tr><td rowspan=2>Amount of inputs per unit of land</td><td>Intensive</td><td>'+T('每單位土地投入多（多人手／資本），農場細','Large inputs per unit of land (many workers / much capital); small farms')+'</td></tr><tr><td>Extensive</td><td>'+T('每單位土地投入少，農場大','Small inputs per unit of land; large farms')+'</td></tr>'
 '<tr><td rowspan=3>Types of output</td><td>Arable</td><td>'+T('種農作物','Growing crops')+'</td></tr><tr><td>Pastoral</td><td>'+T('養牲畜','Rearing livestock')+'</td></tr><tr><td>Mixed</td><td>'+T('兩樣都有','Both crops and livestock')+'</td></tr>'
 '<tr><td rowspan=2>Uses of output</td><td>Subsistence</td><td>'+T('主要供農民同家人食用','Mainly for the farmer and family')+'</td></tr><tr><td>Commercial</td><td>'+T('主要出售賺錢','Mainly for sale')+'</td></tr>'
 '<tr><td rowspan=2>Level of technology</td><td>Low-technology</td><td>'+T('靠人力、牲畜、簡單工具','Labour, animals, simple tools')+'</td></tr><tr><td>High-technology</td><td>'+T('用大型先進機器','Large advanced machines')+'</td></tr></table>'),
(T('Examples 例子（考過）','Examples (seen in past papers)'),'<table class="tb"><tr><th>'+T('例子','Example')+'</th><th>'+T('類型','Type')+'</th></tr>'
 '<tr><td>Rice, Indonesia '+T('（相：人手收割）','(photo: harvesting by hand)')+'</td><td>Intensive · Arable · Low-technology</td></tr>'
 '<tr><td>Wheat, central USA '+T('（相：聯合收割機）','(photo: combine harvester)')+'</td><td>Extensive · Arable · High-technology · Commercial</td></tr>'
 '<tr><td>Rice, Laos</td><td>'+T('勞動力投入高、技術低、自用（subsistence）','High labour input, low technology, own consumption (subsistence)')+'</td></tr>'
 '<tr><td>Wheat-sheep, Australia</td><td>'+T('Mixed farming；每單位土地產量低（extensive）','Mixed farming; low output per unit area (extensive)')+'</td></tr>'
 '<tr><td>'+T('Indonesia 作物出口香港','Indonesian crops exported to Hong Kong')+'</td><td>Commercial farming</td></tr>'
 '<tr><td>'+T('Farm A：300 公頃、大型機器、牲畜、出售','Farm A: 300 ha, large machines, livestock, for sale')+'</td><td>Extensive · Pastoral · Commercial · High-tech</td></tr>'
 '<tr><td>'+T('Farm B：6 公頃、人力同牲畜、農作物、自用','Farm B: 6 ha, labour and animals, crops, for the family')+'</td><td>Intensive · Arable · Subsistence · Low-tech</td></tr></table>'+
 '<p>'+K(T('課本 Table 4（p.11-12）','Textbook Table 4 (pp.11-12)'))+'</p>'+
 '<table class="tb"><tr><th>'+T('例子','Example')+'</th><th>Intensive / Extensive</th><th>Arable / Pastoral / Mixed</th><th>Subsistence / Commercial</th><th>Technology</th></tr>'
 '<tr><td>A '+T('荷蘭 market gardening','Market gardening, Netherlands')+'</td><td>Intensive</td><td>Arable</td><td>Commercial</td><td>High</td></tr>'
 '<tr><td>B '+T('老撾高地稻米','Rice, upland Laos')+'</td><td>Extensive*</td><td>Arable</td><td>Subsistence</td><td>Low</td></tr>'
 '<tr><td>C '+T('澳洲東南 wheat-sheep','Wheat-sheep, SE Australia')+'</td><td>Extensive</td><td>Mixed</td><td>Commercial</td><td>High</td></tr>'
 '<tr><td>D '+T('紐西蘭乳牛','Dairy farming, New Zealand')+'</td><td>Extensive</td><td>Pastoral</td><td>Commercial</td><td>High</td></tr>'
 '<tr><td>E '+T('美國中部小麥','Wheat, central USA')+'</td><td>Extensive</td><td>Arable</td><td>Commercial</td><td>High</td></tr>'
 '<tr><td>F '+T('阿根廷肉牛','Beef cattle, Argentina')+'</td><td>Extensive</td><td>Pastoral</td><td>Commercial</td><td>Low</td></tr></table>'+
 P(T('<b>⚠ *老撾（B）：</b>課本 Table 4 剔咗 extensive，但 2025-26 統測 Q3 標準答案係 D，即 labour input per unit area = <b>High</b>（intensive）。考試以學校標準答案為準，建議問老師點睇。','<b>⚠ *Laos (B):</b> the textbook Table 4 is ticked extensive, but the 2025-26 UT Q3 marking scheme answer is D, i.e. labour input per unit area = <b>High</b> (intensive). Follow the school’s marking scheme in the exam and ask your teacher.'))+
 EG(T('2024-25 QE：Common farming process in both photos = harvesting。','2024-25 QE: the common farming process in both photos = harvesting.'))),
(T('計算：Farmers per unit of land','Calculation: farmers per unit of land'),'<p>'+K('Farmers per unit of land = Number of farmers ÷ Farm size')+'</p>'+
 EG(T('Farm A：300 公頃 × 0.01 = <b>3</b> 個農民（X = 3）','Farm A: 300 ha × 0.01 = <b>3</b> farmers (X = 3)'))+EG('Farm B: 12 ÷ 6 = <b>2</b> (Y = 2)')),
('Growing conditions & farming regions of China','<p>'+K(T('三大農業地區（課本 Unit 2）','Three farming regions (textbook Unit 2)'))+'</p>'+
 '<table class="tb"><tr><th></th><th>Xibei'+T(' 西北','')+'</th><th>Huabei &amp; Dongbei'+T(' 華北東北','')+'</th><th>Huanan'+T(' 華南','')+'</th></tr>'
 '<tr><td>Farm size</td><td>Large</td><td>Large</td><td>Small</td></tr>'
 '<tr><td>Type</td><td>'+T('Mainly extensive pastoral + 少量 arable','Mainly extensive pastoral, some arable')+'</td><td>Extensive arable + pastoral</td><td>Mainly intensive arable</td></tr>'
 '<tr><td>Outputs</td><td>Meat, milk, wool</td><td>Wheat, corn, potato, millet, soybean, wool</td><td>Rice, vegetables, tropical fruits</td></tr>'
 '<tr><td>Growing season</td><td>7–250 '+T('日','days')+'</td><td>7–250 '+T('日','days')+'</td><td>300–365 '+T('日','days')+'</td></tr>'
 '<tr><td>Rainfall</td><td>'+T('多數 &lt;600 mm','Mostly below 600 mm')+'</td><td>0–1,400 mm</td><td>600–over 1,400 mm</td></tr>'
 '<tr><td>Relief</td><td>'+T('山地、高原（Qing Zang / Huangtu Gaoyuan），泥土薄而貧瘠','Mountains and highlands (Qing Zang / Huangtu Gaoyuan); soil thin and infertile')+'</td><td>'+T('高原同低地；兩大平原 Dongbei Pingyuan、Huabei Pingyuan，泥土肥沃','Plateaux and lowlands; two plains: Dongbei and Huabei Pingyuan; soil fertile')+'</td><td>'+T('丘陵同低地；Zhujiang Delta 大片平地，泥土肥沃','Hills and lowlands; large lowland on the Zhujiang Delta; soil fertile')+'</td></tr></table>'+
 P(T('<b>Farming region 農業地區</b> = 農民種同類主要作物或養同類牲畜、用相似方法嘅地區。<br><b>糧倉：</b>2019 全國糧食 613.7 百萬噸；黑龍江 66.5、河南 65.2、山東 52（百萬噸）。Heilongjiang 佔比 = 66.5 ÷ 613.7 × 100% ≈ <b>10.8%</b>（correct to 1 d.p. = 10.8%）。','<b>Farming region</b> = an area where farmers grow the same major crops or raise the same livestock using similar methods.<br><b>Granary:</b> China’s 2019 grain output was 613.7 million tonnes; Heilongjiang 66.5, Henan 65.2, Shandong 52 (million tonnes). Heilongjiang’s share = 66.5 ÷ 613.7 × 100% ≈ <b>10.8%</b>.'))+
 P(T('<b>Climate 氣候</b> = 一個地方多年嘅平均天氣；<b>Relief 地勢</b> = 土地形狀（高度同斜度）。<b>Growing season 生長期</b> = 一年中可以種農作物嘅時期，受 rainfall 同 air temperature 影響；大部分作物要 ≥ 90 日。<br>小麥最低要 6°C、400 mm。<br>水稻 paddy：27–32°C（低過 12°C 唔可以種）、年雨量 &gt;1,000 mm。綿羊：−5 至 28°C、400–800 mm。','<b>Climate</b> = average weather of a place over many years; <b>relief</b> = shape of the land (height and steepness). <b>Growing season</b> = the period of a year when crops can be grown; it depends on rainfall and air temperature, and most crops need ≥ 90 days.<br>Wheat needs at least 6°C and 400 mm. Paddy: 27–32°C (cannot be grown under 12°C), annual rainfall over 1,000 mm. Sheep: −5 to 28°C, 400–800 mm.'))+
 P(T('<b>雨量：</b>由東南向西北遞減；沙漠區喺 <b>oasis 綠洲</b>種作物；雨量低、只有草 → pastoral。<b>氣溫：</b>南高北低 → growing season 南長北短（華南長）。<b>地勢：</b>由西向東遞減；西部多山、陡坡、崎嶇、泥土薄 → pastoral；東部平原同丘陵、泥土肥沃 → arable。<br>只有約 <b>15%</b> 國土適合農業；最好農地喺東部 <b>river valleys</b> 同 <b>near the coast</b>。','<b>Rainfall</b> decreases from south-east to north-west; in deserts crops are grown at <b>oases</b>; where rainfall is low and only grass grows → pastoral. <b>Temperature</b> is higher in the south → longer growing season in the south (Huanan). <b>Relief</b> falls from west to east; the west is mountainous with steep, rugged land and thin soil → pastoral; the east has plains and hills with fertile soil → arable.<br>Only about <b>15%</b> of China’s land is good for farming; the best farmland is in the east along river valleys and near the coast.'))+
 '<p>'+K('Wet rice')+T(' 嘅條件（歷屆試卷）：',' conditions (past papers):')+'</p>'+
 P(T('• Air temperature：27–32°C（QE 版：20–30°C），minimum 唔低過 12°C（QE：10°C）<br>• Annual rainfall：over 1,000 mm，growing season 每月至少 125 mm<br>• Growing season：至少 90 日<br>• In flooded fields（要水浸）<br>• Relief：平坦（plains / lowlands / delta）；Soil：深厚肥沃','• Air temperature: 27–32°C (QE version: 20–30°C), minimum not lower than 12°C (QE: 10°C)<br>• Annual rainfall: over 1,000 mm, at least 125 mm in each month of the growing season<br>• Growing season: at least 90 days<br>• Grown in flooded fields<br>• Relief: flat (plains / lowlands / delta); soil: thick and fertile'))+
 P(T('<b>Huanan Region 華南（Region C）：</b>氣溫高、全年暖；年雨量多（&gt;1,400 mm）；growing season 長（課本 300–365 日；試卷 180–365 日）；地勢平坦（Zhujiang Delta）；泥土深厚肥沃 → 適合種 wet rice，課本稱 mainly intensive arable。','<b>Huanan Region (Region C):</b> warm all year round; high annual rainfall (&gt;1,400 mm); long growing season (180–365 days); flat land (Zhujiang Delta); thick, fertile soil → favourable for wet rice, which is subsistence farming.'))+
 P(T('<b>Xibei Region 西北（Region A）：</b>minimum temperature −40°C；年雨量 &lt;600 mm；growing season 0–180 日；多山／高原（Qing Zang Gaoyuan / Himalayas）、地勢崎嶇；泥土薄而貧瘠、易水土流失 → 只適合 pastoral farming（放牧）。','<b>Xibei Region (Region A):</b> minimum temperature −40°C; annual rainfall &lt;600 mm; growing season 0–180 days; mountainous / plateau (Qing Zang Gaoyuan / Himalayas) with rugged relief; thin, infertile soil and easy soil erosion → only suitable for pastoral farming.'))+
 P(T('<b>影響中國農業分佈嘅因素：</b>relief、rainfall、temperature（三樣都係）。<br><b>影響 length of growing season：</b>rainfall、air temperature（唔係 air pressure）。','<b>Factors affecting the distribution of farming regions in China:</b> relief, rainfall and temperature (all three).<br><b>Factors affecting the length of the growing season:</b> rainfall and air temperature (not air pressure).'))+
 EG(T('適合農業：雨量 1,800 mm ✓；海拔 2,000 m ✗；growing season 20 日 ✗。','Favourable for farming: rainfall 1,800 mm ✓; height 2,000 m ✗; growing season 20 days ✗.'))),
(T('Hong Kong food supply 香港食物供應','Hong Kong food supply'),'<p>'+K(T('Local food production 佔比好細','The share of local food production is very small'))+'</p>'+
 P(T('• 大部分食物靠進口。<br>• Largest source of fresh food = <b>China</b>。<br>• Rice 主要由 <b>Thailand</b> 供應。<br>• 本地唔係生產大部分蔬菜（本地蔬菜只佔好細部分）。','• Most food is imported.<br>• Largest source of fresh food = <b>China</b>.<br>• The major source of rice = <b>Thailand</b>.<br>• Hong Kong does not produce most of the vegetables it consumes.'))+
 '<table class="tb"><tr><th>2019</th><th>Rice (thousand t)</th><th>Fresh vegetables (thousand t)</th><th>Live pigs &amp; cattle (thousand heads)</th></tr>'
 '<tr><td>Imported</td><td>317</td><td>847</td><td>16,112</td></tr>'
 '<tr><td>Local production</td><td>0 (0%)</td><td>15 (1.7%)</td><td>109 (0.7%)</td></tr>'
 '<tr><td>Major source</td><td>Thailand (~52%)</td><td>Mainland (&gt;90%)</td><td>Mainland (&gt;90%)</td></tr></table>'+
 P(T('<b>本地佔比</b> = 本地生產 ÷（進口 + 本地）× 100%：蔬菜 15 ÷ 862 ≈ 1.7%；豬牛 109 ÷ 16,221 ≈ 0.7%。→ 本地生產<b>非常細</b>。','<b>Local share</b> = local ÷ (imported + local) × 100%: vegetables 15 ÷ 862 ≈ 1.7%; pigs and cattle 109 ÷ 16,221 ≈ 0.7% → local production is <b>very small</b>.'))+
 P(T('<b>Staple food 主要糧食</b> = 一個社會經常食、佔飲食最大部分、係能量同營養主要來源；各地唔同。古代「五穀」一般指 wheat, rice, corn, millet, soybeans；<b>現時中國嘅 staple foods = rice, wheat, corn</b>。','<b>Staple foods</b> are eaten regularly in a community, make up the largest part of the diet and are the main source of energy and nutrients; they differ from place to place. The ancient “five grains” are commonly wheat, rice, corn, millet and soybeans; <b>China’s staple foods today = rice, wheat and corn</b>.'))),
(T('Food demand 食物需求','Food demand'),'<p>'+K('Factors affecting food demand')+'</p>'+
 P(T('<b>Population size</b>（人口數量）、<b>Level of income</b>（收入水平）。<br>「Local industrial production」唔係影響需求嘅因素。','<b>Population size</b> and <b>level of income</b>.<br>“Local industrial production” is not a factor affecting food demand.'))+
 P(T('<b>人口：</b>中國人口 1970 年 830 百萬 → 2019 年 1,400 百萬（increased）→ food demand 上升。<br><b>收入：</b>收入愈高，食愈多肉同奶製品、愈少 staple foods（1990→2019 人均：grains 131→111 kg ↓；meat 25→36 kg ↑；milk 5→17 kg ↑，升幅最大）。','<b>Population:</b> China’s population rose from 830 million (1970) to 1,400 million (2019) → food demand rises.<br><b>Income:</b> with higher income people eat more meat and dairy but fewer staple foods (per capita 1990→2019: grains 131→111 kg ↓; meat 25→36 kg ↑; milk 5→17 kg ↑, the biggest rise).'))),
(T('Food supply 食物供應 & self-sufficiency','Food supply and self-sufficiency'),'<p>'+K(T('Food demand &gt; food supply = food shortage','Food demand &gt; food supply = food shortage'))+'</p>'+
 P(T('<b>Food supply 來源：</b>① local production from farming（本地農業生產）② imports（進口）。<br><b>Food shortage 後果：</b>人民捱餓、營養不良 → 拖慢 economic development → 甚至 social unrest（社會動盪）。穩定糧食供應有助經濟增長。','<b>Sources of food supply:</b> ① local production from farming ② imports.<br><b>Consequences of food shortage:</b> hunger and poor nutrition → slows economic development → may even cause social unrest. A stable food supply supports economic growth.'))+
 P(T('<b>中國 2000–2018：</b>2000–2004 demand &gt; supply；2006 年起 supply &gt; demand。中國糧食（rice, wheat, corn）大部分本地生產，進口只佔好細部分。<br><b>Self-sufficiency rate 自給自足率</b>（grains）約 <b>95%</b> → 整體上中國生產到足夠食物；預計人口 2025 年起下降，自給率將繼續高。','<b>China 2000–2018:</b> demand &gt; supply in 2000–2004; supply &gt; demand since 2006. Most grain (rice, wheat, corn) is produced locally and imports are a very small share.<br>The <b>self-sufficiency rate</b> of grains is about <b>95%</b> → China generally produces enough food; population is projected to fall from 2025, so the rate will stay high.')))]
FOODMATCH=[('Intensive farming','High inputs per unit of land'),('Extensive farming','Low inputs per unit of land'),('Arable farming','Growing crops'),('Pastoral farming','Rearing livestock'),('Mixed farming','Both crops and livestock'),('Subsistence farming','Output mainly for the farmer’s family'),('Commercial farming','Output mainly for sale'),('High-technology farming','Large advanced machines'),('Low-technology farming','Labour, animals and simple tools'),('Physical input','Sunlight, soil, rainfall'),('Cultural input','Labour, machines, capital'),('Useless output','Animal waste, crop residue')]
FOODFILL=[
('Types',T('{0} farming：每單位土地投入多（農場細）。　{1} farming：每單位土地投入少（農場大）。','{0} farming: large inputs per unit of land (small farms).　{1} farming: small inputs per unit of land (large farms).'),[['intensive'],['extensive']]),
('Types 2','Growing crops = {0} farming; rearing livestock = {1} farming.',[['arable'],['pastoral']]),
('Types 3','Output mainly for the farmer’s family = {0} farming; output mainly for sale = {1} farming.',[['subsistence'],['commercial']]),
('Inputs','Sunlight, soil nutrients and rainfall are {0} inputs; machines and labour are {1} inputs.',[['physical'],['cultural']]),
('Process','Common farming process in both photos (collecting the crop): {0}.',[['harvesting','harvest']]),
('Calculation','Farm of 300 hectares, 0.01 farmers per hectare. Number of farmers = {0}.　6 hectares with 12 farmers → farmers per hectare = {1}.',[['3'],['2']]),
('China','Wet rice is favourably grown in the {0} Region (Region C) of China, which has the Zhujiang Delta.',[['huanan','south china']]),
('China 2','Xibei Region is mainly suitable for {0} farming because of thin, infertile soil and rugged relief.',[['pastoral']]),
('Rice','Wet rice needs to be grown in {0} fields, growing season at least {1} days.',[['flooded'],['90']]),
('HK','Largest source of fresh food in Hong Kong: {0}.　Main source of rice: {1}.',[['china'],['thailand']]),
('Demand','Two factors affecting food demand: {0} size and level of {1}.',[['population'],['income']]),
('Textbook 1','Physical inputs include sunlight and soil nutrients; {0}, {1} and machines are cultural inputs.',[['fertilizers','fertilisers','pesticides','labour','capital'],['pesticides','fertilizers','fertilisers','labour','capital']]),
('Textbook 2','Cash earned from selling produce goes back to the farm as {0}.',[['feedback']]),
('Textbook 3','Only about {0}% of China’s land is good for farming; the height of land decreases from {1} to east.',[['15'],['west']]),
('Textbook 4','Food supply comes from local production and {0}; when demand is larger than supply, food {1} occur.',[['imports'],['shortages','shortage']]),
('Textbook 6','Staple foods in China at present are rice, wheat and {0}; the major source of rice in Hong Kong is {1}.',[['corn','maize'],['thailand']]),
('Textbook 5','The self-sufficiency rate of grains in China is about {0}%.',[['95']]),
('Output','Animal waste is a {0} output; milk is a {1} output.',[['useless'],['useful']])]
def N(zh,en): return T(zh,en)
FOODMCQ=[
('Sunlight and soil nutrients belong to which of the following?',['Physical inputs','Cultural inputs','Farming processes','Useless outputs'],0,0,N('Sunlight、soil nutrients = physical inputs。','Sunlight and soil nutrients = physical inputs.')),
('Machines and labour are examples of …',['Cultural inputs','Physical inputs','Useful outputs','Farming processes'],0,0,N('Machines、labour = cultural inputs。','Machines and labour = cultural inputs.')),
('Which of the following is a farming process?',['Harvesting','Soil nutrients','Rainfall','Cash'],0,0,N('Ploughing、irrigating、harvesting 都係 processes。','Ploughing, irrigating and harvesting are processes.')),
('Which of the following is a useless output of a farm?',['Animal waste','Milk','Meat','Wheat'],0,0,N('Animal waste、crop residue、pollutants = useless outputs。','Animal waste, crop residue and pollutants = useless outputs.')),
('A farm of 300 hectares has 0.01 farmers per hectare. How many farmers are there?',['3','30','300','0.3'],0,3,'300 × 0.01 = 3.'),
('Which statement about intensive farming is correct?',['Large amount of inputs per unit of land','Small amount of inputs per unit of land','Farm size is very large','Output is never sold'],0,1,N('Intensive = 每單位土地投入多。','Intensive = large inputs per unit of land.')),
('Which pair best describes wheat farming in central USA using combine harvesters?',['Extensive and high-technology','Intensive and low-technology','Extensive and low-technology','Intensive and high-technology'],0,2,N('農場大、用機器 → extensive、high-technology。','Large farms with machines → extensive and high-technology.')),
('Rice grown in Laos is mainly for the farmers’ own consumption. It is …',['Subsistence farming','Commercial farming','Pastoral farming','High-technology farming'],0,2,N('供自己食用 = subsistence。','For own consumption = subsistence.')),
('Crops grown in Indonesia are exported to Hong Kong for sale. This is …',['Commercial farming','Subsistence farming','Pastoral farming','Intensive farming'],0,2,N('出售 = commercial。','For sale = commercial.')),
('Which growing environment does wet rice need?',['Flooded fields','Dry sandy soil','Frozen ground','Steep mountain slopes'],0,4,N('Wet rice 要喺 flooded fields 種。','Wet rice is grown in flooded fields.')),
('Which farming region of China is most favourable for growing wet rice?',['Huanan Region','Xibei Region','Qing Zang Gaoyuan','Huabei Region'],0,4,N('Huanan：暖、雨多、growing season 長、地勢平坦。','Huanan: warm, rainy, long growing season, flat land.')),
('Which set of conditions is favourable for wet rice?',['Rainfall 1,400 mm; growing season 180–365 days','Rainfall 500 mm; growing season 60 days','Minimum temperature −40°C','Rainfall below 600 mm'],0,4,N('>1,000 mm、growing season ≥ 90 日。','More than 1,000 mm and a growing season of at least 90 days.')),
('Cattle grazing on grassland in Xibei Region is an example of …',['Pastoral farming','Arable farming','Intensive arable farming','Wet rice farming'],0,4,N('Xibei：薄而貧瘠嘅泥土、崎嶇地勢，適合 pastoral。','Xibei: thin infertile soil and rugged relief suit pastoral farming.')),
('What is the largest source of fresh food in Hong Kong?',['China','Argentina','South Korea','Thailand'],0,5,'China.'),
('In Hong Kong, the major source of rice and its share is …',['Thailand, around 52%','The Mainland, over 90%','Thailand, over 90%','Local production, around 52%'],0,5,N('Table 1：米主要來自泰國（約 52%）；本地 0%。','Table 1: rice mainly from Thailand (~52%); local production 0%.')),
('China’s staple foods at present are …',['rice, wheat and corn','millet, soybeans and rice','wheat, millet and potatoes','rice, vegetables and meat'],0,5,N('課本：現時 rice, wheat, corn。','Textbook: today rice, wheat and corn.')),
('Which statement about food in Hong Kong is correct?',['Most food is imported and the Mainland is a major supplier','Most food is locally produced','Thailand supplies most fresh vegetables','No food is imported'],0,5,N('課本 p.3。','Textbook p.3.')),
('Which of the following is a factor affecting food demand?',['Population size','Soil fertility','Rainfall','Relief'],0,6,'Population size, level of income.'),
('Which of the following is a cultural input of a farm?',['Pesticides','Sunlight','Rainfall','Soil nutrients'],0,0,N('Cultural inputs：capital、fertilizers、pesticides、technology、labour、irrigation system、machines。','Cultural inputs: capital, fertilizers, pesticides, technology, labour, irrigation system, machines.')),
('Farmers sell their produce and use the cash to buy fertilizers for the next season. This is …',['Feedback','A physical input','A useless output','A farming process'],0,0,N('Cash 返回農場 = feedback。','Cash returning to the farm = feedback.')),
('Which of the following is a physical input?',['Seeds','Machines','Capital','Pesticides'],0,0,N('Physical inputs：sunlight、air temperature、rainfall、seeds、land、soil nutrients。','Physical inputs: sunlight, air temperature, rainfall, seeds, land, soil nutrients.')),
('What is a farming region?',['An area where farmers grow the same major crops or raise the same livestock using similar methods','Any area with a farm','An area with the same population','A place with the same rainfall only'],0,4,N('課本定義。','Textbook definition.')),
('Which region of China has small farms and is mainly intensive arable farming?',['Huanan region','Xibei region','Huabei region','Dongbei region'],0,4,N('Huanan：small farm、intensive arable；Rice, vegetables, tropical fruits。','Huanan: small farms, intensive arable; outputs rice, vegetables and tropical fruits.')),
('Which region of China is mainly extensive pastoral farming, with meat, milk and wool as major outputs?',['Xibei region','Huanan region','Huabei region','Zhujiang Delta'],0,4,N('Xibei = 西北。','Xibei = north-west.')),
('Rainfall in China generally …',['decreases from south-east to north-west','increases from south-east to north-west','decreases from north to south','is the same everywhere'],0,4,N('東南多雨，西北少雨。','Wetter in the south-east, drier in the north-west.')),
('The height of land in China generally …',['decreases from west to east','decreases from east to west','increases from north to south','is the same everywhere'],0,4,N('西高東低。','High in the west, low in the east.')),
('About what percentage of China’s land is good for farming?',['15%','50%','75%','90%'],0,4,N('只有約 15%。','Only about 15%.')),
('Which of the following is the longest growing season in China?',['Southern China','Northwest China','Tibetan Plateau','Northern China'],0,4,N('南方氣溫高 → growing season 最長。','The south is warm, so it has the longest growing season.')),
('From 1970 to 2019, China’s population …',['increased from 830 million to 1,400 million','decreased from 1,400 million to 830 million','stayed at 1,000 million','increased from 1,140 million to 1,400 million'],0,6,N('Table 1：830 → 1,400 百萬。','Table 1: 830 → 1,400 million.')),
('As people’s income rises, they tend to consume …',['more meat and dairy products but fewer staple foods','fewer meat and dairy products','more staple foods only','the same food'],0,6,N('課本 Table 2：grains ↓、meat ↑、milk ↑。','Textbook Table 2: grains down, meat and milk up.')),
('Food is supplied by …',['local production from farming and imports','population and income level','rainfall and relief','cash and feedback'],0,7,N('供應 = 本地生產 + 進口。','Supply = local production + imports.')),
('Food shortages may lead to …',['slower economic development and social unrest','faster economic growth','lower food demand only','higher self-sufficiency'],0,7,N('糧食短缺 → 拖慢經濟、社會動盪。','Shortage → slower development, social unrest.')),
('In China’s grain supply since 2006, …',['supply is larger than demand','demand is larger than supply','imports are the largest share','there is no local production'],0,7,N('2006 年起 supply &gt; demand。','Since 2006 supply &gt; demand.')),
('The self-sufficiency rate of grains in China is about …',['95%','50%','25%','70%'],0,7,N('約 95%，即大部分本地生產。','About 95%: most is locally produced.')),
('Which of the following affect the length of the growing season?',['Rainfall and air temperature','Air pressure and rainfall','Air pressure only','Relief and soil only'],0,4,'Rainfall, air temperature.')]
AIFOOD=[
('A family in Laos grows rice on a small plot with hand tools and eats most of it. The farm is best described as …',['Intensive, subsistence and low-technology','Extensive, commercial and high-technology','Intensive, commercial and high-technology','Extensive, subsistence and low-technology'],2),
('A 500-hectare farm uses GPS-guided tractors, employs only 5 workers and sells grain to supermarkets. Which description is correct?',['Extensive, commercial and high-technology','Intensive, subsistence and low-technology','Intensive, commercial and low-technology','Extensive, subsistence and high-technology'],2),
('Farmers pour river water onto their crops during a dry spell. This farming process is called …',['Irrigating','Harvesting','Ploughing','Selling'],0),
('A farmer keeps cattle and sells milk. Milk is a …',['Useful output','Useless output','Physical input','Cultural input'],0),
('Dung from the cattle on a dairy farm is a …',['Useless output','Useful output','Physical input','Farming process'],0),
('A farm has 20 hectares and 40 farmers. The number of farmers per hectare is …',['2','0.5','20','8'],0),
('A farm of 150 hectares has 0.02 farmers per hectare. How many farmers work there?',['3','30','7.5','300'],0),
('Place P: minimum 15°C, rainfall 1,500 mm, growing season 150 days. Place Q: minimum 2°C, rainfall 400 mm, growing season 60 days. Which place is more suitable for wet rice?',['Place P','Place Q','Both','Neither'],4),
('Why is the Zhujiang Delta favourable for growing wet rice?',['Flat land and thick fertile soil','Steep slopes and thin soil','Very low rainfall','Very short growing season'],4),
('A region has minimum temperature −30°C, rainfall 400 mm and rugged mountains. The most likely farming type is …',['Pastoral farming','Wet rice farming','Intensive arable farming','Mixed farming with irrigation'],4),
('When Hong Kong’s population and income both rise, food demand will most likely …',['Increase','Decrease','Stay the same','Stop'],6),
('Which is a reason why Hong Kong imports most of its food?',['Local food production is very small','Hong Kong has a lot of farmland','Hong Kong has no demand for food','Imports are banned'],5)]
AIFOODFILL=[('AI 5','A farm with a large area, few workers and big machines is {0} farming.',[['extensive']]),
('AI 6','Wet rice grown for the farmer’s family is {0} farming; crops sold abroad are {1} farming.',[['subsistence'],['commercial']]),
('AI 7','Ploughing, irrigating and {0} are farming processes.',[['harvesting','harvest']]),
('AI 8','A farm with 30 farmers on 15 hectares has {0} farmers per hectare.',[['2']]),
('AI 9','Pastoral farming rears {0}; arable farming grows {1}.',[['livestock','animals','cattle'],['crops','crop']])]
AIFOODMATCH=[[('Small plot, many workers','Intensive farming'),('Huge farm, few workers','Extensive farming'),('Grows wheat only','Arable farming'),('Raises cattle only','Pastoral farming'),('Sells produce at market','Commercial farming'),('Eats own produce','Subsistence farming')],
 [('Pouring water on fields','Irrigating'),('Collecting the crop','Harvesting'),('Dung from cows','Useless output'),('Milk from cows','Useful output'),('Tractor','Cultural input'),('Sunlight','Physical input')]]
AIMAP=[
('On a map with scale 1 : 5,000, a road is 8 cm long. Its real length is …',['400 m','40 m','4,000 m','800 m'],0),
('A map has scale 1 : 10,000. This means 1 cm to …',['100 m','10 m','1,000 m','10,000 m'],0),
('A pond is 3.5 cm from a school on a 1 : 20,000 map. The real distance is …',['700 m','70 m','7,000 m','350 m'],0),
('A grid square has easting 12 and northing 68. Its 4-figure grid reference is …',['1268','6812','1286','2168'],0),
('The 6-figure grid reference of a point is 143672. Its easting reading is …',['143','672','14','67'],0),
('Whole-circle bearing 090° corresponds to the compass point …',['E','W','N','S'],0),
('A reduced bearing of S 45° E equals a whole-circle bearing of …',['135°','225°','045°','315°'],0),
('A place is S 30° W of another. Its whole-circle bearing is …',['210°','150°','330°','030°'],0),
('B is due north of A. The whole-circle bearing of B from A is …',['000°','090°','180°','270°'],0),
('Which is more precise for locating a point?',['6-figure grid reference','4-figure grid reference','Compass point','Scale'],0),
('On a 1 : 20,000 map, a real distance of 2,400 m is shown as …',['12 cm','1.2 cm','24 cm','2.4 cm'],0)]
FILLPANE2=T(FILLPANE,'<p class="sub">Type your answers in the blanks, then tap “Check”. Tap “Hint” if you are not sure.</p><div id="fills"></div>')
def _fixhard(L):
    return L
HARDFOOD=[
('Which of the following statements about intensive farming are correct?<br>(1) Farm size is usually small.<br>(2) The number of farmers per unit of land is high.<br>(3) The output must be for the farmers’ own consumption.',['(1) and (2) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],1,T('Intensive 唔一定係 subsistence，亦可以係 commercial（例如印尼作物出口香港）。','Intensive farming is not necessarily subsistence; it can be commercial (e.g. Indonesian crops exported to Hong Kong).')),
('Farm X: 200 ha, 10 farmers. Farm Y: 5 ha, 15 farmers. The number of farmers per hectare on Farm Y is … times that on Farm X.',['60','30','6','600'],1,'X: 10 ÷ 200 = 0.05；Y: 15 ÷ 5 = 3；3 ÷ 0.05 = 60.'),
('A 1,000-hectare dairy ranch in Australia employs 4 workers, uses milking machines and sells milk to supermarkets. Which description is correct?',['Extensive, pastoral, commercial and high-technology','Intensive, pastoral, commercial and high-technology','Extensive, arable, subsistence and low-technology','Intensive, mixed, subsistence and low-technology'],0,T('大農場、少人手 → extensive；養牛 → pastoral；出售 → commercial；機器 → high-technology。','Large farm, few workers → extensive; cattle → pastoral; sold → commercial; machines → high-technology.')),
('Region B has a minimum temperature of 0°C, annual rainfall below 1,000 mm and a growing season of 0–364 days. Why is it unfavourable for wet rice?<br>(1) It is too cold in winter.<br>(2) Rainfall is insufficient.<br>(3) The growing season is too long.',['(1) and (2) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],4,T('水稻需要 min ≥10–12°C、&gt;1,000 mm；growing season 長唔係問題。','Wet rice needs a minimum of 10–12°C and over 1,000 mm; a long growing season is not a problem.')),
('Crop N needs: minimum temperature ≥ 10°C, rainfall ≥ 1,000 mm, growing season ≥ 90 days. Place P: min 14°C, 1,350 mm, 110 days. Place Q: min 8°C, 1,500 mm, 200 days. Place R: min 15°C, 900 mm, 150 days. Which place is suitable?',['Place P only','Place Q only','Place R only','Places P and R'],4,T('P 三項都達標；Q 太冷（8°C）；R 雨量不足（900 mm）。','P meets all three; Q is too cold (8°C); R has too little rainfall (900 mm).')),
('Which statements about wheat-sheep farming in Australia are correct?<br>(1) It is mixed farming.<br>(2) It is extensive.<br>(3) The output is mainly for the farmers’ own consumption.',['(1) and (2) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],2,T('澳洲小麥綿羊農場規模大、出售，係 commercial。','Australian wheat-sheep farms are large and commercial.')),
('Which of the following would increase food demand in Hong Kong directly?<br>(1) a rise in population<br>(2) a rise in income<br>(3) less farmland in Guangdong',['(1) and (2) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],6,T('(3) 影響供應而唔係需求。','(3) affects food supply, not demand.')),
('Which of the following are factors affecting food SUPPLY rather than demand?<br>(1) rainfall<br>(2) population size<br>(3) level of technology',['(1) and (3) only','(1) and (2) only','(2) and (3) only','(1), (2) and (3)'],6,T('Rainfall、technology 影響生產（供應）；population 影響需求。','Rainfall and technology affect production (supply); population affects demand.')),
('Which of the following are cultural inputs of a farm?<br>(1) fertiliser<br>(2) labour<br>(3) soil nutrients',['(1) and (2) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],0,T('Soil nutrients 係 physical input。','Soil nutrients are a physical input.')),
('Which pairs are correct?<br>(1) irrigating — farming process<br>(2) fertiliser — physical input<br>(3) animal waste — useless output',['(1) and (3) only','(1) and (2) only','(2) and (3) only','(1), (2) and (3)'],0,T('Fertiliser 係 cultural input。','Fertiliser is a cultural input.')),
('A farm of 12 hectares has 0.5 farmers per hectare. After 6 more farmers join, the number of farmers per hectare becomes …',['1.0','0.75','1.5','2.0'],0,'12 × 0.5 = 6；6 + 6 = 12；12 ÷ 12 = 1.0.'),
('A farm in Guangdong uses combine harvesters on 80 hectares and sells all of its rice to traders. Which classification is correct?',['Extensive, arable, commercial and high-technology','Intensive, arable, subsistence and low-technology','Extensive, pastoral, commercial and high-technology','Intensive, arable, commercial and low-technology'],0,T('大面積、機器、出售。','Large area, machines, sold.'))]
HARDMAP=[
('A road is 7.2 cm long on a 1 : 25,000 map. Its real length is …',['1,800 m','180 m','18,000 m','2,880 m'],0,'7.2 × 250 m = 1,800 m.'),
('The real distance between two towns is 3.6 km. On a 1 : 20,000 map, the distance would be …',['18 cm','1.8 cm','36 cm','0.18 cm'],0,'3,600 m ÷ 200 m = 18 cm.'),
('Two points are 6 cm apart on a 1 : 5,000 map. How far apart are they on a 1 : 20,000 map of the same area?',['1.5 cm','24 cm','6 cm','0.5 cm'],0,'6 × 50 m = 300 m；300 ÷ 200 = 1.5 cm.'),
('The whole-circle bearing of B from A is 062°. The whole-circle bearing of A from B is …',['242°','118°','298°','062°'],2,T('相反方向 + 180°。','The reverse direction: add 180°.')),
('A whole-circle bearing of 295° is the same as the reduced bearing …',['N 65° W','S 65° W','N 25° W','N 295° W'],2,'360° − 295° = 65°，NW quadrant.'),
('A reduced bearing of S 20° W is a whole-circle bearing of …',['200°','160°','340°','020°'],2,'180° + 20° = 200°.'),
('A whole-circle bearing of 240° points in which compass direction (8-point compass)?',['SW','W','NW','S'],2,T('225° 係 SW，240° 最接近 SW。','225° is SW; 240° is closest to SW.')),
('The 6-figure grid reference of a point is 163657. What is the 4-figure grid reference of the grid square containing it?',['1665','1636','6357','1663'],2,T('取 easting 前兩位 16 + northing 前兩位 65。','Take the first two digits of the easting (16) and of the northing (65).')),
('Point A is at 165660 and point B is at 165670. In which direction is B from A?',['North','South','East','West'],3,T('Easting 相同；northing 由 660 增加到 670 → 向北。','Same easting; northing increases from 660 to 670 → north.')),
('Point P is at 170655 and point Q is at 150655. In which direction is Q from P?',['West','East','North','South'],3,T('Northing 相同；easting 由 170 減少到 150 → 向西。','Same northing; easting decreases from 170 to 150 → west.')),
('Which statement about the bearings 047° and N 47° E is correct?',['They describe the same direction','They are opposite directions','047° is clockwise from east','N 47° E is anticlockwise from north'],3,T('兩者都係由北向東偏 47°。','Both are 47° east of north.')),
('A person walks 4.8 cm and then 3.2 cm along a road on a 1 : 10,000 map. The total real distance walked is …',['800 m','80 m','8,000 m','1,600 m'],3,'8.0 cm × 100 m = 800 m.'),
('Which map shows more detail: 1 : 5,000 or 1 : 20,000?',['1 : 5,000, because it has a larger scale','1 : 20,000, because the number is larger','They show the same detail','Cannot be compared'],3,T('比例尺越大（分母越細），細節越多。','The smaller the denominator, the larger the scale and the more detail.'))]
AIL=T('【AI 出題】','[AI] ')
def build_food():
    ref=''
    for i,(h,b) in enumerate(FOOD):
        ref+=item('g-i%d'%i,'%d. %s'%(i+1,h),b,['','s2','s3','s4'][i%4])
    ref=refpane('<p class="sub"><a href="../geo-farm-3d/"><b>'+T('🏝️ 3D 農場島：行入島睇 inputs、processes、outputs，仲有挑戰','🏝️ 3D Farm Island: explore inputs, processes and outputs, with a challenge')+'</b></a></p><p class="sub">'+T('已對照課本《Exploring Geography 3 Food Problems》Unit 1-3（頁 3-29）同兩份試卷標準答案整理。','Based on the two past papers and marking schemes. Please check against the textbook <i>Exploring Geography 3 Food Problems</i>, Units 1-3 (pp.3-29).')+'</p>'+ref,T('黃色字係重點，撳開睇','Highlighted text = key points. Tap to open'))
    sets=[]
    for n,k in enumerate(range(0,len(FOODMATCH),6)):
        sets.append({'name':T('術語配對（%s）'%'一二'[n],'Terms (%d)'%(n+1)),'help':T('先撳英文術語，再撳相配嘅意思。','Tap a term, then tap its meaning.'),'pairs':[[a,b] for a,b in FOODMATCH[k:k+6]]})
    for n,ps in enumerate(AIFOODMATCH):
        sets.append({'name':T('AI 配對（%s）'%'一二'[n],'AI match (%d)'%(n+1)),'help':T('AI 出題：先撳情境，再撳相配嘅術語。','AI-made: tap a situation, then the matching term.'),'pairs':[[a,b] for a,b in ps]})
    rnd=random.Random(5);M=[]
    for q,o,a,tg,note in FOODMCQ:
        idx=list(range(len(o)));rnd.shuffle(idx)
        M.append([q,[o[j] for j in idx],idx.index(a),'g-i%d'%tg,note])
    for q,o,tg in AIFOOD:
        idx=list(range(len(o)));rnd.shuffle(idx)
        M.append([AIL+q,[o[j] for j in idx],idx.index(0),'g-i%d'%tg,T('答案：','Answer: ')+'<b>%s</b>'%o[0]])
    for q,o,a,note in HARDFOOD:
        idx=list(range(4));rnd.shuffle(idx)
        M.append([q,[o[j] for j in idx],idx.index(0),'g-i1',note,1])
    tagmap={m[3]:m[3] for m in M}
    fq=[{'t':t,'p':p,'b':b} for t,p,b in FOODFILL+AIFOODFILL]
    js=MASK+matchjs(sets)+filljs(fq)+mcq('mcqBestGeoFood',M,tagmap,10,T('十條題，四揀一','10 questions, 4 choices'))
    gpage('geo-food','Food Problems '+T('食物問題',''),T('Unit 1-3：農業系統、農業類型、中國農業地區、香港食物','Units 1-3: farming systems, types of farming, farming regions in China, food in Hong Kong'),'farm',
      [('p-ref',T('重點速覽','Notes')),('p-match',T('配對遊戲','Match')),('p-fill',T('寫字填空','Fill in')),('p-mcq',T('選擇題','Quiz'))],
      [('p-ref',ref),('p-match','<div id="matchroot"></div>'),('p-fill',FILLPANE2),('p-mcq','<div id="mcqroot"></div>')],js)

MAPNOTES=[
('Scale '+T('比例尺',''),'<p>'+K('Representative fraction 1 : 5,000 → 1 cm to 50 m')+'</p>'+
 P(T('<b>換算：</b>1 : n，1 cm 代表 n cm。n 除以 100 就係「1 cm to ? m」。<br>例：1 : 20,000 → 1 cm to 200 m；1 : 5,000 → 1 cm to 50 m。','<b>Conversion:</b> in 1 : n, 1 cm stands for n cm. Divide n by 100 to get “1 cm to ? m”.<br>E.g. 1 : 20,000 → 1 cm to 200 m; 1 : 5,000 → 1 cm to 50 m.'))+
 P(T('<b>Statement scale：</b>1 cm to 50 m　<b>Linear scale：</b>畫一條尺，標 0、50、100…250 m。','<b>Statement scale:</b> 1 cm to 50 m　<b>Linear scale:</b> draw a ruler marked 0, 50, 100 … 250 m.'))+
 P(T('<b>實際距離 = 圖上長度 × 比例尺。</b>','<b>Real distance = map length × scale.</b>'))+EG(T('QE 例：East Rail Line 圖上 6.1 cm × 200 m = 1,220 m（1,200–1,240 m 都接受）。','QE example: East Rail Line 6.1 cm on the map × 200 m = 1,220 m (1,200–1,240 m accepted).'))),
('Grid references'+T(' 方格參考',''),'<p>'+K(T('先 easting（橫），後 northing（直）','Easting first, then northing'))+'</p>'+
 P(T('<b>4-figure：</b>指一個方格（用方格左下角嘅 easting + northing），例：1865。<br><b>6-figure：</b>將每格分成十等份，easting 3 位 + northing 3 位，例：182656。','<b>4-figure:</b> refers to a grid square (easting + northing of its lower-left corner), e.g. 1865.<br><b>6-figure:</b> divide each square into tenths; 3-digit easting + 3-digit northing, e.g. 182656.'))+
 EG(T('UT 例：Legislative Council Complex 4-figure = 1667；church along Hennessy Road 6-figure = 182656。','UT example: Legislative Council Complex, 4-figure = 1667; church along Hennessy Road, 6-figure = 182656.'))),
('Direction'+T(' 方向',''),'<p>'+K('Compass points / whole-circle bearing / reduced bearing')+'</p>'+
 P(T('<b>Compass point（八個方向）：</b>','<b>Compass points (8 directions):</b> ')+'N 0°, NE 45°, E 90°, SE 135°, S 180°, SW 225°, W 270°, NW 315°.')+
 P(T('<b>Whole-circle bearing：</b>由北順時針量度，0°–360°，寫成三位數字（如 027°）。誤差 ±2° 都接受。','<b>Whole-circle bearing:</b> measured clockwise from north, 0°–360°, written with three digits (e.g. 027°). ±2° is accepted.'))+
 P(T('<b>Reduced bearing：</b>由北（N）或南（S）向東（E）或西（W）量，不超過 90°，如 N 45° W。','<b>Reduced bearing:</b> measured from north (N) or south (S) towards east (E) or west (W), up to 90°, e.g. N 45° W.'))+
 P(T('<b>換算：</b>','<b>Conversion:</b> ')+'NE: WCB = θ; SE: WCB = 180° − θ; SW: WCB = 180° + θ; NW: WCB = 360° − θ.')+
 EG(T('QE 例：police station (073721) from fire station → SW，222°；restricted access from spot height 305 → ENE，84°。','QE example: police station (073721) from fire station → SW, 222°; restricted access from spot height 305 → ENE, 84°.'))+
 EG(T('UT 例：shopping mall (177672) from spot height 53.1 (162644) → 027°；cinema from primary school → N 45° W。','UT example: shopping mall (177672) from spot height 53.1 (162644) → 027°; cinema from primary school → N 45° W.'))+
 P(T('<b>量度要點：</b>方向「由 A 去 B」＝站喺 A，望住 B。','<b>Tip:</b> “direction of B from A” = stand at A and look at B.'))),
('Conventional signs'+T(' 圖例',''),'<p>'+K(T('常見符號','Common signs'))+'</p>'+P('Declared monument, Government office, Trigonometric station, Spot height, Church, Hotel, Playground, Kindergarten, Secondary school, Petrol station, Car park, Post office, Clinic, Fire station, Police station.')+EG(T('唔識嘅符號要睇 map extract 嘅 legend／平時練習。','If you do not know a sign, check the legend of the map extract and practise often.')))]
def build_map():
    ref=''.join(item('m-i%d'%i,'%d. %s'%(i+1,h),b,['','s2','s3','s4'][i%4]) for i,(h,b) in enumerate(MAPNOTES))
    ref=refpane('<p class="sub">'+T('新世紀地理 Map Reading Chapter 1, 2（唔考 p.33–35）, 3, 4（唔考 p.59–66）。請對返課本。','New Century Geography Map Reading: Chapters 1, 2 (excluding pp.33–35), 3, 4 (excluding pp.59–66). Please check against the textbook.')+'</p>'+ref,T('黃色字係重點，撳開睇','Highlighted text = key points. Tap to open'))
    drill='<p class="sub">'+T('每次入嚟都係新題目（隨機數字）。想要新一輪就重新整理頁面。','New random numbers every time. Reload the page for a new round.')+'</p><div id="fills"></div>'
    gridtxt=T("'某處喺 easting '+e+' 之後 '+a+' 格（十分一），northing '+n+' 之後 '+b+' 格。6-figure grid reference = {0}　4-figure grid reference = {1}'","'A point is '+a+' tenths east of easting '+e+' and '+b+' tenths north of northing '+n+'. 6-figure grid reference = {0}　4-figure grid reference = {1}'")
    distxt=T("'，圖上長度 '+L.toFixed(1)+' cm，實際距離 = {0} m'","', map length '+L.toFixed(1)+' cm. Real distance = {0} m'")
    js=MASK+'''  var R=function(a,b){return a+Math.floor(Math.random()*(b-a+1))};
  var pick=function(a){return a[R(0,a.length-1)]};
  var FQ=[];
  var sc=[2000,5000,10000,20000,25000];
  for(var i=0;i<3;i++){var n=pick(sc);FQ.push({t:'Scale '+(i+1),p:'Scale 1 : '+n.toLocaleString('en-US')+'　→　1 cm to {0} m',b:[[String(n/100)]]})}
  for(var i=0;i<3;i++){var n=pick([5000,10000,20000]);var L=R(2,9)+R(0,9)/10;var real=Math.round(L*n/100);FQ.push({t:'Distance '+(i+1),p:'Scale 1 : '+n.toLocaleString('en-US')+'''+distxt+''',b:[[String(real)]]})}
  var rb=[['NE',function(t){return t}],['SE',function(t){return 180-t}],['SW',function(t){return 180+t}],['NW',function(t){return 360-t}]];
  for(var i=0;i<4;i++){var q=pick(rb),t=R(1,8)*10;var lbl=(q[0][0]+' '+t+'° '+q[0][1]);FQ.push({t:'Bearing '+(i+1),p:'Reduced bearing '+lbl+'　→　whole-circle bearing = {0}°',b:[[String(q[1](t)),('00'+q[1](t)).slice(-3)]]})}
  var cp=[['N',0],['NE',45],['E',90],['SE',135],['S',180],['SW',225],['W',270],['NW',315]];
  for(var i=0;i<2;i++){var c=pick(cp);FQ.push({t:'Compass '+(i+1),p:'Whole-circle bearing '+('00'+c[1]).slice(-3)+'°　→　compass point = {0}',b:[[c[0]]]})}
  for(var i=0;i<3;i++){var e=R(10,19),n=R(60,69),a=R(0,9),b=R(0,9);FQ.push({t:'Grid ref '+(i+1),p:'''+gridtxt+''',b:[[''+e+a+n+b],[''+e+n]]})}
  TY.fill(document.getElementById('fills'),FQ);
  var sets=[{name:'''+json.dumps(T('讀圖配對（一）','Map terms (1)'),ensure_ascii=False)+''',help:'''+json.dumps(T('先撳術語，再撳相配嘅意思。','Tap a term, then its meaning.'),ensure_ascii=False)+''',pairs:[['Statement scale','1 cm to 50 m'],['Linear scale','A ruler marked 0, 50, 100 … m'],['Easting','Vertical grid line number (read first)'],['Northing','Horizontal grid line number (read second)'],['6-figure grid reference','Locates a point within a grid square'],['4-figure grid reference','Locates a whole grid square']]},
   {name:'''+json.dumps(T('讀圖配對（二）','Map terms (2)'),ensure_ascii=False)+''',help:'''+json.dumps(T('先撳術語，再撳相配嘅意思。','Tap a term, then its meaning.'),ensure_ascii=False)+''',pairs:[['Whole-circle bearing','Measured clockwise from north, 0°–360°'],['Reduced bearing','Measured from N or S towards E or W, up to 90°'],['Compass point','NE, SE, SW, NW …'],['Spot height','Height of a point shown on the map'],['Declared monument','Conventional sign for protected historic site'],['Trigonometric station','Survey point used for mapping']]}];
  sets.push({name:'''+json.dumps(T('AI 配對','AI match'),ensure_ascii=False)+''',help:'''+json.dumps(T('AI 出題：先撳方向，再撳相配嘅 whole-circle bearing。','AI-made: tap a direction, then its whole-circle bearing.'),ensure_ascii=False)+''',pairs:[['Due east','090°'],['Due south','180°'],['Southwest','225°'],['Northwest','315°'],['N 30° E','030°'],['S 45° E','135°']]});
  TY.match(document.getElementById('matchroot'),{sets:sets});
'''
    M=[
     ['Scale 1 : 20,000 can be written as …',['1 cm to 200 m','1 cm to 20 m','1 cm to 2 km','1 cm to 2,000 m'],0,'m-i0','n ÷ 100 = 200 m.'],
     ['In a 6-figure grid reference such as 182656, which part is the easting?',['182','656','18','65'],0,'m-i1',T('Easting 先，northing 後。','Easting comes first, then northing.')],
     ['A 4-figure grid reference refers to …',['A grid square','An exact point','A whole road','A contour line'],0,'m-i1',T('4-figure = 一個方格。','4-figure = one grid square.')],
     ['A whole-circle bearing is measured …',['Clockwise from north','Anticlockwise from east','Clockwise from south','From west to east'],0,'m-i2',T('由北順時針。','Clockwise from north.')],
     ['A place is N 45° W of another. Its whole-circle bearing is …',['315°','045°','135°','225°'],0,'m-i2','NW: 360° − 45° = 315°.'],
     ['Which of the following is a reduced bearing?',['S 30° E','150°','SE','030°'],0,'m-i2',T('Reduced bearing 用 N／S + 角度 + E／W。','A reduced bearing uses N/S + angle + E/W.')],
     ['The compass point of a whole-circle bearing 225° is …',['SW','NW','SE','NE'],0,'m-i2','225° = SW.'],
     ['On a map 1 : 20,000, 6.1 cm represents …',['1,220 m','122 m','12,200 m','610 m'],0,'m-i0','6.1 × 200 = 1,220 m.'],
     ['Direction of B from A means …',['Standing at A and looking at B','Standing at B and looking at A','The distance between them','The height difference'],0,'m-i2',T('由 A 去 B。','From A towards B.')],
     ['Which sign is shown by “I” in the 2024-25 QE map?',['Declared monument','Government office','Trigonometric station','Church'],0,'m-i3','I = Declared monument.']]
    rm=random.Random(21)
    for q,o,*_ in AIMAP:
        idx=list(range(len(o)));rm.shuffle(idx)
        M.append([AIL+q,[o[j] for j in idx],idx.index(0),'m-i%d'%(2 if ('bearing' in q.lower() or 'compass' in q.lower() or 'bearing' in ' '.join(o).lower()) else (1 if 'grid' in q.lower() else 0)),T('答案：','Answer: ')+'<b>%s</b>'%o[0]])
    for q,o,a,note in HARDMAP:
        idx=list(range(4));rm.shuffle(idx)
        M.append([q,[o[j] for j in idx],idx.index(0),'m-i%d'%(0 if ('scale' in q.lower() or 'cm' in ' '.join(o)  or ' m' in ' '.join(o)) else (1 if 'grid' in q.lower() else 2)),note,1])
    tagmap={m[3]:m[3] for m in M}
    js+=mcq('mcqBestGeoMap',M,tagmap,10,T('十條題，四揀一','10 questions, 4 choices'))
    gpage('geo-map','Map Reading'+T(' 讀圖',''),T('Chapter 1-4：比例尺、方格參考、方向、距離','Chapters 1-4: scale, grid references, direction, distance'),'map',
      [('p-ref',T('重點速覽','Notes')),('p-fill',T('計算練習','Practice')),('p-match',T('配對遊戲','Match')),('p-mcq',T('選擇題','Quiz'))],
      [('p-ref',ref),('p-fill',drill),('p-match','<div id="matchroot"></div>'),('p-mcq','<div id="mcqroot"></div>')],js)

PASTMCQ=[
('2025-26 UT Q1','Which of the following statement(s) about food supply of Hong Kong is/are correct?<br>(1) The major source of rice is supplied by Thailand.<br>(2) Hong Kong produces most vegetables consumed.<br>(3) The share of local food production in Hong Kong is very small.',['(2) only','(1) and (2) only','(1) and (3) only','(1), (2) and (3)'],2,T('(1)、(3) 啱；香港本地菜只佔好細部分。','(1) and (3) are correct; local vegetables are only a very small share.')),
('2025-26 UT Q2','Which of the following is/are useless output of a dairy farm?<br>(1) milk (2) meat (3) animal waste',['(1) only','(2) and (3) only','(3) only','(1), (2) and (3)'],2,T('只有 animal waste 係 useless。','Only animal waste is useless.')),
('2025-26 UT Q3','Which information about rice cultivation in Laos is correct?<br>(1) Labour input per unit area of land: High<br>(2) Technology input: Low<br>(3) Uses: Own consumption',['(1) and (2) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],3,T('三項都啱。','All three are correct.')),
('2025-26 UT Q4','Which of the following are factors affecting the distribution of farming regions in China?<br>(1) relief (2) rainfall (3) temperature',['(1) and (2) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],3,T('三樣都係。','All three.')),
('2025-26 UT Q5','Which condition(s) favour(s) farming activities?<br>(1) height of land: 2,000 m (2) growing season: 20 days (3) annual rainfall: 1,800 mm',['(2) only','(3) only','(2) and (3) only','(1), (2) and (3)'],1,T('只有 1,800 mm 雨量有利。','Only the 1,800 mm rainfall is favourable.')),
('2025-26 UT Q6','Which statements about wheat-sheep farming in Australia are correct?<br>(1) It belongs to mixed farming.<br>(2) The output is for the farmers and their family members.<br>(3) The output per unit area of land is low.',['(1) and (2) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],1,T('Mixed、extensive（產量低）；係 commercial，非自用。','Mixed and extensive (low output); it is commercial, not for the family.')),
('2025-26 UT Q7','Which of the following are factors affecting food demand?<br>(1) local industrial production (2) population size (3) level of income',['(1) and (2) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],2,T('人口同收入。','Population and income.')),
('2025-26 UT Q8','Which is the largest source of the fresh food in Hong Kong?',['China','Argentina','South Korea','Thailand'],0,'China.'),
('2024-25 QE Q1','Which items belong to farming processes?<br>(1) ploughing (2) irrigating (3) harvesting',['(1) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],3,T('三樣都係 processes。','All three are processes.')),
('2024-25 QE Q2',T('[相：(1) 牛扒肉　(2) 缸中嘅魚　(3) 水果同蔬菜] ','[Photos: (1) beef steak (2) a fish in a tank (3) fruit and vegetables] ')+'Which of the above are examples of farm produce?',['(1) and (2) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],1,T('肉類同水果／蔬菜係 farm produce。','Meat, fruit and vegetables are farm produce.')),
('2024-25 QE Q3','Which of the following are outputs of a farming system?<br>(1) pollutants (2) cash (3) animal waste',['(1) and (2) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],1,T('標準答案：pollutants 同 animal waste（useless outputs）。','Marking scheme: pollutants and animal waste (useless outputs).')),
('2024-25 QE Q4',T('[相：聯合收割機收割小麥] ','[Photo: a combine harvester harvesting wheat] ')+'Which are the characteristics of the farm shown?<br>(1) arable (2) commercial (3) subsistence',['(1) and (2) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],0,'Arable + commercial.'),
('2024-25 QE Q5','Which are the physical inputs of a farming system?<br>(1) soil (2) sunlight (3) flat land',['(1) and (2) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],3,T('三樣都係 physical inputs。','All three are physical inputs.')),
('2024-25 QE Q6','Which of the following affect the length of growing season?<br>(1) air pressure (2) rainfall (3) air temperature',['(1) and (2) only','(1) and (3) only','(2) and (3) only','(1), (2) and (3)'],2,T('Rainfall 同 air temperature。','Rainfall and air temperature.'))]
def tbl(rows,head=None):
    h=''.join('<th>%s</th>'%c for c in head) if head else ''
    return '<table class="tb">%s%s</table>'%('<tr>%s</tr>'%h if h else '',''.join('<tr>%s</tr>'%''.join('<td>%s</td>'%c for c in r) for r in rows))
STRUCT=[
('2025-26 UT · Section B Q1 '+T('（12 分）','(12 marks)'),'<p>'+T('<b>題目：</b>Photo 1a（印尼，人手收割稻）、Photo 1b（美國中部，聯合收割機收割小麥）、Figure 1c 世界地圖（A–E）。','<b>Question:</b> Photo 1a (Indonesia, rice harvested by hand), Photo 1b (central USA, wheat harvested by combine harvester), Figure 1c world map (A–E).')+'</p>'+
 tbl([['(a)(i) Amount of inputs per unit of land','Intensive','Extensive'],['(ii) Types of output','Arable','Arable'],['(iii) Level of technology','Low-technology','High-technology']],['','Photo 1a','Photo 1b'])+
 P(T('(b)(i) Photo 1a 嘅位置 = <b>D</b>　(ii) Photo 1b 嘅位置 = <b>A</b>','(b)(i) Location of Photo 1a = <b>D</b>　(ii) Location of Photo 1b = <b>A</b>'))+
 P(T('(c) Indonesia 作物出口香港 = <b>commercial</b> farming。','(c) Indonesian crops exported to Hong Kong = <b>commercial</b> farming.'))+P(T('(d) Common process = <b>harvesting</b>。','(d) Common process = <b>harvesting</b>.'))+
 P('(e)(i) Physical input: sunlight / air temperature / land / soil nutrients / seeds　(ii) Cultural input: <b>machine</b>')),
('2025-26 UT · Section B Q2 '+T('（14 分）','(14 marks)'),'<p>'+T('<b>題目：</b>','<b>Question:</b> ')+'Figure 2a: Crop M in Region X; Table 2b: 27–32°C (min ≥12°C), &gt;1,000 mm (≥125 mm each month), ≥90 days, flooded fields, food for the farmers and their families.</p>'+
 P('(a)(i) Crop M = <b>wet rice / paddy / rice</b>')+
 P(T('(a)(ii) <b>Subsistence farming</b>；evidence：useful output mainly provided as food for the farmers and their family members。','(a)(ii) <b>Subsistence farming</b>; evidence: useful output mainly provided as food for the farmers and their family members.'))+
 P('(b)(i) Region X = <b>Huanan Region</b>')+
 P(T('(b)(ii) <b>氣候（每點 = 特點 + 引 Table 2b 證據）：</b><br>① 氣溫全年高／暖 → Table 2b：minimum 12°C。<br>② 年雨量多 → Table 2b：&gt;1,000 mm。<br>③ growing season 長 → Table 2b：至少 90 日。','(b)(ii) <b>Climate (each point = feature + evidence from Table 2b):</b><br>① Air temperature is high / warm all year round → Table 2b: minimum 12°C.<br>② Annual rainfall is high → Table 2b: over 1,000 mm.<br>③ Growing season is long → Table 2b: at least 90 days.'))+
 P(T('(b)(iii) <b>地勢同泥土：</b><br>① 多數係平原／低地／平地同丘陵（Zhujiang Delta）→ 地勢平坦，利於種 Crop M。<br>② 泥土深厚、肥沃 → 利於種 Crop M。','(b)(iii) <b>Relief and soil:</b><br>① Most areas are plains / lowlands / flatland and hills (Zhujiang Delta) → gentle, flat relief favours Crop M.<br>② Soil is thick and fertile → favourable for Crop M.'))),
('2024-25 QE · Section B Q1 '+T('（13 分）','(13 marks)'),'<p>'+T('<b>題目：</b>','<b>Question:</b> ')+T('Table 1：A（300 公頃、X 農民、0.01、大型機器、livestock、for sale）；B（6 公頃、12 農民、Y、人力同牲畜、crops、家人食用）。','Table 1: A (300 ha, X farmers, 0.01, large machines, livestock, for sale); B (6 ha, 12 farmers, Y, labour and animals, crops, for the family).')+'</p>'+
 P('(a) Common cultural input: <b>labour / farmer</b>')+P('(b) <b>X = 3, Y = 2</b>')+
 tbl([['(i) Inputs per unit of land','Extensive','Intensive'],['(ii) Types of output','Pastoral','Arable'],['(iii) Uses of output','Commercial','Subsistence'],['(iv) Level of technology','High-technology','Low-technology']],['','Farm A','Farm B'])+
 P(T('(d)(i) Useful output of A：<b>beef / meat</b>　(ii) Useless output of B：<b>crop residue</b>（或其他合理答案）','(d)(i) Useful output of A: <b>beef / meat</b>　(ii) Useless output of B: <b>crop residue</b> (or other reasonable answers)'))),
('2024-25 QE · Section B Q2 '+T('（16 分）','(16 marks)'),'<p>'+T('<b>題目：</b>','<b>Question:</b> ')+T('Photo 2a（人手插秧）、Photo 2b（牛群放牧）、Figure 2c（Region A、B、C）、Figure 2d 水稻條件（20–30°C，min ≥10°C；≥1,000 mm，每月≥125 mm；≥90 日）、Figure 2e 三個地區氣候。','Photo 2a (planting rice by hand), Photo 2b (cattle grazing), Figure 2c (Regions A, B, C), Figure 2d growing conditions for Crop G (20–30°C, min ≥10°C; ≥1,000 mm, ≥125 mm each month; ≥90 days), Figure 2e climate of the three regions.')+'</p>'+
 P(T('(a)(i) <b>Region C</b>　(ii) <b>Huanan Region</b>','(a)(i) <b>Region C</b>　(ii) <b>Huanan Region</b>'))+
 P(T('(a)(iii) 氣候證據（各 2 分）：<br>① 氣溫：Figure 2d 要 min ≥10°C；Figure 2e Region C min 12°C。<br>② 雨量：Figure 2d 不少於 1,000 mm；Region C &gt;1,400 mm，高。<br>③ growing season：Figure 2d 至少 90 日；Region C 180–365 日，長。','(a)(iii) Climate evidence (2 marks each):<br>① Temperature: Figure 2d needs min ≥10°C; Figure 2e Region C min 12°C.<br>② Rainfall: Figure 2d needs at least 1,000 mm; Region C &gt;1,400 mm, high.<br>③ Growing season: Figure 2d needs at least 90 days; Region C 180–365 days, long.'))+
 P(T('(b)(i) <b>Region A</b>　(ii) <b>Xibei Region</b>','(b)(i) <b>Region A</b>　(ii) <b>Xibei Region</b>'))+
 P(T('(b)(iii) 地勢同泥土（不利水稻，適合放牧）：<br>① Xibei 多山／高原，坡陡、地勢崎嶇（Figure 2c：Qing Zang Gaoyuan / Himalayas）。<br>② 泥土薄而貧瘠，只適合種草；Photo 2b：易有水土流失，進行 pastoral farming。','(b)(iii) Relief and soil (unfavourable for crops, suitable for grazing):<br>① Xibei is hilly / mountainous with steep slopes and rugged relief (Figure 2c: Qing Zang Gaoyuan / Himalayas).<br>② Thin, infertile soil, only suitable for grass; Photo 2b: soil erosion occurs easily, pastoral farming is practised.')))]
MAPANS=[
('2025-26 UT · Section C '+T('（16 分，地圖 1:5,000）','(16 marks, map 1:5,000)'),'<p>'+tbl([
 ['1(a) Statement scale','1 cm to 50 m'],['1(b) Linear scale',T('0 – 250 m（每 50 m 一格）','0 – 250 m (every 50 m)')],
 ['2(a) Easting X / (b) Northing Y','19 / 66'],
 ['3(a) Hotels in square 1665','2'],['3(b) Playgrounds in 1765','0'],['3(c) Kindergarten in 1865','True'],['3(d) Secondary school in 1764','True'],
 ['4(a) Church along Hennessy Rd (6-fig)','182656'],['4(b) Hotel along Jaffe Rd','187660'],['4(c) Car park near Pacific Place','163657 / 163656'],
 ['4(d) Legislative Council Complex (4-fig)','1667'],['4(e) Pacific Place','1665'],['4(f) Petrol station near Kennedy Rd','1764'],
 ['5(a) Whole-circle bearing of shopping mall (177672) from spot height 53.1 (162644)','027° (±2°)'],['5(b) Reduced bearing of cinema (168657) from primary school (178647)','N 45° W (±2°)']],[T('題目','Question'),T('答案','Answer')])+'</p>'+EG(T('3(c)(d) 嘅 True／False 答案我由標準答案表睇，請對返 map extract。5(a) 標準答案 PDF 嘅度數符號顯示唔清，我讀成 027°。','The True / False answers in 3(c)(d) are read from the answer table; please check against the map extract. The degree sign in the 5(a) answer PDF is unclear; I read it as 027°.'))),
('2024-25 QE · Section C '+T('（15 分，地圖 1:20,000）','(15 marks, map 1:20,000)'),'<p>'+tbl([
 ['1(a) Statement scale','1 cm to 200 m'],['1(b) Linear scale',T('0 – 1000 m（每 200 m 一格）','0 – 1000 m (every 200 m)')],
 ['2 Churches south of Northing 73','13'],['3 I / II / III','Declared monument / Government office / Trigonometric station'],
 ['4(a) Clinic at Nam Shan Estate','085725'],['4(b) Post office at Lei Cheng Uk Estate','073730'],
 ['5(a) Police station (073721) from fire station','SW, 222° (±2°)'],['5(b) Restricted access (084741) from spot height 305 (072740)','ENE, 84° (±2°)'],
 ['6 East Rail Line (090720)→(089731)',T('圖上 6.1 cm（6–6.2 cm 接受）× 200 m = 1,220 m（1,200–1,240 m 接受）','6.1 cm on the map (6–6.2 cm accepted) × 200 m = 1,220 m (1,200–1,240 m accepted)')]],[T('題目','Question'),T('答案','Answer')])+'</p>'+EG(T('Fire station 座標：試題寫 082731，答案寫 081731，兩份有出入，以老師講嘅為準。','Fire station grid reference: the question paper says 082731 but the answer says 081731. They differ, so follow your teacher.')))]
def build_past():
    ref=''.join(item('ut-b%d'%i if i<2 else 'qe-b%d'%(i-1),h,b,['','s2','s3','s4'][i%4]) for i,(h,b) in enumerate(STRUCT))
    ref='<p class="sub">'+T('題目圖片（相、世界地圖、地圖摘錄）冇放喺度，答案內容跟標準答案。','The question photos, world map and map extracts are not included. Answers follow the marking schemes.')+'</p>'+refpane(ref,T('撳開睇標準答案','Tap to see the marking scheme'))
    mp=''.join(item('map-%d'%i,h,b,['','s2'][i%2]) for i,(h,b) in enumerate(MAPANS))
    mp='<p class="sub">'+T('讀圖題要對住原本嘅 map extract 做，呢度只有答案同做法。','Map reading questions need the original map extract. Only answers are given here.')+'</p>'+mp
    rnd=random.Random(11);M=[]
    for k,(src,stem,o,a,note) in enumerate(PASTMCQ):
        idx=list(range(4));rnd.shuffle(idx)
        M.append(['【%s】%s'%(src,stem),[o[j] for j in idx],idx.index(a),'ut-b0' if src.startswith('2025') else 'qe-b1',note])
    tagmap={m[3]:m[3] for m in M}
    js=mcq('mcqBestGeoPast',M,tagmap,10,T('歷屆選擇題，十條','Past-paper MCQs, 10 questions'))
    gpage('geo-past',T('歷屆試題','Past papers'),T('2025-26 統一測驗、2024-25 第一次考試：選擇題、結構題、讀圖題答案','2025-26 Uniform Test and 2024-25 First Quarterly Exam: MCQs, structured questions and map-reading answers'),'notebook',
      [('p-mcq',T('歷屆選擇題','Past MCQs')),('p-ref',T('結構題答案','Structured')),('p-map',T('讀圖題答案','Map reading'))],
      [('p-mcq','<div id="mcqroot"></div>'),('p-ref',ref),('p-map',mp)],js)
build_food();build_map();build_past()
GEOHUB='''<!doctype html>
<html lang="zh-HK">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Geography</title>
<meta name="description" content="F.2 Geography">
<meta name="ty-lang" content="bi">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Huninn&display=swap">
<link rel="stylesheet" href="../assets/base.css">
<script src="../assets/theme.js"></script>
</head>
<body>
<div class="wrap">
  <div class="bar"><a href="../../">‹ %(home)s</a><b>Geography</b></div>
  <h1>Geography %(h1)s</h1>
  <p class="sub">First Term Uniform Test 2026-2027 · %(sub)s</p>
  <div data-art="farm"></div>
  <p class="grp">%(scope)s</p>
  <p class="sub">%(scopetxt)s</p>
  <a class="hub h1c" href="../geo-food/"><strong>Food Problems %(fp)s</strong><span class="d">%(d1)s</span><span class="tag">%(t1)s</span><span class="tag">%(t2)s</span><span class="tag">%(t3)s</span><span class="tag">%(t4)s</span></a>
  <a class="hub h2c" href="../geo-map/"><strong>Map Reading %(mr)s</strong><span class="d">%(d2)s</span><span class="tag">%(t1)s</span><span class="tag">%(t5)s</span><span class="tag">%(t2)s</span><span class="tag">%(t4)s</span></a>
  <a class="hub h1c" href="../geo-farm-3d/"><strong>%(fm)s</strong><span class="d">%(d4)s</span><span class="tag">3D</span><span class="tag">%(t4)s</span></a>
  <a class="hub h3c" href="../geo-past/"><strong>%(pp)s</strong><span class="d">%(d3)s</span><span class="tag">%(t4)s</span><span class="tag">%(t6)s</span></a>
  <div class="stat"><h2>%(sth)s</h2><ul>%(stl)s</ul></div>
  <footer>%(foot)s</footer>
</div>
<script src="../assets/art.js"></script>
</body>
</html>
'''
hub=GEOHUB%dict(home=T('首頁','Home'),h1=T('中二地理','(Form 2)'),sub=T('選擇題、結構題、讀圖題 · 可用計數機。','multiple choice, structured and map-reading questions · calculator allowed.'),
 scope=T('範圍','Syllabus'),
 scopetxt=T('課本：<i>Junior Secondary Exploring Geography 3 Food Problems</i> Unit 1（p.3-13）、Unit 2（p.14-21）、Unit 3（p.22-29）；<i>New Century Geography Map Reading</i> Chapter 1、2（唔考 p.33-35）、3、4（唔考 p.59-66）；課堂筆記、功課簿、讀圖練習同小測。','Textbooks: <i>Junior Secondary Exploring Geography 3 Food Problems</i> Unit 1 (pp.3-13), Unit 2 (pp.14-21), Unit 3 (pp.22-29); <i>New Century Geography Map Reading</i> Chapter 1, 2 (excluding pp.33-35), 3, 4 (excluding pp.59-66); in-class notes, assignment book, map reading exercises and quizzes.'),
 fp=T('食物問題',''),mr=T('讀圖',''),pp=T('歷屆試題 2024-25 / 2025-26','Past papers 2024-25 / 2025-26'),
 d1=T('Unit 1 食物從哪裡來、Unit 2 中國農業地區、Unit 3 糧食供求同自給率。','Unit 1 where food comes from, Unit 2 farming regions in China, Unit 3 food demand, supply and self-sufficiency.'),
 d2=T('比例尺、方格參考、方向同距離，附隨機計算練習。','Scale, grid references, direction and distance, with random calculation practice.'),
 d3=T('14 條真實選擇題、結構題同讀圖題標準答案。','14 real MCQs, with marking schemes for structured and map-reading questions.'),
 fm=T('3D 農場島','3D Farm Island'),d4=T('行入島睇 inputs、processes、outputs，比較兩個農場，仲有計時（可關）挑戰。有 2D 版。','Explore inputs, processes and outputs, compare two farms, and take a challenge with an optional timer. A 2D view is included.'),
 t1=T('重點','Notes'),t2=T('配對','Match'),t3=T('填空','Fill in'),t4=T('選擇題','Quiz'),t5=T('計算','Practice'),t6=T('答案','Answers'),
 sth=T('資料狀態','Material status'),
 stl=''.join('<li><span class="st %s">%s</span>%s</li>'%x for x in [
  ('',T('已對照','Checked'),T('Food Problems：課本 Unit 1-3（p.3-29）同兩份試卷','Food Problems: textbook Units 1-3 (pp.3-29) and both past papers')),
  ('',T('已有','Done'),T('歷屆試題 2024-25 / 2025-26 同標準答案','Past papers 2024-25 / 2025-26 with marking schemes')),
  ('p',T('未對課本','Not checked'),T('Map Reading：只依試卷同一般讀圖知識整理，待課本 Chapter 1-4','Map Reading: based on past papers and general knowledge only; textbook Chapters 1-4 still needed')),
  ('t',T('未收到','Missing'),T('課堂筆記、功課簿、讀圖練習','Class notes, workbook and map practice'))]),
 foot=T('Food Problems 已對照課本；Map Reading 仲未對過課本，請對返《Map Reading》。','Food Problems has been checked against the textbook; Map Reading has not yet, so please check it against the Map Reading book.'))
if LANG=='en': hub=postEN(hub).replace('href="../../">','href="../../../">')
os.makedirs(ROOT+'geo',exist_ok=True)
open(ROOT+'geo/index.html','w',encoding='utf-8').write(hub)
