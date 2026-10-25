# Architecture

## Repo layout
```
index.html                 intro page; hub cards → works/ (中文) and works/geo/ (地理)
works/index.html           中文 hub (hand-written) incl. 資料狀態 panel
works/assets/              base.css, theme.js, shared.js, art.js  (shared by every page)
works/<folder>/index.html  zh pages        works/en/<folder>/index.html  English twins
works/geo, geo-food, geo-map, geo-past, geo-farm-3d     地理 hub + 3 sub pages + 3D Farm Island (generated, zh + en)
works/eng, eng-vocab, eng-read, eng-read1, eng-adj, eng-cond, eng-tense, eng-proof, eng-paper, eng-shop-3d   English hub + 9 pages (generated, zh + en; `c5body.py`)
works/part-b, part-c, cy-unit1/2, mingju, yx-*, ...   中文 pages (generated)
works/typhoon-memory-route, yx-3d          three.js route page (+ generated 3D variant)
tools/gen/                 Python generators + build.sh + example Playwright tests
docs/                      this documentation
.claude/skills/            repo skill: revision-page
```

## Generators (tools/gen)
- `gen.py`: helpers `page()`, `refpane()`, `item()`, `K()/P()/EG()`, JS emitters `tfjs() mcqjs() filljs() matchjs()`; then `exec`s `content.py` → `content4.py`.
- `content.py` 楊修之死 pages (yx-*); `content2.py` 成語 (cy-unit1/2, part-b hub); `content3.py` 名句 (mingju); `content4.py` + `c4head.py` + `c4body.py` Geography. `c4body.py` is executed twice: `LANG='zh'` then `'en'` (ROOT switched to `works/en/`); `T(zh,en)` picks the language string.
- `c6farm.py` + `c6farm.html` generate the 3D Farm Island (`geo-farm-3d`, zh + en): Three.js r128 from cdnjs, every model procedural (no Blender assets), own orbit/pinch controls, 2D tile fallback, challenge with optional timer (`tyTimer`, best key `farm3dBest[_nt]`). `c7shop.py` + `c7shop.html` (+ `c7scene.js`, the scene block pasted into the html) generate the 3D Shopping Street (`eng-shop-3d`) with the same engine; views, markers, tag→stop map, 2D tiles and challenge questions come from the Python data (`DATA`). `window.__farm` is a test hook. `c5body.py` English grammar pages (also executed for `zh` then `en`; notes are English, zh build adds Chinese glosses via `G(en,zh)`). `gen3d.py` derives `yx-3d` from `typhoon-memory-route`.
- `build.sh` runs everything and patches meta descriptions (the shared `page()` template defaults to 《楊修之死》 wording).

## Data shapes used in content files
- Notes: list of `(heading, html_body)` → collapsible `item` cards with ids `g-i0…`; question tags point at these ids so a wrong answer can jump to the right note.
- Match: `{name, help, pairs:[[term, meaning],…]}` (6 pairs per set).
- Fill: `{t:title, p:'text with {0} {1}', b:[[accepted answers],[…]]}`.
- MCQ: `[question, options, correctIndex, noteTag, explanation, hardFlag?]` — convention: write the correct option FIRST, then shuffle with a seeded RNG and re-index. Hard questions carry `h:1` (6th element).
- AI questions: same shapes, labelled `AIL` = 【AI 出題】.

## Engine `works/assets/shared.js` → global `TY`
`shuffle, lsGet, lsSet, esc, tabs, mask, quiz, fill, match, derange, scopeOn, scopeInit`.
- `TY.quiz`: modes `'tf'` / `'mcq'`, Kahoot-style scoring (speed bonus), per-question countdown. Settings: timer on/off (`tyTimer`), challenge-only (`tyLevel`, question flag `h`). Best score key `bkey()` = key + (`_nt` if timer off) + (`_h` if hard-only). localStorage only, wrapped in try/catch.
- `TY.scopeOn/scopeInit`: filter switch to hide "not examined" content (used on 楊修之死 pages).
- `L(zh,en)` translates engine UI strings when `<html lang="en">`.

## Theme, language, art
- `theme.js`: injects `#themeBtn` (day/night, `localStorage`), and — when `<meta name="ty-lang" content="bi">` precedes it — `#langBtn` ("EN"/"中") linking to the twin path and remembering `tyLang`; auto-redirects to the stored language. Chinese-only subjects omit the meta.
- `base.css`: picture-book style (Huninn font, thick outlines, pastel tokens, `.hub`, `.tb` tables, `.stat` status panel), CSS variables for day/night.
- `art.js`: SVG scenes mounted on `[data-art]`: scene, walker, notebook, camp, cloud, farm, map, scroll.

## Testing
Playwright chromium against `python3 -m http.server`; abort Google Fonts requests; set `tyLang` via `addInitScript` when testing `/works/en/`. Checks: no `pageerror`, tab switching, match/fill/MCQ playthrough, timer-off flow, EN pages free of `[一-鿿]`, mobile width 390 has no horizontal overflow.

## 3D pages (testing notes)
Launch chromium with `--use-gl=swiftshader --enable-unsafe-swiftshader` (see `tools/gen/test-3d.example.js`). A full-viewport `page.screenshot()` of a WebGL page shows a white box in headless; clipped screenshots or `window.__farm.snap()` (canvas `toDataURL`) render correctly, so use those to inspect visuals.
