"""Danfoss Air coordinator."""

from __future__ import annotations

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

        super().__init__(
            hass,
            _LOGGER,
            name="Danfoss Air CCM",
            update_interval=timedelta(seconds=5),
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
        }

    async def set_fan_step(self, value):

        await self.hass.async_add_executor_job(
            self.client.set_fan_step,
            value,
        )

        await self.async_request_refresh()