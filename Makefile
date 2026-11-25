# ==============================================================================
# Makefile — Unified Build System for Thaker National Educational Platform
# Follows thaker-comprehensive-analysis.md (P0-B & P0-D)
# ==============================================================================

.PHONY: all data books sync-assets test apk clean help

help:
	@echo "ذاكر — نظام البناء الموحد (Unified Build Pipeline)"
	@echo "الاستخدام:"
	@echo "  make all         بناء كل شيء (بيانات + كتب + مزامنة الأصول + اختبارات)"
	@echo "  make data        توليد والتحقق من حزم بيانات المنهج (JSON & data_bundle.js)"
	@echo "  make books       بناء وتحديث الكتب التفاعلية HTML ومعمل الكيمياء 3D"
	@echo "  make sync-assets مزامنة المصدر الموحد للبيانات إلى أصول الأندرويد"
	@echo "  make test        تشغيل جناح الاختبارات الآلية الشاملة"
	@echo "  make apk         بناء حزمة أندرويد النهائية Thaker.apk"
	@echo "  make clean       تنظيف الملفات المؤقتة وسجلات البناء"

all: data books sync-assets test
	@echo "=================================================="
	@echo "✨ اكتمل بناء واختبار جميع مكونات منصة ذاكر بنجاح!"
	@echo "=================================================="

data:
	@echo "[*] Generating curriculum data packs..."
	python3 merge_and_save_chemistry_assessments.py

books:
	@echo "[*] Building interactive HTML books..."
	python3 build_interactive_books_html.py
	@echo "[*] Building 3D Chemistry Lab standalone bundle..."
	python3 chem-lab/build.py
	cp -f chem-lab/dist/chem-lab-book.html chem-lab-book.html
	cp -f chem-lab/dist/chem-lab-book.html thaker-android-src/assets/chem-lab-book.html

sync-assets:
	@echo "[*] Synchronizing Single Source of Truth to Android Assets..."
	python3 sync_assets.py

test:
	@echo "[*] Running comprehensive integrity test suite..."
	python3 -m unittest tests/test_curriculum_integrity.py

apk: sync-assets
	@echo "[*] Building Android APK..."
	python3 build_apk.py

clean:
	@echo "[*] Cleaning build artifacts..."
	rm -rf __pycache__ */__pycache__ */*/__pycache__
	rm -f *.pyc */*.pyc
