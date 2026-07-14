# Danfoss Air CCM Parameters

This document contains all known parameters discovered during reverse engineering of the native Danfoss Air CCM TCP protocol.

> Native TCP protocol (Port **30046**)

---

# Supported Devices

Verified on:

- Danfoss Air CCM
- Danfoss W1A2

---

# Statistics

| Item | Count |
|------|------:|
| Parameters discovered | 27 |
| Parameters implemented | 18 |
| Sensors | 11 |
| Controls | 5 |
| Configuration entities | 5 |
| Diagnostic entities | 3 |

---

## Status Legend

- ✅ Implemented
- 🚧 Verified, implementation pending
- 🔍 Under investigation
- ❌ Invalid / Unsupported

---

## Data Type Conversions

| Type | Conversion |
|------|------------|
| BYTE | value |
| SHORT | value / 100 |
| PERCENT | value × 100 / 255 |
| BOOL | 0 / 1 |
| WORD | 16-bit unsigned |

---

# Implemented Parameters

| Address | Name | Entity | Type | Read | Write | Status | Notes |
|--------:|------|--------|------|:----:|:-----:|:------:|-------|
| 769 | Bypass Room Temperature | — | SHORT | ✅ | ✅ | 🚧 | Room temperature threshold |
| 1008 | Alarm Code | Sensor | WORD | ✅ | ❌ | ✅ | Current alarm code |
| 5138 | Run Mode | Select | BYTE | ✅ | ✅ | ✅ | Demand / Program / Manual |
| 5160 | Current Supply Step | Sensor | BYTE | ✅ | ❌ | ✅ | Current supply airflow (%) |
| 5161 | Current Extract Step | Sensor | BYTE | ✅ | ❌ | ✅ | Current extract airflow (%) |
| 5184 | Basic Supply Step | Number | BYTE | ✅ | ✅ | ✅ | Installer airflow percentage |
| 5185 | Basic Extract Step | Number | BYTE | ✅ | ✅ | ✅ | Installer airflow percentage |
| 5216 | Bypass | Switch | BOOL | ✅ | ✅ | ✅ | Manual bypass |
| 5223 | Bypass Active | Sensor | BOOL | ✅ | ❌ | ✅ | Current bypass state |
| 5232 | Relative Humidity | Sensor | PERCENT | ✅ | ❌ | ✅ | value × 100 / 255 |
| 5234 | Outdoor Temperature | Sensor | SHORT | ✅ | ❌ | ✅ | Outdoor air |
| 5235 | Supply Temperature | Sensor | SHORT | ✅ | ❌ | ✅ | Supply air |
| 5236 | Extract Temperature | Sensor | SHORT | ✅ | ❌ | ✅ | Extract air |
| 5237 | Exhaust Temperature | Sensor | SHORT | ✅ | ❌ | ✅ | Exhaust air |
| 5424 | Boost | Switch | BOOL | ✅ | ✅ | ✅ | Manual Boost |
| 5425 | Boost Duration | Number | BYTE | ✅ | ✅ | ✅ | Boost duration (hours) |
| 5890 | Boost Auto | Switch | BOOL | ✅ | ✅ | ✅ | Automatic Boost |
| 5891 | Boost Max Step | Number | BYTE | ✅ | ✅ | ✅ | Maximum Boost step |
| 6017 | Fan Step | Number + Sensor | BYTE | ✅ | ✅ | ✅ | Main ventilation step |

---

# Verified Parameters

| Address | Name | Type | Read | Write | Status | Notes |
|--------:|------|------|:----:|:-----:|:------:|-------|
| 5218 | Bypass Timer | BYTE | ✅ | ✅ | 🚧 | Bypass duration |
| 5219 | Bypass Outdoor Temperature | SHORT | ✅ | ✅ | 🚧 | Outdoor threshold |
| 5226 | Filter Fouling | PERCENT | ✅ | ❌ | 🚧 | Filter wear |
| 5231 | Filter Reset | BOOL | ❌ | ✅ | 🚧 | Reset counter |
| 5894 | Bypass Auto Enabled | BOOL | ✅ | ✅ | 🚧 | Automatic bypass |
| 6016 | Fan Step Setpoint | BYTE | ✅ | ✅ | 🚧 | Requested fan step |
| 6019 | Resultant Fan Step | BYTE | ✅ | ❌ | 🚧 | Effective fan step |

---

# Invalid Parameters

| Address | Name | Reason |
|--------:|------|--------|
| 5200 | Actual Supply Fan Speed | Always returns 0 |
| 5201 | Actual Extract Fan Speed | Always returns 0 |

---

# Home Assistant Support

## Sensors

- ✅ Fan Step
- ✅ Current Supply Step
- ✅ Current Extract Step
- ✅ Outdoor Temperature
- ✅ Supply Temperature
- ✅ Extract Temperature
- ✅ Exhaust Temperature
- ✅ Relative Humidity
- ✅ Alarm Code
- ✅ Alarm Description
- ✅ Bypass Active

---

## Numbers

- ✅ Fan Step
- ✅ Basic Supply Step
- ✅ Basic Extract Step
- ✅ Boost Duration
- ✅ Boost Max Step

---

## Switches

- ✅ Boost
- ✅ Boost Auto
- ✅ Bypass

---

## Select

- ✅ Run Mode

---

## Buttons

- ✅ Restore Installer Settings

---

## Diagnostics

- ✅ Alarm Code
- ✅ Alarm Description
- ✅ Bypass Active
- 🚧 Filter Fouling
- 🚧 Filter Reset
- 🚧 Resultant Fan Step

---

# Discovery Log

| Date | Description |
|------|-------------|
| 2026-07 | Native TCP protocol reverse engineered |
| 2026-07 | Fan Step read/write implemented |
| 2026-07 | Current Supply / Extract Step implemented |
| 2026-07 | Basic Supply / Extract Step implemented |
| 2026-07 | Outdoor, Supply, Extract and Exhaust temperature sensors implemented |
| 2026-07 | Relative Humidity implemented |
| 2026-07 | Native Bypass switch implemented |
| 2026-07 | Boost implemented |
| 2026-07 | Boost Auto implemented |
| 2026-07 | Boost Duration implemented |
| 2026-07 | Boost Max Step implemented |
| 2026-07 | Run Mode implemented |
| 2026-07 | Alarm Code implemented |
| 2026-07 | Alarm Description implemented |
| 2026-07 | Bypass Active implemented |
| 2026-07 | Installer Mode implemented |
| 2026-07 | Persistent installer settings implemented |
| 2026-07 | Restore Installer Settings button implemented |
| 2026-07 | Native TCP protocol fully replaces Modbus |
| 2026-07 | Home Assistant Device Classes added |
| 2026-07 | Home Assistant State Classes added |
| 2026-07 | Material Design Icons added |