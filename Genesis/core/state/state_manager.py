#!/usr/bin/env python3
"""
Genesis MK2 - State Management Implementation
==============================================
Actual implementation of state management system
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List
import time

class StateManager:
    """Actual state management implementation with basic file locking"""
    
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.state_dir = self.project_path / ".agenkit" / "state"
        self.checkpoints_dir = self.state_dir / "checkpoints"
        self.lock_file = self.state_dir / "state.lock"
        self.sitrep_file = self.project_path / "SITREP.md"
        
        self.state_dir.mkdir(parents=True, exist_ok=True)
        self.checkpoints_dir.mkdir(parents=True, exist_ok=True)
    
    def sync_sitrep(self):
        """Synchronizes JSON state to a human-readable SITREP.md file."""
        session = self.load_session()
        if not session: return
        
        context = self.load_context() or {}
        
        content = f"""# 🚩 PROJECT SITREP (Situation Report)
> **Last Updated:** {datetime.now().isoformat()}
> **Session ID:** {session.get('session_id')}

## 📌 Current Status
- **Phase:** {session.get('current_phase', 'Unknown').upper()}
- **Project:** {session.get('metadata', {}).get('project_name', 'Unnamed')}
- **Status:** {session.get('status', 'Active')}

## 🎯 Current Focus
- **Active Goal:** {context.get('current_focus', {}).get('title', 'None defined')}
- **Progress:** {context.get('current_focus', {}).get('status', 'N/A')}

## ⏭️ Next Immediate Step
{context.get('next_step', 'Please define the next step in the context manager.')}

---
*This file is automatically managed by the Genesis MK2 StateManager. Do not edit manually unless updating the 'Next Immediate Step'.*
"""
        self.sitrep_file.write_text(content, encoding='utf-8')
    
    def _acquire_lock(self, timeout=5):
        """Simple lock file mechanism with stale lock recovery for Windows/Unix compatibility"""
        start_time = time.time()
        while True:
            try:
                self.lock_file.touch(exist_ok=False)
                return True
            except FileExistsError:
                # Stale lock recovery: check if lock is older than 10 minutes
                if self.lock_file.exists():
                    mtime = self.lock_file.stat().st_mtime
                    if time.time() - mtime > 600: # 10 minutes
                        self.lock_file.unlink()
                        continue
                
                if time.time() - start_time > timeout:
                    return False
                time.sleep(0.1)
    
    def update_session(self, updates: Dict[str, Any]) -> bool:
        self._acquire_lock()
        try:
            session = self.load_session()
            if not session: return False
            session.update(updates)
            session_file = self.state_dir / "session.json"
            with open(session_file, 'w', encoding='utf-8') as f:
                json.dump(session, f, indent=2)
            self.sync_sitrep() # Automatic sync
            return True
        finally:
            self._release_lock()

    def update_context(self, updates: Dict[str, Any]) -> bool:
        """Update context and sync SITREP"""
        self._acquire_lock()
        try:
            context = self.load_context()
            if not context: return False
            context.update(updates)
            context["last_updated"] = datetime.now().isoformat()
            context_file = self.state_dir / "context.json"
            with open(context_file, 'w', encoding='utf-8') as f:
                json.dump(context, f, indent=2)
            self.sync_sitrep() # Automatic sync
            return True
        finally:
            self._release_lock()

    
    def load_session(self) -> Optional[Dict[str, Any]]:
        session_file = self.state_dir / "session.json"
        if not session_file.exists():
            return None
        with open(session_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def update_session(self, updates: Dict[str, Any]) -> bool:
        self._acquire_lock()
        try:
            session = self.load_session()
            if not session: return False
            session.update(updates)
            session_file = self.state_dir / "session.json"
            with open(session_file, 'w', encoding='utf-8') as f:
                json.dump(session, f, indent=2)
            return True
        finally:
            self._release_lock()

    
    def create_context(self, context_id: str, session_id: str, summary: str = "") -> Dict[str, Any]:
        """Create active context"""
        context_data = {
            "context_id": context_id,
            "session_id": session_id,
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "summary": summary,
            "key_decisions": [],
            "open_questions": [],
            "current_focus": {
                "type": "none",
                "id": None,
                "title": None,
                "status": None
            },
            "recent_changes": [],
            "memory": {
                "short_term": [],
                "long_term": []
            }
        }
        
        # Save context
        context_file = self.state_dir / "context.json"
        with open(context_file, 'w', encoding='utf-8') as f:
            json.dump(context_data, f, indent=2)
        
        return context_data
    
    def load_context(self) -> Optional[Dict[str, Any]]:
        """Load current context"""
        context_file = self.state_dir / "context.json"
        if not context_file.exists():
            return None
        
        with open(context_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def update_context(self, updates: Dict[str, Any]) -> bool:
        """Update context data"""
        context = self.load_context()
        if not context:
            return False
        
        context.update(updates)
        context["last_updated"] = datetime.now().isoformat()
        
        context_file = self.state_dir / "context.json"
        with open(context_file, 'w', encoding='utf-8') as f:
            json.dump(context, f, indent=2)
        
        return True
    
    def add_decision(self, session_id: str, topic: str, decision: str, 
                    rationale: str, alternatives: List[str] = None,
                    impact: str = "medium", reversible: bool = True) -> Dict[str, Any]:
        """Add decision to history"""
        decisions_file = self.state_dir / "decisions.json"
        
        # Load existing decisions
        decisions = []
        if decisions_file.exists():
            with open(decisions_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                decisions = data.get("decisions", [])
        
        # Add new decision
        new_decision = {
            "id": f"dec_{len(decisions) + 1:03d}",
            "session_id": session_id,
            "timestamp": datetime.now().isoformat(),
            "topic": topic,
            "decision": decision,
            "alternatives_considered": alternatives or [],
            "rationale": rationale,
            "impact": impact,
            "reversible": reversible
        }
        
        decisions.append(new_decision)
        
        # Save decisions
        with open(decisions_file, 'w', encoding='utf-8') as f:
            json.dump({
                "decisions": decisions,
                "total_decisions": len(decisions),
                "last_updated": datetime.now().isoformat()
            }, f, indent=2)
        
        return new_decision
    
    def create_checkpoint(self, checkpoint_type: str = "manual", 
                         description: str = "", state_snapshot: Dict = None) -> Dict[str, Any]:
        """Create checkpoint"""
        checkpoint_id = f"checkpoint_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        checkpoint_data = {
            "checkpoint_id": checkpoint_id,
            "session_id": self.load_session()["session_id"] if self.load_session() else None,
            "created_at": datetime.now().isoformat(),
            "type": checkpoint_type,
            "description": description,
            "state_snapshot": state_snapshot or {},
            "context_snapshot": {},
            "file_state": {},
            "can_restore": True
        }
        
        # Save checkpoint
        checkpoint_file = self.checkpoints_dir / f"{checkpoint_id}.json"
        with open(checkpoint_file, 'w', encoding='utf-8') as f:
            json.dump(checkpoint_data, f, indent=2)
        
        return checkpoint_data
    
    def list_checkpoints(self) -> List[Dict[str, Any]]:
        """List all checkpoints"""
        checkpoints = []
        
        for checkpoint_file in self.checkpoints_dir.glob("*.json"):
            with open(checkpoint_file, 'r', encoding='utf-8') as f:
                checkpoints.append(json.load(f))
        
        # Sort by date (newest first)
        checkpoints.sort(key=lambda x: x["created_at"], reverse=True)
        
        return checkpoints
    
    def restore_checkpoint(self, checkpoint_id: str) -> bool:
        """Restore from checkpoint"""
        checkpoint_file = self.checkpoints_dir / f"{checkpoint_id}.json"
        if not checkpoint_file.exists():
            return False
        
        with open(checkpoint_file, 'r', encoding='utf-8') as f:
            checkpoint = json.load(f)
        
        # Restore session
        if "state_snapshot" in checkpoint:
            self.update_session(checkpoint["state_snapshot"])
        
        # Restore context if available
        if "context_snapshot" in checkpoint:
            self.update_context(checkpoint["context_snapshot"])
        
        return True
    
    def get_session_stats(self) -> Dict[str, Any]:
        """Get session statistics"""
        session = self.load_session()
        if not session:
            return {}
        
        return {
            "session_id": session["session_id"],
            "status": session["status"],
            "current_phase": session["current_phase"],
            "started_at": session["started_at"],
            "context_window": session["context_window"]
        }

# Example usage
if __name__ == "__main__":
    # Test the state manager
    state = StateManager("genesis-mk2")
    
    # Create session
    session = state.create_session(
        session_id="session_20260416_001",
        project_id="project_xyz",
        user_name="John Doe"
    )
    print(f"Created session: {session['session_id']}")
    
    # Create context
    context = state.create_context(
        context_id="ctx_001",
        session_id="session_20260416_001",
        summary="Working on user authentication"
    )
    print(f"Created context: {context['context_id']}")
    
    # Add decision
    decision = state.add_decision(
        session_id="session_20260416_001",
        topic="database_choice",
        decision="postgresql",
        rationale="Better for relational data",
        alternatives=["mongodb", "sqlite"],
        impact="high"
    )
    print(f"Added decision: {decision['id']}")
    
    # Create checkpoint
    checkpoint = state.create_checkpoint(
        checkpoint_type="manual",
        description="Before major implementation",
        state_snapshot={
            "current_phase": "implementation",
            "stories_completed": 3
        }
    )
    print(f"Created checkpoint: {checkpoint['checkpoint_id']}")
    
    # Get stats
    stats = state.get_session_stats()
    print(f"Session stats: {stats}")
    
    print("\n✅ State management implementation working!")
