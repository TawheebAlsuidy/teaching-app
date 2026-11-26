# QA Audit — Science 9 (`eng-sci-9`)

- **Lesson**: `SCIENCE 9 — The Moon`
- **Pupil's Book**: p. 73 (`pdf_page: 75`, `pb-75.png`)
- **Workbook**: pp. 107–108 (`pdf_page: 108–109`, `wb_tail-108.png`..`wb_tail-109.png`)

## Literal Fidelity & Grid Audit
1. Preserved PB p. 73 misprint `prints` (`rotates, or prints, around its own axis`) verbatim in `from_book`, cross-referencing WB `9 C #3` (`spins`) and WB p. 116 (`spin`).
2. Preserved WB `9 A #6` stray quote `' Gibbous Moon?`, and clearly separated external astronomical km distances in `9 A #2, #4` under educational additions alongside PB's relative distance ratios (`367–419×`).
3. Audited every cell of the 9×9 wordsearch in `9 E` (`wb_tail-109.png`): found 9 intact Moon terms (`space`, `rotate`, `axis`, `orbit`/`orbits`, `eclipse`, `phase`, `spin`, `lunar`, `satellite`) plus bottom-row `s-o-l-a-u` (likely a 1-letter print typo `u` for `r` in `solar`).
4. Added `CHECK_WORDSEARCH_ALL` verification via Python across dictionary and PB9 words.
