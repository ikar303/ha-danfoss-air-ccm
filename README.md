# Danfoss Air CCM

Native Home Assistant integration for Danfoss Air ventilation units using the native TCP protocol.

> ⚠️ This project is currently under active development.

---

## Features

- Native TCP communication (port 30046)
- No Modbus required
- No Node-RED required
- Config Flow support
- Fan Step control (parameter 5473)
- Fan Step sensor
- Local polling

---

## Supported units

Currently tested with:

- Danfoss Air CCM
- Danfoss W1A2

More units will be added.

---

## Installation

### HACS (coming soon)

This integration will be available through HACS.

### Manual installation

Copy

custom_components/danfoss_air_ccm

to

/config/custom_components/

Restart Home Assistant.

---

## Current supported parameters

| Parameter | Description | Status |
|-----------|-------------|--------|
|5473|Fan Step|✅|
|5184|Basic Supply|🚧|
|5185|Basic Extract|🚧|
|5138|Run Mode|🚧|

---

## Roadmap

- Fan Step
- Basic Supply
- Basic Extract
- Run Mode
- Temperatures
- Filter status
- Alarms
- Bypass
- Boost mode

---

## Development

This integration uses the native Danfoss TCP protocol on port **30046**.

No cloud.

No reverse proxy.

No external dependencies.

---

## License

MIT