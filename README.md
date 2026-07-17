# Danfoss Air CCM for Home Assistant

Native Home Assistant integration for **Danfoss Air CCM** ventilation units using the original Danfoss TCP protocol.

> ⚠️ This project is currently under active development.

<p align="center">
  <img src="screenshots/logo.png" width="220">
</p>

---

# Features

- 🚀 Native Danfoss TCP protocol
- 🏠 100% Local communication
- 🔧 Native Home Assistant entities
- ⚡ No cloud
- 🔌 No Modbus
- 🤖 No Node-RED
- 🔍 Reverse engineered from the official Danfoss PC Tool

---

# Status

**Current version:** `0.4.1`

| Component | Status |
|-----------|--------|
| Home Assistant | ✅ |
| Config Flow | ✅ |
| Native TCP | ✅ |
| HACS | 🚧 |
| Fan Control | ✅ |
| Fan RPM | ✅ |
| Temperatures | ✅ |
| Relative Humidity | ✅ |
| Boost | ✅ |
| Run Mode | ✅ |
| Bypass | ✅ |
| Diagnostics | ✅ |
| Scheduler | 🚧 |

---

# Supported Features

| Feature | Status |
|----------|:------:|
| Fan Step Control | ✅ |
| Current Supply Step | ✅ |
| Current Extract Step | ✅ |
| Supply Fan Speed (RPM) | ✅ |
| Extract Fan Speed (RPM) | ✅ |
| Run Mode | ✅ |
| Basic Supply Step | ✅ |
| Basic Extract Step | ✅ |
| Boost | ✅ |
| Boost Duration | ✅ |
| Maximum Boost Step | ✅ |
| Auto Boost | ✅ |
| Bypass | ✅ |
| Bypass Active | ✅ |
| Outdoor Temperature | ✅ |
| Supply Temperature | ✅ |
| Extract Temperature | ✅ |
| Exhaust Temperature | ✅ |
| Relative Humidity | ✅ |
| Alarm Code | ✅ |
| Alarm Description | ✅ |
| Filter Fouling | ✅ |
| Filter Reset | ✅ |
| Installer Mode | ✅ |

---

# Supported Devices

Verified on:

- Danfoss Air CCM
- Danfoss W1A2

Additional Danfoss Air models will be tested in future releases.

---

# Installation

## HACS

HACS support is currently under development.

Until then install manually.

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

Add the integration from:

**Settings → Devices & Services → Add Integration**

---

# Supported Parameters

| Address | Parameter | Type | Read | Write |
|--------:|-----------|------|:----:|:-----:|
| 1008 | Alarm Code | WORD | ✅ | ❌ |
| 5138 | Run Mode | BYTE | ✅ | ✅ |
| 5160 | Current Supply Step | BYTE | ✅ | ❌ |
| 5161 | Current Extract Step | BYTE | ✅ | ❌ |
| 5184 | Basic Supply Step | BYTE | ✅ | ✅ |
| 5185 | Basic Extract Step | BYTE | ✅ | ✅ |
| 5200 | Supply Fan Speed | WORD | ✅ | ❌ |
| 5201 | Extract Fan Speed | WORD | ✅ | ❌ |
| 5216 | Bypass | BOOL | ✅ | ✅ |
| 5223 | Bypass Active | BOOL | ✅ | ❌ |
| 5226 | Filter Fouling | BYTE | ✅ | ❌ |
| 5231 | Filter Reset | BOOL | ❌ | ✅ |
| 5232 | Relative Humidity | BYTE | ✅ | ❌ |
| 5234 | Outdoor Temperature | SHORT | ✅ | ❌ |
| 5235 | Supply Temperature | SHORT | ✅ | ❌ |
| 5236 | Extract Temperature | SHORT | ✅ | ❌ |
| 5237 | Exhaust Temperature | SHORT | ✅ | ❌ |
| 5424 | Boost | BOOL | ✅ | ✅ |
| 5425 | Boost Timer | BYTE | ✅ | ✅ |
| 5536 | Program Number | BYTE | ✅ | ✅ |
| 5890 | Auto Boost | BOOL | ✅ | ✅ |
| 5891 | Maximum Boost Step | BYTE | ✅ | ✅ |
| 6017 | Fan Step | BYTE | ✅ | ✅ |

> **Note**
>
> Supply Fan Speed (5200) and Extract Fan Speed (5201) are available through **endpoint 4** of the native Danfoss TCP protocol.

More parameters are continuously being reverse engineered and added.

---

# Home Assistant Entities

## Sensors

- Fan Step
- Current Supply Step
- Current Extract Step
- Supply Fan Speed
- Extract Fan Speed
- Outdoor Temperature
- Supply Temperature
- Extract Temperature
- Exhaust Temperature
- Relative Humidity
- Alarm Code
- Alarm Description
- Filter Fouling
- Bypass Active

## Numbers

- Fan Step
- Basic Supply Step
- Basic Extract Step
- Boost Duration
- Maximum Boost Step

## Switches

- Bypass
- Boost
- Auto Boost

## Selects

- Run Mode

## Buttons

- Restore Installer Settings
- Reset Filter

---

# Reverse Engineering

This integration communicates directly with the Danfoss controller using the original Danfoss TCP protocol on **port 30046**.

The implementation has been verified against:

- Official Danfoss PC Tool
- Original Danfoss HRV .NET source code
- Wireshark packet captures
- Live testing on Danfoss Air CCM
- Live testing on Danfoss W1A2

No Modbus protocol is used.

---

# Design Goals

- Native TCP communication
- Local communication only
- No cloud
- No Modbus
- No Node-RED
- No external dependencies

---

# Roadmap

## Version 0.5.0

- Bypass Timer
- Bypass Outdoor Temperature
- Bypass Room Temperature
- Auto Bypass
- Defrost Status
- Away Mode (Switch)

## Version 0.6.0

- Weekly Scheduler
- Weekly Profiles
- Time Programs
- Operating Modes

## Version 1.0.0

- Full protocol support
- Automatic device discovery
- HACS release
- Complete diagnostics
- Translation support
- Stable release

---

# Project Structure

```text
custom_components/
└── danfoss_air_ccm/
    ├── __init__.py
    ├── alarms.py
    ├── button.py
    ├── config_flow.py
    ├── const.py
    ├── coordinator.py
    ├── entity.py
    ├── number.py
    ├── protocol.py
    ├── select.py
    ├── sensor.py
    ├── storage.py
    └── switch.py
```

---

# Documentation

- 📄 README.md
- 📄 PARAMETERS.md
- 📄 PROTOCOL.md
- 📄 ROADMAP.md
- 📄 CHANGELOG.md

---

# Screenshots

Screenshots are available in the `screenshots` directory.

---

# Contributing

Bug reports, feature requests and pull requests are welcome.

If you own another Danfoss Air controller or discover additional parameters, contributions are highly appreciated.

---

# License

This project is licensed under the MIT License.