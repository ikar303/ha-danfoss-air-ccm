from __future__ import annotations

from homeassistant.components.sensor import (
    SensorEntity,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import UnitOfTemperature

from .const import DOMAIN
from .entity import DanfossEntity
from .alarms import get_alarm_text

from homeassistant.helpers.entity import EntityCategory


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            DanfossFanStepSensor(coordinator),
            DanfossOutdoorTemperatureSensor(coordinator),
            DanfossSupplyTemperatureSensor(coordinator),
            DanfossExtractTemperatureSensor(coordinator),
            DanfossExhaustTemperatureSensor(coordinator),
            DanfossHumiditySensor(coordinator),
            DanfossCurrentSupplyStepSensor(coordinator),
            DanfossCurrentExtractStepSensor(coordinator),
            DanfossBypassActiveSensor(coordinator),
            DanfossAlarmCodeSensor(coordinator),
            DanfossAlarmDescriptionSensor(coordinator),
            DanfossFilterFoulingSensor(coordinator),
            DanfossSupplyFanSpeedSensor(coordinator),
            DanfossExtractFanSpeedSensor(coordinator),
           
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


class DanfossOutdoorTemperatureSensor(DanfossEntity, SensorEntity):

    _attr_name = "Outdoor Temperature"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_suggested_display_precision = 1

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_temp_01"

    @property
    def native_value(self):
        return self.coordinator.data["outdoor_temperature"]


class DanfossSupplyTemperatureSensor(DanfossEntity, SensorEntity):

    _attr_name = "Supply Temperature"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_suggested_display_precision = 1

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_temp_02"

    @property
    def native_value(self):
        return self.coordinator.data["supply_temperature"]


class DanfossExtractTemperatureSensor(DanfossEntity, SensorEntity):

    _attr_name = "Extract Temperature"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_suggested_display_precision = 1

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_temp_03"

    @property
    def native_value(self):
        return self.coordinator.data["extract_temperature"]


class DanfossExhaustTemperatureSensor(DanfossEntity, SensorEntity):

    _attr_name = "Exhaust Temperature"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_suggested_display_precision = 1

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_temp_04"

    @property
    def native_value(self):
        return self.coordinator.data["exhaust_temperature"]

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
    _attr_icon = "mdi:fan-chevron-down"
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator):        
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_supply_step"

    @property
    def native_value(self):
        return self.coordinator.data["current_supply_step"]


class DanfossCurrentExtractStepSensor(DanfossEntity, SensorEntity):

    _attr_name = "Current Extract Step"
    _attr_icon = "mdi:fan-chevron-up"
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_extract_step"

    @property
    def native_value(self):
        return self.coordinator.data["current_extract_step"]
    

class DanfossBypassActiveSensor(DanfossEntity, SensorEntity):

    _attr_name = "Bypass Active"
    _attr_icon = "mdi:valve"

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_bypass_active"

    @property
    def native_value(self):
        return (
            "On"
            if self.coordinator.data["bypass_active"]
            else "Off"
        )


class DanfossAlarmCodeSensor(DanfossEntity, SensorEntity):

    _attr_name = "Alarm Code"
    _attr_icon = "mdi:alert-circle-outline"
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_alarm_code"

    @property
    def native_value(self):
        return self.coordinator.data["alarm_code"]
    
class DanfossAlarmDescriptionSensor(DanfossEntity, SensorEntity):

    _attr_name = "Alarm Description"
    _attr_icon = "mdi:text-box-outline"
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_alarm_description"

    @property
    def native_value(self):

        return get_alarm_text(
            self.coordinator.data["alarm_code"]
        )

class DanfossFilterFoulingSensor(DanfossEntity, SensorEntity):

    _attr_name = "Filter Fouling"
    _attr_native_unit_of_measurement = "%"
    _attr_icon = "mdi:air-filter"

    _attr_entity_category = EntityCategory.DIAGNOSTIC
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_filter_fouling"

    @property
    def native_value(self):
        return self.coordinator.data["filter_fouling"]

class DanfossSupplyFanSpeedSensor(DanfossEntity, SensorEntity):

    _attr_name = "Supply Fan Speed"
    _attr_native_unit_of_measurement = "rpm"
    _attr_icon = "mdi:fan"

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_supply_fan_speed"

    @property
    def native_value(self):
        return self.coordinator.data["supply_fan_speed"]


class DanfossExtractFanSpeedSensor(DanfossEntity, SensorEntity):

    _attr_name = "Extract Fan Speed"
    _attr_native_unit_of_measurement = "rpm"
    _attr_icon = "mdi:fan"

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_extract_fan_speed"

    @property
    def native_value(self):
        return self.coordinator.data["extract_fan_speed"]
