// Drive the Power BI Desktop canvas (WebView2 reportView.html) over a local DevTools port, one session per run.
// usage: node cdp.mjs <steps.json>
// steps: {"op":"metrics","w":2100,"h":1250,"dsf":1} | {"op":"wait","ms":3000} | {"op":"eval","js":"..."}
//        {"op":"shot","out":"x.png"} | {"op":"click","x":1,"y":2,"ctrl":true} | {"op":"key","key":"Escape"}
//        {"op":"pagebox"}  -> rect of the report page in CSS px (logs it and keeps it for page-relative clicks)
//        {"op":"pclick","lx":1488,"ly":988,"ctrl":true}  -> click at LOGICAL page coordinates (1920 x 1080 page)
//        {"op":"pshot","out":"x.png","scale":2}  -> screenshot clipped to the page, at the given scale
import fs from "fs";

const PORT = 9333;
const steps = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const list = await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json();
const target = list.find(t => t.type === "page" && t.url.includes("reportView.html"));
if (!target) throw new Error("reportView target not found");
const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
let id = 0;
const pending = new Map();
ws.onmessage = ev => {
  const m = JSON.parse(ev.data);
  if (m.id && pending.has(m.id)) { const { res, rej } = pending.get(m.id); pending.delete(m.id); m.error ? rej(new Error(JSON.stringify(m.error))) : res(m.result); }
};
const send = (method, params = {}) => new Promise((res, rej) => { const i = ++id; pending.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params })); });
const sleep = ms => new Promise(r => setTimeout(r, ms));
const evaluate = async js => {
  const r = await send("Runtime.evaluate", { expression: js, returnByValue: true, awaitPromise: true });
  if (r.exceptionDetails) throw new Error("eval: " + JSON.stringify(r.exceptionDetails).slice(0, 400));
  return r.result.value;
};

// The page element: the largest element whose box has the 16:9 report-page aspect (displayArea in Power BI).
const PAGEBOX_JS = `(() => {
  // .displayArea is the page plus a 20 px strip on top (visual containers start 20 px down; checked on the logo and
  // card frames 7 Nov), so the page is its full width and the bottom width*9/16.
  const d = document.querySelector('.displayArea');
  if (!d) return null;
  const r = d.getBoundingClientRect();
  const h = r.width * 1080 / 1920;
  return { x: r.x, y: r.y + (r.height - h), w: r.width, h, area: [r.x, r.y, r.width, r.height] };
})()`;

let box = null;
const out = { push: o => console.log(JSON.stringify(o)) };
for (const s of steps) {
  switch (s.op) {
    case "metrics":
      await send("Emulation.setDeviceMetricsOverride", { width: s.w, height: s.h, deviceScaleFactor: s.dsf ?? 1, mobile: false });
      out.push({ op: "metrics", w: s.w, h: s.h }); break;
    case "clearmetrics":
      await send("Emulation.clearDeviceMetricsOverride"); out.push({ op: "clearmetrics" }); break;
    case "wait": await sleep(s.ms); break;
    case "sh": {  // e.g. a bridge reload inside the same DevTools session, so the viewport override stays on
      const { execSync } = await import("child_process");
      const o = execSync(s.cmd, { encoding: "utf8", shell: "powershell.exe", timeout: 240000 });
      out.push({ op: "sh", tail: o.trim().split(/\r?\n/).slice(-3).join(" | ").slice(0, 200) }); box = null; break;
    }
    case "eval": out.push({ op: "eval", value: await evaluate(s.js) }); break;
    case "pagebox": box = await evaluate(PAGEBOX_JS); out.push({ op: "pagebox", box }); break;
    case "shot": {
      const r = await send("Page.captureScreenshot", { format: "png", captureBeyondViewport: false });
      fs.writeFileSync(s.out, Buffer.from(r.data, "base64")); out.push({ op: "shot", out: s.out }); break;
    }
    case "pshot": {
      if (!box) box = await evaluate(PAGEBOX_JS);
      const r = await send("Page.captureScreenshot", { format: "png", clip: { x: box.x, y: box.y, width: box.w, height: box.h, scale: s.scale ?? 1 } });
      fs.writeFileSync(s.out, Buffer.from(r.data, "base64")); out.push({ op: "pshot", out: s.out, box }); break;
    }
    case "click": case "pclick": case "tab": {
      let x = s.x, y = s.y;
      if (s.op === "tab") [x, y] = await evaluate(s.js);
      if (s.op === "pclick") { if (!box) box = await evaluate(PAGEBOX_JS); x = box.x + s.lx * box.w / 1920; y = box.y + s.ly * box.h / 1080; }
      const modifiers = s.ctrl ? 2 : 0;
      await send("Input.dispatchMouseEvent", { type: "mouseMoved", x, y, modifiers });
      await sleep(150);
      await send("Input.dispatchMouseEvent", { type: "mousePressed", x, y, button: "left", clickCount: 1, modifiers });
      await sleep(80);
      await send("Input.dispatchMouseEvent", { type: "mouseReleased", x, y, button: "left", clickCount: 1, modifiers });
      // Settle (batch 2, 7 Nov): a bookmark that hides the button under the cursor left Desktop's canvas in a drag,
      // and the next mouse move dragged the selected visual across the page. Release again where we are, then
      // Escape to drop the edit-mode selection, before anything moves.
      if (!s.nosettle) {
      await sleep(400);
      await send("Input.dispatchMouseEvent", { type: "mouseReleased", x, y, button: "left", clickCount: 1, modifiers: 0 });
      await send("Input.dispatchKeyEvent", { type: "keyDown", key: "Escape", code: "Escape", windowsVirtualKeyCode: 27 });
      await send("Input.dispatchKeyEvent", { type: "keyUp", key: "Escape", code: "Escape", windowsVirtualKeyCode: 27 });
      }
      out.push({ op: s.op, x: Math.round(x), y: Math.round(y), ctrl: !!s.ctrl }); break;
    }
    case "hover": case "phover": {  // mouse moves only (tooltips, hover states); phover in logical page coordinates
      let x = s.x, y = s.y;
      if (s.op === "phover") { if (!box) box = await evaluate(PAGEBOX_JS); x = box.x + s.lx * box.w / 1920; y = box.y + s.ly * box.h / 1080; }
      const from = s.from ?? 12;  // approach from a few px away so the target sees a real enter
      await send("Input.dispatchMouseEvent", { type: "mouseMoved", x: x - from, y: y - from, modifiers: 0 });
      await sleep(120);
      await send("Input.dispatchMouseEvent", { type: "mouseMoved", x, y, modifiers: 0 });
      out.push({ op: s.op, x: Math.round(x), y: Math.round(y) }); break;
    }
    case "fullshot": {  // the whole viewport (a tooltip can sit outside the page box)
      const r = await send("Page.captureScreenshot", { format: "png" });
      fs.writeFileSync(s.out, Buffer.from(r.data, "base64")); out.push({ op: "fullshot", out: s.out }); break;
    }
    case "key": {
      await send("Input.dispatchKeyEvent", { type: "keyDown", key: s.key, code: s.key, windowsVirtualKeyCode: s.vk ?? 27 });
      await send("Input.dispatchKeyEvent", { type: "keyUp", key: s.key, code: s.key, windowsVirtualKeyCode: s.vk ?? 27 });
      out.push({ op: "key", key: s.key }); break;
    }
    default: throw new Error("unknown op " + s.op);
  }
}

ws.close();
process.exit(0);

