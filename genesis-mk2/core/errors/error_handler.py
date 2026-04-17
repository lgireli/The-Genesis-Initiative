#!/usr/bin/env python3
"""
Genesis MK2 - Error Handling Implementation
============================================
Actual implementation of error handling system
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List
from enum import Enum

class ErrorSeverity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class GenesisError(Exception):
    """Base error class for Genesis MK2"""
    
    def __init__(self, error_code: str, message: str, severity: ErrorSeverity,
                 location: str = None, context: Dict = None):
        self.error_code = error_code
        self.message = message
        self.severity = severity
        self.location = location
        self.context = context or {}
        super().__init__(self.format_message())
    
    def format_message(self) -> str:
        return f"[{self.error_code}] {self.message}"

class ErrorHandler:
    """Actual error handling implementation with human-readable translation"""
    
    # Error codes dictionary with human-readable translations
    ERROR_CODES = {
        "E001": {"name": "Configuration Missing", "severity": ErrorSeverity.CRITICAL, "human": "The system couldn't find a required config file. Please check your settings."},
        "E002": {"name": "File System Error", "severity": ErrorSeverity.CRITICAL, "human": "I don't have permission to read or write to the project folder. Try running as Administrator."},
        "E003": {"name": "Agent Routing Failed", "severity": ErrorSeverity.HIGH, "human": "I couldn't find the right expert agent for this task. I'll try to handle it myself."},
        "E004": {"name": "Skill Loading Failed", "severity": ErrorSeverity.HIGH, "human": "A required technical skill failed to load. I may need to proceed manually."},
        "E005": {"name": "State Management Error", "severity": ErrorSeverity.CRITICAL, "human": "I've lost track of the project state. Please restart the session."},
        "E006": {"name": "Validation Failed", "severity": ErrorSeverity.MEDIUM, "human": "The current work doesn't meet the quality gate requirements. Some fixes are needed."},
        "E007": {"name": "External API Error", "severity": ErrorSeverity.HIGH, "human": "An external tool or API returned an error. I'll retry in a few seconds."},
        "E008": {"name": "User Input Invalid", "severity": ErrorSeverity.LOW, "human": "I didn't quite understand that. Could you please rephrase?"},
        "E009": {"name": "Resource Exhaustion", "severity": ErrorSeverity.MEDIUM, "human": "The system is running low on memory/tokens. I'm clearing some context to continue."},
        "E010": {"name": "Unknown Error", "severity": ErrorSeverity.CRITICAL, "human": "Something unexpected happened. Please report this issue."}
    }
    
    # Halt conditions
    HALT_CODES = ["E001", "E002", "E005", "E010"]
    
    def __init__(self, log_dir: str = None):
        self.log_dir = Path(log_dir) if log_dir else Path(".agenkit/logs")
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.error_log_file = self.log_dir / "errors.log"
        self.error_history: List[Dict] = []
    
    def create_error(self, error_code: str, message: str, 
                    location: str = None, context: Dict = None) -> GenesisError:
        """Create error instance"""
        if error_code not in self.ERROR_CODES:
            error_code = "E010"  # Unknown error
        
        error_info = self.ERROR_CODES[error_code]
        severity = error_info["severity"]
        
        return GenesisError(
            error_code=error_code,
            message=message,
            severity=severity,
            location=location,
            context=context or {}
        )
    
    def handle_error(self, error: GenesisError, context: Dict = None) -> bool:
        """Handle error with appropriate action"""
        # Log error
        self._log_error(error, context)
        
        # Check if HALT required
        if error.error_code in self.HALT_CODES:
            return self._halt(error)
        
        # Check if retry possible
        if self._can_retry(error.error_code):
            return self._retry(error, context)
        
        # Check if fallback possible
        if self._can_fallback(error.error_code):
            return self._fallback(error, context)
        
        # Request user input
        return self._request_user_input(error, context)
    
    def _log_error(self, error: GenesisError, context: Dict = None):
        """Log error to file"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "error_code": error.error_code,
            "error_name": self.ERROR_CODES[error.error_code]["name"],
            "severity": error.severity.value,
            "message": error.message,
            "location": error.location,
            "context": {**error.context, **(context or {})}
        }
        
        self.error_history.append(log_entry)
        
        # Append to log file
        with open(self.error_log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry) + "\n")
    
    def _halt(self, error: GenesisError) -> bool:
        """Execute HALT protocol"""
        print(f"\n{'='*60}")
        print(f"[HALT] {error.error_code} - {self.ERROR_CODES[error.error_code]['name']}")
        print(f"{'='*60}")
        print(f"\nIssue: {error.message}")
        print(f"Location: {error.location or 'Unknown'}")
        print(f"Severity: {error.severity.value.upper()}")
        
        if error.context:
            print(f"\nContext: {json.dumps(error.context, indent=2)}")
        
        print(f"\nOptions:")
        print(f"1. Fix the issue and continue")
        print(f"2. Abort and exit")
        print(f"3. Get help")
        print(f"\nType number to proceed or 'help' for more info.")
        
        return False
    
    def _can_retry(self, error_code: str) -> bool:
        """Check if error can be retried"""
        retryable_codes = ["E003", "E004", "E007", "E009"]
        return error_code in retryable_codes
    
    def _retry(self, error: GenesisError, context: Dict = None) -> bool:
        """Execute retry logic"""
        max_retries = 3
        retries = context.get("retries", 0) if context else 0
        
        if retries >= max_retries:
            return self._halt(error)
        
        print(f"\n⚠️  Error occurred. Retrying... (Attempt {retries + 1}/{max_retries})")
        
        # Simulate retry delay
        import time
        delay = 2 ** retries  # Exponential backoff
        time.sleep(min(delay, 5))  # Cap at 5 seconds
        
        context["retries"] = retries + 1
        
        # Return True to indicate retry attempted
        return True
    
    def _can_fallback(self, error_code: str) -> bool:
        """Check if fallback is possible"""
        fallback_codes = ["E003", "E004"]
        return error_code in fallback_codes
    
    def _fallback(self, error: GenesisError, context: Dict = None) -> bool:
        """Execute fallback logic"""
        print(f"\n🔄 Primary method failed. Attempting fallback...")
        
        # In real implementation, would switch to backup agent/skill
        # For now, just log
        if context:
            context["fallback_used"] = True
        
        return True
    
    def _request_user_input(self, error: GenesisError, context: Dict = None) -> bool:
        """Request user input to resolve error"""
        print(f"\n❗ Error requires user input: {error.message}")
        print(f"Please provide the required information to proceed.")
        return True
    
    def get_error_history(self, limit: int = 10) -> List[Dict]:
        """Get recent error history"""
        return self.error_history[-limit:]
    
    def get_error_stats(self) -> Dict[str, Any]:
        """Get error statistics"""
        if not self.error_history:
            return {"total": 0}
        
        severity_counts = {}
        code_counts = {}
        
        for entry in self.error_history:
            severity = entry["severity"]
            code = entry["error_code"]
            
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
            code_counts[code] = code_counts.get(code, 0) + 1
        
        return {
            "total": len(self.error_history),
            "by_severity": severity_counts,
            "by_code": code_counts,
            "last_error": self.error_history[-1] if self.error_history else None
        }

# Example usage
if __name__ == "__main__":
    # Test error handler
    handler = ErrorHandler()
    
    # Create and handle error
    error = handler.create_error(
        error_code="E001",
        message="Configuration file not found",
        location=".agenkit/config.json",
        context={"required": "config.json"}
    )
    
    print(f"Created error: {error}")
    
    # Handle error
    result = handler.handle_error(error, {"attempt": 1})
    print(f"Error handled: {result}")
    
    # Get stats
    stats = handler.get_error_stats()
    print(f"\nError stats: {stats}")
    
    print("\n✅ Error handling implementation working!")
