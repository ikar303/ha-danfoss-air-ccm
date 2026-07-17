# Danfoss Air CCM Parameters

This document contains all currently known Danfoss Air CCM parameters discovered through reverse engineering of the native TCP protocol and analysis of the official Danfoss PC Tool.

> Native TCP Protocol (TCP Port **30046**)

---

# Status Legend

| Status | Meaning |
|---------|---------|
| ✅ Implemented | Fully implemented in Home Assistant |
| ✔ Verified | Confirmed in official Danfoss driver |
| 🧪 To Verify | Present in official driver, not yet tested |
| ❓ Unknown | Purpose still under investigation |

---

# Native Data Types

| Type | Encoding |
|------|----------|
| BOOL | 0 / 1 |
| BYTE | Unsigned 8-bit |
| WORD | Unsigned 16-bit |
| SHORT | Signed 16-bit (value / 100) |
| PERCENT | value × 100 / 255 |
| DATETIME | Second, Minute, Hour, DayOfWeek+Day, Month, Year-2000 |
| BYTEFIELD | Variable length byte array |

---

# Implemented Parameters

| EP | Address | Name | Type | R | W | Status | Notes |
|---:|-------:|------|------|:-:|:-:|:------:|------|
|1|1008|Alarm Code|WORD|✅|❌|✅|Current alarm|
|1|5138|Run Mode|BYTE|✅|✅|✅|Demand / Program / Manual|
|1|5160|Current Supply Step|BYTE|✅|❌|✅|Current supply airflow|
|1|5161|Current Extract Step|BYTE|✅|❌|✅|Current extract airflow|
|1|5184|Basic Supply Step|BYTE|✅|✅|✅|Installer setting|
|1|5185|Basic Extract Step|BYTE|✅|✅|✅|Installer setting|
|4|5200|Supply Fan Speed|WORD|✅|❌|✅|Actual RPM|
|4|5201|Extract Fan Speed|WORD|✅|❌|✅|Actual RPM|
|1|5216|Bypass|BOOL|✅|✅|✅|Manual bypass|
|1|5223|Bypass Active|BOOL|✅|❌|✅|Current state|
|1|5226|Filter Fouling|PERCENT|✅|❌|✅|value ×100 / 255|
|1|5231|Filter Reset|BOOL|❌|✅|✅|Reset filter counter|
|1|5232|Relative Humidity|PERCENT|✅|❌|✅|value ×100 / 255|
|1|5234|Outdoor Temperature|SHORT|✅|❌|✅|Outdoor air|
|4|5235|Supply Temperature|SHORT|✅|❌|✅|Supply air|
|4|5236|Extract Temperature|SHORT|✅|❌|✅|Extract air|
|4|5237|Exhaust Temperature|SHORT|✅|❌|✅|Exhaust air|
|1|5424|Boost|BOOL|✅|✅|✅|Boost switch|
|1|5425|Boost Timer|BYTE|✅|✅|✅|Hours|
|1|5536|Program Number|BYTE|✅|✅|✅|Program mode|
|1|5890|Boost Auto|BOOL|✅|✅|✅|Inverted logic|
|1|5891|Boost Max Step|BYTE|✅|✅|✅|Stored ×10|
|1|6017|Fan Step|BYTE|✅|✅|✅|Main fan step|

---

# Verified Parameters

| EP | Address | Name | Type | R | W | Status | Notes |
|---:|-------:|------|------|:-:|:-:|:------:|------|
|0|820|Outdoor Temperature|SHORT|✔|❌|✔|Used by official Danfoss PC Tool|
|1|5218|Bypass Timer|BYTE|✔|✔|✔|Hours|
|1|5219|Bypass Outdoor Temperature|SHORT|✔|✔|✔|°C|
|1|5408|Away End Time|DATETIME|✔|✔|✔|Away schedule|
|1|5409|Away Start Time|DATETIME|✔|✔|✔|Away schedule|
|1|5410|Away Active|BOOL|✔|❌|✔|Current Away status|
|1|5411|Away Scheduled|BOOL|✔|❌|✔|Away active or planned|
|1|5489|Night Cooling|BOOL|✔|✔|✔|Night cooling|
|1|5617|Defrost Active|BOOL|✔|❌|✔|Defrost status|
|1|5894|Auto Bypass|BOOL|✔|✔|✔|Inverted logic|
|1|6016|Fan Step Setpoint|BYTE|✔|✔|✔|Requested step|
|1|6019|Resultant Fan Step|BYTE|✔|❌|✔|Calculated by controller|

---

# Monitoring Parameters

| EP | Address | Name | Type | Status |
|---:|-------:|------|------|--------|
|0|992|Total Running Time|DWORD|🧪|
|1|5429|Cooking Hood Active|BOOL|🧪|
|1|5456|Heating Surface Installed|BYTE|🧪|
|1|5457|Heating Surface Active|BYTE|🧪|
|1|5895|Fireplace Mode|BOOL|🧪|

---

# Scheduler

| EP | Address | Name | Type | Status |
|---:|-------:|------|------|--------|
|6|5888|Weekday Profile|BYTEFIELD|🧪|
|6|5889|Weekend Profile|BYTEFIELD|🧪|

---

# Alarm Log

| EP | Address | Name | Type | Status |
|---:|-------:|------|------|--------|
|6|5984-5993|Alarm Log Entries|BYTEFIELD|🧪|

---

# Heating Surface Enrollment

| EP | Address | Name | Type | Status |
|---:|-------:|------|------|--------|
|1|1009|Enrollment ACK|WORD|🧪|
|6|5906|Geothermal Enrollment|BYTE|🧪|
|6|5910|Electric Preheater Enrollment|BYTE|🧪|
|6|5911|Electric Afterheater Enrollment|BYTE|🧪|
|6|5912|Water Afterheater Enrollment|BYTE|🧪|

---

# Z-Wave

| EP | Address | Name | Type | Status |
|---:|-------:|------|------|--------|
|6|5952|Z-Wave Command|BYTE|🧪|

---

# Calculated Values

| Name | Formula |
|------|---------|
|Current Fan Step|`max(1, round(Current Extract Step / 10))`|
|Humidity|`value × 100 / 255`|
|Filter Fouling|`value × 100 / 255`|
|Boost Max Step|`value / 10`|
|Running Hours|`parameter 992 / 60`|

---

# Endpoint Usage

Unlike Modbus, the native Danfoss protocol stores parameters on multiple endpoints.

| Endpoint | Usage |
|----------|-------|
|0|System information / runtime counters|
|1|Configuration and operating status|
|4|Live temperatures and actual fan speeds (RPM)|
|6|Arrays, scheduler, alarm log and Z-Wave|

---

# Known Firmware Behaviour

- Boost Auto uses inverted logic (`0 = enabled`, `1 = disabled`)
- Auto Bypass uses inverted logic
- Boost Max Step is stored multiplied by 10
- Humidity uses `value × 100 / 255`
- Filter Fouling uses `value × 100 / 255`
- Current Fan Step is calculated from Current Extract Step
- Supply Fan Speed and Extract Fan Speed are available only through endpoint **4**
- Official Danfoss PC Tool reads Outdoor Temperature from endpoint **0** (parameter **820**)
- Home Assistant integration reads Outdoor Temperature from endpoint **1** (parameter **5234**)
- Away mode is controlled by writing **Away Start Time** and **Away End Time**
- DATETIME values are encoded as:
  - Second
  - Minute
  - Hour
  - DayOfWeek + Day
  - Month
  - Year - 2000

---

# Statistics

| Item | Count |
|------|------:|
|Implemented parameters|22|
|Verified parameters|34+|
|Known endpoints|4|
|Supported sensors|17|
|Supported controls|10|
|Documented protocol parameters|45+|