# Genesis MK2 Skill Dependencies

> **Purpose:** Document all external dependencies for each skill
> **Version:** 1.0.0
> **Status:** CRITICAL FIX - Dependency Documentation

---

## 📋 Skills Requiring External Tools

### 🔴 HIGH PRIORITY - Must Install

| Skill | External Tool | Installation Command | Purpose |
|-------|---------------|---------------------|---------|
| `vulnerability-scanner.md` | `npm audit` | `npm install -g npm` | Security scanning |
| `performance-profiling.md` | Lighthouse CLI | `npm install -g lighthouse` | Performance auditing |
| `webapp-testing.md` | Playwright | `npm install -g playwright` | E2E testing |
| `lint-and-validate.md` | ESLint | `npm install -g eslint` | Code linting |
| `database-design.md` | Prisma | `npm install -g @prisma/cli` | Database schema |

### 🟡 MEDIUM PRIORITY - Recommended

| Skill | External Tool | Installation Command | Purpose |
|-------|---------------|---------------------|---------|
| `seo-fundamentals.md` | Google Search Console | Manual setup | SEO analysis |
| `geo-fundamentals.md` | AI optimization tools | Varies | GenAI optimization |
| `deployment-procedures.md` | Docker | `winget install Docker.Docker` | Containerization |
| `testing-patterns.md` | Jest | `npm install -g jest` | Unit testing |
| `i18n-localization.md` | i18n tools | Varies | Internationalization |

### 🟢 LOW PRIORITY - Optional

| Skill | External Tool | Installation Command | Purpose |
|-------|---------------|---------------------|---------|
| `game-development.md` | Game engine | Varies | Game development |
| `mobile-design.md` | Mobile emulators | Varies | Mobile testing |
| `rust-pro.md` | Rust toolchain | `rustup install stable` | Rust development |
| `python-patterns.md` | Python 3.10+ | `winget install Python.Python.3.10` | Python development |

---

## 🛠️ Quick Installation Script

**File:** `install-dependencies.sh` (or `.ps1` for Windows)

```bash
#!/bin/bash
# Genesis MK2 - Install Required Dependencies

echo "Installing Genesis MK2 dependencies..."

# High priority
echo "Installing high-priority tools..."
npm install -g npm
npm install -g lighthouse
npm install -g playwright
npm install -g eslint
npm install -g @prisma/cli

# Medium priority
echo "Installing medium-priority tools..."
npm install -g jest
npm install -g docker

# Verify installation
echo "Verifying installations..."
npm --version
lighthouse --version
playwright --version
eslint --version
prisma --version

echo "Dependencies installed!"
```

---

## 📝 Skill Dependency Details

### vulnerability-scanner.md

**Required Tools:**
- `npm audit` (Node.js package manager)
- `snyk` (optional, for advanced scanning)

**Installation:**
```bash
# Node.js and npm
winget install OpenJS.NodeJS.LTS

# Snyk (optional)
npm install -g snyk
```

**Usage:**
```bash
npm audit          # Basic security scan
snyk test          # Advanced security scan
snyk protect       # Enable protection
```

**Fallback if missing:**
- Skip automated scanning
- Manual code review required
- Document security concerns

---

### performance-profiling.md

**Required Tools:**
- Lighthouse CLI
- Chrome DevTools (optional)

**Installation:**
```bash
npm install -g lighthouse
```

**Usage:**
```bash
lighthouse https://localhost:3000 --view
```

**Fallback if missing:**
- Use browser DevTools manually
- Document performance metrics manually
- Skip automated scoring

---

### webapp-testing.md

**Required Tools:**
- Playwright
- Chromium/Firefox/WebKit browsers

**Installation:**
```bash
npm install -g playwright
playwright install
```

**Usage:**
```bash
playwright test
```

**Fallback if missing:**
- Manual testing required
- Document test cases manually
- Skip automated E2E tests

---

### lint-and-validate.md

**Required Tools:**
- ESLint
- TypeScript (if TypeScript project)

**Installation:**
```bash
npm install -g eslint
npm install -g typescript
```

**Usage:**
```bash
eslint src/
tsc --noEmit
```

**Fallback if missing:**
- Manual code review
- Basic syntax checking only
- Document linting issues manually

---

### database-design.md

**Required Tools:**
- Prisma CLI
- Database client (PostgreSQL, MySQL, etc.)

**Installation:**
```bash
npm install -g @prisma/cli
```

**Usage:**
```bash
prisma db pull
prisma db push
prisma generate
```

**Fallback if missing:**
- Manual schema design
- SQL scripts only
- Document database structure manually

---

## ✅ Dependency Checklist

Before using skills, verify:

### High Priority (Required):
- [ ] npm installed
- [ ] Lighthouse CLI installed
- [ ] Playwright installed
- [ ] ESLint installed
- [ ] Prisma CLI installed

### Medium Priority (Recommended):
- [ ] Jest installed
- [ ] Docker installed
- [ ] Google Search Console configured
- [ ] i18n tools configured

### Low Priority (Optional):
- [ ] Rust toolchain installed
- [ ] Python 3.10+ installed
- [ ] Game engine installed
- [ ] Mobile emulators installed

---

## 🚨 Dependency Error Handling

### If Tool Not Installed:

**Error Message:**
```
⚠️ SKILL DEPENDENCY MISSING

Skill: vulnerability-scanner.md
Required Tool: npm audit
Status: NOT INSTALLED

Options:
1. Install tool: npm install -g npm
2. Skip automated scanning
3. Use manual code review

Type number or 'install' to proceed.
```

### Auto-Install Option:

```bash
# If user chooses to install
echo "Installing npm..."
winget install OpenJS.NodeJS.LTS
echo "Installation complete!"
```

---

## 📊 Dependency Status

| Skill | Status | Tool | Install Command |
|-------|--------|------|-----------------|
| vulnerability-scanner | ⚠️ Requires | npm | `winget install OpenJS.NodeJS.LTS` |
| performance-profiling | ⚠️ Requires | Lighthouse | `npm install -g lighthouse` |
| webapp-testing | ⚠️ Requires | Playwright | `npm install -g playwright` |
| lint-and-validate | ⚠️ Requires | ESLint | `npm install -g eslint` |
| database-design | ⚠️ Requires | Prisma | `npm install -g @prisma/cli` |
| testing-patterns | ✅ Optional | Jest | `npm install -g jest` |
| deployment-procedures | ✅ Optional | Docker | `winget install Docker.Docker` |

---

## 🔄 Dependency Resolution Flow

```
Skill Request
    ↓
Check Dependencies
    ↓
All Dependencies Met?
    ├── YES → Execute Skill
    └── NO → Show Error
            ↓
    User Choice:
    ├── Install Missing
    ├── Skip Skill
    └── Use Fallback
```

---

## 📝 Documentation Template

For each skill, document:

```markdown
# Skill Name

## Dependencies

### Required
- Tool 1: Installation command
- Tool 2: Installation command

### Optional
- Tool 3: Installation command

## Installation
[Installation steps]

## Fallback
[What to do if tools missing]
```

---

*Skill Dependencies v1.0.0*
*CRITICAL FIX - Dependency Documentation*
