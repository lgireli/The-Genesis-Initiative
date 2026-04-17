---
description: Validation Workflow - Quality Gates and Verification Scripts
version: 1.0.0
generated: 2026-04-10
scope: Two-tier validation (Quick + Full), priority-ordered checks, timeout handling, gate failure responses
---

# Validation Workflow

> **Purpose:** Deterministic quality validation through priority-ordered script execution.
> **Input:** Code changes, stories, or completed project
> **Output:** Validation report with pass/fail/timeout per check
> **Authority:** Scripts provide deterministic validation. LLM NEVER judges quality -- scripts do.

---

## 1. Two-Tier Validation System

### Tier 1: Quick Validation (~30 seconds)

**Execute:** `python execution/checklist.py .`

| Priority | Check | Script | Blocking | Timeout |
|----------|-------|--------|----------|---------|
| **P0** | Security Scan (vulnerabilities, secrets) | `security_scan.py` | **YES** | 60 seconds |
| **P1** | Lint and Type Check (code quality) | `lint_runner.py` | **YES** | 60 seconds |
| **P2** | Schema Validation (database) | `schema_validator.py` | No | 60 seconds |
| **P3** | Test Runner (unit/integration) | `test_runner.py` | No | 60 seconds |
| **P4** | UX Audit (accessibility, psychology) | `ux_audit.py` | No | 60 seconds |
| **P5** | SEO Check (meta tags, structure) | `seo_checker.py` | No | 60 seconds |

### Tier 2: Full Verification (~3-5 minutes)

**Execute:** `python execution/verify_all.py . --url <URL>`

Includes all Tier 1 checks PLUS:

| Priority | Check | Script | Blocking | Timeout |
|----------|-------|--------|----------|---------|
| **P6** | Lighthouse Audit (Core Web Vitals) | `lighthouse_audit.py` | No | 10 minutes |
| **P7** | Playwright E2E | `playwright_runner.py` | No | 10 minutes |
| **P8** | Bundle Analysis | `bundle_analyzer.py` | No | 10 minutes |
| **P9** | Mobile Audit | `mobile_audit.py` | No | 10 minutes |
| **P10** | i18n Check | `i18n_checker.py` | No | 10 minutes |

---

## 2. Timeout Policy

| Tier | Timeout | On Timeout Action |
|------|---------|-------------------|
| **Tier 1 (P0-P5)** | 60 seconds per check | Log warning, mark check as TIMEOUT, continue. Only P0/P1 are blocking. |
| **Tier 2 (P6-P10)** | 10 minutes per check | Log warning, mark check as TIMEOUT, continue. Not blocking. |

**Key Rule:** A TIMEOUT is NOT a FAILURE. It means the check could not be validated. The workflow continues unless P0 or P1 times out (which IS blocking).

---

## 3. When to Run Validation

| Context | Tier | Trigger |
|---------|------|---------|
| **During story development (Step 7)** | Tier 1 (P0-P3 only) | After each task/subtask implementation |
| **After story complete (Gate Q3)** | Tier 1 (P0-P5) | Before marking story `review` |
| **After code review (Gate Q4)** | Tier 1 (P0-P5) | Before marking story `done` |
| **Quick Flow (after review)** | Tier 1 (P0-P1 only) | Before presenting to user |
| **Project/sprint delivery (Gate Q5, 1D)** | Tier 2 (P0-P10) | Before final delivery |
| **User requests "final checks"** | Tier 2 (P0-P10) | Full verification suite |

---

## 4. Validation Script Registry

### Master Scripts

| Script | Location | Purpose | Execution Time | Blocking on Fail |
|--------|----------|---------|----------------|-----------------|
| `checklist.py` | `execution/checklist.py` | Quick validation (P0-P5) | ~30 seconds | YES (P0, P1) |
| `verify_all.py` | `execution/verify_all.py` | Full verification (P0-P10) | ~3-5 minutes | YES (P0, P1) |

### Skill-Level Scripts

| # | Priority | Script | Location | Purpose | Blocking |
|---|----------|--------|----------|---------|----------|
| 1 | **P0** | `security_scan.py` | `.agent/skills/vulnerability-scanner/scripts/` | Vulnerability and secret scanning | **YES** |
| 2 | **P1** | `lint_runner.py` | `.agent/skills/lint-and-validate/scripts/` | Code linting and style validation | **YES** |
| 3 | P2 | `schema_validator.py` | `.agent/skills/database-design/scripts/` | Database schema validation | No |
| 4 | P3 | `test_runner.py` | `.agent/skills/testing-patterns/scripts/` | Unit and integration test execution | No |
| 5 | P4 | `ux_audit.py` | `.agent/skills/frontend-design/scripts/` | UX and accessibility audit | No |
| 6 | P5 | `seo_checker.py` | `.agent/skills/seo-fundamentals/scripts/` | SEO compliance check | No |
| 7 | P6 | `lighthouse_audit.py` | `.agent/skills/performance-profiling/scripts/` | Core Web Vitals audit | No |
| 8 | P7 | `playwright_runner.py` | `.agent/skills/webapp-testing/scripts/` | E2E browser testing | No |
| 9 | P8 | `bundle_analyzer.py` | `.agent/skills/performance-profiling/scripts/` | Bundle size analysis | No |
| 10 | P9 | `mobile_audit.py` | `.agent/skills/frontend-design/scripts/` | Mobile responsiveness audit | No |
| 11 | P10 | `i18n_checker.py` | `.agent/skills/i18n-localization/scripts/` | Internationalization check | No |

---

## 5. Gate Failure Handling

| Gate Level | Failure Response |
|------------|-----------------|
| **Quality Gate Q1 (Story Validation)** | Return to story creation. Fix story deficiencies. If unfixable, escalate to user. |
| **Quality Gate Q2 (RGR Cycle)** | Fix the failing test/implementation. If 3 consecutive failures, HALT. |
| **Quality Gate Q3 (Definition of Done)** | Address each failing DoD item. If systemic issue (e.g., architectural), HALT and escalate. |
| **Quality Gate Q4 (Code Review)** | Address all Critical findings. Document rationale for deferring Important findings. |
| **Quality Gate Q5 (Final Delivery)** | Address all blocking failures. Present non-blocking warnings to user for disposition. |
| **Validation Scripts** | P0/P1 failures = immediate HALT. P2-P10 = log warning, may proceed with documented exception. |

**Phase Exit Gate Failures (1A-1D):** Return to previous phase. Re-execute deficient steps. Maximum 2 iterations before HALT.

---

## 6. Adding New Validation Scripts

To register a new validation script:

1. Place the script in the appropriate skill directory: `.agent/skills/{skill-name}/scripts/`
2. Register it in this document (Section 4 table)
3. Add it to `execution/checklist.py` or `execution/verify_all.py` orchestration arrays
4. Define priority level (P0-P10) and whether it is blocking
5. Define timeout (60 seconds for Tier 1, 10 minutes for Tier 2)
6. Test script execution and error handling
7. Update relevant directives with the new validation requirement

---

## 7. Error Handling

| Error | Recovery |
|-------|----------|
| Script not found | Log warning, skip check, continue. Note gap in validation report. |
| Script crashes (Python error) | Treat as P0 failure (HALT) until script can be re-run successfully. Do NOT interpret crash as "no issues found." |
| Script timeout | Log warning, mark as TIMEOUT, continue. Only P0/P1 timeout is blocking. |
| Script produces unparseable output | Log warning, mark as TIMEOUT, continue. |
| P0 failure (blocking) | HALT immediately. Present specific failure details. Do NOT proceed until resolved. |
| P1 failure (blocking) | HALT immediately. Present specific failure details. Do NOT proceed until resolved. |

---

## 8. Conflict Resolution Priority

When validation checks produce conflicting results:

| Priority | Principle |
|----------|-----------|
| **1 (Highest)** | **Security** (P0) -- Security findings always win |
| **2** | **Performance** (P6-P9) -- Performance findings override convenience |
| **3 (Lowest)** | **Convenience** -- Developer convenience is lowest priority |

**Rule:** Security > Performance > Convenience. Always.

---

## 9. Validation Report Format

After validation completes, produce a structured report:

```markdown
## Validation Report

### Date: YYYY-MM-DD
### Scope: {story_id / sprint / project}

### Tier 1 Results
| Check | Status | Duration | Notes |
|-------|--------|----------|-------|
| P0 Security Scan | PASS/FAIL/TIMEOUT | Xs | {details} |
| P1 Lint/Type | PASS/FAIL/TIMEOUT | Xs | {details} |
| ... | ... | ... | ... |

### Tier 2 Results (if applicable)
| Check | Status | Duration | Notes |
|-------|--------|----------|-------|
| P6 Lighthouse | PASS/FAIL/TIMEOUT | Xs | {details} |
| ... | ... | ... | ... |

### Summary
- Total checks: N
- Passed: N
- Failed: N (blocking: N)
- Timeout: N
- Skipped: N

### Blocking Issues (if any)
1. {P0/P1 failure details}

### Non-Blocking Warnings (if any)
1. {P2-P10 failure/warning details}
```

---

## 10. Quick Reference

**During development:**
```bash
python execution/checklist.py .    # Quick check (~30s)
```

**Before delivery:**
```bash
python execution/verify_all.py . --url <URL>    # Full check (~3-5min)
```

**P0/P1 are blocking. P2-P10 are advisory.**
**Timeouts: 60s (Tier 1), 10min (Tier 2).**
**Security > Performance > Convenience.**

---

*End of Validation Workflow. For implementation workflow, see `directives/procedures/implementation.md`. For code review, see `directives/procedures/code-review.md`. For master workflow, see `directives/Ultimate-Workflow.md`.*
