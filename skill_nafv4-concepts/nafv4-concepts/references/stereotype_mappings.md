# NAF v4 Concepts - Stereotype Mappings

This reference provides quick lookup tables for stereotypes, UML types, and valid connections in NAF v4 Concepts Viewpoints.

## Viewpoints Overview

| Viewpoint | Identifier | Purpose |
|-----------|------------|---------|
| Capability Taxonomy | C1 | Organize capabilities in taxonomies with measures of effectiveness |
| Enterprise Vision | C2 | Provide strategic context for capabilities and architecture scope |
| Capability Dependencies | C3 | Analyze dependencies between capabilities and capability clusters |
| Standard Processes | C4 | Specify standard operational activities for reuse across architectures |
| Effects | C5 | Describe operational effects of capabilities, activities and services |
| Performance Parameters | C7 | Express capability requirements using measures of effectiveness |
| Planning Assumptions | C8 | Identify and describe assumptions for capability implementation |
| Capability Roadmap | Cr | Identify capability gaps and duplications through capability audit |

## Element Stereotypes by Viewpoint

### C1 - Capability Taxonomy
- **Capability** (Class) - High level specification of enterprise's ability to execute a course of action
- **ActualCondition** (Object) - Actual situation regarding circumstances under which activities can be performed
- **ActualEnvironment** (Object) - Actual state describing circumstances of an environment
- **ActualLocation** (Object) - Actual state describing a physical location
- **Measurement** (Part) - Property representing something in physical world in units of measure
- **MeasurementType** (Class) - Type of property representing something in physical world
- **Classification** (Class) - Classification according to STANAG 1059
- **DocumentReference** (Class) - Regulation, instruction or general document
- **Reference** (Class) - All types of references
- **SMEReference** (Class) - Workshop result or expert knowledge
- **StrategicConstraint** (Class) - Rule governing a capability
- **Standard** (Class) - Ratified and peer-reviewed specification
- **Finding** (Class) - Ascertainment made in the model
- **Recommendation** (Class) - Need for action from a finding
- **ActualOrganization** (Object) - Actual formal or informal organizational unit
- **ActualPerson** (Object) - Individual human being
- **ActualPost** (Object) - Actual specific post instance
- **ActualProject** (Object) - Time-limited endeavor to provide resources
- **Concern** (Class) - Stakeholder interest in enterprise phase
- **Organization** (Class) - Group of organizational resources
- **Person** (Class) - Type of human being
- **Post** (Class) - Type of job title or position
- **Project** (Class) - Type of time-limited endeavor

### C2 - Enterprise Vision
- **ActualEnduringTask** (Object) - Actual undertaking essential to achieving enterprise goals
- **EnduringTask** (Class) - Template behavior essential to achieving goals
- **ActualEnterprisePhase** (Object) - Actual state describing phase of enterprise endeavor
- **EnterpriseGoal** (Class) - Statement about enterprise state to be achieved or sustained
- **EnterprisePhase** (Class) - Current or future state of enterprise
- **EnterpriseVision** (Class) - Future state of enterprise without regard to how it's achieved
- **OperationalActivity** (Activity) - Logical process specified independently of how it's carried out
- **OperationalArchitecture** (Class) - Model of architecture from operational perspective
- **OperationalPerformer** (Class) - Logical entity capable of performing operational activities
- **ResourceArchitecture** (Class) - Model of architecture from resource performer perspective
- **ServiceSpecification** (Class) - Specification of functionality provided for use by others
- **TemporalPart** (Part) - Current or future state of enterprise
- **WholeLifeEnterprise** (Class) - Purposeful endeavor involving people, organizations and systems
- **Capability** (Class) - High level specification of enterprise's ability
- **Environment** (Class) - Definition of environmental factors
- **Classification** (Class) - Classification according to STANAG 1059
- **DocumentReference** (Class) - Regulation, instruction or general document
- **Reference** (Class) - All types of references
- **SMEReference** (Class) - Workshop result or expert knowledge
- **StrategicConstraint** (Class) - Rule governing a capability
- **Standard** (Class) - Ratified and peer-reviewed specification
- **Finding** (Class) - Ascertainment made in the model
- **Recommendation** (Class) - Need for action from a finding
- **ActualOrganization** (Object) - Actual organizational unit
- **ActualPerson** (Object) - Individual human being
- **ActualPost** (Object) - Actual specific post instance
- **ActualProject** (Object) - Time-limited endeavor to provide resources
- **Concern** (Class) - Stakeholder interest
- **Organization** (Class) - Group of organizational resources
- **Person** (Class) - Type of human being
- **Post** (Class) - Type of job title or position
- **Project** (Class) - Type of time-limited endeavor

### C3 - Capability Dependencies
- **Capability** (Class) - High level specification of enterprise's ability
- **CapabilityRole** (Part) - High level specification of enterprise's ability in a specific role
- **Classification** (Class) - Classification according to STANAG 1059
- **DocumentReference** (Class) - Regulation, instruction or general document
- **Reference** (Class) - All types of references
- **SMEReference** (Class) - Workshop result or expert knowledge
- **StrategicConstraint** (Class) - Rule governing a capability
- **Standard** (Class) - Ratified and peer-reviewed specification
- **Finding** (Class) - Ascertainment made in the model
- **Recommendation** (Class) - Need for action from a finding
- **ActualOrganization** (Object) - Actual organizational unit
- **ActualPerson** (Object) - Individual human being
- **ActualPost** (Object) - Actual specific post instance
- **ActualProject** (Object) - Time-limited endeavor to provide resources
- **Concern** (Class) - Stakeholder interest
- **Organization** (Class) - Group of organizational resources
- **Person** (Class) - Type of human being
- **Post** (Class) - Type of job title or position
- **Project** (Class) - Type of time-limited endeavor

### C4 - Standard Processes
- **Capability** (Class) - High level specification of enterprise's ability
- **StandardOperationalActivity** (Activity) - Standard operating procedure
- **ActualEnduringTask** (Object) - Actual undertaking essential to goals
- **EnduringTask** (Class) - Template behavior essential to goals
- **Classification** (Class) - Classification according to STANAG 1059
- **DocumentReference** (Class) - Regulation, instruction or general document
- **Reference** (Class) - All types of references
- **SMEReference** (Class) - Workshop result or expert knowledge
- **StrategicConstraint** (Class) - Rule governing a capability
- **Standard** (Class) - Ratified and peer-reviewed specification
- **Finding** (Class) - Ascertainment made in the model
- **Recommendation** (Class) - Need for action from a finding
- **ActualOrganization** (Object) - Actual organizational unit
- **ActualPerson** (Object) - Individual human being
- **ActualPost** (Object) - Actual specific post instance
- **ActualProject** (Object) - Time-limited endeavor to provide resources
- **Concern** (Class) - Stakeholder interest
- **Organization** (Class) - Group of organizational resources
- **Person** (Class) - Type of human being
- **Post** (Class) - Type of job title or position
- **Project** (Class) - Type of time-limited endeavor

### C5 - Effects
- **Capability** (Class) - High level specification of enterprise's ability
- **ActualCondition** (Object) - Actual situation regarding circumstances
- **ActualEnduringTask** (Object) - Actual undertaking essential to goals
- **ActualEnterprisePhase** (Object) - Actual state of enterprise phase
- **ActualMeasurementSet** (Object) - Set of actual measurements
- **ActualProjectMilestone** (Object) - Event with start date in project
- **ActualPropertySet** (Object) - Set or collection of actual properties
- **ActualResource** (Object) - Role in organization with authority to undertake function
- **Environment** (Class) - Definition of environmental factors
- **ActualOrganization** (Object) - Actual organizational unit
- **ActualPerson** (Object) - Individual human being
- **ActualPost** (Object) - Actual specific post instance
- **FieldedCapability** (Object) - Individual fully-realized capability
- **CapabilityConfiguration** (Class) - Composite structure of physical and human resources
- **Organization** (Class) - Group of organizational resources
- **Person** (Class) - Type of human being
- **Post** (Class) - Type of job title or position
- **ServiceSpecification** (Class) - Specification of functionality
- **StandardOperationalActivity** (Activity) - Standard operating procedure
- **Classification** (Class) - Classification according to STANAG 1059
- **DocumentReference** (Class) - Regulation, instruction or general document
- **Reference** (Class) - All types of references
- **SMEReference** (Class) - Workshop result or expert knowledge
- **StrategicConstraint** (Class) - Rule governing a capability
- **Standard** (Class) - Ratified and peer-reviewed specification
- **Finding** (Class) - Ascertainment made in the model
- **Recommendation** (Class) - Need for action from a finding
- **ActualProject** (Object) - Time-limited endeavor to provide resources
- **Concern** (Class) - Stakeholder interest
- **Project** (Class) - Type of time-limited endeavor

### C7 - Performance Parameters
- **ActualCondition** (Object) - Actual situation regarding circumstances
- **ActualEnvironment** (Object) - Actual state describing environment
- **ActualLocation** (Object) - Actual state describing physical location
- **Capability** (Class) - High level specification of enterprise's ability
- **Measurement** (Part) - Property representing something in physical world
- **MeasurementType** (Class) - Type of property representing something in physical world
- **Classification** (Class) - Classification according to STANAG 1059
- **DocumentReference** (Class) - Regulation, instruction or general document
- **Reference** (Class) - All types of references
- **SMEReference** (Class) - Workshop result or expert knowledge
- **StrategicConstraint** (Class) - Rule governing a capability
- **Standard** (Class) - Ratified and peer-reviewed specification
- **Finding** (Class) - Ascertainment made in the model
- **Recommendation** (Class) - Need for action from a finding
- **ActualOrganization** (Object) - Actual organizational unit
- **ActualPerson** (Object) - Individual human being
- **ActualPost** (Object) - Actual specific post instance
- **ActualProject** (Object) - Time-limited endeavor to provide resources
- **Concern** (Class) - Stakeholder interest
- **Organization** (Class) - Group of organizational resources
- **Person** (Class) - Type of human being
- **Post** (Class) - Type of job title or position
- **Project** (Class) - Type of time-limited endeavor

### C8 - Planning Assumptions
- **Classification** (Class) - Classification according to STANAG 1059
- **DocumentReference** (Class) - Regulation, instruction or general document
- **Reference** (Class) - All types of references
- **SMEReference** (Class) - Workshop result or expert knowledge
- **StrategicConstraint** (Class) - Rule governing a capability
- **OperationalConstraint** (Class) - Rule governing logical architectural elements
- **ResourceConstraint** (Class) - Rule governing structural or functional aspects
- **ServicePolicy** (Class) - Constraint governing use of service specifications
- **Standard** (Class) - Ratified and peer-reviewed specification
- **Finding** (Class) - Ascertainment made in the model
- **Recommendation** (Class) - Need for action from a finding
- **ActualOrganization** (Object) - Actual organizational unit
- **ActualPerson** (Object) - Individual human being
- **ActualPost** (Object) - Actual specific post instance
- **ActualProject** (Object) - Time-limited endeavor to provide resources
- **Concern** (Class) - Stakeholder interest
- **Organization** (Class) - Group of organizational resources
- **Person** (Class) - Type of human being
- **Post** (Class) - Type of job title or position
- **Project** (Class) - Type of time-limited endeavor

### Cr - Capability Roadmap
- **Capability** (Class) - High level specification of enterprise's ability
- **CapabilityConfiguration** (Class) - Composite structure of physical and human resources
- **Environment** (Class) - Definition of environmental factors
- **FieldedCapability** (Object) - Individual fully-realized capability
- **ActualProject** (Object) - Time-limited endeavor to provide resources
- **ActualProjectMilestone** (Object) - Event with start date in project
- **Project** (Class) - Type of time-limited endeavor
- **ProjectMilestone** (Class) - Type of event in project by which progress is measured
- **ProjectMilestoneRole** (Part) - Role played by project milestone in context of project
- **Standard** (Class) - Ratified and peer-reviewed specification
- **Finding** (Class) - Ascertainment made in the model
- **Recommendation** (Class) - Need for action from a finding
- **ActualOrganization** (Object) - Actual organizational unit
- **ActualPerson** (Object) - Individual human being
- **ActualPost** (Object) - Actual specific post instance
- **Concern** (Class) - Stakeholder interest
- **Organization** (Class) - Group of organizational resources
- **Person** (Class) - Type of human being
- **Post** (Class) - Type of job title or position

## Association Stereotypes by Viewpoint

### C1 Associations
- **CapabilityGeneralization** (Generalization) - Taxonomic relationship between general and specific capability
- **EnvironmentalContext** (Dependency) - Indicates under which condition a measurement counts
- **OwnsMeasurement** (Dependency) - Expresses which measurement or type an element owns
- **Classified** (Dependency) - Indicates which classification an element has
- **JustifiedBy** (Dependency) - Constraint is derived from a reference
- **OriginatesFrom** (Dependency) - Element in model derives from a reference
- **Satisfy** (Dependency) - Constraint affects an element
- **ConformsTo** (Dependency) - Element conforms to a standard
- **RealizesRecommendation** (Realization) - Recommendation is realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Expresses which concern a stakeholder has

### C2 Associations
- **CapabilityForTask** (Abstraction) - Capability required for enterprise to conduct task phase
- **StatementTask** (Dependency) - Actual enterprise phase fulfills actual enduring task
- **AlignsWithGoal** (Dependency) - Element is aligned with a goal
- **GoalForActualEnterprisePhase** (Dependency) - Actual enterprise phase implements enterprise goal
- **OperationalArchitectureOfEnterprisePhase** (Dependency) - Operational architecture valid in enterprise phase
- **VisionForActualEnterprisePhase** (Dependency) - Actual enterprise phase implements enterprise vision
- **EnvironmentalCondition** (Dependency) - Indicates environment for exhibits relationship
- **Exhibits** (Abstraction) - Capable element meets capability under environmental conditions
- **Classified** (Dependency) - Indicates which classification an element has
- **JustifiedBy** (Dependency) - Constraint is derived from a reference
- **OriginatesFrom** (Dependency) - Element in model derives from a reference
- **Satisfy** (Dependency) - Constraint affects an element
- **ConformsTo** (Dependency) - Element conforms to a standard
- **PhysicalArchitectureOfEnterprisePhase** (Dependency) - Actual enterprise phase has resource architectures
- **RealizesRecommendation** (Realization) - Recommendation is realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Expresses which concern a stakeholder has

### C3 Associations
- **CapabilityDependency** (Dependency) - One capability is dependent on another
- **CapabilityRoleDependency** (Dependency) - One capability role is dependent on another
- **Classified** (Dependency) - Indicates which classification an element has
- **JustifiedBy** (Dependency) - Constraint is derived from a reference
- **OriginatesFrom** (Dependency) - Element in model derives from a reference
- **Satisfy** (Dependency) - Constraint affects an element
- **ConformsTo** (Dependency) - Element conforms to a standard
- **RealizesRecommendation** (Realization) - Recommendation is realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Expresses which concern a stakeholder has

### C4 Associations
- **MapsToCapability** (Abstraction) - Activity contributes to providing a capability
- **CapabilityForTask** (Abstraction) - Capability required for enterprise to conduct task phase
- **Classified** (Dependency) - Indicates which classification an element has
- **JustifiedBy** (Dependency) - Constraint is derived from a reference
- **OriginatesFrom** (Dependency) - Element in model derives from a reference
- **Satisfy** (Dependency) - Constraint affects an element
- **ConformsTo** (Dependency) - Element conforms to a standard
- **RealizesRecommendation** (Realization) - Recommendation is realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Expresses which concern a stakeholder has

### C5 Associations
- **AchievedEffect** (Dependency) - Actual state of element that attempts to achieve desired effect
- **DesiredEffect** (Dependency) - Relates desirer to an actual state
- **EnvironmentalCondition** (Dependency) - Indicates environment for exhibits relationship
- **Exhibits** (Abstraction) - Capable element meets capability under environmental conditions
- **RealizedDesiredEffect** (Dependency) - Connector desired effect that achieved effect realizes
- **RealizingAchievedEffect** (Dependency) - Connector achieved effect that realizes desired effect
- **Classified** (Dependency) - Indicates which classification an element has
- **JustifiedBy** (Dependency) - Constraint is derived from a reference
- **OriginatesFrom** (Dependency) - Element in model derives from a reference
- **Satisfy** (Dependency) - Constraint affects an element
- **ConformsTo** (Dependency) - Element conforms to a standard
- **RealizesRecommendation** (Realization) - Recommendation is realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Expresses which concern a stakeholder has

### C7 Associations
- **EnvironmentalContext** (Dependency) - Indicates under which condition a measurement counts
- **OwnsMeasurement** (Dependency) - Expresses which measurement or type an element owns
- **Classified** (Dependency) - Indicates which classification an element has
- **JustifiedBy** (Dependency) - Constraint is derived from a reference
- **OriginatesFrom** (Dependency) - Element in model derives from a reference
- **Satisfy** (Dependency) - Constraint affects an element
- **ConformsTo** (Dependency) - Element conforms to a standard
- **RealizesRecommendation** (Realization) - Recommendation is realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Expresses which concern a stakeholder has

### C8 Associations
- **Classified** (Dependency) - Indicates which classification an element has
- **JustifiedBy** (Dependency) - Constraint is derived from a reference
- **OriginatesFrom** (Dependency) - Element in model derives from a reference
- **Satisfy** (Dependency) - Constraint affects an element
- **Implements** (Abstraction) - Defines how upper layer element is implemented by lower layer
- **ConformsTo** (Dependency) - Element conforms to a standard
- **RealizesRecommendation** (Realization) - Recommendation is realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Expresses which concern a stakeholder has

### Cr Associations
- **EnvironmentalCondition** (Dependency) - Indicates environment for exhibits relationship
- **Exhibits** (Abstraction) - Capable element meets capability under environmental conditions
- **ActualProjectDependency** (Dependency) - Dependency of actual project on actual project
- **ActualResourceNeededByActualProjectMilestone** (Dependency) - Actual resource needed by milestone
- **ActualResourceToActualProjectMilestone** (Dependency) - Actual resource mapped to milestone
- **MilestoneDependency** (Dependency) - One milestone follows from another
- **OwnedMilestone** (Dependency) - Actual project has actual milestone
- **ProjectMilestoneToProjectTheme** (Dependency) - Project theme handled by milestone
- **ProjectSequence** (Dependency) - One project cannot start before previous finishes
- **RequiredResource** (Dependency) - Indicates which resources a milestone requires
- **VersionReleased** (Dependency) - Actual milestone releases versioned element
- **VersionWithdrawn** (Dependency) - Actual milestone withdraws versioned element
- **ConformsTo** (Dependency) - Element conforms to a standard
- **RealizesRecommendation** (Realization) - Recommendation is realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Expresses which concern a stakeholder has

## Common Aliases and Natural Language Mappings

### Element Types (Casual → Formal)
- "capability" → Capability
- "enterprise vision" → EnterpriseVision
- "enterprise goal" → EnterpriseGoal
- "enterprise phase" → EnterprisePhase
- "enduring task" → EnduringTask
- "operational activity" → OperationalActivity
- "standard operational activity" / "standard process" → StandardOperationalActivity
- "capability configuration" → CapabilityConfiguration
- "fielded capability" → FieldedCapability
- "capability role" → CapabilityRole
- "environment" → Environment
- "measurement" → Measurement
- "measurement type" / "measure of effectiveness" / "MoE" → MeasurementType
- "strategic constraint" → StrategicConstraint
- "operational constraint" → OperationalConstraint
- "resource constraint" → ResourceConstraint
- "service policy" → ServicePolicy
- "standard" / "norm" → Standard
- "reference" / "document" → Reference or DocumentReference
- "SME reference" / "expert knowledge" → SMEReference
- "finding" → Finding
- "recommendation" → Recommendation
- "concern" → Concern
- "organization" → Organization or ActualOrganization
- "person" → Person or ActualPerson
- "post" / "role" → Post or ActualPost
- "project" → Project or ActualProject
- "project milestone" / "milestone" → ProjectMilestone or ActualProjectMilestone
- "operational architecture" → OperationalArchitecture
- "resource architecture" → ResourceArchitecture
- "service specification" / "service" → ServiceSpecification
- "whole life enterprise" → WholeLifeEnterprise

### Association Types (Casual → Formal)
- "generalizes" / "is specialized by" → CapabilityGeneralization
- "depends on" / "dependency" → CapabilityDependency or CapabilityRoleDependency
- "maps to capability" → MapsToCapability
- "exhibits" / "has capability" → Exhibits
- "capability for task" → CapabilityForTask
- "desired effect" → DesiredEffect
- "achieved effect" → AchievedEffect
- "aligns with goal" → AlignsWithGoal
- "conforms to" / "complies with" → ConformsTo
- "originates from" / "derives from" → OriginatesFrom
- "justified by" → JustifiedBy
- "satisfies" / "satisfy" → Satisfy
- "implements" → Implements
- "owns measurement" → OwnsMeasurement
- "environmental context" → EnvironmentalContext
- "environmental condition" → EnvironmentalCondition
- "milestone dependency" → MilestoneDependency
- "project sequence" → ProjectSequence
- "required resource" → RequiredResource
- "version released" → VersionReleased
- "version withdrawn" → VersionWithdrawn
- "realizes recommendation" → RealizesRecommendation
- "refers to" → RefersTo
- "results from" → ResultsFrom
- "stakeholder concern" → StakeholderConcern

## Profile Information
All elements and associations use profile: **NAFv4-ADMBw**
