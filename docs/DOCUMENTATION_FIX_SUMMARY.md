# Documentation Fix Summary
## Corrected Command Line Flag

### ❌ Error Found
The documentation incorrectly referenced `--enable-phoenix-import` which doesn't exist.

**Error Message:**
```
enhanced_npm_compromise_detector_phoenix.py: error: unrecognized arguments: --enable-phoenix-import
```

### ✅ Correction Applied

**Incorrect Flag:**
```bash
--enable-phoenix-import
```

**Correct Flag:**
```bash
--enable-phoenix
```

---

## 📝 Files Corrected

The following documentation files were updated with the correct flag:

1. ✅ `SCANNER_RISK_SCORING_UPDATE.md`
2. ✅ `test_comprehensive_scan/README.md`
3. ✅ `docs/QUICK_REFERENCE_RISK_SCORING.md`
4. ✅ `docs/SCANNER_RISK_SCORING_UPDATE.md`

---

## 🚀 Correct Usage Examples

### Basic Scan (No Phoenix)
```bash
python3 enhanced_npm_compromise_detector_phoenix.py test_comprehensive_scan/
```

### With Phoenix Integration ✅
```bash
python3 enhanced_npm_compromise_detector_phoenix.py test_comprehensive_scan/ --enable-phoenix
```

### With All Libraries Import ✅
```bash
python3 enhanced_npm_compromise_detector_phoenix.py test_comprehensive_scan/ --enable-phoenix --import-all
```

### Full Tree Analysis ✅
```bash
python3 enhanced_npm_compromise_detector_phoenix.py test_comprehensive_scan/ --full-tree
```

### Phoenix with Full Options ✅
```bash
python3 enhanced_npm_compromise_detector_phoenix.py test_comprehensive_scan/ \
  --enable-phoenix \
  --import-all \
  --full-tree \
  --organize-folders
```

---

## 📋 Complete Available Flags

From the script's help output:

```
usage: enhanced_npm_compromise_detector_phoenix.py [-h] 
       [--repo-list] 
       [--repo-url REPO_URL] 
       [--folder-list] 
       [--folders FOLDERS [FOLDERS ...]]
       [--use-embedded-credentials] 
       [--config CONFIG] 
       [--phoenix-config PHOENIX_CONFIG] 
       [--create-config]
       [--output OUTPUT] 
       [--quiet] 
       [--enable-phoenix]          ✅ Correct flag for Phoenix integration
       [--phoenix-only] 
       [--full-tree] 
       [--light-scan]
       [--organize-folders] 
       [--debug] 
       [--delete-local-files] 
       [--detail-log] 
       [--use-tmp] 
       [--import-all]
       [--tag_vuln TAG_VULN] 
       [--tag_asset TAG_ASSET]
       [target]
```

---

## ✅ Verification Test

The corrected command now works successfully:

```bash
$ python3 enhanced_npm_compromise_detector_phoenix.py test_comprehensive_scan/ --enable-phoenix

🔍 Enhanced NPM Package Compromise Detector with Phoenix Integration
======================================================================
✅ Loaded compromise data: 198 packages with specific versions
✅ Loaded 410 potentially compromised packages
✅ Loaded Phoenix API configuration from .config
🔗 Phoenix Security API integration enabled

Total libraries scanned: 45
Clean libraries: 11
Compromised libraries: 34

Severity Distribution:
  CRITICAL: 17 packages (950-1000 risk)
  HIGH: 14 packages (850-900 risk)
  INFO: 3 packages (100 risk)
  CLEAN: 11 packages (50 risk)
```

---

## 📖 Key Flags Explained

| Flag | Description |
|------|-------------|
| `--enable-phoenix` | Enable Phoenix Security API integration and asset/finding import |
| `--import-all` | Import all libraries including clean ones to Phoenix |
| `--full-tree` | Perform full dependency tree analysis (npm list) |
| `--light-scan` | Light scan mode for faster processing |
| `--organize-folders` | Organize output into dated folders |
| `--debug` | Enable debug output |
| `--detail-log` | Show all libraries without truncation |
| `--phoenix-only` | Only import to Phoenix, don't generate local report |
| `--quiet` | Suppress console output |

---

## 🔍 Common Usage Patterns

### Development/Testing
```bash
# Quick local scan without Phoenix
python3 enhanced_npm_compromise_detector_phoenix.py /path/to/project/
```

### Security Audit
```bash
# Full scan with Phoenix import
python3 enhanced_npm_compromise_detector_phoenix.py /path/to/project/ \
  --enable-phoenix \
  --full-tree \
  --detail-log
```

### CI/CD Pipeline
```bash
# Light scan with organized output
python3 enhanced_npm_compromise_detector_phoenix.py /path/to/project/ \
  --light-scan \
  --organize-folders \
  --quiet
```

### Complete Security Assessment
```bash
# Everything enabled
python3 enhanced_npm_compromise_detector_phoenix.py /path/to/project/ \
  --enable-phoenix \
  --import-all \
  --full-tree \
  --organize-folders \
  --detail-log
```

---

## ✅ Status

**Fix Applied**: ✅ Complete  
**Files Updated**: 4 documentation files  
**Verification**: ✅ Tested and working  
**Date**: November 24, 2025

All documentation now uses the correct `--enable-phoenix` flag.

