# 🌌 The Genesis Initiative: Universal AI Development Framework

**The Genesis Initiative** is a high-integrity, portable orchestration framework designed to transform general-purpose AI agents into professional software engineering leads. 

Unlike typical prompts, Genesis MK2 is a **self-contained operating system** for development. It provides a rigorous, state-gated workflow that prevents the "AI drift" and "hallucination loops" common in complex coding tasks.

---

## 🎯 The Core Philosophy: BMAD

Genesis MK2 operates on the **BMAD Strategic Method**, ensuring that no code is written until the problem is solved on paper.

| Phase | Name | Goal | Gate |
| :--- | :--- | :--- | :--- |
| **Phase 1** | **Analysis** | Understand the "What" and "Why" | **Phase Gate 1A** (Product Brief) |
| **Phase 2** | **Planning** | Define the "What" (Requirements) | **Phase Gate 1B** (PRD & UX) |
| **Phase 3** | **Solutioning** | Design the "How" (Architecture) | **Phase Gate 1C** (Readiness = GO) |
| **Phase 4** | **Implementation** | Build and Test (The "Muscle") | **Phase Gate 1D** (Delivery) |

---

## 🚀 Key Capabilities

### 📦 1. Portable "Drag-and-Drop" Design
The entire framework lives in the `genesis-mk2/` folder. To activate it in any project:
1. **Drop** the `genesis-mk2` folder into your project root.
2. **Point** your AI agent to `genesis-mk2/START-HERE.md`.

### 🧠 2. Zero-Config Orchestration
The framework handles its own state. It creates a hidden `.agenkit` directory to track sessions, context, and decision history, ensuring that the AI remembers every architectural choice made.

### ⚡ 3. Dynamic Skill System
Genesis MK2 separates "Knowledge" from "Execution." 
- **Directives (.md)**: Tell the AI *how* to think.
- **Skills (.py)**: Deterministic Python scripts that actually *do* the work (e.g., security scanning, linting, and validation).

### 🔄 4. The Resumption Protocol (Anti-Amnesia)
If a session crashes or a new agent is called, the framework uses a `SITREP.md` (Situation Report). This "Save-Game" file allows any AI to instantly synchronize with the project's current status and resume from the exact last task.

---

## 🛠️ How to Use

### For the Human User
1. **Drop**: Copy the `genesis-mk2` folder into your blank project root.
2. **Point**: Tell your AI: *"Read `genesis-mk2/START-HERE.md` and begin the orchestration."*
3. **Watch**: The AI will automatically bootstrap the project and guide you through the BMAD workflow.

### For the AI Agent
Upon reading `START-HERE.md`, you are activated as the **Chief Orchestrator**. You must:
1. **Bootstrap**: Immediately execute `python genesis-mk2/bootstrap.py` to initialize the project state.
2. **Analyze**: Execute Phase 1 to create a Product Brief.
3. **Plan**: Design the PRD and UX.
4. **Solve**: Architect the solution.
5. **Implement**: Write tested code using the Red-Green-Refactor cycle.

---

## 🏗️ The Development Journey

The Genesis Initiative was evolved through a process of **Adversarial Review**. Using a technique called "Party Mode," we simulated an ensemble of expert personas (The Architect, The Product Manager, and the QA Engineer) to stress-test the framework.

**Major milestones included:**
- **The Shift to Execution**: Moving from purely text-based instructions to a hybrid `.md`/`.py` engine.
- **Path Independence**: Decoupling the framework from specific directory names for total portability.
- **Hardening**: Implementing state-locking and stale-lock recovery to prevent data corruption.
- **The SITREP System**: Creating a cognitive bridge for agent resumption.

---

## ⚖️ License
MIT License - Free to use, modify, and distribute.
