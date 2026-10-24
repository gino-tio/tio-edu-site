# Playbook: how a revision subject is made (repeatable method)

The workflow used for 中文 and 地理. Another session (or the Tio Edu app pipeline) should follow it.

## 0. Intake
1. Ask for the **exam scope** (syllabus image / teacher notice) and the **source material**: textbook pages (photos/PDF), past papers + marking schemes, school handouts. Photos of annotated pages are welcome (handwriting shows what the student/teacher stressed).
2. Render PDFs to JPG (`pdftoppm -scale-to-x 1500`) and read page by page; extract past-paper text (`pdftotext`) and keep page PNGs for diagrams/maps.
3. List what is NOT yet provided and show it on the hub as 資料狀態 (checked / not checked / missing).

## 1. Decide the page set (one page per exam part)
Hub (目錄) → sub pages. Each sub page has tabs: **重點速覽** (notes) · **配對遊戲** · **寫字填空** · **選擇題 / 是非題** (+ **計算練習**, **答案** where relevant). Past papers get their own page with real MCQs and marking-scheme answers.

## 2. Write content as data (in `tools/gen/*.py`)
- Notes: short highlighted key points (`K()`), tables for comparisons, worked examples (`EG()`), exam-source tags ("2025-26 UT Q3").
- Games: match sets of 6 pairs; fill-in with accepted-answer lists (accept spelling variants, e.g. fertilizers/fertilisers); MCQ with a note tag and an explanation.
- Every question links to a note id so a wrong answer can open the right note.
- Question sources, in this order: (a) textbook facts and figures; (b) real past-paper items; (c) **AI-written** items (label 【AI 出題】) following the exam style; (d) **hard/challenge** items (`h:1`) at HK Form 2 Band 1 level: multi-statement "(1)(2)(3)" items, calculations, data interpretation.
- Textbook vs marking-scheme conflicts: show both, mark ⚠, follow the school's marking scheme.
- Remove content the teacher says is not examined (use `scopeOn` filter or delete).

## 3. Bilingual rule
Subjects whose exam is in English (地理, etc.) get an English twin under `works/en/` and a 中/EN switch; 中文 and 中史普通話 do not. Write each string once with `T(zh,en)`. English notes are our own translation; keep textbook terms exactly (e.g. "farming region", "growing season").

## 4. Child-friendly rules (non-negotiable)
Large type; picture-book style; day/night mode; timer switch (on/off, persisted); challenge-only toggle; no ads/tracking; best scores in `localStorage` only.

## 5. Verify, then ship
`./tools/gen/build.sh` → Playwright smoke test → compare facts against the source (re-open the textbook page for any figure) → commit → push `main` (Pages redeploys in ~1-2 min) → tell the user what changed and what conflicts remain.

## 6. Lessons learned
- Look at the source pages before writing: notes made from past papers alone missed ~40% of the textbook.
- Random MCQ order: put the right option first, shuffle with a seeded RNG, re-index; a mixed "which index is correct" field caused wrong answers once.
- Match games must not put answers in a line (shuffle both columns; `derange`).
- Users found standard questions too easy → always add a hard tier; users felt timed → always provide a no-timer mode.
- Mobile first: 390px width, no horizontal overflow, nav chips must not wrap.
- Verify the numbers: percentage questions (e.g. 66.5 ÷ 613.7 = 10.8%) are recomputed in code, not by eye.
