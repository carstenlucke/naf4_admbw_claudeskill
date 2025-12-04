# NAF v4 / ADMBw Claude Skill

Dieses Repository enthält eine umfassende Analyse des NATO Architecture Framework Version 4 (NAF v4) und des Architektur Datenmodells der Bundeswehr (ADMBw), extrahiert aus der offiziellen MDG-Datei für Sparx Enterprise Architect.

## 🎯 Zweck

Dieses Projekt unterstützt die Entwicklung eines Claude Skills, der natürlichsprachliche Anweisungen für die Erstellung von NAF v4 Diagrammen in präzise Befehle für einen MCP-Server übersetzt, der Sparx Enterprise Architect steuert.

### Anwendungsfall
Ein Benutzer kann sagen:
- *"Erstelle ein L4-Diagramm"*
- *"Zeige mir die Capability Taxonomy"*
- *"Ich brauche ein Service Interface Diagramm"*

Der Claude Skill versteht diese Anfragen und generiert präzise MCP-Server-Anweisungen mit korrekten Viewpoint-Codes, Toolboxes und verfügbaren Elementtypen.

## 📊 Analyseergebnisse

Die Analyse der MDG-Datei hat folgende Metamodell-Informationen extrahiert:

- **46 Viewpoints** (Diagrammarten)
- **235 Elementtypen** (Stereotypen)
- **105 Beziehungstypen**
- **47 Toolboxes** mit verfügbaren Elementen
- **6 Viewpoint-Kategorien**

## 📁 Repository-Struktur

### Dokumentation

| Datei | Beschreibung |
|-------|--------------|
| `NAF_V4_OVERVIEW.md` | Umfassende Dokumentation aller Viewpoints, Elementtypen und Beziehungen (11 KB) |
| `VIEWPOINT_QUICK_REFERENCE.md` | Schnellreferenz für alle 46 Viewpoints mit Verwendungsbeispielen (6 KB) |

### Daten

| Datei | Beschreibung |
|-------|--------------|
| `naf_complete_analysis.json` | Vollständige Analysedaten im JSON-Format (325 KB) |
| `mdg_analysis.json` | Basis-Analyse mit Stereotypen (110 KB) |
| `naf_viewpoints_analysis.json` | Viewpoint-spezifische Daten (71 KB) |

### Analyse-Tools

| Datei | Beschreibung |
|-------|--------------|
| `extract_complete_naf_data.py` | Haupt-Extraktionstool - vollständige Analyse der MDG-Datei |
| `analyze_naf_viewpoints.py` | Viewpoint-fokussierte Analyse |
| `analyze_mdg.py` | Basis-Analysetool für Stereotypen |

### Quelldaten

| Datei | Beschreibung |
|-------|--------------|
| `mdg/NAFv4-ADMBw-MDG-2024.06.xml` | Original MDG-Datei für Sparx Enterprise Architect (865 KB) |

## 🚀 Schnellstart

### Analyse erneut durchführen

```bash
# Vollständige Analyse
python3 extract_complete_naf_data.py

# Viewpoint-Analyse
python3 analyze_naf_viewpoints.py

# Basis-Analyse
python3 analyze_mdg.py
```

### JSON-Daten verwenden

```python
import json

# Lade vollständige Analysedaten
with open('naf_complete_analysis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Zugriff auf Viewpoint-Informationen
viewpoints = data['viewpoints']
print(viewpoints['L4'])  # L4 - Logical Activities

# Alle Elementtypen
element_types = data['element_types']  # Liste von 235 Elementtypen

# Alle Beziehungstypen
relationship_types = data['relationship_types']  # Liste von 105 Beziehungstypen
```

## 📖 NAF v4 Viewpoint-Kategorien

### A-Serie: Architecture Foundation (9 Viewpoints)
Metadaten, Architekturprodukte, Standards, Roadmaps
- `A1` - Meta-Data Definitions
- `A2` - Architecture Products
- `A3` - Architecture Correspondence
- `A4` - Methodology Used
- `A5` - Architecture Status
- `A6` - Architecture Version
- `A7` - Architecture Compliance
- `A8` - Standards
- `Ar` - Architecture Roadmap

### C-Serie: Concept (8 Viewpoints)
Capabilities, Enterprise Vision, Performance
- `C1` - Capability Taxonomy
- `C1-S1` - Capability to Service Mapping
- `C2` - Enterprise Vision
- `C3` - Capability Dependencies
- `C4` - Standard Processes
- `C5` - Effects
- `C7` - Performance Parameters
- `C8` - Planning Assumptions
- `Cr` - Capability Roadmap

### S-Serie: Service Specification (9 Viewpoints)
Service-Architektur, SOA
- `S1` - Service Taxonomy
- `S2` - Service Structure
- `S3` - Service Interfaces
- `S4` - Service Functions
- `S5` - Service States
- `S6` - Service Interactions
- `S7` - Service Interface Parameters
- `S8` - Service Policy
- `Sr` - Service Roadmap

### L-Serie: Logical Specification (10 Viewpoints)
Logische Architektur, Operational View
- `L1` - Node Types
- `L2` - Logical Scenario
- `L2-L3` - Logical Concept
- `L3` - Node Interactions
- `L4` - Logical Activities
- `L4-P4` - Activity to Function Mapping
- `L5` - Logical States
- `L6` - Logical Sequence
- `L7` - Information Model
- `L8` - Logical Constraints
- `Lr` - Lines of Development

### P-Serie: Physical Resource Specification (9 Viewpoints)
Physische Architektur, System View
- `P1` - Resource Types
- `P2` - Resource Structure
- `P3` - Resource Connectivity
- `P4` - Resource Functions
- `P5` - Resource States
- `P6` - Resource Sequence
- `P7` - Data Model
- `P8` - Resource Constraints
- `Pr` - Configuration Management

### R-Serie: Requirement (5 Viewpoints)
Requirements Engineering
- `R2` - Requirement Catalogue
- `R3` - Requirement Dependencies
- `R7` - Requirement Derivation
- `R8` - Requirement Fulfilment
- `Rr` - Requirement Realization

## 💡 Integration mit MCP-Server

### Beispiel: Pattern-Matching für natürlichsprachliche Anfragen

```python
import json

# Lade Viewpoint-Daten
with open('naf_complete_analysis.json', 'r') as f:
    naf_data = json.load(f)

def find_viewpoint(user_query):
    """Finde den passenden Viewpoint basierend auf Benutzeranfrage."""

    # Direkte Code-Erkennung
    if 'L4' in user_query:
        return naf_data['viewpoints']['L4']

    # Kategorie + Typ
    if 'logical' in user_query.lower() and 'activit' in user_query.lower():
        return naf_data['viewpoints']['L4']

    # Service-Schnittstellen
    if 'service' in user_query.lower() and 'interface' in user_query.lower():
        return naf_data['viewpoints']['S3']

    # Capability Taxonomy
    if 'capability' in user_query.lower() and 'taxonom' in user_query.lower():
        return naf_data['viewpoints']['C1']

    return None

# Beispiele
print(find_viewpoint("Erstelle ein L4-Diagramm"))
# → {'name': 'L4 - Logical Activities', 'code': 'L4', ...}

print(find_viewpoint("Zeige Service-Schnittstellen"))
# → {'name': 'S3 - Service Interfaces', 'code': 'S3', ...}
```

### Beispiel: MCP-Server-Anweisung generieren

```python
def create_mcp_command(viewpoint_code):
    """Generiere präzise MCP-Server-Anweisung."""
    vp = naf_data['viewpoints'][viewpoint_code]

    return {
        'action': 'create_diagram',
        'viewpoint': vp['code'],
        'diagram_id': vp['diagramID'],
        'toolbox': vp['toolbox'],
        'full_name': vp['name']
    }

# Beispiel
cmd = create_mcp_command('L4')
print(json.dumps(cmd, indent=2))
# {
#   "action": "create_diagram",
#   "viewpoint": "L4",
#   "diagram_id": "L4",
#   "toolbox": "NAFv4-ADMBw-L4-Toolbox",
#   "full_name": "L4 - Logical Activities"
# }
```

## 🔍 Häufige Anwendungsfälle

| Benutzeranfrage | Viewpoint | Kategorie |
|-----------------|-----------|-----------|
| "Capability-Planung" | C1, C2, C3, Cr | Concept |
| "Service-Design" | S1, S2, S3, S4 | Service Specification |
| "Logische Architektur" | L1, L3, L4, L7 | Logical Specification |
| "Physische Architektur" | P1, P2, P3, P4 | Physical Resource |
| "Requirements Management" | R2, R3, R7, R8, Rr | Requirement |
| "Informationsmodell" | L7, P7 | Data/Information Model |
| "Roadmap-Planung" | Ar, Cr, Sr, Lr | Roadmaps |

## 🛠️ Technische Details

### MDG-Datei-Struktur

Die MDG-Datei enthält:
- **DiagramProfile**: Definiert Viewpoints als Custom Diagram Types
- **UMLProfile**: Definiert Stereotypen und Toolboxes
- **ModelTemplates**: Vorlagen für Diagramme
- **TaggedValues**: Elementtypen mit UML-Basis-Klassen

### Extraktionslogik

1. **Viewpoint-Erkennung**: Suche nach Stereotypen mit `type="Diagram_Custom"`
2. **Toolbox-Extraktion**: UMLProfiles mit Namen `*-Toolbox`
3. **Element-Mapping**: TaggedValues im Format `NAFv4-ADMBw::ElementType(UML::BaseClass)`
4. **Beziehungs-Identifikation**: Elemente mit UML-Basis `Dependency`, `Realization`, etc.

## 📚 Weitere Ressourcen

- [NAF v4 Official Documentation](https://www.nato.int/cps/en/natohq/topics_157575.htm)
- [ADMBw Architektur Datenmodell der Bundeswehr](https://www.bundeswehr.de/)
- [Sparx Enterprise Architect](https://sparxsystems.com/)

## 📄 Lizenz

Dieses Projekt dient der Analyse und Dokumentation des NAF v4 / ADMBw Metamodells für Integrationszwecke.

## 🤝 Beitrag

Für Fragen oder Verbesserungen kontaktieren Sie bitte: SystemarchitektIT-SysBw@bundeswehr.org

---

**Version**: 2024.06
**Stand**: 2025-12-04
**Quelle**: NAFv4-ADMBw-MDG-2024.06.xml
