---
name: revision-page
description: Build or extend a bilingual picture-book revision page (notes, match, fill-in, MCQ, hard tier) for a school subject in tio-edu-site from the user's textbook photos and past papers.
---
1. Read `CLAUDE.md`, `docs/PLAYBOOK.md`, `docs/ARCHITECTURE.md`, `docs/CONTENT-STATUS.md`.
2. Get scope + source material from the user; read every page image before writing content.
3. Add the content as data in `tools/gen/` (follow the shapes in ARCHITECTURE.md); add `T(zh,en)` strings if the subject is English-exam.
4. `./tools/gen/build.sh`; smoke-test with Playwright (see `tools/gen/test-*.example.js`).
5. Update the 資料狀態 panel and `docs/CONTENT-STATUS.md`; commit and push to `main`; report in Cantonese what changed, and any textbook/marking-scheme conflicts.
