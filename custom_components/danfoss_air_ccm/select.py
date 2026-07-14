from __future__ import annotations

from homeassistant.components.select import SelectEntity

from .const import DOMAIN
from .entity import DanfossEntity


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            DanfossRunModeSelect(coordinator),
        ]
    )


class DanfossRunModeSelect(DanfossEntity, SelectEntity):

    _attr_name = "Run Mode"

    _attr_options = [
        "Demand",
        "Program",
        "Manual",
    ]

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_run_mode"

    @property
    def current_option(self):

        mode = self.coordinator.data["run_mode"]

        if mode == 0:
            return "Demand"

        if mode == 1:
            return "Program"

        if mode == 2:
            return "Manual"

        return None

    async def async_select_option(self, option):
        await self.coordinator.set_run_mode(option)