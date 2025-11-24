# Test Variations for NPM Compromise Detection

This directory contains 3 different test case variations for validating the NPM compromise detector across different application types and package combinations.

---

## 📁 Test Variations

### 1. Mobile-Focused Test (`mobile-focused/`)

**Focus**: React Native and mobile development packages

**Potentially Compromised Packages Included:**
- `@actbase/react-native-actionsheet`
- `@actbase/react-native-fast-image`
- `@actbase/react-native-kakao-channel`
- `@actbase/react-native-tiktok`
- `@seung-ju/react-native-action-sheet`
- `@strapbuild/react-native-date-time-picker`
- `@strapbuild/react-native-perspective-image-cropper`
- `react-native-datepicker-modal`
- `react-native-email`
- `react-native-fetch`
- `react-native-phone-call`
- `react-native-websocket`
- `capacitor-plugin-purchase`
- `capacitor-voice-recorder-wav`
- `expo-audio-session`
- `posthog-react-native`
- `posthog-react-native-session-replay`

**Clean Packages:**
- `react`, `react-native`, `axios`, `typescript`, `jest`, `eslint`, `prettier`

**Total Packages**: 24 (17 potentially compromised, 7 clean)

---

### 2. Backend/API-Focused Test (`backend-api-focused/`)

**Focus**: Backend services, APIs, and AsyncAPI tooling

**Potentially Compromised Packages Included:**
- `@asyncapi/cli`
- `@asyncapi/generator`
- `@asyncapi/parser`
- `@asyncapi/openapi-schema-parser`
- `@asyncapi/modelina`
- `@asyncapi/nodejs-template`
- `@asyncapi/bundler`
- `@asyncapi/optimizer`
- `@trigo/atrix`
- `@trigo/atrix-postgres`
- `@trigo/atrix-redis`
- `@trigo/keycloak-api`
- `@postman/postman-mcp-server`
- `@postman/tunnel-agent`
- `@zapier/zapier-sdk`
- `@zapier/secret-scrubber`
- `gitsafe`
- `shell-exec`
- `typeorm-orbit`
- `atrix`
- `atrix-mongoose`

**Clean Packages:**
- `express`, `fastify`, `axios`, `typescript`, `jest`, `eslint`, `prettier`, `nodemon`

**Total Packages**: 29 (21 potentially compromised, 8 clean)

---

### 3. Frontend/Web-Focused Test (`frontend-web-focused/`)

**Focus**: Web applications, Web3, ENS, and analytics

**Potentially Compromised Packages Included:**
- `@ensdomains/ensjs`
- `@ensdomains/ens-avatar`
- `@ensdomains/thorin`
- `@ensdomains/ui`
- `@ensdomains/web3modal`
- `@ensdomains/content-hash`
- `ethereum-ens`
- `@posthog/nextjs`
- `@posthog/icons`
- `@posthog/web-dev-server`
- `posthog-js`
- `posthog-docusaurus`
- `@mcp-use/mcp-use`
- `@mcp-use/cli`
- `mcp-use`
- `@kvytech/components`
- `@kvytech/web`
- `@quick-start-soft/quick-markdown`
- `@quick-start-soft/quick-markdown-image`
- `react-keycloak-context`
- `react-qr-image`
- `redux-forge`
- `svelte-autocomplete-select`
- `vite-plugin-httpfile`
- `wenk`

**Clean Packages:**
- `react`, `vue`, `next`, `axios`, `vite`, `webpack`, `typescript`, `jest`, `eslint`, `prettier`

**Total Packages**: 35 (25 potentially compromised, 10 clean)

---

## 🧪 Running Tests

### Test Individual Variations

#### Mobile-Focused Test
```bash
python3 enhanced_npm_compromise_detector_phoenix.py test_variations/mobile-focused/
```

**Expected Results:**
- HIGH severity: ~17 packages (potentially compromised)
- CLEAN: ~7 packages

#### Backend/API-Focused Test
```bash
python3 enhanced_npm_compromise_detector_phoenix.py test_variations/backend-api-focused/
```

**Expected Results:**
- HIGH severity: ~21 packages (potentially compromised)
- CLEAN: ~8 packages

#### Frontend/Web-Focused Test
```bash
python3 enhanced_npm_compromise_detector_phoenix.py test_variations/frontend-web-focused/
```

**Expected Results:**
- HIGH severity: ~25 packages (potentially compromised)
- CLEAN: ~10 packages

---

### Test All Variations at Once

```bash
# Scan all test variations
for dir in test_variations/*/; do
    echo "===== Testing: $dir ====="
    python3 enhanced_npm_compromise_detector_phoenix.py "$dir"
    echo ""
done
```

### With Phoenix Integration

```bash
# Test with Phoenix import
python3 enhanced_npm_compromise_detector_phoenix.py test_variations/mobile-focused/ \
  --enable-phoenix

python3 enhanced_npm_compromise_detector_phoenix.py test_variations/backend-api-focused/ \
  --enable-phoenix

python3 enhanced_npm_compromise_detector_phoenix.py test_variations/frontend-web-focused/ \
  --enable-phoenix
```

---

## 📊 Expected Detection Summary

### Mobile-Focused
| Severity | Count | Phoenix Score | Description |
|----------|-------|---------------|-------------|
| HIGH | ~17 | 8.0 | Potentially compromised packages |
| CLEAN | ~7 | 1.0 | Safe packages |

### Backend/API-Focused
| Severity | Count | Phoenix Score | Description |
|----------|-------|---------------|-------------|
| HIGH | ~21 | 8.0 | Potentially compromised packages |
| CLEAN | ~8 | 1.0 | Safe packages |

### Frontend/Web-Focused
| Severity | Count | Phoenix Score | Description |
|----------|-------|---------------|-------------|
| HIGH | ~25 | 8.0 | Potentially compromised packages |
| CLEAN | ~10 | 1.0 | Safe packages |

---

## 🎯 Use Cases

### 1. Mobile Development Security
Use `mobile-focused/` to test:
- React Native projects
- Mobile app dependencies
- Capacitor plugins
- Mobile analytics (PostHog React Native)

### 2. Backend/API Security
Use `backend-api-focused/` to test:
- API development tools
- Backend frameworks
- AsyncAPI tooling
- Database connectors
- Authentication services

### 3. Frontend/Web Security
Use `frontend-web-focused/` to test:
- Web3 and blockchain projects
- ENS integration
- Web analytics (PostHog)
- MCP (Model Context Protocol) tools
- Modern frontend frameworks

---

## 📋 Package Categories

### By Risk Level

**HIGH (Potentially Compromised - Phoenix: 8.0)**
- All packages from the 410 potentially compromised list
- No specific version information available
- ALL versions should be treated as potentially compromised

**CLEAN (Not Affected - Phoenix: 1.0)**
- Popular frameworks and tools not in compromise database
- `express`, `react`, `vue`, `typescript`, `jest`, etc.

### By Organization

**Major Organizations Represented:**
- `@actbase` - Mobile development
- `@asyncapi` - API specification and tools
- `@ensdomains` - Ethereum Name Service
- `@posthog` - Product analytics
- `@postman` - API testing
- `@zapier` - Integration platform
- `@trigo` - Enterprise framework
- `@kvytech` - E-commerce plugins
- `@mcp-use` - MCP integration
- `@quick-start-soft` - Documentation tools

---

## 🔍 Validation Checklist

For each test variation:

- [ ] Scanner detects all potentially compromised packages
- [ ] HIGH severity (8.0) assigned to potentially compromised
- [ ] CLEAN severity (1.0) assigned to safe packages
- [ ] Risk scores displayed correctly (850/1000 for HIGH)
- [ ] Phoenix API accepts findings (if using --enable-phoenix)
- [ ] Descriptions note "ALL VERSIONS potentially compromised"
- [ ] Remediation advice appropriate for each severity level

---

## 💡 Testing Tips

### Compare Results
```bash
# Save results for comparison
python3 enhanced_npm_compromise_detector_phoenix.py test_variations/mobile-focused/ \
  > results_mobile.txt

python3 enhanced_npm_compromise_detector_phoenix.py test_variations/backend-api-focused/ \
  > results_backend.txt

python3 enhanced_npm_compromise_detector_phoenix.py test_variations/frontend-web-focused/ \
  > results_frontend.txt
```

### Extract Statistics
```bash
# Count findings by severity
grep -E "CRITICAL|HIGH|INFO|CLEAN" results_mobile.txt | sort | uniq -c
```

### Check Specific Packages
```bash
# Look for specific package in results
grep "@asyncapi/cli" results_backend.txt -A 3
```

---

## 🔄 Maintenance

### Updating Test Files

To add more packages or change versions:

1. Edit the respective `package.json` file
2. Add packages from the potentially compromised list
3. Keep a mix of clean packages for comparison
4. Run the scanner to validate changes

### Adding New Variations

To create a new test variation:

1. Create a new directory: `test_variations/[name]/`
2. Add a `package.json` with selected packages
3. Update this README with the new variation
4. Run tests to validate

---

## 📚 Related Documentation

- **Main Test Suite**: `test_comprehensive_scan/`
- **Database Info**: `docs/POTENTIALLY_COMPROMISED_PACKAGES_UPDATE_2025-11-24.md`
- **Risk Scoring**: `SCANNER_RISK_SCORING_UPDATE.md`
- **Phoenix Integration**: `PHOENIX_SEVERITY_SCALE_FIX.md`

---

## 🎯 Summary

These test variations provide:

✅ **Coverage**: 63 potentially compromised packages across 3 scenarios  
✅ **Diversity**: Mobile, Backend, and Frontend use cases  
✅ **Realism**: Mix of clean and compromised packages  
✅ **Validation**: Different package combinations and versions  
✅ **Documentation**: Clear expected results for each variation  

Use these variations to:
- Validate scanner accuracy
- Test Phoenix integration
- Demonstrate detection capabilities
- Train security teams
- Compare detection across application types

---

**Created**: November 24, 2025  
**Database Version**: 2.0 (608 packages)  
**Scanner Version**: 2.0  
**Total Test Packages**: 88 across 3 variations  
**Potentially Compromised**: 63 packages  
**Clean Packages**: 25 packages

