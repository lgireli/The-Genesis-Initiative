#!/usr/bin/env python3
"""
Genesis MK2 - Memory Manager
============================
Handles persistent learnings and decision retrieval.
"""

from pathlib import Path
import json
from typing import List, Dict, Any

class MemoryManager:
    def __init__(self, state_dir: str):
        self.state_dir = Path(state_dir)
        self.memory_file = self.state_dir / "memory.json"
        
    def learn(self, concept: str, details: str):
        """Adds a new learning to the persistent memory."""
        memory = self._load()
        memory["learnings"].append({
            "concept": concept,
            "details": details,
            "timestamp": "now"
        })
        self._save(memory)

    def retrieve_relevant(self, query: str) -> List[Dict]:
        """Simple keyword-based retrieval for demonstration."""
        memory = self._load()
        # In a real system, use vector embeddings here
        relevant = [m for m in memory["learnings"] if query.lower() in m["concept"].lower()]
        return relevant

    def _load(self) -> Dict:
        if not self.memory_file.exists():
            return {"learnings": []}
        with open(self.memory_file, 'r') as f:
            return json.load(f)

    def _save(self, data: Dict):
        with open(self.memory_file, 'w') as f:
            json.dump(data, f, indent=2)
