from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            DanfossFanStepSensor(coordinator),
        ]
    )


class DanfossFanStepSensor(CoordinatorEntity, SensorEntity):

    _attr_has_entity_name = True
    _attr_name = "Fan Step"

    def __init__(self, coordinator):

        super().__init__(coordinator)

        self._attr_unique_id = "danfoss_fan_step"

    @property
    def native_value(self):

        return self.coordinator.data["fan_step"]