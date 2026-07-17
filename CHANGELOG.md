# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog.

---

## [0.4.1] - 2026-07

### Added

- Supply Fan Speed sensor (RPM)
- Extract Fan Speed sensor (RPM)
- Native fan speed reading using endpoint 4
- Connection validation during Config Flow setup

### Changed

- Updated PARAMETERS.md
- Updated PROTOCOL.md
- Updated README
- Updated ROADMAP
- Improved parameter documentation

### Fixed

- Correct endpoint handling for RPM parameters
- Improved sensor naming consistency
- Removed obsolete Resultant Fan Step entity

---

## [0.4.0] - 2026-07

### Added

- Boost switch
- Boost Duration control
- Maximum Boost Step control
- Auto Boost switch
- Native Run Mode Select entity (Demand / Program / Manual)
- Alarm Code diagnostic sensor
- Alarm Description diagnostic sensor
- Filter Fouling diagnostic sensor
- Filter Reset button
- Bypass Active sensor
- Native alarm database (`alarms.py`)
- PARAMETERS.md documentation
- PROTOCOL.md documentation
- ROADMAP.md documentation

### Changed

- Boost Duration limited to 24 hours
- Boost configuration is automatically written before enabling Boost
- Renamed temperature parameter identifiers for improved readability
- Improved protocol documentation
- Expanded parameter documentation
- Updated README
- Updated project roadmap

### Fixed

- Correct Boost activation sequence
- Correct Auto Boost inverted logic (`0 = enabled`, `1 = disabled`)
- Correct Current Supply Step sensor
- Correct Current Extract Step sensor
- Improved Run Mode handling

---

## [0.3.0] - 2026-07

### Added

- Native Bypass switch (read/write)
- Native `SwitchEntity` support
- Basic Supply Step configuration
- Basic Extract Step configuration
- Installer Mode
- Persistent installer settings storage
- Restore Installer Settings button
- Configuration entities for installer airflow settings

### Changed

- Improved entity naming (`Basic` / `Current`)
- Added Home Assistant Device Classes
- Added Home Assistant State Classes
- Added native Material Design Icons
- Improved entity organization (Controls / Sensors / Configuration)
- Reduced polling interval to 30 seconds
- Improved installer settings handling

### Fixed

- Relative Humidity conversion using the original Danfoss algorithm (`value × 100 / 255`)
- Preserved installer airflow settings across Home Assistant restarts
- Improved configuration entity consistency

---

## [0.2.0] - 2026-07

### Added

- Fan Step control (1–10)
- Outdoor Temperature sensor
- Supply Temperature sensor
- Extract Temperature sensor
- Exhaust Temperature sensor
- Relative Humidity sensor
- Basic Supply Step configuration
- Basic Extract Step configuration

### Changed

- Improved coordinator structure
- Improved TCP protocol implementation
- Improved entity naming consistency

### Fixed

- Relative Humidity conversion using the original Danfoss algorithm (`value × 100 / 255`)

---

## [0.1.0] - 2026-07

### Added

- Initial release
- Native TCP communication
- Config Flow
- Fan Step sensor
- Fan Step control