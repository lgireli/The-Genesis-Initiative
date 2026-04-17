---
description: Phase 3 - Solutioning and Architecture (BMAD Strategic)
version: 1.0.0
generated: 2026-04-10
scope: Architecture design, epic/story decomposition, implementation readiness check
---

# Phase 3: Solutioning (BMAD Strategic)

> **Purpose:** Transform PRDs and UX specs into architecture documents, epics, and stories ready for implementation.
> **Input:** Approved `prd.md` + `ux-design.md` from Phase 2
> **Output:** `architecture.md` + `epics.md` + `readiness-report.md` + `sprint-status.yaml` + `project-context.md`
> **Exit:** Phase Gate 1C (Readiness = GO)

---

## 1. Phase Entry Criteria

- [ ] Phase Gate 1B passed (PRD + UX approved)
- [ ] User explicitly requests solutioning phase

---

## 2. Activated Agents

| Agent | Canonical ID | Persona | Role | Key Skills |
|-------|-------------|---------|------|------------|
| Architect | `bmad-agent-architect` (Winston) | Winston | Solution design, technical decisions, ADRs | `bmad-create-architecture`, `bmad-create-epics-and-stories`, `bmad-check-implementation-readiness`, `architecture`, `app-builder` |

---

## 3. Architecture Solution Design (8 Steps)

Execute `bmad-create-architecture`:

| Step | Name | Purpose |
|------|------|---------|
| 1 | **Init** | Load PRD, UX design, project context |
| 2 | **Context** | Technical environment assessment |
| 3 | **Starter Architecture** | Initial architectural sketch |
| 4 | **Decisions** | Key architectural decisions (documented as ADRs) |
| 5 | **Patterns** | Design patterns and their application |
| 6 | **Structure** | Project structure and module organization |
| 7 | **Validation** | Architecture review against PRD requirements |
| 8 | **Complete** | Architecture document finalized |

**Output:** `architecture.md` at `_bmad-output/planning-artifacts/architecture.md`
**ADRs:** Stored alongside architecture document or in `docs/adrs/`

**ADR Template:**
```markdown
# ADR-{num}: {Title}
**Status:** Proposed | Accepted | Deprecated | Superseded
**Date:** YYYY-MM-DD
**Context:** {What requires this decision?}
## Decision
{What approach are we choosing?}
## Consequences
{What becomes easier? What becomes harder?}
## Alternatives Considered
- {Alternative 1}: {Why rejected}
- {Alternative 2}: {Why rejected}
```

---

## 4. Epic and Story Decomposition (4 Steps)

Execute `bmad-create-epics-and-stories`:

| Step | Name | Purpose |
|------|------|---------|
| 1 | **Validate Prerequisites** | Confirm PRD, UX design, and Architecture documents exist |
| 2 | **Design Epics** | Group related functionality into logical epics |
| 3 | **Create Stories** | Decompose epics into user stories, each containing: user story format, acceptance criteria (measurable, testable), tasks/subtasks, dev notes |
| 4 | **Final Validation** | Coverage check: every PRD functional requirement maps to at least one story |

**Output:** `epics.md` at `_bmad-output/implementation-artifacts/epics.md`

**Story Requirements (each story must have):**
- User story format: "As a [role], I want [action], so that [benefit]"
- At least 2 measurable, testable acceptance criteria
- Tasks/subtasks covering all acceptance criteria
- Dev notes with architecture references and technical guidance
- INVEST quality: Independent, Negotiable, Valuable, Estimable, Small, Testable

---

## 5. Implementation Readiness Check (6 Steps)

Execute `bmad-check-implementation-readiness`:

| Step | Name | Purpose | Output |
|------|------|---------|--------|
| 1 | **Document Discovery** | Find all planning artifacts (PRD, UX, Architecture, Epics) | Inventory |
| 2 | **PRD Analysis** | Validate PRD completeness and clarity | PRD quality score |
| 3 | **Epic Coverage Validation** | Map PRD requirements to epics, identify gaps | Coverage matrix |
| 4 | **UX Alignment** | Verify epics implement UX specifications | Alignment report |
| 5 | **Epic Quality Review** | Story granularity, independence, testability (INVEST criteria) | Quality assessment |
| 6 | **Final Assessment** | Go / Needs Work / No-Go recommendation | Readiness report |

**Output:** `readiness-report.md` at `_bmad-output/implementation-artifacts/readiness-report.md`

---

## 6. Phase Gate 1C Exit Criteria

Phase Gate 1C produces one of three outcomes:

| Outcome | Criteria | Action |
|---------|----------|--------|
| **READY (GO)** | All criteria below met | Proceed to Phase 4 |
| **NEEDS WORK** | Minor gaps identified | Return to specific Phase 3 step |
| **NOT READY (NO-GO)** | Major gaps, missing artifacts | Return to Phase 2 or HALT |

### READY Checklist

- [ ] Architecture document complete with ADRs for all significant decisions
- [ ] Epics cover 100% of PRD functional requirements (no gaps)
- [ ] Stories are INVEST-quality: Independent, Negotiable, Valuable, Estimable, Small, Testable
- [ ] Implementation readiness report shows GO recommendation
- [ ] `project-context.md` generated at project root
- [ ] `sprint-status.yaml` initialized from epics (all stories set to `backlog`)
- [ ] User has reviewed and approved all solutioning artifacts
- [ ] **Story conflict detection:** No duplicate stories covering same functionality; no stories with conflicting acceptance criteria; stories are mutually exclusive and collectively exhaustive (MECE)

**Gate 1C Iteration Limit:** Maximum 2 NEEDS WORK iterations. If the gate still produces NEEDS WORK on the third attempt, escalate to NOT READY (NO-GO) and HALT. Present specific deficiencies to the user.

**Phase Gate 1C Output:** Architecture + Epics/Stories + Readiness Report + Sprint Status + Project Context

---

## 7. Skill Availability Check

Before invoking any skill, verify it exists:

```
Check: .agent/skills/{skill-name}/ exists
If missing: HALT with message "Skill {skill-name} not installed. Please install or confirm manual execution."
```

**Required skills for this phase:**
- `bmad-create-architecture`
- `bmad-create-epics-and-stories`
- `bmad-check-implementation-readiness`
- `architecture`
- `app-builder`
- `bmad-advanced-elicitation`

---

## 8. State Updates

After Phase Gate 1C passes (READY):
- Write `architecture.md` to `_bmad-output/planning-artifacts/`
- Write `epics.md` to `_bmad-output/implementation-artifacts/`
- Write `readiness-report.md` to `_bmad-output/implementation-artifacts/`
- Write `project-context.md` to project root
- Initialize `sprint-status.yaml` at `_bmad-output/implementation-artifacts/sprint-status.yaml` with all stories set to `backlog`
- Update document frontmatter with `stepsCompleted` arrays

---

## 9. Error Handling

| Error | Recovery |
|-------|----------|
| Missing skill | HALT, inform user, offer manual fallback |
| Architecture gaps found | Return to Step 3 (Starter Architecture), revise |
| Story coverage incomplete | Return to Step 4 (Epic/Story Decomposition), add missing stories |
| Readiness = NEEDS WORK (iteration 1-2) | Address specific gaps, re-run readiness check |
| Readiness = NOT READY or NEEDS WORK (iteration 3+) | HALT, return to Phase 2, present specific deficiencies |

---

## 10. Next Steps

After Phase Gate 1C passes (READY):
- Load `directives/procedures/implementation.md` (Phase 4)
- Do NOT proceed without READY status

---

*End of Phase 3: Solutioning. For master workflow, see `directives/Ultimate-Workflow.md`. For principles, see `directives/principles.md`.*
