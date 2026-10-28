#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";

const timestamp = process.env.EVIDENCE_TIMESTAMP || new Date().toISOString();
const actor = process.env.EVIDENCE_ACTOR || process.env.GITHUB_ACTOR || "unknown";
const task = process.env.EVIDENCE_TASK || "manual evidence capture";
const status = process.env.EVIDENCE_STATUS || "Inconclusive";
const workflow = process.env.GITHUB_WORKFLOW || "manual";
const runId = process.env.GITHUB_RUN_ID || "";
const commitSha = process.env.GITHUB_SHA || "";
const server = process.env.GITHUB_SERVER_URL || "https://github.com";
const repository = process.env.GITHUB_REPOSITORY || "unknown/unknown";
const evidenceUrl = process.env.EVIDENCE_URL || (runId ? `${server}/${repository}/actions/runs/${runId}` : "");
const note = (process.env.EVIDENCE_NOTE || "Evidence captured by GitHub Actions; interpret status only from the linked run.").replace(/[\r\n]+/g, " ").slice(0, 1000);
if (!/^\d{4}-\d{2}-\d{2}T/.test(timestamp) || Number.isNaN(Date.parse(timestamp))) throw new Error("timestamp must be ISO 8601.");
if (!runId || !/^\d+$/.test(runId)) throw new Error("GITHUB_RUN_ID is required to avoid synthetic evidence.");
if (!/^[0-9a-f]{40}$/i.test(commitSha)) throw new Error("GITHUB_SHA must be a full commit SHA.");
if (!/^https:\/\//.test(evidenceUrl)) throw new Error("evidence URL must be HTTPS.");
const entry = { timestamp, actor, task, status, workflow, runId, commitSha, evidenceUrl, note };
const jsonPath = "hap-aicc/data/usage-log.json";
let records = [];
if (fs.existsSync(jsonPath)) {
  const existing = JSON.parse(fs.readFileSync(jsonPath, "utf8"));
  if (!Array.isArray(existing.entries)) throw new Error("Existing usage log must contain an entries array.");
  records = existing.entries;
}
records.push(entry);
fs.mkdirSync(path.dirname(jsonPath), { recursive: true });
fs.writeFileSync(jsonPath, JSON.stringify({ schemaVersion: "1.0", appendOnly: true, entries: records }, null, 2) + "\n");
fs.mkdirSync("logs", { recursive: true });
const md = `\n## ${timestamp} — ${task}\n- Actor: ${actor}\n- Status: ${status}\n- Workflow: ${workflow}\n- Run ID: ${runId}\n- Commit SHA: ${commitSha}\n- Evidence URL: ${evidenceUrl}\n- Note: ${note}\n`;
fs.appendFileSync("logs/usage-history.md", md);
fs.appendFileSync("logs/workflow-evidence.md", `\n## ${timestamp} — ${workflow}\n- Status: ${status}\n- Run ID: ${runId}\n- Commit SHA: ${commitSha}\n- Evidence URL: ${evidenceUrl}\n- Actor: ${actor}\n- Task: ${task}\n- Note: ${note}\n`);
console.log(`Appended real GitHub run ${runId} to usage and workflow evidence logs.`);
