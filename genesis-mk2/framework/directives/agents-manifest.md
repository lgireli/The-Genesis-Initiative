# Genesis MK2 Agent Manifest

> **Complete roster of all 20 AI specialists in the Genesis MK2 framework**
> **Purpose:** Quick reference for agent selection and routing
> **Last Updated:** Framework v1.0.0
> **Status:** CRITICAL FIXES IN PROGRESS

---

## ⚠️ IMPORTANT: Agent Naming Standardization

**Current Issue:** Agent filenames use kebab-case (e.g., `backend-specialist.md`)

**All references must use:** Actual filenames from `agents/` directory

**Correct references:**
- `agents/backend-specialist.md` ✅
- `agents/qa-automation-engineer.md` ✅ (NOT `agents/qa.md`)
- `agents/product-manager.md` ✅ (NOT `agents/analyst.md`)

---

## 🤖 Agent Categories

### Strategic Agents (High-Level Planning)

| Agent | Correct Filename | When to Use |
|-------|-----------------|-------------|
| **Orchestrator** | `orchestrator.md` | Always (your primary role) |
| **Business Analyst** | `product-manager.md` | Phase 1: Analysis |
| **Product Manager** | `product-manager.md` | Phase 2: Planning |
| **Product Owner** | `product-owner.md` | Phase 2: Planning |
| **Project Planner** | `project-planner.md` | Any phase requiring planning |

### Design & Architecture Agents

| Agent | Correct Filename | When to Use |
|-------|-----------------|-------------|
| **UX Designer** | `frontend-specialist.md` | Phase 2: Planning |
| **Architect** | `database-architect.md` | Phase 3: Solutioning |
| **Database Architect** | `database-architect.md` | Database changes |

### Implementation Agents

| Agent | Correct Filename | When to Use |
|-------|-----------------|-------------|
| **Developer** | `backend-specialist.md` | Phase 4: Implementation |
| **Frontend Specialist** | `frontend-specialist.md` | Frontend development |
| **Backend Specialist** | `backend-specialist.md` | Backend development |
| **Mobile Developer** | `mobile-developer.md` | Mobile development |
| **Game Developer** | `game-developer.md` | Game development |

### Quality & Testing Agents

| Agent | Correct Filename | When to Use |
|-------|-----------------|-------------|
| **QA Engineer** | `qa-automation-engineer.md` | Phase 4: Implementation |
| **Test Engineer** | `test-engineer.md` | Testing phase |
| **Security Auditor** | `security-auditor.md` | Before deployment |
| **Penetration Tester** | `penetration-tester.md` | Security review |

### Maintenance & Operations Agents

| Agent | Correct Filename | When to Use |
|-------|-----------------|-------------|
| **Scrum Master** | `project-planner.md` | Phase 4: Implementation |
| **Debugger** | `debugger.md` | Bug fixes |
| **DevOps Engineer** | `devops-engineer.md` | Deployment phase |
| **Performance Optimizer** | `performance-optimizer.md` | Performance issues |
| **Code Archaeologist** | `code-archaeologist.md` | Code modernization |

### Documentation & Research Agents

| Agent | Correct Filename | When to Use |
|-------|-----------------|-------------|
| **Technical Writer** | `documentation-writer.md` | Documentation tasks |
| **SEO Specialist** | `seo-specialist.md` | Web projects |
| **Explorer Agent** | `explorer-agent.md` | Initial project scan |

---

## 🎯 Agent Selection Guide

### For New Project (BUILD):
1. **Orchestrator** (you) - `agents/orchestrator.md`
2. **Product Manager** - `agents/product-manager.md`
3. **Frontend Specialist** - `agents/frontend-specialist.md`
4. **Database Architect** - `agents/database-architect.md`
5. **Backend Specialist** - `agents/backend-specialist.md`
6. **QA Automation Engineer** - `agents/qa-automation-engineer.md`

### For Bug Fix (FIX):
1. **Orchestrator** (you)
2. **Debugger** - `agents/debugger.md`
3. **Backend Specialist** - `agents/backend-specialist.md`
4. **Test Engineer** - `agents/test-engineer.md`

### For Quick Enhancement (ENHANCE):
1. **Orchestrator** (you)
2. **Frontend/Backend Specialist** - `agents/frontend-specialist.md` or `agents/backend-specialist.md`
3. **QA Automation Engineer** - `agents/qa-automation-engineer.md`

---

## 📊 Agent Statistics

- **Total Agents:** 21 (including orchestrator)
- **Strategic:** 4
- **Design & Architecture:** 2
- **Implementation:** 5
- **Quality & Testing:** 4
- **Maintenance & Operations:** 5
- **Documentation & Research:** 3

---

## 🔗 Agent File Locations

**All agent files are in:** `framework/AGENTS/`

**Example path:** `framework/AGENTS/backend-specialist.md`

---

## 🚨 CRITICAL UPDATE NEEDED

**START-HERE.md must be updated to use correct filenames:**

❌ **WRONG:** `agents/analyst.md`
✅ **CORRECT:** `agents/product-manager.md`

❌ **WRONG:** `agents/developer.md`
✅ **CORRECT:** `agents/backend-specialist.md`

❌ **WRONG:** `agents/qa.md`
✅ **CORRECT:** `agents/qa-automation-engineer.md`

---

*Genesis MK2 Agent Manifest - Version 1.0.0 (CRITICAL FIXES IN PROGRESS)*
*Update all references to use actual filenames*
