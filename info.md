# Local Intent Override

This custom component allows local intents (like GetState) to be processed locally even when an LLM-Agent is active.

## ✨ Features

- **Non-invasive solution**: No changes to Home Assistant Core required
- **Runtime patching**: Overrides intent filter function at runtime
- **Automatic restoration**: Restores original behavior when disabled
- **Debug logging**: Comprehensive logging for troubleshooting

## 🔧 Installation

1. Install this integration via HACS
2. Add the following line to your `configuration.yaml`:
   ```yaml
   local_intent_override:
   ```
3. Restart Home Assistant

## 📋 Compatibility

- **Home Assistant**: 2024.12.0+
- **HACS**: 1.6.0+
- **Python**: 3.13+

## 🐛 Troubleshooting

The component logs its activities to the Home Assistant log. Enable debug logging for `custom_components.local_intent_override` for detailed information.
