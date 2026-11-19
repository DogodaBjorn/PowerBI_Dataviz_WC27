// Capture and measure the opzet comp (px-prototype discipline, project-local variant).
//
// usage (from the repo root):
//   node project/tools/opzet_capture.mjs [scale] [outDir]
// scale: deviceScaleFactor (2 = reference PNGs for the fidelity loop, 1 = quick look)
// outDir: defaults to project/design-prototypes/reference_screenshots
//
// Why a project-local tool: scripts/prototype/extract_layout.mjs measures in a 1600x1200
// viewport, smaller than this project's 1920x1080 canvas, and scripts/ is framework code
// (read-only in a project). This tool measures every [data-visual] slot in a 1920-wide
// viewport and checks it against project/design-prototypes/opzet-layout.json (+-2 px),
// writing project/design-prototypes/opzet-layout-check.json.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright'); // the machine's Playwright (pre-installed) or scripts/prototype's pinned copy
import { pathToFileURL } from 'url';
import { resolve } from 'path';
import { mkdirSync, readFileSync, writeFileSync } from 'fs';

const scale = Number(process.argv[2] || 2);
const outDir = process.argv[3] || 'project/design-prototypes/reference_screenshots';
const comp = 'project/design-prototypes/opzet-goodnight-inn.html';
const layout = JSON.parse(readFileSync('project/design-prototypes/opzet-layout.json', 'utf-8'));
mkdirSync(outDir, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: scale });
await page.goto(pathToFileURL(resolve(comp)).href);
await page.waitForTimeout(1500);
const measured = await page.evaluate(() => {
  const out = {};
  for (const s of document.querySelectorAll('[data-screen-label]')) {
    const sr = s.getBoundingClientRect(); const els = {};
    for (const v of s.querySelectorAll('[data-visual]')) { const r = v.getBoundingClientRect(); els[v.dataset.visual] = { x: r.x - sr.x, y: r.y - sr.y, w: r.width, h: r.height, overflowX: v.scrollWidth > v.clientWidth + 1, overflowY: v.scrollHeight > v.clientHeight + 1 }; }
    out[s.dataset.screenLabel] = { w: sr.width, h: sr.height, visuals: els };
  }
  return out;
});
const report = { tolerance_px: 2, screens: {}, failures: [], overflow: [] };
for (const [label, m] of Object.entries(measured)) {
  const pg = layout.pages.find(p => label === p.name || label.startsWith(p.name + '--'));
  report.screens[label] = { size: [m.w, m.h], checked: 0 };
  if (m.w !== layout.canvas.w || m.h !== layout.canvas.h) report.failures.push(`${label}: screen ${m.w}x${m.h}`);
  for (const [name, r] of Object.entries(m.visuals)) {
    const slot = pg.visuals.find(v => v.name === name);
    if (!slot) { report.failures.push(`${label}/${name}: not in layout`); continue; }
    report.screens[label].checked++;
    for (const [k, sk] of [['x', 'x'], ['y', 'y'], ['w', 'w'], ['h', 'h']]) if (Math.abs(r[k] - slot[sk]) > 2) report.failures.push(`${label}/${name}: ${k} ${r[k]} vs ${slot[sk]}`);
    if (r.overflowX || r.overflowY) report.overflow.push(`${label}/${name}: content overflows its slot (${r.overflowX ? 'x' : ''}${r.overflowY ? 'y' : ''})`);
  }
}
let i = 0;
for (const s of await page.$$('[data-screen-label]')) {
  const label = await s.getAttribute('data-screen-label');
  await s.scrollIntoViewIfNeeded();
  await s.screenshot({ path: `${outDir}/opzet-${label}.png` }); i++;
}
writeFileSync('project/design-prototypes/opzet-layout-check.json', JSON.stringify(report, null, 1) + '\n');
console.log(`${i} screens captured at @${scale}x into ${outDir}; slot check: ${report.failures.length} failures, ${report.overflow.length} overflow warnings`);
for (const f of [...report.failures, ...report.overflow]) console.log('  ' + f);
await browser.close();
