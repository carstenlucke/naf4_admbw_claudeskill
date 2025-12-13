---
name: nafv4-interface-ea-mcp
description: Create and manage NAF v4 (NATO Architecture Framework) / ADMBw Requirements Viewpoints (R2-R6) in Sparx Enterprise Architect. Use when the user wants to create R2 (Requirement Catalogue), R3 (Requirement Dependencies), R4 (Requirement Conformance), R5 (Requirement Derivation), or R6 (Requirement Realization) diagrams, add requirements elements, create associations between requirements, or work with NAF requirements modeling. Also triggers on natural language like "functional requirement", "requirement category", "derived from", "conforms to standard", etc.
---

# NAF v4 Requirements Modeling for Sparx Enterprise Architect

## Overview

This skill enables natural language interaction with Sparx Enterprise Architect's MCP server to create NAF v4 / ADMBw compliant Requirements Viewpoints. It translates informal user requests into precise MCP tool calls with correct stereotypes, UML types, and profiles.

## Core Workflow

When the user requests NAF requirements modeling:

1. **Parse the request** - Identify what the user wants (diagram, element, or association)
2. **Map to NAF metamodel** - Translate natural language to formal stereotypes using references
3. **Execute MCP calls** - Create or update models in Sparx EA
4. **Confirm and offer next steps** - Show what was created and suggest related actions

## Key Principles

- **Interpret flexibly** - Accept natural language like "add a functional requirement" or "create derived from link"
- **Map precisely** - Always use exact stereotypes and UML types from the metamodel
- **Auto-name when needed** - If user provides description but no name, generate concise technical name
- **Validate connections** - Check metaconstraints before creating associations (see JSON data)
- **Ask when ambiguous** - Offer options if request could map to multiple stereotypes

## Supported Viewpoints

| Viewpoint | ID | Purpose | Common Requests |
|-----------|----|---------|-----------------| 
| Requirement Catalogue | R2 | Organize requirements in categories | "Create R2 diagram", "Add requirement category" |
| Requirement Dependencies | R3 | Show relationships between requirements | "Show conflicts", "X refines Y" |
| Requirement Conformance | R4 | Link requirements to standards | "Link to standard", "Conforms to ISO" |
| Requirement Derivation | R5 | Trace requirement origins | "Derived from document", "Trace to source" |
| Requirement Realization | R6 | Map to implementing elements | "Realized by component", "Add acceptance criteria" |

## Creating Diagrams

To create a NAF requirements diagram, use the MCP `create_or_update_diagram` tool:

```javascript
{
  "name": "<diagram-name>",
  "type": "Custom",  // NAF diagrams are always Custom type
  "stereotype": "<viewpoint-identifier>",  // e.g. "R2", "R3", "R4", "R5", "R6"
  "packagePath": "<package-path>",  // e.g. "Model/Requirements"
  "extendedProperties": {
    "alias": "<full-viewpoint-name>",  // e.g. "R2 - Requirement Catalogue"
    "diagramID": "<viewpoint-id>",     // e.g. "R2"
    "toolbox": "<toolbox-name>"        // e.g. "NAFv4-ADMBw-R2-Toolbox"
  }
}
```

**Example user requests:**
- "Create an R2 diagram called 'System Requirements'"
- "Make a new Requirement Dependencies view"
- "I need an R5 diagram for requirements traceability"

## Creating Elements

To create a NAF requirement element, use the MCP `create_or_update_element` tool:

```javascript
{
  "name": "<element-name>",
  "type": "<uml-type>",           // e.g. "Requirement", "Class", "Object"
  "stereotype": "<NAF-stereotype>", // e.g. "FunctionalRequirement"
  "packagePath": "<package-path>",
  "notes": "<description>",        // User's full description text
  "profile": "NAFv4-ADMBw"        // Always use this profile
}
```

**Auto-naming logic:**
When user provides description but no name, generate a concise technical identifier:
- Extract key concepts from description
- Use PascalCase or hyphenated format
- Keep to 3-5 words maximum
- Example: "System shall verify settings" → "VerifySettingsSaved" or "FR-VerifySettings"

**Example user requests:**
- "Add functional requirement 'System shall provide operator verification'"
- "Create a RequirementCategory named 'Security Requirements'"
- "Add Standard element for ISO 27001"
- "Add functional requirement with description: System shall provide the operator with the option to verify that the system has saved the new software settings"

## Creating Associations

To create connections between elements, use the MCP `create_or_update_connector` tool:

```javascript
{
  "sourceElementName": "<source-element>",
  "targetElementName": "<target-element>",
  "connectorType": "<uml-connector-type>",  // e.g. "Dependency", "Aggregation", "Realisation"
  "stereotype": "<NAF-stereotype>",          // e.g. "DerivedFrom", "ConformsTo"
  "packagePath": "<package-path>",
  "profile": "NAFv4-ADMBw"
}
```

**Before creating associations, validate:**
1. Load `references/requirement_viewpoints.json` if not already in context
2. Check metaconstraints for the desired stereotype
3. Ensure source element stereotype matches valid `client` constraint
4. Ensure target element stereotype matches valid `supplier` constraint
5. If invalid, explain to user and suggest valid alternatives

**Example user requests:**
- "Link requirement X to requirement Y with 'derived from'"
- "Create ConformsTo relationship from my requirement to the ISO 27001 standard"
- "Requirement A conflicts with requirement B"
- "Make a 'part of catalogue' connection"

## Handling Ambiguity

When user request could map to multiple stereotypes:

1. **Identify possibilities** - Check `stereotype_mappings.md` and JSON data
2. **Present 2-4 options** - Show most likely matches with brief explanation
3. **Let user choose** - Wait for clarification before proceeding
4. **Execute** - Proceed with selected option

**Example interaction:**
```
User: "Add a requirement about security"

Claude: "I can create several types of requirements. Which would you like?

1. **FunctionalRequirement** - A functional security requirement
2. **NonfunctionalRequirement** - A non-functional security constraint
3. **RequirementCategory** - A category container for grouping security requirements

Which type fits your needs?"
```

## Natural Language Mapping

Load `references/stereotype_mappings.md` for quick lookup when user uses casual terminology:
- "functional requirement" → FunctionalRequirement
- "belongs to" → PartOfCatalogue or PartOfCategory
- "derived from" → DerivedFrom
- "conforms to standard" → ConformsTo

For detailed metamodel constraints, properties, and valid connections, reference `references/requirement_viewpoints.json`.

## Progressive Data Loading

**Always in context:** Core workflow and mapping principles (this SKILL.md file)

**Load on demand:**
- `references/stereotype_mappings.md` - When mapping user's natural language to formal stereotypes
- `references/requirement_viewpoints.json` - When validating metaconstraints, checking detailed properties, or resolving complex associations

This keeps responses efficient while ensuring access to complete metamodel data when needed.

## Common Patterns

### Pattern: Create R2 Diagram with Initial Structure
```
User: "Create R2 diagram with a catalogue and some categories"

Actions:
1. Create R2 diagram using create_or_update_diagram
2. Create RequirementCatalogue element (type: Class)
3. Create 2-3 RequirementCategory elements (type: Class)
4. Create PartOfCatalogue connectors (type: Aggregation) from categories to catalogue
5. Use place_element_on_diagram to add all elements to the diagram
6. Optional: Use layout_diagram for automatic arrangement
```

### Pattern: Add Requirement with Auto-naming
```
User: "Add functional requirement: System shall provide the operator with the option to verify that the system has saved the new software settings."

Actions:
1. Extract key concepts: verify, system, saved, settings
2. Generate concise name: "VerifySettingsSaved" or "FR-VerifySettings"
3. Create element using create_or_update_element:
   {
     "name": "VerifySettingsSaved",
     "type": "Requirement",
     "stereotype": "FunctionalRequirement",
     "notes": "System shall provide the operator with the option to verify that the system has saved the new software settings.",
     "profile": "NAFv4-ADMBw",
     "packagePath": "<current-package>"
   }
```

### Pattern: Create Traced Relationship
```
User: "Requirement X is derived from Document Y"

Actions:
1. Verify both elements exist using find_elements_by_name
2. Load requirement_viewpoints.json to check DerivedFrom metaconstraints
3. Validate: X should be FunctionalRequirement or NonfunctionalRequirement (client)
4. Validate: Y should be Reference, DocumentReference, or SMEReference (supplier)
5. Create connector using create_or_update_connector:
   {
     "sourceElementName": "X",
     "targetElementName": "Y",
     "connectorType": "Dependency",
     "stereotype": "DerivedFrom",
     "profile": "NAFv4-ADMBw"
   }
```

## Error Handling

### Element Not Found
- Use MCP `find_elements_by_name` to search for element
- If multiple matches, present list and ask user to clarify (by GUID or package path)
- If none found, offer to create the element
- Ask for element details if creation is needed

### Invalid Connection Attempt
- Load `requirement_viewpoints.json` and check metaconstraints
- Explain why the connection is invalid (stereotype mismatch)
- Look up valid alternatives from the same viewpoint
- Suggest correct stereotypes for both source and target

### Ambiguous Viewpoint Context
- If user says "add requirement" without viewpoint context, check current open diagram
- If no diagram context available, ask which viewpoint (R2-R6) they're working in
- Default to R2 for basic requirement cataloguing if user is unsure
- Explain briefly what each viewpoint is for

### Missing Package Path
- If package path not specified, check current package using get_current_package
- If no current package, ask user where to create element
- Suggest logical locations like "Model/Requirements" or similar

## Tips for Effective Usage

- **Be specific about viewpoints** - "Create R5 diagram" is clearer than generic "requirements diagram"
- **Use natural language freely** - "Conflicts with" works as well as formal "ConflictsWith"
- **Provide context when possible** - Mentioning parent elements or current diagram helps placement
- **Combine operations** - "Create R2 with catalogue and 3 categories" is efficient and clear
- **Trust auto-naming** - For requirements with long descriptions, let the skill generate concise names
- **Validate before complex operations** - For critical models, ask skill to verify connections first

## Reference Files

This skill includes two reference files for progressive data loading:

- **references/stereotype_mappings.md** - Quick reference for stereotype lookup and natural language → formal term mapping
- **references/requirement_viewpoints.json** - Complete NAF v4 Requirements metamodel extracted from MDG with all stereotypes, properties, metaconstraints, and toolbox definitions
