// Page backgrounds for the opzet report (canvas-studio method: furniture only, brand tokens).
//
// usage (from the repo root):  node project/tools/opzet_backgrounds.mjs
// Reads  project/design-prototypes/opzet-layout.json and the kit lockup;
// writes project/deliverables/backgrounds/<page>.svg and <page>.png (1920x1080), which
// project/tools/opzet_report.py registers as the page background image.
// Drawn: canvas, the always-visible cards (Sheet fill, Seam hairline, radius 12) and the
// lockup. State-dependent tiles (P2 shortlist) are NOT drawn here: a background cannot
// swap with a bookmark, so they are textbox visuals in the report.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
import { mkdirSync, readFileSync, writeFileSync } from 'fs';

const layout = JSON.parse(readFileSync('project/design-prototypes/opzet-layout.json', 'utf-8'));
const lockup = readFileSync('design/brand-kits/goodnight-inn-hanger/assets/goodnight-inn-lockup.svg', 'utf-8')
  .replace(/^<svg[^>]*>/, '').replace(/<\/svg>\s*$/, '');
const T = { canvas: '#F5F3F0', surface: '#FFFFFF', hair: '#E4DEE3' };
const out = 'project/deliverables/backgrounds';
mkdirSync(out, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: layout.canvas.w, height: layout.canvas.h }, deviceScaleFactor: 1 });
for (const p of layout.pages) {
  const cards = p.cards.filter(c => !c.state).map(c => `<rect x="${c.x + 0.5}" y="${c.y + 0.5}" width="${c.w - 1}" height="${c.h - 1}" rx="12" fill="${T.surface}" stroke="${T.hair}" stroke-width="1"/>`).join('\n');
  const s = p.logo.h / 104;
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${layout.canvas.w}" height="${layout.canvas.h}" viewBox="0 0 ${layout.canvas.w} ${layout.canvas.h}">
<rect width="100%" height="100%" fill="${T.canvas}"/>
${cards}
<g transform="translate(${p.logo.x} ${p.logo.y}) scale(${s})">${lockup}</g>
</svg>
`;
  writeFileSync(`${out}/${p.name}.svg`, svg);
  await page.setContent(`<html><body style="margin:0">${svg}</body></html>`);
  await page.locator('svg').first().screenshot({ path: `${out}/${p.name}.png` });
  console.log(`wrote ${out}/${p.name}.svg and .png`);
}
await browser.close();
