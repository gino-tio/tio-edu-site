#!/usr/bin/env bash
# Regenerate all generated pages, then fix meta descriptions that the shared page() template gets wrong.
set -e
cd "$(dirname "$0")/../.."
python3 tools/gen/gen.py
sed -i 's/content="《楊修之死》單元/content="成語名句：單元/' works/cy-unit*/index.html works/en/cy-unit*/index.html 2>/dev/null || true
sed -i 's/content="《楊修之死》名句：忠誠溫習。"/content="校本價值教育名句 1-9：忠誠（責任感、委身、貢獻）溫習。"/' works/mingju/index.html
for f in works/geo*/index.html works/en/geo*/index.html; do sed -i 's/content="《楊修之死》[^"]*"/content="中二地理上學期統一測驗溫習。"/' "$f"; done
echo "built; review with: git status && git diff --stat"
