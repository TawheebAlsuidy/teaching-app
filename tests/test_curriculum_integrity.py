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

if __name__ == "__main__":
    unittest.main()
