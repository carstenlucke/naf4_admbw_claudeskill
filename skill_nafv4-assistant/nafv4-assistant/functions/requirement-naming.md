# Requirement Naming Function

## Purpose

Generate concise, information-rich titles for NAF v4 requirements (functional/non-functional) from verbose requirement descriptions.

## When to Use

- User provides detailed requirement descriptions (50-200 words) but needs short titles (3-8 words)
- Creating requirement elements where description text is provided but names are missing
- Batch processing of multiple requirements needing consistent naming
- Transforming natural language requirements into scannable, searchable titles

## Core Principle

**Extract semantic core, discard linguistic scaffolding.**

Requirements descriptions contain:
- **Content words** (nouns, verbs, domain terms) → Keep these
- **Function words** (articles, conjunctions, modal verbs) → Remove these
- **Qualifiers and elaborations** → Condense or remove based on uniqueness

The goal is maximum information density in minimum words.

## Title Generation Algorithm

### Step 1: Parse Description Structure

Identify these common requirement patterns:

**Actor-Action-Object pattern:**
- "The system shall provide the operator with..."
- "Users must be able to verify..."
- Extraction: [Actor] + [Action] + [Object]

**Constraint pattern:**
- "The system shall not exceed..."
- "Data must be encrypted using..."
- Extraction: [Constraint Type] + [Target] + [Condition]

**Quality attribute pattern:**
- "The system shall respond within 2 seconds..."
- "The interface must support 1000 concurrent users..."
- Extraction: [Quality Attribute] + [Measured Entity] + [Threshold]

### Step 2: Extract Core Components

**Priority extraction order:**

1. **Domain-specific nouns** (highest priority)
   - Technical terms: "encryption", "API", "database"
   - Domain concepts: "invoice", "patient record", "flight plan"
   - System components: "login module", "backup service"

2. **Action verbs** (main function)
   - Core actions: "verify", "validate", "generate", "transmit"
   - Avoid generic verbs: "provide", "allow", "enable" (unless specific)

3. **Key qualifiers** (when essential)
   - Security levels: "encrypted", "authenticated"
   - Performance thresholds: "real-time", "< 2s"
   - Scope limiters: "initial", "backup", "emergency"

### Step 3: Remove Non-Essential Elements

**Always remove:**
- Modal verbs: "shall", "must", "should", "will"
- Articles: "the", "a", "an"
- Filler phrases: "be able to", "provide the capability to", "have the option to"
- Redundant context: "the system", "the operator", "the user" (unless disambiguation needed)
- Politeness/hedging: "please", "if possible", "ideally"

**Conditionally remove:**
- Standard actors ("user", "operator", "system") → Remove unless multiple actor types exist
- Common verbs ("provide", "support", "allow") → Remove if action is implied by object
- Temporal markers ("after", "before", "during") → Keep only if timing is the requirement's essence

### Step 4: Construct Title

**Format options (choose based on requirement type):**

1. **Imperative form** (preferred for functional requirements)
   - Pattern: `[Verb] + [Object] + [Qualifier]`
   - Example: "Verify Settings Saved"
   - Example: "Encrypt Patient Data"

2. **Noun phrase** (preferred for architectural/non-functional)
   - Pattern: `[Adjective] + [Noun] + [Context]`
   - Example: "Real-time Data Synchronization"
   - Example: "Dual-Factor Authentication"

3. **Technical identifier** (for system requirements)
   - Pattern: `[Component] + [Function] + [Constraint]`
   - Example: "API Response Timeout 2s"
   - Example: "Database Backup Daily"

4. **Abbreviated technical format** (optional, with prefix)
   - Pattern: `[FR/NFR]-[ShortCode]`
   - Example: "FR-VerifySettings"
   - Example: "NFR-PerformanceThreshold"

**Length constraints:**
- Target: 3-5 words
- Maximum: 8 words
- Minimum: 2 words
- Character limit: ~50 characters

**Casing conventions:**
- PascalCase: `VerifySettingsSaved` (compact, programming-style)
- Title Case: `Verify Settings Saved` (readable, documentation-style)
- Hyphenated: `verify-settings-saved` (technical identifier style)

Choose casing based on user's preference or organizational standard.

### Step 5: Validate Information Preservation

**Quality checks:**

1. **Uniqueness test**: Would this title distinguish the requirement from others in the same category?
2. **Comprehension test**: Can a domain expert understand the core requirement from the title alone?
3. **Searchability test**: Would someone searching for this requirement use these keywords?
4. **Reversibility test** (weak): Could someone familiar with the domain reconstruct the approximate requirement from the title?

If any test fails, add one key qualifier to improve clarity.

## Common Transformation Patterns

### Pattern: Actor-Action-Object

**Input:** "The system shall provide the operator with the option to verify that the system has saved the new software settings."

**Analysis:**
- Actor: "operator" (common, removable)
- Action: "verify" (core)
- Object: "settings saved" (core)
- Scaffolding: "provide...with the option to", "the system", "new software"

**Output:** `Verify Settings Saved`

---

### Pattern: Constraint Specification

**Input:** "The system must ensure that all patient data is encrypted using AES-256 encryption before transmission over the network."

**Analysis:**
- Core requirement: encryption
- Object: patient data
- Specification: AES-256 (important technical detail)
- Scaffolding: "must ensure", "before transmission over the network"

**Output:** `Encrypt Patient Data AES-256`

---

### Pattern: Performance Requirement

**Input:** "The application shall respond to user queries within 2 seconds under normal load conditions with up to 1000 concurrent users."

**Analysis:**
- Quality attribute: response time
- Threshold: 2 seconds (critical)
- Context: user queries
- Scaffolding: "under normal load conditions", "with up to"

**Output:** `Query Response Time <2s`
**Alternative:** `User Query Performance 2s`

---

### Pattern: Access Control

**Input:** "Only authenticated administrators who have been granted the 'System Admin' role shall be permitted to access the configuration management interface."

**Analysis:**
- Core concept: access control
- Actor: administrators (specific, keep)
- Object: configuration interface
- Qualifier: role-based
- Scaffolding: "who have been granted", "shall be permitted to"

**Output:** `Admin Access Configuration`
**Alternative:** `Role-Based Config Access`

---

### Pattern: Data Validation

**Input:** "Before accepting any input from external sources, the system must validate that the data format conforms to the defined XML schema and reject any non-conforming data."

**Analysis:**
- Action: validate (core)
- Target: external input
- Method: XML schema
- Scaffolding: "Before accepting", "must validate that"

**Output:** `Validate External Input Schema`
**Alternative:** `XML Schema Validation`

## Special Cases

### Case 1: Multiple Requirements in One Description

If description contains multiple distinct requirements (using "and", "also", "additionally"):

1. **Identify** the primary requirement
2. **Generate title** for primary requirement only
3. **Suggest** to user: "This description contains multiple requirements. Consider splitting into separate requirement elements."

**Example:**
Input: "System shall verify settings saved AND notify user of successful save AND log the change."

Output: `Verify Settings Saved` (primary)
Suggestion: "Consider creating separate requirements for user notification and audit logging."

### Case 2: Vague or Underspecified Requirements

If description lacks concrete nouns or verbs:

1. **Extract** available specifics
2. **Use generic qualifiers** where necessary
3. **Flag** to user: "Title may be generic due to vague description. Consider adding more specifics."

**Example:**
Input: "The system should be user-friendly and easy to use."

Output: `User Interface Usability`
Note: "This requirement is vague. Consider specifying measurable usability criteria."

### Case 3: Compound Technical Terms

Preserve domain-specific compound terms intact:

- "two-factor authentication" → Keep as unit
- "real-time synchronization" → Keep as unit
- "end-to-end encryption" → Keep as unit

**Example:**
Input: "System shall implement two-factor authentication for all user logins."

Output: `Two-Factor Authentication`
**NOT:** `Two Factor Login Auth` (breaks semantic unit)

### Case 4: Acronyms and Abbreviations

Handle existing acronyms appropriately:

1. **Keep** well-known acronyms: API, SQL, HTTP, XML, JSON
2. **Keep** domain-specific acronyms if target audience knows them
3. **Expand** obscure acronyms in title, use acronym in description

**Example:**
Input: "The REST API shall return JSON formatted responses compliant with RFC 7159."

Output: `REST API JSON Response`
**NOT:** `REpresentational State Transfer...` (over-expansion)

## Integration Pattern

When invoked by nafv4-assistant:

1. Receive list of requirement descriptions
2. For each description:
   - Apply algorithm (Steps 1-5)
   - Generate title
   - Validate quality
3. Return list of generated titles
4. Assistant routes to nafv4-coordinator to create requirements
5. Coordinator dispatches to nafv4-requirements
6. Requirements created with generated names and full descriptions

## Best Practices

### DO:
- Prioritize domain-specific terminology
- Keep technical precision (numbers, standards, protocols)
- Use active verbs for functional requirements
- Use noun phrases for quality attributes
- Maintain consistency within a requirement set

### DON'T:
- Include full sentences in titles
- Use pronouns without antecedent ("it", "this", "that")
- Include implementation details unless they ARE the requirement
- Use marketing language ("seamless", "robust", "cutting-edge")
- Replicate information better suited for categorization or tagging

## Examples by Requirement Type

### Functional Requirements (FR)

| Description | Generated Title |
|-------------|----------------|
| "System shall authenticate users via LDAP directory" | `LDAP User Authentication` |
| "Application must export reports to PDF format" | `Export Reports PDF` |
| "Operator can override automatic shutdown sequence" | `Override Automatic Shutdown` |
| "System validates credit card using Luhn algorithm" | `Validate Credit Card Luhn` |

### Non-Functional Requirements (NFR)

| Description | Generated Title |
|-------------|----------------|
| "System shall maintain 99.9% uptime annually" | `System Availability 99.9%` |
| "All data transmissions must use TLS 1.3" | `Data Transmission TLS 1.3` |
| "User interface shall support WCAG 2.1 Level AA" | `UI Accessibility WCAG 2.1` |
| "Database queries must complete within 500ms" | `Database Query Performance 500ms` |

### Security Requirements

| Description | Generated Title |
|-------------|----------------|
| "Passwords must meet complexity requirements: 12 chars, mixed case, numbers, symbols" | `Password Complexity Policy` |
| "System shall lock account after 3 failed login attempts" | `Account Lockout After 3 Attempts` |
| "Sensitive data at rest must be encrypted using AES-256" | `Encrypt Data At Rest AES-256` |

### Interface Requirements

| Description | Generated Title |
|-------------|----------------|
| "System exposes RESTful API conforming to OpenAPI 3.0 specification" | `RESTful API OpenAPI 3.0` |
| "Integration with SAP via RFC protocol" | `SAP Integration RFC` |
| "Accepts CSV files with UTF-8 encoding" | `CSV Import UTF-8` |

## Troubleshooting

**Problem:** Generated title is too generic
**Solution:**
- Check if description contains specific technical terms → Include them
- Look for measurable criteria or thresholds → Add to title
- Consider the requirement's distinguishing characteristic

**Problem:** Generated title is too long (>8 words)
**Solution:**
- Remove qualifiers that are implied by context
- Use standard abbreviations (API not "Application Programming Interface")
- Combine compound concepts ("Dual-Factor Auth" not "Dual Factor Authentication System")

**Problem:** Multiple valid title options
**Solution:**
- Choose the option that best matches organizational naming conventions
- Default to imperative form for functional requirements
- Ask user if unsure: "I can generate either '[Option A]' or '[Option B]'. Which fits better?"

## Extended Examples

See `references/extended_examples.md` for:
- Domain-specific examples (Military, Healthcare, Financial, Aerospace)
- Complex linguistic patterns
- Edge cases and special scenarios
- Language-specific patterns
