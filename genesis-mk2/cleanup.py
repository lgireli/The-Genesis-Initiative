#!/usr/bin/env python3
"""
Genesis MK2 - Cleanup Tool
==========================
Safely removes the framework state and logs from a project.
"""

from pathlib import Path
import shutil

def cleanup():
    print("=" * 60)
    print("GENESIS MK2 - PROJECT CLEANUP")
    print("=" * 60)
    
    project_root = Path(__file__).parent.parent
    state_dir = project_root / ".agenkit"
    
    if not state_dir.exists():
        print("No .agenkit directory found. Project is already clean.")
        return

    print(f"Found state directory at: {state_dir}")
    confirm = input("Are you sure you want to delete all session data and logs? (y/N): ").strip().lower()
    
    if confirm == 'y':
        try:
            shutil.rmtree(state_dir)
            print("✓ Successfully removed .agenkit directory.")
            print("Project is now clean.")
        except Exception as e:
            print(f"❌ Error during cleanup: {e}")
    else:
        print("Cleanup cancelled.")

if __name__ == "__main__":
    cleanup()
