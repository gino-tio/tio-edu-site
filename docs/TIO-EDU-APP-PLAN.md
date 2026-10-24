# 計劃：將呢個溫習網站做法搬入 Tio Edu app

目標：學生 login 後，可以**自己上載課本／試卷／筆記**同輸入**考試範圍**，app 自動製作同今次網站一樣嘅溫習頁（重點速覽、配對、填空、選擇題、挑戰題、歷屆題），喺 app 內溫習，並記錄成績同弱點。

## 1. 今次網站教識我哋嘅五件事
1. **內容同引擎分開**：引擎（`shared.js`、`base.css`、`art.js`、`theme.js`）已經通用；內容目前由 Python 生成，要改成 JSON「溫習包」(pack)。
2. **做法可重複**：收資料 → 睇晒每頁 → 整重點 → 出題（課本／歷屆／AI／挑戰）→ 測試 → 標明資料狀態。
3. **質素靠對照來源**：只靠試卷整理嘅筆記漏咗約四成課本內容；每條題目要有來源頁碼。
4. **小朋友友善**：大字、繪本風、日夜模式、可關計時、挑戰題、只存本機／自己帳戶成績。
5. **資料狀態透明**：「已對照／未對照／未收到」標籤，AI 整理嘅內容預設係「未經核對」。

## 2. 目標架構
```
Flutter app（家長帳戶 → 學生子帳戶）
 ├─ 上載：相機／相簿／PDF ──► Supabase Storage（私有 bucket）
 ├─ 溫習播放器：WebView 載入 player.html（重用 shared.js/base.css/art.js）+ pack JSON
 └─ 成績／弱點：attempts、question_stats
Supabase
 ├─ Edge Function `material-ingest`：圖／PDF → 逐頁文字（vision 模型，經 OpenRouter）
 ├─ Edge Function `pack-build`：文字 + 範圍 → pack JSON（notes/match/fill/mcq/hard/AI）
 ├─ Edge Function `pack-verify`：第二次檢查每題有無來源支持，唔過就剔走
 └─ 現有 `ai-proxy` + 每學生每日 AI quota（所有 AI 經 Edge Function，app 內冇 API key）
```
**Pack JSON（重點欄位）**：`subject, exam{term,scope}, lang{zh|en|bi}, status{checked|ai_unchecked|missing}, sources[{materialId,page}], notes[{id,title,html,src}], match[{name,pairs}], fill[{title,text,answers}], mcq[{q,options,correct,note,explain,hard,ai,src}], past[{paper,year,items}]`。形狀同 `docs/ARCHITECTURE.md` 嘅資料格式一致，只係改為 JSON。

**播放器**：寫 `player.js`，由 JSON 生成 tabs 同遊戲（取代 Python 生成器嘅輸出部分），先用 WebView 包入 Flutter（最快、100% 重用現有遊戲同美術）；之後視乎需要先考慮原生 Flutter。

## 3. 資料表（全部 RLS）
`subjects`、`exams(student_id, subject_id, term, scope_text)`、`materials(owner_parent_id, student_id, kind[textbook|paper|scheme|notes|scope], storage_path, page_no, ocr_text, status)`、`packs(exam_id, version, json, status, lang)`、`attempts(student_id, pack_id, mode, score, timer_on, hard_only, created_at)`、`question_stats(student_id, pack_id, qid, wrong_count, last_seen)`。
規則：家長見到名下全部學生；學生只見自己；Storage 路徑 `{parent}/{student}/…`；上載物料預設私有，唔公開。

## 4. 分階段（每階段用「完成準則」驗收，同 tio-edu CLAUDE.md 一致）
| 階段 | 做乜 | 完成準則（可跑嘅檢查） | 負責 |
|---|---|---|---|
| P0 播放器 | 寫 `export_pack.py` 將 geo-food 轉 JSON；寫 `player.html/js`；放入 Flutter assets | app 內開到 geo-food，4 個 tab 都動；做完一輪 MCQ 後 `attempts` 多一行（SQL 查到） | flutter-dev、porter |
| P1 Schema + RLS | 上面資料表同 Storage policy | security advisor 乾淨；SQL 測試：學生 A 讀唔到學生 B 嘅 materials/packs | supabase-dev |
| P2 上載 + OCR | 上載 UI；`material-ingest` | 上載 3 張 Food Problems 相 → 3 行 `materials.ocr_text`，其中包含 "growing season" | flutter-dev、supabase-dev |
| P3 生成溫習包 | `pack-build` + JSON schema 驗證 | 以 Unit 2 相生成 pack：通過 schema；每題有 `src`；同現成 geo-food 對比，「關鍵事實清單」（約 30 條）覆蓋 ≥ 80% | supabase-dev（lead 寫 prompt） |
| P4 核對 + 狀態 | `pack-verify`；資料狀態標籤；矛盾（課本 vs 標準答案）標 ⚠ | 抽樣 20 題人手檢查 ≥ 90% 正確；故意放一題無來源嘅題 → 被剔走 | supabase-dev、qa-verifier |
| P5 弱點溫習 | 錯題簿、按範圍篩選、挑戰題模式、計時開關 | 做錯 3 題後，「弱點」頁顯示該 3 題 | flutter-dev |
| P6 家長審核 + 分享 | 家長標「已核對」；可選：分享只讀 pack 連結（唔含原書相） | 家長改狀態後學生端即時見到；分享連結打開冇原書圖片 | flutter-dev |
| P7 TestFlight | 現有 testflight workflow | build 上載成功，實機走通 P0–P5 | uat-tester |

先做**地理**一科（有現成 benchmark：本 repo 嘅 geo-food 同 geo-past），再加其他科。

## 5. AI 出題品質守則
- Prompt 內附 3–5 題本網站嘅標準題、挑戰題作 few-shot，要求 **HK Form 2 Band 1** 程度。
- 只准用上載資料內嘅事實；每題要引用來源頁；冇來源就唔出。
- 答案、選項、解釋由第二次呼叫獨立檢查；計算題由程式重算。
- 標示【AI 出題】，同「未經核對」狀態；家長可一鍵標「已核對」。
- 課本同標準答案唔一致時，兩邊都顯示，並提示以學校標準答案為準。

## 6. 風險同對策
OCR 讀錯相／手寫 → 逐頁預覽 + 可手動改字；AI 亂作 → 來源引用 + 驗證 + 狀態標籤；成本 → 每日 quota、先 OCR 一次重用、`FAST` 模型做整理、`SMART` 模型只做生成；兒童私隱 → 無廣告無追蹤、物料私有、可刪除；版權 → 原書相只留喺帳戶內，唔公開分享；中英文 → pack 帶 `lang`，英文考試科自動出雙語。

## 7. 需要 Gino 決定
1. 播放器先用 WebView（建議）定直接原生 Flutter？
2. 要唔要「分享 pack 去 WhatsApp」功能（只讀、唔含原書圖）？
3. AI 溫習包由邊個核對：家長，定老師？
4. 第一階段只做地理，OK？
5. 學生可唔可以自己上載，定要家長批准？

## 8. 建議加入 tio-edu CLAUDE.md 嘅一段
「溫習包功能：內容與引擎分開；引擎來自 `gino-tio/tio-edu-site`（`works/assets/*`）；pack JSON 形狀見該 repo `docs/ARCHITECTURE.md`；每條 AI 題必須有 `src`；資料狀態三態 checked / ai_unchecked / missing。」
