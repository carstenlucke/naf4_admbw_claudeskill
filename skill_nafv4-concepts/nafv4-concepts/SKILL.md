---
name: nafv4-concepts
description: Create and manage NAF v4 (NATO Architecture Framework) / ADMBw Concepts Viewpoints (C1-C8, Cr) in Sparx Enterprise Architect. Use when the user wants to create C1 (Capability Taxonomy), C2 (Enterprise Vision), C3 (Capability Dependencies), C4 (Standard Processes), C5 (Effects), C7 (Performance Parameters), C8 (Planning Assumptions), or Cr (Capability Roadmap) diagrams, add capability elements, create associations between capabilities, enterprises, activities, or work with NAF concepts modeling. Also triggers on natural language like "capability", "enterprise vision", "enduring task", "desired effect", "measure of effectiveness", etc.
---

# NAF v4 Concepts Modeling for Sparx Enterprise Architect

## Overview

This skill enables natural language interaction with Sparx Enterprise Architect's MCP server to create NAF v4 / ADMBw compliant Concepts Viewpoints. It translates informal user requests into precise MCP tool calls with correct stereotypes, UML types, and profiles.

## Core Workflow

When the user requests NAF concepts modeling:

1. **Parse the request** - Identify what the user wants (diagram, element, or association)
2. **Map to NAF metamodel** - Translate natural language to formal stereotypes using references
3. **Execute MCP calls** - Create or update models in Sparx EA
4. **Confirm and offer next steps** - Show what was created and suggest related actions

## Key Principles

- **Interpret flexibly** - Accept natural language like "add a capability" or "create enterprise vision"
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

### 3. Automatic Diagram Layout

Never apply automatic diagram layout operations:
- **Do not use** `layout_diagram` or similar automatic layout functions
- **Manual layout only** - Let the user arrange elements manually in Sparx EA
- Elements should be placed on diagrams using `place_element_on_diagram`, but their visual arrangement is left to the user
- The user controls the visual organization of their diagrams

## Supported Viewpoints

| Viewpoint | ID | Purpose | Common Requests |
|-----------|----|---------|-----------------|
| Capability Taxonomy | C1 | Organize capabilities in taxonomies | "Create C1 diagram", "Add capability with MoE" |
| Enterprise Vision | C2 | Strategic context for capabilities | "Show enterprise vision", "Add enterprise goal" |
| Capability Dependencies | C3 | Show capability dependencies | "Show dependencies", "X depends on Y" |
| Standard Processes | C4 | Specify standard operational activities | "Add standard process", "Map to capability" |
| Effects | C5 | Describe operational effects | "Show desired effect", "Add achieved effect" |
| Performance Parameters | C7 | Express capability requirements with MoEs | "Add performance parameter", "Define measure" |
| Planning Assumptions | C8 | Document assumptions for implementation | "Add planning assumption", "Strategic constraint" |
| Capability Roadmap | Cr | Identify capability gaps and roadmap | "Create roadmap", "Add project milestone" |

## Creating Diagrams

To create a NAF concepts diagram, use the MCP `create_or_update_diagram` tool:

```javascript
{
  "name": "<diagram-name>",
  "type": "Custom",  // NAF diagrams are always Custom type
  "stereotype": "<viewpoint-identifier>",  // e.g. "C1", "C2", "C3", "C4", "C5", "C7", "C8", "Cr"
  "packagePath": "<package-path>",  // e.g. "Model/Concepts"
  "extendedProperties": {
    "alias": "<full-viewpoint-name>",  // e.g. "C1 - Capability Taxonomy"
    "diagramID": "<viewpoint-id>",     // e.g. "C1"
    "toolbox": "<toolbox-name>"        // e.g. "NAFv4-ADMBw-C1-Toolbox"
  }
}
```

**Example user requests:**
- "Create a C1 diagram called 'System Capabilities'"
- "Make a new Enterprise Vision view"
- "I need a C5 diagram for effects analysis"

## Creating Elements

To create a NAF concept element, use the MCP `create_or_update_element` tool:

```javascript
{
  "name": "<element-name>",
  "type": "<uml-type>",           // e.g. "Class", "Activity", "Object", "Part"
  "stereotype": "<NAF-stereotype>", // e.g. "Capability", "EnterpriseVision"
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
- Example: "Ability to provide air support" → "AirSupportCapability" or "CAP-AirSupport"

**Example user requests:**
- "Add capability 'Air Support Operations'"
- "Create an EnterpriseVision named 'Future State 2030'"
- "Add standard operational activity for logistics planning"
- "Add capability with description: The enterprise's ability to provide coordinated air support to ground forces in contested environments"

## Creating Associations

To create connections between elements, use the MCP `create_or_update_connector` tool:

```javascript
{
  "sourceElementName": "<source-element>",
  "targetElementName": "<target-element>",
  "connectorType": "<uml-connector-type>",  // e.g. "Dependency", "Abstraction", "Generalization"
  "stereotype": "<NAF-stereotype>",          // e.g. "CapabilityDependency", "Exhibits"
  "packagePath": "<package-path>",
  "profile": "NAFv4-ADMBw"
}
```

**Before creating associations, validate:**
1. Load `references/concept_viewpoints.json` if not already in context
2. Check metaconstraints for the desired stereotype
3. Ensure source element stereotype matches valid `client` constraint
4. Ensure target element stereotype matches valid `supplier` constraint
5. If invalid, explain to user and suggest valid alternatives

**Example user requests:**
- "Capability X depends on capability Y"
- "Create 'exhibits' relationship from configuration to capability"
- "Show that this activity maps to the capability"
- "Create capability generalization hierarchy"

## Handling Ambiguity

When user request could map to multiple stereotypes:

1. **Identify possibilities** - Check `stereotype_mappings.md` and JSON data
2. **Present 2-4 options** - Show most likely matches with brief explanation
3. **Let user choose** - Wait for clarification before proceeding
4. **Execute** - Proceed with selected option

**Example interaction:**
```
User: "Add a constraint about security"

Claude: "I can create several types of constraints. Which would you like?

1. **StrategicConstraint** - A rule governing a capability at strategic level
2. **OperationalConstraint** - A rule governing logical architectural elements
3. **ResourceConstraint** - A rule governing structural/functional implementation aspects

Which type fits your needs?"
```

## Natural Language Mapping

Load `references/stereotype_mappings.md` for quick lookup when user uses casual terminology:
- "capability" → Capability
- "enterprise vision" → EnterpriseVision
- "enduring task" → EnduringTask
- "depends on" → CapabilityDependency
- "measure of effectiveness" → MeasurementType

For detailed metamodel constraints, properties, and valid connections, reference `references/concept_viewpoints.json`.

## Progressive Data Loading

**Always in context:** Core workflow and mapping principles (this SKILL.md file)

**Load on demand:**
- `references/stereotype_mappings.md` - When mapping user's natural language to formal stereotypes
- `references/concept_viewpoints.json` - When validating metaconstraints, checking detailed properties, or resolving complex associations

This keeps responses efficient while ensuring access to complete metamodel data when needed.

## Common Patterns

### Pattern: Create C1 Diagram with Capability Taxonomy
```
User: "Create C1 diagram with capability hierarchy"

Actions:
1. Create C1 diagram using create_or_update_diagram
2. Create parent Capability element (type: Class)
3. Create 2-3 child Capability elements (type: Class)
4. Create CapabilityGeneralization connectors (type: Generalization) from child to parent
5. Use place_element_on_diagram to add all elements to the diagram
6. Optional: Use layout_diagram for automatic arrangement
```

### Pattern: Add Capability with Auto-naming
```
User: "Add capability: The enterprise's ability to provide coordinated air support to ground forces in contested environments."

Actions:
1. Extract key concepts: air support, ground forces, coordinated
2. Generate concise name: "AirSupportCapability" or "CAP-AirSupport"
3. Create element using create_or_update_element:
   {
     "name": "AirSupportCapability",
     "type": "Class",
     "stereotype": "Capability",
     "notes": "The enterprise's ability to provide coordinated air support to ground forces in contested environments.",
     "profile": "NAFv4-ADMBw",
     "packagePath": "<current-package>"
   }
```

### Pattern: Create C2 Enterprise Vision
```
User: "Create enterprise vision for digital transformation"

Actions:
1. Create C2 diagram using create_or_update_diagram
2. Create EnterpriseVision element (type: Class) with name "DigitalTransformation2030"
3. Create 2-3 EnterpriseGoal elements (type: Class)
4. Create AlignsWithGoal connectors (type: Dependency) from goals to vision
5. Create Capability elements that support the vision
6. Place all elements on diagram
```

### Pattern: Create Capability Dependency
```
User: "Capability X depends on Capability Y"

Actions:
1. Verify both elements exist using find_elements_by_name
2. Load concept_viewpoints.json to check CapabilityDependency metaconstraints
3. Validate: X should be Capability (client)
4. Validate: Y should be Capability (supplier)
5. Create connector using create_or_update_connector:
   {
     "sourceElementName": "X",
     "targetElementName": "Y",
     "connectorType": "Dependency",
     "stereotype": "CapabilityDependency",
     "profile": "NAFv4-ADMBw"
   }
```

### Pattern: Create C5 Effects Diagram
```
User: "Show desired and achieved effects for capability"

Actions:
1. Create C5 diagram using create_or_update_diagram
2. Create Capability element (desirer)
3. Create ActualState elements for desired effects (e.g., ActualMeasurementSet)
4. Create CapabilityConfiguration or ActualResource elements (achievers)
5. Create DesiredEffect connectors (type: Dependency) from capability to actual states
6. Create AchievedEffect connectors (type: Dependency) from achievers to actual states
7. Optional: Create RealizedDesiredEffect to link achieved to desired
```

### Pattern: Create Cr Capability Roadmap
```
User: "Create capability roadmap with project milestones"

Actions:
1. Create Cr diagram using create_or_update_diagram
2. Create Capability elements
3. Create FieldedCapability or CapabilityConfiguration elements
4. Create ActualProject elements
5. Create ActualProjectMilestone elements
6. Create Exhibits connectors (type: Abstraction) from configurations to capabilities
7. Create OwnedMilestone connectors (type: Dependency) from projects to milestones
8. Create MilestoneDependency connectors (type: Dependency) between milestones
9. Optional: Create VersionReleased/VersionWithdrawn for capability increments
```

## Error Handling

### Element Not Found
- Use MCP `find_elements_by_name` to search for element
- If multiple matches, present list and ask user to clarify (by GUID or package path)
- If none found, offer to create the element
- Ask for element details if creation is needed

### Invalid Connection Attempt
- Load `concept_viewpoints.json` and check metaconstraints
- Explain why the connection is invalid (stereotype mismatch)
- Look up valid alternatives from the same viewpoint
- Suggest correct stereotypes for both source and target

### Ambiguous Viewpoint Context
- If user says "add capability" without viewpoint context, check current open diagram
- If no diagram context available, ask which viewpoint (C1-C8, Cr) they're working in
- Default to C1 for basic capability taxonomy if user is unsure
- Explain briefly what each viewpoint is for

### Missing Package Path
- If package path not specified, check current package using get_current_package
- If no current package, ask user where to create element
- Suggest logical locations like "Model/Concepts" or similar

## Tips for Effective Usage

- **Be specific about viewpoints** - "Create C1 diagram" is clearer than generic "capability diagram"
- **Use natural language freely** - "Depends on" works as well as formal "CapabilityDependency"
- **Provide context when possible** - Mentioning parent elements or current diagram helps placement
- **Combine operations** - "Create C2 with vision and 3 goals" is efficient and clear
- **Trust auto-naming** - For capabilities with long descriptions, let the skill generate concise names
- **Validate before complex operations** - For critical models, ask skill to verify connections first

## Reference Files

This skill includes two reference files for progressive data loading:

- **references/stereotype_mappings.md** - Quick reference for stereotype lookup and natural language → formal term mapping
- **references/concept_viewpoints.json** - Complete NAF v4 Concepts metamodel extracted from MDG with all stereotypes, properties, metaconstraints, and toolbox definitions
