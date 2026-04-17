#!/usr/bin/env python3
"""\nGenesis - Zero Config Bootstrap\n==================================\nInitializes the framework in a blank project folder.\n"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

def bootstrap():
    print("=" * 60)
    print("GENESIS - BOOTSTRAPPING PROJECT")
    print("=" * 60)
    
    # 1. Identify Paths
    script_path = Path(__file__).resolve()
    framework_path = script_path.parent
    project_root = framework_path.parent
    
    print(f"Framework detected at: {framework_path}")
    print(f"Project root detected at: {project_root}")
    
    # 2. Pre-Flight: Write Permission Check
    state_dir = project_root / ".agenkit"
    try:
        state_dir.mkdir(parents=True, exist_ok=True)
        test_file = state_dir / ".write_test"
        test_file.write_text("test", encoding='utf-8')
        test_file.unlink()
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR: No write permissions in {project_root}")
        print(f"Details: {e}")
        print("Please run as administrator or move the framework to a writable directory.")
        sys.exit(1)

    # Git Check
    if not (project_root / ".git").exists():
        print("\n⚠️  No Git repository detected in project root.")
        print("It is STRONGLY recommended to run 'git init' to enable versioning and checkpoints.")
    
    # 3. Session Protection: Check for existing session
    session_file = state_dir / "state" / "session.json"
    (state_dir / "state").mkdir(parents=True, exist_ok=True)
    (state_dir / "logs").mkdir(parents=True, exist_ok=True)
    
    if session_file.exists():
        print("\n⚠️  Existing session detected!")
        print("Would you like to [R]esume existing session or [S]tart fresh? (R/S)")
        choice = input("> ").strip().upper()
        if choice == 'R':
            print("✓ Resuming existing session. Bootstrap complete.")
            # Ensure SITREP is synced on resume
            try:
                import sys
                sys.path.append(str(framework_path))
                from core.state.state_manager import StateManager
                sm = StateManager(str(project_root))
                sm.sync_sitrep()
                print("✓ SITREP synchronized.")
            except Exception:
                pass
            return
        elif choice != 'S':
            print("Invalid choice. Defaulting to RESUME to prevent data loss.")
            return

    # 4. Create Initial Session
    session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    session_data = {
        "session_id": session_id,
        "project_id": f"project_{session_id}",
        "started_at": datetime.now().isoformat(),
        "status": "active",
        "current_phase": "analysis",
        "metadata": {"project_name": project_root.name, "status": "bootstrapped"}
    }
    
    with open(session_file, 'w', encoding='utf-8') as f:
        json.dump(session_data, f, indent=2)
    
    print(f"✓ Created initial session: {session_id}")
    print("\n" + "=" * 60)
    print("SUCCESS: Project is now Genesis-Ready!")
    print("\n🚀 NEXT STEP FOR THE USER:")
    print("Tell your AI agent: 'Read Genesis/START-HERE.md and begin the orchestration.'")
    print("\nInstructions for AI Agent:")
    print("1. Read START-HERE.md")
    print("2. Adopt the 'Orchestrator' persona.")
    print("3. Begin Phase 1: Analysis.")
    print("=" * 60)

if __name__ == "__main__":
    bootstrap()

