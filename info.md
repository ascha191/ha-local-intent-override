# Local Intent Override

Enables local processing of intents (like GetState) even when an LLM-Agent is active.

## Features
- Non-invasive solution - no Home Assistant Core changes required
- Runtime patching of intent filter function  
- Automatic restoration when disabled

## Installation
1. Install via HACS
2. Add `local_intent_override:` to your `configuration.yaml`
3. Restart Home Assistant

Compatible with Home Assistant 2024.12.0+
