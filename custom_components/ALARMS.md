# Danfoss Air CCM Alarms

This document describes all known alarm codes discovered during reverse engineering of the Danfoss Air CCM native TCP protocol.

> Alarm parameter: **1008**

---

# Alarm Types

The Danfoss controller returns a numeric alarm code.

Some alarms also have sub-codes which provide more detailed information.

Example:

```
128
```

means

```
Sensor error
```

while

```
128.4
```

means

```
T2 sensor open circuit
```

---

# Alarm Codes

| Code | Name | Description |
|------:|------|-------------|
| 0 | No active alarm | System operating normally |
| 1 | Fan error | Fan related fault |
| 2 | Filter error | Replace air filters |
| 3 | Fire | Fire protection activated |
| 4 | Outdoor temperature too low | Outdoor temperature below operating limit |
| 5 | Heating surface error | Heating device error |
| 32 | Supply air temperature too cold | Supply temperature below minimum |
| 64 | Configuration | Configuration information |
| 128 | Sensor error | Temperature or humidity sensor fault |
| 129 | Room temperature too low | Room temperature below minimum |
| 130 | Communication error | Communication failure |

---

# Alarm Details

## Alarm 1 — Fan error

| Subcode | Description |
|---------:|-------------|
| 1 | Supply fan blocked |
| 5 | Extract fan blocked |
| 16 | Fan operating range error |

Recommended action:

- Restart the unit.
- Check both fans.
- Verify wiring.

---

## Alarm 2 — Filter error

Replace both filters.

After replacement reset the filter counter.

---

## Alarm 3 — Fire

One or more temperature sensors exceeded the fire protection threshold.

Recommended action:

- Inspect the ventilation system.
- Verify temperature sensors.
- Restart the unit after the cause has been removed.

---

## Alarm 4 — Outdoor temperature too low

Outdoor temperature is below the permitted operating range.

---

## Alarm 5 — Heating surface error

| Subcode | Description |
|---------:|-------------|
| 1 | Electric pre-heater overheated |
| 2 | Electric after-heater overheated |
| 8 | Water heater frost protection |
| 9 | Critical heater alarm |

Recommended action:

- Inspect the heater.
- Verify airflow.
- Restart the unit.

---

## Alarm 32 — Supply air temperature too cold

Supply air temperature is below the configured minimum.

Recommended action:

- Restart the HRV unit.
- Check heating equipment.

---

## Alarm 64 — Configuration

These are **not faults**.

The controller reports detected hardware during configuration.

| Subcode | Description |
|---------:|-------------|
| 1 | Geothermal heat exchanger detected |
| 8 | Electric pre-heater detected |
| 16 | Electric after-heater detected |
| 17 | Supply temperature control enabled |
| 32 | Water after-heater detected |
| 33 | Water heater control mode |
| 34 | Water heater comfort temperature |

---

## Alarm 128 — Sensor error

| Subcode | Description |
|---------:|-------------|
| 1 | T1 sensor short circuit |
| 2 | T1 sensor open circuit |
| 3 | T2 sensor short circuit |
| 4 | T2 sensor open circuit |
| 5 | T3 sensor short circuit |
| 6 | T3 sensor open circuit |
| 7 | T4 sensor short circuit |
| 8 | T4 sensor open circuit |
| 20 | Relative humidity sensor defect |

Recommended action:

- Check sensor wiring.
- Replace defective sensor.
- Restart the unit.

---

## Alarm 129 — Room temperature too low

Room temperature has dropped below the configured limit.

Recommended action:

- Restart the HRV unit.
- Check the central heating system.

---

## Alarm 130 — Communication error

| Subcode | Description |
|---------:|-------------|
| 1 | HRV unit (Modbus) |
| 2 | Electric pre-heater (Modbus) |
| 3 | Geothermal heat exchanger |
| 4 | Electric after-heater |
| 5 | Water after-heater |
| 16 | Wireless control panel (MMI) |

Recommended action:

- Check communication wiring.
- Verify connected accessories.
- Restart the unit.

---

# Home Assistant

The integration exposes:

- Alarm Code
- Alarm Description

Future releases will include:

- Alarm Details
- Alarm History
- Alarm Log
- Alarm Severity
- Last Alarm Timestamp

---

# Reverse Engineering Notes

The alarm table was reconstructed by analysing:

- Danfoss HRV Driver
- Danfoss PC Tool
- Danfoss resource strings
- Native TCP protocol

The official protocol documentation is not publicly available.