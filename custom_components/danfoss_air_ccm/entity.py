"""Base entity for Danfoss Air CCM."""

from __future__ import annotations

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


class DanfossEntity(CoordinatorEntity):
    """Base Danfoss entity."""

    _attr_has_entity_name = True

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, "danfoss_air_ccm")},
            manufacturer="Danfoss",
            model="Air CCM",
            name="Danfoss Air CCM",
        )