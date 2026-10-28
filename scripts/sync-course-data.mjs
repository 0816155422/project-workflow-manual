#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { validateDocument, scanSecrets } from "./validate-course-data.mjs";

function fail(message) { console.error(`BLOCKED: ${message}`); process.exit(1); }
const args = Object.fromEntries(process.argv.slice(2).map((arg, index, all) => arg.startsWith("--") ? [arg.slice(2), all[index + 1]] : null).filter(Boolean));
const source = args.source || process.env.SOURCE_PATH || "";
const target = args.target || process.env.TARGET_PATH || "";
const note = args.approvalNote || process.env.APPROVAL_NOTE || "";
const actor = args.actor || process.env.GITHUB_ACTOR || "";
const timestamp = args.timestamp || process.env.APPROVED_AT || new Date().toISOString();
if (process.env.GITHUB_ACTIONS !== "true" || process.env.GITHUB_EVENT_NAME !== "workflow_dispatch") fail("sync must run only inside the manually dispatched GitHub Actions approval workflow.");
if (!source.startsWith("pending/")) fail("source must start with pending/.");
if (!(target.startsWith("shared/") || target.startsWith("data/"))) fail("target must start with shared/ or data/.");
if ([source, target].some(p => p.includes("..") || p.includes("\\") || /[\\r\\n]/.test(p) || p.startsWith("/") || p.split("/").some(part => !part || part === "."))) fail("unsafe path syntax.");
if (!source.endsWith(".json") || !target.endsWith(".json")) fail("only JSON files are supported.");
if (!["shared/course/course-data.json", "data/course/course-data.json"].includes(target)) fail("target must be shared/course/course-data.json or data/course/course-data.json.");
if (!note.trim() || note.length > 300 || /[\r\n]/.test(note)) fail("approval note must be a single line of 1-300 characters.");
if (!actor.trim()) fail("actor is required.");
if (!/^\d{4}-\d{2}-\d{2}T/.test(timestamp) || Number.isNaN(Date.parse(timestamp))) fail("approval timestamp is invalid.");
for (const candidate of [source, target, "shared/course/course-data.json", "data/course/course-data.json", "hap-aicc/data/course-data.json"]) {
  let current = "";
  for (const part of candidate.split("/")) {
    current = current ? `${current}/${part}` : part;
    if (fs.existsSync(current) && fs.lstatSync(current).isSymbolicLink()) fail(`symlink path component: ${current}`);
  }
}
if (!fs.existsSync(source) || !fs.statSync(source).isFile()) fail("source must exist and be a regular file.");
for (const finalPath of ["shared/course/course-data.json", "data/course/course-data.json", "hap-aicc/data/course-data.json"]) {
  if (fs.existsSync(finalPath)) fail(`refusing overwrite; final path already exists: ${finalPath}`);
}
const raw = fs.readFileSync(source, "utf8");
let document;
try { document = JSON.parse(raw); } catch (error) { fail(`source JSON is invalid: ${error.message}`); }
const sourceErrors = validateDocument(document);
if (sourceErrors.length) fail(`source validation failed: ${sourceErrors.join("; ")}`);
document.status = "approved";
document.approvedBy = actor;
document.approvedAt = timestamp;
document.approvalNote = note;
const finalErrors = validateDocument(document, { requireApproved: true });
if (finalErrors.length) fail(`approved document validation failed: ${finalErrors.join("; ")}`);
const output = JSON.stringify(document, null, 2) + "\n";
for (const finalPath of ["shared/course/course-data.json", "data/course/course-data.json", "hap-aicc/data/course-data.json"]) {
  fs.mkdirSync(path.dirname(finalPath), { recursive: true });
  fs.writeFileSync(finalPath, output, { flag: "wx" });
}
console.log(JSON.stringify({ status: "approved", actor, source, target, mirroredTo: ["shared/course/course-data.json", "data/course/course-data.json", "hap-aicc/data/course-data.json"], records: document.records.length, approvedAt: timestamp }, null, 2));
