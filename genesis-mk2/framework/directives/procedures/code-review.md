---
description: Code Review Workflow - 3-Layer Parallel Review with Triage
version: 1.0.0
generated: 2026-04-10
scope: Adversarial code review, security scanning, acceptance auditing, findings triage
---

# Code Review Workflow

> **Purpose:** Provide adversarial review of implemented stories through 3 parallel review layers.
> **Input:** Story file with Status = `review`
> **Output:** Review findings triaged by severity, resolved or documented
> **Exit:** All Critical findings resolved, story marked `done`

---

## 1. Entry Criteria

- [ ] Story Status is `review`
- [ ] Quality Gate Q3 (Definition of Done) passed
- [ ] All tasks/subtasks marked `[x]`
- [ ] File List complete

---

## 2. Activated Agents

| Agent | Canonical ID | Role | Key Skills |
|-------|-------------|------|------------|
| Security Auditor | `security-auditor` | Layer 1: Blind Hunter | Vulnerability scanning, OWASP |
| Debugger | `debugger` | Layer 2: Edge Case Hunter | Systematic edge case analysis |
| QA Engineer | `bmad-agent-qa` (Quinn) | Layer 3: Acceptance Auditor | AC coverage verification |

---

## 3. Three-Layer Parallel Review

### Layer 1: Blind Hunter (Security Focus)

**Context:** Reviewer sees ONLY the diff -- no context bias.

**Checklist:**
- [ ] SQL injection vulnerabilities (parameterized queries, ORM usage)
- [ ] Cross-site scripting (XSS) vectors (unescaped output, innerHTML)
- [ ] Authentication/authorization flaws (missing checks, privilege escalation)
- [ ] Hard-coded secrets, API keys, tokens, passwords
- [ ] Insecure data storage (plaintext passwords, unencrypted sensitive data)
- [ ] Path traversal, command injection, SSRF
- [ ] Rate limiting, input validation, CSRF protection
- [ ] Anti-patterns (code smells, technical debt introduced)

### Layer 2: Edge Case Hunter (Robustness Focus)

**Context:** Reviewer sees diff + project context.

**Checklist:**
- [ ] Null/undefined checks on all inputs and external data
- [ ] Empty collection handling (arrays, lists, query results)
- [ ] Boundary conditions (0, -1, MAX_INT, empty strings)
- [ ] Race conditions and concurrent access
- [ ] Error handling (all error paths have descriptive messages)
- [ ] Resource cleanup (file handles, connections, timers)
- [ ] Timeout handling (external API calls, database queries)
- [ ] Unicode/encoding edge cases
- [ ] Pagination limits (offset overflow, page size extremes)

### Layer 3: Acceptance Auditor (Requirements Focus)

**Context:** Reviewer sees diff + story spec + project context.

**Checklist:**
- [ ] Every Acceptance Criterion in story file is fully implemented
- [ ] Every task/subtask in story file is correctly addressed
- [ ] Tests cover every acceptance criterion
- [ ] No extra features implemented beyond story specification
- [ ] Implementation matches Dev Notes technical requirements
- [ ] File List is complete and accurate
- [ ] Only permitted story sections were modified

---

## 4. Findings Triage

All findings from all layers are normalized, deduplicated, and classified:

| Severity | Definition | Required Action |
|----------|------------|-----------------|
| **Critical** | Must fix before merge -- security vulnerability, data loss, correctness | Block merge until resolved. Re-review after fix. |
| **Important** | Should fix, deferrable with rationale | Fix or document rationale in story file. |
| **Advisory** | Consider, no action required | Acknowledge in review report, no action required. |

### Decision Needed Findings

For findings where the correct fix is ambiguous:

1. Present finding to user one-by-one with options
2. User must decide -- do NOT apply ambiguous fixes autonomously
3. HALT until user responds
4. Document user decision in story file

### Patch Findings

For findings fixable without human input:

1. Present batch of patches to user
2. User chooses: batch-apply, auto-fix, leave as action items, or walk-through
3. Apply selected option
4. Re-run validation on patched code

### Defer Findings

For findings that are pre-existing or out of scope:

1. Write to `deferred-work.md` with one-line reason
2. Do NOT fix in current story
3. Document in Change Log

### Dismiss Findings

For false positives or findings handled elsewhere:

1. Drop entirely -- do not document
2. Do NOT waste user attention on noise

---

## 5. Review Resolution Protocol

After all findings triaged:

1. **All Critical resolved?** If no, HALT until resolved.
2. **All Important resolved or documented?** If no, document rationale for deferrals.
3. **Acceptance Auditor confirms 100% AC coverage?** If no, identify gaps, fix or defer.
4. **Security scan passes (or exceptions approved)?** Run `security_scan.py`. If fails with Critical findings, HALT.

### Story Update

After review resolution:
- Write review findings and resolutions to story file under "Senior Developer Review (AI)" section
- Update Deferred Work log for any deferred findings
- If all resolved: update story Status to `done`, sprint status to `done`
- If findings require code changes: update story Status back to `in-progress`, developer addresses findings, re-review

---

## 6. Different LLM Requirement

**CRITICAL:** Run code review using a **DIFFERENT LLM** than the one that implemented the story. Different models have different blind spots.

**Fallback (if different LLM not available):**
1. Perform structured self-review using the Blind Hunter, Edge Case Hunter, and Acceptance Auditor checklists above
2. Walk through each checklist item systematically, documenting findings
3. Flag limitation in review report: "Self-review performed -- different LLM not available. Results may have model-specific blind spots."

---

## 7. Skill Availability Check

Before invoking any skill, verify it exists:

```
Check: .agent/skills/{skill-name}/ exists
If missing: HALT with message "Skill {skill-name} not installed. Please install or confirm manual execution."
```

**Required skills for this workflow:**
- `bmad-code-review`
- `vulnerability-scanner`
- `edge-case-hunter` (or equivalent analysis skill)

---

## 8. Error Handling

| Error | Recovery |
|-------|----------|
| Layer subagent fails/times out | Append layer name to `{failed_layers}`, proceed with remaining layers. If zero findings remain AND failed layers exist, warn user that review may be incomplete. |
| Zero findings from all layers | HALT -- this is suspicious. Re-analyze or ask for guidance. False negatives are a risk. |
| Story file has no Acceptance Criteria | HALT: "Cannot perform Acceptance Audit -- story has no ACs. Return to story creation." |
| Different LLM not available | Perform structured self-review, flag limitation in report (Section 6). |

---

## 9. Quality Gate Q4 Exit Criteria

- [ ] All CRITICAL findings from code review resolved
- [ ] All IMPORTANT findings resolved or documented with rationale
- [ ] Acceptance Auditor confirms 100% AC coverage
- [ ] Edge Case Hunter report reviewed and addressed
- [ ] Security scan passes (or exceptions approved by user)
- [ ] Review follow-up tasks in story marked complete

---

## 10. Next Steps

After Quality Gate Q4 passes:
- If more stories remain in sprint: return to `directives/procedures/implementation.md`, next story
- If all stories done: run full validation (`directives/procedures/validation.md`)
- Mark epic `done` when all stories in epic are `done`

---

*End of Code Review Workflow. For implementation workflow, see `directives/procedures/implementation.md`. For validation, see `directives/procedures/validation.md`. For master workflow, see `directives/Ultimate-Workflow.md`.*
