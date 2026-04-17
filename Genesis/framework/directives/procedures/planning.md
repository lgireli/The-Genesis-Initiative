---
description: Phase 2 - Planning Workflow (BMAD Strategic) - PRD and UX Design
version: 1.0.0
generated: 2026-04-10
scope: Product Requirements Document creation, UX Design Specification
---

# Phase 2: Planning (BMAD Strategic)

> **Purpose:** Transform product briefs into detailed PRDs and UX design specifications.
> **Input:** Approved `product-brief.md` from Phase 1
> **Output:** `prd.md` + `ux-design.md` at `_bmad-output/planning-artifacts/`
> **Exit:** Phase Gate 1B (PRD + UX approved)

---

## 1. Phase Entry Criteria

- [ ] Phase Gate 1A passed (Product Brief approved)
- [ ] User explicitly requests planning phase

---

## 2. Activated Agents

| Agent | Canonical ID | Persona | Role | Key Skills |
|-------|-------------|---------|------|------------|
| Product Manager | `bmad-agent-pm` (John) | John | PRD creation, requirements prioritization, stakeholder alignment | `bmad-create-prd`, `bmad-edit-prd`, `bmad-validate-prd` |
| UX Designer | `bmad-agent-ux-designer` (Sally) | Sally | UX patterns, design specifications, user research | `bmad-create-ux-design`, `ui-ux-pro-max`, `frontend-design` |

---

## 3. PRD Creation Workflow (14 Steps)

Execute `bmad-create-prd`:

| Step | Name | Purpose | Output |
|------|------|---------|--------|
| 1 | **Init** | Initialize configuration, load templates | Config loaded |
| 2 | **Discovery** | User interviews, needs analysis | User needs documented |
| 3 | **Vision** | Product vision and goals | Vision statement |
| 4 | **Executive Summary** | High-level overview for stakeholders | Executive summary |
| 5 | **Success Metrics** | KPIs and measurement criteria | Measurable success criteria |
| 6 | **User Journeys** | Key user flows and paths | Journey maps |
| 7 | **Domain Model** | Core entities and relationships | Entity relationship diagram |
| 8 | **Innovation** | Differentiators and competitive advantages | Innovation section |
| 9 | **Project Type** | Classify (web/mobile/API/full-stack) | Project type determined |
| 10 | **Scoping** | In/out of scope, constraints | Scope boundaries |
| 11 | **Functional Requirements** | Detailed feature specs | Functional requirements list |
| 12 | **Non-Functional Requirements** | Performance, security, accessibility thresholds | NFR list with measurable thresholds |
| 13 | **Polish** | Final review and formatting | Polished PRD |
| 14 | **Complete** | PRD finalized and saved | `prd.md` |

**Critical Rules:**
- YOU ARE A FACILITATOR, not a content generator
- NEVER generate content without user input
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C' (Continue)
- NEVER load multiple step files simultaneously

**A/P/C Menu (at decision points):**
```
[A]dvanced Elicitation - Deep-dive on current section
[P]arty Mode - Multi-agent collaborative review
[C]ontinue - Advance to next step
```

**Output:** `prd.md` at `_bmad-output/planning-artifacts/prd.md`

---

## 4. UX Design Specification (7 Steps)

Execute `bmad-create-ux-design`:

| Step | Name | Purpose |
|------|------|---------|
| 1 | **Init** | Load PRD context, configure |
| 2 | **Discovery** | User research synthesis |
| 3 | **Core Experience** | Primary interaction flows |
| 4 | **Emotional Response** | Desired user feelings and tone |
| 5 | **Inspiration** | Design references and mood boards |
| 6 | **Design System** | Colors, typography, components, patterns |
| 7 | **Defining Experience** | Detailed UX specifications |

**Output:** `ux-design.md` at `_bmad-output/planning-artifacts/ux-design.md`

---

## 5. PRD Validation

After PRD creation, execute `bmad-validate-prd`:

1. Check PRD completeness (no placeholder text, no TBD sections)
2. Validate functional requirements traceable to user journeys
3. Verify non-functional requirements have measurable thresholds
4. Check for internal consistency (no contradictions between sections)
5. Confirm project type is definitively classified

---

## 6. Phase Gate 1B Exit Criteria

- [ ] PRD complete with all sections populated (no placeholder text, no TBD sections)
- [ ] UX design specification complete
- [ ] PRD validated via `bmad-validate-prd`
- [ ] Functional requirements traceable to user journeys
- [ ] Non-functional requirements have measurable thresholds (e.g., "Page loads in < 2 seconds", NOT "Page loads fast")
- [ ] User has reviewed and approved planning artifacts
- [ ] Project type definitively classified (WEB/MOBILE/BACKEND/FULL-STACK/API)

**Phase Gate 1B Output:** Approved `prd.md` + `ux-design.md`

**If Phase Gate 1B fails:** Return to relevant PRD/UX step. If failing after 2 iterations, HALT.

---

## 7. Skill Availability Check

Before invoking any skill, verify it exists:

```
Check: .agent/skills/{skill-name}/ exists
If missing: HALT with message "Skill {skill-name} not installed. Please install or confirm manual execution."
```

**Required skills for this phase:**
- `bmad-create-prd`
- `bmad-edit-prd`
- `bmad-validate-prd`
- `bmad-create-ux-design`
- `ui-ux-pro-max`
- `frontend-design`
- `bmad-advanced-elicitation`

---

## 8. State Updates

After Phase Gate 1B passes:
- Write `prd.md` and `ux-design.md` to `_bmad-output/planning-artifacts/`
- Update document frontmatter:
  ```yaml
  ---
  stepsCompleted: ["step-01-init", "step-02-discovery", ... all 14 PRD steps ..., "step-01-init-ux", ... all 7 UX steps ...]
  generated: YYYY-MM-DD
  version: 1.0.0
  status: complete
  ---
  ```

---

## 9. Error Handling

| Error | Recovery |
|-------|----------|
| Missing skill | HALT, inform user, offer manual fallback |
| User rejects PRD content | Return to relevant step, re-elicit, maximum 2 iterations |
| PRD validation fails | Fix deficiencies, re-validate, maximum 2 iterations |
| UX conflicts with PRD | Reconcile with user input, do NOT assume |

---

## 10. Next Steps

After Phase Gate 1B passes:
- Load `directives/procedures/solutioning.md` (Phase 3)
- Do NOT proceed to implementation

---

*End of Phase 2: Planning. For master workflow, see `directives/Ultimate-Workflow.md`. For principles, see `directives/principles.md`.*
