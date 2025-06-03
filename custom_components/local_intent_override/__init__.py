"""Custom component to override local intent filtering behavior."""

import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.components.assist_pipeline import pipeline

_LOGGER = logging.getLogger(__name__)

DOMAIN = "local_intent_override"


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the local intent override component."""
    _LOGGER.info("Setting up local intent override component")

    # Store the original function
    original_filter = pipeline._async_local_fallback_intent_filter

    def patched_local_fallback_intent_filter(result) -> bool:
        """Patched filter that respects prefer_local_intents setting."""
        _LOGGER.debug(
            "[local_intent_override] Filter called for intent: %s",
            getattr(result.intent, 'name', None),
        )

        # Always allow local intents when this component is active
        # This effectively implements the prefer_local_intents behavior
        return False

    # Replace the function in the pipeline module
    pipeline._async_local_fallback_intent_filter = patched_local_fallback_intent_filter

    # Store references for cleanup
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN]["original_filter"] = original_filter
    hass.data[DOMAIN]["patched_filter"] = patched_local_fallback_intent_filter

    _LOGGER.info("Successfully patched _async_local_fallback_intent_filter to allow all local intents")
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True


async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Remove a config entry."""
    # Restore original function when component is removed
    if DOMAIN in hass.data and "original_filter" in hass.data[DOMAIN]:
        pipeline._async_local_fallback_intent_filter = hass.data[DOMAIN]["original_filter"]
        _LOGGER.info("Restored original _async_local_fallback_intent_filter")


async def async_unload(hass: HomeAssistant) -> bool:
    """Unload the component completely and restore original behavior."""
    # Restore original function
    if DOMAIN in hass.data and "original_filter" in hass.data[DOMAIN]:
        original_filter = hass.data[DOMAIN]["original_filter"]
        pipeline._async_local_fallback_intent_filter = original_filter
        _LOGGER.info("Restored original _async_local_fallback_intent_filter during unload")

    # Clean up stored data
    if DOMAIN in hass.data:
        del hass.data[DOMAIN]

    return True
