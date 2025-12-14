---
name: nafv4-architecture-metadata
description: Create and manage NAF v4 (NATO Architecture Framework) / ADMBw Architecture Foundation/Metadata Viewpoints (A1-A8, Ar) in Sparx Enterprise Architect. Use when the user wants to create A1 (Meta-Data Definitions), A2 (Architecture Products), A3 (Architecture Correspondence), A4 (Methodology Used), A5 (Architecture Status), A6 (Architecture Version), A7 (Architecture Compliance), A8 (Standards), or Ar (Architecture Roadmap) diagrams, add architecture metadata elements, create associations between architecture descriptions, or work with NAF architecture foundation modeling. Also triggers on natural language like "architectural description", "view", "viewpoint", "concern", "standard", "protocol", "architecture correspondence", etc.
---

# NAF v4 Architecture Metadata Modeling for Sparx Enterprise Architect

## Overview

This skill enables natural language interaction with Sparx Enterprise Architect's MCP server to create NAF v4 / ADMBw compliant Architecture Foundation/Metadata Viewpoints. It translates informal user requests into precise MCP tool calls with correct stereotypes, UML types, and profiles.

## Core Workflow

When the user requests NAF architecture metadata modeling:

1. **Parse the request** - Identify what the user wants (diagram, element, or association)
2. **Map to NAF metamodel** - Translate natural language to formal stereotypes using references
3. **Execute MCP calls** - Create or update models in Sparx EA
4. **Confirm and offer next steps** - Show what was created and suggest related actions

## Key Principles

- **Interpret flexibly** - Accept natural language like "add an architectural description" or "create viewpoint link"
- **Map precisely** - Always use exact stereotypes and UML types from the metamodel
- **Auto-name when needed** - If user provides description but no name, generate concise technical name
- **Validate connections** - Check metaconstraints before creating associations (see JSON data)
- **Ask when ambiguous** - Offer options if request could map to multiple stereotypes

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

## Supported Viewpoints

| Viewpoint | ID | Purpose | Common Requests |
|-----------|----|---------|-----------------|
| Meta-Data Definitions | A1 | Define meta-data tags for searching and discovery | "Create A1 diagram", "Add classification" |
| Architecture Products | A2 | Specify architecture structure and products | "Add view", "Create viewpoint", "Link concern" |
| Architecture Correspondence | A3 | Define relations between architecture descriptions | "Link architectures", "Create reference" |
| Methodology Used | A4 | Specify methodology for architecting activities | "Document methodology", "Add metadata" |
| Architecture Status | A5 | Track version numbers and approval status | "Track status", "Add milestone" |
| Architecture Version | A6 | Show complete architecture history | "Show version history", "Link versions" |
| Architecture Compliance | A7 | Specify architecture meta-data compliance | "Add compliance info", "Create same-as link" |
| Standards | A8 | Define technical and non-technical standards | "Add standard", "Create protocol", "Protocol stack" |
| Architecture Roadmap | Ar | Show architecture project history and future | "Create roadmap", "Show sequence" |

## Creating Diagrams

To create a NAF architecture metadata diagram, use the MCP `create_or_update_diagram` tool:

```javascript
{
  "name": "<diagram-name>",
  "type": "Custom",  // NAF diagrams are always Custom type
  "stereotype": "<viewpoint-identifier>",  // e.g. "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "Ar"
  "packagePath": "<package-path>",  // e.g. "Model/Architecture"
  "extendedProperties": {
    "alias": "<full-viewpoint-name>",  // e.g. "A1 - Meta-Data Definitions"
    "diagramID": "<viewpoint-id>",     // e.g. "A1"
    "toolbox": "<toolbox-name>"        // e.g. "NAFv4-ADMBw-A1-Toolbox"
  }
}
```

**Example user requests:**
- "Create an A1 diagram called 'System Metadata'"
- "Make a new Architecture Products view"
- "I need an A8 diagram for standards documentation"

## Creating Elements

To create a NAF architecture metadata element, use the MCP `create_or_update_element` tool:

```javascript
{
  "name": "<element-name>",
  "type": "<uml-type>",           // e.g. "Package", "Class", "Object", "Note", "Part"
  "stereotype": "<NAF-stereotype>", // e.g. "ArchitecturalDescription", "View", "Viewpoint"
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
- Example: "Architecture for C2 system" → "C2ArchitectureDescription" or "AD-C2System"

**Example user requests:**
- "Add architectural description for 'System XYZ Architecture'"
- "Create a View named 'Operational View'"
- "Add Viewpoint element for stakeholder concerns"
- "Add standard for ISO 42010"
- "Create protocol stack for TCP/IP"

## Creating Associations

To create connections between elements, use the MCP `create_or_update_connector` tool:

```javascript
{
  "sourceElementName": "<source-element>",
  "targetElementName": "<target-element>",
  "connectorType": "<uml-connector-type>",  // e.g. "Dependency", "Realization"
  "stereotype": "<NAF-stereotype>",          // e.g. "DescribedBy", "CompliesViewpoint"
  "packagePath": "<package-path>",
  "profile": "NAFv4-ADMBw"
}
```

**Before creating associations, validate:**
1. Load `references/architecture_metadata_viewpoints.json` if not already in context
2. Check metaconstraints for the desired stereotype
3. Ensure source element stereotype matches valid `client` constraint
4. Ensure target element stereotype matches valid `supplier` constraint
5. If invalid, explain to user and suggest valid alternatives

**Example user requests:**
- "Link view X to viewpoint Y with 'complies with'"
- "Create DescribedBy relationship from architecture description to architecture"
- "Architecture A is successor of Architecture B"
- "Mark element X as same as element Y"

## Handling Ambiguity

When user request could map to multiple stereotypes:

1. **Identify possibilities** - Check `stereotype_mappings.md` and JSON data
2. **Present 2-4 options** - Show most likely matches with brief explanation
3. **Let user choose** - Wait for clarification before proceeding
4. **Execute** - Proceed with selected option

**Example interaction:**
```
User: "Add a stakeholder element"

Claude: "I can create several types of stakeholder elements. Which would you like?

1. **ActualOrganization** - A specific organization instance
2. **ActualPerson** - An individual human being
3. **ActualPost** - A specific post/role instance
4. **Organization** - An organization type/template
5. **Person** - A person type/template
6. **Post** - A post/role type/template

Which type fits your needs?"
```

## Natural Language Mapping

Load `references/stereotype_mappings.md` for quick lookup when user uses casual terminology:
- "architectural description" → ArchitecturalDescription
- "view" → View
- "viewpoint" → Viewpoint
- "concern" → Concern
- "complies with viewpoint" → CompliesViewpoint
- "successor of" → ArchitecturalSequence

For detailed metamodel constraints, properties, and valid connections, reference `references/architecture_metadata_viewpoints.json`.

## Progressive Data Loading

**Always in context:** Core workflow and mapping principles (this SKILL.md file)

**Load on demand:**
- `references/stereotype_mappings.md` - When mapping user's natural language to formal stereotypes
- `references/architecture_metadata_viewpoints.json` - When validating metaconstraints, checking detailed properties, or resolving complex associations

This keeps responses efficient while ensuring access to complete metamodel data when needed.

## Common Patterns

### Pattern: Create A2 Diagram with Views and Viewpoints
```
User: "Create A2 diagram with viewpoints and concerns"

Actions:
1. Create A2 diagram using create_or_update_diagram
2. Create ArchitecturalDescription element (type: Package)
3. Create 2-3 Viewpoint elements (type: Class)
4. Create 2-3 Concern elements (type: Class)
5. Create ConcernForViewpoint connectors (type: Dependency)
6. Use place_element_on_diagram to add all elements to the diagram
7. Optional: Use layout_diagram for automatic arrangement
```

### Pattern: Add Architecture Description with Auto-naming
```
User: "Add architectural description: System architecture for the command and control system."

Actions:
1. Extract key concepts: command, control, system
2. Generate concise name: "C2SystemArchitecture" or "AD-C2System"
3. Create element using create_or_update_element:
   {
     "name": "C2SystemArchitecture",
     "type": "Package",
     "stereotype": "ArchitecturalDescription",
     "notes": "System architecture for the command and control system.",
     "profile": "NAFv4-ADMBw",
     "packagePath": "<current-package>"
   }
```

### Pattern: Create View-Viewpoint Relationship
```
User: "View X complies with Viewpoint Y"

Actions:
1. Verify both elements exist using find_elements_by_name
2. Load architecture_metadata_viewpoints.json to check CompliesViewpoint metaconstraints
3. Validate: X should be View (client)
4. Validate: Y should be Viewpoint (supplier)
5. Create connector using create_or_update_connector:
   {
     "sourceElementName": "X",
     "targetElementName": "Y",
     "connectorType": "Dependency",
     "stereotype": "CompliesViewpoint",
     "profile": "NAFv4-ADMBw"
   }
```

### Pattern: Create Protocol Stack (A8)
```
User: "Create TCP/IP protocol stack"

Actions:
1. Create Protocolstack element named "TCP/IP Stack" (type: Class)
2. Create Protocol elements for each layer (e.g., "TCP", "IP", "Ethernet")
3. Create ProtocolLayer elements (type: Part) to define the stack composition
4. Link ProtocolLayers to the Protocolstack using appropriate relationships
5. Add all elements to the A8 diagram
```

## Error Handling

### Element Not Found
- Use MCP `find_elements_by_name` to search for element
- If multiple matches, present list and ask user to clarify (by GUID or package path)
- If none found, offer to create the element
- Ask for element details if creation is needed

### Invalid Connection Attempt
- Load `architecture_metadata_viewpoints.json` and check metaconstraints
- Explain why the connection is invalid (stereotype mismatch)
- Look up valid alternatives from the same viewpoint
- Suggest correct stereotypes for both source and target

### Ambiguous Viewpoint Context
- If user says "add view" without viewpoint context, check current open diagram
- If no diagram context available, ask which viewpoint (A1-A8, Ar) they're working in
- Default to A2 for views and viewpoints if user is unsure
- Explain briefly what each viewpoint is for

### Missing Package Path
- If package path not specified, check current package using get_current_package
- If no current package, ask user where to create element
- Suggest logical locations like "Model/Architecture" or similar

## Tips for Effective Usage

- **Be specific about viewpoints** - "Create A2 diagram" is clearer than generic "architecture diagram"
- **Use natural language freely** - "successor of" works as well as formal "ArchitecturalSequence"
- **Provide context when possible** - Mentioning parent elements or current diagram helps placement
- **Combine operations** - "Create A2 with viewpoints and concerns" is efficient and clear
- **Trust auto-naming** - For descriptions with long text, let the skill generate concise names
- **Validate before complex operations** - For critical models, ask skill to verify connections first

## Reference Files

This skill includes two reference files for progressive data loading:

- **references/stereotype_mappings.md** - Quick reference for stereotype lookup and natural language → formal term mapping
- **references/architecture_metadata_viewpoints.json** - Complete NAF v4 Architecture Metadata metamodel extracted from MDG with all stereotypes, properties, metaconstraints, and toolbox definitions
