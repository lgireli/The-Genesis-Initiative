#!/usr/bin/env python3
"""
Genesis MK2 - Workflow Engine
=============================
Parses Markdown SOPs and enforces phase gates.
"""

import re
from pathlib import Path
from typing import List, Dict, Any

class WorkflowEngine:
    def __init__(self, framework_path: str, state_manager):
        self.framework_path = Path(framework_path)
        self.state = state_manager
        # Procedures are always relative to where the framework was installed
        self.procedures_path = self.framework_path / "directives" / "procedures"

    def get_phase_checks(self, phase_name: str) -> List[str]:
        """Extracts checklist items from the phase's Markdown file."""
        procedure_file = self.procedures_path / f"{phase_name.lower()}.md"
        if not procedure_file.exists():
            return []

        with open(procedure_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find markdown checkboxes: - [ ] or - [x]
        checks = re.findall(r'- \[[ xX]\] (.*)', content)
        return checks

    def validate_gate(self, phase_name: str, artifacts: List[str]) -> Dict[str, Any]:
        """Checks if required artifacts exist for a phase gate."""
        # Simple mapping for Phase Gate 1A (Analysis)
        required_artifacts = {
            "analysis": ["product-brief.md"],
            "planning": ["prd.md", "ux-design.md"],
            "solutioning": ["architecture.md", "epics.md"],
            "implementation": ["sprint-status.yaml"]
        }

        needed = required_artifacts.get(phase_name.lower(), [])
        missing = [a for a in needed if a not in artifacts]

        return {
            "phase": phase_name,
            "cleared": len(missing) == 0,
            "missing": missing
        }
