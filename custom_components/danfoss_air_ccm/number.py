from __future__ import annotations

from homeassistant.components.number import NumberEntity

from .const import DOMAIN
from .entity import DanfossEntity


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            DanfossFanStepNumber(coordinator),
            DanfossSupplyStepNumber(coordinator),
            DanfossExtractStepNumber(coordinator),

        ]
    )


class DanfossFanStepNumber(DanfossEntity, NumberEntity):

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

class DanfossSupplyStepNumber(DanfossEntity, NumberEntity):

    _attr_name = "Supply Step"
    _attr_native_min_value = 0
    _attr_native_max_value = 100
    _attr_native_step = 1

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_supply_step_number"

    @property
    def native_value(self):
        return self.coordinator.data["basic_supply_step"]

    async def async_set_native_value(self, value):
        await self.coordinator.set_basic_supply(int(value))

class DanfossExtractStepNumber(DanfossEntity, NumberEntity):

    _attr_name = "Extract Step"
    _attr_native_min_value = 0
    _attr_native_max_value = 100
    _attr_native_step = 1

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_extract_step_number"

    @property
    def native_value(self):
        return self.coordinator.data["basic_extract_step"]

    async def async_set_native_value(self, value):
        await self.coordinator.set_basic_extract(int(value))