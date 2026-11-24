#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compiler for Standalone Physics & Biology Interactive Textbooks
Generates:
1. physics-12th-book.html
2. biology-12th-book.html
"""
import os
import json

BASE_DIR = "/media/tawheeb/New Volume2/ذاكر/teaching-app"

def build_book(subject_key, title_main, title_sub, primary_color, accent_color, bundle_js_var, bundle_file, out_filename, extra_sims_js):
    print(f"[*] Building interactive HTML for {subject_key} -> {out_filename}...")
    
    # Read the base template from thaker-interactive-book.html
    with open(f"{BASE_DIR}/thaker-interactive-book.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Read data bundle
    with open(f"{BASE_DIR}/{bundle_file}", "r", encoding="utf-8") as f:
        bundle_content = f.read()

    # Cut out the old data bundle (between lines 504 and 1984)
    start_tag = "window.THAKER_CURRICULUM_P2 = {"
    end_tag = "const LESSONS = window.THAKER_CURRICULUM_P2?.lessons || [];"

    idx_start = html.find(start_tag)
    idx_end = html.find(end_tag)

    if idx_start == -1 or idx_end == -1:
        raise ValueError("Could not find curriculum boundary tags in template")

    # Construct the replaced JS data header
    new_data_header = f"""
{bundle_content}

const CURR_DATA = {bundle_js_var};
const PAGES = CURR_DATA?.pages || [];
const INTERACTIONS = CURR_DATA?.interactions || {{}};
const EXPLANATIONS = CURR_DATA?.explanations || {{}};
const DIAGRAMS = CURR_DATA?.diagrams || {{}};
const ASSESSMENTS = CURR_DATA?.assessments || {{}};
const GLOSSARY = CURR_DATA?.glossary || {{}};
const LESSONS = CURR_DATA?.lessons || [];
const UNITS = CURR_DATA?.units || [];
"""

    # Replace the data block
    html_new = html[:idx_start] + new_data_header + html[idx_end + len(end_tag):]

    # Customize titles and colors
    html_new = html_new.replace("<title>ذاكر — كتاب العلوم التفاعلي الذكي (الصف التاسع - الجزء الثاني)</title>", f"<title>{title_main}</title>")
    html_new = html_new.replace('<span class="title-main">كتاب العلوم التفاعلي الذكي</span>', f'<span class="title-main">{title_main}</span>')
    html_new = html_new.replace('<span class="title-sub" id="currentSectionTitle">الصف التاسع الأساسي · الجزء الثاني</span>', f'<span class="title-sub" id="currentSectionTitle">{title_sub}</span>')
    html_new = html_new.replace("فهرس وحدات الجزء الثاني", f"فهرس وحدات {title_sub}")

    # Primary & accent color adjustments
    if primary_color != "#00a859":
        html_new = html_new.replace("--primary: #00a859;", f"--primary: {primary_color};")
        html_new = html_new.replace("--primary-dark: #008f4c;", f"--primary-dark: {primary_color};")
        html_new = html_new.replace("border-color: #00a859;", f"border-color: {primary_color};")

    # Update renderToc logic to handle the new UNITS/LESSONS structure
    toc_old = """function renderToc() {
  const container = document.getElementById('tocListContainer');
  container.innerHTML = LESSONS.map(u => `
    <div style="font-size:12px; font-weight:800; color:var(--primary); margin-top:8px;">الوحدة ${u.unit_num}: ${u.unit_title}</div>
    ${u.lessons.map(l => `
      <div class="toc-item" onclick="jumpToBookPage(${l.p_start})">
        <span>${l.title}</span>
        <span style="opacity:0.6;">ص ${l.p_start}</span>
      </div>
    `).join('')}
  `).join('');
}"""

    toc_new = """function renderToc() {
  const container = document.getElementById('tocListContainer');
  if (!container) return;
  if (UNITS && UNITS.length > 0) {
    container.innerHTML = UNITS.map(u => {
      const uLessons = LESSONS.filter(l => l.unitId === u.id);
      return `
        <div style="font-size:12px; font-weight:800; color:var(--primary); margin-top:10px; padding:4px 8px; background:rgba(0,168,89,0.08); border-radius:6px;">
          ${u.title}
        </div>
        ${uLessons.map(l => `
          <div class="toc-item" onclick="jumpToBookPage(${l.pages[0]})">
            <span>${l.title}</span>
            <span style="opacity:0.75; font-size:11px;">ص ${l.pages[0]}</span>
          </div>
        `).join('')}
      `;
    }).join('');
  } else {
    container.innerHTML = LESSONS.map(l => `
      <div class="toc-item" onclick="jumpToBookPage(${l.pages ? l.pages[0] : 1})">
        <span>${l.title}</span>
      </div>
    `).join('');
  }
}"""
    html_new = html_new.replace(toc_old, toc_new)

    # Inject 3D Simulation extensions before </body>
    sim_script = f"""
<script>
// --- Subject Specific 3D Labs & Simulations ({subject_key}) ---
{extra_sims_js}
</script>
</body>
"""
    html_new = html_new.replace("</body>", sim_script)

    # Save to workspace root
    out_path_root = f"{BASE_DIR}/{out_filename}"
    with open(out_path_root, "w", encoding="utf-8") as f:
        f.write(html_new)

    # Mirror to android assets
    out_path_android = f"{BASE_DIR}/thaker-android-src/assets/{out_filename}"
    with open(out_path_android, "w", encoding="utf-8") as f:
        f.write(html_new)

    print(f"[✓] {out_filename} generated and mirrored successfully ({len(html_new)//1024} KB)!")

# Extra 3D Simulations for Physics
extra_physics_sims = """
function initSubjectSimulations() {
  console.log("Initializing Physics 3D Simulation Engine...");
}
window.addEventListener('DOMContentLoaded', initSubjectSimulations);
"""

# Extra 3D Simulations for Biology
extra_biology_sims = """
function initSubjectSimulations() {
  console.log("Initializing Biology 3D Anatomical Engine...");
}
window.addEventListener('DOMContentLoaded', initSubjectSimulations);
"""

def main():
    # 1. Physics Book
    build_book(
        subject_key="physics",
        title_main="كتاب ومعمل الفيزياء التفاعلي الذكي",
        title_sub="الصف الثالث الثانوي · القسم العلمي",
        primary_color="#0284c7",
        accent_color="#38bdf8",
        bundle_js_var="window.THAKER_CURRICULUM_G12_PHYSICS",
        bundle_file="data/curriculum/grade12/physics/data_bundle.js",
        out_filename="physics-12th-book.html",
        extra_sims_js=extra_physics_sims
    )

    # 2. Biology Book
    build_book(
        subject_key="biology",
        title_main="كتاب ومعمل الأحياء التفاعلي الذكي",
        title_sub="الصف الثالث الثانوي · القسم العلمي",
        primary_color="#00a859",
        accent_color="#10b981",
        bundle_js_var="window.THAKER_CURRICULUM_G12_BIOLOGY",
        bundle_file="data/curriculum/grade12/biology/data_bundle.js",
        out_filename="biology-12th-book.html",
        extra_sims_js=extra_biology_sims
    )

if __name__ == "__main__":
    main()
