import os
import re
from pathlib import Path

def execute(context):
    """
    Genesis MK2 Security Scan Skill
    Performs P0/P1 security checks with .genesisignore support.
    """
    project_path = Path(context.get("project_path", "."))
    findings = []
    
    # 1. Load .genesisignore patterns
    ignore_patterns = {'.git', '.agenkit', '__pycache__', 'node_modules', 'venv'}
    ignore_file = project_path / ".genesisignore"
    if ignore_file.exists():
        with open(ignore_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_patterns.add(line)

    secret_patterns = {
        "Generic Secret": r'(?i)(secret|token|password|auth|api_key|private_key)\s*[:=]\s*["\'][a-zA-Z0-9_\-\.]{8,}',
        "AWS Access Key": r'AKIA[0-9A-Z]{16}',
        "Slack Token": r'xox[baprs]-[0-9a-zA-Z]{10,48}',
        "GitHub Personal Access Token": r'ghp_[a-zA-Z0-9]{36}'
    }
    
    for root, dirs, files in os.walk(project_path):
        # Efficient filtering using ignore_patterns
        dirs[:] = [d for d in dirs if d not in ignore_patterns]
        
        for file in files:
            if any(pat in file for pat in ignore_patterns): continue
            if file.endswith(('.py', '.js', '.ts', '.env', '.json', '.yml', '.yaml')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        for name, pattern in secret_patterns.items():
                            matches = re.finditer(pattern, content)
                            for match in matches:
                                findings.append({"type": "SECRET_EXPOSURE", "severity": "CRITICAL", "file": file_path, "pattern": name})
                        if file.endswith('.py') and ('eval(' in content or 'exec(' in content):
                            findings.append({"type": "DANGEROUS_CALL", "severity": "HIGH", "file": file_path})
                except Exception as e:
                    findings.append({"type": "SCAN_ERROR", "file": file_path, "error": str(e)})

    return {"status": "PASS" if not findings else "FAIL", "total_findings": len(findings), "findings": findings}

    
    # Excluded directories
    exclude_dirs = {'.git', '.agenkit', '__pycache__', 'node_modules', 'venv'}
    
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file.endswith(('.py', '.js', '.ts', '.env', '.json', '.yml', '.yaml')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        
                        # 1. Check for secrets
                        for name, pattern in secret_patterns.items():
                            matches = re.finditer(pattern, content)
                            for match in matches:
                                findings.append({
                                    "type": "SECRET_EXPOSURE",
                                    "severity": "CRITICAL",
                                    "file": file_path,
                                    "pattern": name,
                                    "line": content.count('\n', 0, match.start()) + 1
                                })
                                
                        # 2. Check for dangerous calls (Python specific example)
                        if file.endswith('.py'):
                            if 'eval(' in content or 'exec(' in content:
                                findings.append({
                                    "type": "DANGEROUS_CALL",
                                    "severity": "HIGH",
                                    "file": file_path,
                                    "description": "Use of eval() or exec() detected."
                                })
                                
                except Exception as e:
                    findings.append({"type": "SCAN_ERROR", "file": file_path, "error": str(e)})

    return {
        "status": "PASS" if not findings else "FAIL",
        "total_findings": len(findings),
        "findings": findings
    }
