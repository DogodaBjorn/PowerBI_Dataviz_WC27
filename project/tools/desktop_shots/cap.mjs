// Direct Desktop Bridge capture (report.snapshot.capture/v2 with an optional region), for review screenshots.
// usage: node cap.mjs <pid> <pageId> <scale> <out.png> [x y w h]
import { pathToFileURL } from "url";
import fs from "fs";
const lib = await import(pathToFileURL("C:/Users/TrainerBjorn/AppData/Roaming/npm/node_modules/@microsoft/powerbi-desktop-bridge-cli/dist/index.js").href);
const [pid, pageId, scale, out, x, y, w, h] = process.argv.slice(2);
const client = await new lib.BridgeClient(pid).connect(10000);
const args = { pageId, scale: Number(scale) };
if (w) args.region = { x: Number(x), y: Number(y), width: Number(w), height: Number(h) };
let res;
for (let i = 0; i < 20; i++) {
  try { res = await client.sendBridgeMethod("report.snapshot.capture/v2", args); break; }
  catch (e) { if (!e.retryable || i === 19) { console.error(JSON.stringify({ message: e.message, code: e.code, bridgeCode: e.bridgeCode, details: e.details })); process.exit(1); } await new Promise(r => setTimeout(r, e.retryAfterMs ?? 2000)); }
}
const buf = Buffer.from(res.payload, res.encoding ?? "base64");
fs.writeFileSync(out, buf);
// PNG IHDR: width at byte 16, height at byte 20
console.log(JSON.stringify({ out, width: buf.readUInt32BE(16), height: buf.readUInt32BE(20), keys: Object.keys(res).filter(k => k !== "payload") }));
client.dispose?.();
process.exit(0);
