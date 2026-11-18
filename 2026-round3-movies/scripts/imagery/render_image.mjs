#!/usr/bin/env node
// render_image.mjs v1 — imagery-studio module.
// On-brand generative imagery for report chrome via Gemini image generation.
// Every render is conditioned on the brand kit's real style-anchor images plus
// the profile's style spec, palette, and hard negatives, so output stays
// on-brand by construction.
//
// Zero dependencies: Node >= 18 (global fetch + Buffer), REST call only.
// Adapted from render-image.mjs in Bjorn's LinkedInContentOps pipeline
// (first-party, re-parameterized for pbi-atelier; no LCO paths remain).
//
// CLI:
//   node render_image.mjs --spec <render-spec.json> --out <file.png>
//                         [--root <dir>] [--config <config.json>] [--model <id>]
//
// Key resolution (first hit wins):
//   1. --config <path> to a JSON file { "apiKey": "...", "model": "..." }
//   2. GEMINI_CONFIG_PATH env pointing at the same JSON shape
//   3. GEMINI_API_KEY env (model via GEMINI_MODEL, default gemini-2.5-flash-image)
// No key -> exit 2 with a clear message: the report simply ships without
// generated imagery (canvas-studio SVG backgrounds are the fallback).
//
// Render spec (JSON, composed by the im-imagery skill from the kit's
// imagery-profile.yaml — see modules/imagery-studio/imagery-guide.md):
//   {
//     "scene":         "what the illustration shows (required)",
//     "style_spec":    "medium/linework/mood paragraph from the profile",
//     "palette":       { "accent": "#2563A8", "dominant": "#F5F6F8", ... },
//     "negative":      "extra negatives" | ["no ...", "no ..."],
//     "style_anchors": ["design/brand-kits/<kit>/assets/anchors/a.webp", ...],
//     "aspect_ratio":  "16:9"
//   }
// Hard rule baked in: the no-text negatives are always appended — generated
// imagery never carries words, letters, numbers, or logos.

import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { resolve, dirname, extname } from 'node:path';

function arg(name) { const i = process.argv.indexOf(`--${name}`); return i !== -1 ? process.argv[i + 1] ?? null : null; }
function info(m) { console.log(`[imagery] ${m}`); }
function die(m, code = 1) { console.error(`[imagery] ERROR: ${m}`); process.exit(code); }

const specPath = arg('spec');
const outPath  = arg('out');
const rootDir  = arg('root') ?? process.cwd();
if (!specPath || !outPath) {
  die('Usage: node render_image.mjs --spec <render-spec.json> --out <file.png> [--root <dir>] [--config <config.json>] [--model <id>]');
}
if (typeof fetch !== 'function') die('Node 18+ required (global fetch not found).');

// --- Key + model resolution -------------------------------------------------
let apiKey = null;
let cfgModel = null;
const configPath = arg('config') ?? process.env.GEMINI_CONFIG_PATH ?? null;
if (configPath) {
  if (!existsSync(configPath)) die(`config JSON not found: ${configPath}`);
  try {
    const cfg = JSON.parse(readFileSync(configPath, 'utf8'));
    apiKey   = cfg.apiKey ?? cfg.api_key ?? null;
    cfgModel = cfg.model ?? null;
  } catch (e) { die(`config JSON does not parse: ${e.message}`); }
}
if (!apiKey) apiKey = process.env.GEMINI_API_KEY ?? null;
if (!apiKey) {
  die('No Gemini API key. Set GEMINI_API_KEY, or pass --config <json> / set ' +
      'GEMINI_CONFIG_PATH to a JSON file shaped { "apiKey": "..." }. ' +
      'Not fatal to the project: skip imagery and fall back to canvas-studio backgrounds.', 2);
}
const model = arg('model') ?? process.env.GEMINI_MODEL ?? cfgModel ?? 'gemini-2.5-flash-image';

// --- Spec -------------------------------------------------------------------
if (!existsSync(specPath)) die(`render spec not found: ${specPath}`);
let spec;
try { spec = JSON.parse(readFileSync(specPath, 'utf8')); }
catch (e) { die(`render spec does not parse: ${e.message}`); }

const scene = (spec.scene ?? spec.prompt ?? '').trim();
if (!scene) die('render spec has no "scene" description to generate.');
const aspect    = spec.aspect_ratio || '16:9';
const styleSpec = (spec.style_spec ?? '').trim();

// No-text negatives are non-negotiable (design hard rule: text lives in the
// report layer, never inside generated chrome imagery).
const HARD_NEGATIVES = 'no text, no words, no letters, no numbers, no logos, no watermark, no signature';
const specNegative = Array.isArray(spec.negative) ? spec.negative.join(', ') : (spec.negative ?? '');
const negative = [specNegative, HARD_NEGATIVES].filter(Boolean).join(', ');

let paletteLine = '';
if (spec.palette && typeof spec.palette === 'object') {
  const entries = Object.entries(spec.palette).filter(([, v]) => typeof v === 'string' && v);
  if (entries.length) {
    paletteLine = entries.map(([role, hex]) => `${role} ${hex}`).join(', ');
  }
}

// The anchor images carry the visual style; the text reinforces it and pins
// palette + forbidden elements.
let promptText =
  `Create ONE ${aspect} illustration to be used as decorative page chrome in a business report.\n\n` +
  (styleSpec ? `STYLE (match the reference images exactly: same medium, linework, colours, mood): ${styleSpec}\n\n` : '') +
  (paletteLine ? `PALETTE (only these colours plus soft neutrals): ${paletteLine}\n\n` : '') +
  `SCENE: ${scene}\n\n` +
  `Do NOT include: ${negative}.\n\n` +
  `Output a single image only.`;

// --- Style anchors ------------------------------------------------------------
const mimeFor = (p) => ({ '.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg' }[extname(p).toLowerCase()] || 'image/png');
const parts = [{ text: promptText }];
let anchorsLoaded = 0;
for (const rel of (Array.isArray(spec.style_anchors) ? spec.style_anchors : [])) {
  const abs = resolve(rootDir, rel);
  if (existsSync(abs)) {
    parts.push({ inlineData: { mimeType: mimeFor(abs), data: readFileSync(abs).toString('base64') } });
    anchorsLoaded++;
  } else {
    info(`style anchor not found, skipping: ${rel}`);
  }
}
if (anchorsLoaded === 0) info('WARNING: no style anchors loaded — output may drift off-brand.');
info(`model=${model} anchors=${anchorsLoaded} aspect=${aspect}`);

// --- Gemini REST call ---------------------------------------------------------
const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`;
const body = {
  contents: [{ role: 'user', parts }],
  generationConfig: {
    responseModalities: ['IMAGE', 'TEXT'],
    imageConfig: { aspectRatio: aspect }
  }
};

let res;
try {
  res = await fetch(url, {
    method: 'POST',
    headers: { 'x-goog-api-key': apiKey, 'Content-Type': 'application/json' },
    body: JSON.stringify(body)
  });
} catch (e) { die(`Gemini request failed: ${e.message}`); }
if (!res.ok) {
  const detail = (await res.text().catch(() => '')).slice(0, 500);
  die(`Gemini returned HTTP ${res.status}: ${detail}`);
}
const json = await res.json();

// --- Save ---------------------------------------------------------------------
const outParts = json?.candidates?.[0]?.content?.parts ?? [];
const imagePart = outParts.find((p) => p?.inlineData?.data);
if (!imagePart) {
  const blockReason = json?.promptFeedback?.blockReason;
  die(blockReason
    ? `No image returned: prompt blocked (${blockReason}). Soften the scene description and retry.`
    : 'No image returned by the model. Retry once; if it persists, check the model id supports image output.');
}
const outAbs = resolve(rootDir, outPath);
mkdirSync(dirname(outAbs), { recursive: true });
writeFileSync(outAbs, Buffer.from(imagePart.inlineData.data, 'base64'));
info(`Wrote ${outAbs}`);
