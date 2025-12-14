# NAFv4 / ADMBw Viewpoint-Extraktionen

Dieses Repository enthält strukturierte Exporte der NAFv4-ADMBw-MDG-Datei. Jede Unterstruktur dokumentiert eine Viewpoint-Familie mit zwei Artefakten:

- `*.json`: maschinenlesbare Auflistung der Viewpoints inklusive Diagrammtyp, Toolbox-Definitionen sowie beschreibenden Metadaten zu Element- und Beziehungstypen.
- `README.md`: menschenlesbare Kurzdokumentation mit Tabellen und Stichpunktlisten pro Viewpoint.

## Überblick nach Verzeichnis

| Verzeichnis | Inhaltlicher Fokus | Besonderheiten |
| --- | --- | --- |
| `vp-architecture-metadata/` | Architecture Foundation & Metadaten (A1–A8, Ar) | Meta-Informationen je Architekturbeschreibung, Projektzuordnungen, Status- und Compliance-Diagramme. |
| `vp-concepts/` | Concept Viewpoints (C1–Cr) | Capability-Taxonomien, Enterprise Vision, Performance- und Roadmap-Darstellungen. |
| `vp-logical-specification/` | Logical Specification Viewpoints (Business Process, L1–L8, L2-L3, Lr) | Knoten, Szenarien, logische Abläufe, Informations- und Zustandsmodelle. |
| `vp-physical-resource-specification/` | Physical Resource Specification Viewpoints (P1–Pr) | Physische Ressourcenstrukturen, Funktionen, Sequenzen, Datenmodelle und Constraints. |
| `vp-requirements/` | Requirement Viewpoints (R2–Rr) | Requirements-Kataloge, Abhängigkeiten, Derivation/Fulfilment sowie Realisierung durch Elemente. |
| `vp-service-specification/` | Service Specification Viewpoints (S1–Sr) | Service-Taxonomien, Schnittstellen, Funktionen, Zustände, Interaktionen und Policies. |

## Nutzung

1. Wähle die relevante Viewpoint-Familie über das passende Unterverzeichnis.
2. Nutze das JSON für automatisierte Verarbeitung (z. B. MCP-Server, Codegenerierung).
3. Verwende die README pro Verzeichnis als Nachschlagewerk für Modellierer.
