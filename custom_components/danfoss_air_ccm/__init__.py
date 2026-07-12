from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .coordinator import DanfossCoordinator

PLATFORMS = [
    "sensor",
    "number",
    "switch",
    "button",
]


async def async_setup(hass, config):
    return True


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
):

    coordinator = DanfossCoordinator(
        hass,
        entry.data["host"],
    )

    await coordinator.async_config_entry_first_refresh()

    await coordinator.async_initialize_storage()

    hass.data.setdefault(DOMAIN, {})[
        entry.entry_id
    ] = coordinator

    await hass.config_entries.async_forward_entry_setups(
        entry,
        PLATFORMS,
    )

    return True


async def async_unload_entry(
    hass,
    entry,
):

    return await hass.config_entries.async_unload_platforms(
        entry,
        PLATFORMS,
    )