#!/usr/bin/env bash
set -euo pipefail

command -v jq >/dev/null || { echo "jq is required" >&2; exit 1; }

mapfile -d '' json_files < <(find config data platforms public static-site -type f -name '*.json' -print0 2>/dev/null || true)
for file in "${json_files[@]}"; do
  echo "Checking JSON: $file"
  jq empty "$file"
done

mapfile -d '' scan_files < <(find shared pending config platforms data -type f \( -name '*.md' -o -name '*.json' -o -name '*.txt' \) -print0 2>/dev/null || true)
if (( ${#scan_files[@]} > 0 )); then
  if grep -nE -i 'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|(api[_-]?key|access[_-]?token|password|client_secret)[[:space:]]*[:=][[:space:]]*[A-Za-z0-9/_+=.-]{16,}' "${scan_files[@]}"; then
    echo "Potential credential detected. Remove it and rotate it if real." >&2
    exit 1
  fi
fi

echo "JSON and heuristic secret checks passed. Manual review is still required."
