# Local Intent Override - Custom Component

Diese Custom Component ermöglicht es, dass lokale Intents (wie GetState) auch dann lokal verarbeitet werden, wenn ein LLM-Agent aktiv ist.

## Problem

In Home Assistant werden standardmäßig bestimmte Intents (wie `GetState`) herausgefiltert, wenn ein LLM-Agent aktiv ist. Dies geschieht durch die Funktion `_async_local_fallback_intent_filter` in der Assist Pipeline. Das bedeutet, dass auch einfache Fragen wie "Wie ist der Status von Licht.Wohnzimmer?" an das LLM weitergeleitet werden, obwohl sie lokal viel effizienter verarbeitet werden könnten.

## Lösung

Diese Custom Component überschreibt die Filterfunktion zur Laufzeit und ermöglicht es allen lokalen Intents, lokal verarbeitet zu werden, auch wenn ein LLM-Agent konfiguriert ist.

## Installation

1. Kopieren Sie den Ordner `local_intent_override` in Ihren `custom_components` Ordner
2. Fügen Sie die folgende Zeile zu Ihrer `configuration.yaml` hinzu:
   ```yaml
   local_intent_override:
   ```
3. Starten Sie Home Assistant neu

## Dateien

- `__init__.py` - Hauptkomponente mit der Patch-Logik
- `manifest.json` - Komponenten-Metadaten

## Funktionsweise

Die Component:
1. Speichert eine Referenz auf die ursprüngliche Filterfunktion
2. Ersetzt sie durch eine eigene Funktion, die immer `False` zurückgibt
3. Ermöglicht dadurch allen lokalen Intents die lokale Verarbeitung
4. Loggt Debug-Informationen für Troubleshooting

## Effekt

Nach der Installation werden Anfragen wie:
- "Wie ist der Status von Licht.Wohnzimmer?"
- "Ist das Licht im Wohnzimmer an?"
- "Zeige mir den Status aller Lichter"

...lokal verarbeitet, anstatt an das LLM weitergeleitet zu werden, was zu schnelleren Antworten und geringerem API-Verbrauch führt.

## Debugging

Aktivieren Sie Debug-Logging für diese Component:

```yaml
logger:
  logs:
    custom_components.local_intent_override: debug
```

## Deinstallation

1. Entfernen Sie `local_intent_override:` aus der `configuration.yaml`
2. Löschen Sie den `local_intent_override` Ordner aus `custom_components`
3. Starten Sie Home Assistant neu

Die ursprüngliche Funktionalität wird automatisch wiederhergestellt.
