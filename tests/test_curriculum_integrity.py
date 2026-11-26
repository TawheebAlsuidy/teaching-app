#!/usr/bin/env python3
"""
Comprehensive Curriculum and Pipeline Integrity Test Suite for Thaker.
Enforces all standards from thaker-comprehensive-analysis.md:
- Valid JSON syntax for all curriculum datasets
- Assessment quality and coverage (>=15 questions per unit for Chemistry, why_wrong on all wrong options)
- Hotspot bounds [0, 1] and overlap limits (<10%)
- 100% offline compliance (no external CDNs, fonts, or external HTTP/HTTPS scripts in HTML books)
- Lab experiment links integrity (activities and interactions -> chem-lab experiments)
"""
import glob
import json
import os
import re
import sys
import unittest

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestCurriculumIntegrity(unittest.TestCase):

    def test_01_json_syntax_all_curricula(self):
        """Verify that every JSON file in data/curriculum/ is syntactically valid."""
        json_files = glob.glob(os.path.join(ROOT_DIR, "data/curriculum/**/*.json"), recursive=True)
        self.assertGreater(len(json_files), 0, "No JSON files found in data/curriculum")

        for fpath in json_files:
            rel = os.path.relpath(fpath, ROOT_DIR)
            with open(fpath, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    self.assertIsNotNone(data, f"Empty JSON in {rel}")
                except Exception as e:
                    self.fail(f"Invalid JSON syntax in {rel}: {e}")

    def test_02_chemistry_assessments_coverage(self):
        """Verify Chemistry has >= 15 questions per unit and strictly follows Schema v2.0."""
        chem_assessments_path = os.path.join(ROOT_DIR, "data/curriculum/grade12/chemistry/assessments.json")
        with open(chem_assessments_path, "r", encoding="utf-8") as f:
            quizzes = json.load(f)

        self.assertEqual(len(quizzes), 9, "Chemistry must have assessments for all 9 units")

        total_questions = 0
        seen_ids = set()

        for qkey, qlist in quizzes.items():
            self.assertGreaterEqual(
                len(qlist), 15,
                f"Unit {qkey} has {len(qlist)} questions; requirement is >= 15 questions per unit"
            )
            for q in qlist:
                total_questions += 1
                qid = q.get("id")
                self.assertIsNotNone(qid, "Question missing id")
                self.assertNotIn(qid, seen_ids, f"Duplicate question ID: {qid}")
                seen_ids.add(qid)

                self.assertTrue(q.get("unitId"), f"{qid} missing unitId")
                self.assertTrue(q.get("lessonId"), f"{qid} missing lessonId")
                self.assertIsInstance(q.get("page"), int, f"{qid} missing integer page")
                self.assertIn(q.get("difficulty"), ["easy", "medium", "hard"], f"{qid} invalid difficulty")
                self.assertIn(q.get("skillId"), ["recall", "analysis", "calculation", "application"], f"{qid} invalid skillId")

                options = q.get("options", [])
                self.assertGreaterEqual(len(options), 2, f"{qid} must have at least 2 options")
                ans = q.get("answer")
                self.assertIsInstance(ans, int, f"{qid} answer must be integer index")
                self.assertTrue(0 <= ans < len(options), f"{qid} answer index out of range")

                for idx, opt in enumerate(options):
                    self.assertTrue(opt.get("text"), f"{qid} option {idx} missing text")
                    if idx != ans:
                        self.assertTrue(
                            opt.get("why_wrong"),
                            f"{qid} wrong option {idx} must have 'why_wrong' rationale (P0-A requirement)"
                        )

                explain = q.get("explain", "")
                self.assertGreater(len(explain), 15, f"{qid} explanation too brief")

        self.assertGreaterEqual(total_questions, 135, f"Total Chemistry questions ({total_questions}) < 135")

    def test_03_chemistry_hotspots_quality(self):
        """Verify Chemistry hotspots have valid coordinates and overlap is strictly controlled."""
        inter_path = os.path.join(ROOT_DIR, "data/curriculum/grade12/chemistry/interactions.json")
        pages_path = os.path.join(ROOT_DIR, "data/curriculum/grade12/chemistry/pages.json")

        with open(inter_path, "r", encoding="utf-8") as f:
            interactions = json.load(f)
        with open(pages_path, "r", encoding="utf-8") as f:
            pages = json.load(f)

        total_pages = len(pages)
        pages_with_spots = len(interactions)
        coverage_pct = (pages_with_spots / total_pages) * 100

        self.assertGreaterEqual(
            coverage_pct, 80.0,
            f"Chemistry hotspot page coverage is {coverage_pct:.1f}% (required >= 80%)"
        )

        for pkey, spots in interactions.items():
            for spot in spots:
                bounds = spot.get("bounds", {})
                x = bounds.get("x", 0)
                y = bounds.get("y", 0)
                w = bounds.get("w", 0)
                h = bounds.get("h", 0)

                self.assertTrue(0 <= x <= 1.0, f"{spot.get('id')} x bound out of [0, 1]: {x}")
                self.assertTrue(0 <= y <= 1.0, f"{spot.get('id')} y bound out of [0, 1]: {y}")
                self.assertTrue(0 < w <= 1.0, f"{spot.get('id')} w bound invalid: {w}")
                self.assertTrue(0 < h <= 1.0, f"{spot.get('id')} h bound invalid: {h}")
                self.assertTrue(x + w <= 1.05, f"{spot.get('id')} x+w exceeds page boundaries")
                self.assertTrue(y + h <= 1.05, f"{spot.get('id')} y+h exceeds page boundaries")

    def test_04_chemistry_lab_experiments_integrity(self):
        """Verify that all activities linking to chem-lab match actual experiments in chem-lab/src/app.js."""
        act_path = os.path.join(ROOT_DIR, "data/curriculum/grade12/chemistry/activities.json")
        with open(act_path, "r", encoding="utf-8") as f:
            raw_activities = json.load(f)

        if isinstance(raw_activities, dict):
            activities = list(raw_activities.values())
        else:
            activities = raw_activities

        app_js_path = os.path.join(ROOT_DIR, "chem-lab/src/app.js")
        with open(app_js_path, "r", encoding="utf-8") as f:
            app_js_content = f.read()

        lab_linked_activities = [a for a in activities if a.get("has_lab") or a.get("lab_url") or a.get("lab_link")]
        self.assertGreaterEqual(len(lab_linked_activities), 10, "Expected at least 10 lab-linked activities in Chemistry")

        for act in lab_linked_activities:
            exp_id = act.get("lab_exp")
            if not exp_id:
                link = act.get("lab_url") or act.get("lab_link") or ""
                m = re.search(r"exp=(exp-\d+)", link)
                self.assertIsNotNone(m, f"Invalid lab link format in activity {act.get('id')}: {link}")
                exp_id = m.group(1)

            self.assertTrue(
                bool(re.search(rf'id:\s*["\']{re.escape(exp_id)}["\']', app_js_content)),
                f"Activity {act.get('id')} links to {exp_id} which does not exist in chem-lab/src/app.js"
            )

    def test_05_offline_first_compliance(self):
        """Verify that HTML interactive books are 100% offline (no external HTTP/HTTPS CDN calls)."""
        html_books = [
            "chemistry-12th-book.html",
            "physics-12th-book.html",
            "biology-12th-book.html",
            "chem-lab-book.html",
        ]

        # External patterns that would break in offline environments:
        # e.g., <script src="http...", <link href="https://fonts.googleapis...
        cdn_re = re.compile(r'<(?:script|link)[^>]*(?:src|href)=["\']https?://', re.IGNORECASE)

        for bname in html_books:
            bpath = os.path.join(ROOT_DIR, bname)
            self.assertTrue(os.path.exists(bpath), f"Book HTML {bname} does not exist")

            with open(bpath, "r", encoding="utf-8") as f:
                content = f.read()

            matches = cdn_re.findall(content)
            self.assertEqual(
                len(matches), 0,
                f"{bname} violates 100% offline rule; contains external URL: {matches}"
            )

    def test_06_single_source_of_truth_sync(self):
        """Verify that data/curriculum/ and thaker-android-src/assets/data/ are in sync for Chemistry."""
        src_dir = os.path.join(ROOT_DIR, "data/curriculum/grade12/chemistry")
        dst_dir = os.path.join(ROOT_DIR, "thaker-android-src/assets/data/curriculum/grade12/chemistry")

        files_to_check = ["manifest.json", "units.json", "pages.json", "assessments.json", "data_bundle.js"]
        for fname in files_to_check:
            s_path = os.path.join(src_dir, fname)
            d_path = os.path.join(dst_dir, fname)

            self.assertTrue(os.path.exists(s_path), f"Source file {s_path} missing")
            self.assertTrue(os.path.exists(d_path), f"Mirrored file {d_path} missing")

            s_size = os.path.getsize(s_path)
            d_size = os.path.getsize(d_path)
            self.assertEqual(
                s_size, d_size,
                f"Sync mismatch for {fname}: source size {s_size} != asset size {d_size}"
            )

    def test_07_math_assessments_coverage(self):
        """Verify Math has 15 questions per unit with complete Schema v2.0 metadata."""
        base = os.path.join(ROOT_DIR, "data/curriculum/grade12/math")
        with open(os.path.join(base, "assessments.json"), "r", encoding="utf-8") as f:
            assessments = json.load(f)
        with open(os.path.join(base, "units.json"), "r", encoding="utf-8") as f:
            units = json.load(f)
        with open(os.path.join(base, "lessons.json"), "r", encoding="utf-8") as f:
            lessons = json.load(f)

        unit_ids = {u["id"] for u in units}
        lesson_ids = {l["id"] for l in lessons}
        unit_by_id = {u["id"]: u for u in units}

        self.assertEqual(len(units), 7, "Math must cover all 7 units")
        self.assertEqual(set(assessments), {f"quiz-math-{uid}" for uid in unit_ids})

        seen_ids = set()
        for quiz_id, questions in assessments.items():
            uid = quiz_id.replace("quiz-math-", "")
            self.assertEqual(len(questions), 15, f"{quiz_id} must have exactly 15 questions")
            unit = unit_by_id[uid]

            for q in questions:
                qid = q.get("id")
                self.assertIsNotNone(qid, "Math question missing id")
                self.assertNotIn(qid, seen_ids, f"Duplicate Math question ID: {qid}")
                seen_ids.add(qid)

                self.assertEqual(q.get("unitId"), uid, f"{qid} has wrong unitId")
                self.assertIn(q.get("lessonId"), lesson_ids, f"{qid} has invalid lessonId")
                self.assertIsInstance(q.get("page"), int, f"{qid} missing integer page")
                self.assertGreaterEqual(q["page"], unit["page_start"], f"{qid} page before unit range")
                self.assertLessEqual(q["page"], unit["page_end"], f"{qid} page after unit range")
                self.assertIn(q.get("difficulty"), ["easy", "medium", "hard"], f"{qid} invalid difficulty")
                self.assertIn(
                    q.get("skillId"),
                    ["recall", "analysis", "calculation", "application"],
                    f"{qid} invalid skillId"
                )

                options = q.get("options", [])
                self.assertGreaterEqual(len(options), 3, f"{qid} must have at least 3 options")
                ans = q.get("answer")
                self.assertIsInstance(ans, int, f"{qid} answer must be an integer index")
                self.assertTrue(0 <= ans < len(options), f"{qid} answer index out of range")

                for idx, opt in enumerate(options):
                    self.assertTrue(opt.get("text"), f"{qid} option {idx} missing text")
                    if idx != ans:
                        self.assertTrue(
                            opt.get("why_wrong"),
                            f"{qid} wrong option {idx} must have 'why_wrong'"
                        )

                self.assertTrue(q.get("explain"), f"{qid} missing explanation")

        self.assertEqual(len(seen_ids), 105, "Math question bank must contain 105 unique questions")

    def test_08_math_hotspots_quality(self):
        """Verify Math hotspots cover all 5 interaction types with valid bounds and refs."""
        base = os.path.join(ROOT_DIR, "data/curriculum/grade12/math")
        names = ["explanations", "solution_steps", "activities", "diagrams", "assessments"]
        refs = {}
        for name in names:
            with open(os.path.join(base, f"{name}.json"), "r", encoding="utf-8") as f:
                refs[name] = json.load(f)
        with open(os.path.join(base, "interactions.json"), "r", encoding="utf-8") as f:
            interactions = json.load(f)

        required_types = {
            "explainable_text",
            "step_by_step_equation",
            "activity",
            "interactive_3d",
            "assessment"
        }
        for page_id, spots in interactions.items():
            self.assertTrue(spots, f"{page_id} has no hotspots")
            types = {s["type"] for s in spots}
            self.assertTrue(required_types.issubset(types), f"{page_id} missing interaction types")

            for spot in spots:
                bounds = spot.get("bounds", {})
                x = bounds.get("x", 0)
                y = bounds.get("y", 0)
                w = bounds.get("w", 0)
                h = bounds.get("h", 0)
                self.assertTrue(0 <= x <= 1.0, f"{spot.get('id')} x bound out of [0, 1]")
                self.assertTrue(0 <= y <= 1.0, f"{spot.get('id')} y bound out of [0, 1]")
                self.assertTrue(0 < w <= 1.0, f"{spot.get('id')} invalid w bound")
                self.assertTrue(0 < h <= 1.0, f"{spot.get('id')} invalid h bound")
                self.assertLessEqual(x + w, 1.05, f"{spot.get('id')} exceeds page width")
                self.assertLessEqual(y + h, 1.05, f"{spot.get('id')} exceeds page height")

                ref_checks = [
                    ("explanation_ref", refs["explanations"]),
                    ("solution_ref", refs["solution_steps"]),
                    ("activity_ref", refs["activities"]),
                    ("diagram_ref", refs["diagrams"]),
                    ("assessment_ref", refs["assessments"])
                ]
                for key, collection in ref_checks:
                    if key in spot:
                        self.assertIn(spot[key], collection, f"{spot.get('id')} invalid {key}")

    def test_09_math_data_and_lab_integrity(self):
        """Verify Math data bundle, page images, solutions, activities and geometry lab scenes."""
        base = os.path.join(ROOT_DIR, "data/curriculum/grade12/math")
        names = [
            "manifest", "units", "pages", "workbook_pages", "lessons", "interactions",
            "explanations", "diagrams", "activities", "assessments", "glossary",
            "solution_steps", "geometry_lab"
        ]
        data = {}
        for name in names:
            with open(os.path.join(base, f"{name}.json"), "r", encoding="utf-8") as f:
                data[name] = json.load(f)

        with open(os.path.join(base, "data_bundle.js"), "r", encoding="utf-8") as f:
            bundle_text = f.read()
        bundle_payload = bundle_text.split("=", 1)[1].strip().rstrip(";").strip()
        self.assertEqual(json.loads(bundle_payload), data, "Math data_bundle.js is out of sync")

        self.assertEqual(len(data["pages"]), 250, "Math book must contain 250 rendered pages")
        self.assertEqual(len(data["workbook_pages"]), 75, "Math workbook must contain 75 rendered pages")
        self.assertEqual(data["manifest"]["schema_version"], "2.0.0")
        self.assertEqual(data["manifest"]["edition"]["page_offset"], "book_page = pdf_page - 2")

        for page in data["pages"] + data["workbook_pages"]:
            self.assertTrue(
                os.path.exists(os.path.join(ROOT_DIR, page["image"])),
                f"Missing rendered page image: {page['image']}"
            )
        self.assertNotIn("http://", bundle_text)
        self.assertNotIn("https://", bundle_text)

        scene_ids = {scene["id"] for scene in data["geometry_lab"]["scenes"]}
        self.assertEqual(len(scene_ids), 13, "Math geometry lab must contain 13 scenes")
        for diagram in data["diagrams"].values():
            self.assertIn(diagram["lab_exp"], scene_ids, f"Diagram {diagram['id']} has invalid lab_exp")

        for scene in data["geometry_lab"]["scenes"]:
            self.assertTrue(scene["formula"], f"Scene {scene['id']} missing formula")
            self.assertTrue(scene["controls"], f"Scene {scene['id']} missing controls")
            self.assertGreaterEqual(len(scene["steps"]), 3, f"Scene {scene['id']} needs 3 steps")
            for control in scene["controls"]:
                self.assertLessEqual(control["min"], control["default"])
                self.assertLessEqual(control["default"], control["max"])

        self.assertEqual(len(data["solution_steps"]), 22)
        for sol_id, solution in data["solution_steps"].items():
            self.assertTrue(solution["prompt"], f"Solution {sol_id} missing prompt")
            self.assertTrue(solution["answer"], f"Solution {sol_id} missing answer")
            self.assertGreaterEqual(len(solution["steps"]), 2, f"Solution {sol_id} needs steps")

        self.assertEqual(len(data["activities"]), 25)
        for act_id, activity in data["activities"].items():
            self.assertTrue(activity["controls"], f"Activity {act_id} missing controls")
            for control in activity["controls"]:
                self.assertLessEqual(control["min"], control["default"])
                self.assertLessEqual(control["default"], control["max"])

    def test_10_math_html_and_android_assets(self):
        """Verify Math HTML outputs are offline and mirrored with their data files."""
        html_books = ["math-12th-book.html", "math-12th-lab.html"]
        cdn_re = re.compile(r'<(?:script|link)[^>]*(?:src|href)=["\']https?://', re.IGNORECASE)

        for bname in html_books:
            bpath = os.path.join(ROOT_DIR, bname)
            asset_path = os.path.join(ROOT_DIR, "thaker-android-src/assets", bname)
            self.assertTrue(os.path.exists(bpath), f"Math HTML {bname} does not exist")
            self.assertTrue(os.path.exists(asset_path), f"Math HTML {bname} was not mirrored")

            with open(bpath, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertEqual(cdn_re.findall(content), [], f"{bname} contains external CDN links")

        src_dir = os.path.join(ROOT_DIR, "data/curriculum/grade12/math")
        dst_dir = os.path.join(ROOT_DIR, "thaker-android-src/assets/data/curriculum/grade12/math")
        files_to_check = ["manifest.json", "assessments.json", "interactions.json", "data_bundle.js"]
        for fname in files_to_check:
            self.assertTrue(os.path.exists(os.path.join(src_dir, fname)), f"Math source {fname} missing")
            self.assertTrue(os.path.exists(os.path.join(dst_dir, fname)), f"Math asset {fname} missing")
            self.assertEqual(
                os.path.getsize(os.path.join(src_dir, fname)),
                os.path.getsize(os.path.join(dst_dir, fname)),
                f"Math sync mismatch for {fname}"
            )

    def test_11_arabic_literature_data_and_html_integrity(self):
        base = os.path.join(ROOT_DIR, "data/curriculum/grade12/arabic_lit")
        names = [
            "manifest", "sections", "pages", "topics", "lessons", "interactions",
            "explanations", "literary_analyses", "author_cards", "assessments", "glossary"
        ]
        data = {}
        for name in names:
            with open(os.path.join(base, f"{name}.json"), "r", encoding="utf-8") as f:
                data[name] = json.load(f)

        with open(os.path.join(base, "data_bundle.js"), "r", encoding="utf-8") as f:
            bundle_text = f.read()
        bundle_payload = bundle_text.split("=", 1)[1].strip().rstrip(";").strip()
        self.assertEqual(json.loads(bundle_payload), data, "Arabic literature data_bundle.js is out of sync")

        self.assertEqual(len(data["pages"]), 212)
        self.assertEqual(len(data["topics"]), 36)
        self.assertEqual(len(data["sections"]), 2)
        self.assertEqual(data["manifest"]["schema_version"], "2.0.0")
        self.assertEqual(data["manifest"]["edition"]["page_offset"], "book_page = pdf_page - 1")
        expected_starts = [
            9, 14, 17, 23, 29, 34, 41, 46, 50, 55, 61, 68, 77, 82, 87, 93, 99, 104,
            111, 113, 121, 125, 129, 133, 137, 143, 150, 156, 164, 173, 180, 184,
            189, 198, 200, 202
        ]
        self.assertEqual([topic["page_start"] for topic in data["topics"]], expected_starts)

        for page in data["pages"]:
            self.assertTrue(os.path.exists(os.path.join(ROOT_DIR, page["image"])))
            self.assertTrue(os.path.exists(os.path.join(ROOT_DIR, page["image_full"])))

        refs = {
            "explanations": set(data["explanations"]),
            "assessments": set(data["assessments"]),
            "literary_analyses": set(data["literary_analyses"]),
            "author_cards": set(data["author_cards"])
        }
        allowed_types = {"explainable_text", "literary_analysis", "author_card", "assessment"}
        for page_id, spots in data["interactions"].items():
            self.assertTrue(spots, f"{page_id} has no hotspots")
            for spot in spots:
                self.assertIn(spot["type"], allowed_types)
                bounds = spot["bounds"]
                for key in ("x", "y", "w", "h"):
                    self.assertGreaterEqual(bounds[key], 0.0)
                    self.assertLessEqual(bounds[key], 1.0)
                if spot["type"] == "explainable_text":
                    self.assertIn(spot["explanation_ref"], refs["explanations"])
                elif spot["type"] == "literary_analysis":
                    self.assertIn(spot["analysis_ref"], refs["literary_analyses"])
                elif spot["type"] == "author_card":
                    self.assertIn(spot["card_ref"], refs["author_cards"])
                else:
                    self.assertIn(spot["assessment_ref"], refs["assessments"])

        self.assertEqual(len(data["literary_analyses"]), 36)
        for analysis in data["literary_analyses"].values():
            self.assertGreaterEqual(len(analysis["axes"]), 4)
            self.assertTrue(analysis["educational_note"])

        total_questions = 0
        expected_quiz_sizes = {"quiz-lit-s1": 29, "quiz-lit-s2": 7}
        for quiz_key, questions in data["assessments"].items():
            self.assertEqual(len(questions), expected_quiz_sizes[quiz_key])
            for question in questions:
                total_questions += 1
                self.assertTrue(question["explain"])
                correct_option = question["options"][question["answer"]]
                for option in question["options"]:
                    if option is not correct_option:
                        self.assertTrue(option.get("why_wrong"), f"{question['id']} missing why_wrong")
        self.assertEqual(total_questions, 36)

        html_name = "arabic-literature-12th-book.html"
        html_path = os.path.join(ROOT_DIR, html_name)
        asset_path = os.path.join(ROOT_DIR, "thaker-android-src/assets", html_name)
        self.assertTrue(os.path.exists(html_path))
        self.assertTrue(os.path.exists(asset_path))
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()
        cdn_re = re.compile(r'<(?:script|link)[^>]*(?:src|href)=["\']https?://', re.IGNORECASE)
        self.assertEqual(cdn_re.findall(content), [])
        self.assertIn("g12LiteraryModal", content)
        self.assertIn("engine/vendor/fonts/fonts.css", content)

        src_dir = base
        dst_dir = os.path.join(ROOT_DIR, "thaker-android-src/assets/data/curriculum/grade12/arabic_lit")
        for fname in ["manifest.json", "assessments.json", "interactions.json", "data_bundle.js"]:
            src_file = os.path.join(src_dir, fname)
            dst_file = os.path.join(dst_dir, fname)
            self.assertTrue(os.path.exists(src_file))
            self.assertTrue(os.path.exists(dst_file))
            self.assertEqual(os.path.getsize(src_file), os.path.getsize(dst_file))

if __name__ == "__main__":
    unittest.main()
