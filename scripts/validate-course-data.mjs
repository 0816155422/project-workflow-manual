#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";

const SECRET_PATTERNS = [
  /\bgh[pousr]_[A-Za-z0-9]{20,}\b/,
  /\bgithub_pat_[A-Za-z0-9_]{20,}\b/,
  /\bAKIA[0-9A-Z]{16}\b/,
  /\bASIA[0-9A-Z]{16}\b/,
  /-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----/,
  /\b(?:api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|password|passwd|secret)\s*[:=]\s*["']?[^\s"'<>]{8,}/i,
  /\bsk-[A-Za-z0-9_-]{20,}\b/
];
const STATUSES = new Set(["pending", "approved", "blocked", "rejected"]);
const RECORD_STATUSES = new Set(["pending", "in_progress", "completed", "blocked", "rejected"]);

export function scanSecrets(value, location = "$", findings = []) {
  if (typeof value === "string") {
    for (const pattern of SECRET_PATTERNS) {
      if (pattern.test(value)) findings.push(`${location}: possible secret-like value matched ${pattern}`);
    }
  } else if (Array.isArray(value)) {
    value.forEach((item, index) => scanSecrets(item, `${location}[${index}]`, findings));
  } else if (value && typeof value === "object") {
    for (const [key, item] of Object.entries(value)) scanSecrets(item, `${location}.${key}`, findings);
  }
  return findings;
}

export function validateDocument(document, options = {}) {
  const errors = [];
  if (!document || typeof document !== "object" || Array.isArray(document)) return ["Root must be a JSON object."];
  if (document.schemaVersion !== "1.0") errors.push("schemaVersion must be \"1.0\".");
  if (document.source !== "course-ui") errors.push("source must be \"course-ui\".");
  if (!STATUSES.has(document.status)) errors.push("status must be pending, approved, blocked, or rejected.");
  if (document.status === "approved") {
    if (typeof document.approvedBy !== "string" || !document.approvedBy.trim()) errors.push("approved data requires approvedBy.");
    if (typeof document.approvedAt !== "string" || Number.isNaN(Date.parse(document.approvedAt))) errors.push("approved data requires a valid approvedAt timestamp.");
  } else {
    if (!(document.approvedBy === null || typeof document.approvedBy === "string")) errors.push("approvedBy must be a string or null.");
    if (!(document.approvedAt === null || (typeof document.approvedAt === "string" && !Number.isNaN(Date.parse(document.approvedAt))))) errors.push("approvedAt must be a valid timestamp or null.");
  }
  if (!Array.isArray(document.records) || document.records.length === 0) errors.push("records must be a non-empty array.");
  if (Array.isArray(document.records)) {
    const ids = new Set();
    document.records.forEach((record, index) => {
      const p = `records[${index}]`;
      if (!record || typeof record !== "object" || Array.isArray(record)) { errors.push(`${p} must be an object.`); return; }
      for (const field of ["id", "title", "category", "status", "updatedAt", "owner"]) {
        if (typeof record[field] !== "string" || !record[field].trim()) errors.push(`${p}.${field} is required and must be a non-empty string.`);
      }
      if (typeof record.id === "string") {
        if (ids.has(record.id)) errors.push(`${p}.id duplicates another record id.`);
        ids.add(record.id);
      }
      if (typeof record.status === "string" && !RECORD_STATUSES.has(record.status)) errors.push(`${p}.status has unsupported value.`);
      if (typeof record.updatedAt === "string" && Number.isNaN(Date.parse(record.updatedAt))) errors.push(`${p}.updatedAt must be a valid date/time.`);
      const evidence = record.evidence;
      if (!evidence || typeof evidence !== "object" || Array.isArray(evidence)) {
        errors.push(`${p}.evidence is required.`);
      } else {
        if (typeof evidence.runId !== "string" || !/^\d+$/.test(evidence.runId)) errors.push(`${p}.evidence.runId must be a numeric GitHub Actions run ID string.`);
        if (typeof evidence.commitSha !== "string" || !/^[0-9a-f]{40}$/i.test(evidence.commitSha)) errors.push(`${p}.evidence.commitSha must be a 40-character commit SHA.`);
        if (typeof evidence.url !== "string" || !/^https:\/\/github\.com\/[^/]+\/[^/]+\/actions\/runs\/\d+$/.test(evidence.url)) errors.push(`${p}.evidence.url must be a GitHub Actions run URL.`);
      }
    });
  }
  const secretFindings = scanSecrets(document);
  errors.push(...secretFindings);
  if (options.requireApproved && document.status !== "approved") errors.push("This operation requires status=approved.");
  return errors;
}

function main() {
  const inputPath = process.argv[2] || "pending/course/course-source.json";
  const resolved = path.resolve(inputPath);
  if (inputPath.includes("..") || inputPath.includes("\\")) {
    console.error("BLOCKED: unsafe path syntax.");
    process.exit(2);
  }
  let document;
  try { document = JSON.parse(fs.readFileSync(resolved, "utf8")); }
  catch (error) { console.error(`INVALID JSON: ${error.message}`); process.exit(1); }
  const errors = validateDocument(document);
  if (errors.length) {
    console.error("COURSE DATA VALIDATION: FAIL");
    for (const error of errors) console.error(`- ${error}`);
    process.exit(1);
  }
  console.log("COURSE DATA VALIDATION: PASS");
  console.log(`- Input: ${inputPath}`);
  console.log(`- Status: ${document.status}`);
  console.log(`- Records: ${document.records.length}`);
  console.log("- Secret scan: no heuristic matches (not a guarantee of absence).");
}
if (process.argv[1] && import.meta.url === new URL(`file://${path.resolve(process.argv[1])}`).href) main();
