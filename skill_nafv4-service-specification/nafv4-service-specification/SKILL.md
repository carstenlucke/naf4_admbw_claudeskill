---
name: nafv4-service-specification
description: Create and manage NAF v4 (NATO Architecture Framework) / ADMBw Service Specification Viewpoints (S1-S8, Sr) in Sparx Enterprise Architect. Use when the user wants to create S1 (Service Taxonomy), S2 (Service Structure), S3 (Service Interfaces), S4 (Service Functions), S5 (Service States), S6 (Service Interactions), S7 (Service Interface Parameters), S8 (Service Policy), or Sr (Service Roadmap) diagrams, add service elements, create service interfaces, model service functions, or work with NAF service modeling. Also triggers on natural language like "service specification", "service interface", "service function", "service policy", "service taxonomy", etc.
---

# NAF v4 Service Specification Modeling for Sparx Enterprise Architect

## Overview

This skill enables natural language interaction with Sparx Enterprise Architect's MCP server to create NAF v4 / ADMBw compliant Service Specification Viewpoints. It translates informal user requests into precise MCP tool calls with correct stereotypes, UML types, and profiles.

## Core Workflow

When the user requests NAF service specification modeling:

1. **Parse the request** - Identify what the user wants (diagram, element, or association)
2. **Map to NAF metamodel** - Translate natural language to formal stereotypes using references
3. **Execute MCP calls** - Create or update models in Sparx EA
4. **Confirm and offer next steps** - Show what was created and suggest related actions

## Key Principles

- **Interpret flexibly** - Accept natural language like "add a service interface" or "create service taxonomy"
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
| Service Taxonomy | S1 | Governance structure for SOA | "Create S1 diagram", "Add service specification", "Service taxonomy" |
| Service Structure | S2 | Service composition and dependencies | "Show service structure", "Service depends on", "Add service role" |
| Service Interfaces | S3 | Service interface definitions | "Define service interface", "Add service port", "Interface contract" |
| Service Functions | S4 | Service behavioral specifications | "Add service function", "Service behavior", "Function action" |
| Service States | S5 | Service state machines | "Service states", "State transitions", "Service state machine" |
| Service Interactions | S6 | Service interaction sequences | "Service interactions", "Service messages", "Sequence diagram" |
| Service Interface Parameters | S7 | Interface compatibility specifications | "Interface parameters", "Service compatibility" |
| Service Policy | S8 | Service constraints and policies | "Service policy", "Service constraints", "Policy governance" |
| Service Roadmap | Sr | Service lifecycle and evolution | "Service roadmap", "Service timeline", "Project milestones" |

## Creating Diagrams

To create a NAF service specification diagram, use the MCP `create_or_update_diagram` tool:

```javascript
{
  "name": "<diagram-name>",
  "type": "Custom",  // NAF diagrams are Custom type (except S6 which is Sequence)
  "stereotype": "<viewpoint-identifier>",  // e.g. "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "Sr"
  "packagePath": "<package-path>",  // e.g. "Model/Services"
  "extendedProperties": {
    "alias": "<full-viewpoint-name>",  // e.g. "S1 - Service Taxonomy"
    "diagramID": "<viewpoint-id>",     // e.g. "S1"
    "toolbox": "<toolbox-name>"        // e.g. "NAFv4-ADMBw-S1-Toolbox"
  }
}
```

**Special case - S6 Service Interactions:**
- S6 uses diagram type "Sequence" instead of "Custom"
- Otherwise follows the same pattern

**Example user requests:**
- "Create an S1 diagram called 'Enterprise Service Taxonomy'"
- "Make a new Service Interfaces view"
- "I need an S4 diagram for service behavior"
- "Create S6 sequence diagram for authentication flow"

## Creating Elements

To create a NAF service element, use the MCP `create_or_update_element` tool:

```javascript
{
  "name": "<element-name>",
  "type": "<uml-type>",           // e.g. "Class", "Activity", "Port", "Object", "StateMachine"
  "stereotype": "<NAF-stereotype>", // e.g. "ServiceSpecification", "ServiceInterface"
  "packagePath": "<package-path>",
  "notes": "<description>",        // User's full description text
  "profile": "NAFv4-ADMBw"        // Always use this profile
}
```

**Auto-naming logic:**
When user provides description but no name, generate a concise technical identifier:
- Extract key concepts from description
- Use PascalCase format for services and interfaces
- Keep to 3-5 words maximum
- Example: "authentication service for user login" → "UserAuthenticationService" or "AuthService"

**Example user requests:**
- "Add service specification 'User Authentication Service'"
- "Create a ServiceInterface named 'IAuthenticationProvider'"
- "Add service function for validating credentials"
- "Create service port for external access"
- "Add service policy to enforce encryption"

## Creating Associations

To create connections between elements, use the MCP `create_or_update_connector` tool:

```javascript
{
  "sourceElementName": "<source-element>",
  "targetElementName": "<target-element>",
  "connectorType": "<uml-connector-type>",  // e.g. "Dependency", "Generalization", "Abstraction"
  "stereotype": "<NAF-stereotype>",          // e.g. "ServiceDependency", "ServiceClassification"
  "packagePath": "<package-path>",
  "profile": "NAFv4-ADMBw"
}
```

**Before creating associations, validate:**
1. Load `references/service_specification_viewpoints.json` if not already in context
2. Check metaconstraints for the desired stereotype
3. Ensure source element stereotype matches valid `client` constraint
4. Ensure target element stereotype matches valid `supplier` constraint
5. If invalid, explain to user and suggest valid alternatives

**Example user requests:**
- "Service X depends on Service Y"
- "Create generalization from BaseService to SpecializedService"
- "Link service to implementing function"
- "Service interface provides authentication function"
- "Project milestone releases new service version"

## Handling Ambiguity

When user request could map to multiple stereotypes:

1. **Identify possibilities** - Check `stereotype_mappings.md` and JSON data
2. **Present 2-4 options** - Show most likely matches with brief explanation
3. **Let user choose** - Wait for clarification before proceeding
4. **Execute** - Proceed with selected option

**Example interaction:**
```
User: "Add a service element"

Claude: "I can create several types of service elements. Which would you like?

1. **ServiceSpecification** - The specification of service functionality
2. **ServiceInterface** - A contract defining service methods
3. **ServiceFunction** - A behavioral function of a service
4. **ServicePolicy** - A constraint governing service use

Which type fits your needs?"
```

## Natural Language Mapping

Load `references/stereotype_mappings.md` for quick lookup when user uses casual terminology:
- "service" → ServiceSpecification
- "interface" → ServiceInterface
- "function" → ServiceFunction
- "policy" → ServicePolicy
- "depends on" → ServiceDependency
- "provides function" → ProvidesServiceFunction

For detailed metamodel constraints, properties, and valid connections, reference `references/service_specification_viewpoints.json`.

## Progressive Data Loading

**Always in context:** Core workflow and mapping principles (this SKILL.md file)

**Load on demand:**
- `references/stereotype_mappings.md` - When mapping user's natural language to formal stereotypes
- `references/service_specification_viewpoints.json` - When validating metaconstraints, checking detailed properties, or resolving complex associations

This keeps responses efficient while ensuring access to complete metamodel data when needed.

## Common Patterns

### Pattern: Create S1 Diagram with Service Taxonomy
```
User: "Create S1 diagram with a service taxonomy"

Actions:
1. Create S1 diagram using create_or_update_diagram
2. Create 2-3 ServiceSpecification elements (type: Class) with hierarchical names
3. Create ServiceSpecificationGeneralization connectors (type: Generalization) to show taxonomy
4. Use place_element_on_diagram to add all elements to the diagram
5. Optional: Use layout_diagram for automatic arrangement
```

### Pattern: Add Service Interface with Ports
```
User: "Add service interface with input and output ports"

Actions:
1. Create ServiceInterface element (type: Class)
2. Create 2 ServicePort elements (type: Port) - one for input, one for output
3. Associate ports with the interface (typically through containment)
4. If a diagram is open, add all elements to it
```

### Pattern: Model Service Function Behavior
```
User: "Model authentication service function"

Actions:
1. Create ServiceFunction element (type: Activity) named "AuthenticateUser"
2. Create ServiceSpecification element if not exists
3. Create IsCapableToPerform relationship (type: Abstraction) from ServiceSpecification to ServiceFunction
4. Add to S4 diagram if one is open
```

### Pattern: Define Service Dependencies
```
User: "Service X depends on Service Y and Resource Z"

Actions:
1. Verify all elements exist using find_elements_by_name
2. Load service_specification_viewpoints.json to check ServiceDependency metaconstraints
3. Validate: X should be ServiceSpecification (client)
4. Validate: Y should be ServiceSpecification (supplier)
5. Validate: Z should be ResourcePerformer or compatible type (supplier)
6. Create two ServiceDependency connectors (type: Dependency):
   - From X to Y
   - From X to Z
```

### Pattern: Create Service Roadmap with Milestones
```
User: "Create service roadmap showing project milestones"

Actions:
1. Create Sr diagram using create_or_update_diagram
2. Create ActualProject elements (type: Object)
3. Create ActualProjectMilestone elements (type: Object)
4. Create OwnedMilestone connectors (type: Dependency) from projects to milestones
5. Create ActualService or ServiceSpecification elements
6. Create VersionReleased connectors linking milestones to services
7. Add all to diagram and layout
```

### Pattern: Add Service Policy Constraints
```
User: "Add service policy requiring encryption"

Actions:
1. Create ServicePolicy element (type: Class) named "EncryptionPolicy"
2. Set notes to describe the encryption requirement
3. If reference document exists, create JustifiedBy relationship to it
4. Create Satisfy relationship from policy to affected ServiceSpecification
5. Add to S8 diagram if one is open
```

## Error Handling

### Element Not Found
- Use MCP `find_elements_by_name` to search for element
- If multiple matches, present list and ask user to clarify (by GUID or package path)
- If none found, offer to create the element
- Ask for element details if creation is needed

### Invalid Connection Attempt
- Load `service_specification_viewpoints.json` and check metaconstraints
- Explain why the connection is invalid (stereotype mismatch)
- Look up valid alternatives from the same viewpoint
- Suggest correct stereotypes for both source and target

### Ambiguous Viewpoint Context
- If user says "add service" without viewpoint context, check current open diagram
- If no diagram context available, ask which viewpoint (S1-S8, Sr) they're working in
- Default to S1 for basic service taxonomy if user is unsure
- Explain briefly what each viewpoint is for

### Missing Package Path
- If package path not specified, check current package using get_current_package
- If no current package, ask user where to create element
- Suggest logical locations like "Model/Services" or "Model/ServiceArchitecture"

### Diagram Type Confusion
- Remember S6 (Service Interactions) uses "Sequence" diagram type
- All other service viewpoints use "Custom" diagram type
- If user requests S6 and you use wrong type, correct it

## Viewpoint-Specific Guidance

### S1 - Service Taxonomy
**Purpose:** Establish governance structure for service-oriented architecture
**Key elements:** ServiceSpecification, ServicePolicy
**Key relationships:** ServiceClassification, ServiceSpecificationGeneralization
**Common use:** Creating hierarchies of service types, showing service governance

### S2 - Service Structure
**Purpose:** Define how services are composed and their dependencies
**Key elements:** ServiceSpecification, ServiceSpecificationRole, ServiceInterface, ServiceFunction
**Key relationships:** ServiceDependency, IsCapableToPerform, ProvidesServiceFunction
**Common use:** Showing service compositions, dependencies on resources/nodes

### S3 - Service Interfaces
**Purpose:** Define contracts and interfaces between services
**Key elements:** ServiceInterface, ServicePort, DataElement
**Key relationships:** ServiceConnector
**Common use:** Specifying interface definitions, data exchanges between services

### S4 - Service Functions
**Purpose:** Specify behavioral functions that services perform
**Key elements:** ServiceFunction, ServiceFunctionAction, ServiceSpecificationRole
**Key relationships:** IsCapableToPerform, PerformsInContext
**Common use:** Modeling service behavior, function decomposition

### S5 - Service States
**Purpose:** Define allowable states and transitions for services
**Key elements:** ServiceSpecification, ServiceStateDescription
**Common use:** State machine modeling (though services are typically stateless)

### S6 - Service Interactions
**Purpose:** Model interaction sequences between services
**Key elements:** ServiceMessage, ServiceSpecificationRole
**Diagram type:** Sequence (not Custom!)
**Common use:** Sequence diagrams showing service call patterns

### S7 - Service Interface Parameters
**Purpose:** Specify interface parameters and compatibility
**Key elements:** ServiceSpecification, ServiceInterface, ServiceFunction
**Key relationships:** ProvidesServiceFunction
**Common use:** Detailed interface specifications, compatibility matrices

### S8 - Service Policy
**Purpose:** Define constraints governing service implementations
**Key elements:** ServicePolicy, StrategicConstraint, OperationalConstraint, ResourceConstraint
**Key relationships:** Satisfy, Implements, JustifiedBy
**Common use:** Policy governance, constraint enforcement

### Sr - Service Roadmap
**Purpose:** Track service lifecycle and evolution over time
**Key elements:** ActualService, ActualProject, ActualProjectMilestone
**Key relationships:** NeedsService, VersionReleased, VersionWithdrawn, ProjectSequence
**Common use:** Timeline planning, service versioning, project milestones

## Tips for Effective Usage

- **Be specific about viewpoints** - "Create S3 diagram" is clearer than generic "service diagram"
- **Use natural language freely** - "Service depends on database" works as well as formal "ServiceDependency"
- **Provide context when possible** - Mentioning parent services or current diagram helps placement
- **Combine operations** - "Create S2 with service and its dependencies" is efficient and clear
- **Trust auto-naming** - For services with long descriptions, let the skill generate concise names
- **Validate before complex operations** - For critical models, ask skill to verify connections first
- **Remember S6 is special** - It's the only service viewpoint using Sequence diagrams
- **Use roadmap for planning** - Sr viewpoint is powerful for timeline and version planning

## Reference Files

This skill includes two reference files for progressive data loading:

- **references/stereotype_mappings.md** - Quick reference for stereotype lookup and natural language → formal term mapping
- **references/service_specification_viewpoints.json** - Complete NAF v4 Service Specification metamodel extracted from MDG with all stereotypes, properties, metaconstraints, and toolbox definitions
