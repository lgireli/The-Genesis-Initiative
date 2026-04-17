---
description: Phase 1 - Analysis and Discovery Workflow (BMAD Strategic)
version: 1.0.0
generated: 2026-04-10
scope: Product brief creation, domain/market/technical research, requirements elicitation
---

# Phase 1: Analysis (BMAD Strategic)

> **Purpose:** Transform vague requests into structured product briefs through deep analysis and elicitation.
> **Input:** User request + Socratic Gate output
> **Output:** `product-brief.md` at `_bmad-output/planning-artifacts/product-brief.md`
> **Exit:** Phase Gate 1A (Product Brief approved)

---

## 1. Phase Entry Criteria

- [ ] Request classified as BUILD, INVESTIGATE, or complex ENHANCE
- [ ] Socratic Gate completed and cleared (Tier 1 or Tier 2 per `_routing.md`)
- [ ] User engagement confirmed

---

## 2. Activated Agents

| Agent | Canonical ID | Persona | Role | Key Skills |
|-------|-------------|---------|------|------------|
| Business Analyst | `bmad-agent-analyst` (Mary) | Mary | Requirements elicitation, domain analysis, market research | `bmad-domain-research`, `bmad-market-research`, `bmad-technical-research`, `bmad-advanced-elicitation` |
| Technical Writer | `bmad-agent-tech-writer` (Paige) | Paige | Documentation standards, knowledge curation, Mermaid diagrams | `bmad-editorial-review-prose`, `bmad-editorial-review-structure` |

For INVESTIGATE requests: Business Analyst is primary agent.
For DOCUMENT requests: Technical Writer is primary agent.

---

## 3. Workflow Steps

### Step 1.1: Project Context Discovery

1. Check for existing `project-context.md` at project root -- load if present
2. Scan project directory structure for existing artifacts
3. Identify tech stack, frameworks, and conventions in use
4. Load `_bmad/bmm/config.yaml` for project configuration

### Step 1.2: Requirements Elicitation

Apply advanced elicitation techniques based on request type:

| Technique | Purpose | Example |
|-----------|---------|---------|
| **Socratic Questioning** | Challenge underlying assumptions | "Why does this need to be a real-time system?" |
| **Pre-mortem Analysis** | Identify failure modes early | "Imagine this failed at launch -- what went wrong?" |
| **Red Team Review** | Adversarial analysis of proposed approach | "What is the strongest argument against this?" |
| **First Principles** | Break down to fundamental truths | "What is the core problem we are actually solving?" |

Document all findings in structured format.

### Step 1.3: Domain and Market Research (As Applicable)

Execute skills in parallel where possible:

| Skill | Purpose | Output |
|-------|---------|--------|
| `bmad-domain-research` (6 steps) | Industry and domain context | Domain analysis report |
| `bmad-market-research` (6 steps) | Customer and competitive landscape | Market research report |
| `bmad-technical-research` (6 steps) | Technology selection and feasibility | Technical research report |

### Step 1.4: Product Brief Creation

Execute `bmad-product-brief` with 4-agent ensemble review:

| Reviewer | Role | Focus |
|----------|------|-------|
| `artifact-analyzer` | Technical feasibility | Can we build it with available resources? |
| `opportunity-reviewer` | Market fit | Does this solve a real user problem? |
| `skeptic-reviewer` | Risk identification | What could go wrong? |
| `web-researcher` | Competitive intelligence | Who else is doing this? |

**Output:** Product Brief at `_bmad-output/planning-artifacts/product-brief.md`

### Step 1.5: Investigation Report (For INVESTIGATE Requests)

If request was classified as INVESTIGATE:

1. Perform root cause analysis using systematic debugging
2. Document findings with evidence
3. Provide recommendations with confidence levels
4. Classify recommended next action (FIX/ENHANCE/BUILD or "insufficient data")

**Output:** Investigation report at `_bmad-output/planning-artifacts/investigation-report.md`

**Content:**
- Root cause analysis (if identified)
- Evidence and supporting data
- Recommended next action with justification
- Confidence level (High/Medium/Low)
- Open questions requiring further investigation

---

## 4. Phase Gate 1A Exit Criteria

- [ ] Domain research completed or explicitly scoped as not applicable
- [ ] Stakeholder needs documented
- [ ] Problem statement clearly defined
- [ ] Product Brief created and validated (or investigation report for INVESTIGATE)
- [ ] User has reviewed and approved analysis output
- [ ] Request re-classified with refined scope
- [ ] Sufficient information exists to proceed to Planning phase

**Phase Gate 1A Output:** `product-brief.md` (or `investigation-report.md`)

**If Phase Gate 1A fails:** Return to Step 1.2 for additional elicitation. If still failing after 2 iterations, HALT and request user guidance.

---

## 5. Skill Availability Check

Before invoking any skill, verify it exists:

```
Check: .agent/skills/{skill-name}/ exists
If missing: HALT with message "Skill {skill-name} not installed. Please install or confirm manual execution."
```

**Required skills for this phase:**
- `bmad-product-brief`
- `bmad-domain-research`
- `bmad-market-research`
- `bmad-technical-research`
- `bmad-advanced-elicitation`
- `bmad-editorial-review-prose`
- `bmad-editorial-review-structure`

---

## 6. Error Handling

| Error | Recovery |
|-------|----------|
| Missing skill | HALT, inform user, offer manual fallback |
| Ambiguous request after elicitation | HALT with specific question, do NOT assume |
| User cannot provide required information | Propose smallest safe assumption, ask for confirmation |
| Research skills unavailable | Proceed with available knowledge, document gaps |

---

## 7. State Updates

After Phase Gate 1A passes:
- Write `product-brief.md` to `_bmad-output/planning-artifacts/`
- Update document frontmatter with `stepsCompleted` array
- Set `status: complete` in frontmatter

---

## 8. Next Steps

After Phase Gate 1A passes:
- Load `directives/procedures/planning.md` (Phase 2)
- Do NOT proceed to implementation

---

*End of Phase 1: Analysis. For master workflow, see `directives/Ultimate-Workflow.md`. For principles, see `directives/principles.md`.*
