from __future__ import annotations

from homeassistant.components.sensor import (
    SensorEntity,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import UnitOfTemperature

from .const import DOMAIN
from .entity import DanfossEntity


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            DanfossFanStepSensor(coordinator),
            DanfossTemperature01Sensor(coordinator),
            DanfossTemperature02Sensor(coordinator),
            DanfossTemperature03Sensor(coordinator),
            DanfossTemperature04Sensor(coordinator),
            DanfossHumiditySensor(coordinator),
            DanfossCurrentSupplyStepSensor(coordinator),
            DanfossCurrentExtractStepSensor(coordinator),
        ]
    )


class DanfossFanStepSensor(DanfossEntity, SensorEntity):

    _attr_name = "Fan Step"
    _attr_icon = "mdi:fan"
    
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_fan_step"

    @property
    def native_value(self):
        return self.coordinator.data["fan_step"]


class DanfossTemperature01Sensor(DanfossEntity, SensorEntity):

    _attr_name = "Outdoor Temperature"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_temp_01"

    @property
    def native_value(self):
        return self.coordinator.data["temp_01"]


class DanfossTemperature02Sensor(DanfossEntity, SensorEntity):

    _attr_name = "Supply Temperature"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_temp_02"

    @property
    def native_value(self):
        return self.coordinator.data["temp_02"]


class DanfossTemperature03Sensor(DanfossEntity, SensorEntity):

    _attr_name = "Extract Temperature"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_temp_03"

    @property
    def native_value(self):
        return self.coordinator.data["temp_03"]


class DanfossTemperature04Sensor(DanfossEntity, SensorEntity):

    _attr_name = "Exhaust Temperature"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_temp_04"

    @property
    def native_value(self):
        return self.coordinator.data["temp_04"]
    
class DanfossHumiditySensor(DanfossEntity, SensorEntity):

    _attr_name = "Relative Humidity"
    _attr_native_unit_of_measurement = "%"
    _attr_device_class = SensorDeviceClass.HUMIDITY
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_unique_id = "danfoss_humidity"
    _attr_suggested_display_precision = 1

    def __init__(self, coordinator):
        super().__init__(coordinator)

    @property
    def native_value(self):
        return self.coordinator.data["humidity"]
    
   
class DanfossCurrentSupplyStepSensor(DanfossEntity, SensorEntity):

    _attr_name = "Current Supply Step"
    _attr_icon = "mdi:account"

    def __init__(self, coordinator):        
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_supply_step"

    @property
    def native_value(self):
        return self.coordinator.data["basic_supply_step"]


class DanfossCurrentExtractStepSensor(DanfossEntity, SensorEntity):

    _attr_name = "Current Extract Step"
    _attr_icon = "mdi:fan-chevron-up"

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_extract_step"

    @property
    def native_value(self):
        return self.coordinator.data["basic_extract_step"]