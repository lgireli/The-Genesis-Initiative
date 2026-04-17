---
description: Phase 4 - Implementation Workflow (AGTK Execution) - Sprint loop, Dev Story, Red-Green-Refactor
version: 1.0.0
generated: 2026-04-10
scope: Sprint planning, story creation, dev story execution (10 steps), code review, QA, sprint status updates
---

# Phase 4: Implementation (AGTK Execution)

> **Purpose:** Implement all stories through sprint execution loop with Red-Green-Refactor discipline.
> **Input:** Approved stories from Phase 3 (`epics.md`, `sprint-status.yaml`)
> **Output:** Working, tested, documented product
> **Exit:** Phase Gate 1D (All stories done + validated)

---

## 1. Phase Entry Criteria

- [ ] Phase Gate 1C passed (all solutioning artifacts approved, readiness = GO)
- [ ] At least one story in `ready-for-dev` status
- [ ] User explicitly requests implementation

---

## 2. Activated Agents

| Agent | Canonical ID | Persona | Role | Key Skills |
|-------|-------------|---------|------|------------|
| Scrum Master | `bmad-agent-sm` (Bob) | Bob | Sprint planning, story preparation, backlog management | `bmad-sprint-planning`, `bmad-create-story` |
| Developer | `bmad-agent-dev` (Amelia) | Amelia | Story execution, TDD, clean code | `bmad-dev-story` |
| QA Engineer | `bmad-agent-qa` (Quinn) | Quinn | E2E test generation, coverage analysis | `bmad-qa-generate-e2e-tests` |

---

## 3. Sprint Planning Loop

### 3.1 Sprint Planning

Execute `bmad-sprint-planning`:
1. Read epics from `_bmad-output/implementation-artifacts/epics.md`
2. Generate `sprint-status.yaml` at `_bmad-output/implementation-artifacts/sprint-status.yaml`
3. Initialize all epic and story statuses to `backlog`
4. Mark first epic as `in-progress` when work begins

### 3.2 Story Creation

Execute `bmad-create-story`:
1. Find next `backlog` story in sprint status
2. Load epic context and story requirements
3. Create dedicated story file with all required sections (see Section 7 for template)
4. Update sprint status: `backlog` -> `ready-for-dev`

### 3.3 Dev Story Workflow (Red-Green-Refactor) -- 10 Steps

Execute `bmad-dev-story`. This is the **core implementation engine**. All 10 steps MUST be executed in exact order.

| Step | Name | Description | Critical Rules |
|------|------|-------------|----------------|
| **1** | **Find Next Ready Story** | Search `sprint-status.yaml` for first story with status `ready-for-dev`. Load complete story file. Parse all sections. | If no ready story found, HALT and offer options. |
| **2** | **Load Context** | Load `project-context.md` for coding standards. Extract Dev Notes for technical guidance. Load any referenced architecture documents. | Never implement without context. |
| **3** | **Detect Review Continuation** | Check if resuming after code review (look for "Senior Developer Review (AI)" section). Extract pending review items. Prioritize review follow-ups. | Review items take priority over regular tasks. |
| **4** | **Mark In-Progress** | Update `sprint-status.yaml`: `ready-for-dev` -> `in-progress`. Use write lock protocol (see `_routing.md` Section 7). | Verify valid state transition. |
| **5** | **Implement (RGR)** | **RED:** Write failing tests first. Confirm tests fail. **GREEN:** Implement MINIMAL code to pass. Run tests. **REFACTOR:** Improve structure while tests stay green. Follow tasks EXACTLY -- no deviation. | NEVER implement anything not mapped to a task/subtask. HALT on: 3 consecutive failures, missing config, ambiguous requirements. |
| **6** | **Author Tests** | Unit tests for business logic. Integration tests for component interactions. E2E tests for critical flows (if required). Cover edge cases from Dev Notes. | All new code must have corresponding tests. |
| **7** | **Run Validations** | Run ALL existing tests (no regressions). Run new tests (correctness). Run linting and code quality checks. Validate against ALL acceptance criteria. | If any test fails: STOP and fix before continuing. |
| **8** | **Validate and Mark Complete** | Verify ALL tests ACTUALLY EXIST and PASS 100%. Confirm implementation matches EXACTLY what task specifies. Validate ALL related ACs satisfied. Ensure NO regressions. ONLY THEN mark task `[x]`. Update File List. | NEVER mark task complete unless ALL gates pass. Tests must assert specific behavior (not `assert True`). |
| **9** | **Story Completion** | Verify ALL tasks `[x]`. Run full regression. Confirm File List complete. Execute Definition of Done validation (Section 5). Update story Status to `review`. Update sprint status to `review`. | If any task incomplete or DoD fails: HALT. |
| **10** | **Completion Communication** | Summarize: story ID, key changes, tests added, files modified. Provide story file path and status. Offer explanations tailored to user skill level. Suggest next steps. | Best practice: Run code review with a DIFFERENT LLM. |

**Test Quality Verification (Step 8):**
- [ ] Tests assert specific behavior (not trivially passing like `assert True`)
- [ ] Tests cover the acceptance criteria for this task/subtask
- [ ] Tests would fail if the implementation were removed (mutation sanity check)

### HALT Conditions During Dev Story

| Condition | Action |
|-----------|--------|
| 3 consecutive implementation failures on same task | HALT and request user guidance |
| Missing configuration or dependency | HALT: "Cannot proceed without [X]. Please provide or configure it." |
| Ambiguous task/subtask requirements | HALT: "Requirements for [X] are ambiguous. Please clarify: [specific question]" |
| Additional dependencies needed beyond story spec | HALT: "Additional dependencies need user approval" |
| Context overflow risk (75%+) | Checkpoint save, warn user, suggest continuation |

---

## 4. Code Review (3 Parallel Layers)

Execute `bmad-code-review` after story marked `review`:

| Layer | Name | Focus | What It Finds |
|-------|------|-------|---------------|
| **Layer 1** | **Blind Hunter** | Security vulnerabilities, anti-patterns, code smells | OWASP issues, injection risks, hard-coded secrets |
| **Layer 2** | **Edge Case Hunter** | Unhandled edge cases, boundary conditions, error paths | Missing null checks, unhandled exceptions, race conditions |
| **Layer 3** | **Acceptance Auditor** | Story AC coverage verification | ACs not fully implemented, missing test coverage |

**Review Triage:**
| Severity | Required Action |
|----------|-----------------|
| **Critical** | Block merge until resolved |
| **Important** | Fix or document rationale for deferral |
| **Advisory** | Acknowledge, no action required |

**Different LLM Requirement:** Run code review using a DIFFERENT LLM than implementation. **Fallback:** If different LLM not available, perform structured self-review using Blind Hunter/Edge Case Hunter/Acceptance Auditor checklists manually. Flag limitation in review report.

For full code review workflow, see `directives/procedures/code-review.md`.

---

## 5. Quality Gates (Implementation-Level)

### Quality Gate Q1: Story Validation (Before Dev)
- [ ] User story follows proper format: "As a [role], I want [action], so that [benefit]"
- [ ] At least 2 acceptance criteria, all measurable and testable
- [ ] Tasks/subtasks cover all acceptance criteria
- [ ] Dev notes include architecture references
- [ ] Story is independent (can be developed in any order)
- [ ] Story file has all required sections populated
- [ ] No duplicate stories or conflicting ACs

### Quality Gate Q2: Red-Green-Refactor (During Each Task)
- [ ] Tests written BEFORE implementation (RED)
- [ ] Tests fail before implementation (validates correctness)
- [ ] Minimal code implemented to pass (GREEN)
- [ ] All tests pass after implementation
- [ ] Code refactored while tests stay green (REFACTOR)
- [ ] Tests assert specific behavior (not trivially passing)

### Quality Gate Q3: Definition of Done (After Story Complete)
**Context and Requirements:**
- [ ] Dev Notes contains ALL necessary technical requirements
- [ ] Implementation follows all architectural requirements
- [ ] All technical specifications implemented correctly

**Implementation Completion:**
- [ ] Every task and subtask marked complete with `[x]`
- [ ] Implementation satisfies EVERY Acceptance Criterion
- [ ] Error conditions and edge cases addressed

**Testing and Quality:**
- [ ] Unit tests added/updated for ALL core functionality
- [ ] Integration tests added for component interactions when required
- [ ] E2E tests created for critical flows when story requires them
- [ ] ALL existing tests pass (no regressions)
- [ ] Linting and static checks pass

**Documentation and Tracking:**
- [ ] File List includes EVERY new, modified, or deleted file
- [ ] Dev Agent Record contains implementation notes
- [ ] Change Log includes summary of changes
- [ ] Review follow-ups completed (if applicable)

**Final Status:**
- [ ] Story Status set to `review`
- [ ] Sprint status updated to `review`
- [ ] All quality gates passed
- [ ] No HALT conditions active

---

## 6. Sprint Status Management

### Story Status Transitions

```
backlog --> ready-for-dev --> in-progress --> review --> done
```

| From | To | Authorized Agent |
|------|----|-----------------|
| `backlog` | `ready-for-dev` | Scrum Master |
| `ready-for-dev` | `in-progress` | Developer |
| `in-progress` | `review` | Developer |
| `review` | `done` | Reviewer/QA |
| `review` | `in-progress` | Developer (if review findings require changes) |

**INVALID Transitions:**
- `backlog` -> `in-progress` (skips validation)
- `ready-for-dev` -> `review` (skips implementation)
- `done` -> any (done is terminal)

### Epic Status Transitions

```
backlog --> in-progress --> done
```

Epic is `done` when ALL stories in epic are `done`.

---

## 7. Story File Template

```markdown
# Story {epic_num}.{story_num}: {story_title}

Status: ready-for-dev

## Story

As a {role},
I want {action},
So that {benefit}.

## Acceptance Criteria

1. {measurable, testable criterion}
2. {measurable, testable criterion}
3. {measurable, testable criterion}

## Tasks / Subtasks

- [ ] Task 1 (AC: #1, #2)
  - [ ] Subtask 1.1
  - [ ] Subtask 1.2
- [ ] Task 2 (AC: #3)
  - [ ] Subtask 2.1

## Dev Notes

- Architecture patterns to follow: [reference]
- Relevant constraints: [details]
- Previous story learnings: [if applicable]
- Technical specifications: [libraries, frameworks, versions]

### References

- [Source: docs/<file>.md#Section]
- [Source: architecture.md#Component]

## Dev Agent Record

### Agent Model Used

{agent_model_name_version}

### Debug Log

{Chronological log of implementation decisions and issues encountered}

### Completion Notes

{Summary of what was implemented, tested, and validated}

### File List

{All new, modified, and deleted files (relative paths)}

## Change Log

| Date | Change | Author |
|------|--------|--------|
| {date} | {Summary of changes} | {agent} |

## Status

Current: ready-for-dev
```

---

## 8. Skill Availability Check

Before invoking any skill, verify it exists:

```
Check: .agent/skills/{skill-name}/ exists
If missing: HALT with message "Skill {skill-name} not installed. Please install or confirm manual execution."
```

**Required skills for this phase:**
- `bmad-sprint-planning`
- `bmad-create-story`
- `bmad-dev-story`
- `bmad-code-review`
- `bmad-qa-generate-e2e-tests`
- `bmad-retrospective`
- `bmad-correct-course`

---

## 9. Error Handling

| Error | Recovery |
|-------|----------|
| No ready-for-dev stories found | Offer: create stories, validate stories, or specify path manually |
| 3 consecutive implementation failures | HALT, present failure details, request user guidance on approach |
| Missing configuration/dependency | HALT with specific missing item, wait for user to provide |
| Test failures unfixable | HALT, identify root cause, escalate to user (may require architectural change) |
| Story file inaccessible | HALT: "Cannot find/read story file at [path]. Please verify." |
| Context overflow (90%+) | Mandatory checkpoint save to `.tmp/checkpoint-{story_id}.md`, request continuation |

---

## 10. Phase Gate 1D Exit Criteria (Definition of Done)

- [ ] All stories in all epics marked `done`
- [ ] All epics marked `done`
- [ ] All retrospectives completed (or explicitly skipped by user)
- [ ] Full regression suite passes with zero failures
- [ ] Final validation (`execution/verify_all.py`) passes (or documented exceptions approved)
- [ ] User has accepted delivery
- [ ] All P0 and P1 validation checks pass

**Phase Gate 1D Output:** Complete, tested, documented product with passing validation.

---

## 11. Next Steps

After Phase Gate 1D passes:
- Run full validation suite (`directives/procedures/validation.md`)
- Present delivery summary to user
- Project is complete

---

*End of Phase 4: Implementation. For full code review workflow, see `directives/procedures/code-review.md`. For validation, see `directives/procedures/validation.md`. For master workflow, see `directives/Ultimate-Workflow.md`.*
