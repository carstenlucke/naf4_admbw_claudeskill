# NAF v4 Service Specification - Stereotype Mappings

This reference provides quick lookup tables for stereotypes, UML types, and valid connections in NAF v4 Service Specification Viewpoints.

## Viewpoints Overview

| Viewpoint | Identifier | Purpose |
|-----------|------------|---------|
| Service Taxonomy | S1 | Provide governance structure for SOA service specifications |
| Service Structure | S2 | Define service composition and dependencies |
| Service Interfaces | S3 | Identify and define service interfaces |
| Service Functions | S4 | Specify behavioral functions of services |
| Service States | S5 | Define allowable states and transitions |
| Service Interactions | S6 | Model interactions between services |
| Service Interface Parameters | S7 | Specify interface compatibility |
| Service Policy | S8 | Define constraints on service implementations |
| Service Roadmap | Sr | Track service lifecycle and evolution |

## Element Stereotypes by Viewpoint

### S1 - Service Taxonomy
**Core Service Elements:**
- **ServiceSpecification** (Class) - Specification of service functionality
- **ServicePolicy** (Class) - Constraints governing service use

**Supporting Elements:**
- **Standard** (Class) - Standards and norms
- **Reference** (Class) - General references
- **DocumentReference** (Class) - Specific document reference
- **SMEReference** (Class) - Subject matter expert reference
- **Finding** (Class) - Assessment findings
- **Recommendation** (Class) - Recommendations from assessments
- **Classification** (Class) - STANAG 1059 classification
- **Concern** (Class) - Stakeholder concerns

**Measurement Elements:**
- **MeasurementType** (Class) - Type of measurement property
- **Measurement** (Part) - Actual measurement property
- **ActualCondition** (Object) - Specific condition instance
- **ActualEnvironment** (Object) - Specific environment instance
- **ActualLocation** (Object) - Specific location instance

**Stakeholder Elements:**
- **Organization** (Class) - Organization type
- **Person** (Class) - Person type
- **Post** (Class) - Post/role type
- **Project** (Class) - Project type
- **ActualOrganization** (Object) - Specific organization instance
- **ActualPerson** (Object) - Specific person instance
- **ActualPost** (Object) - Specific post instance
- **ActualProject** (Object) - Specific project instance

### S2 - Service Structure
**Service Elements:**
- **ServiceSpecification** (Class) - Service specification
- **ServiceSpecificationRole** (Part) - Service role in composition
- **ServiceInterface** (Class) - Service interface contract
- **ServicePort** (Port) - Service interaction point
- **ServiceFunction** (Activity) - Service behavior

**Dependency Elements:**
- **OperationalPerformer** (Class) - Logical operational agent
- **CapabilityConfiguration** (Class) - Resource assembly for capability
- **ResourceArchitecture** (Class) - Resource architecture model
- **ResourceInterface** (Class) - Resource interface specification
- **System** (Class) - Integrated system
- **Software** (Class) - Software artifact
- **ResourceArtifact** (Class) - Man-made resource object
- **NaturalResource** (Class) - Natural resource
- **Organization** (Class) - Organization type
- **Person** (Class) - Person type
- **Post** (Class) - Post/role type

**Policy and Measurement:** (Same as S1)

### S3 - Service Interfaces
**Interface Elements:**
- **ServiceSpecification** (Class) - Service specification
- **ServiceInterface** (Class) - Service interface contract
- **ServicePort** (Port) - Service interaction point
- **DataElement** (Class) - Data structure definition
- **DataRole** (Part) - Data usage in context

**Policy Elements:** (Same as S1)

### S4 - Service Functions
**Function Elements:**
- **ServiceSpecification** (Class) - Service specification
- **ServiceSpecificationRole** (Part) - Service role
- **ServiceFunction** (Activity) - Service behavior function
- **ServiceFunctionAction** (Action) - Service function invocation

**Policy Elements:** (Same as S1)

### S5 - Service States
**State Elements:**
- **ServiceSpecification** (Class) - Service specification
- **ServiceStateDescription** (StateMachine) - Service state machine

**Policy Elements:** (Same as S1)

### S6 - Service Interactions
**Interaction Elements:**
- **ServiceSpecificationRole** (Part) - Service role in interaction
- **ServiceMessage** (Message) - Service interaction message
- **OperationalRole** (Part) - Operational role
- **OperationalMessage** (Message) - Operational message
- **ResourceRole** (Part) - Resource role
- **ResourceMessage** (Message) - Resource message

**Supporting Elements:** (Standard, Finding, Recommendation, Stakeholders)

### S7 - Service Interface Parameters
**Interface Parameter Elements:**
- **ServiceSpecification** (Class) - Service specification
- **ServiceInterface** (Class) - Service interface
- **ServiceFunction** (Activity) - Service function

**Policy Elements:** (Same as S1)

### S8 - Service Policy
**Policy Elements:**
- **ServicePolicy** (Class) - Service constraint
- **Classification** (Class) - Security classification
- **Reference** (Class) - General reference
- **DocumentReference** (Class) - Document reference
- **SMEReference** (Class) - Expert reference

**Constraint Elements:**
- **StrategicConstraint** (Class) - Capability-level constraint
- **OperationalConstraint** (Class) - Operational constraint
- **ResourceConstraint** (Class) - Implementation constraint

**Measurement Elements:** (Same as S1)

### Sr - Service Roadmap
**Service Elements:**
- **ServiceSpecification** (Class) - Service type
- **ActualService** (Object) - Service instance
- **ProvidedServiceLevel** (Object) - Provided service level
- **RequiredServiceLevel** (Object) - Required service level

**Project Elements:**
- **Project** (Class) - Project type
- **ProjectMilestone** (Class) - Milestone type
- **ProjectMilestoneRole** (Part) - Milestone role
- **ActualProject** (Object) - Specific project instance
- **ActualProjectMilestone** (Object) - Specific milestone instance

**Supporting Elements:** (Standard, Finding, Recommendation, Stakeholders)

## Association Stereotypes by Viewpoint

### S1 Associations
- **ServiceClassification** (Dependency) - Taxonomic service relationship
- **ServiceSpecificationGeneralization** (Generalization) - Service taxonomy hierarchy
- **ConformsTo** (Dependency) - Conforms to standard
- **JustifiedBy** (Dependency) - Constraint justified by reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **Classified** (Dependency) - Element classification
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - General reference
- **ResultsFrom** (Dependency) - Results from finding
- **StakeholderConcern** (Dependency) - Stakeholder concern relationship
- **EnvironmentalContext** (Dependency) - Measurement context
- **OwnsMeasurement** (Dependency) - Owns measurement

### S2 Associations
- **ServiceDependency** (Dependency) - Service depends on service/node/resource
- **IsCapableToPerform** (Abstraction) - Performs activity/action
- **ProvidesServiceFunction** (Dependency) - Interface provides function
- **IsAccountableFor** (Dependency) - Accountable for resource/service/project
- **IsResponsibleFor** (Dependency) - Responsible for resource/service/project
- **ConformsTo** (Dependency) - Conforms to standard
- **JustifiedBy** (Dependency) - Constraint justified by reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **Classified** (Dependency) - Element classification
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - General reference
- **ResultsFrom** (Dependency) - Results from finding
- **StakeholderConcern** (Dependency) - Stakeholder concern relationship
- **EnvironmentalContext** (Dependency) - Measurement context
- **OwnsMeasurement** (Dependency) - Owns measurement

### S3 Associations
- **ServiceConnector** (Connector) - Channel between services
- **ConformsTo** (Dependency) - Conforms to standard
- **JustifiedBy** (Dependency) - Constraint justified by reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **Classified** (Dependency) - Element classification
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - General reference
- **ResultsFrom** (Dependency) - Results from finding
- **StakeholderConcern** (Dependency) - Stakeholder concern relationship

### S4 Associations
- **IsCapableToPerform** (Abstraction) - Performs activity/action
- **PerformsInContext** (Abstraction) - Role performs activity in context
- **ConformsTo** (Dependency) - Conforms to standard
- **JustifiedBy** (Dependency) - Constraint justified by reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **Classified** (Dependency) - Element classification
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - General reference
- **ResultsFrom** (Dependency) - Results from finding
- **StakeholderConcern** (Dependency) - Stakeholder concern relationship

### S5 Associations
- **ConformsTo** (Dependency) - Conforms to standard
- **JustifiedBy** (Dependency) - Constraint justified by reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **Classified** (Dependency) - Element classification
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - General reference
- **ResultsFrom** (Dependency) - Results from finding
- **StakeholderConcern** (Dependency) - Stakeholder concern relationship

### S6 Associations
- **ConformsTo** (Dependency) - Conforms to standard
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - General reference
- **ResultsFrom** (Dependency) - Results from finding
- **StakeholderConcern** (Dependency) - Stakeholder concern relationship

### S7 Associations
- **ProvidesServiceFunction** (Dependency) - Interface provides function
- **ConformsTo** (Dependency) - Conforms to standard
- **JustifiedBy** (Dependency) - Constraint justified by reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **Classified** (Dependency) - Element classification
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - General reference
- **ResultsFrom** (Dependency) - Results from finding
- **StakeholderConcern** (Dependency) - Stakeholder concern relationship

### S8 Associations
- **Implements** (Abstraction) - Implements constraint
- **JustifiedBy** (Dependency) - Constraint justified by reference
- **OriginatesFrom** (Dependency) - Derived from reference
- **Satisfy** (Dependency) - Constraint affects element
- **Classified** (Dependency) - Element classification
- **ConformsTo** (Dependency) - Conforms to standard
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - General reference
- **ResultsFrom** (Dependency) - Results from finding
- **StakeholderConcern** (Dependency) - Stakeholder concern relationship
- **EnvironmentalContext** (Dependency) - Measurement context
- **OwnsMeasurement** (Dependency) - Owns measurement

### Sr Associations
- **NeedsService** (Dependency) - Project needs service
- **ActualProjectDependency** (Dependency) - Project depends on project
- **ProjectSequence** (Dependency) - Project follows project
- **MilestoneDependency** (Dependency) - Milestone follows milestone
- **OwnedMilestone** (Dependency) - Project owns milestone
- **ProjectMilestoneToProjectTheme** (Dependency) - Milestone handles theme
- **RequiredResource** (Dependency) - Milestone requires resource
- **VersionReleased** (Dependency) - Milestone releases version
- **VersionWithdrawn** (Dependency) - Milestone withdraws version
- **IsAccountableFor** (Dependency) - Accountable for project
- **IsResponsibleFor** (Dependency) - Responsible for project
- **ConformsTo** (Dependency) - Conforms to standard
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - General reference
- **ResultsFrom** (Dependency) - Results from finding
- **StakeholderConcern** (Dependency) - Stakeholder concern relationship

## Common Aliases and Natural Language Mappings

### Element Types (Casual → Formal)
- "service" / "service specification" → ServiceSpecification
- "service interface" / "interface" → ServiceInterface
- "service port" / "port" → ServicePort
- "service function" / "function" → ServiceFunction
- "service role" → ServiceSpecificationRole
- "service policy" / "policy" / "constraint" → ServicePolicy
- "service state" / "state machine" → ServiceStateDescription
- "service message" / "message" → ServiceMessage
- "service action" → ServiceFunctionAction
- "service connector" → ServiceConnector
- "actual service" / "service instance" → ActualService
- "service level" → ProvidedServiceLevel or RequiredServiceLevel
- "data element" / "data" → DataElement
- "data role" → DataRole
- "standard" / "norm" → Standard
- "reference" / "document" → Reference or DocumentReference
- "expert reference" / "SME" → SMEReference
- "finding" → Finding
- "recommendation" → Recommendation
- "classification" → Classification
- "concern" → Concern
- "measurement" → Measurement or MeasurementType
- "condition" → ActualCondition
- "environment" → ActualEnvironment
- "location" → ActualLocation
- "project" → Project or ActualProject
- "milestone" → ProjectMilestone or ActualProjectMilestone
- "organization" → Organization or ActualOrganization
- "person" → Person or ActualPerson
- "post" / "role" → Post or ActualPost
- "operational performer" / "operational agent" → OperationalPerformer
- "system" → System
- "software" → Software
- "resource" → ResourceArtifact or NaturalResource
- "capability configuration" → CapabilityConfiguration
- "strategic constraint" → StrategicConstraint
- "operational constraint" → OperationalConstraint
- "resource constraint" → ResourceConstraint

### Association Types (Casual → Formal)
- "classifies" / "taxonomy" → ServiceClassification
- "specializes" / "is a" → ServiceSpecificationGeneralization
- "depends on" → ServiceDependency
- "capable to perform" / "performs" → IsCapableToPerform
- "performs in context" → PerformsInContext
- "provides function" → ProvidesServiceFunction
- "connects to" → ServiceConnector
- "conforms to" / "complies with" → ConformsTo
- "justified by" / "based on" → JustifiedBy
- "originates from" / "derived from" → OriginatesFrom
- "satisfies" / "affects" → Satisfy
- "classified as" → Classified
- "realizes recommendation" / "implements recommendation" → RealizesRecommendation
- "refers to" → RefersTo
- "results from" → ResultsFrom
- "stakeholder concern" → StakeholderConcern
- "environmental context" / "context" → EnvironmentalContext
- "owns measurement" / "has measurement" → OwnsMeasurement
- "accountable for" → IsAccountableFor
- "responsible for" → IsResponsibleFor
- "implements" / "implements constraint" → Implements
- "needs service" / "requires service" → NeedsService
- "project dependency" → ActualProjectDependency
- "project sequence" / "follows" → ProjectSequence
- "milestone dependency" → MilestoneDependency
- "owned milestone" / "has milestone" → OwnedMilestone
- "milestone theme" → ProjectMilestoneToProjectTheme
- "required resource" / "requires resource" → RequiredResource
- "version released" / "releases" → VersionReleased
- "version withdrawn" / "withdraws" → VersionWithdrawn

## Profile Information
All elements and associations use profile: **NAFv4-ADMBw**
