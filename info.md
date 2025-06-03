# Local Intent Override

Diese Custom Component ermöglicht es, dass lokale Intents (wie GetState) auch dann lokal verarbeitet werden, wenn ein LLM-Agent aktiv ist.

## ✨ Funktionen

- **Non-invasive Lösung**: Keine Änderungen am Home Assistant Core erforderlich
- **Runtime Patching**: Überschreibt zur Laufzeit die Intent-Filterfunktion
- **Automatische Wiederherstellung**: Stellt ursprüngliches Verhalten beim Deaktivieren wieder her
- **Debug-Logging**: Umfassendes Logging für Fehlerbehebung

## 🔧 Installation

1. Installieren Sie diese Integration über HACS
2. Fügen Sie die folgende Zeile zu Ihrer `configuration.yaml` hinzu:
   ```yaml
   local_intent_override:
   ```
3. Starten Sie Home Assistant neu

## 📋 Kompatibilität

- **Home Assistant**: 2024.12.0+
- **HACS**: 1.6.0+
- **Python**: 3.13+

## 🐛 Problemlösung

Die Component protokolliert ihre Aktivitäten im Home Assistant Log. Aktivieren Sie Debug-Logging für `custom_components.local_intent_override` um detaillierte Informationen zu erhalten.
