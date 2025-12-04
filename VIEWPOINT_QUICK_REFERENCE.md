# NAF v4 Viewpoint Quick Reference

Schnellreferenz für alle NAF v4 / ADMBw Viewpoints zur Verwendung mit dem MCP-Server.

## A-Serie: Architecture Foundation

| Code | Name | Verwendung |
|------|------|-----------|
| A1 | Meta-Data Definitions | Meta-Daten, Tags, Klassifikationen |
| A2 | Architecture Products | Architekturstruktur, Views, Viewpoints, Stakeholder |
| A3 | Architecture Correspondence | Beziehungen zwischen Architekturelementen |
| A4 | Methodology Used | Methodik, Prozesse |
| A5 | Architecture Status | Versionen, Genehmigungsstatus |
| A6 | Architecture Version | Versionshistorie |
| A7 | Architecture Compliance | Compliance, Metadaten-Spezifikation |
| A8 | Standards | Technische/nicht-technische Standards, Protokolle |
| Ar | Architecture Roadmap | Projekthistorie, Zukunftsplanung |

## C-Serie: Concept

| Code | Name | Verwendung |
|------|------|-----------|
| C1 | Capability Taxonomy | Fähigkeiten-Taxonomie, Kategorisierung |
| C1-S1 | Capability to Service Mapping | Zuordnung Services ↔ Capabilities |
| C2 | Enterprise Vision | Vision, Ziele, Enterprise-Phasen |
| C3 | Capability Dependencies | Capability-Abhängigkeiten |
| C4 | Standard Processes | Standard-Prozesse, wiederverwendbare Aktivitäten |
| C5 | Effects | Effekte, Auswirkungen, Desired/Achieved Effects |
| C7 | Performance Parameters | Leistungsparameter, Measures of Effectiveness |
| C8 | Planning Assumptions | Planungsannahmen, Constraints |
| Cr | Capability Roadmap | Capability-Roadmap, Gap-Analyse, Projekte |

## S-Serie: Service Specification

| Code | Name | Verwendung |
|------|------|-----------|
| S1 | Service Taxonomy | Service-Taxonomie, SOA-Governance |
| S2 | Service Structure | Service-Komposition, Aggregation |
| S3 | Service Interfaces | Service-Schnittstellen |
| S4 | Service Functions | Service-Funktionen, Verhalten |
| S5 | Service States | Service-Zustände, State Machines |
| S6 | Service Interactions | Service-Sequenzen, Interaktionen |
| S7 | Service Interface Parameters | Schnittstellenparameter, Kompatibilität |
| S8 | Service Policy | Service-Policies, Constraints |
| Sr | Service Roadmap | Service-Roadmap, Gap-Analyse |

## L-Serie: Logical Specification

| Code | Name | Verwendung |
|------|------|-----------|
| L1 | Node Types | Logische Nodes, Operational Performers |
| L2 | Logical Scenario | Szenarien, Use Cases |
| L2-L3 | Logical Concept | Konzept-Überblick, High-Level |
| L3 | Node Interactions | Node-Interaktionen, logische Flows |
| L4 | Logical Activities | Aktivitäten, Activity Diagrams |
| L4-P4 | Activity to Function Mapping | Mapping Activities ↔ Functions |
| L5 | Logical States | Zustände, State Machines (logisch) |
| L6 | Logical Sequence | Sequenzen, Zeitabläufe (logisch) |
| L7 | Information Model | Informationsmodell, Datenstrukturen |
| L8 | Logical Constraints | Logische Constraints, Regeln |
| Lr | Lines of Development | Entwicklungslinien, Projekte |

## P-Serie: Physical Resource Specification

| Code | Name | Verwendung |
|------|------|-----------|
| P1 | Resource Types | Ressourcentypen, Hardware, Software |
| P2 | Resource Structure | Ressourcenstruktur, Komponenten |
| P3 | Resource Connectivity | Netzwerke, physische Verbindungen |
| P4 | Resource Functions | Ressourcen-Funktionen |
| P5 | Resource States | Ressourcen-Zustände, State Machines |
| P6 | Resource Sequence | Ressourcen-Sequenzen |
| P7 | Data Model | Physisches Datenmodell, Datenbanken |
| P8 | Resource Constraints | Physische Constraints, Limitierungen |
| Pr | Configuration Management | Konfigurationsmanagement, Versionen |

## R-Serie: Requirement

| Code | Name | Verwendung |
|------|------|-----------|
| R2 | Requirement Catalogue | Anforderungskatalog |
| R3 | Requirement Dependencies | Anforderungs-Abhängigkeiten |
| R7 | Requirement Derivation | Anforderungs-Ableitung |
| R8 | Requirement Fulfilment | Anforderungs-Erfüllung, Test |
| Rr | Requirement Realization | Anforderungs-Realisierung |

## Häufige Begriffe und ihre Viewpoints

| Begriff | Viewpoint(s) |
|---------|--------------|
| Capability | C1, C2, C3, C7, Cr, C1-S1 |
| Service | S1, S2, S3, S4, S5, S6, S7, S8, Sr, C1-S1 |
| Activity | L4, C4, L4-P4 |
| Function | S4, P4, L4-P4 |
| Resource | P1, P2, P3, P4, P5, P6, P7, P8, Pr |
| Node | L1, L2, L3, L2-L3 |
| Information/Data | L7, P7 |
| States | S5, L5, P5 |
| Sequence | S6, L6, P6 |
| Interface | S3, S7, L3, P3 |
| Requirement | R2, R3, R7, R8, Rr |
| Roadmap | Ar, Cr, Sr, Lr |
| Constraints | C8, L8, P8, S8 |

## Typische Anwendungsfälle

### Capability-Planung
→ C1 (Taxonomie), C2 (Vision), C3 (Dependencies), C7 (Performance), Cr (Roadmap)

### Service-Design
→ S1 (Taxonomie), S2 (Struktur), S3 (Interfaces), S4 (Functions), S8 (Policy)

### Logische Architektur
→ L1 (Nodes), L3 (Interactions), L4 (Activities), L7 (Information Model)

### Physische Architektur
→ P1 (Resources), P2 (Structure), P3 (Connectivity), P4 (Functions)

### Requirements Engineering
→ R2 (Catalogue), R3 (Dependencies), R7 (Derivation), R8 (Fulfilment), Rr (Realization)

### Enterprise-Architektur-Management
→ A1 (Metadata), A2 (Products), A5 (Status), A6 (Version), Ar (Roadmap)

## Mapping-Viewpoints

Spezielle Viewpoints für Zuordnungen zwischen Ebenen:

- **C1-S1**: Capability ↔ Service
- **L4-P4**: Logical Activity ↔ Resource Function
- **L2-L3**: Logical Scenario ↔ Node Interactions (kombiniert)

## Verwendung im Claude Skill

### Pattern 1: Direkter Code
```
User: "Erstelle ein L4-Diagramm"
Skill: Erkenne "L4" → "L4 - Logical Activities"
MCP: create_diagram(viewpoint="L4", toolbox="NAFv4-ADMBw-L4-Toolbox")
```

### Pattern 2: Kategorie
```
User: "Ich brauche ein Logical Architecture Diagramm für Activities"
Skill: "Logical" + "Activities" → L4
MCP: create_diagram(viewpoint="L4")
```

### Pattern 3: Natürlichsprachlich
```
User: "Zeige mir die Service-Schnittstellen"
Skill: "Service" + "Schnittstellen/Interfaces" → S3
MCP: create_diagram(viewpoint="S3")
```

### Pattern 4: Zweck-basiert
```
User: "Ich möchte Requirements verwalten"
Skill: "Requirements" → R-Serie, Standard: R2 (Catalogue)
MCP: create_diagram(viewpoint="R2")
```
