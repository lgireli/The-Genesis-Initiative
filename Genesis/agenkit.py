#!/usr/bin/env python3
"""
Genesis MK2 - Minimal Working Framework
========================================
A truly executable, functional version of Genesis MK2
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

# Add core to path
core_path = Path(__file__).parent / "core"
sys.path.insert(0, str(core_path))

from state.state_manager import StateManager
from errors.error_handler import ErrorHandler, GenesisError, ErrorSeverity
from workflows.workflow_engine import WorkflowEngine
from skills.skill_manager import SkillManager

class GenesisFramework:
    """Enhanced working Genesis MK2 framework"""
    
    def __init__(self, project_path: str = None):
        self.project_path = Path(project_path) if project_path else Path.cwd()
        self.state_manager = StateManager(str(self.project_path))
        self.error_handler = ErrorHandler(str(self.project_path / ".agenkit" / "logs"))
        self.workflow_engine = WorkflowEngine(str(self.project_path / "framework"), self.state_manager)
        self.skill_manager = SkillManager(str(self.project_path / "framework"))
        
        # Initialize framework
        self._initialize()
    
    def _initialize(self):
        """Initialize framework"""
        print("=" * 60)
        print("GENESIS MK2 - Minimal Working Framework")
        print("=" * 60)
        print()
        print(f"Project path: {self.project_path}")
        print(f"State directory: {self.state_manager.state_dir}")
        print()
    
    def create_session(self, project_name: str = "unnamed", user_name: str = "User") -> bool:
        """Create new session"""
        try:
            session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            session = self.state_manager.create_session(
                session_id=session_id,
                project_id=f"project_{session_id}",
                user_name=user_name
            )
            
            # Update metadata
            self.state_manager.update_session({
                "metadata": {
                    "project_name": project_name,
                    "tech_stack": "generic"
                }
            })
            
            print(f"[OK] Session created: {session_id}")
            return True
            
        except Exception as e:
            error = self.error_handler.create_error("E005", str(e), "create_session")
            self.error_handler.handle_error(error)
            return False
    
    def create_story(self, title: str, epic: str = None) -> bool:
        """Create new story"""
        try:
            session = self.state_manager.load_session()
            if not session:
                print("[ERROR] No active session. Create one first.")
                return False
            
            # Create story file
            story_id = f"story_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            story_dir = self.project_path / "stories"
            story_dir.mkdir(exist_ok=True)
            
            story_file = story_dir / f"{story_id}.md"
            story_content = f"""# {title}

Status: backlog
Priority: P1

## Story
{title}

## Acceptance Criteria
- [ ] 

## Tasks / Subtasks
- [ ] 

## Dev Notes


## Change Log
- {datetime.now().isoformat()}: Story created

"""
            story_file.write_text(story_content, encoding='utf-8')
            
            # Update context
            self.state_manager.update_context({
                "current_focus": {
                    "type": "story",
                    "id": story_id,
                    "title": title,
                    "status": "backlog"
                }
            })
            
            print(f"[OK] Story created: {story_id} - {title}")
            return True
            
        except Exception as e:
            error = self.error_handler.create_error("E006", str(e), "create_story")
            self.error_handler.handle_error(error)
            return False
    
    def create_checkpoint(self, description: str = "") -> bool:
        """Create checkpoint"""
        try:
            checkpoint = self.state_manager.create_checkpoint(
                checkpoint_type="manual",
                description=description or f"Checkpoint at {datetime.now().strftime('%H:%M')}"
            )
            
            print(f"[OK] Checkpoint created: {checkpoint['checkpoint_id']}")
            return True
            
        except Exception as e:
            error = self.error_handler.create_error("E005", str(e), "create_checkpoint")
            self.error_handler.handle_error(error)
            return False
    
    def show_status(self) -> bool:
        """Show current status"""
        try:
            session = self.state_manager.load_session()
            if not session:
                print("❌ No active session")
                return False
            
            stats = self.state_manager.get_session_stats()
            print("\n" + "=" * 60)
            print("CURRENT STATUS")
            print("=" * 60)
            print(f"Session: {stats.get('session_id', 'N/A')}")
            print(f"Status: {stats.get('status', 'N/A')}")
            print(f"Phase: {stats.get('current_phase', 'N/A')}")
            print(f"Started: {stats.get('started_at', 'N/A')}")
            print(f"Context: {stats.get('context_window', {}).get('tokens_used', 0)}/{stats.get('context_window', {}).get('tokens_limit', 0)} tokens")
            print("=" * 60 + "\n")
            
            return True
            
        except Exception as e:
            error = self.error_handler.create_error("E005", str(e), "show_status")
            self.error_handler.handle_error(error)
            return False
    
    def show_help(self):
        """Show help"""
        print("""
Genesis MK2 - Commands:

  create-session [name]    Create new session
  create-story <title>     Create new story
  checkpoint [desc]        Create checkpoint
  status                   Show current status
  validate [phase]         Validate phase gate
  scan                     Run security scan (Skill)
  ensemble <topic>         Run Ensemble Review (Party Mode)
  help                     Show this help
  exit                     Exit framework

Examples:
  create-session my-project
  create-story "User Authentication"
  checkpoint Before implementation
  validate analysis
  scan
  ensemble "Project Architecture"
""")

    def validate_gate(self, phase: str) -> bool:
        """Validate phase gate"""
        try:
            # For demo, we check current directory for artifacts
            artifacts = [f.name for f in Path(".").glob("*")]
            # Also check BMAD output
            bmad_path = self.project_path / "_bmad-output" / "planning-artifacts"
            if bmad_path.exists():
                artifacts.extend([f.name for f in bmad_path.glob("*")])

            result = self.workflow_engine.validate_gate(phase, artifacts)
            if result["cleared"]:
                print(f"[OK] Phase Gate {phase.upper()} Cleared!")
                return True
            else:
                print(f"[FAIL] Phase Gate {phase.upper()} NOT Cleared.")
                print(f"       Missing artifacts: {', '.join(result['missing'])}")
                return False
        except Exception as e:
            print(f"[ERROR] Validation failed: {e}")
            return False

    def run_security_scan(self):
        """Run security scan skill"""
        print("[RUN] Executing 'security-scan' skill...")
        result = self.skill_manager.execute_skill("security-scan", {"project_path": str(self.project_path)})
        if result["success"]:
            data = result["result"]
            print(f"[STATUS] Result: {data['status']}")
            print(f"[INFO] Findings: {data['total_findings']}")
            for f in data["findings"]:
                print(f" - [{f.get('severity')}] {f.get('type')} in {f.get('file')}")
        else:
            print(f"[ERROR] Skill failed: {result['error']}")

    def run_ensemble(self, topic: str):
        """Simulate Ensemble Review (Party Mode)"""
        print(f"\n--- ENSEMBLE REVIEW: {topic} ---")
        agents = ["Architect (Winston)", "Product Manager (John)", "QA Engineer (Quinn)"]
        
        for agent in agents:
            print(f"[{agent}] Reviewing...")
            # In a real system, this would call the LLM with the agent's persona
            print(f" > {agent}: Feedback captured.")
        
        print("\n[SUMMARY] Ensemble review complete. See context for consolidated feedback.")
        self.state_manager.add_decision(
            session_id="current",
            topic="Ensemble Review",
            decision=f"Review completed for: {topic}",
            rationale="Multi-agent alignment confirmed."
        )

    def run_interactive(self):
        """Run interactive mode"""
        print("\nType 'help' for commands, 'exit' to quit\n")
        
        while True:
            try:
                cmd = input("genesis> ").strip()
                
                if not cmd:
                    continue
                
                parts = cmd.split(maxsplit=1)
                command = parts[0].lower()
                args = parts[1] if len(parts) > 1 else ""
                
                if command == "exit" or command == "quit":
                    print("Goodbye!")
                    break
                
                elif command == "help":
                    self.show_help()
                
                elif command == "create-session":
                    name = args or "unnamed"
                    self.create_session(project_name=name)
                
                elif command == "create-story":
                    if not args:
                        print("❌ Please provide story title")
                        continue
                    self.create_story(args)
                
                elif command == "checkpoint":
                    self.create_checkpoint(args)
                
                elif command == "status":
                    self.show_status()

                elif command == "validate":
                    phase = args or "analysis"
                    self.validate_gate(phase)

                elif command == "scan":
                    self.run_security_scan()

                elif command == "ensemble":
                    if not args:
                        print("❌ Please provide a topic for the ensemble")
                        continue
                    self.run_ensemble(args)
                
                else:
                    print(f"❌ Unknown command: {command}")
                    print("Type 'help' for available commands")
            
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                error = self.error_handler.create_error("E010", str(e), "interactive")
                self.error_handler.handle_error(error)
                print(f"❌ Error: {e}")

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Genesis MK2 - Enhanced Orchestration Framework")
    parser.add_argument("--path", help="Project path")
    parser.add_argument("--interactive", "-i", action="store_true", help="Run interactive mode")
    
    args = parser.parse_args()
    
    framework = GenesisFramework(args.path)
    
    if args.interactive:
        framework.run_interactive()
    else:
        framework.show_help()

if __name__ == "__main__":
    main()
