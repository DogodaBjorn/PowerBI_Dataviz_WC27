// Build step 12 of doc 23: who gets the mouse? Runs inside the published page (web.mjs, op "evalfile").
// In the service every visual container is 20 px taller than its visual: a strip above it for the visual header,
// which takes the mouse even when the header is switched off. A visual higher in the z-order therefore blinds the
// 20 px above itself for whatever lies under it. For every container: the share of its visual's area where it is
// the topmost container, and who covers the rest, split into "strip" (the 20 px above the other visual) and
// "body". For every mark (scatter dot, column, bar, slicer tile, button): whether its centre reaches it.
(() => {
  const d = document.querySelector('.displayArea').getBoundingClientRect();
  const k = d.width / 1920, ox = d.x, oy = d.y + (d.height - d.width * 1080 / 1920);
  const page = r => [Math.round((r.x - ox) / k), Math.round((r.y - oy) / k), Math.round(r.width / k), Math.round(r.height / k)];
  const cons = [...document.querySelectorAll('.visualContainer')].filter(c => { const r = c.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
  const vis = c => (c.querySelector('.visual') || c).getBoundingClientRect();
  const owner = (x, y) => { const e = document.elementFromPoint(x, y); return e ? e.closest('.visualContainer') : null; };
  const out = { scale: k, containers: [], marks: [] };
  cons.forEach((c, i) => {
    const r = vis(c); let total = 0, own = 0; const by = {};
    const step = Math.max(3, Math.min(r.width, r.height) / 12);
    for (let x = r.x + 1.5; x < r.right - 1; x += step) for (let y = r.y + 1.5; y < r.bottom - 1; y += step) {
      total++; const o = owner(x, y);
      if (o === c) { own++; continue; }
      const j = cons.indexOf(o); const where = o && y < vis(o).y ? 'strip' : 'body';
      by[j + ':' + where] = (by[j + ':' + where] || 0) + 1;
    }
    out.containers.push({ i, z: Number(getComputedStyle(c).zIndex) || Number(getComputedStyle(c.parentElement).zIndex) || 0, rect: page(r), type: (String((c.querySelector('.visual') || c).className).match(/visual-(\w+)/) || [])[1] || '', total, own, by });
  });
  const sel = 'path.scatterMarker, rect.column, rect.bar, .slicerItemContainer, [role="button"], [role="option"], [role="link"], [role="tab"], button';
  document.querySelectorAll(sel).forEach(m => {
    const c = m.closest('.visualContainer'); if (!c) return;
    const r = m.getBoundingClientRect(); if (!r.width || !r.height) return;
    const x = r.x + r.width / 2, y = r.y + r.height / 2; const o = owner(x, y);
    out.marks.push({ of: cons.indexOf(c), at: [Math.round((x - ox) / k), Math.round((y - oy) / k)], kind: m.tagName + '.' + String(m.getAttribute('class') || m.getAttribute('role') || '').split(' ')[0],
      label: (m.getAttribute('aria-label') || m.textContent || '').trim().slice(0, 50), ok: o === c, by: o === c ? -1 : cons.indexOf(o), where: o && o !== c && y < vis(o).y ? 'strip' : 'body' });
  });
  return out;
})()
