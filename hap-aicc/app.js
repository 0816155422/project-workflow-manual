(() => {
  "use strict";
  const root = document.getElementById("course-data-app");
  if (!root) return;
  const statusNode = root.querySelector("[data-course-state]");
  const recordsNode = root.querySelector("[data-course-records]");
  const allowedStatuses = new Set(["approved", "pending", "blocked", "rejected", "in_progress", "completed"]);
  const setState = (message, kind = "pending") => {
    statusNode.textContent = message;
    statusNode.dataset.kind = kind;
    statusNode.hidden = false;
  };
  const safeText = (value) => typeof value === "string" ? value : "";
  const validEvidence = (evidence) => evidence &&
    typeof evidence.runId === "string" && /^\d+$/.test(evidence.runId) &&
    typeof evidence.commitSha === "string" && /^[0-9a-f]{40}$/i.test(evidence.commitSha) &&
    typeof evidence.url === "string" &&
    /^https:\/\/github\.com\/[^/]+\/[^/]+\/actions\/runs\/\d+$/.test(evidence.url);
  function validate(data) {
    if (!data || typeof data !== "object" || Array.isArray(data)) return false;
    if (data.schemaVersion !== "1.0" || data.source !== "course-ui" || !allowedStatuses.has(data.status)) return false;
    if (!Array.isArray(data.records) || data.records.length === 0) return false;
    if (data.status === "approved" && (!safeText(data.approvedBy).trim() || !Number.isFinite(Date.parse(data.approvedAt)))) return false;
    return data.records.every(record =>
      record && typeof record === "object" &&
      ["id", "title", "category", "status", "updatedAt", "owner"].every(key => safeText(record[key]).trim()) &&
      allowedStatuses.has(record.status) && Number.isFinite(Date.parse(record.updatedAt)) && validEvidence(record.evidence)
    );
  }
  function addText(parent, tag, text, className) {
    const node = document.createElement(tag);
    node.textContent = text;
    if (className) node.className = className;
    parent.appendChild(node);
    return node;
  }
  function render(data) {
    recordsNode.replaceChildren();
    const status = safeText(data.status);
    setState(status === "approved" ? "Approved dataset loaded from repository data." :
      status === "pending" ? "Awaiting approved dataset" : `Dataset status: ${status}`, status);
    const fragment = document.createDocumentFragment();
    for (const record of data.records) {
      const card = document.createElement("article");
      card.className = "course-record";
      const badge = addText(card, "span", safeText(record.status), "course-badge");
      badge.dataset.status = safeText(record.status);
      addText(card, "h3", safeText(record.title));
      addText(card, "p", safeText(record.category), "course-meta");
      addText(card, "p", `Updated: ${new Date(record.updatedAt).toISOString()}`, "course-meta");
      addText(card, "p", `Owner: ${safeText(record.owner)}`, "course-meta");
      const evidence = document.createElement("p");
      evidence.className = "course-meta";
      const link = document.createElement("a");
      link.href = record.evidence.url;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.textContent = `GitHub Actions run ${record.evidence.runId}`;
      evidence.appendChild(link);
      card.appendChild(evidence);
      addText(card, "p", `Commit: ${record.evidence.commitSha}`, "course-small");
      fragment.appendChild(card);
    }
    recordsNode.appendChild(fragment);
  }
  async function load() {
    setState("Loading repository dataset…", "pending");
    try {
      const response = await fetch("data/course-data.json", { cache: "no-store" });
      if (!response.ok) {
        recordsNode.replaceChildren();
        setState(response.status === 404 ? "Awaiting approved dataset" : "Data unavailable or invalid", "pending");
        return;
      }
      const data = await response.json();
      if (!validate(data)) {
        recordsNode.replaceChildren();
        setState("Data unavailable or invalid", "blocked");
        return;
      }
      render(data);
    } catch {
      recordsNode.replaceChildren();
      setState("Data unavailable or invalid", "blocked");
    }
  }
  load();
})();
