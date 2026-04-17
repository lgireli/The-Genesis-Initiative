---
description: Quick Flow Workflow - Rapid Solo Development Path
version: 1.0.0
generated: 2026-04-10
scope: Bug fixes, small changes, solo dev work with minimum ceremony
---

# Quick Flow Workflow

> **Purpose:** Handle simple requests with minimum ceremony -- bug fixes, small changes, solo dev work.
> **Input:** User request classified as FIX, simple ENHANCE, or trivial BUILD
> **Output:** Working code change with self-review and P0/P1 validation
> **Exit:** Implementation complete, self-review passed, P0/P1 validation passed

---

## 1. Eligibility Criteria

**ALL of the following must be true for Quick Flow:**

- [ ] Single story or < 2 days of effort
- [ ] No architectural changes required (see definition below)
- [ ] No security implications (no auth, user data, payment, API changes)
- [ ] Clear acceptance criteria provided
- [ ] No cross-domain changes needed (single agent can handle)

**If ANY check fails -> Use Full BMAD**
**When in doubt -> Use Full BMAD (safer to over-engineer process)**

### Definition of Architectural Changes

Architectural changes include ANY of the following and render a request **ineligible** for Quick Flow:
- Adding, removing, or upgrading project dependencies
- Changing data models or database schemas
- Introducing new services, layers, or modules
- Altering authentication or authorization patterns
- Modifying the project structure
- Changing API contracts or communication protocols
- Introducing new external service integrations

---

## 2. Activated Agents

| Agent | Canonical ID | Persona | Role | Key Skills |
|-------|-------------|---------|------|------------|
| Quick Flow Dev | `bmad-agent-quick-flow-solo-dev` (Barry) | Barry | Rapid implementation, minimum ceremony | `bmad-quick-dev` |
| Debugger | `debugger` | -- | Root cause analysis (for bug fixes) | Systematic debugging |

---

## 3. Workflow Steps

Execute `bmad-quick-dev`:

| Step | Name | Description | Key Actions |
|------|------|-------------|-------------|
| **1** | **Clarify and Route** | Understand the request, select implementation approach | Confirm scope with user (Socratic Gate Tier 1 if needed). Identify files to touch. Select implementation approach. |
| **2** | **Plan** | Quick implementation plan (minimal documentation) | State the plan verbally or in a brief note. Identify dependencies. Identify risks. **C6 satisfied by articulating plan before coding.** |
| **3** | **Implement** | Direct code changes following existing conventions | Follow Red-Green-Refactor discipline for any non-trivial change (>1 line). Write tests. Run tests. Verify pass. |
| **4** | **Review** | Self-review of changes | Walk through diff. Check for: security issues, edge cases, error handling, code quality. Verify against acceptance criteria. |
| **5** | **Present** | Summary of what was done | Summarize: files changed, tests added, acceptance criteria met. Provide next steps if any. |

### Oneshot Option

For trivial changes (single-line fixes, obvious corrections):
- Combine all 5 steps into a single execution
- Still follow RGR discipline for non-trivial changes
- Still run P0/P1 validation before presenting

---

## 4. Quick Flow Quality Gate

After Step 4 (Review), run validation:

1. Run P0 (security scan): `python execution/checklist.py .` (checks P0-P1 only)
2. If P0 or P1 fails:
   - Present specific failure details to user
   - Offer to fix within Quick Flow (if fixable in < 30 minutes)
   - If not quickly fixable, **offer escalation to Full BMAD**:
     ```
     "Quick Flow validation failed. This issue requires more extensive analysis.
     Recommend escalating to Full BMAD Phase 4 for proper handling.
     Proceed with Full BMAD escalation?"
     ```
3. If P0 and P1 pass but P2-P10 have failures:
   - Log warnings
   - Present to user
   - Ask whether to proceed or fix

---

## 5. Skill Availability Check

Before invoking any skill, verify it exists:

```
Check: .agent/skills/{skill-name}/ exists
If missing: HALT with message "Skill {skill-name} not installed. Please install or confirm manual execution."
```

**Required skills for this workflow:**
- `bmad-quick-dev`
- `vulnerability-scanner` (for P0 validation)
- `lint-and-validate` (for P1 validation)

---

## 6. Error Handling

| Error | Recovery |
|-------|----------|
| Change turns out to be architectural | HALT: "This change requires architectural modifications. Quick Flow not suitable. Recommend Full BMAD. Escalate?" |
| P0/P1 validation fails and not fixable in < 30 min | Offer Full BMAD escalation (Section 4) |
| Multiple files/domains affected | HALT: "Cross-domain changes detected. Quick Flow not suitable. Recommend Full BMAD. Escalate?" |
| Security implications discovered | HALT: "Security implications discovered. Quick Flow not suitable. Recommend Full BMAD with security-auditor. Escalate?" |
| Context overflow risk | Checkpoint save, request continuation |

---

## 7. Escalation to Full BMAD

When Quick Flow is not suitable:

1. Present specific reason for escalation
2. Get user confirmation
3. Transition to Full BMAD:
   - Classify request appropriately (BUILD/ENHANCE/FIX)
   - Route to appropriate phase per `_routing.md`
   - Document what was attempted in Quick Flow
4. Proceed through Full BMAD workflow

---

## 8. Next Steps

After Quick Flow completes successfully:
- Present summary to user (Step 5)
- If user confirms acceptance: done
- If user reports issues: re-enter Quick Flow or escalate to Full BMAD
- If more work needed: classify new request, re-enter routing

---

*End of Quick Flow Workflow. For Full BMAD implementation, see `directives/procedures/implementation.md`. For validation, see `directives/procedures/validation.md`. For master workflow, see `directives/Ultimate-Workflow.md`.*
