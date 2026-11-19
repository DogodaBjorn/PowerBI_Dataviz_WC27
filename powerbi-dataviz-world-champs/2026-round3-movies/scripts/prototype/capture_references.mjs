// scripts/prototype/capture_references.mjs — render each screen of an HTML design comp
// to an exact-size @2x PNG: the pixel-diff targets for the stage-6 fidelity loop
// (px-prototype module). Vendored from Bjorn's hp-world-champs pixel-perfect handoff
// bundle (design_handoff_powerbi/tools/capture_references.mjs, MIT) and generalized.
//
// usage (from the repo root):
//   node scripts/prototype/capture_references.mjs <comp.html> [outDir]
// outDir defaults to project/design-prototypes/reference_screenshots/.
// One PNG per [data-screen-label] element; the label names the file (non-word
// characters become underscores), so keep labels equal to page ids.
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import { resolve, join } from 'path';
import { mkdirSync } from 'fs';

const [file, outDir = 'project/design-prototypes/reference_screenshots'] = process.argv.slice(2);
if (!file) { console.error('usage: node scripts/prototype/capture_references.mjs <comp.html> [outDir]'); process.exit(1); }
mkdirSync(outDir, { recursive: true });
const browser = await chromium.launch();
// deviceScaleFactor 2 = @2x capture (a 1280x720 screen yields a 2560x1440 PNG).
const page = await browser.newPage({ viewport: { width: 1600, height: 1000 }, deviceScaleFactor: 2 });
await page.goto(pathToFileURL(resolve(file)).href);
await page.waitForTimeout(5000); // let the comp runtime + webfonts settle before capturing
let count = 0;
for (const el of await page.locator('[data-screen-label]').all()) {
  const label = await el.getAttribute('data-screen-label');
  const name = label.trim().replace(/\W+/g, '_');
  await el.scrollIntoViewIfNeeded();
  await el.screenshot({ path: join(outDir, name + '.png') });
  console.log(name + '.png');
  count++;
}
if (count === 0) console.error('WARNING: no [data-screen-label] screens found - check the comp conventions');
await browser.close();
