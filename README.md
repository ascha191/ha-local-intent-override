# Local Intent Override - Custom Component

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/ascha191/ha-local-intent-override.svg)](https://github.com/ascha191/ha-local-intent-override/releases)

This custom component allows local intents (like GetState) to be processed locally even when an LLM-Agent (ChatGPT, Claude, etc.) is active.

## 🎯 Problem

In Home Assistant, certain intents (like `GetState`) are filtered out by default when an LLM-Agent is active. This happens through the `_async_local_fallback_intent_filter` function in the Assist Pipeline. This means that even simple questions like "What is the status of Light.LivingRoom?" are forwarded to the LLM, even though they could be processed much more efficiently locally.

## ✅ Solution

This custom component overrides the filter function at runtime and allows all local intents to be processed locally, even when an LLM-Agent is configured.

## 📦 Installation

### Option 1: HACS (Recommended)

1. **Open HACS** in Home Assistant
2. Go to **Integrations** → **⋮** (Three dots) → **Custom repositories**
3. **Add repository**:
   - URL: `https://github.com/ascha191/ha-local-intent-override`
   - Category: `Integration`
4. Click **Add**
5. Find **Local Intent Override** in the list and click **Install**
6. **Restart Home Assistant**
7. **Add configuration** (see below)

### Option 2: Manual Installation

1. **Download files**:

   ```bash
   cd /config/custom_components/
   git clone https://github.com/ascha191/ha-local-intent-override.git local_intent_override
   ```

2. **Or download ZIP** and extract to `/config/custom_components/local_intent_override/`

3. **Restart Home Assistant**

4. **Add configuration** (see below)

## ⚙️ Configuration

Add this line to your `configuration.yaml`:

```yaml
# Local Intent Override - enables local intents even when LLM is active
local_intent_override:
```

**After configuration**: Restart Home Assistant

## 🚀 Usage

After installation, requests like:

- ✅ "What is the status of Light.LivingRoom?"
- ✅ "Is the living room light on?"
- ✅ "Show me the status of all lights"
- ✅ "Turn on the living room light"

...will be processed locally instead of being forwarded to the LLM. This results in:

- 🚀 **Faster responses**
- 💰 **Lower API usage**
- 🔒 **Better privacy** (no transmission to external APIs)
- ⚡ **More reliable function** (no internet dependency)

## 🔍 Debugging

Enable debug logging for detailed information:

```yaml
logger:
  logs:
    custom_components.local_intent_override: debug
```

You should then see messages like these in the log:

```
[local_intent_override] Filter called for intent: GetState
Successfully patched _async_local_fallback_intent_filter to allow all local intents
```

## 🔧 Advanced Configuration

The component works without further configuration. If you want to temporarily disable the functionality:

```yaml
# Comment out or remove the line
# local_intent_override:
```

## 📋 System Requirements

- **Home Assistant**: 2024.1 or newer
- **Python**: 3.11 or newer
- **Assist Pipeline**: Must be enabled
- **LLM-Agent**: OpenAI, Anthropic Claude, or other Conversation-Agents

## 🛠️ Technical Details

The component:

1. Loads at runtime and stores a reference to the original filter function
2. Replaces `_async_local_fallback_intent_filter` with its own implementation
3. Filters out only problematic intents that interfere with LLM-Agents
4. Allows all other local intents to be processed locally
5. Restores original functionality when uninstalled

## 🗑️ Uninstallation

### HACS:

1. **HACS** → **Integrations** → **Local Intent Override**
2. Click **Remove**
3. Remove line from `configuration.yaml`:
   ```yaml
   # Remove this line:
   # local_intent_override:
   ```
4. **Restart Home Assistant**

### Manual:

1. Remove `local_intent_override:` from `configuration.yaml`
2. Delete folder `/config/custom_components/local_intent_override/`
3. **Restart Home Assistant**

The original functionality will be automatically restored.

## 🐛 Troubleshooting

### Component doesn't load:

- Check that the folder is correctly located under `/config/custom_components/local_intent_override/`
- Check the logs for error messages
- Ensure all files are present (`__init__.py`, `manifest.json`)

### Intents are still sent to LLM:

- Enable debug logging (see above)
- Check that the component loaded: `Successfully patched _async_local_fallback_intent_filter`
- Restart Home Assistant

### Errors after installation:

- Check `home-assistant.log` for error messages
- Ensure your Home Assistant version is supported

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Create a pull request

## ⭐ Support

If you like this component, give the repository a star ⭐!

For problems or questions, please create an [Issue](https://github.com/ascha191/ha-local-intent-override/issues).
