# NAF v4 Architecture Metadata - Stereotype Mappings

This reference provides quick lookup tables for stereotypes, UML types, and valid connections in NAF v4 Architecture Foundation/Metadata Viewpoints.

## Viewpoints Overview

| Viewpoint | Identifier | Purpose |
|-----------|------------|---------|
| Meta-Data Definitions | A1 | Define meta-data tags for searching and discovery |
| Architecture Products | A2 | Specify architecture structure and products |
| Architecture Correspondence | A3 | Define relations between architecture descriptions |
| Methodology Used | A4 | Specify methodology for architecting activities |
| Architecture Status | A5 | Track version numbers and approval status |
| Architecture Version | A6 | Show complete architecture history |
| Architecture Compliance | A7 | Specify architecture meta-data compliance |
| Standards | A8 | Define technical and non-technical standards |
| Architecture Roadmap | Ar | Show architecture project history and future direction |

## Element Stereotypes by Viewpoint

### A1 - Meta-Data Definitions
- **ArchitecturalDescription** (Package) - Architecture description work product
- **ArchitectureMetadata** (Note) - Supplemental metadata information
- **Classification** (Class) - Classification according to STANAG 1059
- **ActualProject** (Object) - Specific time-limited endeavor
- **ActualProjectMilestone** (Object) - Event with start date in project
- **Standard** (Class) - Ratified specification for architecture
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation from finding
- **ActualOrganization** (Object) - Specific organization instance
- **ActualPerson** (Object) - Individual human being instance
- **ActualPost** (Object) - Specific post/role instance
- **ActualProject** (Object) - Specific project instance
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Organization type
- **Person** (Class) - Person type
- **Post** (Class) - Post/role type
- **Project** (Class) - Project type

### A2 - Architecture Products
- **Concern** (Class) - Stakeholder interest in enterprise phase
- **View** (Class) - Architecture view expressing the architecture
- **Viewpoint** (Class) - Architecture viewpoint framing concerns
- **ActualOrganization** (Object) - Specific organization instance
- **ActualPerson** (Object) - Individual human being instance
- **ActualPost** (Object) - Specific post/role instance
- **Organization** (Class) - Organization type
- **Person** (Class) - Person type
- **Post** (Class) - Post/role type
- **Responsibility** (Class) - Duty type required of person or organization
- **ActualEnterprisePhase** (Object) - Actual state of enterprise phase
- **EnterprisePhase** (Class) - Current or future state of enterprise
- **WholeLifeEnterprise** (Class) - Purposeful endeavor of any size
- **Standard** (Class) - Ratified specification
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualProject** (Object) - Specific project instance
- **Project** (Class) - Project type

### A3 - Architecture Correspondence
- **ArchitecturalDescription** (Package) - Architecture description work product
- **Standard** (Class) - Ratified specification
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualOrganization** (Object) - Specific organization instance
- **ActualPerson** (Object) - Individual human being instance
- **ActualPost** (Object) - Specific post/role instance
- **ActualProject** (Object) - Specific project instance
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Organization type
- **Person** (Class) - Person type
- **Post** (Class) - Post/role type
- **Project** (Class) - Project type

### A4 - Methodology Used
- **ArchitecturalDescription** (Package) - Architecture description work product
- **ArchitectureMetadata** (Note) - Supplemental metadata information
- **Classification** (Class) - Classification according to STANAG 1059
- **ActualProject** (Object) - Specific time-limited endeavor
- **ActualProjectMilestone** (Object) - Event with start date in project
- **Standard** (Class) - Ratified specification
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualOrganization** (Object) - Specific organization instance
- **ActualPerson** (Object) - Individual human being instance
- **ActualPost** (Object) - Specific post/role instance
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Organization type
- **Person** (Class) - Person type
- **Post** (Class) - Post/role type
- **Project** (Class) - Project type

### A5 - Architecture Status
- **ArchitecturalDescription** (Package) - Architecture description work product
- **ArchitectureMetadata** (Note) - Supplemental metadata information
- **Classification** (Class) - Classification according to STANAG 1059
- **ActualProject** (Object) - Specific time-limited endeavor
- **ActualProjectMilestone** (Object) - Event with start date in project
- **Standard** (Class) - Ratified specification
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualOrganization** (Object) - Specific organization instance
- **ActualPerson** (Object) - Individual human being instance
- **ActualPost** (Object) - Specific post/role instance
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Organization type
- **Person** (Class) - Person type
- **Post** (Class) - Post/role type
- **Project** (Class) - Project type

### A6 - Architecture Version
- **ArchitecturalDescription** (Package) - Architecture description work product
- **Standard** (Class) - Ratified specification
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualOrganization** (Object) - Specific organization instance
- **ActualPerson** (Object) - Individual human being instance
- **ActualPost** (Object) - Specific post/role instance
- **ActualProject** (Object) - Specific project instance
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Organization type
- **Person** (Class) - Person type
- **Post** (Class) - Post/role type
- **Project** (Class) - Project type

### A7 - Architecture Compliance
- **Information** (Note) - Comment describing state of item of interest
- **Standard** (Class) - Ratified specification
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualOrganization** (Object) - Specific organization instance
- **ActualPerson** (Object) - Individual human being instance
- **ActualPost** (Object) - Specific post/role instance
- **ActualProject** (Object) - Specific project instance
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Organization type
- **Person** (Class) - Person type
- **Post** (Class) - Post/role type
- **Project** (Class) - Project type

### A8 - Standards
- **ActualOrganization** (Object) - Specific organization instance
- **Protocol** (Class) - Standard for network communication
- **ProtocolLayer** (Part) - Usage of protocol in context of another protocol
- **Protocolstack** (Class) - Protocol subtype containing protocol layers
- **Standard** (Class) - Ratified specification
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualPerson** (Object) - Individual human being instance
- **ActualPost** (Object) - Specific post/role instance
- **ActualProject** (Object) - Specific project instance
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Organization type
- **Person** (Class) - Person type
- **Post** (Class) - Post/role type
- **Project** (Class) - Project type

### Ar - Architecture Roadmap
- **ArchitecturalDescription** (Package) - Architecture description work product
- **Standard** (Class) - Ratified specification
- **Finding** (Class) - Assessment finding
- **Recommendation** (Class) - Action recommendation
- **ActualOrganization** (Object) - Specific organization instance
- **ActualPerson** (Object) - Individual human being instance
- **ActualPost** (Object) - Specific post/role instance
- **ActualProject** (Object) - Specific project instance
- **Concern** (Class) - Stakeholder concern
- **Organization** (Class) - Organization type
- **Person** (Class) - Person type
- **Post** (Class) - Post/role type
- **Project** (Class) - Project type

## Association Stereotypes by Viewpoint

### A1 Associations
- **Classified** (Dependency) - Indicates element classification
- **DescribedBy** (Dependency) - Architectural description describes architecture
- **Expresses** (Dependency) - Architectural description includes architectures
- **ArchitectureForProject** (Dependency) - Architectural description belongs to project
- **ConformsTo** (Dependency) - Element conforms to standard
- **RealizesRecommendation** (Realization) - Recommendation realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Links stakeholder to concern

### A2 Associations
- **CompliesViewpoint** (Dependency) - View created according to viewpoint
- **ConcernForView** (Dependency) - Concerns covered by view
- **ConcernForViewpoint** (Dependency) - Concerns covered by viewpoint
- **StakeholderConcern** (Dependency) - Stakeholder has concern
- **ViewpointsInArchitecturalDescription** (Dependency) - Architectural description includes viewpoints
- **ViewpointToStakeholder** (Dependency) - Stakeholder needs viewpoint
- **ViewsInArchitecturalDescription** (Dependency) - Architectural description includes views
- **ConformsTo** (Dependency) - Element conforms to standard
- **RealizesRecommendation** (Realization) - Recommendation realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding

### A3 Associations
- **ArchitecturalReference** (Dependency) - One architectural description refers to another
- **ConformsTo** (Dependency) - Element conforms to standard
- **RealizesRecommendation** (Realization) - Recommendation realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Links stakeholder to concern

### A4 Associations
- **Classified** (Dependency) - Indicates element classification
- **DescribedBy** (Dependency) - Architectural description describes architecture
- **Expresses** (Dependency) - Architectural description includes architectures
- **ArchitectureForProject** (Dependency) - Architectural description belongs to project
- **ConformsTo** (Dependency) - Element conforms to standard
- **RealizesRecommendation** (Realization) - Recommendation realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Links stakeholder to concern

### A5 Associations
- **Classified** (Dependency) - Indicates element classification
- **DescribedBy** (Dependency) - Architectural description describes architecture
- **Expresses** (Dependency) - Architectural description includes architectures
- **ArchitectureForProject** (Dependency) - Architectural description belongs to project
- **ConformsTo** (Dependency) - Element conforms to standard
- **RealizesRecommendation** (Realization) - Recommendation realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Links stakeholder to concern

### A6 Associations
- **ArchitecturalSequence** (Dependency) - One architectural description is successor of another
- **ConformsTo** (Dependency) - Element conforms to standard
- **RealizesRecommendation** (Realization) - Recommendation realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Links stakeholder to concern

### A7 Associations
- **SameAs** (Dependency) - Two elements refer to same real-world thing
- **ConformsTo** (Dependency) - Element conforms to standard
- **RealizesRecommendation** (Realization) - Recommendation realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Links stakeholder to concern

### A8 Associations
- **RatifiedStandards** (Dependency) - Organization releases standard
- **ConformsTo** (Dependency) - Element conforms to standard
- **RealizesRecommendation** (Realization) - Recommendation realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Links stakeholder to concern

### Ar Associations
- **ArchitecturalSequence** (Dependency) - One architectural description is successor of another
- **ConformsTo** (Dependency) - Element conforms to standard
- **RealizesRecommendation** (Realization) - Recommendation realized through element
- **RefersTo** (Dependency) - Assigns finding to recommendation
- **ResultsFrom** (Dependency) - Element is reason for finding
- **StakeholderConcern** (Dependency) - Links stakeholder to concern

## Common Aliases and Natural Language Mappings

### Element Types (Casual → Formal)
- "architectural description" / "architecture description" → ArchitecturalDescription
- "architecture metadata" / "metadata" → ArchitectureMetadata
- "classification" → Classification
- "view" → View
- "viewpoint" → Viewpoint
- "concern" → Concern
- "standard" / "norm" → Standard
- "protocol" → Protocol
- "protocol layer" → ProtocolLayer
- "protocol stack" → Protocolstack
- "finding" → Finding
- "recommendation" → Recommendation
- "information" / "note" → Information
- "project" (actual) → ActualProject
- "project milestone" → ActualProjectMilestone
- "enterprise phase" (actual) → ActualEnterprisePhase
- "enterprise phase" → EnterprisePhase
- "whole life enterprise" → WholeLifeEnterprise
- "organization" (actual) → ActualOrganization
- "organization" → Organization
- "person" (actual) → ActualPerson
- "person" → Person
- "post" (actual) / "role" (actual) → ActualPost
- "post" / "role" → Post
- "responsibility" → Responsibility

### Association Types (Casual → Formal)
- "classified as" / "has classification" → Classified
- "described by" → DescribedBy
- "expresses" / "includes architectures" → Expresses
- "architecture for project" / "belongs to project" → ArchitectureForProject
- "complies with viewpoint" / "follows viewpoint" → CompliesViewpoint
- "concern for view" / "view addresses concern" → ConcernForView
- "concern for viewpoint" / "viewpoint frames concern" → ConcernForViewpoint
- "stakeholder concern" / "stakeholder has concern" → StakeholderConcern
- "viewpoints in description" → ViewpointsInArchitecturalDescription
- "viewpoint to stakeholder" / "stakeholder needs viewpoint" → ViewpointToStakeholder
- "views in description" → ViewsInArchitecturalDescription
- "architectural reference" / "refers to architecture" → ArchitecturalReference
- "architectural sequence" / "successor of" / "follows" → ArchitecturalSequence
- "same as" / "equivalent to" → SameAs
- "ratified by" / "organization releases" → RatifiedStandards
- "conforms to" / "complies with" → ConformsTo
- "realizes recommendation" / "implements recommendation" → RealizesRecommendation
- "refers to" → RefersTo
- "results from" / "caused by" → ResultsFrom

## Profile Information
All elements and associations use profile: **NAFv4-ADMBw**
