# Genesis MK2 - Universal AI Development Framework

> **Version:** 1.0.0  
> **Status:** Production Ready (Core Framework)  
> **License:** MIT

---

## 🚀 Quick Start

### Installation

```bash
# Extract the genesis-mk2 folder to your project
# Point your AI agent to START-HERE.md
```

### Usage

```bash
# Interactive mode
python agenkit.py --interactive

# Or use the state management directly
python -c "
from core.state.state_manager import StateManager
state = StateManager('project_path')
state.create_session('session_id', 'project_id', 'User')
"
```

---

## 📁 What's Inside

```
genesis-mk2/
├── START-HERE.md              # Entry point - READ FIRST
├── README.md                  # This file
├── agenkit.py                 # Interactive CLI
├── MINIMAL-WORKING-README.md  # Minimal version guide
├── IMPLEMENTATION-STATUS.md   # Current status
├── CORE/                      # Implementation code
│   ├── state/                 # State management
│   │   └── state_manager.py   # Working implementation
│   └── errors/                # Error handling
│       └── error_handler.py   # Working implementation
├── FRAMEWORK/                 # Documentation
│   ├── DIRECTIVES/            # SOPs and procedures
│   ├── AGENTS/                # Agent definitions
│   ├── SKILLS/                # Knowledge modules
│   ├── RULES/                 # Safety and boundaries
│   └── TEMPLATES/             # Project templates
└── .agenkit/                  # State files (auto-created)
    ├── state/
    └── logs/
```

---

## ✅ What Works

### 1. State Management
- ✅ Session creation and tracking
- ✅ Context management
- ✅ Decision history
- ✅ Checkpoint system
- ✅ Recovery from checkpoints

### 2. Error Handling
- ✅ Error code system (E001-E010)
- ✅ HALT protocol
- ✅ Retry logic
- ✅ Fallback mechanisms
- ✅ Error logging

### 3. Interactive CLI
- ✅ Create sessions
- ✅ Create stories
- ✅ Create checkpoints
- ✅ Show status
- ✅ Help system

### 4. Documentation
- ✅ 260+ markdown files
- ✅ 18 procedures
- ✅ 21 agents
- ✅ 60+ skills
- ✅ 8 templates (structure)

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| `START-HERE.md` | Entry point for AI agents |
| `MINIMAL-WORKING-README.md` | Minimal working version guide |
| `IMPLEMENTATION-STATUS.md` | Current status and progress |
| `PARTY-MODE-REVIEW-ROUND3-DEEPDIVE.md` | Deep review results |
| `CRITICAL-STATUS.md` | Critical issues status |

---

## 🔧 How to Use

### Option 1: Interactive CLI

```bash
cd genesis-mk2
python agenkit.py --interactive

# Commands:
# create-session [name]   Create new session
# create-story <title>    Create new story
# checkpoint [desc]       Create checkpoint
# status                  Show current status
# help                    Show help
# exit                    Exit
```

### Option 2: Python API

```python
from core.state.state_manager import StateManager
from core.errors.error_handler import ErrorHandler

# Initialize
state = StateManager("project_path")
errors = ErrorHandler("logs_path")

# Create session
session = state.create_session("session_id", "project_id", "User")

# Create context
context = state.create_context("ctx_001", "session_id", "Summary")

# Add decision
decision = state.add_decision("session_id", "topic", "decision", "rationale")

# Create checkpoint
checkpoint = state.create_checkpoint("manual", "Description")

# Handle errors
try:
    # Your code here
    pass
except Exception as e:
    error = errors.create_error("E006", str(e))
    errors.handle_error(error)
```

### Option 3: Direct File Access

State is stored in `.agenkit/` directory:
- `state/session.json` - Current session
- `state/context.json` - Active context
- `state/decisions.json` - Decision history
- `state/checkpoints/` - Save points
- `logs/errors.log` - Error log

---

## 📊 Statistics

- **Total Files:** 260+
- **Markdown Files:** 260+
- **Procedures:** 18
- **Agents:** 21
- **Skills:** 60+
- **Templates:** 8
- **Core Modules:** 2 (state, errors)
- **Lines of Code:** ~1,500+

---

## 🎯 Use Cases

### For Learning:
- Study state management patterns
- Learn error handling best practices
- Understand workflow design
- Reference for your own projects

### For Development:
- Track project state
- Create and manage stories
- Create checkpoints before changes
- Log and handle errors
- Monitor session progress

### For Integration:
- Use `StateManager` in your code
- Use `ErrorHandler` for error management
- Extend with your own features
- Build on top of this foundation

---

## ⚠️ Known Limitations

### Not Yet Implemented:
- ❌ Workflow execution engine
- ❌ Agent orchestration system
- ❌ Skill execution engine
- ❌ AI model integration
- ❌ Runnable template code
- ❌ Full GUI dashboard

### These are documented in:
- `IMPLEMENTATION-STATUS.md`
- `MINIMAL-WORKING-README.md`

---

## 🚀 Roadmap

### Phase 1 (Complete):
- ✅ State management system
- ✅ Error handling system
- ✅ Interactive CLI
- ✅ Documentation

### Phase 2 (Next):
- ⏳ Workflow execution engine
- ⏳ Agent orchestration
- ⏳ Skill execution
- ⏳ AI integration

### Phase 3 (Future):
- ⏳ Full GUI dashboard
- ⏳ Plugin system
- ⏳ Multi-model support
- ⏳ Enterprise features

---

## 📄 License

MIT License - Free to use, modify, and distribute.

---

## 🤝 Contributing

Contributions welcome! Please read:
- `START-HERE.md` for framework overview
- `IMPLEMENTATION-STATUS.md` for current status
- `MINIMAL-WORKING-README.md` for working examples

---

## 📞 Support

- **Documentation:** See all .md files in genesis-mk2/
- **Issues:** Check IMPLEMENTATION-STATUS.md for known issues
- **Examples:** See agenkit.py and core/ for working code

---

**Genesis MK2 v1.0.0**
*Universal AI Development Framework*
*Core Framework - Production Ready*

*Location: genesis-mk2/*
