# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog.

---

## [0.3.0] - 2026-07

### Added

- Native Bypass switch (read/write)
- Native SwitchEntity support
- Basic Supply Step control
- Basic Extract Step control
- Installer Mode
- Persistent installer settings storage
- Restore Installer Settings button
- Configuration entities for installer airflow settings

### Changed

- Improved entity naming (`Current` / `Basic`)
- Added native Home Assistant icons
- Added Home Assistant Device Classes
- Added Home Assistant State Classes
- Improved entity organization (Controls / Sensors / Configuration)
- Reduced polling interval to 30 seconds

### Fixed

- Relative Humidity conversion using the original Danfoss algorithm (`value × 100 / 255`)
- Preserved installer airflow settings across Home Assistant restarts

---

## [0.2.0] - 2026-07

### Added

- Fan Step control (1–10)
- Supply Step control (0–100)
- Extract Step control (0–100)
- Outdoor Temperature sensor
- Supply Temperature sensor
- Extract Temperature sensor
- Exhaust Temperature sensor
- Relative Humidity sensor

### Changed

- Improved coordinator structure
- Improved TCP protocol implementation
- Renamed entities for consistency

### Fixed

- Removed invalid Supply Fan Speed parameter (5200)
- Removed invalid Extract Fan Speed parameter (5201)
- Correct Relative Humidity conversion using the original Danfoss algorithm (`value × 100 / 255`)

---

## [0.1.0] - 2026-07

### Added

- Initial project
- Native TCP client
- Config Flow
- Fan Step read support
- Fan Step write support
- Fan Step sensor
- Fan Step number entity