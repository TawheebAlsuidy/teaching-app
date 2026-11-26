# English Interactive Book (`english`) — Complete Coverage & QA Report

**Subject**: English Course — Pupil's Book 6 & Workbook 6 (3rd Secondary, Yemen)  
**Target Directory**: `books/english/` (`content/english/`, `QA/english/`)  
**Validation Status**: `92 / 92` lesson JSONs **PASS** (`engine/build/validate_book.py --book-root books/english --check-assets`)  
**Build Status**: `Built english: 92 lessons` (`engine/build/build_book.py --subject english`)  
**Offline Status**: 100% local assets (`assets/ref/*.webp`, `assets/media/*.webp`, `engine/vendor/`), zero CDN dependencies.

---

## 1. Aggregate Curriculum Statistics

| Section / Unit | ID | Lessons | Content Blocks | WB Activities | Section Check MCQs | Flashcards | Glossary Terms (`in_book_wordlist`) |
|---|---|---:|---:|---:|---:|---:|---:|
| Unit 1: Describing things | `u1` | 12 | 45 | 31 | 25 | 54 | 133 (83) |
| Unit 2: Reporting events | `u2` | 12 | 32 | 36 | 24 | 41 | 90 (68) |
| Unit 3: Looking for a job | `u3` | 12 | 25 | 33 | 24 | 32 | 85 (65) |
| Unit 4: Tables, flow charts and diagrams | `u4` | 12 | 19 | 31 | 24 | 24 | 87 (72) |
| Unit 5: Working things out | `u5` | 12 | 17 | 28 | 24 | 24 | 44 (34) |
| Unit 6: Looking back | `u6` | 12 | 15 | 32 | 24 | 31 | 75 (47) |
| Arts Reader (Literary Section) | `arts` | 10 | 15 | 43 | 20 | 30 | 96 (96) |
| Science Reader (Scientific Section) | `science` | 10 | 15 | 34 | 20 | 30 | 139 (139 / incl. lesson WL) |
| **Total** | **8 units** | **92** | **183** | **268** | **185** | **266** | **749 (610 marked `in_book_wordlist`)** |

---

## 2. Page-by-Page Audit Against Official PDFs

### A) Pupil's Book 6 (`انجليزي-الطالب-للصف-الثالث-الثانوي.pdf` — **77 PDF pages**)
- **PDF p. 1**: Front cover.
- **PDF p. 2**: Official Table of Contents (`Contents`; note Units 1–5 omit `.9–.12` numbers in the PB TOC header while inside pages and Workbook contain all `.1–.12` lessons — all 12 per unit are implemented).
- **PDF pp. 3–76 (`Book pp. 1–74`)**: **74 / 74 (`100%`)** content pages covered inside `lesson.source_refs`, with local reference scans (`assets/ref/pb_p001.webp` .. `pb_p074.webp`).  
  *(Note: PDF p. 65 / Book p. 63 is a blank separator page before the yellow `Science reader` cover on PDF p. 66 / Book p. 64; both are attached to `SR1`.)*
- **PDF p. 77**: Rear emblem page (single small school emblem in center; verified visually and excluded as an unneeded asset).

### B) Workbook 6 (`english_work_12th (1).pdf` — **120 PDF pages**)
- **PDF p. 1**: Front cover.
- **PDF pp. 2–111 (`Book pp. 1–110`)**: **110 / 110 (`100%`)** exercise pages covered inside `lesson.source_refs` (`u1–u6`, `arts`, `science`), with local reference images (`assets/ref/wb_p001.webp` .. `wb_p110.webp`).
- **PDF pp. 112–118 (`Book pp. 111–117`)**: **7 / 7 Word list pages** (`Unit 1`..`Unit 6`, `Arts 1–10`, `Science 1–10`) mapped across `word_glossary_map` (`610` entries flagged with `in_book_wordlist: true` and cited `wb_page` numbers across `1..69` and `111..117`). Note all Arts and Science Reader lessons (`AR1–AR10`, `SR1–SR10`) explicitly carry `wb_page: 114–117` vocabulary entries matching the printed Word list.
- **PDF p. 119**: Imprint / Copyright page (`Terry O'Neil and Peter Snow`, Garnet Publishing Limited for the Ministry of Education, Republic of Yemen, © 2000).
- **PDF p. 120**: Official Workbook `Contents` table (`Units 1–6`, `Arts 1–10`, `Science 1–10`).

---

## 3. Complete 92-Lesson Coverage Matrix

| Unit | Code | Lesson ID | Title | PB Pages (PDF) | WB Pages (PDF) | Blocks / Acts / MCQs / FC | Glossary (`in_book_wordlist`) |
|---|---|---|---|---|---|---|---:|
| u1 | `1.1` | `eng-u1-1_1` | Shapes, coverings and materials | PB [1] (PDF [3]) | WB [1] (PDF [2]) | 5 / 2 / 3 / 10 | 24 (11 WL) |
| u1 | `1.2` | `eng-u1-1_2` | Listening and describing | PB [] (PDF []) | WB [2, 3] (PDF [3, 4]) | 3 / 1 / 1 / 3 | 6 (0 WL) |
| u1 | `1.3` | `eng-u1-1_3` | Lost | PB [2] (PDF [4]) | WB [3, 4] (PDF [4, 5]) | 4 / 4 / 2 / 5 | 15 (14 WL) |
| u1 | `1.4` | `eng-u1-1_4` | An unusual animal | PB [3] (PDF [5]) | WB [4] (PDF [5]) | 6 / 2 / 3 / 8 | 16 (10 WL) |
| u1 | `1.5` | `eng-u1-1_5` | Language review 1 | PB [4] (PDF [6]) | WB [5] (PDF [6]) | 3 / 3 / 2 / 3 | 10 (10 WL) |
| u1 | `1.6` | `eng-u1-1_6` | The countryside | PB [5] (PDF [7]) | WB [5, 6] (PDF [6, 7]) | 3 / 4 / 2 / 4 | 13 (5 WL) |
| u1 | `1.7` | `eng-u1-1_7` | Listening and map directions | PB [] (PDF []) | WB [6, 7] (PDF [7, 8]) | 4 / 3 / 2 / 3 | 8 (2 WL) |
| u1 | `1.8` | `eng-u1-1_8` | Vocabulary and comprehension (PB p. 6) | PB [6] (PDF [8]) | WB [8] (PDF [9]) | 3 / 2 / 2 / 4 | 8 (4 WL) |
| u1 | `1.9` | `eng-u1-1_9` | A drive in the countryside | PB [6] (PDF [8]) | WB [9, 10] (PDF [10, 11]) | 4 / 3 / 2 / 4 | 9 (9 WL) |
| u1 | `1.10` | `eng-u1-1_10` | Language review 2 | PB [7] (PDF [9]) | WB [10, 11] (PDF [11, 12]) | 3 / 3 / 2 / 3 | 6 (5 WL) |
| u1 | `1.11` | `eng-u1-1_11` | A view from a window | PB [8] (PDF [10]) | WB [11, 12] (PDF [12, 13]) | 5 / 3 / 2 / 4 | 14 (13 WL) |
| u1 | `1.12` | `eng-u1-1_12` | Write a description in your copybook | PB [] (PDF []) | WB [12] (PDF [13]) | 2 / 1 / 2 / 3 | 4 (0 WL) |
| u2 | `2.1` | `eng-u2-2_1` | Newspaper headlines | PB [9] (PDF [11]) | WB [13, 14] (PDF [14, 15]) | 3 / 2 / 2 / 4 | 12 (10 WL) |
| u2 | `2.2` | `eng-u2-2_2` | Today's news | PB [10] (PDF [12]) | WB [14, 15] (PDF [15, 16]) | 3 / 3 / 2 / 4 | 12 (9 WL) |
| u2 | `2.3` | `eng-u2-2_3` | Listening to news interviews | PB [] (PDF []) | WB [15, 16] (PDF [16, 17]) | 3 / 3 / 2 / 3 | 4 (0 WL) |
| u2 | `2.4` | `eng-u2-2_4` | Don and Debbie: dreamers | PB [11] (PDF [13]) | WB [16, 17] (PDF [17, 18]) | 3 / 4 / 2 / 4 | 10 (9 WL) |
| u2 | `2.5` | `eng-u2-2_5` | Language review 3 | PB [12] (PDF [14]) | WB [17, 18] (PDF [18, 19]) | 3 / 3 / 2 / 3 | 7 (7 WL) |
| u2 | `2.6` | `eng-u2-2_6` | Natural disasters | PB [13] (PDF [15]) | WB [18, 19] (PDF [19, 20]) | 2 / 3 / 2 / 4 | 13 (12 WL) |
| u2 | `2.7` | `eng-u2-2_7` | A newspaper report | PB [14] (PDF [16]) | WB [19, 20] (PDF [20, 21]) | 2 / 5 / 2 / 4 | 10 (10 WL) |
| u2 | `2.8` | `eng-u2-2_8` | Listening to the radio news | PB [] (PDF []) | WB [21, 22] (PDF [22, 23]) | 3 / 2 / 2 / 3 | 3 (0 WL) |
| u2 | `2.9` | `eng-u2-2_9` | Questions, intonation and interviewing | PB [] (PDF []) | WB [22, 23, 24] (PDF [23, 24, 25]) | 3 / 2 / 2 / 3 | 4 (0 WL) |
| u2 | `2.10` | `eng-u2-2_10` | Language review 4 | PB [15] (PDF [17]) | WB [24, 25, 26] (PDF [25, 26, 27]) | 2 / 3 / 2 / 4 | 5 (5 WL) |
| u2 | `2.11` | `eng-u2-2_11` | Armenia - 7, December 1988 | PB [16] (PDF [18]) | WB [26, 27] (PDF [27, 28]) | 3 / 4 / 2 / 3 | 8 (6 WL) |
| u2 | `2.12` | `eng-u2-2_12` | Planning and writing a newspaper report | PB [] (PDF []) | WB [27, 28] (PDF [28, 29]) | 2 / 2 / 2 / 2 | 2 (0 WL) |
| u3 | `3.1` | `eng-u3-3_1` | Getting work experience | PB [17] (PDF [19]) | WB [29, 30] (PDF [30, 31]) | 3 / 4 / 2 / 4 | 15 (15 WL) |
| u3 | `3.2` | `eng-u3-3_2` | Listening: worthwhile jobs & interview | PB [] (PDF []) | WB [30, 31] (PDF [31, 32]) | 2 / 2 / 2 / 3 | 4 (1 WL) |
| u3 | `3.3` | `eng-u3-3_3` | Thinking about the future | PB [18] (PDF [20]) | WB [31, 32] (PDF [32, 33]) | 2 / 3 / 2 / 3 | 10 (9 WL) |
| u3 | `3.4` | `eng-u3-3_4` | Getting careers advice | PB [19] (PDF [21]) | WB [32] (PDF [33]) | 3 / 3 / 2 / 3 | 4 (3 WL) |
| u3 | `3.5` | `eng-u3-3_5` | Language review 5 | PB [20] (PDF [22]) | WB [32, 33] (PDF [33, 34]) | 2 / 3 / 2 / 2 | 4 (3 WL) |
| u3 | `3.6` | `eng-u3-3_6` | Job and qualities | PB [21] (PDF [23]) | WB [34, 35] (PDF [35, 36]) | 2 / 3 / 2 / 3 | 15 (15 WL) |
| u3 | `3.7` | `eng-u3-3_7` | Listening: job advertisements | PB [] (PDF []) | WB [35, 36] (PDF [36, 37]) | 2 / 2 / 2 / 3 | 3 (0 WL) |
| u3 | `3.8` | `eng-u3-3_8` | Applying for a job | PB [22] (PDF [24]) | WB [36, 37] (PDF [37, 38]) | 2 / 3 / 2 / 3 | 7 (7 WL) |
| u3 | `3.9` | `eng-u3-3_9` | Intonation and job interview roleplay | PB [] (PDF []) | WB [38, 39] (PDF [39, 40]) | 2 / 3 / 2 / 2 | 6 (3 WL) |
| u3 | `3.10` | `eng-u3-3_10` | Language review 6 | PB [23] (PDF [25]) | WB [39, 40] (PDF [40, 41]) | 2 / 3 / 2 / 2 | 7 (7 WL) |
| u3 | `3.11` | `eng-u3-3_11` | A business letter: layout and vocabulary | PB [24] (PDF [26]) | WB [40] (PDF [41]) | 1 / 2 / 2 / 2 | 5 (2 WL) |
| u3 | `3.12` | `eng-u3-3_12` | Writing a letter of application | PB [24] (PDF [26]) | WB [40] (PDF [41]) | 2 / 2 / 2 / 2 | 5 (4 WL) |
| u4 | `4.1` | `eng-u4-4_1` | Food | PB [25] (PDF [27]) | WB [41] (PDF [42]) | 2 / 2 / 2 / 2 | 13 (12 WL) |
| u4 | `4.2` | `eng-u4-4_2` | Flow charts | PB [] (PDF []) | WB [41, 42] (PDF [42, 43]) | 2 / 2 / 2 / 2 | 3 (0 WL) |
| u4 | `4.3` | `eng-u4-4_3` | Learning to cook | PB [26] (PDF [28]) | WB [43] (PDF [44]) | 1 / 3 / 2 / 2 | 11 (11 WL) |
| u4 | `4.4` | `eng-u4-4_4` | Agriculture in Yemen | PB [27] (PDF [29]) | WB [44] (PDF [45]) | 2 / 2 / 2 / 2 | 12 (12 WL) |
| u4 | `4.5` | `eng-u4-4_5` | Tables and cooking conversations | PB [] (PDF []) | WB [44, 45] (PDF [45, 46]) | 1 / 3 / 2 / 2 | 3 (1 WL) |
| u4 | `4.6` | `eng-u4-4_6` | Language review 7 | PB [28] (PDF [30]) | WB [45, 46] (PDF [46, 47]) | 2 / 3 / 2 / 2 | 3 (2 WL) |
| u4 | `4.7` | `eng-u4-4_7` | Words and more words | PB [29] (PDF [31]) | WB [46, 47] (PDF [47, 48]) | 2 / 3 / 2 / 2 | 10 (10 WL) |
| u4 | `4.8` | `eng-u4-4_8` | Investigating the world around us | PB [30] (PDF [32]) | WB [48] (PDF [49]) | 1 / 2 / 2 / 2 | 11 (11 WL) |
| u4 | `4.9` | `eng-u4-4_9` | Water displacement and Ahmed's experiment | PB [] (PDF []) | WB [49, 50] (PDF [50, 51]) | 2 / 3 / 2 / 2 | 3 (1 WL) |
| u4 | `4.10` | `eng-u4-4_10` | Language review 8 | PB [31] (PDF [33]) | WB [51, 52] (PDF [52, 53]) | 2 / 3 / 2 / 2 | 3 (1 WL) |
| u4 | `4.11` | `eng-u4-4_11` | Frozen peas | PB [32] (PDF [34]) | WB [52, 53] (PDF [53, 54]) | 1 / 3 / 2 / 2 | 10 (9 WL) |
| u4 | `4.12` | `eng-u4-4_12` | Stuffed olives: flow chart and process | PB [32] (PDF [34]) | WB [53, 54] (PDF [54, 55]) | 1 / 2 / 2 / 2 | 5 (2 WL) |
| u5 | `5.1` | `eng-u5-5_1` | Word sets | PB [33] (PDF [35]) | WB [55, 56] (PDF [56, 57]) | 2 / 3 / 2 / 2 | 7 (7 WL) |
| u5 | `5.2` | `eng-u5-5_2` | Possibilities | PB [34] (PDF [36]) | WB [56, 57] (PDF [57, 58]) | 2 / 2 / 2 / 2 | 2 (2 WL) |
| u5 | `5.3` | `eng-u5-5_3` | Listening: Where are they? & The Coronation | PB [] (PDF []) | WB [57, 58] (PDF [58, 59]) | 1 / 2 / 2 / 2 | 3 (1 WL) |
| u5 | `5.4` | `eng-u5-5_4` | Puzzles and riddles | PB [35] (PDF [37]) | WB [59, 60] (PDF [60, 61]) | 2 / 3 / 2 / 2 | 6 (6 WL) |
| u5 | `5.5` | `eng-u5-5_5` | Language review 9 | PB [36] (PDF [38]) | WB [60, 61] (PDF [61, 62]) | 2 / 2 / 2 / 2 | 3 (2 WL) |
| u5 | `5.6` | `eng-u5-5_6` | The mystery of the Mary Celeste | PB [37] (PDF [39]) | WB [61, 62, 63] (PDF [62, 63, 64]) | 1 / 3 / 2 / 2 | 8 (8 WL) |
| u5 | `5.7` | `eng-u5-5_7` | What could have happened? | PB [38] (PDF [40]) | WB [63, 64] (PDF [64, 65]) | 1 / 2 / 2 / 2 | 4 (4 WL) |
| u5 | `5.8` | `eng-u5-5_8` | Listening: Fosdyke's story | PB [] (PDF []) | WB [64, 65] (PDF [65, 66]) | 1 / 2 / 2 / 2 | 2 (2 WL) |
| u5 | `5.9` | `eng-u5-5_9` | Language review 10 | PB [39] (PDF [41]) | WB [65, 66] (PDF [66, 67]) | 2 / 3 / 2 / 2 | 2 (2 WL) |
| u5 | `5.10` | `eng-u5-5_10` | Picture puzzle: What happened in the street? | PB [] (PDF []) | WB [67, 68] (PDF [68, 69]) | 1 / 2 / 2 / 2 | 3 (0 WL) |
| u5 | `5.11` | `eng-u5-5_11` | Tracks in the sand: reading and planning | PB [40] (PDF [42]) | WB [68, 69, 70] (PDF [69, 70, 71]) | 1 / 2 / 2 / 2 | 2 (0 WL) |
| u5 | `5.12` | `eng-u5-5_12` | Tracks in the sand: writing the ending | PB [40] (PDF [42]) | WB [70] (PDF [71]) | 1 / 2 / 2 / 2 | 2 (2 WL) |
| u6 | `6.1` | `eng-u6-6_1` | Emergencies in the news | PB [41] (PDF [43]) | WB [71] (PDF [72]) | 1 / 2 / 2 / 3 | 7 (7 WL) |
| u6 | `6.2` | `eng-u6-6_2` | A lucky escape | PB [42] (PDF [44]) | WB [72, 73] (PDF [73, 74]) | 2 / 3 / 2 / 2 | 5 (0 WL) |
| u6 | `6.3` | `eng-u6-6_3` | Accident at Jebel Kebir | PB [43] (PDF [45]) | WB [73, 74] (PDF [74, 75]) | 1 / 2 / 2 / 3 | 10 (8 WL) |
| u6 | `6.4` | `eng-u6-6_4` | Saving Anwar: listening & vocabulary | PB [44] (PDF [46]) | WB [74, 75] (PDF [75, 76]) | 1 / 4 / 2 / 3 | 5 (1 WL) |
| u6 | `6.5` | `eng-u6-6_5` | Saving Anwar: retelling the story | PB [44] (PDF [46]) | WB [75] (PDF [76]) | 1 / 3 / 2 / 2 | 3 (1 WL) |
| u6 | `6.6` | `eng-u6-6_6` | How a hospital works | PB [45] (PDF [47]) | WB [75] (PDF [76]) | 2 / 2 / 2 / 3 | 10 (10 WL) |
| u6 | `6.7` | `eng-u6-6_7` | Working in public service | PB [46] (PDF [48]) | WB [76] (PDF [77]) | 1 / 3 / 2 / 3 | 8 (5 WL) |
| u6 | `6.8` | `eng-u6-6_8` | Huge changes in Libyan health care: reading | PB [47] (PDF [49]) | WB [] (PDF []) | 1 / 2 / 2 / 3 | 12 (9 WL) |
| u6 | `6.9` | `eng-u6-6_9` | Huge changes in Libyan health care: comprehension & vocabulary | PB [47] (PDF [49]) | WB [77, 78] (PDF [78, 79]) | 1 / 4 / 2 / 2 | 4 (2 WL) |
| u6 | `6.10` | `eng-u6-6_10` | Discovering Yemen | PB [48] (PDF [50]) | WB [78] (PDF [79]) | 1 / 2 / 2 / 2 | 3 (0 WL) |
| u6 | `6.11` | `eng-u6-6_11` | Tourism and the future: reading | PB [49] (PDF [51]) | WB [78, 79] (PDF [79, 80]) | 1 / 3 / 2 / 3 | 4 (1 WL) |
| u6 | `6.12` | `eng-u6-6_12` | Tourism and the future: writing about your future | PB [49] (PDF [51]) | WB [79, 80] (PDF [80, 81]) | 2 / 2 / 2 / 2 | 4 (3 WL) |
| arts | `AR1` | `eng-arts-1` | A difficult choice? | PB [50, 51] (PDF [52, 53]) | WB [81, 82] (PDF [82, 83]) | 1 / 5 / 2 / 3 | 9 (9 WL) |
| arts | `AR2` | `eng-arts-2` | Proverbs and idioms | PB [52] (PDF [54]) | WB [82, 83] (PDF [83, 84]) | 2 / 5 / 2 / 3 | 10 (10 WL) |
| arts | `AR3` | `eng-arts-3` | Telford Hall Episode 1 | PB [53] (PDF [55]) | WB [84, 85] (PDF [85, 86]) | 1 / 3 / 2 / 3 | 8 (8 WL) |
| arts | `AR4` | `eng-arts-4` | A famous play by Shakespeare | PB [54] (PDF [56]) | WB [85, 86, 87] (PDF [86, 87, 88]) | 1 / 5 / 2 / 3 | 10 (10 WL) |
| arts | `AR5` | `eng-arts-5` | Telford Hall Episode 2 | PB [55, 56] (PDF [57, 58]) | WB [87, 88, 89] (PDF [88, 89, 90]) | 2 / 4 / 2 / 3 | 10 (10 WL) |
| arts | `AR6` | `eng-arts-6` | Critics and criticism | PB [57] (PDF [59]) | WB [89, 90] (PDF [90, 91]) | 2 / 5 / 2 / 3 | 10 (10 WL) |
| arts | `AR7` | `eng-arts-7` | Telford Hall Episode 3 | PB [58, 59] (PDF [60, 61]) | WB [90, 91, 92] (PDF [91, 92, 93]) | 2 / 5 / 2 / 3 | 10 (10 WL) |
| arts | `AR8` | `eng-arts-8` | Calligraphy | PB [60] (PDF [62]) | WB [92, 93] (PDF [93, 94]) | 1 / 4 / 2 / 3 | 10 (10 WL) |
| arts | `AR9` | `eng-arts-9` | A poem | PB [61] (PDF [63]) | WB [93, 94] (PDF [94, 95]) | 1 / 3 / 2 / 3 | 10 (10 WL) |
| arts | `AR10` | `eng-arts-10` | Strange happenings | PB [62] (PDF [64]) | WB [94, 95] (PDF [95, 96]) | 2 / 4 / 2 / 3 | 9 (9 WL) |
| science | `SR1` | `eng-sci-1` | Acids and alkalis | PB [63, 64, 65] (PDF [65, 66, 67]) | WB [96, 97] (PDF [97, 98]) | 2 / 3 / 2 / 3 | 10 (10 WL) |
| science | `SR2` | `eng-sci-2` | States of matter | PB [66] (PDF [68]) | WB [97, 98] (PDF [98, 99]) | 1 / 4 / 2 / 3 | 10 (10 WL) |
| science | `SR3` | `eng-sci-3` | Light | PB [67] (PDF [69]) | WB [98, 99] (PDF [99, 100]) | 2 / 3 / 2 / 3 | 10 (10 WL) |
| science | `SR4` | `eng-sci-4` | Sound | PB [68] (PDF [70]) | WB [100] (PDF [101]) | 2 / 3 / 2 / 3 | 10 (10 WL) |
| science | `SR5` | `eng-sci-5` | Arab scientists | PB [69] (PDF [71]) | WB [101] (PDF [102]) | 1 / 3 / 2 / 3 | 10 (10 WL) |
| science | `SR6` | `eng-sci-6` | Vaccinations | PB [70] (PDF [72]) | WB [102, 103] (PDF [103, 104]) | 1 / 4 / 2 / 3 | 10 (10 WL) |
| science | `SR7` | `eng-sci-7` | Experimental procedures | PB [71] (PDF [73]) | WB [103, 104, 105] (PDF [104, 105, 106]) | 1 / 3 / 2 / 3 | 10 (10 WL) |
| science | `SR8` | `eng-sci-8` | Internal combustion engine | PB [72] (PDF [74]) | WB [105, 106, 107] (PDF [106, 107, 108]) | 1 / 4 / 2 / 3 | 21 (21 WL) |
| science | `SR9` | `eng-sci-9` | The Moon | PB [73] (PDF [75]) | WB [107, 108] (PDF [108, 109]) | 2 / 4 / 2 / 3 | 27 (27 WL) |
| science | `SR10` | `eng-sci-10` | Radioactivity | PB [74] (PDF [76]) | WB [109, 110] (PDF [110, 111]) | 2 / 3 / 2 / 3 | 21 (21 WL) |

---

## 4. Verification & Fidelity Notes

- **Golden Rule 2 (Literal Print Preservation)**: Printed textbook typos across Units 1–6, Arts Reader `AR1–AR10`, and Science Reader `SR1–SR10` (e.g., `An orange is around`, `female IIama`, `rotates, or prints`, `Henri Becequerel`, `check you ideas.`, `solau` in `9 E`, `For years later`, `Ahmed met Bob's brother`) are preserved verbatim inside `from_book` blocks and `prompt_literal` strings, accompanied by gentle Arabic clarifications under `edu_note_html` and logged in `REVIEW_NEEDED.md` (Section B rows `1–24`).
- **Golden Rule 7 (Zero Guessing on Missing Cassette Audio & Blurred Bitmap Labels)**: Missing teacher's book cassette dialogues/orders (`1.2`, `1.7`, `2.3`, `2.8`, `3.2 B`, `3.7 C–E`, `3.9 C`, `4.9 E`, `5.3`, `5.8 A`, `6.4 A/B/D`, `6.10 B`) and unreadable 50 ppi blurred scan labels (`1.6`, `5.1 A`, `6.11` surname, `SR8` Diagram A tiny callouts) were never guessed; all determinable text items were solved and missing cassette answers are flagged cleanly in `REVIEW_NEEDED.md`.
- **Teacher Review Artifacts**: Built 92 side-by-side offline review pages (`QA/english/<lesson-id>_review.html`) and 92 per-lesson audit sheets (`QA/english/<lesson-id>.md`), plus 360px mobile browser verification captures.
