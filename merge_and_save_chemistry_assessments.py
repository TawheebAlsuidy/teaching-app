#!/usr/bin/env python3
"""
Merge and validate the 135 questions for Grade 12 Chemistry,
update data/curriculum/grade12/chemistry/assessments.json,
re-generate data_bundle.js, and sync to thaker-android-src.
"""
import json
import os
import shutil

from chemistry_assessments_part1 import get_unit_1, get_unit_2, get_unit_3, get_unit_4
from chemistry_assessments_part2 import get_unit_5, get_unit_6, get_unit_7, get_unit_8, get_unit_9

DATA_DIR = "data/curriculum/grade12/chemistry"
ANDROID_DATA_DIR = "thaker-android-src/assets/data/curriculum/grade12/chemistry"

def main():
    quizzes = {
        "quiz-chem-u1": get_unit_1(),
        "quiz-chem-u2": get_unit_2(),
        "quiz-chem-u3": get_unit_3(),
        "quiz-chem-u4": get_unit_4(),
        "quiz-chem-u5": get_unit_5(),
        "quiz-chem-u6": get_unit_6(),
        "quiz-chem-u7": get_unit_7(),
        "quiz-chem-u8": get_unit_8(),
        "quiz-chem-u9": get_unit_9(),
    }

    total_q = 0
    seen_ids = set()

    for qkey, qlist in quizzes.items():
        assert len(qlist) >= 15, f"{qkey} has {len(qlist)} questions; required >= 15"
        for q in qlist:
            total_q += 1
            qid = q["id"]
            assert qid not in seen_ids, f"Duplicate question ID: {qid}"
            seen_ids.add(qid)

            assert "unitId" in q and q["unitId"], f"{qid} missing unitId"
            assert "lessonId" in q and q["lessonId"], f"{qid} missing lessonId"
            assert "page" in q and isinstance(q["page"], int), f"{qid} missing valid page"
            assert "difficulty" in q, f"{qid} missing difficulty"
            assert "skillId" in q, f"{qid} missing skillId"
            assert "options" in q and len(q["options"]) >= 2, f"{qid} options invalid"
            assert "answer" in q and 0 <= q["answer"] < len(q["options"]), f"{qid} answer index out of bounds"
            assert "explain" in q and len(q["explain"]) > 10, f"{qid} explain too short"

            for idx, opt in enumerate(q["options"]):
                assert "text" in opt and opt["text"], f"{qid} option {idx} missing text"
                if idx != q["answer"]:
                    assert "why_wrong" in opt and opt["why_wrong"], f"{qid} wrong option {idx} missing why_wrong"

    print(f"Validation successful! Total questions: {total_q} across {len(quizzes)} units.")

    # 1. Save assessments.json
    assessments_path = os.path.join(DATA_DIR, "assessments.json")
    with open(assessments_path, "w", encoding="utf-8") as f:
        json.dump(quizzes, f, ensure_ascii=False, indent=2)
    print(f"Wrote {assessments_path}")

    # 2. Rebuild data_bundle.js
    bundle_files = [
        ("manifest", "manifest.json"),
        ("units", "units.json"),
        ("pages", "pages.json"),
        ("lessons", "lessons.json"),
        ("glossary", "glossary.json"),
        ("explanations", "explanations.json"),
        ("diagrams", "diagrams.json"),
        ("activities", "activities.json"),
        ("assessments", "assessments.json"),
        ("interactions", "interactions.json"),
    ]
    bundle_data = {}
    for key, fname in bundle_files:
        fpath = os.path.join(DATA_DIR, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                bundle_data[key] = json.load(f)
        else:
            print(f"Warning: {fpath} does not exist!")

    bundle_js_path = os.path.join(DATA_DIR, "data_bundle.js")
    with open(bundle_js_path, "w", encoding="utf-8") as f:
        f.write("window.THAKER_CURRICULUM_G12_CHEMISTRY = ")
        json.dump(bundle_data, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Wrote {bundle_js_path}")

    # 3. Sync to android assets
    os.makedirs(ANDROID_DATA_DIR, exist_ok=True)
    shutil.copy2(assessments_path, os.path.join(ANDROID_DATA_DIR, "assessments.json"))
    shutil.copy2(bundle_js_path, os.path.join(ANDROID_DATA_DIR, "data_bundle.js"))
    print(f"Synced assessments.json and data_bundle.js to {ANDROID_DATA_DIR}")

if __name__ == "__main__":
    main()
