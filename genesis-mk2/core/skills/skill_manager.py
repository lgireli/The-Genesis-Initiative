#!/usr/bin/env python3
"""
Genesis MK2 - Skill Manager
===========================
Dynamically loads and executes Python-based skills.
"""

import importlib.util
import sys
from pathlib import Path
from typing import Any, Dict, Optional

class SkillManager:
    def __init__(self, framework_path: str):
        self.framework_path = Path(framework_path)
        self.skills_base = self.framework_path / "skills"

    def _validate_context(self, skill_name: str, context: Dict[str, Any]) -> bool:
        """Ensure required context keys are present for the skill."""
        # Basic schema: Most skills require 'project_path'
        if "project_path" not in context:
            return False
        return True

    def execute_skill(self, skill_name: str, context: Dict[str, Any]) -> Dict[str, Any]:
        if not self._validate_context(skill_name, context):
            return {
                "success": False,
                "error": f"Missing required context for skill {skill_name}. 'project_path' is mandatory."
            }
        
        skill_dir = self.skills_base / skill_name
        skill_script = skill_dir / "SKILL.py"
        
        if not skill_script.exists():
            return {
                "success": False,
                "error": f"Skill script not found: {skill_script}"
            }
        
        try:
            spec = importlib.util.spec_from_file_location(f"skill_{skill_name}", skill_script)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "execute"):
                result = module.execute(context)
                return {"success": True, "result": result}
            else:
                return {"success": False, "error": "Skill script missing execute() function"}
        except Exception as e:
            return {"success": False, "error": str(e)}

