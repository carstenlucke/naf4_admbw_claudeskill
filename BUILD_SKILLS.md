# Skill-Dateien Build-Prozess

## Anweisung für Claude Code

Wenn der Nutzer sagt **"erstelle die Skill Dateien"** oder **"build the skill files"**, bedeutet das:

### Was zu tun ist

Für jeden Skill im Projekt eine zugehörige `*.skill` Datei erstellen.

### Was sind .skill Dateien?

- `*.skill` Dateien sind **ZIP-Archive**, die als `*.skill` benannt sind
- Jede `.skill` Datei enthält **alle Dateien des jeweiligen Skills**
- Sie werden im jeweiligen Skill-Verzeichnis abgelegt

### Projektstruktur

Das Projekt enthält mehrere Skills in folgenden Verzeichnissen:
- `skill_nafv4-architecture-metadata/`
- `skill_nafv4-assistant/`
- `skill_nafv4-concepts/`
- `skill_nafv4-coordinator/`
- `skill_nafv4-logical-specification/`
- `skill_nafv4-physical-resources/`
- `skill_nafv4-requirements/`
- `skill_nafv4-service-specification/`

### Verzeichnisstruktur pro Skill

Jedes Skill-Verzeichnis hat folgende Struktur:

```
skill_nafv4-<name>/
├── nafv4-<name>/              # Unterverzeichnis mit Skill-Dateien
│   ├── SKILL.md               # Hauptdefinition des Skills
│   ├── functions/             # (optional) Skill-Funktionen
│   └── references/            # (optional) Referenzdokumente
└── nafv4-<name>.skill         # ZIP-Archiv (zu erstellen)
```

### Build-Prozess

Für jeden Skill:

1. **In das Skill-Verzeichnis wechseln** (z.B. `skill_nafv4-assistant/`)
2. **Das Unterverzeichnis zippen** (z.B. `nafv4-assistant/`)
3. **Als .skill Datei speichern** (z.B. `nafv4-assistant.skill`)

### Bash-Befehl Beispiel

```bash
cd skill_nafv4-assistant
zip -r nafv4-assistant.skill nafv4-assistant/
```

### Vollständiger Build für alle Skills

```bash
# Architecture Metadata
cd skill_nafv4-architecture-metadata
zip -r nafv4-architecture-metadata.skill nafv4-architecture-metadata/
cd ..

# Assistant
cd skill_nafv4-assistant
zip -r nafv4-assistant.skill nafv4-assistant/
cd ..

# Concepts
cd skill_nafv4-concepts
zip -r nafv4-concepts.skill nafv4-concepts/
cd ..

# Coordinator
cd skill_nafv4-coordinator
zip -r nafv4-coordinator.skill nafv4-coordinator/
cd ..

# Logical Specification
cd skill_nafv4-logical-specification
zip -r nafv4-logical-specification.skill nafv4-logical-specification/
cd ..

# Physical Resources
cd skill_nafv4-physical-resources
zip -r nafv4-physical-resources.skill nafv4-physical-resources/
cd ..

# Requirements
cd skill_nafv4-requirements
zip -r nafv4-requirements.skill nafv4-requirements/
cd ..

# Service Specification
cd skill_nafv4-service-specification
zip -r nafv4-service-specification.skill nafv4-service-specification/
cd ..
```

## Hinweise

- Die `.skill` Dateien sind bereits im Repository vorhanden und werden bei Bedarf neu erstellt
- Stelle sicher, dass alle Änderungen in den Unterverzeichnissen (z.B. `nafv4-assistant/SKILL.md`) vor dem Build gespeichert sind
- Die `.skill` Dateien sollten nach dem Build committet werden, wenn sich Inhalte geändert haben
