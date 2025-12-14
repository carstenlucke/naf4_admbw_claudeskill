---
name: nafv4-assistant
description: NAF v4 / ADMBw modeling assistant providing convenience functions for common modeling tasks. Offers specialized utilities like requirement naming, batch operations, and modeling helpers. Automatically routes to appropriate function based on user request or allows browsing available functions. Integrates with nafv4-coordinator for all NAF modeling operations.
---

# NAF v4 Assistant - Convenience Functions

## Overview

This assistant skill provides high-level convenience functions for NAF v4 / ADMBw modeling in Sparx Enterprise Architect. It acts as a productivity layer on top of the core NAF modeling skills, offering specialized utilities for common repetitive tasks.

## Core Responsibilities

1. **Function Routing** - Recognize which convenience function the user needs based on keywords and context
2. **Function Discovery** - Help users discover available convenience functions
3. **Coordinator Integration** - Route all NAF modeling operations through nafv4-coordinator
4. **Batch Processing** - Handle multiple modeling operations efficiently

## Architecture

The assistant follows a cascading skill architecture:

```
User Request
    ↓
nafv4-assistant (this skill)
    ↓
nafv4-coordinator
    ↓
Specialized NAF Skills:
  - nafv4-requirements
  - nafv4-architecture-metadata
  - nafv4-concepts
  - nafv4-logical-specification
  - nafv4-physical-resources
  - nafv4-service-specification
```

**Exception:** If the user explicitly mentions a specific NAF skill (e.g., "use nafv4-requirements"), the assistant can directly invoke that skill.

## General Modeling Rules

These rules apply to all NAF v4 modeling tasks:

### 1. Modeling Target Clarification

When the modeling target is unclear, always ask the user where to model:
- **Currently open diagram** - Add elements to the active diagram
- **Specific (non-displayed) diagram** - Add to a named diagram that may not be open
- **Package in workspace** - Create elements in a specific package location
- **New diagram** - Create a new diagram first

**Default behavior:** If not explicitly specified, use the currently open diagram as the modeling target.

### 2. Element Existence Verification

Before using element names in any operation, especially when creating connections:
- **Always check first** if the element already exists in the diagram or workspace
- Use MCP `find_elements_by_name` to search for elements
- If multiple elements with the same name exist, ask the user to clarify which one (by package path or GUID)
- If the element doesn't exist, offer to create it or ask for clarification

**This prevents:**
- Creating duplicate elements
- Invalid connections to non-existent elements
- Confusion about which element is being referenced

## Available Convenience Functions

### 1. Requirement Naming

**Function:** Generate concise, information-rich titles for NAF v4 requirements from verbose descriptions.

**Triggers:**
- Keywords: "requirement naming", "name requirements", "create titles", "short names"
- Context: User provides list of requirement descriptions without names
- Pattern: "create requirement with description: [long text]"

**Load details:** `functions/requirement-naming.md`

**Usage Examples:**
```
"I have 20 detailed requirement descriptions. Can you create short names for them?"
"Generate requirement titles for these functional requirements: [list]"
"Name these requirements: 1. The system shall..., 2. Users must be able to..."
```

**See:** Extended examples in `references/extended_examples.md`

---

### [Future Functions]

Additional convenience functions will be added here as they are developed:
- **Batch Element Creation** - Create multiple similar elements efficiently
- **Diagram Template Application** - Apply standard diagram layouts
- **Traceability Matrix Generation** - Generate requirement traceability reports
- **Model Validation** - Check model completeness and consistency
- **Import/Export Helpers** - Import requirements from Excel, export to documentation

## Function Routing Logic

### Automatic Detection

The assistant analyzes user requests for:

1. **Explicit function mention**
   - Example: "Use requirement naming for these descriptions"
   - Action: Confirm with user, then activate function

2. **Keyword triggers**
   - Example: "Create short names for 15 requirements"
   - Detected keywords: "short names", "requirements"
   - Match: Requirement Naming function
   - Action: Confirm detection, then activate

3. **Context pattern matching**
   - Example: User provides list of verbose requirement texts
   - Detected pattern: Multiple long descriptions, likely needs naming
   - Action: Ask user if requirement naming is needed

4. **No clear match**
   - Action: Present list of available functions and ask user to select

### Confirmation Before Execution

When a function is detected (via keywords or pattern):

```
Assistant: "I've detected you might need the Requirement Naming function.
           Is that correct?

           This function will:
           - Analyze each requirement description
           - Generate concise 3-8 word titles
           - Preserve full descriptions in notes field

           Proceed with requirement naming?"

User: "Yes" / "No, I meant..."
```

### Manual Function Selection

User can explicitly request to see available functions:

```
User: "What convenience functions do you offer?"
User: "Show me what the assistant can do"
User: "List available functions"
```

**Response format:**

```
Assistant: "NAF v4 Assistant - Available Convenience Functions:

1. **Requirement Naming**
   Generate concise titles from verbose requirement descriptions
   Use when: You have detailed requirements needing short names

2. [Future functions will appear here]

Which function would you like to use?"
```

## Integration with NAF Coordinator

All modeling operations are routed through **nafv4-coordinator**, which then dispatches to specialized skills:

### Available Skills

The assistant can work with these NAF v4 skills:

**Coordinator:**
- **nafv4-coordinator** - Routes to specialized viewpoint skills, handles cross-viewpoint relationships

**Specialized Viewpoint Skills:**
- **nafv4-requirements** - Requirements Viewpoints (R2-R6)
- **nafv4-architecture-metadata** - Architecture Metadata Viewpoints (A1-A8, Ar)
- **nafv4-concepts** - Concepts Viewpoints (C1-C8, Cr)
- **nafv4-logical-specification** - Logical Specification Viewpoints (L1-L8, Lr)
- **nafv4-physical-resources** - Physical Resource Specification Viewpoints (P1-P8, Pr)
- **nafv4-service-specification** - Service Specification Viewpoints (S1-S8, Sr)

### Standard Routing Pattern

```
User: "Create these 10 requirements with generated names: [list]"

↓ nafv4-assistant recognizes requirement naming need

Assistant (internal): Load functions/requirement-naming.md

↓ Generate titles using naming algorithm

Assistant (internal): Call nafv4-coordinator to create requirements

↓ nafv4-coordinator routes to nafv4-requirements

↓ nafv4-requirements creates requirement elements via MCP

↓ Result returned to user
```

### Direct Skill Invocation

If user explicitly names a specific NAF skill:

```
User: "Use nafv4-requirements to add this functional requirement: [description]"

↓ nafv4-assistant detects explicit skill mention

↓ Directly invoke nafv4-requirements (skip nafv4-coordinator)

↓ nafv4-requirements handles the request

↓ Result returned to user
```

## Workflow Examples

### Example 1: Batch Requirement Creation with Naming

**User Input:**
```
"I have these 3 functional requirements that need short names:

1. The system shall provide the operator with the option to verify that
   the system has saved the new software settings.

2. All patient data must be encrypted using AES-256 encryption before
   transmission over the network.

3. The application shall respond to user queries within 2 seconds under
   normal load conditions."
```

**Assistant Workflow:**

1. **Detect function:** Keywords "short names" + list of requirements → Requirement Naming
2. **Confirm:** "I've detected you need requirement naming. Proceed?"
3. **Load function details:** `functions/requirement-naming.md`
4. **Generate titles:**
   - FR-1: "Verify Settings Saved"
   - FR-2: "Encrypt Patient Data AES-256"
   - FR-3: "Query Response Time <2s"
5. **Route to coordinator:** Request creation of 3 FunctionalRequirement elements
6. **Coordinator routes** to nafv4-requirements
7. **Confirm to user:**
   ```
   Created 3 functional requirements:
   1. "Verify Settings Saved"
   2. "Encrypt Patient Data AES-256"
   3. "Query Response Time <2s"

   Full descriptions preserved in notes field.
   ```

### Example 2: Function Discovery

**User Input:**
```
"What can the assistant do?"
```

**Assistant Response:**
```
NAF v4 Assistant - Available Convenience Functions:

1. **Requirement Naming**
   Generate concise, information-rich titles from verbose requirement descriptions

   Typical use: "I have 20 requirements needing short names"
   Triggers: "requirement naming", "create titles", "short names"

[Future functions listed here as added]

Would you like to use any of these functions?
```

### Example 3: Ambiguous Request

**User Input:**
```
"Help me with these requirements: [list of 5 detailed descriptions]"
```

**Assistant Response:**
```
I see you have 5 requirement descriptions. Which function would help you?

1. **Requirement Naming** - Generate short titles for these requirements
2. **Create Requirements** - Add these to your NAF model (via coordinator)
3. **Both** - Generate names AND create in model

Which would you like?
```

## Progressive Data Loading

**Always in context:**
- Core routing logic (this SKILL.md)
- Available functions list
- Integration patterns

**Load on demand:**
- `functions/requirement-naming.md` - When requirement naming is needed
- `references/extended_examples.md` - When user needs examples or edge cases
- [Future function files] - As additional functions are developed

This keeps the skill efficient while providing access to detailed algorithms when needed.

## Best Practices

### For Users

1. **Be explicit when possible**
   - Good: "Use requirement naming for these 10 descriptions"
   - Okay: "Create short names for these requirements"
   - Vague: "Help with these" (assistant will ask for clarification)

2. **Provide context**
   - If working on a specific diagram, mention it
   - If targeting a specific package, specify it
   - If using organizational naming conventions, state them

3. **Batch operations are efficient**
   - Process multiple requirements at once
   - Assistant handles iteration internally

4. **Review generated output**
   - Titles are algorithmically generated
   - Review for accuracy and consistency
   - Request adjustments if needed

### For the Assistant (Internal Guidelines)

1. **Always confirm before execution**
   - Especially for batch operations
   - Show what will be done before doing it

2. **Load function details only when needed**
   - Keep initial response fast
   - Load detailed algorithms on demand

3. **Route through coordinator by default**
   - Exception: Explicit skill mention
   - Coordinator handles cross-viewpoint complexity

4. **Preserve user intent**
   - Keep full descriptions in notes
   - Generated names supplement, don't replace

## Error Handling

### Function Not Recognized

```
User: "Create widget names for these items"