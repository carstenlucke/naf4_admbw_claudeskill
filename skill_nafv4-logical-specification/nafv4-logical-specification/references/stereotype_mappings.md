# NAF v4 Logical Specification - Stereotype Mappings

This reference provides quick lookup tables for stereotypes, UML types, and valid connections in NAF v4 Logical Specification Viewpoints.

## Viewpoints Overview

| Viewpoint | Identifier | Purpose |
|-----------|------------|---------|
| Node Types | L1 | Define nodes appearing in logical architecture with measures of performance |
| Logical Scenario | L2 | Specify nodes in context with information/resource flows between them |
| Node Interactions | L3 | Detail interoperability requirements and logical flows crossing boundaries |
| Logical Activities | L4 | Describe operational activities at logical, solution-neutral level |
| Logical States | L5 | Specify node states and transitions between them |
| Logical Sequence | L6 | Trace interactions and event sequences between nodes |
| Information Model | L7 | Document business information exchanged along logical flows |
| Logical Constraints | L8 | Constrain logical architecture with textual requirements |
| Lines of Development | Lr | Support acquisition across projects with capability dependencies |

## Element Stereotypes by Viewpoint

### L1 - Node Types
- **OperationalPerformer** (Class) - Logical entity that performs operational activities
- **OperationalRole** (Part) - Usage of performer in specific context
- **OperationalActivity** (Activity) - Logical process specification
- **OperationalActivityAction** (Action) - Call of activity in another activity context
- **Environment** (Class) - Environmental factors definition
- **Measurement** (Part) - Property with unit of measure
- **MeasurementType** (Class) - Type of measurement property
- **ActualCondition** (Object) - Actual situation for activity performance
- **ActualEnvironment** (Object) - Actual environmental circumstances
- **ActualLocation** (Object) - Actual physical location
- **Standard** (Class) - Ratified specification
- **OperationalConstraint** (Class) - Rule governing logical elements
- **Classification** (Class) - STANAG 1059 classification
- **DocumentReference** (Class) - Regulation or document
- **Reference** (Class) - All types of references
- **SMEReference** (Class) - Workshop or expert knowledge
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Recommendation from finding
- **ActualOrganization** (Object) - Specific organization instance
- **ActualPerson** (Object) - Individual person instance
- **ActualPost** (Object) - Specific post/role instance
- **ActualProject** (Object) - Specific project instance
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Organization type
- **Person** (Class) - Person type
- **Post** (Class) - Post/role type
- **Project** (Class) - Project type

### L2 - Logical Scenario
- **OperationalPerformer** (Class) - Logical entity performing activities
- **OperationalRole** (Part) - Performer usage in context
- **OperationalArchitecture** (Class) - Operational perspective architecture
- **OperationalInterface** (Class) - Interaction contract specification
- **OperationalPort** (Port) - Interaction point for performer
- **ProblemDomain** (Part) - Logical architecture scope
- **KnownResource** (Class) - Known resource constraining implementation
- **InformationElement** (Class) - Information flowing between performers
- **OperationalSignal** (Signal) - Information signal
- **Energy** (Class) - Energy representation
- **NaturalResource** (Class) - Physical resource occurring in nature
- **Organization** (Class) - Organizational resources group
- **Person** (Class) - Human being type
- **Post** (Class) - Job title or position type
- **Project** (Class) - Time-limited endeavor type
- **ResourceArchitecture** (Class) - Resource performer perspective
- **ResourceArtifact** (Class) - Man-made object
- **Responsibility** (Class) - Duty required of person/organization
- **GeoPoliticalExtentType** (DataType) - Geospatial extent
- **Condition** (Class) - Location, environment, geopolitical extent
- **Environment** (Class) - Environmental factors
- **Location** (Class) - Generic area specification
- **ActualCondition** (Object) - Actual situation instance
- **ActualEnvironment** (Object) - Actual environmental state
- **ActualLocation** (Object) - Actual physical location
- **Measurement** (Part) - Property with unit
- **MeasurementType** (Class) - Measurement type
- **OperationalConstraint** (Class) - Logical architecture rule
- **Standard** (Class) - Specification standard
- **Classification** (Class) - Classification per STANAG 1059
- **DocumentReference** (Class) - Document reference
- **Reference** (Class) - Reference types
- **SMEReference** (Class) - Expert knowledge reference

### L3 - Node Interactions
- **OperationalPerformer** (Class) - Logical entity performing activities
- **OperationalRole** (Part) - Performer in specific context
- **OperationalArchitecture** (Class) - Operational architecture
- **OperationalInterface** (Class) - Interaction contract
- **OperationalPort** (Port) - Interaction point
- **ProblemDomain** (Part) - Problem scope
- **KnownResource** (Class) - Known constraining resource
- **InformationElement** (Class) - Information item
- **InformationRole** (Part) - Information usage in context
- **OperationalSignal** (Signal) - Information signal
- **Energy** (Class) - Energy type
- **NaturalResource** (Class) - Natural physical resource
- **Organization** (Class) - Organization type
- **Person** (Class) - Person type
- **Post** (Class) - Position type
- **PostRole** (Class) - Post usage in context
- **Project** (Class) - Project type
- **ResourceArchitecture** (Class) - Resource architecture
- **ResourceArtifact** (Class) - Man-made object
- **Responsibility** (Class) - Required duty
- **SubOrganization** (Class) - Sub-organizational unit
- **CapabilityConfiguration** (Class) - Physical and human resources assembly
- **GeoPoliticalExtentType** (DataType) - Geospatial boundaries
- **ServiceSpecification** (Class) - Functionality specification
- **ServiceSpecificationRole** (Part) - Service specification usage
- **Condition** (Class) - Location/environment/geopolitical extent
- **Environment** (Class) - Environmental factors
- **Location** (Class) - Generic area
- **ActualCondition** (Object) - Actual condition
- **ActualEnvironment** (Object) - Actual environment
- **ActualLocation** (Object) - Actual location
- **Measurement** (Part) - Measured property
- **MeasurementType** (Class) - Measurement type

### L4 - Logical Activities
- **OperationalActivity** (Activity) - Logical process
- **OperationalActivityAction** (Action) - Activity call
- **StandardOperationalActivity** (Activity) - Standard operating procedure
- **OperationalPerformer** (Class) - Activity performer
- **OperationalRole** (Part) - Performer role
- **InformationElement** (Class) - Information item
- **InformationRole** (Part) - Information in context
- **OperationalSignal** (Signal) - Information signal
- **KnownResource** (Class) - Known resource
- **NaturalResource** (Class) - Natural resource
- **Organization** (Class) - Organization
- **Person** (Class) - Person
- **Post** (Class) - Position
- **Project** (Class) - Project
- **ResourceArchitecture** (Class) - Resource architecture
- **ResourceArtifact** (Class) - Artifact
- **Responsibility** (Class) - Duty
- **PaperForm** (Class) - Digitized document
- **GeoPoliticalExtentType** (DataType) - Geopolitical extent
- **ActualCondition** (Object) - Actual condition
- **ServiceSpecification** (Class) - Service specification
- **ActualService** (Object) - Individual service
- **RequiredServiceLevel** (Object) - Required service level
- **OperationalConstraint** (Class) - Operational constraint
- **Standard** (Class) - Standard
- **Classification** (Class) - Classification
- **DocumentReference** (Class) - Document
- **Reference** (Class) - Reference
- **SMEReference** (Class) - SME reference

### L5 - Logical States
- **OperationalPerformer** (Class) - Logical entity
- **OperationalArchitecture** (Class) - Operational architecture
- **OperationalStateDescription** (StateMachine) - State machine for performer behavior
- **OperationalConstraint** (Class) - Constraint
- **Standard** (Class) - Standard
- **Classification** (Class) - Classification
- **DocumentReference** (Class) - Document
- **Reference** (Class) - Reference
- **SMEReference** (Class) - SME reference

### L6 - Logical Sequence
- **OperationalRole** (Part) - Performer role for sequence
- **ServiceSpecificationRole** (Part) - Service role for sequence
- **OperationalMessage** (Message) - Operational exchange message
- **ServiceMessage** (Message) - Service message
- **Standard** (Class) - Standard
- **OperationalConstraint** (Class) - Constraint
- **Classification** (Class) - Classification
- **DocumentReference** (Class) - Document
- **Reference** (Class) - Reference
- **SMEReference** (Class) - SME reference

### L7 - Information Model
- **InformationElement** (Class) - Information item
- **InformationRole** (Part) - Information in context
- **DataModel** (Package) - Data type structural specification
- **OperationalConstraint** (Class) - Operational constraint
- **ResourceConstraint** (Class) - Resource constraint
- **Standard** (Class) - Standard
- **Classification** (Class) - Classification
- **DocumentReference** (Class) - Document
- **Reference** (Class) - Reference
- **SMEReference** (Class) - SME reference

### L8 - Logical Constraints
- **OperationalConstraint** (Class) - Logical architecture constraint
- **ResourceConstraint** (Class) - Implementation constraint
- **ServicePolicy** (Class) - Service specification constraint
- **StrategicConstraint** (Class) - Capability constraint
- **Standard** (Class) - Standard
- **Classification** (Class) - Classification
- **DocumentReference** (Class) - Document
- **Reference** (Class) - Reference
- **SMEReference** (Class) - SME reference

### Lr - Lines of Development
- **ActualProject** (Object) - Actual project instance
- **ActualProjectMilestone** (Object) - Project milestone instance
- **Project** (Class) - Project type
- **ProjectMilestone** (Class) - Milestone type
- **ProjectMilestoneRole** (Part) - Milestone role
- **ProjectTheme** (Part) - Milestone aspect
- **CapabilityConfiguration** (Class) - Capability assembly
- **EnterprisePhase** (Class) - Enterprise state
- **ServiceSpecification** (Class) - Service specification
- **ArchitecturalDescription** (Package) - Architecture description
- **Standard** (Class) - Standard
- **OperationalConstraint** (Class) - Constraint
- **Classification** (Class) - Classification
- **DocumentReference** (Class) - Document
- **Reference** (Class) - Reference
- **SMEReference** (Class) - SME reference

## Association Stereotypes by Viewpoint

### L1 Associations
- **Exhibits** (Abstraction) - Capable element meets capability under conditions
- **MapsToCapability** (Abstraction) - Activity contributes to capability
- **EnvironmentalCondition** (Dependency) - Environment for exhibits relationship
- **PropertySetGeneralisation** (Generalization) - Property set taxonomy
- **OwnsMeasurement** (Dependency) - Element owns measurement
- **EnvironmentalContext** (Dependency) - Condition for measurement
- **ConformsTo** (Dependency) - Conforms to standard
- **Classified** (Dependency) - Classification assignment
- **JustifiedBy** (Dependency) - Constraint derived from reference
- **OriginatesFrom** (Dependency) - Element derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - Finding to recommendation
- **ResultsFrom** (Dependency) - Element causes finding
- **StakeholderConcern** (Dependency) - Stakeholder has concern

### L2 Associations
- **OperationalConnector** (Connector) - Connection between operational roles
- **OperationalExchange** (InformationFlow) - Flow between performers
- **LocationType** (Dependency) - Location assignment
- **PhysicalLocation** (Dependency) - Operates in actual location
- **RequiredEnvironment** (Dependency) - Operates under environment
- **OwnsMeasurement** (Dependency) - Owns measurement
- **EnvironmentalContext** (Dependency) - Measurement condition
- **Satisfy** (Dependency) - Constraint affects element
- **ConformsTo** (Dependency) - Conforms to standard
- **Classified** (Dependency) - Classification assignment
- **JustifiedBy** (Dependency) - Derived from reference
- **OriginatesFrom** (Dependency) - Originates from reference

### L3 Associations
- **OperationalConnector** (Connector) - Connection between roles
- **OperationalExchange** (InformationFlow) - Exchange between performers
- **IsCapableToPerform** (Abstraction) - Performs activity
- **PerformsInContext** (Abstraction) - Role performs in context
- **ConsumedBy** (Dependency) - Service consumed by node
- **Provides** (Dependency) - Agent provides service
- **LocationType** (Dependency) - Location assignment
- **PhysicalLocation** (Dependency) - Operates in location
- **RequiredEnvironment** (Dependency) - Environmental conditions
- **OwnsMeasurement** (Dependency) - Owns measurement
- **EnvironmentalContext** (Dependency) - Measurement condition

### L4 Associations
- **IsCapableToPerform** (Abstraction) - Capable to perform activity
- **PerformsInContext** (Abstraction) - Performs in context
- **OperationalExchange** (InformationFlow) - Operational exchange
- **ProcessGeneralization** (Generalization) - Process taxonomy
- **Consumes** (Abstraction) - Service assists activity
- **ActsUpon** (Dependency) - Activity acts upon resource
- **AffectedActivity** (Dependency) - Resource affects activity
- **AffectedResource** (Dependency) - Activity affects resource
- **ActivityPerformableUnderCondition** (Dependency) - Activity under condition
- **ActivitySupportsService** (Realization) - Process implements service
- **Implements** (Abstraction) - Implements upper layer element
- **ConformsTo** (Dependency) - Conforms to standard
- **Classified** (Dependency) - Classification
- **JustifiedBy** (Dependency) - Derived from reference
- **OriginatesFrom** (Dependency) - Originates from reference
- **Satisfy** (Dependency) - Constraint affects element

### L5 Associations
- **ConformsTo** (Dependency) - Conforms to standard
- **Classified** (Dependency) - Classification
- **JustifiedBy** (Dependency) - Derived from reference
- **OriginatesFrom** (Dependency) - Originates from reference
- **Satisfy** (Dependency) - Constraint affects element
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - Finding to recommendation
- **ResultsFrom** (Dependency) - Causes finding
- **StakeholderConcern** (Dependency) - Stakeholder concern

### L6 Associations
- **ConformsTo** (Dependency) - Conforms to standard
- **Classified** (Dependency) - Classification
- **JustifiedBy** (Dependency) - Derived from reference
- **OriginatesFrom** (Dependency) - Originates from reference
- **Satisfy** (Dependency) - Constraint affects element
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - Finding to recommendation
- **ResultsFrom** (Dependency) - Causes finding
- **StakeholderConcern** (Dependency) - Stakeholder concern

### L7 Associations
- **Implements** (Abstraction) - Implements upper layer element
- **ConformsTo** (Dependency) - Conforms to standard
- **Classified** (Dependency) - Classification
- **JustifiedBy** (Dependency) - Derived from reference
- **OriginatesFrom** (Dependency) - Originates from reference
- **Satisfy** (Dependency) - Constraint affects element
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - Finding to recommendation
- **ResultsFrom** (Dependency) - Causes finding
- **StakeholderConcern** (Dependency) - Stakeholder concern

### L8 Associations
- **Implements** (Abstraction) - Constraint implements constraint
- **ConformsTo** (Dependency) - Conforms to standard
- **Classified** (Dependency) - Classification
- **JustifiedBy** (Dependency) - Derived from reference
- **OriginatesFrom** (Dependency) - Originates from reference
- **Satisfy** (Dependency) - Constraint affects element
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - Finding to recommendation
- **ResultsFrom** (Dependency) - Causes finding
- **StakeholderConcern** (Dependency) - Stakeholder concern

### Lr Associations
- **ActualProjectConsults** (Dependency) - Project consults resource
- **ActualProjectDependency** (Dependency) - Project dependency
- **ActualProjectInforms** (Dependency) - Project informs resource
- **IsAccountableFor** (Dependency) - Accountable for resource/service/project
- **IsResponsibleFor** (Dependency) - Responsible for resource/service/project
- **MilestoneDependency** (Dependency) - Milestone follows milestone
- **OwnedMilestone** (Dependency) - Project has milestone
- **ProjectMilestoneToProjectTheme** (Dependency) - Theme handled by milestone
- **ProjectSequence** (Dependency) - Project sequence
- **VersionReleased** (Dependency) - Milestone releases version
- **VersionWithdrawn** (Dependency) - Milestone withdraws version
- **RequiredResource** (Dependency) - Milestone requires resources
- **ArchitectureForProject** (Dependency) - Architecture for project

## Common Aliases and Natural Language Mappings

### Element Types (Casual → Formal)
- "node" / "logical node" → OperationalPerformer
- "operational performer" → OperationalPerformer
- "role" → OperationalRole
- "operational role" → OperationalRole
- "activity" / "logical activity" → OperationalActivity
- "operational activity" → OperationalActivity
- "action" → OperationalActivityAction
- "standard activity" / "SOP" → StandardOperationalActivity
- "interface" → OperationalInterface
- "port" → OperationalPort
- "connector" → OperationalConnector
- "architecture" / "logical architecture" → OperationalArchitecture
- "information" / "info element" → InformationElement
- "signal" → OperationalSignal
- "information role" → InformationRole
- "data model" → DataModel
- "state machine" / "states" → OperationalStateDescription
- "message" / "operational message" → OperationalMessage
- "service message" → ServiceMessage
- "service" / "service spec" → ServiceSpecification
- "service role" → ServiceSpecificationRole
- "constraint" / "logical constraint" → OperationalConstraint
- "resource constraint" → ResourceConstraint
- "service policy" → ServicePolicy
- "strategic constraint" → StrategicConstraint
- "environment" → Environment
- "location" → Location
- "condition" → Condition
- "measurement" / "measure" → Measurement
- "measurement type" / "MOP" / "measure of performance" → MeasurementType
- "project" → ActualProject or Project
- "milestone" → ActualProjectMilestone or ProjectMilestone
- "capability configuration" → CapabilityConfiguration
- "enterprise phase" → EnterprisePhase
- "standard" / "norm" → Standard
- "reference" / "document" → Reference or DocumentReference
- "SME reference" / "expert knowledge" → SMEReference
- "finding" → Finding
- "recommendation" → Recommendation
- "concern" → Concern
- "organization" → Organization or ActualOrganization
- "person" → Person or ActualPerson
- "post" / "position" → Post or ActualPost

### Association Types (Casual → Formal)
- "exchanges" / "flows to" / "sends to" → OperationalExchange
- "connected to" / "links to" → OperationalConnector
- "capable to perform" / "performs" → IsCapableToPerform
- "performs in context" / "role performs" → PerformsInContext
- "exhibits capability" / "provides capability" → Exhibits
- "maps to capability" / "contributes to" → MapsToCapability
- "provides service" → Provides
- "consumes service" / "consumed by" → ConsumedBy or Consumes
- "acts upon" / "affects" → ActsUpon
- "affected by" → AffectedActivity or AffectedResource
- "supports service" → ActivitySupportsService
- "implements" / "realizes" → Implements
- "conforms to" / "complies with" → ConformsTo
- "satisfies" / "constrained by" → Satisfy
- "originates from" / "derived from" → OriginatesFrom
- "justified by" / "based on" → JustifiedBy
- "classified as" → Classified
- "owns measurement" / "has measure" → OwnsMeasurement
- "environmental condition" / "under environment" → EnvironmentalCondition or RequiredEnvironment
- "in location" / "at location" → PhysicalLocation or LocationType
- "project dependency" / "depends on" → ActualProjectDependency or ProjectSequence
- "milestone dependency" → MilestoneDependency
- "responsible for" → IsResponsibleFor
- "accountable for" → IsAccountableFor
- "releases version" → VersionReleased
- "withdraws version" → VersionWithdrawn

## Profile Information
All elements and associations use profile: **NAFv4-ADMBw**

Note: L6 (Logical Sequence) uses **Diagram_Sequence** UML type, all other viewpoints use **Diagram_Custom**.
