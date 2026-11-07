// Page backgrounds for the opzet report (canvas-studio method: furniture only, brand tokens).
//
// usage (from the repo root):  node project/tools/opzet_backgrounds.mjs
// Reads  project/design-prototypes/opzet-layout.json and the kit lockup;
// writes project/deliverables/backgrounds/<page>.svg and <page>.png (1920x1080), which
// project/tools/opzet_report.py registers as the page background image.
// Drawn: canvas, the always-visible cards (Sheet fill, Seam hairline, radius 12) and the
// lockup (asleep on P1, awake on P2). State-dependent tiles (P2 shortlist) are NOT drawn here: a background cannot
// swap with a bookmark, so they are textbox visuals in the report.
// v2 (2026-11-07): also draws the layout's hairline 'rules' (the P1 KPI band), and renders with headless Edge when
// Playwright is not installed (same pixels: Chromium either way; a fresh --user-data-dir keeps it off a running Edge).
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
import { mkdirSync, readFileSync, writeFileSync, existsSync, unlinkSync, statSync } from 'fs';
import { execFileSync } from 'child_process';
import { tmpdir } from 'os';
import { join, resolve } from 'path';
import { pathToFileURL } from 'url';
let chromium = null;
try { ({ chromium } = require('playwright')); } catch { chromium = null; }
const EDGE = ['C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', 'C:/Program Files/Microsoft/Edge/Application/msedge.exe'].find(p => existsSync(p));
if (!chromium && !EDGE) throw new Error('neither Playwright nor Microsoft Edge is available to render the PNGs');

const layout = JSON.parse(readFileSync('project/design-prototypes/opzet-layout.json', 'utf-8'));
const lockup = readFileSync('design/brand-kits/goodnight-inn-hanger/assets/goodnight-inn-lockup.svg', 'utf-8')
  .replace(/^<svg[^>]*>/, '').replace(/<\/svg>\s*$/, '');
// The kit wants the sleeping hanger on P1 and the awake hanger on P2 (brand-guide sections 3-5).
// The kit ships an awake mark but no awake lockup; the tile geometry is identical, so the awake
// lockup is the lockup with the awake mark's eyes (goodnight-inn-hanger-awake.svg). To retire
// when project/tools/brand_logos.py emits goodnight-inn-lockup-awake.svg.
const SLEEP_EYES = '<path d="M16 60 q6 7 12 0 M36 60 q6 7 12 0" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>';
const AWAKE_EYES = '<circle cx="22" cy="62" r="4" fill="#FFFFFF"/><circle cx="42" cy="62" r="4" fill="#FFFFFF"/>';
if (!lockup.includes(SLEEP_EYES)) throw new Error('lockup eyes not found: the kit asset changed, update the awake derivation');
const LOCKUP = { 'p1-brand-review': lockup, 'p2-investment-strategy': lockup.replace(SLEEP_EYES, AWAKE_EYES) };
const T = { canvas: '#F5F3F0', surface: '#FFFFFF', hair: '#E4DEE3' };
const out = 'project/deliverables/backgrounds';
mkdirSync(out, { recursive: true });
const browser = chromium ? await chromium.launch() : null;
const page = browser ? await browser.newPage({ viewport: { width: layout.canvas.w, height: layout.canvas.h }, deviceScaleFactor: 1 }) : null;
for (const p of layout.pages) {
  if (!p.logo) continue;  // v3: the tooltip page (tt-package) has no masthead
  // v2: the cards are report visuals now (opzet_report.py card_frames), so they scale with the content on any
  // viewport; the background keeps only the canvas colour and the lockup.
  const cards = '';
  const rules = '';
  const s = p.logo.h / 104;
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${layout.canvas.w}" height="${layout.canvas.h}" viewBox="0 0 ${layout.canvas.w} ${layout.canvas.h}">
<rect width="100%" height="100%" fill="${T.canvas}"/>
${cards}
${rules}
<g transform="translate(${p.logo.x} ${p.logo.y}) scale(${s})">${LOCKUP[p.name]}</g>
</svg>
`;
  writeFileSync(`${out}/${p.name}.svg`, svg);
  const html = `<html><body style="margin:0;overflow:hidden">${svg}</body></html>`;
  if (page) {
    await page.setContent(html);
    await page.locator('svg').first().screenshot({ path: `${out}/${p.name}.png` });
  } else {
    const tmp = join(tmpdir(), `opzet-bg-${p.name}.html`);
    const png = resolve(out, p.name + '.png');
    writeFileSync(tmp, html);
    if (existsSync(png)) unlinkSync(png);
    execFileSync(EDGE, ['--headless=new', '--disable-gpu', '--hide-scrollbars', `--user-data-dir=${join(tmpdir(), 'opzet-bg-edge')}`,
      `--window-size=${layout.canvas.w},${layout.canvas.h}`, `--screenshot=${png}`, '--force-device-scale-factor=1', pathToFileURL(tmp).href]);
    // Edge can return before the screenshot is on disk (7 Nov: opzet_report.py then copied the previous PNG):
    // wait until the file exists and its size has settled.
    let last = -1;
    for (let i = 0; i < 100; i++) {
      const size = existsSync(png) ? statSync(png).size : -1;
      if (size > 0 && size === last) break;
      last = size;
      await new Promise(r => setTimeout(r, 200));
    }
    if (!existsSync(png)) throw new Error(`Edge did not write ${png}`);
  }
  console.log(`wrote ${out}/${p.name}.svg and .png`);

  // v2: the lockup as its own PNG (asleep on P1, awake on P2) for an image visual, so the logo scales with the
  // content like the cards do. 2x the kit's 368x104, on the canvas colour.
  const LW = 736, LH = 208;
  const lsvg = `<svg xmlns="http://www.w3.org/2000/svg" width="${LW}" height="${LH}" viewBox="0 0 368 104"><rect width="368" height="104" fill="${T.canvas}"/>${LOCKUP[p.name]}</svg>`;
  const lhtml = `<html><body style="margin:0;overflow:hidden;background:${T.canvas}">${lsvg}</body></html>`;
  const lpng = resolve(out, `lockup-${p.name}.png`);
  if (page) {
    await page.setViewportSize({ width: LW, height: LH });
    await page.setContent(lhtml);
    await page.locator('svg').first().screenshot({ path: lpng });
    await page.setViewportSize({ width: layout.canvas.w, height: layout.canvas.h });
  } else {
    const tmp = join(tmpdir(), `opzet-lockup-${p.name}.html`);
    writeFileSync(tmp, lhtml);
    if (existsSync(lpng)) unlinkSync(lpng);
    execFileSync(EDGE, ['--headless=new', '--disable-gpu', '--hide-scrollbars', `--user-data-dir=${join(tmpdir(), 'opzet-bg-edge')}`,
      `--window-size=${LW},${LH}`, `--screenshot=${lpng}`, '--force-device-scale-factor=1', pathToFileURL(tmp).href]);
    let last = -1;
    for (let i = 0; i < 100; i++) {
      const size = existsSync(lpng) ? statSync(lpng).size : -1;
      if (size > 0 && size === last) break;
      last = size;
      await new Promise(r => setTimeout(r, 200));
    }
    if (!existsSync(lpng)) throw new Error(`Edge did not write ${lpng}`);
  }
  console.log(`wrote ${lpng}`);
}
if (browser) await browser.close();
