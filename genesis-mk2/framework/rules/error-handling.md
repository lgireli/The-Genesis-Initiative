# Genesis MK2 Error Handling Protocol

> **Purpose:** Standardized error handling and recovery
> **Version:** 1.0.0
> **Status:** CRITICAL FIX - Error Recovery

---

## 🚨 Error Code System

### Error Categories

| Code | Category | Severity | Action |
|------|----------|----------|--------|
| **E001** | Configuration | Critical | HALT |
| **E002** | File System | Critical | HALT |
| **E003** | Agent Routing | High | Retry |
| **E004** | Skill Loading | High | Fallback |
| **E005** | State Management | Critical | Recovery |
| **E006** | Validation | Medium | Fix & Continue |
| **E007** | API/External | High | Retry/Fallback |
| **E008** | User Input | Low | Request Correction |
| **E009** | Resource | Medium | Optimize |
| **E010** | Unknown | Critical | HALT & Report |

---

## 🛑 HALT Protocol

### When to HALT:

1. **Critical errors** (E001-E005)
2. **3 consecutive failures** on same task
3. **Missing configuration** required for task
4. **Ambiguous requirements** that cannot be clarified
5. **User confirmation** required for destructive action
6. **Budget exceeded** threshold

### HALT Message Format:

```
🚨 HALT: [Error Code] - [Error Name]

Issue: [Specific description]
Location: [File/Line/Context]
Impact: [What is blocked]
Required: [What is needed to proceed]

Options:
1. [Action 1]
2. [Action 2]
3. [Action 3]

Type number to proceed or 'help' for more info.
```

### Example HALT Message:

```
🚨 HALT: E001 - Configuration Missing

Issue: Required configuration file not found
Location: .agenkit/config.json
Impact: Cannot proceed with implementation
Required: Valid configuration file

Options:
1. Create config file with defaults
2. Provide custom configuration
3. Abort and exit

Type number or 'help' for more info.
```

---

## 🔄 Retry Logic

### Retry Strategy:

| Error Code | Max Retries | Delay | Backoff |
|------------|-------------|-------|---------|
| E003 | 3 | 1s | Exponential |
| E004 | 2 | 1s | Linear |
| E007 | 3 | 2s | Exponential |
| E009 | 2 | 5s | Linear |

### Retry Implementation:

```python
def retry_operation(operation, max_retries=3):
    for attempt in range(max_retries):
        try:
            return operation()
        except Exception as e:
            if attempt == max_retries - 1:
                raise Error(e.error_code, str(e))
            delay = 2 ** attempt  # Exponential backoff
            wait(delay)
```

---

## 🛡️ Fallback Mechanisms

### Skill Fallback Chain:

```
Primary Skill → Fallback 1 → Fallback 2 → Manual
```

**Example:**
```
react-best-practices.md
  → frontend-design.md (fallback)
  → clean-code.md (fallback)
  → Manual intervention
```

### Agent Fallback Chain:

```
Primary Agent → Backup Agent → Generalist → Orchestrator
```

**Example:**
```
frontend-specialist.md
  → backend-specialist.md (fallback)
  → developer.md (fallback)
  → orchestrator.md (escalation)
```

---

## 📋 Error Recovery Procedures

### E001 - Configuration Missing

**Recovery Steps:**
1. Check if config file exists
2. If missing, create with defaults
3. Ask user to review/modify
4. Proceed with confirmed config

**Default Config:**
```json
{
  "project": {
    "name": "unnamed",
    "type": "web",
    "stack": "generic"
  },
  "agents": ["orchestrator"],
  "skills": ["clean-code"],
  "approval_required": []
}
```

### E002 - File System Error

**Recovery Steps:**
1. Verify file path exists
2. Check permissions
3. Create missing directories
4. Retry operation
5. If still fails, HALT with details

### E003 - Agent Routing Failed

**Recovery Steps:**
1. Log routing failure
2. Try fallback agent
3. If still fails, escalate to orchestrator
4. Ask user for agent selection

### E004 - Skill Loading Failed

**Recovery Steps:**
1. Check skill file exists
2. Verify skill dependencies
3. Load fallback skill
4. If still fails, skip skill and continue

### E005 - State Management Error

**Recovery Steps:**
1. Check state file integrity
2. Load last known good checkpoint
3. Recover context
4. Notify user of recovery
5. Resume from checkpoint

### E006 - Validation Failed

**Recovery Steps:**
1. Log validation error
2. Identify specific failure
3. Fix issue automatically if possible
4. If manual fix needed, HALT with instructions
5. Retry validation after fix

### E007 - External API Error

**Recovery Steps:**
1. Check API availability
2. Retry with exponential backoff
3. Use cached data if available
4. If still fails, use mock data
5. Notify user of degraded mode

### E008 - User Input Invalid

**Recovery Steps:**
1. Validate input format
2. Provide clear error message
3. Show expected format
4. Request corrected input
5. Retry with new input

### E009 - Resource Exhaustion

**Recovery Steps:**
1. Check available resources
2. Optimize operation (reduce memory, etc.)
3. Process in smaller batches
4. If still fails, HALT with resource requirements

### E010 - Unknown Error

**Recovery Steps:**
1. Log full error details
2. Capture stack trace
3. Create error report
4. HALT and notify user
5. Provide error ID for support

---

## 📊 Error Logging Format

**File:** `.agenkit/logs/errors.log`

```json
{
  "timestamp": "2026-04-16T10:30:00Z",
  "error_code": "E003",
  "error_name": "Agent Routing Failed",
  "severity": "high",
  "session_id": "session_20260416_001",
  "context": {
    "current_phase": "implementation",
    "current_story": "story_123",
    "agent_attempted": "frontend-specialist"
  },
  "details": {
    "message": "Agent file not found",
    "file_path": "framework/AGENTS/frontend-specialist.md",
    "actual_file": "framework/AGENTS/frontend-specialist.md"
  },
  "action_taken": "Retried with fallback agent",
  "resolved": true,
  "resolution_time_ms": 1500
}
```

---

## 🚦 Error Severity Levels

### CRITICAL (Red) - Must HALT:
- E001: Configuration
- E002: File System
- E005: State Management
- E010: Unknown

### HIGH (Orange) - Retry or Fallback:
- E003: Agent Routing
- E004: Skill Loading
- E007: External API

### MEDIUM (Yellow) - Fix and Continue:
- E006: Validation
- E009: Resource

### LOW (Blue) - Request Correction:
- E008: User Input

---

## 🎯 Error Prevention

### Before Implementation:

1. ✅ **Pre-flight checklist**
   - Config exists
   - Required files present
   - Agent files exist
   - Skills available
   - State directory writable

2. ✅ **Validation checks**
   - Validate user input
   - Validate file paths
   - Validate agent selection
   - Validate skill dependencies

3. ✅ **Resource checks**
   - Check disk space
   - Check memory availability
   - Check API availability

### During Implementation:

1. ✅ **Monitor state**
   - Track context window
   - Monitor error rate
   - Check resource usage

2. ✅ **Auto-recovery**
   - Auto-checkpoint on errors
   - Auto-retry on transient errors
   - Auto-fallback on failures

---

## 📝 Error Handler Implementation

```python
class ErrorHandler:
    def __init__(self):
        self.error_log = []
        self.halt_conditions = ['E001', 'E002', 'E005', 'E010']
    
    def handle_error(self, error, context):
        error_code = error.get('code', 'E010')
        
        # Log error
        self._log_error(error, context)
        
        # Check if HALT required
        if error_code in self.halt_conditions:
            self._halt(error, context)
            return False
        
        # Check if retry possible
        if self._can_retry(error_code):
            return self._retry(error, context)
        
        # Check if fallback possible
        if self._can_fallback(error_code):
            return self._fallback(error, context)
        
        # Request user input
        return self._request_user_input(error, context)
    
    def _halt(self, error, context):
        """Execute HALT protocol"""
        message = self._format_halt_message(error, context)
        print(message)
        return False
    
    def _retry(self, error, context):
        """Execute retry logic"""
        max_retries = self._get_retry_count(error['code'])
        # Implement retry with backoff
        ...
    
    def _fallback(self, error, context):
        """Execute fallback logic"""
        # Try fallback agent/skill
        ...
```

---

## ✅ Implementation Checklist

- [ ] Define error code system
- [ ] Implement HALT protocol
- [ ] Implement retry logic
- [ ] Implement fallback mechanisms
- [ ] Create error logging format
- [ ] Add pre-flight checks
- [ ] Add auto-checkpoint on errors
- [ ] Test all error scenarios
- [ ] Document error codes
- [ ] Add error recovery procedures

---

*Error Handling Protocol v1.0.0*
*CRITICAL FIX - Error Recovery*
