"""Builds the HTML comp of the new report set-up (opzet, 2026-11-06).

Run from the repo root:
    python project/tools/build_opzet_comp.py
Inputs : project/design-prototypes/opzet-layout.json  (slot map: the single source of positions)
         project/design-prototypes/opzet-data.json    (facts from project/analysis/41_opzet_facts.py)
         design/brand-kits/goodnight-inn-hanger/       (tokens and the lockup)
Output : project/design-prototypes/opzet-goodnight-inn.html (self-contained, three screens:
         p1-brand-review, p2-investment-strategy (shortlist state), p2-investment-strategy--plan).

The comp is a picture of the report, not the report: every number in it comes from the offline
facts, and the PBIR generator (project/tools/opzet_report.py) binds the same slots to model
measures that re-derive those numbers. Fonts are the kit's (Trebuchet MS, Verdana); a machine
without them renders fallbacks, which moves text but not the slot rectangles.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROTO = ROOT / "project" / "design-prototypes"
KIT = ROOT / "design" / "brand-kits" / "goodnight-inn-hanger" / "assets"

layout = json.loads((PROTO / "opzet-layout.json").read_text(encoding="utf-8"))
data = json.loads((PROTO / "opzet-data.json").read_text(encoding="utf-8"))
lockup = (KIT / "goodnight-inn-lockup.svg").read_text(encoding="utf-8")
lockup = lockup.replace('<svg ', '<svg preserveAspectRatio="xMinYMid meet" ', 1)

HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Goodnight Inn opzet</title>
<style>
:root{--canvas:#F5F3F0;--surface:#FFFFFF;--ink:#24192B;--ink2:#5B5163;--hair:#E4DEE3;--accent:#B5175F;--mark:#D6336C;
--good:#1D5FA8;--bad:#B45309;--neutral:#82798A;--plum:#3E2C55;--lilac:#B8B0BE;--linen:#D9D2CC;--tint:#F8D7E3;--tint2:#EE9DBA;
--display:"Trebuchet MS",Verdana,sans-serif;--body:Verdana,Arial,sans-serif}
html,body{margin:0;background:#D9D2CC;color:var(--ink);font-family:var(--body)}
.screen{position:relative;width:1920px;height:1080px;background:var(--canvas);overflow:hidden;margin:0 0 48px 0}
.card{position:absolute;background:var(--surface);border:1px solid var(--hair);border-radius:12px;box-sizing:border-box}
.tile{position:absolute;background:var(--canvas);border:1px solid var(--hair);border-radius:12px;box-sizing:border-box}
.v{position:absolute;box-sizing:border-box;overflow:hidden}
.logo{position:absolute}
.logo svg{width:100%;height:100%}
.v svg{display:block}
table.geo th:nth-child(2){text-align:right}
.mast{font-size:13px;letter-spacing:.08em;color:var(--ink2);text-align:right;line-height:24px}
.head{font-family:var(--display);font-weight:bold;font-size:37px;line-height:48px;color:var(--ink)}
.sub{font-size:15px;line-height:32px;color:var(--ink2);white-space:nowrap}
.title{font-family:var(--display);font-weight:bold;font-size:17px;line-height:32px;color:var(--ink);white-space:nowrap}
.cap{font-size:13px;line-height:20px;color:var(--ink2)}
.foot{font-size:13px;line-height:24px;color:var(--ink2);white-space:nowrap}
table{border-collapse:collapse;width:100%;font-size:14.5px}
th{font-weight:normal;color:var(--ink2);text-align:right;padding:0 8px;height:34px;border-bottom:1px solid var(--ink2);font-size:13px}
th:nth-child(1),th:nth-child(2){text-align:left}
td{height:33px;border-bottom:1px solid var(--hair);padding:0 8px;text-align:right;white-space:nowrap}
td.l{text-align:left}
td.f{color:var(--accent);font-weight:bold;font-size:13px}
td.gn,th.gn{background:var(--tint)}
.good{color:var(--good)}.bad{color:var(--bad)}.mute{color:var(--ink2)}
.chip{display:inline-block;border-radius:999px;padding:0 14px;line-height:30px;font-size:14px;border:1px solid var(--hair);background:var(--surface);color:var(--ink2);margin-right:4px}
.chip.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.slh{font-size:13px;color:var(--ink2);line-height:20px}
.dd{border:1px solid var(--hair);border-radius:999px;line-height:30px;padding:0 14px;font-size:14px;background:var(--surface);display:flex;justify-content:space-between}
.btn{border-radius:999px;background:var(--accent);color:#fff;font-size:14px;line-height:40px;text-align:center;font-weight:bold}
.btn.ghost{background:var(--surface);color:var(--ink);border:1px solid var(--ink2);line-height:38px}
.ph{font-size:14.5px;font-weight:bold;color:var(--ink);line-height:24px;white-space:nowrap}
.mix{font-size:14.5px;line-height:24px;color:var(--ink)}
.nums{display:flex;gap:16px}
.num{flex:1}
.num b{display:block;font-size:22px;line-height:32px;font-weight:bold;white-space:nowrap}
.num span{font-size:13px;color:var(--ink2);line-height:16px;display:block}
.note{font-size:13px;line-height:20px;color:var(--ink2)}
svg text{font-family:Verdana,Arial,sans-serif}
.plan table{font-size:13px}.plan th{font-size:12px;height:30px;padding:0 5px}.plan td{height:28px;padding:0 5px}
td.chipc{padding:0 4px;width:40px}
td.chipc svg{display:inline-block;vertical-align:middle}
.st-on{color:var(--accent);font-weight:bold}.st-off{color:var(--ink2)}
</style>
</head>
<body>
<div id="root"></div>
<script id="layout" type="application/json">__LAYOUT__</script>
<script id="facts" type="application/json">__DATA__</script>
<template id="lockup">__LOCKUP__</template>
<script>
const L = JSON.parse(document.getElementById('layout').textContent);
const F = JSON.parse(document.getElementById('facts').textContent);
const C = {ink:'#24192B',ink2:'#5B5163',hair:'#E4DEE3',accent:'#B5175F',mark:'#D6336C',good:'#1D5FA8',bad:'#B45309',neutral:'#82798A',plum:'#3E2C55',lilac:'#B8B0BE',tint:'#F8D7E3',tint2:'#EE9DBA',surface:'#FFFFFF'};
const MINUS = '−';
const sgn = (v, s) => (v < 0 ? MINUS : '+') + s;
const pct = (v, d=1) => (v*100).toFixed(d) + '%';
const usdM = (v, d=1) => '$' + (Math.abs(v)/1e6).toFixed(d) + 'M';
const susdM = (v, d=1) => sgn(v, usdM(v, d));
const SHORT = {'GI-01':'Booking app','GI-02':'Kiosks at 20 desks','GI-03':'Energy programme','GI-04':'Toronto +40 rooms','GI-05':'Gatwick +40 rooms','GI-06':'Kingston +40 rooms','GI-07':'Refresh 10 oldest','GI-08':'Boston new hotel','GI-09':'Breakfast upgrade','GI-10':'Revenue management'};
const ANSWERS = {'GI-01':'F2','GI-02':'F3','GI-03':'F1','GI-04':'F4','GI-05':'F4','GI-06':'F4','GI-07':'F3','GI-08':'F4','GI-09':'F3','GI-10':'F1'};
const BR = ['Goodnight Inn','P&K Select',"Maison d'Or",'Pebble & Pine'];
const G = F.brands['Goodnight Inn'];
const PROJ = Object.fromEntries(F.projects.map(p => [p.id, p]));
const MON = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const monthText = s => { const [y,m] = s.split('-'); return MON[+m-1] + ' ' + y; };

function el(tag, cls, html){ const e = document.createElement(tag); if (cls) e.className = cls; if (html !== undefined) e.innerHTML = html; return e; }
function place(parent, slot, cls, html, label){
  const e = el('div', 'v ' + (cls||''), html);
  Object.assign(e.style, {left:slot.x+'px', top:slot.y+'px', width:slot.w+'px', height:slot.h+'px'});
  e.dataset.visual = slot.name; if (label) e.setAttribute('aria-label', label);
  parent.appendChild(e); return e;
}
function svg(w, h){ const s = document.createElementNS('http://www.w3.org/2000/svg','svg'); s.setAttribute('width', w); s.setAttribute('height', h); s.setAttribute('viewBox', `0 0 ${w} ${h}`); return s; }
function add(s, tag, attrs, text){ const e = document.createElementNS('http://www.w3.org/2000/svg', tag); for (const k in attrs) e.setAttribute(k, attrs[k]); if (text !== undefined) e.textContent = text; s.appendChild(e); return e; }
function ticks(min, max, n){ const span = max - min, step0 = span / n, mag = Math.pow(10, Math.floor(Math.log10(step0))); const step = [1,2,2.5,5,10].map(m => m*mag).find(s => s >= step0); const out = []; for (let v = Math.ceil(min/step)*step; v <= max + 1e-9; v += step) out.push(+v.toFixed(10)); return out; }

// ---------------------------------------------------------------- shared chrome
function screen(page, label){
  const s = el('div', 'screen'); s.dataset.screenLabel = label; document.getElementById('root').appendChild(s);
  return s;
}
const SLEEP_EYES = '<path d="M16 60 q6 7 12 0 M36 60 q6 7 12 0" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>';
const AWAKE_EYES = '<circle cx="22" cy="62" r="4" fill="#FFFFFF"/><circle cx="42" cy="62" r="4" fill="#FFFFFF"/>';
function cards(s, page, state){
  for (const c of page.cards) { if (c.state && c.state !== state) continue; const d = el('div', c.id.startsWith('tile') ? 'tile' : 'card'); Object.assign(d.style, {left:c.x+'px', top:c.y+'px', width:c.w+'px', height:c.h+'px'}); s.appendChild(d); }
  const svgLogo = document.getElementById('lockup').innerHTML; // asleep on P1, awake on P2 (brand-guide sections 3-5)
  const lg = el('div', 'logo', page.name.startsWith('p2') ? svgLogo.replace(SLEEP_EYES, AWAKE_EYES) : svgLogo); Object.assign(lg.style, {left:page.logo.x+'px', top:page.logo.y+'px', width:page.logo.w+'px', height:page.logo.h+'px'}); s.appendChild(lg);
}
const slots = page => Object.fromEntries(page.visuals.map(v => [v.name, v]));
const FOOTER = "Data: Pillow & Key Group dataset, Power BI Dataviz World Champs 2027. Guest scores response-weighted. Margins before commissions unless marked. 2021 is a depressed base year. Projections: scenario logic from FinanceParameters.";

// ---------------------------------------------------------------- P1
const KPI = [
  ['F1','Full, margin slipping','Occupancy','occupancy',1,v=>pct(v),v=>sgn(v, Math.abs(v*100).toFixed(1)+' pt')],
  ['F1','','Average daily rate (segment)','adr',0,v=>'$'+v.toFixed(0),v=>sgn(v,'$'+Math.abs(v).toFixed(0))],
  ['F1','','RevPAR (segment)','revpar',0,v=>'$'+v.toFixed(0),v=>sgn(v,'$'+Math.abs(v).toFixed(0))],
  ['F1','','GOP margin before commissions','gop_margin',1,v=>pct(v),v=>sgn(v, Math.abs(v*100).toFixed(1)+' pt')],
  ['F1','','GOP margin after commissions','gop_margin_after',1,v=>pct(v),v=>sgn(v, Math.abs(v*100).toFixed(1)+' pt')],
  ['F2','Booked with us?','OTA share of room revenue','ota_share',-1,v=>pct(v),v=>sgn(v, Math.abs(v*100).toFixed(1)+' pt')],
  ['F2','','Direct share (web, app, phone)','direct_share',1,v=>pct(v),v=>sgn(v, Math.abs(v*100).toFixed(1)+' pt')],
  ['F2','','Distribution cost, % of room revenue','dist_pct_room',-1,v=>pct(v),v=>sgn(v, Math.abs(v*100).toFixed(1)+' pt')],
  ['F3','A good night?','Room comfort score (0 to 10)','comfort',1,v=>v.toFixed(2),v=>sgn(v, Math.abs(v).toFixed(2))],
  ['F3','','Room-condition complaints per 1,000','room_cond_1k',-1,v=>v.toFixed(2),v=>sgn(v, Math.abs(v).toFixed(2))],
  ['F3','','All complaints per 1,000 room nights','complaints_1k',-1,v=>v.toFixed(1),v=>sgn(v, Math.abs(v).toFixed(1))],
  ['F3','A fair price?','Value for money score (0 to 10)','value',1,v=>v.toFixed(2),v=>sgn(v, Math.abs(v).toFixed(2))],
  ['F3','Recommend us?','Net promoter score','nps',1,v=>sgn(v, Math.abs(v).toFixed(1)),v=>sgn(v, Math.abs(v).toFixed(1))],
];
function rankText(key, dir){
  if (!dir) return ['not ranked','mute'];
  const vals = BR.map(b => F.brands[b].y2025[key]); const gn = vals[0];
  const r = 1 + vals.filter(v => dir*v > dir*gn).length;
  return [r === 1 ? '\u25B2 best of 4' : r === 4 ? '\u25BC last of 4' : (r === 2 ? '2nd' : '3rd') + ' of 4', r === 1 ? 'good' : r === 4 ? 'bad' : 'mute'];
}
function p1(page){
  const s = screen(page, page.name); cards(s, page); const S = slots(page);
  place(s, S.z_masthead, 'mast', 'THE BRAND REVIEW &nbsp;·&nbsp; 2021 TO 2025 &nbsp;·&nbsp; FOR THE BOARD OF PILLOW &amp; KEY GROUP');
  place(s, S.z_headline, 'head', 'Do not disturb, since 2020.');
  const y = G.y2025;
  place(s, S.c_subtitle, 'sub', `Goodnight Inn fills the most rooms (${pct(y.occupancy)}) and keeps the widest margin before commissions (${pct(y.gop_margin)}); after commissions it is second (${pct(y.gop_margin_after)}), and on guests, channels and complaints it is last of four. The last renovation started in ${monthText(G.last_reno_start.slice(0,7))}.`);
  place(s, S.c_compare_title, 'title', 'Goodnight Inn leads on occupancy, and is last of four on what guests and booking channels say');
  place(s, S.c_compare_sub, 'cap', 'The brand promise is “A good night. A fair price.” The lines test it: booked with us, a good night, a fair price, recommend us. 2025, the four Pillow & Key brands; rates reflect each segment and are not ranked; change is 2023 to 2025.');
  let rows = '';
  for (const [code, fname, label, key, dir, fmt, dfmt] of KPI) {
    const [rk, rc] = rankText(key, dir);
    const dv = G.y2025[key] - G.y2023[key]; const dc = !dir ? 'mute' : (dir*dv > 0 ? 'good' : 'bad');
    rows += `<tr><td class="l f">${fname ? code + ' · ' + fname : ''}</td><td class="l">${label}</td>` + BR.map((b,i) => `<td class="${i===0?'gn':''}">${fmt(F.brands[b].y2025[key])}</td>`).join('') + `<td class="${rc}">${rk}</td><td class="${dc}">${dfmt(dv)}</td></tr>`;
  }
  place(s, S.hero_brand_compare, '', `<table><thead><tr><th>Finding</th><th>Measure</th>${BR.map((b,i)=>`<th class="${i===0?'gn':''}">${b}</th>`).join('')}<th>Goodnight Inn rank</th><th>Change since 2023</th></tr></thead><tbody>${rows}</tbody></table>`, 'Four-brand comparison table');
  const L1 = F.location;
  place(s, S.c_geo_title, 'title', `F4 · The airports are the fullest: ${pct(L1.Airport.occ)} occupancy, against ${pct(L1.Highway.occ)} on the highway`);
  place(s, S.c_geo_sub, 'cap', 'Occupancy 2025 by region and location type · number of hotels');
  const types = ['Airport','City','Highway'], regs = ['Asia-Pacific','Europe','North America'];
  const cell = (hs) => { if (!hs.length) return ['', '#FFFFFF']; const sold = hs.reduce((a,h)=>a+h.occ*h.rooms,0), rooms = hs.reduce((a,h)=>a+h.rooms,0); const o = sold/rooms; return [`${pct(o)} · ${hs.length}`, o >= .85 ? C.tint2 : o >= .80 ? C.tint : '#FFFFFF']; };
  let g = `<table class="geo"><thead><tr><th>Region</th>${types.map(t=>`<th>${t}</th>`).join('')}<th>Total</th></tr></thead><tbody>`;
  for (const r of [...regs, 'Total']) {
    const hr = F.hotels.filter(h => r === 'Total' || h.region === r);
    g += `<tr><td class="l">${r}</td>` + [...types.map(t => hr.filter(h => h.type === t)), hr].map(hs => { const [t, bg] = cell(hs); return `<td style="background:${bg}">${t}</td>`; }).join('') + '</tr>';
  }
  place(s, S.tbl_geo, '', g + '</tbody></table>', 'Occupancy by region and location type');
  place(s, S.c_full_title, 'cap', 'The seven fullest hotels, 2025 occupancy · airports in raspberry');
  const top = [...F.hotels].sort((a,b) => b.occ - a.occ).slice(0, 7);
  { const sl = S.ch_fullest_hotels, sv = svg(sl.w, sl.h), lw = 232, bw = sl.w - lw - 72, rh = sl.h / top.length;
    top.forEach((h, i) => { const yy = i*rh; add(sv,'text',{x:0,y:yy+rh/2+5,'font-size':13,fill:C.ink},h.name); add(sv,'rect',{x:lw,y:yy+8,width:bw*h.occ,height:rh-16,fill:h.type==='Airport'?C.accent:C.neutral,rx:2}); add(sv,'text',{x:lw+bw*h.occ+8,y:yy+rh/2+5,'font-size':13,fill:C.ink},pct(h.occ)); });
    place(s, sl, '', '').appendChild(sv); }
  const trend = (slot, key, title, scale, fmt) => {
    const sv = svg(slot.w, slot.h), top0 = 40, bot = slot.h - 24, left = 48, right = slot.w - 120;
    add(sv,'text',{x:0,y:16,'font-size':14,'font-weight':'bold',fill:C.ink,'font-family':'Trebuchet MS, Verdana'},title);
    const yrs = [2021,2022,2023,2024,2025]; const all = BR.flatMap(b => yrs.map(y => F.brands[b].trend[y][key]*scale));
    const mn = Math.min(...all), mx = Math.max(...all), pad = (mx-mn)*.08, y0 = mn - pad, y1 = mx + pad;
    const X = i => left + i*(right-left)/4, Y = v => bot - (v - y0)/(y1 - y0)*(bot - top0);
    for (const t of ticks(y0, y1, 4)) { add(sv,'line',{x1:left,x2:right,y1:Y(t),y2:Y(t),stroke:C.hair}); add(sv,'text',{x:left-6,y:Y(t)+4,'font-size':13,fill:C.ink2,'text-anchor':'end'},fmt(t)); }
    yrs.forEach((y,i) => add(sv,'text',{x:X(i),y:slot.h-6,'font-size':13,fill:C.ink2,'text-anchor':'middle'},y));
    const labs = BR.map(b => ({b, y: Y(F.brands[b].trend[2025][key]*scale)})).sort((a,c) => a.y - c.y);
    for (let i = 1; i < labs.length; i++) if (labs[i].y - labs[i-1].y < 14) labs[i].y = labs[i-1].y + 14;
    [...BR].reverse().forEach(b => { const gn = b === 'Goodnight Inn'; const pts = yrs.map((y,i) => `${X(i)},${Y(F.brands[b].trend[y][key]*scale)}`).join(' ');
      add(sv,'polyline',{points:pts,fill:'none',stroke:gn?C.accent:C.neutral,'stroke-width':gn?3:1.5}); });
    for (const l of labs) { const gn = l.b === 'Goodnight Inn'; add(sv,'text',{x:right+8,y:l.y+4,'font-size':13,fill:gn?C.accent:C.ink2,'font-weight':gn?'bold':'normal'},l.b); }
    place(s, slot, '', '').appendChild(sv);
  };
  const t = G.trend;
  trend(S.ch_trend_margin, 'gop_margin_after', `F1 · After commissions: ${pct(t[2023].gop_margin_after)} (2023) down to ${pct(t[2025].gop_margin_after)}`, 100, v => v.toFixed(0)+'%');
  trend(S.ch_trend_ota, 'ota_share', `F2 · OTAs book ${pct(t[2025].ota_share)} of room revenue, up from ${pct(t[2021].ota_share)}`, 100, v => v.toFixed(0)+'%');
  trend(S.ch_trend_nps, 'nps', `F3 · NPS down every year, to ${sgn(t[2025].nps, Math.abs(t[2025].nps).toFixed(1))}; sisters higher`, 1, v => (v>0?'+':'')+v.toFixed(0));
  place(s, S.z_footer, 'foot', FOOTER);
}

// ---------------------------------------------------------------- P2 helpers
const SCEN = 'Expected';
const PK = F.packages;
const ids = p => p.id.split('+').map(x => 'GI-' + x);
function presets(sc){
  const by = (arr, f) => arr.reduce((a,b) => f(b) > f(a) ? b : a);
  const A = by(PK, p => p.npv[sc]);
  const pos = PK.filter(p => p.npv[sc] >= 0);
  const B = pos.length ? pos.reduce((a,b) => (b.rated > a.rated || (b.rated === a.rated && b.npv[sc] > a.npv[sc])) ? b : a) : null;
  const C2 = by(PK.filter(p => p.refresh), p => p.npv[sc]);
  return {A, B, C: C2};
}
function cumulative(pkg, sc){ const yrs = [2027,2028,2029,2030,2031,2032]; let c = 0; return yrs.map(y => (c += ids(pkg).reduce((a,id) => a + PROJ[id].net_by_year[sc][y], 0))); }
function payback(pkg, sc){ const cum = cumulative(pkg, sc); const i = cum.findIndex(v => v >= 0); return i < 0 ? null : 2027 + i; }
function liveBy(pkg){ return ids(pkg).map(id => PROJ[id].live).sort().slice(-1)[0]; }
const mix = pkg => ids(pkg).map(id => SHORT[id]).join(' + ');

function p2common(s, page, S, focus, state){
  cards(s, page, state);
  place(s, S.z_masthead2, 'mast', 'THE INVESTMENT STRATEGY &nbsp;·&nbsp; 2027 TO 2032 &nbsp;·&nbsp; GOODNIGHT INN BUDGET $60.0M');
  place(s, S.z_headline2, 'head', 'Please make up the room.');
  const n = ids(focus).length, g = ids(focus).filter(id => PROJ[id].growth === 'Yes').length;
  place(s, S.c_subtitle2, 'sub', `In focus, package ${focus.id}: ${usdM(focus.capex)} of the $60.0M budget on ${n} initiatives (${g} growth). NPV through 2032 ${susdM(focus.npv[SCEN])} (${SCEN}; Low ${susdM(focus.npv.Low)}, High ${susdM(focus.npv.High)}); ${susdM(focus.rr[SCEN])} a year of operating profit by 2032.`);
  const pos = PK.filter(p => p.npv[SCEN] >= 0).length;
  place(s, S.c_scatter_title, 'title', `${pos === 0 ? 'None' : pos} of ${PK.length} valid packages ${pos === 1 ? 'is' : 'are'} worth more than ${pos === 1 ? 'it costs' : 'they cost'} by December 2032 (${SCEN} case)`);
  place(s, S.c_scatter_sub, 'cap', 'One dot per package the rules allow: three or more initiatives, at least one growth initiative, within $60M, kiosks only with the app. Raspberry: the package in focus · plum: without the room refresh · grey: with it.');
  { const sl = S.hero_packages, sv = svg(sl.w, sl.h), left = 72, right = sl.w - 16, top0 = 16, bot = sl.h - 48;
    const xs = PK.map(p => p.capex/1e6), ys = PK.map(p => p.npv[SCEN]/1e6);
    const x0 = 0, x1 = 60, y0 = Math.floor(Math.min(...ys)/5)*5 - 5, y1 = Math.ceil(Math.max(...ys)/5)*5 + 5;
    const X = v => left + (v-x0)/(x1-x0)*(right-left), Y = v => bot - (v-y0)/(y1-y0)*(bot-top0);
    for (const t of ticks(y0, y1, 8)) { add(sv,'line',{x1:left,x2:right,y1:Y(t),y2:Y(t),stroke:t===0?C.ink2:C.hair,'stroke-width':t===0?1.5:1}); add(sv,'text',{x:left-8,y:Y(t)+4,'font-size':13,fill:C.ink2,'text-anchor':'end'},(t>0?'+':t<0?MINUS:'')+'$'+Math.abs(t)+'M'); }
    for (const t of ticks(x0, x1, 6)) add(sv,'text',{x:X(t),y:bot+20,'font-size':13,fill:C.ink2,'text-anchor':'middle'},'$'+t+'M');
    add(sv,'text',{x:(left+right)/2,y:sl.h-6,'font-size':13,fill:C.ink2,'text-anchor':'middle'},'Capex of the package, $M');
    const yl = add(sv,'text',{x:16,y:(top0+bot)/2,'font-size':13,fill:C.ink2,'text-anchor':'middle',transform:`rotate(-90 16 ${(top0+bot)/2})`},'NPV through 2032, $M (2025 dollars, 8%)');
    add(sv,'text',{x:right-4,y:Y(0)-8,'font-size':13,fill:C.ink2,'text-anchor':'end'},'worth its cost by 2032 above this line');
    PK.forEach(p => { if (p.id !== focus.id) add(sv,'circle',{cx:X(p.capex/1e6),cy:Y(p.npv[SCEN]/1e6),r:4.5,fill:p.refresh?C.neutral:C.plum,'fill-opacity':.85}); });
    add(sv,'circle',{cx:X(focus.capex/1e6),cy:Y(focus.npv[SCEN]/1e6),r:11,fill:C.accent,stroke:'#fff','stroke-width':2});
    add(sv,'text',{x:X(focus.capex/1e6)+16,y:Y(focus.npv[SCEN]/1e6)+5,'font-size':13,'font-weight':'bold',fill:C.accent},focus.id);
    place(s, sl, '', '', 'Scatter of all valid packages').appendChild(sv); }
  place(s, S.sl_scenario, '', `<div class="slh">Scenario</div>${['Low','Expected','High'].map(x => `<span class="chip ${x===SCEN?'on':''}">${x}</span>`).join('')}`);
  place(s, S.sl_package, '', `<div class="slh">Package in focus</div><div class="dd"><span>A · Highest NPV through 2032</span><span>▾</span></div>`);
  place(s, S.z_footer2, 'foot', FOOTER);
}
function p2shortlist(page){
  const s = screen(page, page.name); const S = slots(page); const P3 = presets(SCEN);
  p2common(s, page, S, P3.A, 'shortlist');
  place(s, S.c_short_title, 'title', `Three packages, one per criterion (${SCEN} case)`);
  const heads = {A:'A · Highest NPV through 2032', B:'B · Most hotels with a guest-score effect, NPV at least zero', C:'C · Highest NPV that includes the refresh of the ten oldest hotels'};
  for (const k of ['A','B','C']) { const p = P3[k], lk = k.toLowerCase();
    place(s, S[`c_preset_${lk}_head`], 'ph', heads[k]);
    place(s, S[`c_preset_${lk}_mix`], 'mix', p ? `${p.id}: ${mix(p)}` : 'No package qualifies in this case.');
    place(s, S[`c_preset_${lk}_nums`], 'nums', p ? [[usdM(p.capex),'capex'],[susdM(p.npv[SCEN]),'NPV, '+SCEN],[`${sgn(p.npv.Low, Math.abs(p.npv.Low/1e6).toFixed(1))} to ${sgn(p.npv.High, Math.abs(p.npv.High/1e6).toFixed(1))}`,'NPV, Low to High, $M'],[susdM(p.rr[SCEN]),'a year by 2032']].map(([v,l]) => `<div class="num"><b>${v}</b><span>${l}</span></div>`).join('') : ''); }
  const gross = PROJ['GI-01'];
  place(s, S.c_uncertainty, 'note', `Read with care: no package is worth its cost by 2032 in the Low case, and nothing after 2032 is counted. Profit impacts are taken as net of running costs; read gross, the booking app earns $0.6M a year less.`);
  place(s, S.btn_open_plan, 'btn', 'Open the plan for the package in focus &nbsp;→');
}
function p2plan(page){
  const s = screen(page, page.name + '--plan'); const S = slots(page); const focus = presets(SCEN).A;
  p2common(s, page, S, focus, 'plan');
  const pr = ids(focus);
  place(s, S.c_plan_title, 'title', `${focus.id} in focus: ${usdM(focus.capex)} on ${pr.length} initiatives, all live by ${monthText(liveBy(focus))}`);
  { const sl = S.ch_plan_waterfall, sv = svg(sl.w, sl.h), left = 8, right = sl.w - 8, top0 = 36, bot = sl.h - 40;
    add(sv,'text',{x:0,y:16,'font-size':13,'font-weight':'bold',fill:C.ink},`Where the NPV comes from, $M through 2032 (${SCEN})`);
    const vals = pr.map(id => PROJ[id].npv[SCEN]/1e6); let run = 0; const steps = vals.map(v => { const a = run; run += v; return [a, run]; });
    const lo = Math.min(0, ...steps.flat()), hi = Math.max(0, ...steps.flat()), pad = (hi-lo)*.15; const Y = v => bot - (v-(lo-pad))/((hi+pad)-(lo-pad))*(bot-top0);
    const n = pr.length + 1, bw = (right-left)/n;
    add(sv,'line',{x1:left,x2:right,y1:Y(0),y2:Y(0),stroke:C.ink2});
    steps.forEach(([a,b], i) => { const v = b - a; add(sv,'rect',{x:left+i*bw+8,y:Math.min(Y(a),Y(b)),width:bw-16,height:Math.max(2,Math.abs(Y(a)-Y(b))),fill:v>=0?C.good:C.bad}); add(sv,'text',{x:left+i*bw+bw/2,y:Math.min(Y(a),Y(b))-6,'font-size':12,'text-anchor':'middle',fill:C.ink},susdM(v*1e6)); add(sv,'text',{x:left+i*bw+bw/2,y:sl.h-20,'font-size':11,'text-anchor':'middle',fill:C.ink2},SHORT[pr[i]]); });
    add(sv,'rect',{x:left+pr.length*bw+8,y:Math.min(Y(0),Y(run)),width:bw-16,height:Math.max(2,Math.abs(Y(0)-Y(run))),fill:C.ink});
    add(sv,'text',{x:left+pr.length*bw+bw/2,y:Math.min(Y(0),Y(run))-6,'font-size':12,'font-weight':'bold','text-anchor':'middle',fill:C.ink},susdM(run*1e6));
    add(sv,'text',{x:left+pr.length*bw+bw/2,y:sl.h-20,'font-size':11,'text-anchor':'middle',fill:C.ink2},'Package');
    place(s, sl, '', '').appendChild(sv); }
  const chip = on => { const h = on ? `<rect x="4" y="4" width="56" height="96" rx="14" fill="#FFFFFF"/><circle cx="22" cy="62" r="4" fill="${C.accent}"/><circle cx="42" cy="62" r="4" fill="${C.accent}"/>` : `<rect x="4" y="4" width="56" height="96" rx="14" fill="${C.accent}"/><path d="M16 60 q6 7 12 0 M36 60 q6 7 12 0" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>`;
    return `<svg width="40" height="28" viewBox="0 0 40 28"><rect x="0.5" y="0.5" width="39" height="27" rx="13.5" fill="${on ? C.accent : '#FFFFFF'}" stroke="${on ? C.accent : C.hair}"/><g transform="translate(14.2 3) scale(0.2115)">${h}</g></svg>`; };
  const all = F.projects.map(p => p.id).sort((a,b) => (pr.includes(b) - pr.includes(a)) || (PROJ[b].npv[SCEN] - PROJ[a].npv[SCEN]));
  let t = '<table><thead><tr><th></th><th style="text-align:left">Status</th><th style="text-align:left">Initiative</th><th style="text-align:left">Answers</th><th>Capex</th><th>Live</th><th>Run-rate</th><th>NPV</th><th>Guest pts</th></tr></thead><tbody>';
  for (const id of all) { const p = PROJ[id], on = pr.includes(id); t += `<tr><td class="chipc">${chip(on)}</td><td class="l ${on ? 'st-on' : 'st-off'}">${on ? 'Funded' : 'Not funded'}</td><td class="l">${SHORT[id]}</td><td class="l f">${ANSWERS[id]}</td><td>${usdM(p.capex)}</td><td>${monthText(p.live)}</td><td>${susdM(p.runrate[SCEN])}</td><td>${susdM(p.npv[SCEN])}</td><td>${p.sat[SCEN] ? '+' + p.sat[SCEN].toFixed(2) + ' on ' + p.hotels : '·'}</td></tr>`; }
  place(s, S.tbl_plan_initiatives, 'plan', t + '</tbody></table>', 'All ten initiatives: funded in the package in focus, or not');
  { const sl = S.ch_plan_cumulative, sv = svg(sl.w, sl.h), left = 48, right = sl.w - 8, top0 = 28, bot = sl.h - 20;
    add(sv,'text',{x:0,y:14,'font-size':13,'font-weight':'bold',fill:C.ink},'Cumulative net impact, $M · Low to High');
    const series = ['Low','Expected','High'].map(sc => cumulative(focus, sc).map(v => v/1e6)); const all = series.flat().concat([0]);
    const mn = Math.min(...all), mx = Math.max(...all); const X = i => left + i*(right-left)/5, Y = v => bot - (v-mn)/(mx-mn)*(bot-top0);
    add(sv,'line',{x1:left,x2:right,y1:Y(0),y2:Y(0),stroke:C.ink2});
    [2027,2028,2029,2030,2031,2032].forEach((y,i) => add(sv,'text',{x:X(i),y:sl.h-4,'font-size':10,'text-anchor':'middle',fill:C.ink2},y));
    for (const tk of ticks(mn, mx, 3)) add(sv,'text',{x:left-6,y:Y(tk)+4,'font-size':10,'text-anchor':'end',fill:C.ink2},(tk<0?MINUS:'')+Math.abs(tk));
    series.forEach((ser, k) => add(sv,'polyline',{points:ser.map((v,i)=>`${X(i)},${Y(v)}`).join(' '),fill:'none',stroke:C.accent,'stroke-width':k===1?2:1}));
    place(s, sl, '', '').appendChild(sv); }
  const rooms_ref = pr.includes('GI-07') ? F.refresh10.rooms : 0;
  place(s, S.c_plan_ops, 'nums', [[focus.added.toString(),'rooms added'],[rooms_ref.toLocaleString('en-US'),'rooms refreshed'],[focus.rated.toString(),'hotels, guest effect']].map(([v,l]) => `<div class="num"><b>${v}</b><span>${l}</span></div>`).join('').replace(/class="nums"/,''));
  const pb = payback(focus, SCEN);
  const dis = pr.includes('GI-07') ? `15% of ${F.refresh10.rooms.toLocaleString('en-US')} rooms out of service for 14 months; ` : '';
  place(s, S.c_plan_risk, 'note', `Risks: ${dis}NPV in the Low case ${susdM(focus.npv.Low)}; the cumulative net turns positive ${pb ? 'in ' + pb : 'after 2032'} (${SCEN}). Kiosks wait for the app: they start when it goes live.`);
  place(s, S.btn_back, 'btn ghost', '←&nbsp; Back to the three packages');
}

const [P1, P2] = L.pages;
p1(P1); p2shortlist(P2); p2plan(P2);
</script>
</body>
</html>
"""

out = HTML.replace("__LAYOUT__", json.dumps(layout)).replace("__DATA__", json.dumps(data)).replace("__LOCKUP__", lockup)
(PROTO / "opzet-goodnight-inn.html").write_text(out, encoding="utf-8", newline="\n")
print("written", PROTO / "opzet-goodnight-inn.html", len(out) // 1024, "KB")
