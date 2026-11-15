// Build step 12 of doc 23: drive the PUBLISHED report (Publish to Web link) in headless Edge, signed out, in a chosen
// browser locale and window size. One fresh browser profile per run, so nothing of a signed-in session leaks in.
// usage: node web.mjs <url> <steps.json> [--lang nl-NL] [--w 1920] [--h 1080] [--dsf 1] [--touch] [--port 9444]
// steps: {"op":"wait","ms":3000} | {"op":"ready"}  (waits until the report page has visuals and no spinner)
//        {"op":"eval","js":"..."} | {"op":"shot","out":"x.png"} | {"op":"pagebox"}
//        {"op":"pshot","out":"x.png","scale":1}             screenshot clipped to the report page
//        {"op":"pmove","lx":100,"ly":200}                   mouse to LOGICAL page coordinates (1920 x 1080 page)
//        {"op":"pclick","lx":100,"ly":200} | {"op":"ptap","lx":100,"ly":200}  (ptap = one touch)
//        {"op":"key","key":"Tab"} | {"op":"focus"}          focus = what holds the keyboard focus (role, name)
//        {"op":"tabto","match":"regex","max":90}            Tab until the focused element's name matches (review round 2)
//        {"op":"texts","out":"x.txt"}                       every visible text of the page, one per line
import fs from "fs";
import os from "os";
import path from "path";
import { spawn } from "child_process";

const argv = process.argv.slice(2);
const opt = (n, d) => (argv.includes(n) ? argv[argv.indexOf(n) + 1] : d);
const [URL_, STEPS] = argv;
const LANG = opt("--lang", "en-US"), W = +opt("--w", 1920), H = +opt("--h", 1080), DSF = +opt("--dsf", 1);
const PORT = +opt("--port", 9444), TOUCH = argv.includes("--touch");
const EDGE = process.env.EDGE_PATH || "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe";
const profile = fs.mkdtempSync(path.join(os.tmpdir(), "p2w-"));
const sleep = ms => new Promise(r => setTimeout(r, ms));

const edge = spawn(EDGE, ["--headless=new", `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`,
  `--lang=${LANG}`, `--accept-lang=${LANG}`, `--window-size=${W},${H}`, "--no-first-run", "--hide-scrollbars",
  "about:blank"], { stdio: "ignore" });
let list;
for (let i = 0; i < 40 && !list; i++) {
  try { list = await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json(); } catch { await sleep(250); }
}
const target = list.find(t => t.type === "page");
const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
let id = 0;
const pending = new Map();
ws.onmessage = ev => {
  const m = JSON.parse(ev.data);
  if (m.id && pending.has(m.id)) { const { res, rej } = pending.get(m.id); pending.delete(m.id); m.error ? rej(new Error(JSON.stringify(m.error))) : res(m.result); }
};
const send = (method, params = {}) => new Promise((res, rej) => { const i = ++id; pending.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params })); });
const evaluate = async js => {
  const r = await send("Runtime.evaluate", { expression: js, returnByValue: true, awaitPromise: true });
  if (r.exceptionDetails) throw new Error("eval: " + JSON.stringify(r.exceptionDetails).slice(0, 400));
  return r.result.value;
};
const log = o => console.log(JSON.stringify(o));

// .displayArea is the report page plus a 20 px strip on top, in the service as in Desktop (measured 14 Nov: 1920 x
// 1100 at y 10 in a 1920 x 1180 window, the logo 30 px under the window's top): the page is its bottom w * 9/16.
const PAGEBOX_JS = `(() => { const d = document.querySelector('.displayArea'); if (!d) return null;
  const r = d.getBoundingClientRect(); const h = r.width * 1080 / 1920;
  return { x: r.x, y: r.y + (r.height - h), w: r.width, h }; })()`;
const READY_JS = `(() => ({ visuals: document.querySelectorAll('.visualContainer, visual-container').length,
  busy: document.querySelectorAll('.spinner, .powerbi-spinner, .circle').length }))()`;
const TEXTS_JS = `(() => { const out = []; const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let n = w.nextNode(); n; n = w.nextNode()) { const t = n.nodeValue.trim(); if (!t) continue;
    const e = n.parentElement; const r = e.getBoundingClientRect(); if (r.width && r.height) out.push(t); }
  document.querySelectorAll('[aria-label]').forEach(e => out.push('aria: ' + e.getAttribute('aria-label')));
  return out; })()`;
// Which report the link really shows: its name in the service, when it was last published, its pages. The page's
// own public call (modelsAndExploration) is asked again with the link's key; run it after "ready".
const KEY = (() => { try { return JSON.parse(Buffer.from(new URL(URL_).searchParams.get("r"), "base64").toString()).k; } catch { return ""; } })();
const META_JS = `(async () => { const u = performance.getEntriesByType('resource').map(e => e.name).find(n => /public\\/reports.*modelsAndExploration/.test(n));
  if (!u) return { error: 'no modelsAndExploration call seen' };
  const j = await (await fetch(u, { headers: { 'X-PowerBI-ResourceKey': '${KEY}' } })).json();
  const r = (j.exploration || {}).report || {};
  return { report: r.displayName, lastPublished: r.lastUpdatedTime, reportId: r.objectId,
    pages: ((j.exploration || {}).sections || []).map(s => s.displayName) }; })()`;
const VK = { Tab: 9, Enter: 13, Escape: 27, " ": 32, ArrowLeft: 37, ArrowUp: 38, ArrowRight: 39, ArrowDown: 40 };
const FOCUS_JS =`(() => { let e = document.activeElement; while (e && e.shadowRoot && e.shadowRoot.activeElement) e = e.shadowRoot.activeElement;
  return e ? { tag: e.tagName, role: e.getAttribute('role'), name: (e.getAttribute('aria-label') || e.innerText || '').slice(0, 120) } : null; })()`;

try {
  await send("Emulation.setLocaleOverride", { locale: LANG }).catch(() => {});
  // --lang alone leaves navigator.languages on the Windows list (measured: "nl" in a de-DE run). The user-agent
  // override carries the Accept-Language header and navigator.language(s); the locale override carries Intl.
  const ua = (await send("Browser.getVersion")).userAgent.replace("Headless", "");
  await send("Emulation.setUserAgentOverride", { userAgent: ua, acceptLanguage: LANG });
  await send("Emulation.setDeviceMetricsOverride", { width: W, height: H, deviceScaleFactor: DSF, mobile: TOUCH });
  if (TOUCH) await send("Emulation.setTouchEmulationEnabled", { enabled: true, maxTouchPoints: 1 });
  await send("Page.enable");
  await send("Page.navigate", { url: URL_ });
  log({ op: "open", lang: await evaluate("navigator.language"), w: W, h: H, touch: TOUCH });
  let box = null;
  const pt = async s => { if (!box) box = await evaluate(PAGEBOX_JS); return [box.x + s.lx * box.w / 1920, box.y + s.ly * box.h / 1080]; };
  for (const s of JSON.parse(fs.readFileSync(STEPS, "utf8"))) {
    switch (s.op) {
      case "wait": await sleep(s.ms); break;
      case "ready": {
        let st, same = 0, last = -1;
        for (let i = 0; i < 90 && same < 4; i++) { await sleep(1000); st = await evaluate(READY_JS); same = st.visuals > 0 && st.visuals === last ? same + 1 : 0; last = st.visuals; }
        box = null; log({ op: "ready", ...st, lang: await evaluate("navigator.language") }); break;
      }
      case "eval": log({ op: "eval", value: await evaluate(s.js) }); break;
      case "evalfile": { const v = await evaluate(fs.readFileSync(s.file, "utf8")); fs.writeFileSync(s.out, JSON.stringify(v), "utf8"); log({ op: "evalfile", out: s.out }); break; }
      case "meta":log({ op: "meta", ...(await evaluate(META_JS)) }); break;
      case "pagebox": box = await evaluate(PAGEBOX_JS); log({ op: "pagebox", box }); break;
      case "shot": { const r = await send("Page.captureScreenshot", { format: "png" });
        fs.writeFileSync(s.out, Buffer.from(r.data, "base64")); log({ op: "shot", out: s.out }); break; }
      case "pshot": { if (!box) box = await evaluate(PAGEBOX_JS);
        const r = await send("Page.captureScreenshot", { format: "png", clip: { x: box.x, y: box.y, width: box.w, height: box.h, scale: s.scale ?? 1 } });
        fs.writeFileSync(s.out, Buffer.from(r.data, "base64")); log({ op: "pshot", out: s.out, box }); break; }
      case "pmove": { const [x, y] = await pt(s); await send("Input.dispatchMouseEvent", { type: "mouseMoved", x, y }); log({ op: "pmove", x, y }); break; }
      case "pclick": { const [x, y] = await pt(s);
        await send("Input.dispatchMouseEvent", { type: "mouseMoved", x, y }); await sleep(150);
        await send("Input.dispatchMouseEvent", { type: "mousePressed", x, y, button: "left", clickCount: 1 }); await sleep(80);
        await send("Input.dispatchMouseEvent", { type: "mouseReleased", x, y, button: "left", clickCount: 1 }); log({ op: "pclick", x, y }); break; }
      case "ptap": { const [x, y] = await pt(s);
        await send("Input.dispatchTouchEvent", { type: "touchStart", touchPoints: [{ x, y }] }); await sleep(80);
        await send("Input.dispatchTouchEvent", { type: "touchEnd", touchPoints: [] }); log({ op: "ptap", x, y }); break; }
      case "key": { const k = { key: s.key, code: s.code ?? s.key, windowsVirtualKeyCode: s.vk ?? VK[s.key] ?? 0, modifiers: (s.shift ? 8 : 0) | (s.ctrl ? 2 : 0) };
        await send("Input.dispatchKeyEvent", { type: "keyDown", ...k }); await send("Input.dispatchKeyEvent", { type: "keyUp", ...k }); break; }
      // review round 2, step E (J-AC-8): Tab until the focused element's name matches, so a walk can step INTO a visual
      case "tabto": { const re = new RegExp(s.match, "i"); const k = { key: "Tab", code: "Tab", windowsVirtualKeyCode: 9, modifiers: 0 }; let hit = null, n = 0;
        while (n < (s.max ?? 90) && !hit) { await send("Input.dispatchKeyEvent", { type: "keyDown", ...k }); await send("Input.dispatchKeyEvent", { type: "keyUp", ...k }); n++; await sleep(350);
          const f = await evaluate(FOCUS_JS); if (f && re.test(f.name || "")) hit = f; }
        log({ op: "tabto", match: s.match, presses: n, value: hit }); break; }
      case "focus": log({ op: "focus", value: await evaluate(FOCUS_JS) }); break;
      case "texts": { const t = await evaluate(TEXTS_JS); fs.writeFileSync(s.out, t.join("\n"), "utf8"); log({ op: "texts", out: s.out, n: t.length }); break; }
      default: throw new Error("unknown op " + s.op);
    }
  }
} finally {
  await send("Browser.close").catch(() => {});
  ws.close();
  setTimeout(() => { try { edge.kill(); } catch {} try { fs.rmSync(profile, { recursive: true, force: true }); } catch {} process.exit(0); }, 1500);
}
