---
description: Agent Routing Matrix and Boundary Enforcement Protocol
version: 1.0.0
generated: 2026-04-10
scope: Agent registry, domain ownership, boundary enforcement, multi-agent orchestration
---

# Agent Routing Matrix

> **Purpose:** Central reference for all 18 agents, their domains, skills, and file ownership. Load this file when routing requests or enforcing agent boundaries.
> **Authority:** Agent boundaries are absolute. Cross-domain file writes constitute a **VIOLATION**.

---

## 1. Unified Agent Registry (BMAD + AGTK)

| # | Agent | BMAD ID | AGTK ID | Domain | Key Skills | File Ownership |
|---|-------|---------|---------|--------|------------|----------------|
| 1 | **Business Analyst** | `bmad-agent-analyst` (Mary) | `product-manager` | Requirements | Domain research, elicitation, market analysis | Analysis artifacts, `product-brief.md` |
| 2 | **Technical Writer** | `bmad-agent-tech-writer` (Paige) | `documentation-writer` | Documentation | CommonMark, DITA, OpenAPI, Mermaid | `docs/`, `directives/` |
| 3 | **Product Manager** | `bmad-agent-pm` (John) | `product-manager` | PRD, Stories | PRD creation, stakeholder alignment, JTBD | `prd.md`, epics |
| 4 | **UX Designer** | `bmad-agent-ux-designer` (Sally) | `frontend-specialist` | UX/UI | User research, interaction design, UI patterns | `ux-design.md` |
| 5 | **Architect** | `bmad-agent-architect` (Winston) | `project-planner`, `architecture` | Architecture | Distributed systems, cloud, API design | `architecture.md`, ADRs |
| 6 | **Developer** | `bmad-agent-dev` (Amelia) | Domain specialists | Implementation | TDD, clean code, existing patterns | Source code (non-test) |
| 7 | **QA Engineer** | `bmad-agent-qa` (Quinn) | `qa-automation-engineer` | E2E Testing | Playwright, API testing, coverage | `**/*.test.*`, `**/__tests__/**` |
| 8 | **Quick Flow Dev** | `bmad-agent-quick-flow-solo-dev` (Barry) | Domain specialists | Rapid dev | Full-stack, minimal ceremony | Source code |
| 9 | **Scrum Master** | `bmad-agent-sm` (Bob) | `project-planner` | Sprint mgmt | Agile ceremonies, story prep | `sprint-status.yaml` |
| 10 | **Frontend Specialist** | -- | `frontend-specialist` | UI/UX | React, Next.js, Tailwind, components | `**/components/**` |
| 11 | **Backend Specialist** | -- | `backend-specialist` | API/Server | Node.js, Express, FastAPI, APIs | `**/api/**`, `**/server/**` |
| 12 | **Database Architect** | -- | `database-architect` | Database | Schema, SQL, Prisma, migrations | `**/prisma/**`, `**/drizzle/**` |
| 13 | **Security Auditor** | -- | `security-auditor` | Security | OWASP, vulnerability scanning, auth | Security configs |
| 14 | **Penetration Tester** | -- | `penetration-tester` | Security Testing | Red team, offensive security | Test findings |
| 15 | **DevOps Engineer** | -- | `devops-engineer` | CI/CD, Infra | Docker, deployment, monitoring | CI/CD configs, Dockerfiles |
| 16 | **Test Engineer** | -- | `test-engineer` | Testing | Jest, Vitest, TDD, strategies | Test files |
| 17 | **Debugger** | -- | `debugger` | Debugging | Root cause analysis, systematic debugging | Bug fix code |
| 18 | **Performance Optimizer** | -- | `performance-optimizer` | Performance | Profiling, Web Vitals, caching | Performance code |

---

## 2. Boundary Enforcement Protocol

**CRITICAL:** Each agent MUST stay within its domain. Cross-domain file writes constitute a **VIOLATION**.

| File Pattern | Owner Agent(s) | Blocked Agents |
|-------------|----------------|----------------|
| `**/*.test.{ts,tsx,js,py}` | `test-engineer`, `qa-automation-engineer` | **ALL** others |
| `**/__tests__/**` | `test-engineer`, `qa-automation-engineer` | **ALL** others |
| `**/components/**` | `frontend-specialist`, `mobile-developer` (mobile) | `backend`, `test` agents |
| `**/api/**`, `**/server/**` | `backend-specialist` | `frontend`, `test` agents |
| `**/prisma/**`, `**/drizzle/**`, `**/migrations/**` | `database-architect` | `frontend`, `backend` agents |
| `**/*.md` (docs/) | `documentation-writer`, `tech-writer` (Paige) | Implementation agents |
| `directives/**/*.md` | Layer 2 (Orchestrator) | **ALL** others |
| `execution/**/*.py` | Layer 3 (as directed by Layer 2) | **ALL** others |
| `.agent/**` | Orchestrator only | **ALL** others |
| `package.json`, `pyproject.toml`, `Cargo.toml` | `database-architect`, `backend-specialist`, `architect` | `frontend`, `test` agents |
| `Dockerfile`, `docker-compose.*`, `.dockerignore` | `devops-engineer` | **ALL** others |
| `.github/workflows/*`, `.gitlab-ci.yml`, `Jenkinsfile` | `devops-engineer` | **ALL** others |
| `.env*` (except `.env.example`) | **No agent** -- user-managed only | **ALL** agents |
| `*.config.js`, `*.config.ts`, `tsconfig.json` | `backend-specialist`, `frontend-specialist` (own domain) | Cross-domain agents |

### Enforcement Protocol

```
BEFORE any agent writes a file:
  1. Check file path against boundary table above
  2. IF file.path MATCHES another agent domain:
     - STOP immediately
     - INVOKE the correct agent for that file
     - DO NOT write the file yourself
  3. IF file.path is within agent domain:
     - Proceed with write
  4. LOG all file writes for audit trail
```

**Post-Hoc Validation:** After each story completion, run a boundary audit: compare all files modified during the story against the boundary table. Report any violations to the user as part of the completion communication.

---

## 3. Multi-Agent Orchestration Protocol

**Minimum 3 agents** for complex orchestration tasks.

### Phase 1: Planning (Sequential -- NO parallel)

| Order | Agent | Purpose | Output Passed To Next |
|-------|-------|---------|----------------------|
| 1 | `explorer-agent` | Map affected areas of codebase | File list, dependency map |
| 2 | `project-planner` | Create or validate implementation plan | Plan document |
| 3 | Domain specialists | Analyze and design within their domains | Design decisions, ADRs |

### Phase 2: Implementation (Parallel After Approval)

| Order | Agent | Purpose | Constraint |
|-------|-------|---------|------------|
| 1 | Domain specialists | Implement in parallel | Non-overlapping file sets only |
| 2 | `test-engineer` | Verify all changes | After implementation agents complete |
| 3 | `security-auditor` | Final security check | If touching auth, user data, payment, APIs |

### Context Passing Protocol

When invoking any subagent, the orchestrator MUST include:

1. **Original User Request:** Full text of what the user asked
2. **Decisions Made:** All user answers to Socratic questions
3. **Previous Agent Work:** Summary of what previous agents did
4. **Current Plan State:** If plan files exist in workspace, include them

**Example Context Block:**
```
**CONTEXT:**
- User Request: "A social platform for students, using mock data"
- Decisions: Tech=Vue 3, Layout=Grid Widgets, Auth=Mock, Design=Youthful & dynamic
- Previous Work: Orchestrator asked 6 questions, user chose all options
- Current Plan: playful-roaming-dream.md exists in workspace with initial structure

**TASK:** Create detailed PLAN.md based on ABOVE decisions. Do NOT infer from folder name.
```

### Agent Selection Matrix

| Task Type | Required Agents (minimum) |
|-----------|--------------------------|
| **Web App** | frontend-specialist, backend-specialist, test-engineer |
| **API** | backend-specialist, security-auditor, test-engineer |
| **UI/Design** | frontend-specialist, seo-specialist, performance-optimizer |
| **Database** | database-architect, backend-specialist, security-auditor |
| **Full Stack** | project-planner, frontend-specialist, backend-specialist, devops-engineer |
| **Debug** | debugger, explorer-agent, test-engineer |
| **Security** | security-auditor, penetration-tester, devops-engineer |

---

## 4. Conflict Resolution

When agents or checks produce conflicting recommendations, resolve in this order:

| Priority | Principle | Example |
|----------|-----------|---------|
| **1 (Highest)** | **Security** | A security vulnerability finding ALWAYS overrides performance or convenience |
| **2** | **Performance** | A performance bottleneck finding overrides developer convenience |
| **3 (Lowest)** | **Convenience** | Developer convenience is the lowest priority |

### Same File Edits
1. Collect all suggestions from agents
2. Present merged recommendation
3. Ask user for preference if conflicts exist

### Disagreement Between Agents
1. Note both perspectives
2. Explain trade-offs
3. Recommend based on priority order: security > performance > convenience

---

## 5. Agent Quick-Select Matrix

| Need | Primary Agent | Secondary Agent | Validation |
|------|--------------|-----------------|------------|
| New feature | PM (John) -> Architect (Winston) -> Dev (Amelia) | UX Designer (Sally) | PRD validation, DoD |
| Bug fix | Debugger -> Dev (Amelia) | Test Engineer | Regression tests pass |
| Security review | Security Auditor | Penetration Tester | Security scan (P0) |
| Performance issue | Performance Optimizer | Backend Specialist | Lighthouse (P6) |
| Database change | Database Architect | Backend Specialist | Schema validation (P2) |
| UI/UX change | Frontend Specialist | UX Designer (Sally) | UX audit (P4) |
| E2E tests | QA Engineer (Quinn) | Test Engineer | Test suite passes |
| Documentation | Technical Writer (Paige) | Documentation Writer | Doc validation |
| Sprint planning | Scrum Master (Bob) | Architect (Winston) | Sprint status initialized |
| Code review | Code Review workflow | Different LLM required | All Critical findings resolved |
| Investigation | Business Analyst (Mary) | Technical Writer (Paige) | Investigation report |

---

*End of Agent Routing Matrix. For phase-specific workflows, see `directives/procedures/`. For core principles, see `directives/principles.md`. For master workflow, see `directives/Ultimate-Workflow.md`.*
