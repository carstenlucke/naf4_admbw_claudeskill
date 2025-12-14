# Extended Examples for NAF Requirement Title Generation

## Domain-Specific Examples

### Military/Defense Domain

| Full Description | Generated Title | Rationale |
|-----------------|----------------|-----------|
| "The command and control system shall provide tactical commanders with real-time situational awareness data within 500ms of sensor input reception" | `Tactical Situational Awareness 500ms` | Keeps domain term "tactical", key metric, removes redundant context |
| "All classified information at SECRET level or above must be encrypted using NSA Suite B cryptographic algorithms" | `Classify SECRET Encrypt Suite B` | Preserves classification level and crypto standard |
| "The system shall maintain Common Operational Picture (COP) consistency across all federation nodes with maximum 2-second latency" | `COP Consistency 2s Latency` | Uses known acronym COP, keeps performance constraint |

### Healthcare Domain

| Full Description | Generated Title | Rationale |
|-----------------|----------------|-----------|
| "Patient health records must comply with HIPAA Privacy Rule requirements for protected health information (PHI) storage and transmission" | `PHI HIPAA Compliance` | Uses standard acronyms PHI and HIPAA |
| "The electronic prescription system shall validate drug interactions against the current FDA-approved contraindication database before confirming prescription" | `Validate Drug Interactions FDA` | Core action + domain object + authority |
| "Medical imaging data in DICOM format must be transmitted using TLS 1.3 with mutual authentication" | `DICOM Transmission TLS 1.3` | Keeps medical standard DICOM, security protocol |

### Financial Services Domain

| Full Description | Generated Title | Rationale |
|-----------------|----------------|-----------|
| "All payment card transactions must be processed in compliance with PCI DSS Level 1 requirements including encryption of cardholder data" | `Payment Card PCI DSS Level 1` | Industry standard PCI DSS with level specification |
| "The trading system shall execute market orders within 10 milliseconds of receipt during normal market conditions" | `Execute Market Orders 10ms` | Core function with critical latency requirement |
| "Customer identity verification must follow Know Your Customer (KYC) regulations including multi-source identity document validation" | `KYC Identity Verification` | Standard financial acronym KYC |

### Aerospace Domain

| Full Description | Generated Title | Rationale |
|-----------------|----------------|-----------|
| "Flight control software must achieve DO-178C Level A certification for all safety-critical components" | `Flight Control DO-178C Level A` | Aviation standard with criticality level |
| "The autopilot system shall maintain altitude within ±50 feet of commanded altitude during cruise flight" | `Autopilot Altitude Control ±50ft` | Specific tolerance requirement |
| "All avionic systems must comply with ARINC 653 partitioning requirements to ensure spatial and temporal isolation" | `Avionics ARINC 653 Partitioning` | Standard avionics protocol |

## Complex Linguistic Patterns

### Nested Conditionals

**Input:** "If the user authentication fails three consecutive times within a 15-minute window, then the system shall lock the account and send notification to the security administrator unless the user is accessing from a whitelisted IP address"

**Analysis:** Multiple conditions create complexity
- Primary requirement: Account lockout
- Key parameters: 3 attempts, 15 minutes
- Secondary action: Notification
- Exception: Whitelisted IPs

**Title Options:**
1. `Account Lockout 3 Failed Attempts` (Focus on main action)
2. `Authenticate Lockout 3x15min` (Condensed parameters)
3. `Failed Login Account Lock` (Simple action-result)

**Recommended:** `Account Lockout 3 Failed Attempts`
**Note to user:** "This requirement contains multiple conditions. Consider splitting into: (1) Lockout policy, (2) Admin notification, (3) Whitelist exception"

### Negation Requirements

**Input:** "The system shall not store any credit card numbers, CVV codes, or magnetic stripe data in any database or log file after transaction authorization is complete"

**Analysis:**
- Negative requirement (what NOT to do)
- Multiple prohibited items
- Temporal constraint: after authorization

**Title Options:**
1. `No PCI Data Storage Post-Auth` (Negative + constraint)
2. `Prohibit Card Data Retention` (Positive framing)
3. `Delete Card Data After Auth` (Action-oriented)

**Recommended:** `Delete Card Data After Auth` (Positive framing preferred)

### Compound Requirements

**Input:** "The system shall validate, sanitize, and escape all user input before processing to prevent SQL injection, cross-site scripting, and command injection attacks"

**Analysis:**
- Multiple actions: validate, sanitize, escape
- Multiple threat types
- Core concept: Input security

**Title:** `Validate Sanitize User Input`
**Alternative:** `Input Security Anti-Injection`
**Note to user:** "This combines multiple security measures. All are captured in the description."

## Handling Ambiguity

### Generic vs. Specific

**Vague input:** "The system should be fast"
**Title:** `System Performance` (Generic but unavoidable)
**Note:** "This requirement is too vague. Specify: What operation? How fast? Under what conditions?"

**Better input:** "The dashboard shall load within 1 second on initial access"
**Title:** `Dashboard Load Time 1s` (Specific and measurable)

### Implied vs. Explicit

**Input with implied actor:** "Shall authenticate using biometric factors"
**Analysis:** Who authenticates? System or user?
**Title:** `Biometric Authentication` (Neutral)
**Question:** "Should I specify 'User Biometric Authentication' or 'System Biometric Verification'?"

**Input with explicit actor:** "Administrator shall configure system parameters via web interface"
**Title:** `Admin Configure Parameters` (Actor is distinctive, kept)

## Edge Cases

### Pure Compliance Requirements

**Input:** "The system shall comply with all applicable provisions of GDPR Article 17 regarding the right to erasure of personal data"

**Title:** `GDPR Article 17 Compliance`
**Alternative:** `Right to Erasure GDPR`

**Reasoning:** When requirement IS compliance, compliance becomes the functional element

### Threshold Boundaries

**Input:** "System shall support minimum 1000 concurrent users with 95% of transactions completing under 3 seconds and 99% under 5 seconds"

**Analysis:** Multiple performance tiers
**Title:** `Concurrent Users 1000 3s Response`
**Alternative:** `Performance 1000 Users 95%@3s`

**Recommendation:** Choose based on primary constraint (capacity vs. latency)

### Multi-Level Decomposition

**Input:** "The API gateway shall implement rate limiting with tier-based thresholds: Bronze tier limited to 100 requests/hour, Silver to 1000 requests/hour, Gold to 10000 requests/hour, and Platinum unlimited with burst protection"

**Analysis:** One requirement with multiple configuration values
**Title:** `API Rate Limiting Tiered`
**Note:** "Tier details preserved in description. Title captures capability, not configuration."

## Language-Specific Patterns

### German Requirements (Common in ADMBw Context)

**Input:** "Das System muss die Möglichkeit bieten, Einstellungen zu überprüfen und zu speichern"

**Title (English):** `Verify Save Settings`
**Title (German):** `Einstellungen Prüfen Speichern`

**Note:** NAF models typically use English titles even for German descriptions, but maintain language consistency if specified.

### Passive Voice Conversion

**Input:** "User credentials must be validated against the LDAP directory before access is granted"

**Passive Construction Analysis:**
- Who validates? System (implied)
- What is validated? Credentials
- Against what? LDAP

**Title:** `Validate Credentials LDAP`
**Active Voice Alternative:** `LDAP Credential Validation`

## Quality Attributes Mapping

### Performance Requirements

| Attribute | Pattern | Example Title |
|-----------|---------|---------------|
| Latency | `[Operation] [Threshold]` | `API Response 200ms` |
| Throughput | `[System] [Volume]/[Time]` | `Process 10000 Transactions/Hour` |
| Capacity | `[Resource] [Limit]` | `Support 50000 Concurrent Users` |
| Efficiency | `[Resource] [Usage] [Constraint]` | `Memory Usage <4GB` |

### Security Requirements

| Attribute | Pattern | Example Title |
|-----------|---------|---------------|
| Authentication | `[Method] [Scope]` | `Multi-Factor User Authentication` |
| Authorization | `[Control Type] [Resource]` | `Role-Based Access Control` |
| Encryption | `[Data Type] [Algorithm]` | `Data At Rest AES-256` |
| Audit | `[Event Type] Logging` | `Security Event Logging` |

### Usability Requirements

| Attribute | Pattern | Example Title |
|-----------|---------|---------------|
| Learnability | `[User Type] Training [Time]` | `New User Training <2 Hours` |
| Accessibility | `[Standard] [Level]` | `WCAG 2.1 Level AA` |
| Error Prevention | `[Validation Type]` | `Input Validation User Errors` |

## Advanced Condensation Techniques

### Abbreviation Principles

**Standard Technical Abbreviations (Keep):**
- API, REST, SOAP, HTTP, HTTPS, FTP, SSH
- SQL, NoSQL, JSON, XML, YAML, CSV
- CPU, RAM, GB, MB, KB
- TLS, SSL, AES, RSA, SHA

**Domain Abbreviations (Context-dependent):**
- NAF, DoDAF, TOGAF (architecture frameworks)
- CRUD (Create, Read, Update, Delete)
- RBAC (Role-Based Access Control)
- SSO (Single Sign-On)

**Avoid Unless Standard:**
- Custom project acronyms
- Company-specific abbreviations
- Locale-specific terms

### Number Formatting

**Prefer compact notation:**
- `1000 users` → `1000 Users` or `1K Users`
- `500 milliseconds` → `500ms`
- `2 gigabytes` → `2GB`
- `99.99% availability` → `99.99% Uptime` or `Availability 99.99%`

### Temporal Expression

**Time periods:**
- Daily, Weekly, Monthly, Annually → Keep as-is
- "every 24 hours" → `Daily`
- "once per week" → `Weekly`
- "within 2 business days" → `Within 2 Days` (if critical) or omit

**Duration:**
- "for 30 days" → `30 Days`
- "maximum 5 minutes" → `Max 5min`
- "at least 1 hour" → `Min 1 Hour`

## Title Evolution Through Requirement Lifecycle

### Initial Draft → Final Title

**Draft 1:** "Need something to check if settings are saved"
**Title:** `Settings Verification` (Generic initial)

**Draft 2:** "System should verify that settings are saved"
**Title:** `Verify Settings Saved` (More specific)

**Draft 3:** "System shall provide operator verification that configuration settings have been successfully persisted to non-volatile storage"
**Title:** `Verify Settings Saved` (Same - technical details in description)

**Observation:** Title stabilizes early, additional precision goes to description

## User Preference Patterns

### Organizational Styles

**Software Development Team:**
- Prefers: `VerifySettingsSaved` (PascalCase, code-like)
- Format: Technical identifier style

**Systems Engineering:**
- Prefers: `Verify Settings Saved` (Title Case, readable)
- Format: Clear descriptive style

**Compliance/Audit:**
- Prefers: `REQ-FUNC-001: Verify Settings Saved` (With formal ID)
- Format: Traceable identifier

**Defense/Military:**
- Prefers: `FR-SYS-VERIFY-01` (Hierarchical codes)
- Format: Strict taxonomy

**Recommendation:** Establish organizational standard, then apply consistently
