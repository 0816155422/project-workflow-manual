# Security Checklist

- [ ] No API keys, tokens, passwords, private keys, cookies, or credentials
- [ ] No sensitive personal, health, financial, or identifying data
- [ ] Source and purpose documented
- [ ] Accuracy, necessity, and privacy manually reviewed
- [ ] JSON parses successfully where applicable
- [ ] Destination is under `shared/` and does not overwrite an existing file
- [ ] Approval note does not reveal sensitive information
- [ ] Workflow result, commit, and audit entry checked

Secret detection is heuristic. It can miss secrets and flag harmless text; manual review remains mandatory.