from __future__ import annotations

from homeassistant.components.number import NumberEntity

from homeassistant.helpers.entity import EntityCategory

from .const import DOMAIN
from .entity import DanfossEntity


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            DanfossFanStepNumber(coordinator),
            DanfossSupplyStepNumber(coordinator),
            DanfossExtractStepNumber(coordinator),
            DanfossBoostTimerNumber(coordinator),
            DanfossBoostStepNumber(coordinator),
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

    _attr_name = "Basic Supply Step"
    _attr_icon = "mdi:fan-chevron-down"
    _attr_native_min_value = 0
    _attr_native_max_value = 100
    _attr_native_step = 1
    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_supply_step_number"


    @property
    def native_value(self):
        return self.coordinator.data["basic_supply_step"]

    async def async_set_native_value(self, value):
        await self.coordinator.set_basic_supply(int(value))

class DanfossExtractStepNumber(DanfossEntity, NumberEntity):

    _attr_name = "Basic Extract Step"
    _attr_icon = "mdi:fan-chevron-up"
    _attr_native_min_value = 0
    _attr_native_max_value = 100
    _attr_native_step = 1
    _attr_entity_category = EntityCategory.CONFIG
    
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_extract_step_number"

    @property
    def native_value(self):
        return self.coordinator.data["basic_extract_step"]

    async def async_set_native_value(self, value):
        await self.coordinator.set_basic_extract(int(value))

class DanfossBoostTimerNumber(DanfossEntity, NumberEntity):



    _attr_name = "Boost Duration"
    _attr_icon = "mdi:timer-outline"
    _attr_native_unit_of_measurement = "h"

    _attr_native_min_value = 1
    _attr_native_max_value = 24
    _attr_native_step = 1

    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_boost_timer"

    @property
    def native_value(self):
        return self.coordinator.data["boost_timer"]

    async def async_set_native_value(self, value):
        await self.coordinator.set_boost_timer(int(value))


class DanfossBoostStepNumber(DanfossEntity, NumberEntity):

    _attr_name = "Boost Max Step"
    _attr_icon = "mdi:fan-plus"

    _attr_native_min_value = 1
    _attr_native_max_value = 10
    _attr_native_step = 1

    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_boost_step"

    @property
    def native_value(self):
        return self.coordinator.data["boost_max_step"]

    async def async_set_native_value(self, value):
        await self.coordinator.set_boost_max_step(int(value))