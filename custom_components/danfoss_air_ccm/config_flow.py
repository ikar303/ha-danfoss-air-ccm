from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST

from .const import DOMAIN
from .protocol import DanfossClient


class DanfossAirConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Danfoss Air CCM config flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:

            client = DanfossClient(user_input[CONF_HOST])

            try:
                await self.hass.async_add_executor_job(
                    client.get_fan_step,
                )

            except Exception:
                errors["base"] = "cannot_connect"

            finally:
                client.disconnect()

            if not errors:
                return self.async_create_entry(
                    title=user_input[CONF_HOST],
                    data=user_input,
                )

        schema = vol.Schema(
            {
                vol.Required(CONF_HOST): str,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )