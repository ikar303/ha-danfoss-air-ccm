"""Danfoss Air coordinator."""

from __future__ import annotations

from .storage import DanfossStorage

from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .protocol import DanfossClient

_LOGGER = logging.getLogger(__name__)


class DanfossCoordinator(DataUpdateCoordinator):

    def __init__(self, hass: HomeAssistant, host: str):

        self.client = DanfossClient(host)

        self.storage = DanfossStorage(hass)

        super().__init__(
            hass,
            _LOGGER,
            name="Danfoss Air CCM",
            update_interval=timedelta(seconds=30),
        )

    async def _async_update_data(self):

        try:

            return await self.hass.async_add_executor_job(
                self._read_all
            )

        except Exception as err:
            raise UpdateFailed(str(err)) from err

    def _read_all(self):

        return {
            "fan_step": self.client.get_fan_step(),

            "temp_01": self.client.get_temp_01(),
            "temp_02": self.client.get_temp_02(),
            "temp_03": self.client.get_temp_03(),
            "temp_04": self.client.get_temp_04(),

            "humidity": self.client.get_humidity(),
          
            "basic_supply_step": self.client.get_basic_supply(),
            "basic_extract_step": self.client.get_basic_extract(),

            "bypass": self.client.get_bypass(),
            
            "boost": self.client.get_boost(),
            "boost_timer": self.client.get_boost_timer(),
            "boost_max_step": self.client.get_boost_max_step(),
            "boost_auto": self.client.get_boost_auto(),
            "run_mode": self.client.get_run_mode(),

            "bypass_active": self.client.get_bypass_active(),

            "alarm_code": self.client.get_alarm_code(),
            "current_supply_step": self.client.get_current_supply_step(),
            "current_extract_step": self.client.get_current_extract_step(),
        }

    async def set_fan_step(self, value):

        await self.hass.async_add_executor_job(
            self.client.set_fan_step,
            value,
        )

        await self.async_request_refresh()

    async def set_basic_supply(self, value):

        await self.hass.async_add_executor_job(
            self.client.set_basic_supply,
            value,
    )

        await self.async_request_refresh()


    async def set_basic_extract(self, value):

        await self.hass.async_add_executor_job(
            self.client.set_basic_extract,
            value,
    )

        await self.async_request_refresh()

    async def set_bypass(self, enabled: bool):

        await self.hass.async_add_executor_job(
            self.client.set_bypass,
            enabled,
        )

        await self.async_request_refresh()

    async def set_boost(self, enabled: bool):

        await self.hass.async_add_executor_job(
            self.client.set_boost,
            enabled,
        )

        await self.async_request_refresh()


    async def set_boost_timer(self, value):

        await self.hass.async_add_executor_job(
            self.client.set_boost_timer,
            value,
        )

        await self.async_request_refresh()


    async def set_boost_max_step(self, value):

        await self.hass.async_add_executor_job(
            self.client.set_boost_max_step,
            value,
        )

        await self.async_request_refresh()


    async def set_boost_auto(self, enabled: bool):

        await self.hass.async_add_executor_job(
            self.client.set_boost_auto,
            enabled,
        )

        await self.async_request_refresh()

    async def set_run_mode(self, mode: str):

        if mode == "Demand":

            await self.hass.async_add_executor_job(
                self.client.set_run_mode_demand,
            )

        elif mode == "Program":

            await self.hass.async_add_executor_job(
                self.client.set_run_mode_program,
            )

        elif mode == "Manual":

            await self.hass.async_add_executor_job(
                self.client.set_run_mode_manual,
                self.data["fan_step"],
            )

        await self.async_request_refresh()


    async def async_initialize_storage(self):

        """Save installer settings on first run."""

        data = await self.storage.load()

        if (
            data["installer_supply_step"] is None
            or data["installer_extract_step"] is None
        ):

            if self.data is None:
                _LOGGER.warning("No coordinator data available.")
                return

            data["installer_supply_step"] = self.data["basic_supply_step"]
            data["installer_extract_step"] = self.data["basic_extract_step"]

            await self.storage.save(data)

            _LOGGER.info(
                "Installer settings saved: Supply=%s Extract=%s",
                data["installer_supply_step"],
                data["installer_extract_step"],
            )


    async def restore_installer_settings(self):
        """Restore installer airflow settings."""

        data = await self.storage.load()

        await self.set_basic_supply(data["installer_supply_step"])
        await self.set_basic_extract(data["installer_extract_step"])


    async def get_installer_settings(self):
        """Return stored installer settings."""

        return await self.storage.load()