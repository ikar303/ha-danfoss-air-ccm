from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.storage import Store

STORAGE_VERSION = 1
STORAGE_KEY = "danfoss_air_ccm.installer_settings"

DEFAULTS = {
    "installer_supply_step": None,
    "installer_extract_step": None,
}


class DanfossStorage:

    def __init__(self, hass: HomeAssistant):
        self.store = Store(
            hass,
            STORAGE_VERSION,
            STORAGE_KEY,
        )

    async def load(self):
        data = await self.store.async_load()

        if data is None:
            return DEFAULTS.copy()

        return data

    async def save(self, data):
        await self.store.async_save(data)