from __future__ import annotations

from homeassistant.components.button import ButtonEntity
from homeassistant.helpers.entity import EntityCategory

from .const import DOMAIN
from .entity import DanfossEntity


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            DanfossRestoreInstallerSettingsButton(coordinator),
            DanfossFilterResetButton(coordinator),
        ]
    )


class DanfossRestoreInstallerSettingsButton(
    DanfossEntity,
    ButtonEntity,
):

    _attr_name = "Restore Installer Settings"
    _attr_unique_id = "danfoss_restore_installer_settings"

    _attr_icon = "mdi:restore"

    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, coordinator):
        super().__init__(coordinator)

    async def async_press(self):

        await self.coordinator.restore_installer_settings()

class DanfossFilterResetButton(DanfossEntity, ButtonEntity):

    _attr_name = "Reset Filter"
    _attr_icon = "mdi:air-filter"
    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_unique_id = "danfoss_filter_reset"

    async def async_press(self):
        await self.coordinator.reset_filter()