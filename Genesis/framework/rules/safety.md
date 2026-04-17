---
description: Core Operating Principles and Commandments for AI-Driven Development
version: 1.0.0
generated: 2026-04-10
scope: Cross-cutting principles applicable to all phases and agents
---

# Core Operating Principles

> **Purpose:** These principles govern EVERY action across ALL phases. Load this file at session start for constant reference.
> **Authority:** These are the non-negotiable rules of the system. Violations constitute failed orchestration.

---

## 1. Unified Workflow Philosophy

You operate as a **Unified Engineering Ecosystem** with three integrated layers:

| Layer | System | Responsibility |
|-------|--------|----------------|
| **Strategic** | BMAD | Manages the "What" and "Why" -- Discovery, PRD, Epic/Story Lifecycle, Sprint Planning |
| **Technical** | AGTK | Manages the "How" and "Implementation" -- Code generation, Architecture, Security Audit, E2E Testing |
| **Operational** | 4-Layer Architecture | Provides the execution backbone -- SOPs, deterministic scripts, intelligent routing, self-healing |

---

## 2. Core Operating Principles (P1-P10)

| # | Principle | Description |
|---|-----------|-------------|
| **P1** | **Tool-First Approach** | Always check `execution/` for existing scripts before writing new code. Push complexity into Layer 3 (deterministic scripts). |
| **P2** | **Progressive Disclosure** | Surface information in priority tiers (P0 > P1 > P2). Never overwhelm with low-priority details when blockers exist. |
| **P3** | **Plan-Before-Build** | Every implementation action must be preceded by a plan. No code is written without understanding the problem, constraints, and acceptance criteria. |
| **P4** | **Questions-Before-Assumptions** | When requests are vague, ambiguous, or missing constraints, ask clarifying questions. **NEVER** build based on assumptions. |
| **P5** | **Deterministic Validation** | LLMs handle decision-making and routing; deterministic Python scripts (`execution/`) handle API calls, data processing, and file operations. The probabilism/determinism boundary is inviolable. |
| **P6** | **Boundary Enforcement** | Each agent MUST stay within its domain. Cross-domain file writes are violations. Enforcement is automatic and non-negotiable. |
| **P7** | **Self-Annealing** | Every failure makes the system stronger. Errors trigger a 5-step loop: Analyze, Patch, Test, Document, Preserve. Directives grow; they are never deleted. |
| **P8** | **State Isolation** | Ephemeral (`.tmp/`), Persistent (`_bmad-output/`), Directive (`directives/`), and Registry (`.agent/`) directories have strictly separated lifecycles. |
| **P9** | **Multi-Speed Operation** | The system supports Full BMAD (strategic, multi-sprint), AGTK Implementation (tactical, sprint-level), and Quick Flow (rapid, single-task) modes with explicit selection criteria. |
| **P10** | **Synthesis Over Aggregation** | Analysis outputs are synthesized into coherent artifacts (PRDs, architectures, epics), not merely aggregated. Each artifact must be internally consistent and traceable to requirements. |

---

## 3. The 10 Commandments (Non-Negotiable)

These rules **MUST** be followed under all circumstances. Violations constitute failed orchestration.

| # | Commandment | Violation Example |
|---|-------------|-------------------|
| **C1** | **THOU SHALT NOT assume requirements** -- clarify first | Implementing a feature without asking about scope |
| **C2** | **THOU SHALT NOT skip quality gates** -- all gates must pass | Marking a task done without tests passing |
| **C3** | **THOU SHALT NOT write outside thy domain** -- agent boundaries are absolute | Developer writing test files |
| **C4** | **THOU SHALT NOT destroy without permission** -- no deletes, drops, or overwrites without explicit confirmation | Deleting a database table |
| **C5** | **THOU SHALT NOT expose secrets** -- API keys, tokens, and credentials are never logged, output, or committed | Printing an API key in a response |
| **C6** | **THOU SHALT NOT skip the plan** -- no implementation before planning | Writing code without understanding architecture |
| **C7** | **THOU SHALT NOT lie about completion** -- tasks are only marked done when ALL validation gates pass | Checking a task box without tests passing |
| **C8** | **THOU SHALT NOT modify directives without permission** -- scope lock on core files (**C8 is exempt for Self-Annealing Loop directive updates**; see `directives/Ultimate-Workflow.md` Section 13.3) | Overwriting the workflow file |
| **C9** | **THOU SHALT NOT halt silently** -- all failures must be communicated with specific messages | Failing without telling the user why |
| **C10** | **THOU SHALT preserve and grow directives** -- append-only, never delete (**scoped: applies ONLY to `directives/` and workflow files; ephemeral files in `.tmp/` may be deleted at any time**) | Deleting an SOP instead of updating it |

---

## 4. Conflict Resolution Priority

When agents or checks produce conflicting recommendations, resolve in this order:

| Priority | Principle | Example |
|----------|-----------|---------|
| **1 (Highest)** | **Security** | A security vulnerability finding ALWAYS overrides performance or convenience |
| **2** | **Performance** | A performance bottleneck finding overrides developer convenience |
| **3 (Lowest)** | **Convenience** | Developer convenience is the lowest priority |

**Rule:** Security > Performance > Convenience. Always.

---

## 5. Gate Taxonomy

The system uses two distinct gate families with separate numbering. These are NOT interchangeable.

### Phase Exit Gates (1A-1D) -- Control phase transitions

| Gate | From -> To | Key Output |
|------|-----------|------------|
| **Phase Gate 1A** | Analysis -> Planning | Product Brief approved |
| **Phase Gate 1B** | Planning -> Solutioning | PRD + UX approved |
| **Phase Gate 1C** | Solutioning -> Implementation | Readiness = GO |
| **Phase Gate 1D** | Implementation -> Delivery | All stories validated, verify_all.py passes |

### Quality Gates (Q1-Q5) -- Validate work products

| Gate | When | Purpose |
|------|------|---------|
| **Quality Gate Q1** | After story creation, before dev | Ensure story is well-formed and implementable |
| **Quality Gate Q2** | During each task/subtask | Ensure TDD discipline and code quality |
| **Quality Gate Q3** | After all tasks in story complete | Comprehensive story-level validation (Definition of Done) |
| **Quality Gate Q4** | After story marked `review` | Adversarial review by fresh context |
| **Quality Gate Q5** | At project/sprint delivery | Final integration and acceptance validation |

---

## 6. Safety and Security Rules

### 6.1 Destructive Action Policy

**ALWAYS** ask for explicit user confirmation before:
- DELETE operations (API deletes, file deletion outside `.tmp/`)
- Database drops (tables, collections, schemas)
- Overwriting code without backup
- Destructive migrations (delete data/columns)
- Paid API usage (consuming tokens, credits)

### 6.2 Secret Protection

- **NEVER** output secrets (API keys, tokens, passwords, connection strings)
- **NEVER** log secrets or commit secrets
- Use environment variables for all sensitive configuration
- Mask secrets in output: `sk-****-****-****-abcd`

### 6.3 Scope Lock

The following files are **LOCKED** and must NOT be modified without explicit user command:
- `directives/Ultimate-Workflow.md`
- `directives/master-workflow.md`
- `.gitignore`
- `.env`, `credentials.json`, `token.json`
- Existing code outside current task scope

**Exception:** C8 is exempt for Self-Annealing Loop updates.

---

## 7. Definition of Architectural Changes (for Quick Flow Eligibility)

Architectural changes include ANY of the following and render a request **ineligible** for Quick Flow:

- Adding, removing, or upgrading project dependencies (libraries, frameworks, packages)
- Changing data models or database schemas (new tables, columns, migrations, ORM changes)
- Introducing new services, layers, or modules (caching layer, message queue, microservice)
- Altering authentication or authorization patterns (OAuth, JWT, RBAC, session management)
- Modifying the project structure (new directories, reorganizing source trees, changing build tooling)
- Changing API contracts or communication protocols (REST to GraphQL, synchronous to asynchronous)
- Introducing new external service integrations (third-party APIs, webhooks, payment gateways)

---

## 8. Self-Annealing Loop (Quick Reference)

When an error occurs:

```
FAILURE -> 1. ANALYZE (error + stack trace + root cause)
        -> 2. PATCH (fix script/code in execution/)
        -> 3. TEST (verify fix works, no regression)
        -> 4. DOCUMENT (update directive in directives/, append-only)
        -> 5. PRESERVE (version track, system is now stronger)
```

**C8 Exemption:** Self-Annealing Loop directive updates are append-only and do NOT require explicit user permission.

---

## 9. Quick Reference: Mode Selection

```
IF ALL of the following are true:
  [ ] Single story or < 2 days of effort
  [ ] No architectural changes required
  [ ] No security implications
  [ ] Clear acceptance criteria provided
  [ ] No cross-domain changes needed
THEN -> Quick Flow
ELSE -> Full BMAD

When in doubt, default to Full BMAD.
```

---

*End of Core Operating Principles. For phase-specific workflows, see `directives/procedures/`. For agent routing, see `directives/agent-matrix.md`. For master workflow, see `directives/Ultimate-Workflow.md`.*
