# NAF v4 Viewpoint Overview

Quick reference for all NAF v4 / ADMBw viewpoints across all categories.

## All Viewpoints by Category

### Requirements (R) - nafv4-requirements

| ID | Name | Purpose |
|----|------|---------|
| R2 | Requirement Catalogue | Organize requirements in categories |
| R3 | Requirement Dependencies | Show relationships between requirements |
| R4 | Requirement Conformance | Link requirements to standards |
| R5 | Requirement Derivation | Trace requirement origins |
| R6 | Requirement Realization | Map to implementing elements |

### Architecture Metadata (A) - nafv4-architecture-metadata

| ID | Name | Purpose |
|----|------|---------|
| A1 | Meta-Data Definitions | Architecture meta-data tags for discovery |
| A2 | Architecture Products | Structure and products of architecture |
| A3 | Architecture Correspondence | Architecture correspondence and rules |
| A4 | Methodology Used | Architecting methodology |
| A5 | Architecture Status | Version numbers and approval status |
| A6 | Architecture Version | Complete architecture history |
| A7 | Architecture Compliance | Overall architecture meta-data |
| A8 | Standards | Technical and non-technical standards |
| Ar | Architecture Roadmap | Architecture project history and future |

### Concepts (C) - nafv4-concepts

| ID | Name | Purpose |
|----|------|---------|
| C1 | Capability Taxonomy | All capabilities with MoEs in taxonomies |
| C2 | Enterprise Vision | Strategic context and scope for capabilities |
| C3 | Capability Dependencies | Analyze dependencies between capabilities |
| C4 | Standard Processes | Standard operational activities for reuse |
| C5 | Effects | Operational effect of capabilities and activities |
| C7 | Performance Parameters | Capability requirements as MoEs |
| C8 | Planning Assumptions | Assumptions for capability implementation |
| Cr | Capability Roadmap | Capability audit, gaps, and delivery milestones |

### Logical Specification (L) - nafv4-logical-specification

| ID | Name | Purpose |
|----|------|---------|
| L1 | Node Types | Define logical nodes with performance measures |
| L2 | Logical Scenario | Nodes in context with information/resource flows |
| L3 | Node Interactions | Interoperability requirements and logical flows |
| L4 | Logical Activities | Operational activities at logical level |
| L5 | Logical States | Node states and transitions |
| L6 | Logical Sequence | Event sequences between nodes |
| L7 | Information Model | Business information exchanged along flows |
| L8 | Logical Constraints | Constrain logical architecture |
| Lr | Lines of Development | Acquisition support with capability dependencies |

### Physical Resources (P) - nafv4-physical-resources

| ID | Name | Purpose |
|----|------|---------|
| P1 | Resource Types | Catalog resource types with performance |
| P2 | Resource Structure | How resources realize logical architecture |
| P3 | Resource Connectivity | Networks and physical pathways |
| P4 | Resource Functions | Function allocation to resources |
| P5 | Resource States | Resource states and transitions |
| P6 | Resource Sequence | Sequence of functions and interactions |
| P7 | Data Model | Physical implementation of logical data |
| P8 | Resource Constraints | Constraints on resources and communications |
| Pr | Configuration Management | Track resource asset changes over time |

### Service Specification (S) - nafv4-service-specification

| ID | Name | Purpose |
|----|------|---------|
| S1 | Service Taxonomy | Governance structure for SOA specifications |
| S2 | Service Structure | Service composition and dependencies |
| S3 | Service Interfaces | Identify and define service interfaces |
| S4 | Service Functions | Behavioral functions of services |
| S5 | Service States | Allowable states and transitions |
| S6 | Service Interactions | Interactions between services |
| S7 | Service Interface Parameters | Interface compatibility |
| S8 | Service Policy | Constraints on service implementations |
| Sr | Service Roadmap | Service lifecycle and evolution |

## Viewpoint Selection Guide

### By Architecture Layer

**Strategic/Capability Layer:**
- C1-C8, Cr (Concepts)
- R2-R6 (Requirements)

**Logical/Design Layer:**
- L1-L8, Lr (Logical Specification)
- S1-S8, Sr (Service Specification)

**Physical/Implementation Layer:**
- P1-P8, Pr (Physical Resources)

**Meta/Governance Layer:**
- A1-A8, Ar (Architecture Metadata)

### By Typical Usage

**Planning & Strategy:**
- C2 (Enterprise Vision)
- C1 (Capability Taxonomy)
- Cr (Capability Roadmap)

**Requirements Management:**
- R2 (Requirement Catalogue)
- R3 (Requirement Dependencies)
- R5 (Requirement Derivation)
- R6 (Requirement Realization)

**Logical Design:**
- L1 (Node Types)
- L2 (Logical Scenario)
- L4 (Logical Activities)

**Service Design:**
- S1 (Service Taxonomy)
- S2 (Service Structure)
- S3 (Service Interfaces)

**System Implementation:**
- P1 (Resource Types)
- P2 (Resource Structure)
- P3 (Resource Connectivity)

**Architecture Documentation:**
- A1 (Meta-Data)
- A2 (Architecture Products)
- A8 (Standards)

**Project Planning:**
- Ar (Architecture Roadmap)
- Cr (Capability Roadmap)
- Lr (Lines of Development)
- Pr (Configuration Management)
- Sr (Service Roadmap)

## Common Cross-Viewpoint Relationships

### Requirements ↔ Capabilities
- R2 FunctionalRequirement → C1 Capability (MapsToCapability)
- R5 BWRequirement → C1 Capability (DerivedFrom)

### Capabilities ↔ Logical
- C1 Capability → L1 OperationalPerformer (Exhibits)
- C1 Capability → L4 OperationalActivity (MapsToCapability)

### Capabilities ↔ Services
- C1 Capability → S2 ServiceSpecification (Consumes, Provides)

### Capabilities ↔ Physical
- C1 Capability → P1 CapabilityConfiguration (Exhibits)

### Logical ↔ Services
- L4 OperationalActivity → S4 ServiceFunction (ActivitySupportsService)
- L2 OperationalPerformer → S2 ServiceSpecification (Consumes)

### Logical ↔ Physical
- L1 OperationalPerformer → P1 System (Implements)
- L4 OperationalActivity → P4 Function (Implements)
- L2 OperationalRole → P2 ResourceRole (Implements)

### Services ↔ Physical
- S2 ServiceSpecification → P1 System (ServiceProvision)
- S4 ServiceFunction → P4 Function (Implements)

### Requirements ↔ Physical
- R6 FunctionalRequirement → P1 System (RealiseRequirement, ToBeRealizedBy)

## Diagram Types

### Custom Diagrams (Diagram_Custom)
Most viewpoints use this type:
- All R viewpoints (R2-R6)
- All A viewpoints (A1-A8, Ar)
- All C viewpoints (C1-C8, Cr)
- L1, L2, L3, L4, L5, L7, L8, Lr
- P1, P2, P3, P4, P5, P7, P8, Pr
- S1, S2, S3, S4, S5, S7, S8, Sr

### Sequence Diagrams (Diagram_Sequence)
Only three viewpoints use this type:
- L6 (Logical Sequence)
- P6 (Resource Sequence)
- S6 (Service Interactions)

## Profile

All NAF v4 / ADMBw elements use profile: **NAFv4-ADMBw**
