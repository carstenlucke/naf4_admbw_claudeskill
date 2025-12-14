# NAF v4 Physical Resources - Stereotype Mappings

This reference provides quick lookup tables for stereotypes, UML types, and valid connections in NAF v4 Physical Resource Specification Viewpoints.

## Viewpoints Overview

| Viewpoint | Identifier | Purpose |
|-----------|------------|---------|
| Resource Types | P1 | Catalog resource types with performance characteristics |
| Resource Structure | P2 | Show how resources are structured to realize logical architecture |
| Resource Connectivity | P3 | Document networks and physical implementation pathways |
| Resource Functions | P4 | Detail allocation of functions to resources and flows |
| Resource States | P5 | Identify states and transitions of resources |
| Resource Sequence | P6 | Define sequence of functions and resource interactions |
| Data Model | P7 | Describe physical implementation of logical data model |
| Resource Constraints | P8 | Document constraints on resources and communications |
| Configuration Management | Pr | Track resource asset changes over time |

## Element Stereotypes by Viewpoint

### P1 - Resource Types
- **CapabilityConfiguration** (Class) - Physical and human resources assembled to meet a capability
- **Energy** (Class) - Any kind of energy
- **NaturalResource** (Class) - Physical resource occurring in nature
- **ResourceArchitecture** (Class) - Architecture model from resource perspective
- **ResourceArtifact** (Class) - Man-made object without human beings
- **ResourceInterface** (Class) - Contract specification between resources
- **Software** (Class) - Executable computer program
- **System** (Class) - Integrated set of elements accomplishing defined objective
- **Technology** (Class) - Technology domain (nuclear, mechanical, electronic, etc.)
- **ActualEnterprisePhase** (Object) - Phase of enterprise endeavor
- **EnterprisePhase** (Class) - Current or future state of enterprise
- **Competence** (Class) - Set of abilities (knowledge, skills, aptitude)
- **Organization** (Class) - Group of organizational resources
- **Person** (Class) - Type of human being
- **Post** (Class) - Job title or position
- **ActualResource** (Object) - Individual resource instance
- **ActualService** (Object) - Individual service specification
- **ProvidedServiceLevel** (Object) - Specific service level delivered
- **RequiredServiceLevel** (Object) - Specific service level required
- **DataElement** (Class) - Formalized data representation
- **PaperForm** (Class) - Digitized or digitizable document
- **ServiceSpecification** (Class) - Set of functionality provided
- **ActualCondition** (Object) - Actual operational situation
- **ActualEnvironment** (Object) - Actual environmental circumstances
- **ActualLocation** (Object) - Physical location
- **Measurement** (Part) - Property expressed in unit of measure
- **MeasurementType** (Class) - Type of measured property
- **Classification** (Class) - Classification according to STANAG 1059
- **DocumentReference** (Class) - Regulation, instruction, or document
- **Reference** (Class) - All types of references
- **ResourceConstraint** (Class) - Rule governing implementation aspects
- **SMEReference** (Class) - Workshop result or expert knowledge
- **Standard** (Class) - Ratified specification guiding architecture
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Recommendation from finding
- **ActualOrganization** (Object) - Specific organization instance
- **ActualPerson** (Object) - Specific person instance
- **ActualPost** (Object) - Specific post/role instance
- **ActualProject** (Object) - Specific project instance
- **Concern** (Class) - Stakeholder concern
- **Project** (Class) - Time-limited endeavor type

### P2 - Resource Structure
- **CapabilityConfiguration** (Class) - Physical and human resources assembled
- **NaturalResource** (Class) - Resource occurring in nature
- **ResourceArchitecture** (Class) - Architecture from resource perspective
- **ResourceArtifact** (Class) - Man-made object
- **ResourceRole** (Part) - Usage of resource in context
- **Software** (Class) - Executable program
- **System** (Class) - Integrated set of elements
- **DataElement** (Class) - Formalized data representation
- **DataRole** (Part) - Usage of data element in context
- **Energy** (Class) - Any kind of energy
- **GeoPoliticalExtentType** (DataType) - Geospatial extent
- **Competence** (Class) - Set of abilities
- **Organization** (Class) - Group of resources
- **Person** (Class) - Type of human being
- **Post** (Class) - Job title or position
- **PostRole** (Part) - Usage of post in context
- **SubOrganization** (Part) - Part of organization
- **ActualProject** (Object) - Specific project instance
- **Function** (Activity) - Activity performed by resource
- **ServiceSpecification** (Class) - Functionality specification
- **ServiceSpecificationRole** (Part) - Service calling another service
- **ActualCondition** (Object) - Actual operational situation
- **ActualEnvironment** (Object) - Environmental circumstances
- **ActualLocation** (Object) - Physical location
- **Measurement** (Part) - Measured property
- **MeasurementType** (Class) - Type of measurement
- **Environment** (Class) - Environmental factors definition
- **Location** (Class) - Generic area specification
- **Classification** (Class) - STANAG 1059 classification
- **DocumentReference** (Class) - Document or regulation
- **Reference** (Class) - Reference types
- **ResourceConstraint** (Class) - Implementation rule
- **SMEReference** (Class) - Expert knowledge
- **Standard** (Class) - Ratified specification
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualOrganization** (Object) - Specific organization
- **ActualPerson** (Object) - Specific person
- **ActualPost** (Object) - Specific post
- **Concern** (Class) - Stakeholder concern
- **Project** (Class) - Endeavor type

### P3 - Resource Connectivity
- **CapabilityConfiguration** (Class) - Resources assembled for capability
- **ResourceArchitecture** (Class) - Resource perspective architecture
- **ResourceArtifact** (Class) - Man-made object
- **ResourceRole** (Part) - Resource in context
- **Software** (Class) - Computer program
- **System** (Class) - Integrated elements
- **ResourceInterface** (Class) - Contract between resources
- **ResourcePort** (Port) - Interaction point for resource
- **Protocol** (Class) - Network communication standard
- **ProtocolLayer** (Part) - Protocol in context
- **Protocolstack** (Class) - Complete protocol stack
- **Standard** (Class) - Ratified specification
- **DataElement** (Class) - Data representation
- **DataRole** (Part) - Data in context
- **ResourceSignal** (Signal) - Physical world property
- **Classification** (Class) - STANAG classification
- **DocumentReference** (Class) - Document reference
- **Reference** (Class) - Reference type
- **ResourceConstraint** (Class) - Implementation rule
- **SMEReference** (Class) - Expert knowledge
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualCondition** (Object) - Operational situation
- **ActualEnvironment** (Object) - Environmental circumstances
- **ActualLocation** (Object) - Physical location
- **Measurement** (Part) - Measured property
- **MeasurementType** (Class) - Measurement type
- **ActualOrganization** (Object) - Specific organization
- **ActualPerson** (Object) - Specific person
- **ActualPost** (Object) - Specific post
- **ActualProject** (Object) - Specific project
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Resource group
- **Person** (Class) - Human being type
- **Post** (Class) - Job position
- **Project** (Class) - Endeavor type

### P4 - Resource Functions
- **DataElement** (Class) - Data representation
- **FunctionAction** (Action) - Function call in context
- **Function** (Activity) - Activity performed by resource
- **ActualCondition** (Object) - Operational situation
- **ActualEnvironment** (Object) - Environmental circumstances
- **ActualLocation** (Object) - Physical location
- **Measurement** (Part) - Measured property
- **MeasurementType** (Class) - Measurement type
- **Classification** (Class) - STANAG classification
- **DocumentReference** (Class) - Document reference
- **Reference** (Class) - Reference type
- **ResourceConstraint** (Class) - Implementation rule
- **SMEReference** (Class) - Expert knowledge
- **Standard** (Class) - Ratified specification
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualOrganization** (Object) - Specific organization
- **ActualPerson** (Object) - Specific person
- **ActualPost** (Object) - Specific post
- **ActualProject** (Object) - Specific project
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Resource group
- **Person** (Class) - Human being type
- **Post** (Class) - Job position
- **Project** (Class) - Endeavor type

### P5 - Resource States
- **ResourceStateDescription** (StateMachine) - State machine for resource behavior
- **Classification** (Class) - STANAG classification
- **DocumentReference** (Class) - Document reference
- **Reference** (Class) - Reference type
- **ResourceConstraint** (Class) - Implementation rule
- **SMEReference** (Class) - Expert knowledge
- **Standard** (Class) - Ratified specification
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualOrganization** (Object) - Specific organization
- **ActualPerson** (Object) - Specific person
- **ActualPost** (Object) - Specific post
- **ActualProject** (Object) - Specific project
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Resource group
- **Person** (Class) - Human being type
- **Post** (Class) - Job position
- **Project** (Class) - Endeavor type

### P6 - Resource Sequence
- **ResourceMessage** (Message) - Message carrying resource exchange
- **ResourceRole** (Part) - Resource in context
- **ServiceMessage** (Message) - Message for service event-trace
- **ServiceSpecificationRole** (Part) - Service in context
- **Classification** (Class) - STANAG classification
- **DocumentReference** (Class) - Document reference
- **Reference** (Class) - Reference type
- **ResourceConstraint** (Class) - Implementation rule
- **SMEReference** (Class) - Expert knowledge
- **Standard** (Class) - Ratified specification
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualOrganization** (Object) - Specific organization
- **ActualPerson** (Object) - Specific person
- **ActualPost** (Object) - Specific post
- **ActualProject** (Object) - Specific project
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Resource group
- **Person** (Class) - Human being type
- **Post** (Class) - Job position
- **Project** (Class) - Endeavor type

### P7 - Data Model
- **DataElement** (Class) - Data representation
- **DataModel** (Package) - Structural specification of data types
- **DataRole** (Part) - Data in context
- **Standard** (Class) - Ratified specification
- **Classification** (Class) - STANAG classification
- **DocumentReference** (Class) - Document reference
- **Reference** (Class) - Reference type
- **ResourceConstraint** (Class) - Implementation rule
- **SMEReference** (Class) - Expert knowledge
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualOrganization** (Object) - Specific organization
- **ActualPerson** (Object) - Specific person
- **ActualPost** (Object) - Specific post
- **ActualProject** (Object) - Specific project
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Resource group
- **Person** (Class) - Human being type
- **Post** (Class) - Job position
- **Project** (Class) - Endeavor type

### P8 - Resource Constraints
- **Classification** (Class) - STANAG classification
- **DocumentReference** (Class) - Document reference
- **Reference** (Class) - Reference type
- **ResourceConstraint** (Class) - Implementation rule
- **SMEReference** (Class) - Expert knowledge
- **Standard** (Class) - Ratified specification
- **OperationalConstraint** (Class) - Logical architecture rule
- **ServicePolicy** (Class) - Service specification constraint
- **StrategicConstraint** (Class) - Capability rule
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualOrganization** (Object) - Specific organization
- **ActualPerson** (Object) - Specific person
- **ActualPost** (Object) - Specific post
- **ActualProject** (Object) - Specific project
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Resource group
- **Person** (Class) - Human being type
- **Post** (Class) - Job position
- **Project** (Class) - Endeavor type

### Pr - Configuration Management
- **VersionOfConfiguration** (Part) - Version control property
- **WholeLifeConfiguration** (Class) - Set of versioned elements
- **ActualProject** (Object) - Specific project
- **ActualProjectMilestone** (Object) - Project event with date
- **Project** (Class) - Endeavor type
- **ProjectMilestone** (Class) - Event type in project
- **ProjectMilestoneRole** (Part) - Milestone in project context
- **Classification** (Class) - STANAG classification
- **DocumentReference** (Class) - Document reference
- **Reference** (Class) - Reference type
- **ResourceConstraint** (Class) - Implementation rule
- **SMEReference** (Class) - Expert knowledge
- **Standard** (Class) - Ratified specification
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualOrganization** (Object) - Specific organization
- **ActualPerson** (Object) - Specific person
- **ActualPost** (Object) - Specific post
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Resource group
- **Person** (Class) - Human being type
- **Post** (Class) - Job position

## Association Stereotypes by Viewpoint

### P1 Associations
- **PropertySetGeneralisation** (Generalization) - Taxonomic relationship between property sets
- **Forecast** (Dependency) - Transition from one asset to future one
- **ForecastPeriod** (Dependency) - Planning phase for forecast
- **RequiresCompetence** (Abstraction) - Required competencies assertion
- **Implements** (Abstraction) - Upper to lower abstraction layer implementation
- **DataElementStoredIn** (Dependency) - Data stored in software
- **FormStoredIn** (Dependency) - Digital form stored in software
- **ServiceProvision** (Abstraction) - Resource delivers service
- **EnvironmentalContext** (Dependency) - Measurement environmental condition
- **OwnsMeasurement** (Dependency) - Element owns measurement
- **Classified** (Dependency) - Element classification
- **JustifiedBy** (Dependency) - Constraint derived from reference
- **OriginatesFrom** (Dependency) - Element derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **ConformsTo** (Dependency) - Conforms to standard
- **RealizesRecommendation** (Realization) - Realizes recommendation
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Stakeholder has concern

### P2 Associations
- **HostedOn** (Dependency) - Software/hardware hosted on platform
- **ResourceDependency** (Dependency) - Resource dependency
- **Control** (InformationFlow) - Physical resource controls another
- **ResourceExchange** (InformationFlow) - Flow between resources
- **Command** (InformationFlow) - Organizational resource commands another
- **CompetenceForRole** (Dependency) - Role requires competencies
- **ActualProjectConsults** (Dependency) - Project consults resource
- **ActualProjectInforms** (Dependency) - Project informs resource
- **IsAccountableFor** (Dependency) - Responsible in approval context
- **IsResponsibleFor** (Dependency) - Responsible for resource/service/project
- **NeedsModificationOf** (Dependency) - Project modifies resource
- **NeedsResource** (Dependency) - Project needs resource
- **ProjectProvidesFunction** (Dependency) - Project realizes function
- **ProjectSupportActivity** (Dependency) - Project supports activity
- **Responsible** (Dependency) - Project responsible for service/resource
- **ResourceToServiceDependency** (Dependency) - Resource depends on service
- **ServiceProvision** (Abstraction) - Resource delivers service
- **Implements** (Abstraction) - Implementation mapping
- **EnvironmentalContext** (Dependency) - Measurement condition
- **OwnsMeasurement** (Dependency) - Element owns measurement
- **LocationType** (Dependency) - Location assignment
- **PhysicalLocation** (Dependency) - Operates in actual location
- **RequiredEnvironment** (Dependency) - Environmental conditions
- **Classified** (Dependency) - Element classification
- **JustifiedBy** (Dependency) - Constraint from reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **ConformsTo** (Dependency) - Conforms to standard
- **RealizesRecommendation** (Realization) - Realizes recommendation
- **RefersTo** (Dependency) - Finding to recommendation
- **ResultsFrom** (Dependency) - Reason for finding
- **StakeholderConcern** (Dependency) - Stakeholder concern

### P3 Associations
- **ResourceDependency** (Dependency) - Resource dependency
- **BoundaryCondition** (Dependency) - Environment for exchange
- **ResourceConnector** (Connector) - Channel between resource roles
- **ConformsTo** (Dependency) - Conforms to standard
- **ImplementsProtocol** (Dependency) - Protocol implementation
- **Control** (InformationFlow) - Resource controls another
- **ResourceExchange** (InformationFlow) - Flow between resources
- **Classified** (Dependency) - Element classification
- **JustifiedBy** (Dependency) - Constraint from reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **RealizesRecommendation** (Realization) - Realizes recommendation
- **RefersTo** (Dependency) - Finding to recommendation
- **ResultsFrom** (Dependency) - Reason for finding
- **EnvironmentalContext** (Dependency) - Measurement condition
- **OwnsMeasurement** (Dependency) - Element owns measurement
- **StakeholderConcern** (Dependency) - Stakeholder concern

### P4 Associations
- **FunctionControlFlow** (ControlFlow) - Control flow between actions
- **FunctionObjectFlow** (ObjectFlow) - Object/data flow between actions
- **IsCapableToPerform** (Abstraction) - Element performs activity
- **PerformsInContext** (Abstraction) - Role performs in context
- **EnvironmentalContext** (Dependency) - Measurement condition
- **OwnsMeasurement** (Dependency) - Element owns measurement
- **AffectedFunctions** (Dependency) - Function affected by resource
- **FunctionSubject** (Dependency) - Function uses resources
- **Classified** (Dependency) - Element classification
- **JustifiedBy** (Dependency) - Constraint from reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **ConformsTo** (Dependency) - Conforms to standard
- **RealizesRecommendation** (Realization) - Realizes recommendation
- **RefersTo** (Dependency) - Finding to recommendation
- **ResultsFrom** (Dependency) - Reason for finding
- **StakeholderConcern** (Dependency) - Stakeholder concern

### P5 Associations
- **Classified** (Dependency) - Element classification
- **JustifiedBy** (Dependency) - Constraint from reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **ConformsTo** (Dependency) - Conforms to standard
- **RealizesRecommendation** (Realization) - Realizes recommendation
- **RefersTo** (Dependency) - Finding to recommendation
- **ResultsFrom** (Dependency) - Reason for finding
- **StakeholderConcern** (Dependency) - Stakeholder concern

### P6 Associations
- **Classified** (Dependency) - Element classification
- **JustifiedBy** (Dependency) - Constraint from reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **ConformsTo** (Dependency) - Conforms to standard
- **RealizesRecommendation** (Realization) - Realizes recommendation
- **RefersTo** (Dependency) - Finding to recommendation
- **ResultsFrom** (Dependency) - Reason for finding
- **StakeholderConcern** (Dependency) - Stakeholder concern

### P7 Associations
- **Implements** (Abstraction) - Implementation mapping
- **ConformsTo** (Dependency) - Conforms to standard
- **Classified** (Dependency) - Element classification
- **JustifiedBy** (Dependency) - Constraint from reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **RealizesRecommendation** (Realization) - Realizes recommendation
- **RefersTo** (Dependency) - Finding to recommendation
- **ResultsFrom** (Dependency) - Reason for finding
- **StakeholderConcern** (Dependency) - Stakeholder concern

### P8 Associations
- **Classified** (Dependency) - Element classification
- **JustifiedBy** (Dependency) - Constraint from reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **ConformsTo** (Dependency) - Conforms to standard
- **Implements** (Abstraction) - Implementation mapping
- **RealizesRecommendation** (Realization) - Realizes recommendation
- **RefersTo** (Dependency) - Finding to recommendation
- **ResultsFrom** (Dependency) - Reason for finding
- **StakeholderConcern** (Dependency) - Stakeholder concern

### Pr Associations
- **SuccessorOf** (Dependency) - Element succession
- **VersionSuccession** (Dependency) - Version succession
- **ActualProjectDependency** (Dependency) - Project dependency
- **MilestoneDependency** (Dependency) - Milestone succession
- **OwnedMilestone** (Dependency) - Project owns milestone
- **ProjectMilestoneToProjectTheme** (Dependency) - Milestone handles theme
- **ProjectSequence** (Dependency) - Project start sequence
- **RequiredResource** (Dependency) - Milestone requires resources
- **VersionReleased** (Dependency) - Milestone releases version
- **VersionWithdrawn** (Dependency) - Milestone withdraws version
- **Classified** (Dependency) - Element classification
- **JustifiedBy** (Dependency) - Constraint from reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **ConformsTo** (Dependency) - Conforms to standard
- **RealizesRecommendation** (Realization) - Realizes recommendation
- **RefersTo** (Dependency) - Finding to recommendation
- **ResultsFrom** (Dependency) - Reason for finding
- **StakeholderConcern** (Dependency) - Stakeholder concern

## Common Aliases and Natural Language Mappings

### Element Types (Casual → Formal)
- "resource type" / "resource" → ResourceArtifact, System, Software, or NaturalResource
- "system" → System
- "software" → Software
- "capability configuration" → CapabilityConfiguration
- "interface" → ResourceInterface
- "port" → ResourcePort
- "function" → Function
- "function action" → FunctionAction
- "state machine" → ResourceStateDescription
- "data" / "data element" → DataElement
- "service" → ServiceSpecification
- "organization" → Organization or ActualOrganization
- "person" → Person or ActualPerson
- "post" / "role" → Post or ActualPost
- "project" → Project or ActualProject
- "milestone" → ProjectMilestone or ActualProjectMilestone
- "measurement" → Measurement or MeasurementType
- "constraint" → ResourceConstraint
- "standard" → Standard
- "protocol" → Protocol or Protocolstack
- "energy" → Energy
- "technology" → Technology
- "competence" / "skill" → Competence
- "environment" → Environment or ActualEnvironment
- "location" → Location or ActualLocation
- "configuration" → WholeLifeConfiguration or VersionOfConfiguration
- "finding" → Finding
- "recommendation" → Recommendation
- "concern" → Concern
- "reference" / "document" → Reference or DocumentReference

### Association Types (Casual → Formal)
- "resource exchange" / "flows to" → ResourceExchange
- "controls" → Control
- "commands" → Command
- "hosted on" / "runs on" → HostedOn
- "depends on" → ResourceDependency or ResourceToServiceDependency
- "implements" → Implements
- "provides service" → ServiceProvision
- "performs" / "capable of" → IsCapableToPerform or PerformsInContext
- "conforms to" / "complies with" → ConformsTo
- "implements protocol" → ImplementsProtocol
- "connected to" → ResourceConnector
- "control flow" → FunctionControlFlow
- "object flow" → FunctionObjectFlow
- "requires competence" → RequiresCompetence or CompetenceForRole
- "forecast" / "transitions to" → Forecast
- "stored in" → DataElementStoredIn or FormStoredIn
- "owns measurement" → OwnsMeasurement
- "justified by" → JustifiedBy
- "originates from" / "derived from" → OriginatesFrom
- "satisfies" / "affected by" → Satisfy
- "realizes recommendation" → RealizesRecommendation
- "refers to" → RefersTo
- "results from" → ResultsFrom
- "stakeholder concern" → StakeholderConcern
- "located at" → PhysicalLocation or LocationType
- "required environment" → RequiredEnvironment
- "successor of" → SuccessorOf
- "version succession" → VersionSuccession
- "project dependency" → ActualProjectDependency
- "milestone dependency" → MilestoneDependency
- "needs resource" → NeedsResource or RequiredResource
- "responsible for" → IsResponsibleFor or Responsible
- "accountable for" → IsAccountableFor

## Profile Information
All elements and associations use profile: **NAFv4-ADMBw**
