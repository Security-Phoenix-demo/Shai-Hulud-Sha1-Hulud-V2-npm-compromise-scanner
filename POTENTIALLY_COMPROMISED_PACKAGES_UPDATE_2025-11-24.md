# Potentially Compromised Packages - Update Report
## Date: November 24, 2025

---

## Executive Summary

This document details a significant update to the NPM supply chain compromise database, adding **425 potentially compromised packages** to the existing list of 208 confirmed compromised packages.

### Critical Update Statistics

- **Total Confirmed Compromised Packages**: 208 (with version information)
- **Total Potentially Compromised Packages**: 425 (newly added - no version info available)
- **Grand Total Packages Under Investigation**: 633
- **Severity Level**: CRITICAL
- **Recommended Action**: Immediate audit and remediation

---

## Key Findings

### New Organizations Affected

The following organizations have packages under investigation:

#### Major Organizations Added:
- **@actbase** - React Native and mobile development tools
- **@asyncapi** - AsyncAPI tooling and templates (32 packages)
- **@ensdomains** - Ethereum Name Service ecosystem (41 packages)
- **@posthog** - Product analytics platform (48 packages)
- **@postman** - API development tools (20 packages)
- **@zapier** - Integration platform tools (12 packages)
- **@trigo** - Enterprise application framework (15 packages)
- **@kvytech** - Medusa e-commerce plugins (7 packages)
- **@lessondesk** - Educational platform tools (4 packages)
- **@mcp-use** - MCP integration tools (3 packages)
- **@orbitgtbelgium** - Mapping and GIS tools (4 packages)
- **@quick-start-soft** - Documentation and translation tools (9 packages)
- **@strapbuild** - React Native image processing (4 packages)
- **@varsityvibe** - API clients and validation (2 packages)

### Package Categories Affected

1. **API & Integration Tools**
   - AsyncAPI ecosystem (generators, parsers, templates)
   - Postman tooling and MCP servers
   - Zapier platform SDKs

2. **Blockchain & Web3**
   - ENS (Ethereum Name Service) complete ecosystem
   - Crypto address codecs
   - Web3 connectors

3. **Analytics & Monitoring**
   - PostHog complete suite (analytics, plugins, session replay)
   - Event tracking and data processing

4. **React Native & Mobile**
   - @actbase mobile development tools
   - Capacitor plugins
   - React Native components and utilities

5. **Enterprise Frameworks**
   - @trigo application framework
   - Medusa e-commerce plugins
   - Database connectors and ORMs

6. **Developer Tools**
   - CLI tools and generators
   - ESLint and Babel configurations
   - Build and bundling tools

---

## Detailed Package List

### @actbase Packages (15 packages)
```
@actbase/css-to-react-native-transform
@actbase/native
@actbase/node-server
@actbase/react-absolute
@actbase/react-daum-postcode
@actbase/react-kakaosdk
@actbase/react-native-actionsheet
@actbase/react-native-devtools
@actbase/react-native-fast-image
@actbase/react-native-kakao-channel
@actbase/react-native-kakao-navi
@actbase/react-native-less-transformer
@actbase/react-native-naver-login
@actbase/react-native-simple-video
@actbase/react-native-tiktok
```

### @asyncapi Packages (32 packages)
```
@asyncapi/avro-schema-parser
@asyncapi/bundler
@asyncapi/cli
@asyncapi/converter
@asyncapi/diff
@asyncapi/dotnet-rabbitmq-template
@asyncapi/edavisualiser
@asyncapi/generator
@asyncapi/generator-components
@asyncapi/generator-helpers
@asyncapi/generator-react-sdk
@asyncapi/go-watermill-template
@asyncapi/html-template
@asyncapi/java-spring-cloud-stream-template
@asyncapi/java-spring-template
@asyncapi/java-template
@asyncapi/keeper
@asyncapi/markdown-template
@asyncapi/modelina
@asyncapi/modelina-cli
@asyncapi/multi-parser
@asyncapi/nodejs-template
@asyncapi/nodejs-ws-template
@asyncapi/nunjucks-filters
@asyncapi/openapi-schema-parser
@asyncapi/optimizer
@asyncapi/parser
@asyncapi/php-template
@asyncapi/problem
@asyncapi/protobuf-schema-parser
@asyncapi/python-paho-template
@asyncapi/react-component
@asyncapi/server-api
@asyncapi/specs
@asyncapi/studio
@asyncapi/web-component
```

### @ensdomains Packages (41 packages)
```
@ensdomains/address-encoder
@ensdomains/blacklist
@ensdomains/buffer
@ensdomains/ccip-read-cf-worker
@ensdomains/ccip-read-dns-gateway
@ensdomains/ccip-read-router
@ensdomains/ccip-read-worker-viem
@ensdomains/content-hash
@ensdomains/curvearithmetics
@ensdomains/cypress-metamask
@ensdomains/dnsprovejs
@ensdomains/dnssec-oracle-anchors
@ensdomains/dnssecoraclejs
@ensdomains/durin
@ensdomains/durin-middleware
@ensdomains/ens-archived-contracts
@ensdomains/ens-avatar
@ensdomains/ens-contracts
@ensdomains/ens-test-env
@ensdomains/ens-validation
@ensdomains/ensjs
@ensdomains/ensjs-react
@ensdomains/eth-ens-namehash
@ensdomains/hackathon-registrar
@ensdomains/hardhat-chai-matchers-viem
@ensdomains/hardhat-toolbox-viem-extended
@ensdomains/mock
@ensdomains/name-wrapper
@ensdomains/offchain-resolver-contracts
@ensdomains/op-resolver-contracts
@ensdomains/react-ens-address
@ensdomains/renewal
@ensdomains/renewal-widget
@ensdomains/reverse-records
@ensdomains/server-analytics
@ensdomains/solsha1
@ensdomains/subdomain-registrar
@ensdomains/test-utils
@ensdomains/thorin
@ensdomains/ui
@ensdomains/unicode-confusables
@ensdomains/unruggable-gateways
@ensdomains/vite-plugin-i18next-loader
@ensdomains/web3modal
```

### @posthog Packages (48 packages)
```
@posthog/agent
@posthog/ai
@posthog/automatic-cohorts-plugin
@posthog/bitbucket-release-tracker
@posthog/cli
@posthog/clickhouse
@posthog/core
@posthog/currency-normalization-plugin
@posthog/customerio-plugin
@posthog/databricks-plugin
@posthog/drop-events-on-property-plugin
@posthog/event-sequence-timer-plugin
@posthog/filter-out-plugin
@posthog/first-time-event-tracker
@posthog/geoip-plugin
@posthog/github-release-tracking-plugin
@posthog/gitub-star-sync-plugin
@posthog/heartbeat-plugin
@posthog/hedgehog-mode
@posthog/icons
@posthog/ingestion-alert-plugin
@posthog/intercom-plugin
@posthog/kinesis-plugin
@posthog/laudspeaker-plugin
@posthog/lemon-ui
@posthog/maxmind-plugin
@posthog/migrator3000-plugin
@posthog/netdata-event-processing
@posthog/nextjs
@posthog/nextjs-config
@posthog/nuxt
@posthog/pagerduty-plugin
@posthog/piscina
@posthog/plugin-contrib
@posthog/plugin-server
@posthog/plugin-unduplicates
@posthog/postgres-plugin
@posthog/react-rrweb-player
@posthog/rrdom
@posthog/rrweb
@posthog/rrweb-player
@posthog/rrweb-record
@posthog/rrweb-replay
@posthog/rrweb-snapshot
@posthog/rrweb-utils
@posthog/sendgrid-plugin
@posthog/siphash
@posthog/snowflake-export-plugin
@posthog/taxonomy-plugin
@posthog/twilio-plugin
@posthog/twitter-followers-plugin
@posthog/url-normalizer-plugin
@posthog/variance-plugin
@posthog/web-dev-server
@posthog/wizard
@posthog/zendesk-plugin
```

Plus associated unscoped packages:
```
posthog-docusaurus
posthog-js
posthog-node
posthog-plugin-hello-world
posthog-react-native
posthog-react-native-session-replay
```

### @postman Packages (20 packages)
```
@postman/aether-icons
@postman/csv-parse
@postman/final-node-keytar
@postman/mcp-ui-client
@postman/node-keytar
@postman/pm-bin-linux-x64
@postman/pm-bin-macos-arm64
@postman/pm-bin-macos-x64
@postman/pm-bin-windows-x64
@postman/postman-collection-fork
@postman/postman-mcp-cli
@postman/postman-mcp-server
@postman/pretty-ms
@postman/secret-scanner-wasm
@postman/tunnel-agent
@postman/wdio-allure-reporter
@postman/wdio-junit-reporter
```

### @zapier Packages (12 packages)
```
@zapier/ai-actions
@zapier/ai-actions-react
@zapier/babel-preset-zapier
@zapier/browserslist-config-zapier
@zapier/eslint-plugin-zapier
@zapier/mcp-integration
@zapier/secret-scrubber
@zapier/spectral-api-ruleset
@zapier/stubtree
@zapier/zapier-sdk
```

Plus associated unscoped packages:
```
zapier-async-storage
zapier-platform-cli
zapier-platform-core
zapier-platform-legacy-scripting-runner
zapier-platform-schema
zapier-scripts
```

### @trigo Packages (15 packages)
```
@trigo/atrix
@trigo/atrix-acl
@trigo/atrix-elasticsearch
@trigo/atrix-mongoose
@trigo/atrix-orientdb
@trigo/atrix-postgres
@trigo/atrix-pubsub
@trigo/atrix-redis
@trigo/atrix-soap
@trigo/atrix-swagger
@trigo/bool-expressions
@trigo/eslint-config-trigo
@trigo/fsm
@trigo/hapi-auth-signedlink
@trigo/jsdt
@trigo/keycloak-api
@trigo/node-soap
@trigo/pathfinder-ui-css
@trigo/trigo-hapijs
```

### Additional High-Risk Categories

#### MCP (Model Context Protocol) Related:
```
@mcp-use/cli
@mcp-use/inspector
@mcp-use/mcp-use
mcp-use
mcp-knowledge-base
mcp-knowledge-graph
lite-serper-mcp-server
@postman/postman-mcp-cli
@postman/postman-mcp-server
@postman/mcp-ui-client
@zapier/mcp-integration
```

#### React Native & Mobile Development:
```
react-native-datepicker-modal
react-native-email
react-native-fetch
react-native-get-pixel-dimensions
react-native-jam-icons
react-native-log-level
react-native-phone-call
react-native-retriable-fetch
react-native-use-modal
react-native-view-finder
react-native-websocket
react-native-worklet-functions
```

#### Blockchain & Crypto:
```
ethereum-ens
crypto-addr-codec
gate-evm-check-code2
gate-evm-tools-test
evm-checkcode-cli
bytecode-checker-cli
```

#### Developer CLI Tools:
```
asyncapi-preview
create-glee-app
create-hardhat3-app
create-mcp-use-app
devstart-cli
zuper-cli
@kvytech/cli
@lessondesk/eslint-config
claude-token-updater
```

---

## Risk Assessment

### Critical Risk Factors

1. **Scope of Compromise**
   - 425 new packages under investigation
   - Multiple major platforms affected (PostHog, AsyncAPI, ENS, Postman, Zapier)
   - Core infrastructure tools compromised

2. **Impact on Enterprise**
   - Analytics and monitoring tools (PostHog suite)
   - API development and testing (Postman, AsyncAPI)
   - Integration platforms (Zapier)
   - Blockchain infrastructure (ENS ecosystem)

3. **Supply Chain Implications**
   - Many packages are developer tools that could inject malicious code into build processes
   - CLI tools have elevated privileges during installation
   - Framework packages affect entire application stacks

4. **Version Information Gap**
   - **No specific version information available** for these 425 packages
   - Unable to identify safe versions for rollback
   - **ALL versions should be considered potentially compromised**

---

## Immediate Actions Required

### 1. Inventory Check
```bash
# Check your project for potentially compromised packages
npm list | grep -E "@actbase|@asyncapi|@ensdomains|@posthog|@postman|@zapier|@trigo|@kvytech|@mcp-use"
```

### 2. Emergency Audit
```bash
# Run comprehensive audit
npm audit
npm audit fix --force  # Use with extreme caution
```

### 3. Dependency Review
- Review all direct and transitive dependencies
- Check for any packages from the affected organizations
- Look for recently updated packages that may have introduced compromised code

### 4. Code Scanning
- Scan for suspicious patterns in node_modules
- Check for unexpected network connections
- Review build scripts and postinstall hooks

### 5. Alternative Solutions
- Research alternative packages for critical dependencies
- Consider switching to well-maintained, verified alternatives
- Implement package lock strategies

---

## Detection Commands

### Using the Verifier Tool

```bash
# Scan a specific project
python3 enhanced_npm_compromise_detector_phoenix.py /path/to/project

# Scan with Phoenix Security API integration
./enhanced-quick-check-with-phoenix.sh

# Quick check for compromised packages
./quick-check-compromised-packages-2025.sh /path/to/project
```

### Manual Detection

```bash
# Check for PostHog packages
npm list | grep "@posthog"

# Check for AsyncAPI packages
npm list | grep "@asyncapi"

# Check for ENS packages
npm list | grep "@ensdomains"

# Check for Postman packages
npm list | grep "@postman"

# Check for Zapier packages
npm list | grep "@zapier"

# Check for MCP-related packages
npm list | grep "mcp"
```

---

## Remediation Strategy

### Phase 1: Immediate (0-24 hours)
1. **Stop all CI/CD pipelines** using affected packages
2. **Inventory all affected projects** across your organization
3. **Isolate affected systems** from production networks
4. **Alert security teams** and stakeholders

### Phase 2: Short-term (1-7 days)
1. **Remove compromised packages** where possible
2. **Implement temporary alternatives** or workarounds
3. **Audit git history** for unauthorized changes
4. **Review access logs** for suspicious activity
5. **Scan for data exfiltration** attempts

### Phase 3: Long-term (1-4 weeks)
1. **Establish package vetting process**
2. **Implement private NPM registry** with scanning
3. **Set up dependency monitoring** and alerts
4. **Create incident response playbook**
5. **Train development teams** on supply chain security

---

## Package Vetting Checklist

Before using any package from the affected list:

- [ ] Check package ownership and maintenance history
- [ ] Review recent commits and releases
- [ ] Verify package signatures if available
- [ ] Check for suspicious code patterns
- [ ] Review issue tracker for security concerns
- [ ] Consult with security team
- [ ] Document approval and justification
- [ ] Set up monitoring for package updates

---

## Monitoring Recommendations

### Continuous Monitoring

1. **Automated Scanning**
   ```bash
   # Add to CI/CD pipeline
   npm audit --json | python3 parse_audit.py
   python3 enhanced_npm_compromise_detector_phoenix.py .
   ```

2. **Dependency Tracking**
   - Use tools like Snyk, Dependabot, or Renovate
   - Enable GitHub security alerts
   - Set up Phoenix Security API monitoring

3. **Runtime Monitoring**
   - Monitor outbound network connections
   - Track file system access patterns
   - Log package installation events

---

## Additional Resources

### Related Documentation
- [USAGE_GUIDE.md](docs/USAGE_GUIDE.md) - How to use the detector tool
- [PHOENIX_INTEGRATION_GUIDE.md](docs/PHOENIX_INTEGRATION_GUIDE.md) - Phoenix Security API setup
- [GITHUB_ACTIONS_SUMMARY.md](docs/GITHUB_ACTIONS_SUMMARY.md) - CI/CD integration
- [REPOSITORY_SCANNING_GUIDE.md](REPOSITORY_SCANNING_GUIDE.md) - Scanning strategies

### External References
- NPM Security Advisory: https://docs.npmjs.com/about-security-audits
- OWASP Dependency Check: https://owasp.org/www-project-dependency-check/
- Phoenix Security API: https://phoenix.security

---

## Incident Timeline

- **2025-09-17**: Initial compromise detected (208 packages)
- **2025-11-24**: Significant expansion - 425 additional potentially compromised packages identified
- **Status**: ONGOING INVESTIGATION

---

## Contact & Support

### For Security Issues
- Security Team: [Your security team contact]
- Incident Response: [Your IR team contact]

### For Tool Support
- GitHub Issues: [Your repository issues page]
- Documentation: [Your docs location]

---

## Conclusion

This update represents a **significant escalation** in the NPM supply chain compromise incident. The addition of 425 potentially compromised packages, including major platforms like PostHog, AsyncAPI, ENS, Postman, and Zapier, indicates a sophisticated and wide-reaching attack.

### Key Takeaways

1. **Immediate action required** - Do not wait for version-specific information
2. **Assume compromise** - All versions of listed packages should be treated as potentially malicious
3. **Defense in depth** - Implement multiple layers of security controls
4. **Continuous vigilance** - This is an ongoing threat requiring sustained attention

### Next Steps

1. Run the detection tool on all projects
2. Review and update your dependency management policies
3. Implement continuous monitoring
4. Prepare incident response procedures
5. Stay informed about updates to this incident

---

**Document Version**: 1.0  
**Last Updated**: November 24, 2025  
**Classification**: CRITICAL - FOR IMMEDIATE DISTRIBUTION  
**Author**: Security Team / Senior Developer






