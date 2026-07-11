"""Danfoss Air CCM TCP client."""

from __future__ import annotations

import socket
import logging

from .const import (
    PORT,
    ENDPOINT,
    PARAM_FAN_STEP,
    PARAM_BASIC_SUPPLY,
    PARAM_BASIC_EXTRACT,
    PARAM_RUN_MODE,
    PARAM_TEMP_01,
    PARAM_TEMP_02,
    PARAM_TEMP_03,
    PARAM_TEMP_04,
    PARAM_HUMIDITY,
    PARAM_SUPPLY_FAN_SPEED,
    PARAM_EXHAUST_FAN_SPEED,
)

_LOGGER = logging.getLogger(__name__)


class DanfossClient:
    """TCP client for Danfoss CCM."""

    def __init__(self, host: str):
        self.host = host
        self.sock = None

    def connect(self):
        """Open TCP connection."""
        if self.sock is not None:
            return

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(5)
        self.sock.connect((self.host, PORT))

        _LOGGER.info("Connected to Danfoss CCM %s:%s", self.host, PORT)

    def disconnect(self):
        """Close TCP connection."""
        if self.sock:
            self.sock.close()
            self.sock = None

    def _exchange(self, frame: bytes):

        try:

            self.connect()
            
            _LOGGER.debug("TX %s", frame.hex())

            self.sock.sendall(frame)

            data = b""

            while len(data) < 63:

                packet = self.sock.recv(63 - len(data))

                if not packet:
                    raise ConnectionError("Socket closed")

                data += packet

            _LOGGER.debug("RX %s", data.hex())

            return data

        except Exception:

            self.disconnect()
            raise
        
    def read_parameter(self, parameter: int):

        frame = bytearray(63)

        frame[0] = ENDPOINT
        frame[1] = 0x04

        frame[2] = (parameter >> 8) & 0xFF
        frame[3] = parameter & 0xFF


        return self._exchange(frame)

    def write_parameter(self, parameter: int, value: int):

        frame = bytearray(63)

        frame[0] = ENDPOINT
        frame[1] = 0x06

        frame[2] = (parameter >> 8) & 0xFF
        frame[3] = parameter & 0xFF

        frame[4] = value


        return self._exchange(frame)
    def get_temp_01(self):
        return self.get_parameter_short(PARAM_TEMP_01)

    def get_temp_02(self):
        return self.get_parameter_short(PARAM_TEMP_02)

    def get_temp_03(self):
        return self.get_parameter_short(PARAM_TEMP_03)

    def get_temp_04(self):
        return self.get_parameter_short(PARAM_TEMP_04)

    #
    # Danfoss API
    #

    def get_fan_step(self):
        return self.get_parameter_byte(PARAM_FAN_STEP)

    def set_fan_step(self, step: int):
        self.write_parameter(PARAM_FAN_STEP, step)
        return self.get_fan_step()

    def get_parameter_byte(self, parameter: int):
        data = self.read_parameter(parameter)
        return data[0]
    def get_parameter_short(self, parameter):

        data = self.read_parameter(parameter)

        value = (data[0] << 8) | data[1]

        if value >= 32768:
            value -= 65536

        return value / 100.0
    
    def get_parameter_word(self, parameter):

        data = self.read_parameter(parameter)

        return (data[0] << 8) | data[1]
        
    def get_basic_supply(self):
        return self.get_parameter_byte(PARAM_BASIC_SUPPLY)

    def get_basic_extract(self):
        return self.get_parameter_byte(PARAM_BASIC_EXTRACT)

    def get_run_mode(self):
        return self.get_parameter_byte(PARAM_RUN_MODE)
    
    def get_humidity(self):
        return self.get_parameter_byte(PARAM_HUMIDITY) - 90
    
    def get_supply_fan_speed(self):
        return self.get_parameter_word(PARAM_SUPPLY_FAN_SPEED)

    def get_exhaust_fan_speed(self):
        return self.get_parameter_word(PARAM_EXHAUST_FAN_SPEED)