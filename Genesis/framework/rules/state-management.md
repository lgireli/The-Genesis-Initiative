# Genesis MK2 State Management Specification

> **Purpose:** Define state file format for context persistence and session recovery
> **Version:** 1.0.0
> **Status:** CRITICAL FIX - Context Management

---

## 📁 State File Location

**Default:** `.agenkit/state/`

**Files:**
- `session.json` - Current session state
- `decisions.json` - Decision history
- `context.json` - Active context
- `checkpoints/` - Save points

---

## 🗂️ Session State Format

**File:** `.agenkit/state/session.json`

```json
{
  "session_id": "session_20260416_001",
  "project_id": "project_xyz",
  "started_at": "2026-04-16T10:00:00Z",
  "status": "active",
  "current_phase": "implementation",
  "current_story_id": null,
  "current_task_id": null,
  "context_window": {
    "tokens_used": 45000,
    "tokens_limit": 128000,
    "last_updated": "2026-04-16T10:30:00Z"
  },
  "metadata": {
    "user_name": "John Doe",
    "project_name": "My App",
    "tech_stack": "nextjs-supabase"
  }
}
```

---

## 🧠 Active Context Format

**File:** `.agenkit/state/context.json`

```json
{
  "context_id": "ctx_20260416_001",
  "session_id": "session_20260416_001",
  "created_at": "2026-04-16T10:00:00Z",
  "last_updated": "2026-04-16T10:30:00Z",
  "summary": "Brief summary of current state",
  "key_decisions": [
    {
      "id": "dec_001",
      "timestamp": "2026-04-16T10:05:00Z",
      "topic": "database_choice",
      "decision": "postgresql",
      "rationale": "Better for relational data"
    }
  ],
  "open_questions": [
    {
      "id": "q_001",
      "question": "What authentication method?",
      "assigned_to": "product-manager",
      "status": "pending"
    }
  ],
  "current_focus": {
    "type": "story",
    "id": "story_123",
    "title": "User Authentication",
    "status": "in-progress"
  },
  "recent_changes": [
    {
      "file": "src/auth.ts",
      "action": "modified",
      "timestamp": "2026-04-16T10:25:00Z"
    }
  ],
  "memory": {
    "short_term": "Last 5 interactions",
    "long_term": "Key project decisions"
  }
}
```

---

## 📝 Decision History Format

**File:** `.agenkit/state/decisions.json`

```json
{
  "decisions": [
    {
      "id": "dec_001",
      "session_id": "session_20260416_001",
      "timestamp": "2026-04-16T10:05:00Z",
      "agent": "product-manager",
      "topic": "database_choice",
      "decision": "postgresql",
      "alternatives_considered": ["mongodb", "sqlite"],
      "rationale": "Better for relational data, ACID compliance",
      "impact": "high",
      "reversible": false
    },
    {
      "id": "dec_002",
      "session_id": "session_20260416_001",
      "timestamp": "2026-04-16T10:10:00Z",
      "agent": "frontend-specialist",
      "topic": "ui_framework",
      "decision": "tailwind-css",
      "alternatives_considered": ["material-ui", "chakra-ui"],
      "rationale": "Utility-first, fast development",
      "impact": "medium",
      "reversible": true
    }
  ],
  "total_decisions": 2,
  "last_updated": "2026-04-16T10:10:00Z"
}
```

---

## 💾 Checkpoint Format

**Directory:** `.agenkit/state/checkpoints/`

**File:** `checkpoint_20260416_103000.json`

```json
{
  "checkpoint_id": "checkpoint_20260416_103000",
  "session_id": "session_20260416_001",
  "created_at": "2026-04-16T10:30:00Z",
  "type": "manual",
  "description": "Before major implementation",
  "state_snapshot": {
    "current_phase": "implementation",
    "current_story_id": "story_123",
    "stories_completed": 3,
    "stories_total": 10,
    "progress_percent": 30
  },
  "context_snapshot": {
    "summary": "3 stories completed, working on authentication",
    "key_decisions": ["dec_001", "dec_002"],
    "open_questions": ["q_001"]
  },
  "file_state": {
    "total_files": 45,
    "modified_files": ["src/auth.ts", "src/user.ts"],
    "new_files": ["tests/auth.test.ts"]
  },
  "can_restore": true
}
```

---

## 🔄 Checkpoint Types

| Type | When to Create | Auto/Manual |
|------|---------------|-------------|
| **auto_start** | Session begins | Auto |
| **auto_phase** | Phase change | Auto |
| **auto_story** | Story complete | Auto |
| **manual** | User request | Manual |
| **error_recovery** | Before error | Auto |
| **deployment** | Before deploy | Manual |

---

## 📋 State Operations

### Create Checkpoint
```json
POST /api/checkpoints
{
  "type": "manual",
  "description": "Before major change"
}
```

### Restore Checkpoint
```json
POST /api/checkpoints/restore
{
  "checkpoint_id": "checkpoint_20260416_103000"
}
```

### Save Context
```json
POST /api/context/save
{
  "summary": "Current state summary",
  "key_decisions": [...],
  "open_questions": [...]
}
```

### Load Context
```json
GET /api/context/load
```

---

## 🎯 Context Window Management

### When Context Fills:

1. **Auto-checkpoint** current state
2. **Summarize** old decisions
3. **Keep** recent 5 interactions
4. **Archive** older context
5. **Notify** user: "Context checkpoint created"

### Context Summary Format:
```json
{
  "summary": "Completed 3 stories, working on auth",
  "decisions_made": 5,
  "files_modified": 12,
  "tests_written": 8,
  "open_issues": 2
}
```

---

## 🔒 State File Permissions

**Recommended:**
- Read/Write: Agent
- Read: Human user
- No Execute

**Backup:**
- Auto-backup to `.agenkit/state/backups/`
- Keep last 10 checkpoints
- Compress old checkpoints

---

## 🚨 State Recovery Protocol

### On Session Crash:

1. **Detect** missing session file
2. **Search** for latest checkpoint
3. **Load** checkpoint state
4. **Restore** context
5. **Notify** user: "Session restored from checkpoint"
6. **Resume** from last known state

### Recovery Steps:
```
1. Check .agenkit/state/session.json
2. If missing, find latest checkpoint
3. Load checkpoint data
4. Update session.json
5. Restore context.json
6. Resume workflow
```

---

## 📊 State File Size Limits

| File | Max Size | Action When Exceeded |
|------|----------|---------------------|
| session.json | 10KB | Archive old sessions |
| context.json | 50KB | Summarize older entries |
| decisions.json | 100KB | Archive to separate file |
| checkpoints/ | 1GB | Compress old checkpoints |

---

## ✅ Implementation Checklist

- [ ] Create state directory structure
- [ ] Implement session.json format
- [ ] Implement context.json format
- [ ] Implement decisions.json format
- [ ] Implement checkpoint system
- [ ] Add auto-checkpoint triggers
- [ ] Add context summarization
- [ ] Add recovery protocol
- [ ] Add backup system
- [ ] Test crash recovery

---

*State Management Specification v1.0.0*
*CRITICAL FIX - Context Persistence*
