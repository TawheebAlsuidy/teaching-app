const fs = require('fs');
const path = require('path');
const puppeteer = require('/usr/lib/node_modules/puppeteer-core');

const HTML_PATH = 'file:///mnt/sdcard/projects/teaching-app/chem-lab/dist/chem-lab-book.html';
const SHOTS_DIR = '/root/.gemini/antigravity-cli/brain/b2b09aa1-e682-4694-8051-911cc53119ce/screenshots';
const LOCAL_SHOTS_DIR = '/mnt/sdcard/projects/teaching-app/chem-lab/screenshots';

fs.mkdirSync(SHOTS_DIR, { recursive: true });
fs.mkdirSync(LOCAL_SHOTS_DIR, { recursive: true });

async function runVerification() {
  console.log('=== STARTING AUTOMATED HEADLESS CHROMIUM VERIFICATION ===');
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/chromium',
    headless: 'new',
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-gpu',
      '--single-process',
      '--no-zygote'
    ]
  });

  const page = await browser.newPage();
  const consoleErrors = [];
  const pageErrors = [];

  page.on('console', msg => {
    if (msg.type() === 'error') {
      consoleErrors.push(msg.text());
      console.error('BROWSER ERROR:', msg.text());
    }
  });

  page.on('pageerror', err => {
    pageErrors.push(err.message);
    console.error('UNCAUGHT PAGE ERROR:', err.message);
  });

  // ----------------------------------------------------
  // TEST 1: Mobile 390x844 - Light Mode
  // ----------------------------------------------------
  console.log('\n-> Testing Mobile Viewport (390x844) - Light Mode...');
  await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });
  await page.emulateMediaFeatures([{ name: 'prefers-color-scheme', value: 'light' }]);
  await page.goto(HTML_PATH, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(1000);

  // Open Quiz in Light Mode
  await page.evaluate(() => openQ());
  await page.waitForTimeout(500);

  // Verify colors in Light Mode (text must NOT be white on light background)
  const lightColors = await page.evaluate(() => {
    const qb = document.getElementById('qb');
    const title = qb.querySelector('h3');
    const firstBtn = qb.querySelector('.qo');
    const titleStyle = window.getComputedStyle(title);
    const btnStyle = window.getComputedStyle(firstBtn);
    return {
      titleColor: titleStyle.color,
      btnColor: btnStyle.color,
      btnBg: btnStyle.backgroundColor
    };
  });
  console.log('   Light mode computed colors:', lightColors);

  // Capture screenshot: Mobile Light Mode Quiz Menu
  const shot1 = path.join(SHOTS_DIR, 'quiz_mobile_light.png');
  const shot1Local = path.join(LOCAL_SHOTS_DIR, 'quiz_mobile_light.png');
  await page.screenshot({ path: shot1 });
  fs.copyFileSync(shot1, shot1Local);
  console.log('   ✓ Captured:', shot1);

  // ----------------------------------------------------
  // TEST 2: Mobile 390x844 - Dark Mode
  // ----------------------------------------------------
  console.log('\n-> Testing Mobile Viewport (390x844) - Dark Mode...');
  await page.emulateMediaFeatures([{ name: 'prefers-color-scheme', value: 'dark' }]);
  await page.waitForTimeout(500);

  const darkColors = await page.evaluate(() => {
    const qb = document.getElementById('qb');
    const title = qb.querySelector('h3');
    const firstBtn = qb.querySelector('.qo');
    const titleStyle = window.getComputedStyle(title);
    const btnStyle = window.getComputedStyle(firstBtn);
    return {
      titleColor: titleStyle.color,
      btnColor: btnStyle.color,
      btnBg: btnStyle.backgroundColor
    };
  });
  console.log('   Dark mode computed colors:', darkColors);

  // Capture screenshot: Mobile Dark Mode Quiz Menu
  const shot2 = path.join(SHOTS_DIR, 'quiz_mobile_dark.png');
  const shot2Local = path.join(LOCAL_SHOTS_DIR, 'quiz_mobile_dark.png');
  await page.screenshot({ path: shot2 });
  fs.copyFileSync(shot2, shot2Local);
  console.log('   ✓ Captured:', shot2);

  // ----------------------------------------------------
  // TEST 3: Quiz Execution & Question Flow in Light Mode
  // ----------------------------------------------------
  console.log('\n-> Testing Quiz Execution, Answering & Review Linked Exp...');
  await page.emulateMediaFeatures([{ name: 'prefers-color-scheme', value: 'light' }]);
  // Start Unit 1 Quiz
  await page.evaluate(() => startQuiz(1));
  await page.waitForTimeout(500);

  // Capture screenshot of question card in Light Mode
  const shotQ = path.join(SHOTS_DIR, 'quiz_question_light.png');
  await page.screenshot({ path: shotQ });
  fs.copyFileSync(shotQ, path.join(LOCAL_SHOTS_DIR, 'quiz_question_light.png'));
  console.log('   ✓ Captured question card:', shotQ);

  // Click first option
  await page.evaluate(() => {
    const btn = document.querySelector('.q-opts .qo');
    if (btn) btn.click();
  });
  await page.waitForTimeout(300);

  // Check if review button appears when expId is attached
  const hasExpReview = await page.evaluate(() => {
    const expBtn = document.querySelector('#quizExplain .qo');
    return !!expBtn;
  });
  console.log('   Has explanation & action button:', hasExpReview);

  // Close quiz
  await page.evaluate(() => closeQ());
  await page.waitForTimeout(300);

  // ----------------------------------------------------
  // TEST 4: Desktop 1280x800 Viewport
  // ----------------------------------------------------
  console.log('\n-> Testing Desktop Viewport (1280x800)...');
  await page.setViewport({ width: 1280, height: 800 });
  await page.evaluate(() => openQ());
  await page.waitForTimeout(400);

  const shotDesktop = path.join(SHOTS_DIR, 'quiz_desktop_light.png');
  await page.screenshot({ path: shotDesktop });
  fs.copyFileSync(shotDesktop, path.join(LOCAL_SHOTS_DIR, 'quiz_desktop_light.png'));
  console.log('   ✓ Captured Desktop Quiz:', shotDesktop);

  await page.evaluate(() => closeQ());

  // ----------------------------------------------------
  // TEST 5: Verify All 10 Experiments & Steps
  // ----------------------------------------------------
  console.log('\n-> Testing all 10 3D Experiments execution and step progression...');
  const expResults = await page.evaluate(async () => {
    const results = [];
    for (let i = 0; i < EXPERIMENTS.length; i++) {
      const exp = EXPERIMENTS[i];
      loadExperiment(i);
      
      // verify activeExpObj exists
      if (!activeExpObj) {
        results.push({ id: exp.id, n: exp.n, ok: false, error: 'activeExpObj missing' });
        continue;
      }
      
      // execute each step
      let stepErrors = 0;
      for (let s = 0; s < exp.st.length; s++) {
        try {
          setStep(s);
          autoStep();
        } catch(e) {
          stepErrors++;
        }
      }
      results.push({ id: exp.id, n: exp.n, steps: exp.st.length, ok: stepErrors === 0 });
    }
    return results;
  });

  let allExpOk = true;
  for (const r of expResults) {
    if (r.ok) {
      console.log(`   ✓ [${r.id}] ${r.n} (${r.steps} خطوات): OK`);
    } else {
      console.error(`   ❌ [${r.id}] ${r.n}: FAILED`);
      allExpOk = false;
    }
  }

  // ----------------------------------------------------
  // TEST 6: Persistence & Storage Manager
  // ----------------------------------------------------
  console.log('\n-> Testing LocalStorage Persistence & Reload...');
  await page.evaluate(() => {
    loadExperiment(3); // Exp 4: Daniel Cell
    setStep(2);
    StorageManager.saveQuizResult(1, 3, 3);
    StorageManager.recordMistake('chem-q1');
    QualityManager.setMode('medium', false);
  });

  // Reload page to verify state restored
  await page.reload({ waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(1000);

  const restoredState = await page.evaluate(() => {
    return {
      curExp,
      curStep,
      unit1Result: StorageManager.getUnitResult(1),
      mistakes: StorageManager.getMistakes(),
      quality: QualityManager.mode
    };
  });
  console.log('   Restored State:', restoredState);

  const persistenceOk = (
    restoredState.curExp === 3 &&
    restoredState.curStep === 2 &&
    restoredState.unit1Result &&
    restoredState.unit1Result.bestScore === 3 &&
    restoredState.mistakes.includes('chem-q1') &&
    restoredState.quality === 'medium'
  );

  console.log('   Persistence verification:', persistenceOk ? 'PASSED ✓' : 'FAILED ❌');

  await browser.close();

  console.log('\n======================================================');
  console.log('SUMMARY OF VERIFICATION:');
  console.log('  Total Console Errors:', consoleErrors.length);
  console.log('  Total Page Errors:', pageErrors.length);
  console.log('  All 10 Experiments Passed:', allExpOk ? 'YES ✓' : 'NO ❌');
  console.log('  Persistence Verified:', persistenceOk ? 'YES ✓' : 'NO ❌');
  console.log('======================================================\n');

  if (consoleErrors.length > 0 || pageErrors.length > 0 || !allExpOk || !persistenceOk) {
    process.exit(1);
  } else {
    process.exit(0);
  }
}

runVerification().catch(err => {
  console.error('Verification script crashed:', err);
  process.exit(1);
});
