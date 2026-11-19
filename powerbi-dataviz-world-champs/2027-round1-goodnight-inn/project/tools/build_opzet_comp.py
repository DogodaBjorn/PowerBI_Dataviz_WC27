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
.rule{position:absolute;width:1px;background:var(--hair)}
.kick{font-size:13px;line-height:24px;letter-spacing:.08em;color:var(--accent);font-weight:bold}
.kpi .lab{font-size:13px;line-height:20px;color:var(--ink2)}
.kpi .val{font-family:var(--display);font-size:37px;line-height:44px;font-weight:bold;color:var(--ink)}
.kpi .ctx{font-size:13px;line-height:20px;color:var(--ink2);white-space:nowrap}
.folio table{font-size:13px}.folio th{height:28px;font-size:12px}.folio td{height:26px}
.folio td.keep{font-weight:bold;border-bottom:none}
.figs{display:flex;gap:24px}.figs div{flex:1}
.figs b{display:block;font-family:var(--display);font-size:28px;line-height:36px}
.figs span{display:block;font-size:13px;line-height:20px;color:var(--ink2)}
.recn{display:flex;gap:16px}.recn div{flex:1}
.recn b{display:block;font-family:var(--display);font-size:28px;line-height:40px;white-space:nowrap}
.recn span{display:block;font-size:13px;line-height:18px;color:var(--ink2)}
.alt{font-size:14px;line-height:20px;color:var(--ink)}.alt b{color:var(--ink)}
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
const FOOTER = "Source: Pillow & Key Group dataset, Power BI Dataviz World Champs 2027. Guest scores weighted by survey responses. 2021 is a depressed base year.";
const FOOTER2 = "Source: Pillow & Key Group dataset and its FinanceParameters (ramp-up, 8% discount rate, impact horizon 2032). Package values are scenario logic, labelled Low, Expected and High.";

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
  const y = G.y2025, y21 = G.y2021, y23 = G.y2023, t = G.trend;
  const others = key => BR.slice(1).map(b => F.brands[b].y2025[key]);
  place(s, S.z_masthead, 'mast', 'THE BRAND REVIEW &nbsp;·&nbsp; 2021 TO 2025 &nbsp;·&nbsp; FOR THE BOARD OF PILLOW &amp; KEY GROUP');
  place(s, S.z_headline, 'head', 'Full rooms, a slipping margin: Goodnight Inn pays the middleman and is losing its guests.');
  place(s, S.c_subtitle, 'sub', 'Goodnight Inn in 2025, against the three other Pillow &amp; Key Group brands.');
  // the KPI band: one value, one comparison each (DC-051), drawn as one card with hairline rules, not four cards
  const kpi = (slot, lab, val, ctx) => place(s, slot, 'kpi', `<div class="lab">${lab}</div><div class="val">${val}</div><div class="ctx">${ctx}</div>`, lab + ' ' + val + ', ' + ctx);
  const [rOcc] = rankText('occupancy', 1), [rMar] = rankText('gop_margin_after', 1), [rOta] = rankText('ota_share', -1), [rNps] = rankText('nps', 1);
  const sig1 = v => sgn(v, Math.abs(v).toFixed(1));
  kpi(S.kpi_occ, 'Occupancy', pct(y.occupancy), `${rOcc} · the others ${pct(Math.min(...others('occupancy')))} to ${pct(Math.max(...others('occupancy')))}`);
  kpi(S.kpi_margin, 'Operating margin after commissions', pct(y.gop_margin_after), `${rMar} · ${sgn(y.gop_margin_after - y23.gop_margin_after, Math.abs((y.gop_margin_after - y23.gop_margin_after)*100).toFixed(1) + ' pt')} since 2023`);
  kpi(S.kpi_ota, 'Room revenue booked through online agencies', pct(y.ota_share), `${rOta.replace('last', 'highest')} · ${pct(y21.ota_share)} in 2021`);
  kpi(S.kpi_nps, 'Net promoter score', sig1(y.nps), `${rNps} · the others ${sig1(Math.min(...others('nps')))} to ${sig1(Math.max(...others('nps')))}`);
  // the three findings, one chart each
  place(s, S.c_f1_kicker, 'kick', 'F1 · THE MARGIN');
  place(s, S.c_f1_title, 'title', `After commissions, the margin fell from ${pct(t[2023].gop_margin_after)} to ${pct(t[2025].gop_margin_after)}`);
  { const g0 = (t[2021].gop_margin - t[2021].gop_margin_after)*100, g1 = (t[2025].gop_margin - t[2025].gop_margin_after)*100;
    place(s, S.c_f1_note, 'cap', `Before commissions Goodnight Inn still has the widest margin of the four. The gap, what the booking channels take, grew from ${g0.toFixed(1)} to ${g1.toFixed(1)} points since 2021.`); }
  place(s, S.c_f2_kicker, 'kick', 'F2 · THE MIDDLEMAN');
  place(s, S.c_f2_title, 'title', `Online agencies now book ${pct(y.ota_share, 0)} of room revenue, up from ${pct(y21.ota_share, 0)}`);
  { const o = F.folio['Online Travel Agencies'], d = F.folio['Direct Website & App'], m = v => '$' + v.toFixed(2);
    place(s, S.tbl_f2_folio, 'folio', `<table><thead><tr><th style="text-align:left">One room night, 2025</th><th>Via an online agency</th><th>Direct, web and app</th></tr></thead><tbody>`
      + `<tr><td class="l">The guest pays</td><td>${m(o.adr)}</td><td>${m(d.adr)}</td></tr>`
      + `<tr><td class="l">Commission and fees</td><td>${MINUS}${m(o.dist)}</td><td>${MINUS}${m(d.dist)}</td></tr>`
      + `<tr><td class="l keep">Goodnight Inn keeps</td><td class="keep">${m(o.kept)}</td><td class="keep">${m(d.kept)}</td></tr></tbody></table>`, 'One room night by channel'); }
  place(s, S.c_f2_note, 'cap', `The guest pays about the same either way. At the 2021 channel mix, 2025 commissions would have been ${usdM(F.counterfactual_2021_mix)} lower.`);
  place(s, S.c_f3_kicker, 'kick', 'F3 · THE FADING WELCOME');
  const AB = F.age_bands, old = AB[AB.length - 1];
  place(s, S.c_f3_title, 'title', `Hotels last renovated ${old.band} ago score NPS ${sig1(old.nps)}`);
  { const sl = S.ch_f3_age, sv = svg(sl.w, sl.h), top0 = 24, bot = sl.h - 48, n = AB.length, bw = (sl.w - 32) / n;
    const vals = AB.map(a => a.nps), mn = Math.min(0, ...vals) - 2, mx = Math.max(0, ...vals) + 2, Y = v => bot - (v - mn)/(mx - mn)*(bot - top0);
    add(sv,'line',{x1:0,x2:sl.w,y1:Y(0),y2:Y(0),stroke:C.ink2});
    AB.forEach((a, i) => { const x = 16 + i*bw + bw*.2, w = bw*.6, last = i === n - 1;
      add(sv,'rect',{x, y:Math.min(Y(0), Y(a.nps)), width:w, height:Math.max(2, Math.abs(Y(a.nps) - Y(0))), fill:last ? C.accent : C.neutral});
      add(sv,'text',{x:x + w/2, y:(a.nps >= 0 ? Y(a.nps) - 8 : Y(a.nps) + 20), 'font-size':15, 'font-weight':'bold', 'text-anchor':'middle', fill:last ? C.accent : C.ink}, sig1(a.nps));
      add(sv,'text',{x:x + w/2, y:sl.h - 26, 'font-size':13, 'text-anchor':'middle', fill:C.ink}, a.band);
      add(sv,'text',{x:x + w/2, y:sl.h - 8, 'font-size':12, 'text-anchor':'middle', fill:C.ink2}, a.hotels + ' hotels'); });
    place(s, sl, '', '', 'Net promoter score by years since the last renovation').appendChild(sv); }
  place(s, S.c_f3_note, 'cap', `Occupancy is the same in every group (${pct(Math.min(...AB.map(a=>a.occ)),0)} to ${pct(Math.max(...AB.map(a=>a.occ)),0)}): age costs loyalty, not yet rooms. An association, not proof of cause.`);
  // F4
  const L1 = F.location, top = [...F.hotels].sort((a,b) => b.occ - a.occ).slice(0, 7), nAir = top.filter(h => h.type === 'Airport').length;
  place(s, S.c_f4_kicker, 'kick', 'F4 · WHERE WE ARE FULL');
  place(s, S.c_f4_title, 'title', `The airports are the fullest at ${pct(L1.Airport.occ)}, and ${nAir} of the 7 fullest hotels are airports`);
  place(s, S.c_f4_types, 'figs', ['Airport','City','Highway'].map(k => `<div><b>${pct(L1[k].occ)}</b><span>${k} hotels</span></div>`).join(''), 'Occupancy by location type');
  // as the report draws it: value axis from 0 to 110 % (never truncate a bar axis), labels above, full names
  { const sl = S.ch_f4_fullest, sv = svg(sl.w, sl.h), n = top.length, cw = sl.w / n, top0 = 4, bot = sl.h - 24, Y = v => bot - v/1.1*(bot - top0);
    top.forEach((h, i) => { const x = i*cw + cw*.25, w = cw*.5;
      add(sv,'rect',{x, y:Y(h.occ), width:w, height:bot - Y(h.occ), fill:h.type === 'Airport' ? C.accent : C.neutral});
      add(sv,'text',{x:x + w/2, y:Y(h.occ) - 6, 'font-size':13, 'text-anchor':'middle', fill:C.ink}, pct(h.occ));
      add(sv,'text',{x:x + w/2, y:sl.h - 6, 'font-size':12, 'text-anchor':'middle', fill:C.ink}, h.name); });
    add(sv,'line',{x1:0,x2:sl.w,y1:bot,y2:bot,stroke:C.ink2});
    place(s, sl, '', '', 'The seven fullest hotels, 2025 occupancy').appendChild(sv); }
  const trend = (slot, key, title, scale, fmt) => {
    const sv = svg(slot.w, slot.h), top0 = 16, bot = slot.h - 24, left = 48, right = slot.w - 120;
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
  // F1: Goodnight Inn's margin before and after commissions; the shaded gap is what the channels take
  { const sl = S.ch_f1_margin, sv = svg(sl.w, sl.h), top0 = 28, bot = sl.h - 28, left = 48, right = sl.w - 16, yrs = [2021,2022,2023,2024,2025];
    const bef = yrs.map(yy => t[yy].gop_margin*100), aft = yrs.map(yy => t[yy].gop_margin_after*100), y0 = 25, y1 = 50;
    const X = i => left + i*(right-left)/4, Y = v => bot - (v-y0)/(y1-y0)*(bot-top0);
    for (const tk of [25,30,35,40,45,50]) { add(sv,'line',{x1:left,x2:right,y1:Y(tk),y2:Y(tk),stroke:C.hair}); add(sv,'text',{x:left-6,y:Y(tk)+4,'font-size':13,fill:C.ink2,'text-anchor':'end'},tk+'%'); }
    yrs.forEach((yy,i) => add(sv,'text',{x:X(i),y:sl.h-6,'font-size':13,fill:C.ink2,'text-anchor':'middle'},yy));
    // as the report draws it (native line chart): two lines, legend top-left, no shading or end labels
    add(sv,'polyline',{points:bef.map((v,i)=>`${X(i)},${Y(v)}`).join(' '),fill:'none',stroke:C.neutral,'stroke-width':2});
    add(sv,'polyline',{points:aft.map((v,i)=>`${X(i)},${Y(v)}`).join(' '),fill:'none',stroke:C.accent,'stroke-width':3});
    [['Before commissions', C.neutral], ['After commissions', C.accent]].forEach(([t, c], i) => { add(sv,'circle',{cx:left+6+i*170,cy:6,r:5,fill:c}); add(sv,'text',{x:left+16+i*170,y:10,'font-size':12,fill:C.ink2},t); });
    place(s, sl, '', '', 'Goodnight Inn operating margin before and after commissions, 2021 to 2025').appendChild(sv); }
  trend(S.ch_f2_ota, 'ota_share', '', 100, v => v.toFixed(0)+'%');
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
  const P3 = presets(SCEN), A = P3.A, held = 60e6 - A.capex;
  place(s, S.z_headline2, 'head', `Fund the three moves that pay: ${usdM(A.capex)} now, ${usdM(held)} held back.`);
  place(s, S.c_subtitle2, 'sub', `${SCEN} case &nbsp;·&nbsp; NPV through 2032 in 2025 dollars at 8% &nbsp;·&nbsp; nothing after 2032 is counted`);
  const posP = PK.filter(p => p.npv[SCEN] >= 0), pos = posP.length, maxCap = Math.max(...posP.map(p => p.capex));
  // same rule as the model's Scatter Title: the next whole $M above the largest (01+05+10 costs exactly $14.0M)
  place(s, S.c_scatter_title, 'title', `${pos} of ${PK.length} possible packages pay back by 2032, all of them under $${Math.floor(maxCap/1e6) + 1}M`);
  place(s, S.c_scatter_sub, 'cap', 'Each dot is a package the rules allow; above the line it pays back by 2032. Raspberry: our recommendation A. Plum-black: B and C.');
  { const sl = S.hero_packages, sv = svg(sl.w, sl.h), left = 72, right = sl.w - 16, top0 = 16, bot = sl.h - 48;
    // one fixed axis for all three scenarios, so a switch never rescales the picture (DC-034)
    const every = PK.flatMap(p => ['Low','Expected','High'].map(k => p.npv[k]/1e6));
    const x0 = 0, x1 = 60, y0 = Math.floor(Math.min(...every)/10)*10, y1 = Math.ceil(Math.max(...every)/10)*10;
    const X = v => left + (v-x0)/(x1-x0)*(right-left), Y = v => bot - (v-y0)/(y1-y0)*(bot-top0);
    for (const t of ticks(y0, y1, 8)) { add(sv,'line',{x1:left,x2:right,y1:Y(t),y2:Y(t),stroke:t===0?C.ink2:C.hair,'stroke-width':t===0?1.5:1}); add(sv,'text',{x:left-8,y:Y(t)+4,'font-size':13,fill:C.ink2,'text-anchor':'end'},(t>0?'+':t<0?MINUS:'')+'$'+Math.abs(t)+'M'); }
    for (const t of ticks(x0, x1, 6)) add(sv,'text',{x:X(t),y:bot+20,'font-size':13,fill:C.ink2,'text-anchor':'middle'},'$'+t+'M');
    add(sv,'text',{x:(left+right)/2,y:sl.h-6,'font-size':13,fill:C.ink2,'text-anchor':'middle'},'Capex of the package, $M');
    add(sv,'text',{x:16,y:(top0+bot)/2,'font-size':13,fill:C.ink2,'text-anchor':'middle',transform:`rotate(-90 16 ${(top0+bot)/2})`},'NPV through 2032, $M');
    PK.forEach(p => { if (p.id !== focus.id) add(sv,'circle',{cx:X(p.capex/1e6),cy:Y(p.npv[SCEN]/1e6),r:4,fill:C.neutral,'fill-opacity':.45}); });
    // as the report draws it (native scatter, no point labels): B and C plum-black, the recommendation raspberry
    for (const p of [P3.B, P3.C]) { if (!p || p.id === focus.id) continue;
      add(sv,'circle',{cx:X(p.capex/1e6),cy:Y(p.npv[SCEN]/1e6),r:7,fill:C.ink}); }
    add(sv,'circle',{cx:X(focus.capex/1e6),cy:Y(focus.npv[SCEN]/1e6),r:11,fill:C.accent,stroke:'#fff','stroke-width':2});
    place(s, sl, '', '', 'Scatter of all valid packages').appendChild(sv); }
  place(s, S.sl_scenario, '', `<div class="slh">Scenario</div>${['Low','Expected','High'].map(x => `<span class="chip ${x===SCEN?'on':''}">${x}</span>`).join('')}`);
  place(s, S.sl_package, '', `<div class="slh">Package in focus</div><div class="dd"><span>A · Our recommendation</span><span>▾</span></div>`);
  place(s, S.z_footer2, 'foot', FOOTER2);
}
function p2shortlist(page){
  const s = screen(page, page.name); const S = slots(page); const P3 = presets(SCEN);
  p2common(s, page, S, P3.A, 'shortlist');
  const A = P3.A, B = P3.B, C3 = P3.C, rng = p => `${sgn(p.npv.Low, Math.abs(p.npv.Low/1e6).toFixed(1))} to ${sgn(p.npv.High, Math.abs(p.npv.High/1e6).toFixed(1))}`;
  place(s, S.c_rec_title, 'title', 'Our recommendation: package A');
  place(s, S.c_rec_mix, 'mix', mix(A));
  // the texts below follow the model's measures word for word (Rec Answers, Alt B, Alt C, Not Funded)
  place(s, S.c_rec_nums, 'recn', [[usdM(A.capex),'capex'],[susdM(A.npv[SCEN]),'NPV through 2032'],[rng(A),'NPV, Low to High, $M'],[susdM(A.rr[SCEN]),'profit a year by 2032']].map(([v,l]) => `<div><b>${v}</b><span>${l}</span></div>`).join(''), 'Package A in numbers');
  place(s, S.c_rec_answers, 'cap', `Each move answers a finding on page 1: ${ids(A).map(id => SHORT[id].toLowerCase() + ' ' + ANSWERS[id]).join(', ')}. The other ${usdM(60e6 - A.capex)} is held back.`);
  place(s, S.c_alt_title, 'title', 'Considered, not recommended');
  const added = ids(B).filter(id => !ids(A).includes(id)).map(id => SHORT[id].toLowerCase()), dropped = ids(A).filter(id => !ids(B).includes(id)).map(id => SHORT[id].toLowerCase());
  place(s, S.c_alt_b, 'alt', `B · ${dropped.length ? 'With the ' + added.join(' and ') + ' instead of the ' + dropped.join(' and ') : 'A plus the ' + added.join(' and ')}: ${usdM(B.capex)}, NPV ${susdM(B.npv[SCEN])}. A guest-score effect in ${B.rated} hotels instead of ${A.rated}, for ${usdM(B.capex - A.capex)} more and a lower NPV.`);
  place(s, S.c_alt_c, 'alt', `C · With the refresh of the 10 oldest hotels: ${usdM(C3.capex)}, NPV ${susdM(C3.npv[SCEN])}. It answers F3 most directly, ${C3.npv[SCEN] < 0 ? 'but it does not pay back by 2032.' : 'and it pays back by 2032.'}`);
  const late = F.projects.filter(p => !ids(A).includes(p.id) && !ids(B).includes(p.id) && p.id !== 'GI-07' && p.npv[SCEN] < 0).map(p => SHORT[p.id].replace(' +40 rooms',' extension'));
  place(s, S.c_not_funded, 'alt', `Not funded · ${late.join(', ')}: each has a negative NPV through 2032, the airport extensions for F4 included.`);
  place(s, S.c_uncertainty, 'note', `Read with care: in the Low case no package pays back by 2032, and A ends at ${susdM(A.npv.Low)}.`);
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
  { const sl = S.ch_plan_cumulative, sv = svg(sl.w, sl.h), left = 48, right = sl.w - 24, top0 = 28, bot = sl.h - 20;
    add(sv,'text',{x:0,y:14,'font-size':13,'font-weight':'bold',fill:C.ink},'Cumulative net impact, $M · Low to High');
    const series = ['Low','Expected','High'].map(sc => cumulative(focus, sc).map(v => v/1e6)); const all = series.flat().concat([0]);
    const mn = Math.min(...all), mx = Math.max(...all); const X = i => left + i*(right-left)/5, Y = v => bot - (v-mn)/(mx-mn)*(bot-top0);
    add(sv,'line',{x1:left,x2:right,y1:Y(0),y2:Y(0),stroke:C.ink2});
    [2027,2028,2029,2030,2031,2032].forEach((y,i) => add(sv,'text',{x:X(i),y:sl.h-4,'font-size':10,'text-anchor':'middle',fill:C.ink2},y));
    for (const tk of ticks(mn, mx, 3)) add(sv,'text',{x:left-6,y:Y(tk)+4,'font-size':10,'text-anchor':'end',fill:C.ink2},(tk<0?MINUS:'')+Math.abs(tk));
    series.forEach((ser, k) => add(sv,'polyline',{points:ser.map((v,i)=>`${X(i)},${Y(v)}`).join(' '),fill:'none',stroke:C.accent,'stroke-width':k===1?2:1}));
    place(s, sl, '', '').appendChild(sv); }
  const rooms_ref = pr.includes('GI-07') ? F.refresh10.rooms : 0;
  place(s, S.c_plan_ops, 'nums', [[focus.added.toString(),'rooms added'],[rooms_ref.toLocaleString('en-US'),'rooms refreshed'],[focus.rated.toString(),'hotels, score up']].map(([v,l]) => `<div class="num"><b>${v}</b><span>${l}</span></div>`).join('').replace(/class="nums"/,''));
  const pb = payback(focus, SCEN);
  const dis = pr.includes('GI-07') ? `15% of ${F.refresh10.rooms.toLocaleString('en-US')} rooms out of service for 14 months; ` : '';
  place(s, S.c_plan_risk, 'note', `Risks: ${dis}NPV in the Low case ${susdM(focus.npv.Low)}; the cumulative net turns positive ${pb ? 'in ' + pb : 'after 2032'} (${SCEN}). Kiosks wait for the app: they start when it goes live.`);
  place(s, S.btn_back, 'btn ghost', '←&nbsp; Back to the recommendation');
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
