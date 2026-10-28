import fs from 'node:fs';
import path from 'node:path';

const root = 'raw_data/openai_research';
const manifestPath = path.join(root, 'manifest.json');
const indexPath = path.join(root, 'sources.jsonl');
const required = ['source_id','title','source_url','publisher','publish_date','category','summary','excerpt','tags','confidence_level','verification_status','notes','ingested_at'];
const allowedStatus = new Set(['Verified','Unverified']);
const allowedCategories = new Set(['model','research','safety','evaluation','multimodal','agents','policy','product','ecosystem','benchmark']);
const secretLike = /(?:gh[pousr]_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{16,}|AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)/;
const errors = [];
function fail(message) { errors.push(message); }
if (!fs.existsSync(manifestPath) || !fs.existsSync(indexPath)) {
  console.error('BLOCKED: manifest.json or sources.jsonl is missing');
  process.exit(1);
}
let manifest;
try { manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8')); } catch { fail('manifest.json is invalid JSON'); }
const lines = fs.readFileSync(indexPath, 'utf8').split(/\r?\n/).filter(line => line.trim());
const ids = new Set();
const counts = {};
let verified = 0;
let unverified = 0;
for (let i=0; i<lines.length; i++) {
  let r;
  try { r = JSON.parse(lines[i]); } catch { fail(\`sources.jsonl line \${i+1} is invalid JSON\`); continue; }
  for (const key of required) if (!(key in r)) fail(\`line \${i+1}: missing \${key}\`);
  if (typeof r.source_url !== 'string' || !/^https:\/\/(?:openai\.com|cdn\.openai\.com|arxiv\.org|platform\.openai\.com|developers\.openai\.com)(?:\/|$)/.test(r.source_url)) fail(\`line \${i+1}: source_url is not on an allowed public domain\`);
  if (!allowedStatus.has(r.verification_status)) fail(\`line \${i+1}: invalid verification_status\`);
  if (!allowedCategories.has(r.category)) fail(\`line \${i+1}: invalid category\`);
  if (!Array.isArray(r.tags)) fail(\`line \${i+1}: tags must be an array\`);
  if (typeof r.ingested_at !== 'string' || Number.isNaN(Date.parse(r.ingested_at))) fail(\`line \${i+1}: ingested_at must be a parseable timestamp\`);
  if (r.source_id && ids.has(r.source_id)) fail(\`line \${i+1}: duplicate source_id \${r.source_id}\`);
  if (r.source_id) ids.add(r.source_id);
  if (r.verification_status === 'Verified') verified++; else unverified++;
  counts[r.category] = (counts[r.category] || 0) + 1;
  if (secretLike.test(JSON.stringify(r))) fail(\`line \${i+1}: secret-like value detected\`);
  const slug = String(r.source_id || '');
  if (!/^[a-z0-9][a-z0-9-]{2,100}$/.test(slug)) fail(\`line \${i+1}: unsafe source_id\`);
  for (const file of [path.join(root,'raw',slug+'.txt'),path.join(root,'metadata',slug+'.json')]) {
    if (!fs.existsSync(file)) fail(\`line \${i+1}: missing companion file \${file}\`);
    else if (secretLike.test(fs.readFileSync(file,'utf8'))) fail(\`secret-like value detected in \${file}\`);
  }
}
if (manifest) {
  if (manifest.total_sources !== lines.length) fail('manifest total_sources does not match JSONL line count');
  if (manifest.total_verified !== verified) fail('manifest total_verified does not match JSONL');
  if (manifest.total_unverified !== unverified) fail('manifest total_unverified does not match JSONL');
  const actual = Object.fromEntries(Object.entries(counts).sort());
  const expected = Object.fromEntries(Object.entries(manifest.source_count_by_category || {}).sort());
  if (JSON.stringify(actual) !== JSON.stringify(expected)) fail('manifest source_count_by_category does not match JSONL');
}
if (errors.length) {
  console.error('VALIDATION_FAILED');
  for (const e of errors) console.error('- ' + e);
  process.exit(1);
}
console.log(JSON.stringify({status:'PASS',records:lines.length,verified,unverified,category_counts:counts},null,2));
