# NAF v4 / ADMBw - Metamodell Übersicht

Dieses Dokument bietet einen umfassenden Überblick über das NATO Architecture Framework Version 4 (NAF v4) und das Architektur Datenmodell der Bundeswehr (ADMBw), wie es in der MDG-Datei für Sparx Enterprise Architect definiert ist.

## Extrahiert aus
- **Datei**: `mdg/NAFv4-ADMBw-MDG-2024.06.xml`
- **Version**: 2024.06
- **Analysiert am**: 2025-12-04

## Statistiken

- **Viewpoints gesamt**: 46
- **Viewpoint-Kategorien**: 6
- **Elementtypen**: 235
- **Beziehungstypen**: 105
- **Stereotypen**: 690+

---

## 1. Viewpoint-Kategorien

NAF v4 / ADMBw organisiert die Viewpoints in 6 Hauptkategorien:

1. **Architecture Foundation Viewpoints** (A-Serie)
2. **Concept Viewpoints** (C-Serie)
3. **Service Specification Viewpoints** (S-Serie)
4. **Logical Specification Viewpoints** (L-Serie)
5. **Physical Resource Specification Viewpoints** (P-Serie)
6. **Requirement Viewpoints** (R-Serie)

---

## 2. Alle NAF v4 Viewpoints

### Architecture Foundation Viewpoints (A-Serie)

| Code | Vollständiger Name | Beschreibung |
|------|-------------------|--------------|
| **A1** | Meta-Data Definitions | Meta-Daten-Tags zur Suche und Auffindbarkeit |
| **A2** | Architecture Products | Struktur der Architektur und ihre Produkte |
| **A3** | Architecture Correspondence | Beziehungen zwischen Architekturbeschreibungselementen |
| **A4** | Methodology Used | Verwendete Methodik für Architekturaktivitäten |
| **A5** | Architecture Status | Versionsnummern und Genehmigungsstatus |
| **A6** | Architecture Version | Vollständige Architekturhistorie |
| **A7** | Architecture Compliance | Spezifikation von Architektur-Metadaten |
| **A8** | Standards | Technische und nicht-technische Standards |
| **Ar** | Architecture Roadmap | Historie und zukünftige Richtung des Architekturprojekts |

### Concept Viewpoints (C-Serie)

| Code | Vollständiger Name | Beschreibung |
|------|-------------------|--------------|
| **C1** | Capability Taxonomy | Taxonomie aller Fähigkeiten (Capabilities) |
| **C1-S1** | Capability to Service Mapping | Zuordnung von Services zu Capabilities |
| **C2** | Enterprise Vision | Strategischer Kontext für Capabilities |
| **C3** | Capability Dependencies | Abhängigkeiten zwischen Capabilities |
| **C4** | Standard Processes | Wiederverwendbare Standard-Betriebsaktivitäten |
| **C5** | Effects | Betriebliche Effekte von Capabilities und Services |
| **C7** | Performance Parameters | Leistungsparameter (Measures of Effectiveness) |
| **C8** | Planning Assumptions | Annahmen für die Implementierung von Capabilities |
| **Cr** | Capability Roadmap | Capability Audit und Gap-Analyse |

### Service Specification Viewpoints (S-Serie)

| Code | Vollständiger Name | Beschreibung |
|------|-------------------|--------------|
| **S1** | Service Taxonomy | Governance-Struktur für Service-Oriented Architecture |
| **S2** | Service Structure | Strukturierung von Services |
| **S3** | Service Interfaces | Identifikation und Definition von Service-Schnittstellen |
| **S4** | Service Functions | Verhaltensspezifikation für Services |
| **S5** | Service States | Zulässige Zustände und Zustandsübergänge |
| **S6** | Service Interactions | Service-Interaktionen |
| **S7** | Service Interface Parameters | Schnittstellenspezifikationen |
| **S8** | Service Policy | Constraints für Services |
| **Sr** | Service Roadmap | Service Audit und Gap-Analyse |

### Logical Specification Viewpoints (L-Serie)

| Code | Vollständiger Name | Beschreibung |
|------|-------------------|--------------|
| **L1** | Node Types | Definition aller Nodes in der logischen Architektur |
| **L2** | Logical Scenario | Szenario-basierte Kommunikation |
| **L2-L3** | Logical Concept | Executive-Level-Kommunikation von Architekturzweck |
| **L3** | Node Interactions | Interoperabilitätsanforderungen |
| **L4** | Logical Activities | Aktivitäten und deren Zusammenhänge |
| **L4-P4** | Activity to Function Mapping | Zuordnung von Resource Functions zu Activities |
| **L5** | Logical States | Zustände und Zustandsübergänge von Nodes |
| **L6** | Logical Sequence | Sequenzen und Zeitabläufe |
| **L7** | Information Model | Business-Informationsmodell |
| **L8** | Logical Constraints | Constraints für die logische Architektur |
| **Lr** | Lines of Development | Unterstützung für Akquisitionsprozesse |

### Physical Resource Specification Viewpoints (P-Serie)

| Code | Vollständiger Name | Beschreibung |
|------|-------------------|--------------|
| **P1** | Resource Types | Ressourcentypen und Leistungsmerkmale |
| **P2** | Resource Structure | Struktur und Interaktion von Ressourcen |
| **P3** | Resource Connectivity | Netzwerke und physische Pfade |
| **P4** | Resource Functions | Zuordnung von Funktionen zu Ressourcen |
| **P5** | Resource States | Ressourcenzustände und Zustandsübergänge |
| **P6** | Resource Sequence | Ressourcensequenzen |
| **P7** | Data Model | Datenmodell (nahe am System-Design) |
| **P8** | Resource Constraints | Constraints für physische Architektur |
| **Pr** | Configuration Management | Änderungen von Resource Assets über Zeit |

### Requirement Viewpoints (R-Serie)

| Code | Vollständiger Name | Beschreibung |
|------|-------------------|--------------|
| **R2** | Requirement Catalogue | Katalog von Anforderungen |
| **R3** | Requirement Dependencies | Abhängigkeiten zwischen Anforderungen |
| **R7** | Requirement Derivation | Zuordnung von Anforderungen zu Architekturelementen |
| **R8** | Requirement Fulfilment | Akzeptanz- und Evaluierungskriterien |
| **Rr** | Requirement Realization | Zuordnung von Anforderungen zu realisierenden Elementen |

---

## 3. Wichtige Informationen für MCP-Server Integration

### Viewpoint-Codes für natürlichsprachliche Anweisungen

Der MCP-Server sollte folgende Viewpoint-Codes verstehen:

#### A-Serie (Architecture Foundation)
`A1`, `A2`, `A3`, `A4`, `A5`, `A6`, `A7`, `A8`, `Ar`

#### C-Serie (Concept)
`C1`, `C1-S1`, `C2`, `C3`, `C4`, `C5`, `C7`, `C8`, `Cr`

#### S-Serie (Service Specification)
`S1`, `S2`, `S3`, `S4`, `S5`, `S6`, `S7`, `S8`, `Sr`

#### L-Serie (Logical Specification)
`L1`, `L2`, `L2-L3`, `L3`, `L4`, `L4-P4`, `L5`, `L6`, `L7`, `L8`, `Lr`

#### P-Serie (Physical Resource Specification)
`P1`, `P2`, `P3`, `P4`, `P5`, `P6`, `P7`, `P8`, `Pr`

#### R-Serie (Requirement)
`R2`, `R3`, `R7`, `R8`, `Rr`

### Mapping von natürlichsprachlichen Anfragen

Beispiele für die Interpretation von Benutzeranweisungen:

| Benutzeranweisung | Viewpoint-Code | Vollständiger Name |
|-------------------|---------------|-------------------|
| "Erstelle ein L4-Diagramm" | L4 | L4 - Logical Activities |
| "Zeige mir die Capability Taxonomy" | C1 | C1 - Capability Taxonomy |
| "Ich brauche ein Service Interface Diagramm" | S3 | S3 - Service Interfaces |
| "Erstelle einen Resource Types View" | P1 | P1 - Resource Types |
| "Zeige die Architecture Roadmap" | Ar | Ar - Architecture Roadmap |
| "Information Model erstellen" | L7 | L7 - Information Model |

### Kategorie-Zuordnung

Der Skill sollte auch Kategorie-Namen verstehen:

- **"Logical Architecture"** → L-Serie Viewpoints
- **"Physical Architecture"** → P-Serie Viewpoints
- **"Service Architecture"** → S-Serie Viewpoints
- **"Concept"** → C-Serie Viewpoints
- **"Requirements"** → R-Serie Viewpoints
- **"Architecture Foundation"** → A-Serie Viewpoints

---

## 4. Verfügbare Elementtypen (Auswahl)

### Häufig verwendete Elementtypen

#### Capabilities & Concepts
- `Capability`
- `CapabilityConfiguration`
- `EnterpriseVision`
- `EnterpriseGoal`
- `EnduringTask`

#### Services
- `ServiceSpecification`
- `ServiceInterface`
- `ServiceFunction`
- `ServicePolicy`

#### Logical Architecture
- `OperationalPerformer`
- `OperationalActivity`
- `OperationalRole`
- `OperationalInterface`

#### Physical Resources
- `Resource`
- `ResourceType`
- `ResourceFunction`
- `ResourceInterface`

#### Requirements
- `Requirement`
- `FunctionalRequirement`
- `NonFunctionalRequirement`

#### Organizations & Stakeholders
- `Organization`
- `Person`
- `Post`
- `Stakeholder`

---

## 5. Wichtige Beziehungstypen (Auswahl)

### Capability-Beziehungen
- `CapabilityDependency`
- `CapabilityForTask`
- `MapsToCapability`

### Service-Beziehungen
- `ServiceSupportsCapability`
- `ServiceInterface`
- `ServiceComposition`

### Logical-Physical Mapping
- `LogicalPhysicalMapping`
- `ActivitySupportsService`
- `ResourcePerformsActivity`

### Requirement-Beziehungen
- `RequirementDerivation`
- `RequirementFulfilment`
- `RequirementRealization`
- `RequirementDependency`

### Allgemeine Beziehungen
- `ConformsTo`
- `Satisfy`
- `RefersTo`
- `JustifiedBy`

---

## 6. Toolboxes

Jeder Viewpoint hat eine zugeordnete Toolbox mit verfügbaren Elementen:

### Beispiel: L4 - Logical Activities

**Toolbox**: `NAFv4-ADMBw-L4-Toolbox`

**Verfügbare Elemente**:
- **Activity**: OperationalActivity, StandardOperationalActivity
- **Class**: Capability
- **Dependency**: ActivitySupportsService, CapabilitySupportsService
- **Part**: OperationalRole
- **Und weitere...**

Alle detaillierten Informationen zu Toolboxes sind in `naf_complete_analysis.json` verfügbar.

---

## Dateien

Die folgenden Dateien wurden generiert:

1. **`naf_complete_analysis.json`** - Vollständige Analyse im JSON-Format
   - Alle Viewpoints mit Details
   - Toolboxes und verfügbare Elemente
   - Alle Elementtypen
   - Alle Beziehungstypen

2. **`NAF_V4_OVERVIEW.md`** - Dieses Dokument

3. **Python-Analysetools**:
   - `extract_complete_naf_data.py` - Vollständige Extraktion
   - `analyze_naf_viewpoints.py` - Viewpoint-Analyse
   - `analyze_mdg.py` - Basis-Analyse

---

## Verwendung für Claude Skill

Für die Entwicklung eines Claude Skills, der mit dem MCP-Server kommuniziert:

1. **Viewpoint-Erkennung**: Nutze die Viewpoint-Codes (A1-Ar, C1-Cr, S1-Sr, L1-Lr, P1-Pr, R2-Rr)
2. **Kategorie-Mapping**: Verstehe Kategorie-Anfragen (z.B. "Logical Architecture" → L-Serie)
3. **Präzise Anweisungen**: Übersetze natürlichsprachliche Anfragen in:
   - Viewpoint-Code (z.B. "L4")
   - Diagramm-ID (z.B. "L4")
   - Toolbox (z.B. "NAFv4-ADMBw-L4-Toolbox")

4. **Elementtypen**: Verstehe verfügbare Elementtypen pro Viewpoint
5. **Beziehungstypen**: Kenne die zulässigen Beziehungen zwischen Elementen

---

## Nächste Schritte

Für die Entwicklung des Claude Skills:

1. Lade die JSON-Datei `naf_complete_analysis.json` als Wissensbasis
2. Implementiere Pattern-Matching für Viewpoint-Erkennung
3. Mappe natürlichsprachliche Anfragen auf NAF-Codes
4. Generiere präzise MCP-Server-Anweisungen
5. Validiere Elementtypen gegen Viewpoint-Toolboxes

---

**Stand**: 2025-12-04
**Quelle**: NAFv4-ADMBw-MDG-2024.06.xml
