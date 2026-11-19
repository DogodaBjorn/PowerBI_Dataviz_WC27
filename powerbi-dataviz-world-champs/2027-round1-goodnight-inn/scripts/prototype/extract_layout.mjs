// scripts/prototype/extract_layout.mjs — dump exact element rects from an HTML design comp
// (px-prototype module). Vendored from Bjorn's hp-world-champs pixel-perfect handoff
// bundle (design_handoff_powerbi/tools/extract_layout.mjs, MIT) and generalized.
//
// usage (from the repo root):
//   node scripts/prototype/extract_layout.mjs <comp.html> [outFile|-]
// outFile defaults to project/design-prototypes/layout.json; "-" prints to stdout.
//
// Comp convention: each screen is an element carrying data-screen-label, sized
// exactly to its page canvas (1280x720 default; tooltip pages at their own size).
// Output: per screen (keyed by data-screen-label), every element >= 2px with tag,
// own text, rect {x, y, w, h} relative to the screen's top-left (= report-canvas
// coordinates), computed font, background, and border. Copy the rects verbatim
// into visual.json positions — never eyeball.
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import { resolve, dirname } from 'path';
import { mkdirSync, writeFileSync } from 'fs';

const [file, outFile = 'project/design-prototypes/layout.json'] = process.argv.slice(2);
if (!file) { console.error('usage: node scripts/prototype/extract_layout.mjs <comp.html> [outFile|-]'); process.exit(1); }
const browser = await chromium.launch();
// Viewport must exceed the largest screen in the comp or rects clip.
const page = await browser.newPage({ viewport: { width: 1600, height: 1200 } });
await page.goto(pathToFileURL(resolve(file)).href);
await page.waitForTimeout(4000); // let the comp runtime + webfonts settle before measuring
const data = await page.evaluate(() => {
  const out = {};
  const r2 = (n) => Math.round(n * 10) / 10;
  for (const screen of document.querySelectorAll('[data-screen-label]')) {
    const sr = screen.getBoundingClientRect();
    const els = [];
    for (const el of screen.querySelectorAll('*')) {
      const r = el.getBoundingClientRect();
      if (r.width < 2 || r.height < 2) continue;
      const cs = getComputedStyle(el);
      const ownText = [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent.trim()).join(' ').trim();
      els.push({
        tag: el.tagName.toLowerCase(),
        text: ownText.slice(0, 80) || undefined,
        rect: { x: r2(r.x - sr.x), y: r2(r.y - sr.y), w: r2(r.width), h: r2(r.height) },
        font: ownText ? { family: cs.fontFamily, size: cs.fontSize, weight: cs.fontWeight, color: cs.color, letterSpacing: cs.letterSpacing, transform: cs.textTransform } : undefined,
        bg: cs.backgroundColor !== 'rgba(0, 0, 0, 0)' ? cs.backgroundColor : undefined,
        bgImage: cs.backgroundImage !== 'none' ? cs.backgroundImage : undefined,
        border: cs.borderTopWidth !== '0px' ? cs.borderTopWidth + ' ' + cs.borderTopStyle + ' ' + cs.borderTopColor : undefined,
      });
    }
    out[screen.dataset.screenLabel] = { size: { w: r2(sr.width), h: r2(sr.height) }, elements: els };
  }
  return out;
});
const screens = Object.keys(data).length;
if (screens === 0) console.error('WARNING: no [data-screen-label] screens found - check the comp conventions');
const json = JSON.stringify(data, null, 1);
if (outFile === '-') {
  console.log(json);
} else {
  mkdirSync(dirname(resolve(outFile)), { recursive: true });
  writeFileSync(resolve(outFile), json + '\n'); // UTF-8, no BOM
  console.error('wrote ' + outFile + ' (' + screens + ' screens)');
}
await browser.close();
