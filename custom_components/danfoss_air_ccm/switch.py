from __future__ import annotations

from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.entity import EntityCategory

from .const import DOMAIN
from .entity import DanfossEntity


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            DanfossBypassSwitch(coordinator),
            DanfossBoostSwitch(coordinator),
            DanfossBoostAutoSwitch(coordinator),
        ]
    )


class DanfossBypassSwitch(DanfossEntity, SwitchEntity):

    _attr_name = "Bypass"
    _attr_icon = "mdi:valve"

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_bypass"

    @property
    def is_on(self):
        return self.coordinator.data["bypass"]

    async def async_turn_on(self, **kwargs):
        await self.coordinator.set_bypass(True)

    async def async_turn_off(self, **kwargs):
        await self.coordinator.set_bypass(False)

class DanfossBoostSwitch(DanfossEntity, SwitchEntity):

    _attr_name = "Boost"
    _attr_icon = "mdi:rocket-launch"

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_boost"
        

    @property
    def is_on(self):
        return self.coordinator.data["boost"]

    async def async_turn_on(self, **kwargs):
        await self.coordinator.set_boost(True)

    async def async_turn_off(self, **kwargs):
        await self.coordinator.set_boost(False)


class DanfossBoostAutoSwitch(DanfossEntity, SwitchEntity):

    _attr_name = "Boost Auto"
    _attr_icon = "mdi:auto-mode"
    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_boost_auto"

    @property
    def is_on(self):
        return self.coordinator.data["boost_auto"]

    async def async_turn_on(self, **kwargs):
        await self.coordinator.set_boost_auto(True)

    async def async_turn_off(self, **kwargs):
        await self.coordinator.set_boost_auto(False)