from __future__ import annotations

from homeassistant.components.number import NumberEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            DanfossFanStepNumber(coordinator),
        ]
    )


class DanfossFanStepNumber(CoordinatorEntity, NumberEntity):

    _attr_has_entity_name = True
    _attr_name = "Fan Step"

    _attr_native_min_value = 1
    _attr_native_max_value = 10
    _attr_native_step = 1

    def __init__(self, coordinator):

        super().__init__(coordinator)

        self._attr_unique_id = "danfoss_fan_step_number"

    @property
    def native_value(self):

        return self.coordinator.data["fan_step"]

    async def async_set_native_value(self, value):

        await self.coordinator.set_fan_step(int(value))