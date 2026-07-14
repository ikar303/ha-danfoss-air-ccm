"""Danfoss Air CCM TCP client."""

from __future__ import annotations

import socket
import logging
from time import time

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
    PARAM_BYPASS,
    PARAM_BOOST,
    PARAM_BOOST_TIMER,
    PARAM_BOOST_AUTO,
    PARAM_BOOST_MAX_STEP,
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
    
    def get_parameter_bool(self, parameter):
        return self.get_parameter_byte(parameter) != 0

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
        value = self.get_parameter_byte(PARAM_HUMIDITY)

        if value <= 0:
            return None

        return round(value * 100.0 / 255.0, 1)
    
   
    def set_basic_supply(self, value: int):
        self.write_parameter(PARAM_BASIC_SUPPLY, value)
        return self.get_basic_supply()


    def set_basic_extract(self, value: int):
        self.write_parameter(PARAM_BASIC_EXTRACT, value)
        return self.get_basic_extract()
    

    def get_bypass(self):
        return self.get_parameter_bool(PARAM_BYPASS)


    def set_bypass(self, enabled: bool):
        self.write_parameter(PARAM_BYPASS, 1 if enabled else 0)
        return self.get_bypass()
    
    #
    # Boost
    #

    def get_boost(self):
        return self.get_parameter_bool(PARAM_BOOST)

    def write_boost_settings(self):
        """Write all Boost configuration parameters."""

        self.write_parameter(
            PARAM_BOOST_MAX_STEP,
            self.get_boost_max_step() * 10,
        )

        self.write_parameter(
            PARAM_BOOST_TIMER,
            self.get_boost_timer(),
        )

        # Danfoss uses inverted logic:
        # 0 = Auto ON
        # 1 = Auto OFF
        self.write_parameter(
            PARAM_BOOST_AUTO,
            0 if self.get_boost_auto() else 1,
        )

    def set_boost(self, enabled: bool):
        """Enable or disable Boost."""

        if enabled:
            self.write_boost_settings()

        self.write_parameter(
            PARAM_BOOST,
            1 if enabled else 0,
        )   

        import time
        time.sleep(0.1)

        return self.get_boost()

    def get_boost_timer(self):
        return self.get_parameter_byte(PARAM_BOOST_TIMER)

    def set_boost_timer(self, value: int):
        self.write_parameter(PARAM_BOOST_TIMER, value)
        return self.get_boost_timer()

    def get_boost_max_step(self):
        return self.get_parameter_byte(PARAM_BOOST_MAX_STEP) // 10

    def set_boost_max_step(self, value: int):
        self.write_parameter(PARAM_BOOST_MAX_STEP, value * 10)
        return self.get_boost_max_step()

    def get_boost_auto(self):
        return not self.get_parameter_bool(PARAM_BOOST_AUTO)

    def set_boost_auto(self, enabled: bool):
        self.write_parameter(PARAM_BOOST_AUTO, 0 if enabled else 1)
        return self.get_boost_auto()