---
name: nafv4-physical-resources
description: Create and manage NAF v4 (NATO Architecture Framework) / ADMBw Physical Resource Specification Viewpoints (P1-P8, Pr) in Sparx Enterprise Architect. Use when the user wants to create P1 (Resource Types), P2 (Resource Structure), P3 (Resource Connectivity), P4 (Resource Functions), P5 (Resource States), P6 (Resource Sequence), P7 (Data Model), P8 (Resource Constraints), or Pr (Configuration Management) diagrams, add resource elements, create associations between resources, or work with NAF physical architecture modeling. Also triggers on natural language like "system", "resource type", "function", "interface", "protocol", "state machine", etc.
---

# NAF v4 Physical Resources Modeling for Sparx Enterprise Architect

## Overview

This skill enables natural language interaction with Sparx Enterprise Architect's MCP server to create NAF v4 / ADMBw compliant Physical Resource Specification Viewpoints. It translates informal user requests into precise MCP tool calls with correct stereotypes, UML types, and profiles.

## Core Workflow

When the user requests NAF physical resources modeling:

1. **Parse the request** - Identify what the user wants (diagram, element, or association)
2. **Map to NAF metamodel** - Translate natural language to formal stereotypes using references
3. **Execute MCP calls** - Create or update models in Sparx EA
4. **Confirm and offer next steps** - Show what was created and suggest related actions

## Key Principles

- **Interpret flexibly** - Accept natural language like "add a system" or "create resource exchange"
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
| Resource Types | P1 | Catalog resource types with performance characteristics | "Create P1 diagram", "Add system", "Add technology" |
| Resource Structure | P2 | Show resource structure realizing logical architecture | "Show resource structure", "Add capability configuration" |
| Resource Connectivity | P3 | Document networks and physical pathways | "Show connectivity", "Add resource port", "Add protocol" |
| Resource Functions | P4 | Detail function allocation to resources | "Map functions", "Add function action" |
| Resource States | P5 | Identify states and transitions | "Show states", "Add state machine" |
| Resource Sequence | P6 | Define sequence of functions and interactions | "Create sequence", "Add resource message" |
| Data Model | P7 | Describe physical data implementation | "Create data model", "Add data element" |
| Resource Constraints | P8 | Document constraints on resources | "Add constraint", "Show resource constraints" |
| Configuration Management | Pr | Track resource changes over time | "Show configuration", "Add version", "Add milestone" |

## Creating Diagrams

To create a NAF physical resources diagram, use the MCP `create_or_update_diagram` tool:

```javascript
{
  "name": "<diagram-name>",
  "type": "Custom",  // NAF diagrams are Custom (except P6 which is Sequence)
  "stereotype": "<viewpoint-identifier>",  // e.g. "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "Pr"
  "packagePath": "<package-path>",  // e.g. "Model/Physical Resources"
  "extendedProperties": {
    "alias": "<full-viewpoint-name>",  // e.g. "P1 - Resource Types"
    "diagramID": "<viewpoint-id>",     // e.g. "P1"
    "toolbox": "<toolbox-name>"        // e.g. "NAFv4-ADMBw-P1-Toolbox"
  }
}
```

**Note:** P6 - Resource Sequence uses `"type": "Sequence"` instead of "Custom".

**Example user requests:**
- "Create a P1 diagram called 'System Resource Types'"
- "Make a new Resource Structure view"
- "I need a P4 diagram for function mapping"
- "Create a P6 sequence diagram"

## Creating Elements

To create a NAF physical resource element, use the MCP `create_or_update_element` tool:

```javascript
{
  "name": "<element-name>",
  "type": "<uml-type>",           // e.g. "Class", "Activity", "Part", "Port", "Object"
  "stereotype": "<NAF-stereotype>", // e.g. "System", "Function", "ResourcePort"
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
- Example: "Radar system for air surveillance" → "RadarAirSurveillance" or "P1-RadarSystem"

**Example user requests:**
- "Add system 'Command and Control System'"
- "Create a ResourceInterface named 'DataBusInterface'"
- "Add Function for 'Process Sensor Data'"
- "Add software component with description: Real-time operating system managing sensor data processing and communication protocols"

## Creating Associations

To create connections between elements, use the MCP `create_or_update_connector` tool:

```javascript
{
  "sourceElementName": "<source-element>",
  "targetElementName": "<target-element>",
  "connectorType": "<uml-connector-type>",  // e.g. "InformationFlow", "Dependency", "Abstraction"
  "stereotype": "<NAF-stereotype>",          // e.g. "ResourceExchange", "Implements", "HostedOn"
  "packagePath": "<package-path>",
  "profile": "NAFv4-ADMBw"
}
```

**Before creating associations, validate:**
1. Load `references/physical_resource_specification_viewpoints.json` if not already in context
2. Check metaconstraints for the desired stereotype
3. Ensure source element stereotype matches valid `client` constraint
4. Ensure target element stereotype matches valid `supplier` constraint
5. If invalid, explain to user and suggest valid alternatives

**Example user requests:**
- "Create resource exchange from System A to System B"
- "Show that Software X is hosted on System Y"
- "Link Function to the System that performs it"
- "Create implements relationship from System to Service"

## Handling Ambiguity

When user request could map to multiple stereotypes:

1. **Identify possibilities** - Check `stereotype_mappings.md` and JSON data
2. **Present 2-4 options** - Show most likely matches with brief explanation
3. **Let user choose** - Wait for clarification before proceeding
4. **Execute** - Proceed with selected option

**Example interaction:**
```
User: "Add a resource for processing data"

Claude: "I can create several types of resources. Which would you like?

1. **System** - An integrated set of elements accomplishing a defined objective
2. **Software** - An executable computer program for data processing
3. **Function** - An activity performed by a resource

Which type fits your needs?"
```

## Natural Language Mapping

Load `references/stereotype_mappings.md` for quick lookup when user uses casual terminology:
- "system" → System
- "resource type" → ResourceArtifact, System, or Software
- "function" → Function
- "interface" → ResourceInterface
- "flows to" → ResourceExchange
- "hosted on" → HostedOn
- "implements" → Implements

For detailed metamodel constraints, properties, and valid connections, reference `references/physical_resource_specification_viewpoints.json`.

## Progressive Data Loading

**Always in context:** Core workflow and mapping principles (this SKILL.md file)

**Load on demand:**
- `references/stereotype_mappings.md` - When mapping user's natural language to formal stereotypes
- `references/physical_resource_specification_viewpoints.json` - When validating metaconstraints, checking detailed properties, or resolving complex associations

This keeps responses efficient while ensuring access to complete metamodel data when needed.

## Common Patterns

### Pattern: Create P1 Diagram with System Types
```
User: "Create P1 diagram with several system types"

Actions:
1. Create P1 diagram using create_or_update_diagram
2. Create System elements (type: Class) for different system types
3. Optional: Add Technology elements to show technology domains
4. Optional: Add Measurement elements for performance characteristics
5. Use place_element_on_diagram to add all elements to the diagram
6. Optional: Use layout_diagram for automatic arrangement
```

### Pattern: Create P2 Resource Structure
```
User: "Show how System X is composed of subsystems A, B, and C"

Actions:
1. Create or find P2 diagram
2. Create System element for "System X" (type: Class)
3. Create ResourceRole elements for subsystems A, B, C (type: Part)
4. Create composition relationships from System X to each ResourceRole
5. Optional: Add ResourceExchange flows between subsystems
6. Place elements on diagram and arrange
```

### Pattern: Create P3 Connectivity with Interfaces
```
User: "Show connectivity between System A and System B via data bus"

Actions:
1. Create or find P3 diagram
2. Create System elements for A and B if not exist
3. Create ResourcePort elements for each system (type: Port)
4. Create ResourceInterface element for "DataBusInterface" (type: Class)
5. Create ResourceConnector between ports (type: Connector)
6. Optional: Add Protocol element showing communication protocol
7. Use ImplementsProtocol to link connector to protocol
8. Place and arrange on diagram
```

### Pattern: Create P4 Function Mapping
```
User: "Map function 'Process Data' to System X"

Actions:
1. Create or find P4 diagram
2. Create Function element "ProcessData" (type: Activity) if not exist
3. Create or find System element
4. Create IsCapableToPerform relationship (type: Abstraction):
   - Source: System
   - Target: Function
5. Optional: Create FunctionAction elements (type: Action) to show function calls
6. Optional: Add FunctionControlFlow and FunctionObjectFlow between actions
7. Place and arrange on diagram
```

### Pattern: Create P5 State Machine
```
User: "Show states for System X: Idle, Active, Maintenance"

Actions:
1. Create or find P5 diagram
2. Create ResourceStateDescription element (type: StateMachine)
3. Add states within the state machine: Idle, Active, Maintenance
4. Add transitions between states with triggers/events
5. Associate state machine with System X
6. Place on diagram
```

### Pattern: Create P6 Sequence Diagram
```
User: "Show sequence of interactions between Systems A, B, and C"

Actions:
1. Create P6 diagram using type: "Sequence"
2. Create ResourceRole elements for each system (type: Part)
3. Add lifelines for each ResourceRole
4. Create ResourceMessage elements (type: Message) showing exchanges
5. Order messages in sequence
6. Optional: Add timing constraints or conditions
```

### Pattern: Create P7 Data Model
```
User: "Show data structure for sensor data"

Actions:
1. Create or find P7 diagram
2. Create DataModel package if needed (type: Package)
3. Create DataElement elements (type: Class) for data entities
4. Create relationships between DataElements (associations, compositions)
5. Optional: Add DataRole elements (type: Part) for data usage
6. Optional: Show Implements relationships to logical data model
7. Place and arrange on diagram
```

### Pattern: Create P8 with Constraints
```
User: "Document constraint that System X must comply with security standard Y"

Actions:
1. Create or find P8 diagram
2. Create ResourceConstraint element describing the constraint (type: Class)
3. Create Standard element for "Security Standard Y" (type: Class) if not exist
4. Create ConformsTo relationship from ResourceConstraint to Standard
5. Create Satisfy relationship from System X to ResourceConstraint
6. Optional: Add DocumentReference for regulatory documentation
7. Place and arrange on diagram
```

### Pattern: Create Pr Configuration Management
```
User: "Show evolution of System X with versions 1.0, 2.0, and 3.0"

Actions:
1. Create Pr diagram
2. Create WholeLifeConfiguration element (type: Class)
3. Create VersionOfConfiguration elements for each version (type: Part)
4. Create VersionSuccession relationships between versions
5. Optional: Add ActualProject and ActualProjectMilestone elements
6. Optional: Link milestones to versions with VersionReleased relationships
7. Place and arrange on timeline
```

## Error Handling

### Element Not Found
- Use MCP `find_elements_by_name` to search for element
- If multiple matches, present list and ask user to clarify (by GUID or package path)
- If none found, offer to create the element
- Ask for element details if creation is needed

### Invalid Connection Attempt
- Load `physical_resource_specification_viewpoints.json` and check metaconstraints
- Explain why the connection is invalid (stereotype mismatch)
- Look up valid alternatives from the same viewpoint
- Suggest correct stereotypes for both source and target

### Ambiguous Viewpoint Context
- If user says "add system" without viewpoint context, check current open diagram
- If no diagram context available, ask which viewpoint (P1-P8, Pr) they're working in
- Default to P1 for basic resource type cataloging if user is unsure
- Explain briefly what each viewpoint is for

### Missing Package Path
- If package path not specified, check current package using get_current_package
- If no current package, ask user where to create element
- Suggest logical locations like "Model/Physical Resources" or similar

### Wrong Diagram Type for P6
- P6 is a Sequence diagram, not Custom
- If user tries to create P6 as Custom, correct to Sequence type
- Explain that P6 uses UML sequence diagram notation

## Tips for Effective Usage

- **Be specific about viewpoints** - "Create P2 diagram" is clearer than generic "resource diagram"
- **Use natural language freely** - "Flows to" works as well as formal "ResourceExchange"
- **Provide context when possible** - Mentioning parent elements or current diagram helps placement
- **Combine operations** - "Create P1 with 3 systems and their technologies" is efficient and clear
- **Trust auto-naming** - For resources with long descriptions, let the skill generate concise names
- **Validate before complex operations** - For critical models, ask skill to verify connections first
- **Remember viewpoint purposes**:
  - P1: What resources exist (types catalog)
  - P2: How resources are structured (composition)
  - P3: How resources connect (interfaces, networks)
  - P4: What resources do (functions)
  - P5: What states resources have (behavior)
  - P6: When resources interact (sequences)
  - P7: What data resources use (physical data)
  - P8: What constraints apply (rules)
  - Pr: When resources change (versions, timeline)

## Reference Files

This skill includes two reference files for progressive data loading:

- **references/stereotype_mappings.md** - Quick reference for stereotype lookup and natural language → formal term mapping
- **references/physical_resource_specification_viewpoints.json** - Complete NAF v4 Physical Resources metamodel extracted from MDG with all stereotypes, properties, metaconstraints, and toolbox definitions
