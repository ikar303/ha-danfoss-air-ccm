# Danfoss Air CCM for Home Assistant

Native Home Assistant integration for **Danfoss Air CCM** ventilation units using the original Danfoss TCP protocol.

> ⚠️ This project is currently under active development.

---

# Status

**Current version:** `0.3.0-beta`

| Component | Status |
|-----------|--------|
| Home Assistant | ✅ |
| Config Flow | ✅ |
| Native TCP | ✅ |
| HACS | 🚧 |
| Fan Control | ✅ |
| Temperatures | ✅ |
| Relative Humidity | ✅ |
| Bypass | ✅ |
| Installer Mode | ✅ |
| Scheduler | 🚧 |

---

# Features

- ✅ Native TCP communication (Port **30046**)
- ✅ Local communication only
- ✅ No cloud
- ✅ No Modbus
- ✅ No Node-RED
- ✅ Config Flow
- ✅ Local polling
- ✅ Fan Step control (1–10)
- ✅ Basic Supply Step control
- ✅ Basic Extract Step control
- ✅ Native Bypass switch
- ✅ Installer Mode
- ✅ Persistent installer airflow settings
- ✅ Restore Installer Settings
- ✅ Outdoor Temperature
- ✅ Supply Temperature
- ✅ Extract Temperature
- ✅ Exhaust Temperature
- ✅ Relative Humidity

---

# Supported Devices

Tested with:

- Danfoss Air CCM
- Danfoss W1A2

Additional Danfoss Air models will be tested in future releases.

---

# Installation

## HACS

Coming soon.

## Manual Installation

Copy

```text
custom_components/danfoss_air_ccm
```

to

```text
/config/custom_components/
```

Restart Home Assistant.

---

# Supported Parameters

| Address | Parameter | Read | Write |
|--------:|-----------|:----:|:-----:|
| 5160 | Current Supply Step | ✅ | ❌ |
| 5161 | Current Extract Step | ✅ | ❌ |
| 5184 | Basic Supply Step | ✅ | ✅ |
| 5185 | Basic Extract Step | ✅ | ✅ |
| 5216 | Bypass | ✅ | ✅ |
| 5232 | Relative Humidity | ✅ | ❌ |
| 5234 | Outdoor Temperature | ✅ | ❌ |
| 5235 | Supply Temperature | ✅ | ❌ |
| 5236 | Extract Temperature | ✅ | ❌ |
| 5237 | Exhaust Temperature | ✅ | ❌ |
| 6017 | Fan Step | ✅ | ✅ |

More parameters are continuously being reverse engineered and added.

---

# Home Assistant Entities

## Sensors

- Fan Step
- Current Supply Step
- Current Extract Step
- Outdoor Temperature
- Supply Temperature
- Extract Temperature
- Exhaust Temperature
- Relative Humidity

## Controls

- Fan Step
- Bypass

## Configuration

- Basic Supply Step
- Basic Extract Step
- Restore Installer Settings

---

# Roadmap

## Version 0.4

- Alarm Code
- Filter Fouling
- Filter Reset
- Bypass Active

## Version 0.5

- Boost
- Maximum Boost Step
- Resultant Fan Step
- Night Cooling

## Version 0.6

- Bypass Timer
- Bypass Outdoor Temperature
- Bypass Room Temperature
- Auto Bypass

## Version 0.7

- Weekly Scheduler
- Weekly Profiles
- Operating Modes

---

# Development

This integration communicates directly with the Danfoss controller using the original Danfoss TCP protocol on **port 30046**.

The protocol has been reverse engineered from the official Danfoss PC Tool.

Features:

- Native TCP protocol
- Local communication
- No cloud
- No Modbus
- No Node-RED
- No external dependencies

---

# Project Structure

```text
custom_components/
└── danfoss_air_ccm/
    ├── __init__.py
    ├── button.py
    ├── config_flow.py
    ├── const.py
    ├── coordinator.py
    ├── entity.py
    ├── number.py
    ├── protocol.py
    ├── sensor.py
    ├── storage.py
    └── switch.py
```

---

# Documentation

- PARAMETERS.md
- CHANGELOG.md
- ROADMAP.md

---

# Screenshots

Screenshots are available in the `screenshots` directory.

---

# Contributing

Bug reports, feature requests and pull requests are welcome.

---

# License

MIT