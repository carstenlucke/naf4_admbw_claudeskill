# Skill-Übersicht

Dieses Repository sammelt MCP-Skills, die natürliche Sprache mit den NAF v4 / ADMBw Artefakten in Sparx Enterprise Architect verbinden. Jeder Skill befindet sich im Verzeichnis `skill_<name>` und bringt eine eigene `SKILL.md` und Referenzen mit.

## Vorhandene Skills

### `skill_nafv4-interface-ea-mcp`
- **Zweck**: Übersetzt Anforderungen zur Modellierung der NAF Requirement Viewpoints (R2–R6) in MCP-Aufrufe für Sparx Enterprise Architect.
- **Kernfähigkeiten**:
  - Anlegen von R2–R6-Diagrammen inkl. Toolbox-Auswahl.
  - Erstellen von Requirement-Elementen (Functional/Nonfunctional Requirement, RequirementCategory, Standards usw.) mit automatischer Benennung.
  - Erzeugen von Beziehungen (z. B. `DerivedFrom`, `PartOfCatalogue`, `ConformsTo`) unter Berücksichtigung der Metakonstraints.
  - Arbeit mit naturalsprachlichen Befehlen wie „füge eine funktionale Anforderung hinzu“ oder „erstelle einen derived-from Link“.
- **Referenzen**:
  - `SKILL.md` – beschreibt Workflow, MCP-Aufrufe und typische Muster.
  - `references/requirement_viewpoints.json` – vollständige Metadaten zu R2–R6.
  - `references/stereotype_mappings.md` – Mapping natürlicher Begriffe zu Stereotypen.

## Geplante Skills

| Platzhalter | Beschreibung |
| --- | --- |
| _TBD_ | Ein weiterer Skill ist vorgesehen (z. B. für Logical oder Service Viewpoints). Sobald das Ziel feststeht, wird hier eine neue Sektion ergänzt. |

> Ergänze dieses Dokument, sobald neue Skills hinzukommen oder bestehende erweitert werden, damit andere Teams schnell verstehen, welche Fähigkeiten bereits verfügbar sind.
