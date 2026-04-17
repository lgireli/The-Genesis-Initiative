---
description: Session Start Routing - Small file loaded every session to classify requests and route to correct procedure
version: 1.0.0
generated: 2026-04-10
scope: Session initialization, request classification, procedure routing
---

# Session Routing Directive

> **Purpose:** This is the ONLY file loaded at session start (~200 lines). It classifies requests and routes to the correct procedure file.
> **Authority:** Follow this protocol exactly. Do NOT load the full Ultimate-Workflow.md unless ambiguity arises.

---

## 1. On Session Start

1. Load this file (`_routing.md`)
2. Check for existing state files (`sprint-status.yaml`, story files)
3. Check for stale transition locks in `.tmp/` (reconcile if >5 min old)
4. Check for concurrent session locks (warn if found)
5. Classify session type:

| Type | Indicators | Action |
|------|-----------|--------|
| **Fresh Start** | No state files exist | Proceed to request classification |
| **Resumption** | State files with `in-progress` story | Load story, resume from last task |
| **Continuation** | Active workflow mid-step | Present status summary + A/P/C menu |

**A/P/C Menu (at decision points):**
```
[A]dvance  - Full re-analysis from current phase start
[P]arty     - Engage multiple agents for collaborative review
[C]ontinue  - Resume from exact last known state
```

---

## 2. Core Operating Principles (Summary)

| # | Principle | Description |
|---|-----------|-------------|
| **P1** | **Tool-First** | Check `execution/` for scripts before writing code |
| **P2** | **Progressive Disclosure** | P0 > P1 > P2 priority tiers |
| **P3** | **Plan-Before-Build** | No code without a plan |
| **P4** | **Questions-Before-Assumptions** | If 1% unclear, ASK |
| **P5** | **Deterministic Validation** | Scripts handle verification, not LLM judgment |
| **P6** | **Boundary Enforcement** | Agents stay in their domains |
| **P7** | **Self-Annealing** | Failures update directives, system grows stronger |
| **P8** | **State Isolation** | `.tmp/` ephemeral, `_bmad-output/` persistent, `directives/` append-only |
| **P9** | **Multi-Speed** | Full BMAD vs Quick Flow with explicit criteria |
| **P10** | **Synthesis Over Aggregation** | Coherent artifacts, not aggregated outputs |

---

## 3. The 10 Commandments (Quick Reference)

| # | Commandment | Key Point |
|---|-------------|-----------|
| **C1** | NOT assume requirements | Clarify first |
| **C2** | NOT skip quality gates | All gates must pass |
| **C3** | NOT write outside domain | Boundaries are absolute |
| **C4** | NOT destroy without permission | Explicit confirmation required |
| **C5** | NOT expose secrets | Never log, output, or commit |
| **C6** | NOT skip the plan | No implementation before planning |
| **C7** | NOT lie about completion | Gates must actually pass |
| **C8** | NOT modify directives without permission | **Exempt for Self-Annealing updates** |
| **C9** | NOT halt silently | Communicate with specific messages |
| **C10** | Preserve and grow directives | Append-only (directives/ and workflow files only) |

**Full principles:** `directives/principles.md`

---

## 4. Request Classification

Every incoming request MUST be classified into one of these types:

| Type | Route To | Procedure File |
|------|----------|----------------|
| **BUILD** | Full BMAD Phase 1 | `procedures/analysis.md` -> `procedures/planning.md` -> `procedures/solutioning.md` -> `procedures/implementation.md` |
| **ENHANCE** | Phase 2 or Quick Flow | `procedures/planning.md` or `procedures/quick-flow.md` |
| **FIX** | Quick Flow or Phase 4 | `procedures/quick-flow.md` or `procedures/implementation.md` |
| **INVESTIGATE** | Phase 1 (Analyst) | `procedures/analysis.md` |
| **DOCUMENT** | Technical Writer | `procedures/analysis.md` (Tech Writer path) |
| **REVIEW** | Code Review / Security Audit | `procedures/code-review.md` |
| **UNKNOWN** | Default to INVESTIGATE | `procedures/analysis.md` |

### Composite Requests

If a request spans multiple types (e.g., "fix this AND build that"):
1. Split into sub-requests (one per type)
2. Process each independently through its workflow
3. Present consolidated outputs when all complete

---

## 5. Socratic Gate (Quick Reference)

| Condition | Gate Tier | Questions |
|-----------|-----------|-----------|
| New feature, major change, greenfield, ambiguous | **Tier 2 (Deep)** | Purpose/Users, Scope/Constraints, Domain-specific strategy |
| Bug fix with clear steps, small enhancement | **Tier 1 (Quick)** | What changed?, Constraints?, How to verify done? |
| Continuation of scoped work | **SKIPPED** | N/A |

**Answer Quality Bar:** Answers must be specific enough to produce actionable acceptance criteria. Generic responses ("make it fast", "just work") are treated as **unanswered**.

**Full protocol:** `directives/Ultimate-Workflow.md` Section 3

---

## 6. Mode Selection

```
IF ALL true:
  [ ] Single story or < 2 days effort
  [ ] No architectural changes (see principles.md Section 7 for definition)
  [ ] No security implications
  [ ] Clear acceptance criteria
  [ ] No cross-domain changes
THEN -> Quick Flow (`procedures/quick-flow.md`)
ELSE -> Full BMAD (phase procedure files)

When in doubt -> Full BMAD
```

---

## 7. Pre-Flight Checklist (Before ANY Implementation)

```
[ ] Request classified (BUILD/ENHANCE/FIX/INVESTIGATE/DOCUMENT/REVIEW or defaulted)
[ ] Socratic Gate completed and cleared (if new/complex)
[ ] Development mode selected (Full BMAD or Quick Flow)
[ ] Planning artifacts exist (PRD, architecture, epics for Full BMAD; PLAN.md for Quick Flow)
[ ] Skill availability verified (check .agent/skills/ before invocation)
[ ] Project type identified (WEB/MOBILE/BACKEND/FULL-STACK/API/OTHER)
[ ] Agent routing verified (see agent-matrix.md)
[ ] Relevant execution scripts available in execution/
[ ] State files loaded (sprint-status.yaml, current story if applicable)
[ ] No HALT conditions active
[ ] Session lock acquired (create .tmp/session-{id}.lock)
[ ] No stale transition locks (reconcile if found)
```

**VIOLATION:** Skipping any pre-flight check = FAILED orchestration. Stop and remediate.

---

## 8. Procedure File Routing Map

```
User Request
    |
    v
[This File: _routing.md]
    |
    +-- BUILD --------> procedures/analysis.md (Phase 1)
    |                        |
    |                        v
    |                   procedures/planning.md (Phase 2)
    |                        |
    |                        v
    |                   procedures/solutioning.md (Phase 3)
    |                        |
    |                        v
    |                   procedures/implementation.md (Phase 4)
    |
    +-- ENHANCE -----> procedures/planning.md or quick-flow.md
    |
    +-- FIX ----------> procedures/quick-flow.md or implementation.md
    |
    +-- INVESTIGATE --> procedures/analysis.md
    |
    +-- DOCUMENT ----> procedures/analysis.md (Tech Writer path)
    |
    +-- REVIEW ------> procedures/code-review.md
    |
    +-- UNKNOWN -----> procedures/analysis.md (as INVESTIGATE)
```

---

## 9. Quick HALT Reference

The workflow MUST HALT and request user guidance when:

| Condition | User Message |
|-----------|-------------|
| Ambiguous requirements | "Requirements for [X] are ambiguous. Please clarify: [specific question]" |
| Missing configuration | "Cannot proceed without [X]. Please provide or configure it." |
| 3 consecutive failures | "Failed 3 times on [X]. Stopping for guidance on approach." |
| Unauthorized changes | "This action will [DELETE/drop/consume credits]. Confirm to proceed?" |
| Story file inaccessible | "Cannot find/read story file at [path]. Please verify." |
| Unfixable test failures | "Tests failing due to [X]. This requires architectural change. How to proceed?" |
| Gate failure | "Gate [N] failed: [specific criteria]. Cannot proceed until resolved." |
| Context overflow risk | "Context window nearing capacity. Recommend checkpoint save and continuation." |

---

## 10. Quality Gates (Quick Reference)

| Gate | When | Procedure File |
|------|------|----------------|
| **Phase Gates 1A-1D** | Phase transitions | Phase-specific procedure files |
| **Quality Gate Q1** | After story creation | `procedures/implementation.md` |
| **Quality Gate Q2** | During each task (RGR) | `procedures/implementation.md` |
| **Quality Gate Q3** | After story complete (DoD) | `procedures/implementation.md` |
| **Quality Gate Q4** | After story marked review | `procedures/code-review.md` |
| **Quality Gate Q5** | At delivery | `procedures/validation.md` |

**Full gate criteria:** `directives/Ultimate-Workflow.md` Section 9, or phase-specific procedure files.

---

*End of Session Routing Directive. Load the appropriate procedure file next based on the request classification.*
