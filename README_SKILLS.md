# Skill-Übersicht

Dieses Repository sammelt MCP-Skills, die natürliche Sprache mit den NAF v4 / ADMBw Artefakten in Sparx Enterprise Architect verbinden. Jeder Skill befindet sich im Verzeichnis `skill_<name>` und bringt eine eigene `SKILL.md` und Referenzen mit.

## Architektur

Die Skills sind modular nach NAF v4 Viewpoint-Kategorien organisiert:

- **Spezialisierte Skills** - Ein Skill pro Viewpoint-Kategorie (Requirements, Concepts, Logical, Physical, Services, Architecture Metadata)
- **Coordinator Skill** - Routet Anfragen an die spezialisierten Skills und verwaltet cross-viewpoint Beziehungen
- **Progressive Data Loading** - Jeder Skill lädt seine Metadaten bei Bedarf (JSON und MD Referenzen)

## Vorhandene Skills

### `skill_nafv4-assistant`
- **Zweck**: Bietet Bequemlichkeitsfunktionen für NAF v4 / ADMBw Modellierung.
- **Kernfähigkeiten**:
  - Automatisches Routing zu spezialisierten Funktionen basierend auf Kontext/Keywords
  - Requirement Naming: Generierung prägnanter Titel aus ausführlichen Anforderungsbeschreibungen
  - Batch-Operationen für häufige Modellierungsaufgaben
  - Integration mit nafv4-coordinator für alle NAF-Modellierungsoperationen
- **Architektur**: Cascading Skills (Assistant → Coordinator → Specialized Skills)
- **Verfügbare Funktionen**:
  - `functions/requirement-naming.md` - Anforderungsbenennung
  - [Weitere Funktionen werden künftig hinzugefügt]
- **Referenzen**:
  - `references/extended_examples.md` - Erweiterte Beispiele für Requirement Naming

### `skill_nafv4-coordinator`
- **Zweck**: Koordiniert NAF v4 / ADMBw Modellierung über alle Viewpoint-Kategorien hinweg.
- **Kernfähigkeiten**:
  - Erkennung der benötigten Viewpoint-Kategorie
  - Routing zu spezialisierten Skills
  - Verwaltung von cross-viewpoint Beziehungen (z. B. Requirement → Capability, Capability → Service)
  - Hilfestellung bei der Viewpoint-Auswahl
- **Referenzen**:
  - `references/viewpoint_overview.md` - Übersicht aller NAF v4 Viewpoints

### `skill_nafv4-requirements`
- **Zweck**: NAF v4 Requirements Viewpoints (R2-R6) modellieren.
- **Viewpoints**: R2 (Requirement Catalogue), R3 (Requirement Dependencies), R4 (Requirement Conformance), R5 (Requirement Derivation), R6 (Requirement Realization)
- **Kernfähigkeiten**:
  - Anlegen von R2-R6 Diagrammen
  - Erstellen von Requirements (Functional/Nonfunctional, Categories, Standards)
  - Beziehungen (DerivedFrom, PartOfCatalogue, ConformsTo, etc.)
  - Automatische Benennung bei Anforderungen mit Beschreibung
- **Referenzen**:
  - `references/requirement_viewpoints.json`
  - `references/stereotype_mappings.md`

### `skill_nafv4-architecture-metadata`
- **Zweck**: NAF v4 Architecture Metadata Viewpoints (A1-A8, Ar) modellieren.
- **Viewpoints**: A1 (Meta-Data), A2 (Architecture Products), A3 (Capability to Organisational Development Mapping), A4 (Standard Processes), A5 (Architecture Status), A6 (Architecture Versions), A7 (Architecture Compliance), A8 (Architecture Governance), Ar (Roadmap)
- **Kernfähigkeiten**:
  - Dokumentation von Architektur-Metadaten
  - Verwaltung von Architecture Products und Standards
  - Version Control und Compliance Tracking
  - Roadmap Planning
- **Referenzen**:
  - `references/architecture_metadata_viewpoints.json`
  - `references/stereotype_mappings.md`

### `skill_nafv4-concepts`
- **Zweck**: NAF v4 Concepts Viewpoints (C1-C8, Cr) modellieren.
- **Viewpoints**: C1 (Capability Taxonomy), C2 (Enterprise Vision), C3 (Capability Dependencies), C4 (Standard Processes), C5 (Effects), C6 (Capability Parameters), C7 (Capability Assumptions), C8 (Capability Timeline), Cr (Roadmap)
- **Kernfähigkeiten**:
  - Definition von Capabilities und Capability Hierarchies
  - Enterprise Vision und Goals modellieren
  - Capability Dependencies und Effects
  - Measures of Effectiveness (MoE)
- **Referenzen**:
  - `references/concept_viewpoints.json`
  - `references/stereotype_mappings.md`

### `skill_nafv4-logical-specification`
- **Zweck**: NAF v4 Logical Specification Viewpoints (L1-L8, Lr) modellieren.
- **Viewpoints**: L1 (Node Types), L2 (Operational Scenario), L3 (Node Interactions), L4 (Logical Activities), L5 (Operational State), L6 (Operational Sequence), L7 (Information Model), L8 (Constraints), Lr (Lines of Development)
- **Kernfähigkeiten**:
  - Lösungsneutrale Architekturmodellierung
  - Operational Nodes, Activities, States
  - Information Model und Constraints
  - Scenario und Sequence Modelling
- **Referenzen**:
  - `references/logical_specification_viewpoints.json`
  - `references/stereotype_mappings.md`

### `skill_nafv4-physical-resources`
- **Zweck**: NAF v4 Physical Resource Specification Viewpoints (P1-P8, Pr) modellieren.
- **Viewpoints**: P1 (Resource Types), P2 (Resource Structure), P3 (Resource Connectivity), P4 (Resource Functions), P5 (Resource States), P6 (Resource Sequence), P7 (Information Systems Data Model), P8 (Resource Constraints), Pr (Configuration Management)
- **Kernfähigkeiten**:
  - Physische Systeme, Software, Hardware modellieren
  - System Structure und Connectivity
  - Resource States und Functions
  - Configuration Management
- **Referenzen**:
  - `references/physical_resource_specification_viewpoints.json`
  - `references/stereotype_mappings.md`

### `skill_nafv4-service-specification`
- **Zweck**: NAF v4 Service Specification Viewpoints (S1-S8, Sr) modellieren.
- **Viewpoints**: S1 (Service Taxonomy), S2 (Service Definitions), S3 (Service Interfaces), S4 (Service Functions), S5 (Service States), S6 (Service Interactions), S7 (Service Policy), S8 (Service Parameters), Sr (Roadmap)
- **Kernfähigkeiten**:
  - Service-orientierte Architektur modellieren
  - Service Taxonomy und Interfaces
  - Service Functions, States, Interactions
  - Service Policies und Parameters
- **Referenzen**:
  - `references/service_specification_viewpoints.json`
  - `references/stereotype_mappings.md`

## Nutzung

### Einzelne Viewpoint-Kategorie
Wenn du mit einer spezifischen Viewpoint-Kategorie arbeitest, aktiviert sich automatisch der passende Skill:

```
"Create an R2 diagram" → nafv4-requirements
"Define capabilities" → nafv4-concepts
"Model logical nodes" → nafv4-logical-specification
"Add a system" → nafv4-physical-resources
"Create service interface" → nafv4-service-specification
"Document architecture products" → nafv4-architecture-metadata
```

### Cross-Viewpoint Beziehungen
Für Beziehungen zwischen Viewpoint-Kategorien arbeitet der Coordinator:

```
"Link requirement to capability" → nafv4-coordinator
"Map capability to service" → nafv4-coordinator
"Show logical to physical implementation" → nafv4-coordinator
```

### Viewpoint-Auswahl
Wenn unklar ist, welcher Viewpoint benötigt wird:

```
"I need to model constraints" → nafv4-coordinator (bietet Optionen an)
"Help me choose a viewpoint" → nafv4-coordinator
```

## Typischer Workflow

1. **Requirements & Capabilities** (R2, C1) - Was soll das System können?
2. **Logical Design** (L1-L8, S1-S8) - Wie wird es logisch gelöst?
3. **Physical Implementation** (P1-P8) - Welche Systeme setzen es um?
4. **Traceability** (R5, R6) - Wie sind Requirements realisiert?
5. **Documentation** (A1-A8) - Architektur dokumentieren

> Die Skills nutzen progressive data loading: Core workflows sind immer verfügbar, detaillierte Metadaten werden bei Bedarf geladen.
