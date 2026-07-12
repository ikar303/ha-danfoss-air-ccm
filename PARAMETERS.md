# Danfoss Air CCM Parameters

This document contains all known parameters discovered during reverse engineering of the Danfoss Air CCM native TCP protocol.

> Native TCP protocol (Port **30046**)

---

# Statistics

| Item | Count |
|------|------:|
| Parameters discovered | 18 |
| Parameters implemented | 11 |
| Sensors | 8 |
| Controls | 4 |
| Configuration entities | 3 |
| Diagnostic entities | 0 |

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
| 5160 | Supply Step | Sensor | BYTE | ✅ | ❌ | ✅ | Current supply fan step (0–100) |
| 5161 | Extract Step | Sensor | BYTE | ✅ | ❌ | ✅ | Current extract fan step (0–100) |
| 5184 | Basic Supply Step | Number | BYTE | ✅ | ✅ | ✅ | Installer airflow setting |
| 5185 | Basic Extract Step | Number | BYTE | ✅ | ✅ | ✅ | Installer airflow setting |
| 5216 | Bypass | Switch | BOOL | ✅ | ✅ | ✅ | Enable / Disable bypass |
| 5218 | Bypass Timer | — | BYTE | ✅ | ✅ | 🚧 | Minutes |
| 5219 | Bypass Outdoor Temperature | — | SHORT | ✅ | ✅ | 🚧 | Outdoor temperature threshold |
| 5232 | Relative Humidity | Sensor | PERCENT | ✅ | ❌ | ✅ | Converted using `value × 100 / 255` |
| 5234 | Outdoor Temperature | Sensor | SHORT | ✅ | ❌ | ✅ | Outdoor air temperature |
| 5235 | Supply Temperature | Sensor | SHORT | ✅ | ❌ | ✅ | Supply air temperature |
| 5236 | Extract Temperature | Sensor | SHORT | ✅ | ❌ | ✅ | Extract air temperature |
| 5237 | Exhaust Temperature | Sensor | SHORT | ✅ | ❌ | ✅ | Exhaust air temperature |
| 5894 | Bypass Auto Enabled | — | BOOL | ✅ | ✅ | 🚧 | Automatic bypass |
| 6017 | Fan Step | Number + Sensor | BYTE | ✅ | ✅ | ✅ | Main ventilation step (1–10) |

---

# Verified Parameters

| Address | Name | Type | Read | Write | Status | Notes |
|--------:|------|------|:----:|:-----:|:------:|-------|
| 1008 | Alarm Code | WORD | ✅ | ❌ | 🚧 | Alarm identifier |
| 5223 | Bypass Active | BOOL | ✅ | ❌ | 🚧 | Current bypass state |
| 5226 | Filter Fouling | PERCENT | ✅ | ❌ | 🚧 | Filter wear level |
| 5231 | Filter Reset | BOOL | ❌ | ✅ | 🚧 | Reset filter counter |
| 5424 | Boost | BOOL | ✅ | ✅ | 🚧 | Boost mode |
| 5891 | Maximum Boost Step | BYTE | ✅ | ✅ | 🚧 | Maximum boost level |
| 6016 | Fan Step Setpoint | BYTE | ✅ | ✅ | 🚧 | Requested fan step |
| 6019 | Resultant Fan Step | BYTE | ✅ | ❌ | 🚧 | Effective fan step |

---

# Invalid Parameters

| Address | Name | Reason |
|--------:|------|--------|
| 5200 | Actual Supply Fan Speed | Always returns 0 |
| 5201 | Actual Exhaust Fan Speed | Always returns 0 |

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

## Controls

- ✅ Fan Step
- ✅ Bypass

## Configuration

- ✅ Basic Supply Step
- ✅ Basic Extract Step
- ✅ Restore Installer Settings

## Diagnostics

- ⏳ Alarm Code
- ⏳ Filter Fouling
- ⏳ Filter Reset

---

# Discovery Log

| Date | Description |
|------|-------------|
| 2026-07 | Native TCP protocol reverse engineered |
| 2026-07 | Fan Step read/write implemented |
| 2026-07 | Temperature sensors implemented |
| 2026-07 | Relative Humidity implemented |
| 2026-07 | Current Supply / Extract Step implemented |
| 2026-07 | Basic Supply / Extract Step implemented |
| 2026-07 | Native Bypass switch implemented |
| 2026-07 | Installer Mode implemented |
| 2026-07 | Persistent installer settings added |
| 2026-07 | Restore Installer Settings button implemented |