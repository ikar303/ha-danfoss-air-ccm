# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog.

---

## [Unreleased]

### Added

- Boost support
- Boost Timer
- Boost Maximum Step
- Auto Boost

### Changed

### Fixed


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

- Removed invalid Supply Fan Speed parameter (5200)
- Removed invalid Extract Fan Speed parameter (5201)
- Relative Humidity conversion using the original Danfoss algorithm (`value × 100 / 255`)

---

## [0.1.0] - 2026-07

### Added

- Initial release
- Native TCP communication
- Config Flow
- Fan Step sensor
- Fan Step control