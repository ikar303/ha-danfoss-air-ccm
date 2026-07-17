"""Alarm descriptions for Danfoss Air CCM."""

ALARM_TEXT = {
    0: "No active alarm",

    1: "Fan error",
    2: "Filter error",
    3: "Fire",
    4: "Outdoor temperature too low",
    5: "Heating surface error",

    32: "Supply air temperature too cold",

    64: "Configuration",

    128: "Sensor error",

    129: "Room temperature too low",

    130: "Communication error",
}


ALARM_DESCRIPTION = {

    2: (
        "Replace air filters and reset the filter counter."
    ),

    3: (
        "One or more temperature sensors exceeded the fire limit."
    ),

    32: (
        "Supply air temperature below minimum threshold. Restart the unit if the problem persists."
    ),

    129: (
        "Power HRV Unit OFF and ON to restart. "
        "Check the central heating system for defects."
    ),
}


def get_alarm_text(code: int) -> str:
    """Return short alarm text."""
    return ALARM_TEXT.get(code, f"Unknown alarm ({code})")


def get_alarm_description(code: int) -> str | None:
    """Return detailed alarm description."""
    return ALARM_DESCRIPTION.get(code)