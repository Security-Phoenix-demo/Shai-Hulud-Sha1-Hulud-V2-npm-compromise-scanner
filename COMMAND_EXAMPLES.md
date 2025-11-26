# 💻 Command Examples & Quick Reference

This document provides ready-to-use commands for all NPM security scanning scenarios.

## 🚀 Quick Start Commands

### **Basic Local Scanning**
```bash
# Scan current directory
python3 enhanced_npm_compromise_detector_phoenix.py .

# Scan with output file
python3 enhanced_npm_compromise_detector_phoenix.py . --output security-report.txt

# Scan specific directory
python3 enhanced_npm_compromise_detector_phoenix.py /path/to/project --output project-scan.txt
```

### **Organized Output**
```bash
# Create timestamped results folder
python3 enhanced_npm_compromise_detector_phoenix.py . --organize-folders --output organized-scan.txt

# Results will be in: result/YYYYMMDD/organized-scan.txt
```

## 🔗 Phoenix Integration Commands

### **Basic Phoenix Integration**
```bash
# Enable Phoenix Security API
python3 enhanced_npm_compromise_detector_phoenix.py . --enable-phoenix --output phoenix-scan.txt

# Phoenix with debug mode
python3 enhanced_npm_compromise_detector_phoenix.py . --enable-phoenix --debug --output phoenix-debug-scan.txt

# Phoenix with organized folders
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --enable-phoenix \
  --organize-folders \
  --debug \
  --output phoenix-organized-scan.txt
```

### **Phoenix Configuration Setup**
```bash
# Create configuration file template
python3 enhanced_npm_compromise_detector_phoenix.py --create-config

# Use embedded credentials (for local development)
python3 enhanced_npm_compromise_detector_phoenix.py . --use-embedded-credentials --output embedded-scan.txt
```

## 🌳 Full Tree Analysis Commands

### **Local Full Tree**
```bash
# Full dependency tree analysis
python3 enhanced_npm_compromise_detector_phoenix.py . --full-tree --output full-tree-report.txt

# Full tree with Phoenix integration
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --full-tree \
  --enable-phoenix \
  --organize-folders \
  --output phoenix-full-tree.txt

# Full tree with debug mode
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --full-tree \
  --enable-phoenix \
  --debug \
  --organize-folders \
  --output debug-full-tree.txt
```

### **Remote Repository Full Tree**
```bash
# Create repo list and run full tree analysis
cat > repos.txt << EOF
https://github.com/facebook/react
https://github.com/vuejs/vue
EOF

python3 enhanced_npm_compromise_detector_phoenix.py \
  --repo-list repos.txt \
  --full-tree \
  --organize-folders \
  --output remote-full-tree.txt
```

## 🪶 Light Scan Commands

### **Single Repository Light Scan**
```bash
# Light scan single repository
echo "https://github.com/facebook/react" > single-repo.txt
python3 enhanced_npm_compromise_detector_phoenix.py \
  --light-scan \
  --repo-list single-repo.txt \
  --output react-light-scan.txt

# Light scan with Phoenix
python3 enhanced_npm_compromise_detector_phoenix.py \
  --light-scan \
  --repo-list single-repo.txt \
  --enable-phoenix \
  --organize-folders \
  --output react-phoenix-light.txt
```

### **Multiple Repository Light Scan**
```bash
# Create comprehensive repository list
cat > external-repos.txt << EOF
https://github.com/facebook/react
https://github.com/vuejs/vue
https://github.com/angular/angular
https://github.com/microsoft/TypeScript
https://github.com/nodejs/node
https://github.com/expressjs/express
https://github.com/lodash/lodash
EOF

# Light scan all repositories
python3 enhanced_npm_compromise_detector_phoenix.py \
  --light-scan \
  --repo-list external-repos.txt \
  --organize-folders \
  --output multi-repo-light-scan.txt

# Light scan with Phoenix integration
python3 enhanced_npm_compromise_detector_phoenix.py \
  --light-scan \
  --repo-list external-repos.txt \
  --enable-phoenix \
  --debug \
  --organize-folders \
  --output multi-repo-phoenix-light.txt
```

## 📁 Local Folder Scanning Commands

### **Single Folder**
```bash
# Scan specific folder
python3 enhanced_npm_compromise_detector_phoenix.py /path/to/project --output project-scan.txt

# Multiple specific folders
python3 enhanced_npm_compromise_detector_phoenix.py \
  --folders /path/to/project1 /path/to/project2 \
  --output multi-folder-scan.txt
```

### **Folder List File**
```bash
# Create folder list
cat > my-projects.txt << EOF
/Users/developer/projects/frontend-app
/Users/developer/projects/backend-api
/Users/developer/projects/mobile-client
/Users/developer/projects/shared-utils
EOF

# Scan all folders in list
python3 enhanced_npm_compromise_detector_phoenix.py \
  --folder-list my-projects.txt \
  --organize-folders \
  --output local-projects-scan.txt

# Folder list with Phoenix
python3 enhanced_npm_compromise_detector_phoenix.py \
  --folder-list my-projects.txt \
  --enable-phoenix \
  --organize-folders \
  --output local-projects-phoenix.txt
```

## 🐙 GitHub Automatic Pull & Scan Commands

### **Pull All User Repositories**
```bash
# Automatically fetch and scan ALL repositories you have access to
python3 enhanced_npm_compromise_detector_phoenix.py --pull-all --output github-all-repos.txt

# With organized folders
python3 enhanced_npm_compromise_detector_phoenix.py \
  --pull-all \
  --organize-folders \
  --output github-all-repos-organized.txt

# With Phoenix integration
python3 enhanced_npm_compromise_detector_phoenix.py \
  --pull-all \
  --enable-phoenix \
  --organize-folders \
  --output github-all-repos-phoenix.txt

# With debug mode (see API calls and repository discovery)
python3 enhanced_npm_compromise_detector_phoenix.py \
  --pull-all \
  --debug \
  --organize-folders \
  --output github-all-repos-debug.txt
```

### **GitHub Authentication Setup**
```bash
# Set GitHub token as environment variable (recommended)
export GITHUB_TOKEN="ghp_your_personal_access_token_here"
python3 enhanced_npm_compromise_detector_phoenix.py --pull-all --output scan.txt

# Or use git credentials helper
git config --global credential.helper store
python3 enhanced_npm_compromise_detector_phoenix.py --pull-all --output scan.txt
```

### **Single Repository GitHub Scan**
```bash
# Scan specific GitHub repository
python3 enhanced_npm_compromise_detector_phoenix.py \
  https://github.com/Security-Phoenix-demo/Shai-Hulud-Hulud-Shai-npm-tinycolour-compromise-verifier \
  --output single-repo-scan.txt

# With full tree analysis
python3 enhanced_npm_compromise_detector_phoenix.py \
  https://github.com/facebook/react \
  --full-tree \
  --organize-folders \
  --output react-full-tree.txt

# With Phoenix integration
python3 enhanced_npm_compromise_detector_phoenix.py \
  https://github.com/vuejs/vue \
  --enable-phoenix \
  --organize-folders \
  --output vue-phoenix-scan.txt
```

### **GitHub Organization Scanning**
```bash
# Scan all repositories from an organization
# First, get org repos using GitHub CLI
gh repo list myorg --limit 1000 --json url --jq '.[].url' > org-repos.txt

# Then scan all org repositories
python3 enhanced_npm_compromise_detector_phoenix.py \
  --repo-list org-repos.txt \
  --organize-folders \
  --output org-scan.txt

# Or use --pull-all if you have access to org repos
python3 enhanced_npm_compromise_detector_phoenix.py \
  --pull-all \
  --enable-phoenix \
  --organize-folders \
  --output org-all-repos-scan.txt
```

### **Private Repository Scanning**
```bash
# Scan private repositories (requires GitHub token with repo scope)
export GITHUB_TOKEN="ghp_token_with_repo_scope"

# Scan all accessible private repos
python3 enhanced_npm_compromise_detector_phoenix.py \
  --pull-all \
  --organize-folders \
  --output private-repos-scan.txt

# Scan specific private repository
python3 enhanced_npm_compromise_detector_phoenix.py \
  https://github.com/company/private-repo \
  --organize-folders \
  --output private-repo-scan.txt
```

## 🔄 Repository List Commands

### **Basic Repository List**
```bash
# Create repository list
cat > company-repos.txt << EOF
https://github.com/company/frontend
https://github.com/company/backend
https://github.com/company/mobile
EOF

# Scan repository list (clones repositories)
python3 enhanced_npm_compromise_detector_phoenix.py \
  --repo-list company-repos.txt \
  --organize-folders \
  --output company-scan.txt
```

### **Repository List with Full Tree**
```bash
# Full tree analysis of repository list
python3 enhanced_npm_compromise_detector_phoenix.py \
  --repo-list company-repos.txt \
  --full-tree \
  --organize-folders \
  --output company-full-tree.txt

# With Phoenix integration
python3 enhanced_npm_compromise_detector_phoenix.py \
  --repo-list company-repos.txt \
  --full-tree \
  --enable-phoenix \
  --debug \
  --organize-folders \
  --output company-phoenix-full.txt
```

## 🎯 Specialized Scanning Commands

### **Quick Assessment Commands**
```bash
# Quick scan without detailed output
python3 enhanced_npm_compromise_detector_phoenix.py . --quiet --output quick-scan.txt

# Quick scan multiple projects
python3 enhanced_npm_compromise_detector_phoenix.py \
  --folder-list my-projects.txt \
  --quiet \
  --output quick-multi-scan.txt
```

### **Development Workflow Commands**
```bash
# Pre-commit security check
python3 enhanced_npm_compromise_detector_phoenix.py . --output pre-commit-check.txt

# Post-merge security validation
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --organize-folders \
  --output post-merge-validation.txt

# Release preparation scan
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --full-tree \
  --enable-phoenix \
  --organize-folders \
  --output release-security-check.txt
```

### **CI/CD Integration Commands**
```bash
# Jenkins/GitHub Actions command
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --enable-phoenix \
  --organize-folders \
  --debug \
  --output "ci-security-scan-${BUILD_NUMBER:-$(date +%Y%m%d_%H%M%S)}.txt"

# Fail on critical vulnerabilities (for CI)
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --enable-phoenix \
  --output ci-scan.txt || exit 1
```

## 🏢 Enterprise Commands

### **Organization-Wide Scanning**
```bash
# Option 1: Automatic discovery and scanning (recommended)
# Scans ALL repositories your GitHub credentials have access to
export GITHUB_TOKEN="ghp_your_org_token_here"
python3 enhanced_npm_compromise_detector_phoenix.py \
  --pull-all \
  --full-tree \
  --enable-phoenix \
  --organize-folders \
  --output "enterprise-security-audit-$(date +%Y%m%d).txt"

# Option 2: Manual repository list
cat > org-repos.txt << EOF
https://github.com/org/frontend-main
https://github.com/org/frontend-admin
https://github.com/org/backend-api
https://github.com/org/backend-auth
https://github.com/org/mobile-ios
https://github.com/org/mobile-android
https://github.com/org/shared-components
https://github.com/org/deployment-tools
https://github.com/org/monitoring-stack
https://github.com/org/documentation-site
EOF

# Enterprise-grade scanning with manual list
python3 enhanced_npm_compromise_detector_phoenix.py \
  --repo-list org-repos.txt \
  --full-tree \
  --enable-phoenix \
  --debug \
  --organize-folders \
  --output "enterprise-security-audit-$(date +%Y%m%d).txt"

# Option 3: Use GitHub CLI to generate list
gh repo list myorg --limit 1000 --json url --jq '.[].url' > org-repos.txt
python3 enhanced_npm_compromise_detector_phoenix.py \
  --repo-list org-repos.txt \
  --full-tree \
  --enable-phoenix \
  --organize-folders \
  --output "org-comprehensive-scan-$(date +%Y%m%d).txt"
```

### **Supply Chain Analysis**
```bash
# Focus on supply chain security
cat > supply-chain-repos.txt << EOF
https://github.com/company/app-using-lodash
https://github.com/company/app-using-express
https://github.com/company/app-using-react
https://github.com/company/service-using-fastify
EOF

python3 enhanced_npm_compromise_detector_phoenix.py \
  --repo-list supply-chain-repos.txt \
  --full-tree \
  --enable-phoenix \
  --organize-folders \
  --output "supply-chain-analysis-$(date +%Y%m%d).txt"
```

### **Compliance Scanning**
```bash
# Compliance-focused scanning with full documentation
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --full-tree \
  --enable-phoenix \
  --debug \
  --organize-folders \
  --output "compliance-scan-$(date +%Y%m%d_%H%M%S).txt"

# Multi-environment compliance
for env in dev staging prod; do
    echo "Scanning $env environment..."
    python3 enhanced_npm_compromise_detector_phoenix.py "environments/$env" \
      --full-tree \
      --enable-phoenix \
      --organize-folders \
      --output "$env-compliance-$(date +%Y%m%d).txt"
done
```

## 🔧 Troubleshooting Commands

### **Diagnostic Commands**
```bash
# Debug mode with maximum verbosity
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --debug \
  --enable-phoenix \
  --output diagnostic-scan.txt

# Test Phoenix connection
python3 enhanced_npm_compromise_detector_phoenix.py --create-config
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --enable-phoenix \
  --debug \
  --output phoenix-test.txt
```

### **Recovery Commands**
```bash
# Fallback to local scan if Phoenix fails
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --output fallback-scan.txt || \
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --enable-phoenix \
  --output phoenix-fallback.txt

# Light scan if full scan times out
timeout 1800 python3 enhanced_npm_compromise_detector_phoenix.py . \
  --full-tree \
  --output full-scan.txt || \
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --light-scan \
  --output light-fallback.txt
```

## 📊 Monitoring & Automation Commands

### **Daily Monitoring**
```bash
#!/bin/bash
# daily-monitor.sh
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Monitor production repositories
cat > production-monitor.txt << EOF
https://github.com/company/prod-frontend
https://github.com/company/prod-api
https://github.com/company/prod-mobile
EOF

python3 enhanced_npm_compromise_detector_phoenix.py \
  --light-scan \
  --repo-list production-monitor.txt \
  --enable-phoenix \
  --organize-folders \
  --output "daily-monitor-$TIMESTAMP.txt"

# Check for critical vulnerabilities
if grep -q "CRITICAL" "result/$(date +%Y%m%d)/daily-monitor-$TIMESTAMP.txt"; then
    echo "🚨 CRITICAL vulnerabilities found in production!"
    # Send alert notification here
fi
```

### **Weekly Full Audit**
```bash
#!/bin/bash
# weekly-audit.sh
WEEK=$(date +%Y%U)

python3 enhanced_npm_compromise_detector_phoenix.py \
  --repo-list org-repos.txt \
  --full-tree \
  --enable-phoenix \
  --debug \
  --organize-folders \
  --output "weekly-audit-week-$WEEK.txt"

echo "📊 Weekly audit completed for week $WEEK"
```

### **Continuous Integration**
```bash
#!/bin/bash
# ci-security-check.sh

# For pull requests - quick scan
if [ "$CI_EVENT" == "pull_request" ]; then
    python3 enhanced_npm_compromise_detector_phoenix.py . \
      --output "pr-security-check-$PR_NUMBER.txt"
fi

# For main branch - full scan with Phoenix
if [ "$CI_BRANCH" == "main" ]; then
    python3 enhanced_npm_compromise_detector_phoenix.py . \
      --full-tree \
      --enable-phoenix \
      --organize-folders \
      --output "main-branch-scan-$BUILD_NUMBER.txt"
fi

# For releases - comprehensive audit
if [[ "$CI_TAG" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    python3 enhanced_npm_compromise_detector_phoenix.py . \
      --full-tree \
      --enable-phoenix \
      --debug \
      --organize-folders \
      --output "release-audit-$CI_TAG.txt"
fi
```

## 🎨 Custom Workflow Commands

### **Development Team Workflow**
```bash
# Team daily standup security check
python3 enhanced_npm_compromise_detector_phoenix.py \
  --folder-list team-projects.txt \
  --quiet \
  --output "team-daily-$(date +%Y%m%d).txt"

# Sprint security review
python3 enhanced_npm_compromise_detector_phoenix.py \
  --folder-list sprint-projects.txt \
  --full-tree \
  --enable-phoenix \
  --organize-folders \
  --output "sprint-review-$(date +%Y%m%d).txt"
```

### **Security Team Workflow**
```bash
# Monthly security assessment
python3 enhanced_npm_compromise_detector_phoenix.py \
  --repo-list all-org-repos.txt \
  --full-tree \
  --enable-phoenix \
  --debug \
  --organize-folders \
  --output "monthly-security-$(date +%Y%m).txt"

# Incident response scanning
python3 enhanced_npm_compromise_detector_phoenix.py \
  --repo-list affected-repos.txt \
  --full-tree \
  --enable-phoenix \
  --debug \
  --organize-folders \
  --output "incident-response-$(date +%Y%m%d_%H%M%S).txt"
```

### **DevOps Team Workflow**
```bash
# Pre-deployment security gate
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --full-tree \
  --enable-phoenix \
  --output "pre-deploy-gate.txt"

# Check exit code for deployment decision
if [ $? -eq 0 ]; then
    echo "✅ Security gate passed - proceeding with deployment"
else
    echo "❌ Security gate failed - blocking deployment"
    exit 1
fi

# Post-deployment verification
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --enable-phoenix \
  --organize-folders \
  --output "post-deploy-verification-$(date +%Y%m%d_%H%M%S).txt"
```

## 📚 Command Combination Examples

### **Comprehensive Security Pipeline**
```bash
#!/bin/bash
# comprehensive-pipeline.sh

echo "🔒 Starting Comprehensive Security Pipeline"

# Step 1: Quick local assessment
echo "📋 Step 1: Quick Assessment"
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --quiet \
  --output "step1-quick-assessment.txt"

# Step 2: Full tree analysis
echo "🌳 Step 2: Full Tree Analysis"
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --full-tree \
  --organize-folders \
  --output "step2-full-tree.txt"

# Step 3: Phoenix integration
echo "🔗 Step 3: Phoenix Integration"
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --full-tree \
  --enable-phoenix \
  --debug \
  --organize-folders \
  --output "step3-phoenix-integration.txt"

# Step 4: External dependency assessment
echo "🌐 Step 4: External Dependencies"
cat > external-deps.txt << EOF
https://github.com/lodash/lodash
https://github.com/expressjs/express
https://github.com/facebook/react
EOF

python3 enhanced_npm_compromise_detector_phoenix.py \
  --light-scan \
  --repo-list external-deps.txt \
  --organize-folders \
  --output "step4-external-deps.txt"

echo "✅ Comprehensive Security Pipeline Complete!"
```

### **Multi-Environment Scanning**
```bash
#!/bin/bash
# multi-env-scan.sh

environments=("dev" "staging" "prod")

for env in "${environments[@]}"; do
    echo "🔍 Scanning $env environment"
    
    python3 enhanced_npm_compromise_detector_phoenix.py "environments/$env" \
      --full-tree \
      --enable-phoenix \
      --organize-folders \
      --output "$env-security-scan-$(date +%Y%m%d).txt"
    
    echo "✅ $env environment scan complete"
done

echo "🎉 All environments scanned successfully!"
```

## 🚀 Advanced GitHub Scanning Workflows

### **Comprehensive GitHub Security Audit**
```bash
#!/bin/bash
# github-security-audit.sh

echo "🔒 Starting GitHub Security Audit"

# Set GitHub token
export GITHUB_TOKEN="ghp_your_token_here"

# Step 1: Discover and scan all accessible repositories
echo "📋 Step 1: Discovering all accessible repositories..."
python3 enhanced_npm_compromise_detector_phoenix.py \
  --pull-all \
  --debug \
  --organize-folders \
  --output "step1-github-discovery-$(date +%Y%m%d).txt"

# Step 2: Full tree analysis with Phoenix
echo "🌳 Step 2: Full tree analysis with Phoenix integration..."
python3 enhanced_npm_compromise_detector_phoenix.py \
  --pull-all \
  --full-tree \
  --enable-phoenix \
  --organize-folders \
  --output "step2-github-full-analysis-$(date +%Y%m%d).txt"

echo "✅ GitHub Security Audit Complete!"
```

### **Multi-Team Repository Scanning**
```bash
# Scan repositories across multiple teams/organizations
# Team 1 repositories
gh repo list team1-org --limit 100 --json url --jq '.[].url' > team1-repos.txt

# Team 2 repositories  
gh repo list team2-org --limit 100 --json url --jq '.[].url' > team2-repos.txt

# Combine and scan
cat team1-repos.txt team2-repos.txt > all-teams-repos.txt
python3 enhanced_npm_compromise_detector_phoenix.py \
  --repo-list all-teams-repos.txt \
  --full-tree \
  --enable-phoenix \
  --organize-folders \
  --output "multi-team-scan-$(date +%Y%m%d).txt"
```

### **GitHub Actions Integration**
```bash
# .github/workflows/npm-security-scan.yml
# name: NPM Supply Chain Security Scan
# 
# on:
#   schedule:
#     - cron: '0 0 * * *'  # Daily at midnight
#   push:
#     branches: [ main ]
#   pull_request:
#     branches: [ main ]
#
# jobs:
#   security-scan:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v3
#       
#       - name: Run NPM Security Scanner
#         env:
#           GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
#         run: |
#           python3 enhanced_npm_compromise_detector_phoenix.py . \
#             --full-tree \
#             --enable-phoenix \
#             --organize-folders \
#             --output "security-scan-${GITHUB_SHA}.txt"
```

### **Continuous Repository Monitoring**
```bash
#!/bin/bash
# monitor-github-repos.sh

# Daily monitoring of all accessible repositories
export GITHUB_TOKEN="${GITHUB_TOKEN:-ghp_default_token}"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Run comprehensive scan
python3 enhanced_npm_compromise_detector_phoenix.py \
  --pull-all \
  --full-tree \
  --enable-phoenix \
  --organize-folders \
  --output "github-monitoring-$TIMESTAMP.txt"

# Check for critical findings
RESULT_FILE="result/$(date +%Y%m%d)/github-monitoring-$TIMESTAMP.txt"
if grep -q "CRITICAL" "$RESULT_FILE"; then
    echo "🚨 CRITICAL vulnerabilities found!"
    # Send alert (Slack, email, etc.)
    # Example: curl -X POST -H 'Content-type: application/json' \
    #   --data '{"text":"Critical NPM vulnerabilities detected!"}' \
    #   $SLACK_WEBHOOK_URL
else
    echo "✅ No critical vulnerabilities found"
fi
```

---

## 🎯 Quick Command Reference

### **Most Common Commands**
```bash
# Basic scan
python3 enhanced_npm_compromise_detector_phoenix.py .

# With Phoenix
python3 enhanced_npm_compromise_detector_phoenix.py . --enable-phoenix

# Full tree with Phoenix
python3 enhanced_npm_compromise_detector_phoenix.py . --full-tree --enable-phoenix

# GitHub: Scan all accessible repos
python3 enhanced_npm_compromise_detector_phoenix.py --pull-all --organize-folders

# GitHub: Single repository
python3 enhanced_npm_compromise_detector_phoenix.py https://github.com/user/repo

# Light scan repositories
python3 enhanced_npm_compromise_detector_phoenix.py --light-scan --repo-list repos.txt

# Organized output
python3 enhanced_npm_compromise_detector_phoenix.py . --organize-folders --output report.txt
```

### **Flag Combinations**
```bash
# Maximum features (local)
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --full-tree \
  --enable-phoenix \
  --debug \
  --organize-folders \
  --output comprehensive-scan.txt

# Maximum features (GitHub)
python3 enhanced_npm_compromise_detector_phoenix.py \
  --pull-all \
  --full-tree \
  --enable-phoenix \
  --debug \
  --organize-folders \
  --output github-comprehensive-scan.txt

# CI/CD optimized
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --enable-phoenix \
  --organize-folders \
  --output "ci-scan-${BUILD_NUMBER}.txt"

# Development workflow
python3 enhanced_npm_compromise_detector_phoenix.py . \
  --organize-folders \
  --output "dev-scan-$(date +%Y%m%d).txt"

# GitHub organization audit
python3 enhanced_npm_compromise_detector_phoenix.py \
  --pull-all \
  --enable-phoenix \
  --organize-folders \
  --output "org-audit-$(date +%Y%m%d).txt"
```

---

## 📋 GitHub Token Setup Guide

### **Creating a GitHub Personal Access Token**

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name: "NPM Security Scanner"
4. Select scopes:
   - `repo` (Full control of private repositories)
   - `read:org` (Read org and team membership, read org projects)
5. Click "Generate token"
6. Copy the token (starts with `ghp_`)

### **Setting the Token**

**Option 1: Environment Variable (Recommended)**
```bash
# Linux/macOS - Add to ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN="ghp_your_token_here"

# Windows PowerShell
$env:GITHUB_TOKEN="ghp_your_token_here"

# Then run scanner
python3 enhanced_npm_compromise_detector_phoenix.py --pull-all
```

**Option 2: Git Credential Helper**
```bash
# Configure git to store credentials
git config --global credential.helper store

# Clone a private repo (will prompt for username and token)
git clone https://github.com/user/private-repo

# Future pulls will use stored credentials
python3 enhanced_npm_compromise_detector_phoenix.py --pull-all
```

**Option 3: GitHub CLI**
```bash
# Authenticate with GitHub CLI
gh auth login

# Scanner will use gh credentials automatically
python3 enhanced_npm_compromise_detector_phoenix.py --pull-all
```

---

## 🔍 GitHub Scanning Comparison

| Feature | --pull-all | --repo-list | Direct URL |
|---------|-----------|-------------|------------|
| **Discovery** | Automatic | Manual | Manual |
| **Private Repos** | ✅ (with token) | ✅ (with token) | ✅ (with token) |
| **Rate Limits** | Uses GitHub API | Clone only | Clone only |
| **Best For** | Organizations, audits | Specific projects | Single repo |
| **Setup Required** | GitHub token | Repo list file | None |

### **When to Use Each Method**

**Use `--pull-all` when:**
- You want to scan ALL repositories you have access to
- Performing organization-wide security audits
- You have a GitHub token with appropriate scopes
- You want automatic discovery of new repositories

**Use `--repo-list` when:**
- You have a specific set of repositories to scan
- You want to scan repositories from multiple sources
- You need to mix GitHub and non-GitHub repositories
- You want fine control over what gets scanned

**Use direct URL when:**
- You need to scan a single specific repository
- Quick ad-hoc security check
- Testing the scanner
- Scanning public repositories

---

**💻 Copy, paste, and customize these commands for your specific security scanning needs!**

This reference provides battle-tested commands for every NPM security scanning scenario, including comprehensive GitHub integration with automatic repository discovery and scanning. Adapt the examples to fit your workflow and security requirements. 🛡️✨
