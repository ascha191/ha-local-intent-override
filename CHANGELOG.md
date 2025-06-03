# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-06-02

### Added
- Initial release of Local Intent Override custom component
- Runtime patching of `_async_local_fallback_intent_filter` function
- Support for allowing all local intents to be processed locally
- Proper cleanup when component is unloaded or removed
- Comprehensive logging for debugging

### Features
- Non-invasive solution that doesn't require core Home Assistant modifications
- Automatic restoration of original behavior when component is disabled
- Debug logging to help troubleshoot intent filtering
- Compatible with Home Assistant 2024.12+
