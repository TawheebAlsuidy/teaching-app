#!/usr/bin/env python3
"""Negative & positive tests for validate_book.py (Item 8 strict enforcement)."""
import copy
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate_book  # noqa: E402

VALID_BASE = {
    "schema_version": "3.0.0",
    "subject": "arabic_lit",
    "book_title": "Test",
    "unit": {"id": "u1", "number": 1, "title": "U1"},
    "lesson": {"id": "t1", "code": "1", "title": "L1", "source_refs": []},
    "blocks": [
        {
            "id": "b1",
            "origin": "from_book",
            "type": "paragraph",
            "source": {"book": "PB", "page": 10},
            "dir": "rtl",
            "content": {"text": "نص عربي سليم بالتشكيل."},
        }
    ],
    "activities": [],
    "section_checks": [
        {
            "id": "chk-1",
            "origin": "educational_addition",
            "page_ref": 10,
            "questions": [
                {
                    "id": "q1",
                    "type": "mcq",
                    "stem": "سؤال تجريبي؟",
                    "evidence_block_id": "b1",
                    "options": [
                        {"text": "أ", "is_correct": True, "why_wrong": None},
                        {"text": "ب", "is_correct": False, "why_wrong": "خيار ب يخالف المعنى."},
                    ],
                }
            ],
        }
    ],
    "flashcards": [{"id": "f1", "page_ref": 10, "front": "أ", "back": "ب"}],
}


def run_tests():
    assert validate_book.validate_lesson_data(copy.deepcopy(VALID_BASE)) == []

    # 1. Missing page ref on from_book block
    d1 = copy.deepcopy(VALID_BASE)
    d1["blocks"][0]["source"] = {"book": "PB"}
    assert validate_book.validate_lesson_data(d1), "Should fail on missing page ref"

    # 2. Arabic text with replacement char / mojibake / unexpected Latin
    for bad in ["نص \ufffd مكسور", "نص مشوه ≤”", "نص عربي مع Latin word غير معزول"]:
        d2 = copy.deepcopy(VALID_BASE)
        d2["blocks"][0]["content"]["text"] = bad
        assert validate_book.validate_lesson_data(d2), f"Should fail on bad Arabic: {bad}"

    # Should PASS when Latin is cleanly isolated inside <bdi dir="ltr">...</bdi>
    d2_ok = copy.deepcopy(VALID_BASE)
    d2_ok["blocks"][0]["content"]["text"] = 'يُرمز لها بـ <bdi dir="ltr">pH</bdi> في الكتاب.'
    assert validate_book.validate_lesson_data(d2_ok) == []

    # 3. Quran / verse without verified field
    d3 = copy.deepcopy(VALID_BASE)
    d3["blocks"][0]["type"] = "quote_quran"
    assert validate_book.validate_lesson_data(d3), "Should fail on quote_quran without verified"
    d3v = copy.deepcopy(d3)
    d3v["blocks"][0]["type"] = "verse"
    assert validate_book.validate_lesson_data(d3v), "Should fail on verse without verified"

    # 4. Wrong option missing why_wrong, or != 1 correct option
    d4a = copy.deepcopy(VALID_BASE)
    d4a["section_checks"][0]["questions"][0]["options"][1]["why_wrong"] = ""
    assert validate_book.validate_lesson_data(d4a), "Should fail on missing why_wrong"
    d4b = copy.deepcopy(VALID_BASE)
    d4b["section_checks"][0]["questions"][0]["options"][1]["is_correct"] = True
    assert validate_book.validate_lesson_data(d4b), "Should fail on 2 correct answers"

    # 5. Placeholder / TODO / "..."
    for ph in ["TODO: complete", "وهكذا في بقية الدروس", "..."]:
        d5 = copy.deepcopy(VALID_BASE)
        d5["blocks"][0]["content"]["text"] = ph
        assert validate_book.validate_lesson_data(d5), f"Should fail on placeholder: {ph}"

    print("ALL_VALIDATOR_TESTS_PASSED")


if __name__ == "__main__":
    run_tests()
