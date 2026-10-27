// HAP/AICC MCP API — stateless Streamable HTTP transport for Vercel.
const { McpServer } = require("@modelcontextprotocol/sdk/server/mcp.js");
const { StreamableHTTPServerTransport } = require("@modelcontextprotocol/sdk/server/streamableHttp.js");
const { z } = require("zod");
const crypto = require("node:crypto");

const OWNER = process.env.GITHUB_OWNER || "0816155422";
const REPO = process.env.GITHUB_REPO || "project-workflow-manual";
const BRANCH = process.env.GITHUB_BRANCH || "main";
const API_BASE = "https://api.github.com";
const LOG_PATH = "logs/mcp-audit.jsonl";

function responseText(value) {
  return { content: [{ type: "text", text: typeof value === "string" ? value : JSON.stringify(value, null, 2) }] };
}
function githubHeaders() {
  const headers = { Accept: "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "HAP-AICC-MCP" };
  if (process.env.GITHUB_TOKEN) headers.Authorization = `Bearer ${process.env.GITHUB_TOKEN}`;
  return headers;
}
async function gh(path, options = {}) {
  const res = await fetch(`${API_BASE}${path}`, { ...options, headers: { ...githubHeaders(), ...(options.headers || {}) } });
  const body = await res.text();
  let parsed; try { parsed = body ? JSON.parse(body) : {}; } catch { parsed = { message: body }; }
  if (!res.ok) throw new Error(`GitHub API ${res.status}: ${parsed.message || res.statusText}`);
  return parsed;
}
function encodeContent(s) { return Buffer.from(s, "utf8").toString("base64"); }
function decodeContent(s) { return Buffer.from(s.replace(/\n/g, ""), "base64").toString("utf8"); }
function assertWriteReady() {
  if (!process.env.GITHUB_TOKEN) throw new Error("GITHUB_TOKEN is not configured. Read/write tools and durable audit logging are disabled until configured.");
}
function safePath(path) {
  if (!path || path.startsWith("/") || path.split("/").some(p => p === ".." || p === ".") || path.includes("\\") || path.startsWith(".github/workflows/") || /(^|\/)\.env($|\.)/.test(path) || path === LOG_PATH) {
    throw new Error("Path is not allowed. Absolute paths, traversal, secrets, workflow files, and audit log paths are protected.");
  }
}
async function appendAudit(entry) {
  assertWriteReady();
  const line = JSON.stringify(entry) + "\n";
  for (let attempt = 0; attempt < 4; attempt++) {
    let current = "";
    let sha;
    try {
      const file = await gh(`/repos/${OWNER}/${REPO}/contents/${LOG_PATH}?ref=${encodeURIComponent(BRANCH)}`);
      sha = file.sha; current = decodeContent(file.content || "");
    } catch (e) {
      if (!String(e.message).includes("404")) throw e;
    }
    const body = { message: `MCP audit: ${entry.tool} (${entry.status})`, content: encodeContent(current + line), branch: BRANCH };
    if (sha) body.sha = sha;
    try {
      await gh(`/repos/${OWNER}/${REPO}/contents/${LOG_PATH}`, { method: "PUT", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
      return;
    } catch (e) {
      if (attempt === 3 || !/409|422|sha|Conflict/i.test(e.message)) throw e;
    }
  }
}
async function audited(name, details, action) {
  const id = crypto.randomUUID();
  const started = Date.now();
  let status = "success";
  let error = null;
  try {
    const result = await action();
    return result;
  } catch (e) {
    status = "error"; error = String(e.message || e).slice(0, 500);
    throw e;
  } finally {
    const record = { id, timestamp: new Date().toISOString(), tool: name, ...details, status, duration_ms: Date.now() - started, ...(error ? { error } : {}) };
    try { await appendAudit(record); } catch (auditError) {
      // Do not silently claim a durable audit trail when the append failed.
      console.error("HAP/AICC audit append failed", String(auditError.message || auditError));
    }
  }
}
function createServer() {
  const server = new McpServer({ name: "hap-aicc-project-workflow-manual", version: "1.0.0" });

  server.tool("repository_status", "Return repository identity and current branch. This call is audit-logged.", {}, async () =>
    audited("repository_status", {}, async () => {
      const r = await gh(`/repos/${OWNER}/${REPO}`);
      return responseText({ repository: r.full_name, private: r.private, default_branch: r.default_branch, branch: BRANCH, url: r.html_url });
    }));

  server.tool("list_files", "List tracked repository files. Supply a path prefix to filter. This call is audit-logged.", {
    prefix: z.string().optional().describe("Optional directory prefix, e.g. hap-aicc/ or source/")
  }, async ({ prefix = "" }) => audited("list_files", { prefix }, async () => {
    const repo = await gh(`/repos/${OWNER}/${REPO}`);
    const tree = await gh(`/repos/${OWNER}/${REPO}/git/trees/${encodeURIComponent(BRANCH)}?recursive=1`);
    return responseText({ repository: repo.full_name, branch: BRANCH, truncated: tree.truncated, files: (tree.tree || []).filter(x => x.type === "blob" && x.path.startsWith(prefix)).map(x => ({ path: x.path, size: x.size, sha: x.sha })) });
  }));

  server.tool("read_file", "Read UTF-8 content of a repository file. This call is audit-logged; file contents are not copied into the log.", {
    path: z.string().min(1).describe("Repository-relative path")
  }, async ({ path }) => audited("read_file", { path }, async () => {
    const file = await gh(`/repos/${OWNER}/${REPO}/contents/${path.split("/").map(encodeURIComponent).join("/")}?ref=${encodeURIComponent(BRANCH)}`);
    if (Array.isArray(file) || file.type !== "file") throw new Error("Path is not a file");
    const content = file.encoding === "base64" ? decodeContent(file.content || "") : file.content;
    return responseText({ path, sha: file.sha, size: file.size, content });
  }));

  server.tool("write_file", "Create or update a UTF-8 file in the repository. Writes require GITHUB_TOKEN. Sensitive paths and workflow files are protected. Every attempt is audit-logged without recording file contents.", {
    path: z.string().min(1).describe("Repository-relative file path"),
    content: z.string().describe("Complete UTF-8 file contents"),
    message: z.string().min(3).max(180).describe("Commit message")
  }, async ({ path, content, message }) => audited("write_file", { path, bytes: Buffer.byteLength(content, "utf8") }, async () => {
    assertWriteReady(); safePath(path);
    let sha;
    try {
      const old = await gh(`/repos/${OWNER}/${REPO}/contents/${path.split("/").map(encodeURIComponent).join("/")}?ref=${encodeURIComponent(BRANCH)}`);
      sha = old.sha;
    } catch (e) { if (!String(e.message).includes("404")) throw e; }
    const body = { message, content: encodeContent(content), branch: BRANCH };
    if (sha) body.sha = sha;
    const result = await gh(`/repos/${OWNER}/${REPO}/contents/${path.split("/").map(encodeURIComponent).join("/")}`, { method: "PUT", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
    return responseText({ ok: true, path, commit: result.commit?.sha, blob: result.content?.sha, bytes: Buffer.byteLength(content, "utf8") });
  }));

  server.tool("audit_log_tail", "Read the latest durable audit records from logs/mcp-audit.jsonl. This read is also logged.", {
    lines: z.number().int().min(1).max(100).optional().describe("Number of latest records to return, default 20")
  }, async ({ lines = 20 }) => audited("audit_log_tail", { lines }, async () => {
    const file = await gh(`/repos/${OWNER}/${REPO}/contents/${LOG_PATH}?ref=${encodeURIComponent(BRANCH)}`);
    const records = decodeContent(file.content || "").split("\n").filter(Boolean);
    return responseText({ path: LOG_PATH, total_records: records.length, records: records.slice(-lines).map(s => { try { return JSON.parse(s); } catch { return { raw: s }; } }) });
  }));

  return server;
}

module.exports = async function handler(req, res) {
  if (req.url === "/api/mcp/health" || req.url?.startsWith("/api/mcp/health?")) {
    res.statusCode = 200; res.setHeader("Content-Type", "application/json");
    return res.end(JSON.stringify({ ok: true, service: "HAP/AICC MCP API", version: "1.0.0", repository: `${OWNER}/${REPO}`, auth_configured: Boolean(process.env.MCP_API_KEY), github_write_configured: Boolean(process.env.GITHUB_TOKEN), audit_log: LOG_PATH }));
  }
  const expected = process.env.MCP_API_KEY;
  const auth = req.headers.authorization || "";
  if (!expected || auth !== `Bearer ${expected}`) {
    res.statusCode = 401; res.setHeader("Content-Type", "application/json");
    return res.end(JSON.stringify({ error: "unauthorized", message: "Supply a valid Authorization: Bearer <MCP_API_KEY> header." }));
  }
  if (!["GET", "POST", "DELETE"].includes(req.method)) {
    res.statusCode = 405; res.setHeader("Allow", "GET, POST, DELETE"); return res.end("Method Not Allowed");
  }
  const server = createServer();
  const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined });
  res.on("close", () => { transport.close(); server.close(); });
  try {
    await server.connect(transport);
    await transport.handleRequest(req, res, req.body);
  } catch (e) {
    console.error("HAP/AICC MCP request failed", String(e.message || e));
    if (!res.headersSent) { res.statusCode = 500; res.setHeader("Content-Type", "application/json"); res.end(JSON.stringify({ error: "internal_error" })); }
  }
};
