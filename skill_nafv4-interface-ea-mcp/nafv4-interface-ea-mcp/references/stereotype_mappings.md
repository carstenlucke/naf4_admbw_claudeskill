# NAF v4 Requirements - Stereotype Mappings

This reference provides quick lookup tables for stereotypes, UML types, and valid connections in NAF v4 Requirements Viewpoints.

## Viewpoints Overview

| Viewpoint | Identifier | Purpose |
|-----------|------------|---------|
| Requirement Catalogue | R2 | Catalog requirements in categories |
| Requirement Dependencies | R3 | Show dependencies between requirements |
| Requirement Conformance | R4 | Link requirements to standards |
| Requirement Derivation | R5 | Trace requirement origins and derivations |
| Requirement Realization | R6 | Map requirements to implementing elements |

## Element Stereotypes by Viewpoint

### R2 - Requirement Catalogue
- **FunctionalRequirement** (Requirement) - Functional requirements
- **NonfunctionalRequirement** (Requirement) - Non-functional requirements  
- **RequirementCatalogue** (Class) - Container for requirements
- **RequirementCategory** (Class) - Categorization grouping
- **Standard** (Class) - Standards and norms
- **Finding** (Class) - Assessment findings
- **Recommendation** (Class) - Recommendations from assessments
- **ActualOrganization** (Object) - Specific organization instance
- **ActualPerson** (Object) - Specific person instance
- **ActualPost** (Object) - Specific post/role instance
- **ActualProject** (Object) - Specific project instance
- **Concern** (Class) - Stakeholder concerns
- **Organization** (Class) - Organization type
- **Person** (Class) - Person type
- **Post** (Class) - Post/role type
- **Project** (Class) - Project type

### R3 - Requirement Dependencies
- **FunctionalRequirement** (Requirement)
- **NonfunctionalRequirement** (Requirement)

### R4 - Requirement Conformance
- **FunctionalRequirement** (Requirement)
- **NonfunctionalRequirement** (Requirement)
- **Standard** (Class)

### R5 - Requirement Derivation
- **FunctionalRequirement** (Requirement)
- **NonfunctionalRequirement** (Requirement)
- **BWRequirement** (Requirement) - Generic requirement type
- **Reference** (Class) - Reference document/source
- **DocumentReference** (Class) - Specific document reference
- **SMEReference** (Class) - Subject matter expert reference

### R6 - Requirement Realization
- **FunctionalRequirement** (Requirement)
- **NonfunctionalRequirement** (Requirement)
- **FitCriterion** (Class) - Acceptance criteria
- **FulfilmentCriterion** (Class) - Evaluation criteria

## Association Stereotypes by Viewpoint

### R2 Associations
- **PartOfCatalogue** (Aggregation) - Element belongs to catalogue
- **PartOfCategory** (Aggregation) - Element belongs to category
- **ConformsTo** (Dependency) - Conforms to standard
- **RealizesRecommendation** (Realization) - Implements recommendation
- **RefersTo** (Dependency) - General reference
- **ResultsFrom** (Dependency) - Results from finding
- **StakeholderConcern** (Dependency) - Links stakeholder to concern

### R3 Associations
- **ConflictsWith** (Dependency) - Requirements conflict
- **IsDuplicateOf** (Dependency) - Duplicate requirement
- **Refines** (Dependency) - Refines another requirement
- **SupportsRequirement** (Dependency) - Supports achievement

### R4 Associations
- **ConformsTo** (Dependency) - Conforms to standard

### R5 Associations
- **DerivedFrom** (Dependency) - Derived from source
- **OriginatesFrom** (Dependency) - Originates from reference

### R6 Associations
- **ToBeRealizedBy** (Dependency) - To be implemented by element
- **RealiseRequirement** (Realisation) - Realizes requirement
- **Checks** (Dependency) - FitCriterion checks requirement
- **Evaluates** (Realisation) - FulfilmentCriterion evaluates FitCriterion

## Common Aliases and Natural Language Mappings

### Element Types (Casual → Formal)
- "functional requirement" → FunctionalRequirement
- "non-functional requirement" → NonfunctionalRequirement
- "catalogue" / "catalog" → RequirementCatalogue
- "category" → RequirementCategory
- "standard" / "norm" → Standard
- "finding" → Finding
- "recommendation" → Recommendation
- "concern" → Concern
- "requirement" (generic) → BWRequirement
- "reference" / "document" → Reference or DocumentReference
- "acceptance criterion" → FitCriterion
- "evaluation criterion" → FulfilmentCriterion

### Association Types (Casual → Formal)
- "part of" → PartOfCatalogue or PartOfCategory
- "belongs to" → PartOfCatalogue or PartOfCategory
- "conforms to" / "complies with" → ConformsTo
- "conflicts with" → ConflictsWith
- "duplicate of" / "duplicates" → IsDuplicateOf
- "refines" / "elaborates" → Refines
- "supports" → SupportsRequirement
- "derived from" / "derives from" → DerivedFrom
- "originates from" / "comes from" → OriginatesFrom
- "to be realized by" / "should be realized by" → ToBeRealizedBy
- "realizes" / "implements" → RealiseRequirement
- "realizes recommendation" → RealizesRecommendation
- "checks" / "verifies" → Checks
- "evaluates" / "assesses" → Evaluates
- "refers to" → RefersTo
- "results from" → ResultsFrom

## Profile Information
All elements and associations use profile: **NAFv4-ADMBw**
